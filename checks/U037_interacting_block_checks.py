"""Exact finite audits for U037; not a continuum mass-gap certificate.

Run: python checks/U037_interacting_block_checks.py --output evidence/U037_checks.json
Binary block kernels test comparison algebra, not Wilson numerical data.
Q8 tests only the boundary-gluing representation identity. The continuous SU(2)
and arbitrary-volume conclusions require the separate written proof.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
import itertools
import json
from pathlib import Path
import platform
import time
import unittest

import sympy as sp

Matrix = list[list[F]]
STATES = tuple(itertools.product((-1, 1), repeat=2))


def multiply(a: Matrix, b: Matrix) -> Matrix:
    if not a or not b or len(a[0]) != len(b):
        raise ValueError("Incompatible nonempty matrices")
    return [[sum((a[i][k] * b[k][j] for k in range(len(b))), F(0))
             for j in range(len(b[0]))] for i in range(len(a))]


def power(a: Matrix, n: int) -> Matrix:
    if n < 0 or any(len(row) != len(a) for row in a):
        raise ValueError("Square matrix and nonnegative power required")
    out = [[F(i == j) for j in range(len(a))] for i in range(len(a))]
    for _ in range(n):
        out = multiply(out, a)
    return out


def max_cross_ratio(a: Matrix) -> F:
    if not a or any(x <= 0 for row in a for x in row):
        raise ValueError("Strictly positive matrix required")
    n, m = len(a), len(a[0])
    return max(a[i][k] * a[j][l] / (a[i][l] * a[j][k])
               for i, j, k, l in itertools.product(range(n), range(n), range(m), range(m)))


def kernel(internal_weight: int) -> Matrix:
    if internal_weight < 1:
        raise ValueError("Positive integer internal weight required")
    d = [F(internal_weight if x[0] == x[1] else 1) for x in STATES]
    return [[d[i] * d[j] * F(4 ** sum(x[k] == y[k] for k in range(2)))
             for j, y in enumerate(STATES)] for i, x in enumerate(STATES)]


def row_tv(a: Matrix, i: int, j: int, message: list[F]) -> F:
    p = [x * y for x, y in zip(a[i], message, strict=True)]
    q = [x * y for x, y in zip(a[j], message, strict=True)]
    ptotal, qtotal = sum(p), sum(q)
    return sum((abs(x / ptotal - y / qtotal) for x, y in zip(p, q, strict=True)), F(0)) / 2


def blocking_counts(side: int, block: int) -> tuple[int, set[int], set[int], set[int]]:
    if block < 1 or side % block or side < max(4, 2 * block):
        raise ValueError("Require an admissible periodic tiling")
    vertices = itertools.product(range(side), repeat=3)
    block_ids = tuple(itertools.product(range(side // block), repeat=3))
    internal = dict.fromkeys(block_ids, 0)
    boundary = dict.fromkeys(block_ids, 0)
    influence = dict.fromkeys(block_ids, 0)
    for x in vertices:
        for mu in range(3):
            for nu in range(mu + 1, 3):
                xm, xn = list(x), list(x)
                xm[mu] = (xm[mu] + 1) % side
                xn[nu] = (xn[nu] + 1) % side
                # Edge ownership is by base vertex; the fourth edge also starts at x.
                ids = {tuple(v[k] // block for k in range(3)) for v in (x, xm, xn)}
                if len(ids) == 1:
                    internal[next(iter(ids))] += 1
                else:
                    for bid in ids:
                        boundary[bid] += 1
                        influence[bid] += len(ids) - 1
    return len(block_ids), set(internal.values()), set(boundary.values()), set(influence.values())


def tilted_marginals(tilt_at: int | None) -> list[list[F]]:
    """Two binary spins per block and five times: exactly 4**5 paths."""
    length = 5
    fields = ((64, 1, 3, 32), (16, 2, 1, 48), (80, 3, 2, 40),
              (20, 1, 2, 72), (48, 2, 1, 64))
    total = 0
    sums = [[0] * 4 for _ in range(length)]
    for path in itertools.product(range(4), repeat=length):
        weight = 1
        for t, state in enumerate(path):
            weight *= fields[t][state]
            if t == tilt_at and state in (0, 3):
                weight *= 9
        for t in range(length - 1):
            x, y = STATES[path[t]], STATES[path[t + 1]]
            weight *= 4 ** sum(x[k] == y[k] for k in range(2))
        total += weight
        for t, state in enumerate(path):
            sums[t][state] += weight
    return [[F(x, total) for x in row] for row in sums]


class BlockChecks(unittest.TestCase):
    def test_01_geometric_partition(self) -> None:
        for side, m in ((4, 1), (4, 2), (6, 3), (8, 4)):
            _, internal, boundary, influence = blocking_counts(side, m)
            self.assertEqual(internal, {3 * m * (m - 1) ** 2})
            self.assertEqual(boundary, {12 * m**2 - 3 * m})
            self.assertEqual(influence, {12 * m**2 + 6 * m})

    def test_02_arbitrary_internal_weight_cancels(self) -> None:
        for weight in (1, 16, 10000):
            self.assertEqual(max_cross_ratio(kernel(weight)), F(256))

    def test_03_all_boundary_power_bound(self) -> None:
        r = F(15, 17)
        for weight in (1, 16, 10000):
            a = kernel(weight)
            for b in (1, 2, 4, 12):
                ratio = max_cross_ratio(power(a, b))
                self.assertLessEqual(ratio, ((1 + r**b) / (1 - r**b)) ** 2)
            self.assertLessEqual(r**12, F(1, 4))

    def test_04_endpoint_messages(self) -> None:
        a = power(kernel(16), 12)
        for message in ([F(1)] * 4, [F(7), F(3), F(2), F(101)],
                        [F(10**8), F(1), F(13), F(5)]):
            for i, j in itertools.product(range(4), repeat=2):
                self.assertLessEqual(row_tv(a, i, j, message), F(1, 4))

    def test_05_exact_interface_tilt_sandwich(self) -> None:
        c = kernel(1)
        internal = [F(256), F(1), F(1), F(256)]
        q = F(65, 64)
        tilt = [q, 1 / q, q, 1 / q]
        base = multiply(c, [[internal[i] * c[i][j] for j in range(4)] for i in range(4)])
        changed = multiply(c, [[internal[i] * tilt[i] * c[i][j] for j in range(4)] for i in range(4)])
        for i, j in itertools.product(range(4), repeat=2):
            self.assertLessEqual(base[i][j] / q, changed[i][j])
            self.assertLessEqual(changed[i][j], q * base[i][j])
        self.assertLessEqual(max_cross_ratio(changed), q**4 * max_cross_ratio(base))

    def test_06_joint_path_marginal_consequence(self) -> None:
        p, q = tilted_marginals(None), tilted_marginals(2)
        for t in range(5):
            tv = sum((abs(x-y) for x, y in zip(p[t], q[t], strict=True)), F(0)) / 2
            self.assertLessEqual(tv, F(1, 2) * F(15, 17) ** abs(t-2))

    def test_07_bridge_and_weight_constants(self) -> None:
        ratio = F(5, 3) * F(8, 7)  # exp(1/8) <= 8/7
        self.assertEqual((ratio-1)/(ratio+1), F(19, 61))
        self.assertLess(F(19, 61), F(1, 2))
        for b in (1, 2, 12, 100):
            self.assertEqual(F(1, 16*b) * 8*b, F(1, 2))
            self.assertLess(F(4*b-1, 16*b), F(1, 4))

    def test_08_block_state_is_not_a_tensor_of_singlets(self) -> None:
        eye = sp.eye(2)
        pauli = [sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -sp.I], [sp.I, 0]]),
                 sp.Matrix([[1, 0], [0, -1]])]
        group = [eye, -eye] + [s * sp.I * p for p in pauli for s in (1, -1)]
        vals = [(a*b).trace() for a in group for b in group]
        self.assertEqual(sum(vals), 0)
        self.assertEqual(sum(v**2 for v in vals) / 64, 1)
        for a, b in itertools.product(group, repeat=2):
            self.assertEqual(sum((h*a*b).trace() for h in group), 0)
        a, b, g0, g1 = group[2], group[4], group[6], group[3]
        glued = (g0*a*g1.inv()) * (g1*b*g0.inv())
        self.assertEqual(sp.simplify(glued.trace() - (a*b).trace()), 0)

    def test_09_temporal_anisotropy_product(self) -> None:
        a, tau, g = sp.symbols('a tau g', positive=True)
        beta_t, beta_s = 4*a/(g**2*tau), 4*tau/(g**2*a)
        self.assertEqual(sp.simplify(beta_t * beta_s), 16/g**4)
        self.assertEqual(sp.simplify((sp.Rational(1, 1) / (576*beta_t)) / tau), g**2/(2304*a))

    def test_10_invalid_inputs(self) -> None:
        for side, block in ((3, 1), (4, 3), (4, 0)):
            with self.assertRaises(ValueError):
                blocking_counts(side, block)
        with self.assertRaises(ValueError):
            max_cross_ratio([[F(1), F(0)], [F(1), F(1)]])
        with self.assertRaises(ValueError):
            power(kernel(1), -1)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    start = time.perf_counter()
    result = unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(BlockChecks))
    record = {
        'status': 'passed' if result.wasSuccessful() else 'failed',
        'tests_run': result.testsRun, 'failures': len(result.failures), 'errors': len(result.errors),
        'seconds': time.perf_counter()-start, 'python': platform.python_version(), 'sympy': sp.__version__,
        'arithmetic': 'Fraction and SymPy exact rational/matrix identities; no floating decisions',
        'binary_path_population': 1024, 'binary_kernel_dimension': 4,
        'finite_group': 'Q8, boundary-gluing identity only; not SU(2) numerical physics',
        'geometry': [{'block_side': m, 'internal_plaquettes': 3*m*(m-1)**2,
                      'crossing_incidence': 12*m*m-3*m, 'influence_incidence': 12*m*m+6*m}
                     for m in (1, 2, 3, 4)],
        'bridge_constant': '19/61', 'auxiliary_two_bit_contraction': '15/17',
        'physical_status': 'No continuum mass-gap bound; continuous and all-volume results require written proof',
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(record, indent=2)+'\n')
    if not result.wasSuccessful():
        raise SystemExit(1)


if __name__ == '__main__':
    main()

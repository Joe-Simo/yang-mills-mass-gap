"""Exact finite audits of history-conditioned slabs; not a Yang--Mills gap proof.

Run: python checks/U033_history_conditioned_slab_checks.py --output evidence/U033_checks.json
Python integers/Fraction and SymPy rationals only for decisions. The universal
continuous-SU(2) theorem has a separate written proof and a checked source leaf.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
from itertools import combinations, product
import json
from pathlib import Path
import platform
import time
import unittest

import sympy as sp

from U029_exact_link_integration_checks import outward_decimal, periodic_faces
from U032_conditional_memory_checks import exp_interval, psd_exact, tilted_transfer

Matrix = sp.MatrixBase
RATE = F(3, 5)


def aggregate_rate(rates: tuple[F, ...], steps: int) -> F:
    if steps < 1 or any(r < 0 or r >= 1 for r in rates):
        raise ValueError("positive step count and rates in [0,1) required")
    upper = F(1)
    lower = F(1)
    for rate in rates:
        x = rate ** steps
        upper *= 1 + x
        lower *= 1 - x
    return (upper - lower) / (upper + lower)


def chain_kernel(weights: tuple[tuple[int, int], ...]) -> Matrix:
    c = sp.Matrix([[4, 1], [1, 4]])
    result = c.copy()
    for a, b in weights:
        if a <= 0 or b <= 0:
            raise ValueError("interior weights must be strictly positive")
        result = result * sp.diag(a, b) * c
    return result


def max_cross_ratio(kernel: Matrix) -> sp.Rational:
    if any(v <= 0 for v in kernel):
        raise ValueError("strictly positive matrix required")
    return max(kernel[i, j] * kernel[k, l] / (kernel[i, l] * kernel[k, j])
               for i, k in product(range(kernel.rows), repeat=2)
               for j, l in product(range(kernel.cols), repeat=2))


def history_split(k: Matrix, pi: Matrix, steps: int) -> tuple[Matrix, Matrix, Matrix]:
    """Enumerate all paths of this four-state fixture, retaining the first bit."""
    if steps < 1 or steps > 4 or k.shape != (4, 4):
        raise ValueError("fixture contract: dimension 4 and steps 1..4")
    masses: dict[tuple[int, ...], sp.Rational] = {}
    left: dict[tuple[int, ...], Matrix] = {}
    right: dict[tuple[int, ...], Matrix] = {}
    joint = sp.zeros(4)
    for states in product(range(4), repeat=steps + 1):
        mass = pi[states[0]]
        for t in range(steps):
            mass *= k[states[t], states[t + 1]]
        key = tuple(s // 2 for s in states)
        if key not in masses:
            masses[key] = sp.Rational(0)
            left[key] = sp.zeros(4, 1)
            right[key] = sp.zeros(4, 1)
        masses[key] += mass
        left[key][states[0]] += mass
        right[key][states[-1]] += mass
        joint[states[0], states[-1]] += mass
    explained_joint = sp.zeros(4)
    for key, mass in masses.items():
        explained_joint += left[key] * right[key].T / mass
    w = sp.diag(*pi)
    return w.inv() * explained_joint, w.inv() * (joint - explained_joint), joint


def z_squared_interval(z2: F, terms: int = 160) -> tuple[F, F]:
    """Z(sqrt(z2)) = sum (z2/4)^k/[k!(k+1)!], full positive tail."""
    if z2 < 0 or terms < 0:
        raise ValueError("nonnegative squared argument and term cap required")
    p = z2 / 4
    total = term = F(1)
    for k in range(terms):
        term *= p / ((k + 1) * (k + 2))
        total += term
    nxt = term * p / ((terms + 1) * (terms + 2))
    ratio = p / ((terms + 2) * (terms + 3))
    if ratio >= 1:
        raise ValueError("insufficient terms for geometric tail")
    return total, total + nxt / (1 - ratio)


def su2_two_step_certificates() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    north = (F(1), F(0), F(0), F(0))
    south = tuple(-x for x in north)
    cases = [(beta, (source, F(0), F(0), F(0)), north, south, north, south)
             for beta in (F(1, 2), F(2), F(6))
             for source in (F(0), beta, 4 * beta)]
    cases.append((F(2), (F(1, 2), F(1), F(0), F(-1)),
                  north, (F(0), F(1), F(0), F(0)),
                  (F(3, 5), F(0), F(4, 5), F(0)),
                  (F(0), F(0), F(0), F(1))))
    for beta, source, u, up, v, vp in cases:
        for point in (u, up, v, vp):
            if sum(x * x for x in point) != 1:
                raise ValueError("unit quaternions required")
        squares = [sum((beta * (x + y) + h) ** 2
                       for x, y, h in zip(a, b, source, strict=True))
                   for a, b in ((u, v), (up, vp), (u, vp), (up, v))]
        intervals = [z_squared_interval(z2) for z2 in squares]
        lo = intervals[0][0] * intervals[1][0] / (intervals[2][1] * intervals[3][1])
        hi = intervals[0][1] * intervals[1][1] / (intervals[2][0] * intervals[3][0])
        el, _ = exp_interval(2 * beta, 160)
        r_lower = (el - 1) / (el + 1)
        cap_lower = ((1 + r_lower ** 2) / (1 - r_lower ** 2)) ** 2
        if not max(hi, 1 / lo) < cap_lower:
            raise AssertionError("two-step Birkhoff cross-ratio certificate failed")
        rows.append({
            "beta": str(beta), "source": [str(x) for x in source],
            "squared_Z_arguments": [str(x) for x in squares],
            "cross_ratio_interval": [outward_decimal(lo, 18, False),
                                     outward_decimal(hi, 18, True)],
            "cross_ratio_cap_lower": outward_decimal(cap_lower, 18, False),
            "tail_terms": 160, "both_cross_ratio_directions_verified": True,
        })
    return rows


class SlabChecks(unittest.TestCase):
    def test_extensive_spatial_selection(self) -> None:
        for n in (4, 6):
            chosen = {(x, 0) for x in product(range(n), repeat=3)
                      if (x[1] + x[2]) % 2 == 0}
            self.assertEqual(len(chosen), n ** 3 // 2)
            for face in periodic_faces(3, n):
                self.assertLessEqual(len(set(face) & chosen), 1)
        # Deliberate bad geometry: all links of direction 0 violate the condition.
        all_parallel = {(x, 0) for x in product(range(4), repeat=3)}
        self.assertTrue(any(len(set(f) & all_parallel) == 2
                            for f in periodic_faces(3, 4)))

    def test_one_step_and_empty_set_limits(self) -> None:
        self.assertEqual(aggregate_rate((), 3), 0)
        self.assertEqual(aggregate_rate((F(0),), 3), 0)
        self.assertEqual(aggregate_rate((RATE,), 1), RATE)
        self.assertEqual(aggregate_rate((RATE, RATE), 1), F(15, 17))
        for l in (1, 2, 3, 8):
            self.assertEqual(aggregate_rate((RATE,) * l, 1), F(4**l - 1, 4**l + 1))

    def test_time_composition_with_arbitrary_interior_weights(self) -> None:
        profiles = ((1, 1), (1, 3), (7, 2), (2, 5), (11, 1))
        for steps in range(1, 7):
            k = chain_kernel(tuple(profiles[j % len(profiles)] for j in range(steps - 1)))
            cap = ((1 + RATE ** steps) / (1 - RATE ** steps)) ** 2
            self.assertLessEqual(max_cross_ratio(k), sp.Rational(cap))

    def test_joint_endpoint_weights_cancel(self) -> None:
        k1 = chain_kernel(((1, 7), (3, 2)))
        k2 = chain_kernel(((5, 2), (1, 3)))
        tensor = sp.kronecker_product(k1, k2)
        tilted = sp.diag(1000, 2, 3, 1000) * tensor * sp.diag(9, 1, 2, 17)
        self.assertEqual(max_cross_ratio(tensor), max_cross_ratio(tilted))
        theta = aggregate_rate((RATE, RATE), 3)
        cap = ((1 + theta) / (1 - theta)) ** 2
        self.assertLessEqual(max_cross_ratio(tilted), sp.Rational(cap))

    def test_binary_tensor_bound_is_sharp_for_kernel_diameter(self) -> None:
        for steps in (1, 2, 4):
            c = chain_kernel(((1, 1),) * (steps - 1))
            for links in (1, 2, 3):
                k = c
                for _ in range(links - 1):
                    k = sp.kronecker_product(k, c)
                theta = aggregate_rate((RATE,) * links, steps)
                cap = ((1 + theta) / (1 - theta)) ** 2
                self.assertEqual(max_cross_ratio(k), sp.Rational(cap))

    def test_rate_sum_and_slab_depth(self) -> None:
        for steps in range(1, 12):
            self.assertLessEqual(aggregate_rate((F(1, 3), RATE, F(7, 9)), steps),
                                 F(1, 3) ** steps + RATE ** steps + F(7, 9) ** steps)
        for links in (1, 2, 16, 256, 4096):
            steps = 1
            while links * RATE ** steps > F(1, 100):
                steps += 1
            self.assertLessEqual(aggregate_rate((RATE,) * links, steps), F(1, 100))
            self.assertGreater(links * RATE ** (steps - 1), F(1, 100))

    def test_full_true_weighted_path_history_identity(self) -> None:
        k, pi, w = tilted_transfer((1, 2, 3, 5))
        for steps in range(1, 5):
            explained, residual, joint = history_split(k, pi, steps)
            self.assertEqual(joint, w * k ** steps)
            self.assertEqual(explained + residual, k ** steps)
            self.assertEqual(w * explained, explained.T * w)
            self.assertEqual(explained * sp.ones(4, 1), sp.ones(4, 1))
            self.assertTrue(psd_exact(sp.Rational(RATE ** (2 * steps)) * w
                                      - residual.T * w * residual))

    def test_slow_retained_mode_is_not_removed(self) -> None:
        k, pi, w = tilted_transfer((1000, 1, 1, 1000))
        f = sp.Matrix([1, 0, 0, -1])
        lam = sp.Rational(15000, 17008)
        self.assertEqual(k * f, lam * f)
        self.assertEqual((pi.T * f)[0], 0)
        explained, residual, _ = history_split(k, pi, 3)
        self.assertTrue(psd_exact(sp.Rational(RATE ** 6) * w - residual.T * w * residual))
        rayleigh = (f.T * w * explained * f)[0] / (f.T * w * f)[0]
        self.assertGreater(rayleigh, sp.Rational(RATE ** 3))
        self.assertGreater(lam ** 3, sp.Rational(RATE ** 3))

    def test_history_conditioning_does_not_protect_retained_gap(self) -> None:
        sigma = sp.Rational(99, 100)
        r = sp.Rational(RATE)
        j = sp.ones(2) / 2
        slow = j + sigma * (sp.eye(2) - j)
        fast = j + r * (sp.eye(2) - j)
        k = sp.kronecker_product(slow, fast)
        pi = sp.ones(4, 1) / 4
        for steps in (1, 2, 3):
            explained, residual, _ = history_split(k, pi, steps)
            self.assertEqual(explained, sp.kronecker_product(slow ** steps, j))
            self.assertEqual(residual, sp.kronecker_product(slow ** steps,
                                                           r ** steps * (sp.eye(2) - j)))
            f = sp.Matrix([1, 1, -1, -1])
            self.assertEqual(explained * f, sigma ** steps * f)
            self.assertGreater(sigma ** steps, r ** steps)

    def test_weighted_all_time_remainder_formula(self) -> None:
        r, q = sp.symbols('r q', positive=True)
        for m in (0, 1, 4, 10):
            full = r / (q - r)
            prefix = sum((r / q) ** j for j in range(1, m + 1))
            tail = (r / q) ** (m + 1) / (1 - r / q)
            self.assertEqual(sp.cancel(full - prefix - tail), 0)

    def test_continuous_su2_two_step_certificates(self) -> None:
        self.assertEqual(len(su2_two_step_certificates()), 10)
        self.assertEqual(z_squared_interval(F(0)), (F(1), F(1)))

    def test_invalid_inputs_rejected(self) -> None:
        for rates, steps in (((RATE,), 0), ((F(1),), 1), ((F(-1),), 1)):
            with self.assertRaises(ValueError):
                aggregate_rate(rates, steps)
        with self.assertRaises(ValueError):
            chain_kernel(((1, 0),))
        with self.assertRaises(ValueError):
            z_squared_interval(F(-1))
        with self.assertRaises(ValueError):
            z_squared_interval(F(100), 0)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    start = time.perf_counter()
    result = unittest.TextTestRunner(verbosity=2).run(
        unittest.defaultTestLoader.loadTestsFromTestCase(SlabChecks))
    rows: list[dict[str, object]] = []
    if result.wasSuccessful():
        for links in (1, 2, 16, 256, 4096):
            steps = 1
            while links * RATE ** steps > F(1, 100):
                steps += 1
            rows.append({'links': links, 'steps_sufficient': steps,
                         'tolerance': '1/100', 'single_step_rate': '3/5',
                         'union_upper_bound': str(links * RATE ** steps)})
    output = {
        'status': 'passed' if result.wasSuccessful() else 'failed',
        'tests_run': result.testsRun, 'seconds': time.perf_counter() - start,
        'python': platform.python_version(), 'sympy': sp.__version__,
        'arithmetic': 'exact integers, Fraction, and SymPy rationals; no fitted spectrum',
        'seed': None, 'binary_rate_table': rows,
        'su2_two_step_certificates': su2_two_step_certificates() if result.wasSuccessful() else [],
        'scope': 'finite formula/geometry/path tests; universal proof in the U033 note',
    }
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(output, indent=2) + '\n')
    print(json.dumps(output, indent=2))
    return 0 if result.wasSuccessful() else 1


if __name__ == '__main__':
    raise SystemExit(main())

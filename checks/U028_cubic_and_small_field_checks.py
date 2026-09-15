"""Exact finite checks supporting U028; not a continuum or interacting-gap certificate.

Model: open cubical SU(2) spatial graphs and the precisely specified quadratic
reference. Uses SymPy exact arithmetic, no random sampling or fitted eigenvalues.
Run: python checks/U028_cubic_and_small_field_checks.py --output evidence/U028_checks.json
"""
from __future__ import annotations

import argparse
from collections import Counter
from dataclasses import dataclass
from functools import lru_cache
import hashlib
from itertools import combinations, product
import json
from pathlib import Path
import platform
import time
import unittest

import sympy as sp

Cell = tuple[tuple[int, ...], tuple[int, ...]]
BOXES = ((1, 1, 1), (2, 1, 1), (2, 2, 1), (2, 2, 2))


@dataclass(frozen=True)
class Complex:
    sizes: tuple[int, ...]
    cells: tuple[tuple[Cell, ...], ...]
    coboundaries: tuple[sp.MutableDenseMatrix, ...]


@lru_cache(maxsize=None)
def cubical(sizes: tuple[int, ...]) -> Complex:
    """All cells of an open product of paths, each orientation counted once."""
    if len(sizes) not in (2, 3) or any(type(n) is not int or n < 1 for n in sizes):
        raise ValueError("two or three strictly positive integral cell counts required")
    dim = len(sizes)
    cells: list[tuple[Cell, ...]] = []
    for degree in range(dim + 1):
        level: list[Cell] = []
        for axes in combinations(range(dim), degree):
            ranges = [range(n if i in axes else n + 1) for i, n in enumerate(sizes)]
            level.extend((axes, tuple(x)) for x in product(*ranges))
        cells.append(tuple(level))
    maps = []
    for degree in range(dim):
        index = {cell: i for i, cell in enumerate(cells[degree])}
        matrix = sp.zeros(len(cells[degree + 1]), len(cells[degree]))
        for row, (axes, point) in enumerate(cells[degree + 1]):
            for j, axis in enumerate(axes):
                subaxes = axes[:j] + axes[j + 1:]
                upper = list(point)
                upper[axis] += 1
                sign = (-1)**j
                matrix[row, index[(subaxes, tuple(upper))]] += sign
                matrix[row, index[(subaxes, point)]] -= sign
        maps.append(matrix)
    return Complex(sizes, tuple(cells), tuple(maps))


def product_spectrum(sizes: tuple[int, ...]) -> Counter:
    """Predicted positive curl spectrum; multiplicity is active directions minus one."""
    values: Counter = Counter()
    for labels in product(*(range(n + 1) for n in sizes)):
        active = sum(k > 0 for k in labels)
        if active < 2:
            continue
        eigenvalue = sp.simplify(sum(4*sp.sin(sp.pi*k/(2*(n + 1)))**2
                                     for k, n in zip(labels, sizes)))
        values[eigenvalue] += active - 1
    return values


def full_charpoly_from_spectrum(sizes: tuple[int, ...], variable: sp.Symbol) -> sp.Expr:
    v = sp.prod(n + 1 for n in sizes)
    polynomial = variable**(v - 1)
    for value, multiplicity in product_spectrum(sizes).items():
        polynomial *= (variable - value)**multiplicity
    return sp.expand(polynomial)


class CubicalTests(unittest.TestCase):
    def test_cell_counts(self) -> None:
        for sizes in BOXES:
            k = cubical(sizes)
            nx, ny, nz = sizes
            expected = ((nx + 1)*(ny + 1)*(nz + 1),
                        nx*(ny + 1)*(nz + 1) + ny*(nx + 1)*(nz + 1) + nz*(nx + 1)*(ny + 1),
                        nx*ny*(nz + 1) + nx*nz*(ny + 1) + ny*nz*(nx + 1), nx*ny*nz)
            self.assertEqual(tuple(map(len, k.cells)), expected)

    def test_chain_conditions_and_ranks(self) -> None:
        for sizes in BOXES:
            k = cubical(sizes)
            d0, d1, d2 = k.coboundaries
            self.assertEqual(d1*d0, sp.zeros(d1.rows, d0.cols))
            self.assertEqual(d2*d1, sp.zeros(d2.rows, d1.cols))
            v, e, f, c = map(len, k.cells)
            self.assertEqual(d0.rank(), v - 1)
            self.assertEqual(d1.rank(), e - v + 1)
            self.assertEqual(d2.rank(), c)
            self.assertEqual(e - v + 1, f - c)

    def test_single_cube_has_one_face_constraint(self) -> None:
        k = cubical((1, 1, 1))
        c, b = k.coboundaries[1:]
        self.assertEqual(list((c*c.T).diagonal()), [4]*6)
        self.assertEqual((c*c.T).det(), 0)
        self.assertNotEqual(c.rank(), c.rows)
        self.assertEqual((c*c.T).eigenvals(), {sp.Integer(0): 1, sp.Integer(4): 3, sp.Integer(6): 2})
        self.assertEqual(c.T*b.T, sp.zeros(12, 1))
        self.assertEqual(b*b.T, sp.Matrix([[6]]))

    def test_product_formula_against_full_matrix(self) -> None:
        z = sp.Symbol('z')
        for sizes in BOXES:
            c = cubical(sizes).coboundaries[1]
            actual = (c.T*c).charpoly(z).as_expr()
            self.assertEqual(sp.expand(actual - full_charpoly_from_spectrum(sizes, z)), 0)

    def test_orientation_reversal_keeps_spectrum(self) -> None:
        d0, c, b = cubical((1, 1, 1)).coboundaries
        edges, faces = sp.eye(c.cols), sp.eye(c.rows)
        edges[0, 0] = faces[2, 2] = -1
        changed = faces*c*edges
        self.assertEqual(changed*(edges*d0), sp.zeros(c.rows, d0.cols))
        self.assertEqual((b*faces)*changed, sp.zeros(b.rows, c.cols))
        z = sp.Symbol('z')
        self.assertEqual((changed.T*changed).charpoly(z).as_expr(), (c.T*c).charpoly(z).as_expr())

    def test_tensor_curl_symbol_and_gradient(self) -> None:
        u, v, w = sp.symbols('u v w', real=True)
        d = sp.Matrix([u, v, w])
        c = sp.Matrix([[-v, u, 0], [-w, 0, u], [0, -w, v]])
        self.assertEqual(c*d, sp.zeros(3, 1))
        self.assertEqual(c.T*c, (u*u + v*v + w*w)*sp.eye(3) - d*d.T)

    def test_planar_control_and_smallest_cubic_values(self) -> None:
        for sizes in ((1, 1), (2, 1), (2, 2)):
            c = cubical(sizes).coboundaries[1]
            self.assertEqual(c.rank(), c.rows)
        for n, expected in ((1, 4), (2, 2)):
            values = product_spectrum((n, n, n))
            self.assertEqual(min(values), expected)
            self.assertEqual(values[expected], 3)
            self.assertEqual(sum(values.values()), 2*n**3 + 3*n**2)

    def test_invalid_geometry(self) -> None:
        for sizes in ((0, 1, 1), (1,), (2.5, 1, 1)):
            with self.assertRaises(ValueError):
                cubical(sizes)


class AnalyticChecks(unittest.TestCase):
    def test_oscillator_ground_and_singlet(self) -> None:
        # Set sqrt(lambda*mu)=z. This avoids branch-dependent symbolic square roots.
        x = sp.symbols('x0:3', real=True)
        z = sp.Symbol('z', positive=True)
        r2 = sum(v*v for v in x)
        psi = sp.exp(-z*r2)
        def action(f: sp.Expr) -> sp.Expr:
            return -sum(sp.diff(f, v, 2) for v in x)/8 + z*z*r2*f/2
        self.assertEqual(sp.simplify(action(psi) - 3*z*psi/4), 0)
        excited = (r2 - sp.Rational(3, 4)/z)*psi
        self.assertEqual(sp.simplify(action(excited) - 7*z*excited/4), 0)
        # Density psi^2 gives variance 1/(4z) in each real normal coordinate.
        integral = sp.integrate(x[0]**2*sp.exp(-2*z*x[0]**2), (x[0], -sp.oo, sp.oo))
        norm = sp.integrate(sp.exp(-2*z*x[0]**2), (x[0], -sp.oo, sp.oo))
        self.assertEqual(sp.simplify(integral/norm), 1/(4*z))

    def test_sobolev_scalar_step_and_constant(self) -> None:
        a, b = sp.symbols('a b', nonnegative=True)
        self.assertEqual(sp.expand(2*(a**3 + b**3) - (a + b)*(a*a + b*b)), sp.expand((a + b)*(a - b)**2))
        self.assertEqual((8*4/sp.sqrt(3))**2, sp.Rational(1024, 3))
        delta = sp.sqrt(3)/64
        self.assertEqual(sp.simplify((32/sp.sqrt(3))*delta), sp.Rational(1, 2))

    def test_discrete_hodge_identity_for_interior_curl(self) -> None:
        # Compact support is padded: an interior face cochain generates A=d1*B.
        k = cubical((3, 3, 3))
        d0, c, _ = k.coboundaries
        face = ((0, 1), (1, 1, 1))
        b = sp.zeros(c.rows, 1)
        b[k.cells[2].index(face)] = 1
        a = c.T*b
        self.assertEqual(d0.T*a, sp.zeros(d0.cols, 1))
        field = {(point, axes[0]): a[i] for i, (axes, point) in enumerate(k.cells[1]) if a[i] != 0}
        norm_grad = sp.S.Zero
        for point in product(range(-1, 5), repeat=3):
            for mu in range(3):
                nxt = list(point); nxt[mu] += 1
                for nu in range(3):
                    diff = field.get((tuple(nxt), nu), 0) - field.get((point, nu), 0)
                    norm_grad += diff**2
        self.assertEqual(norm_grad, (c*a).dot(c*a))

    def test_nonlinear_noncommuting_plaquette(self) -> None:
        t, s = sp.symbols('t s', real=True)
        sig1 = sp.Matrix([[0, 1], [1, 0]])
        sig2 = sp.Matrix([[0, -sp.I], [sp.I, 0]])
        u = sp.cos(t)*sp.eye(2) + sp.I*sp.sin(t)*sig1
        v = sp.cos(s)*sp.eye(2) + sp.I*sp.sin(s)*sig2
        hol = u*v*u.conjugate().T*v.conjugate().T
        deficit = sp.trigsimp(1 - sp.trace(hol)/2)
        self.assertEqual(sp.trigsimp(deficit - 2*sp.sin(t)**2*sp.sin(s)**2), 0)
        self.assertEqual(sp.limit((deficit.subs(s, t))/t**4, t, 0), 2)

    def test_gaussian_chernoff_and_spectral_floor(self) -> None:
        tau = sp.Symbol('tau', positive=True)
        f = -sp.log(tau) - 1 + tau - (1 - tau)**2/2
        self.assertEqual(sp.factor(sp.diff(f, tau)), -(tau - 1)**2/tau)
        self.assertEqual(f.subs(tau, 1), 0)
        n = sp.Symbol('n', integer=True, positive=True)
        rank = 3*n*(n + 1)**2 - (n + 1)**3 + 1
        self.assertEqual(sp.expand(rank), 2*n**3 + 3*n**2)
        # The uniform conservative variance floor uses mu<=12.
        g = sp.Symbol('g', positive=True)
        floor = g*g/(8*sp.sqrt(12))
        self.assertEqual(sp.simplify((n + 1)*(sp.sqrt(3)/64)**2/(3*rank*floor)), sp.sqrt(3)*(n + 1)/(256*g*g*n*n*(2*n + 3)))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    start = time.perf_counter()
    suite = unittest.defaultTestLoader.loadTestsFromModule(__import__(__name__))
    outcome = unittest.TextTestRunner(verbosity=2).run(suite)
    c = cubical((1, 1, 1))
    payload = {
        'base_commit': '8c03d35c20d265e0259c4c8e2be1d48b60e8a8c3',
        'python': platform.python_version(), 'sympy': sp.__version__,
        'arithmetic': 'exact integers, rationals, symbolic identities; no random sampling',
        'tests_run': outcome.testsRun, 'passed': outcome.wasSuccessful(),
        'runtime_seconds': round(time.perf_counter() - start, 6),
        'boxes_tested': [list(b) for b in BOXES],
        'cube_face_edge_incidence': [[int(v) for v in row] for row in c.coboundaries[1].tolist()],
        'cube_bianchi_row': [int(v) for v in c.coboundaries[2].tolist()[0]],
        'cube_curl_spectrum': {'0': 1, '4': 3, '6': 2},
        'general_proof_status': 'Written derivations in U028, not inferred from finite tests',
        'code_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'nonclaims': ['No joint weak-coupling/volume limit', 'No true-vacuum probability bound', 'No continuum mass gap'],
    }
    text = json.dumps(payload, indent=2)
    print(text)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text + '\n')
    return 0 if outcome.wasSuccessful() else 1


if __name__ == '__main__':
    raise SystemExit(main())

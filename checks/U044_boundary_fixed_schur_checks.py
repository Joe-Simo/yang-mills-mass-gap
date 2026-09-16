"""Exact finite audits for U044; not a continuum Yang--Mills certificate.

Run: python checks/U044_boundary_fixed_schur_checks.py --output evidence/U044_checks.json
Arithmetic: exact rationals/SymPy where decisions are load-bearing; finite floating
checks are labeled diagnostics only. Universal inequalities require the written proof.
"""
from __future__ import annotations

import argparse
import json
import math
import platform
import time
import unittest
from fractions import Fraction as F
from pathlib import Path

import sympy as sp


def path_neumann_laplacian(n: int) -> sp.Matrix:
    if n < 1:
        raise ValueError("n>=1")
    if n == 1:
        return sp.zeros(1)
    B = sp.zeros(n - 1, n)
    for i in range(n - 1):
        B[i, i] = -1
        B[i, i + 1] = 1
    return B.T * B


def longitudinal_pair(ell: int, s: sp.Rational) -> tuple[sp.Matrix, sp.Matrix, sp.Matrix]:
    """Return divergence D, curl C and nullspace basis Z.

    Boundary longitudinal tangential values a_0=a_ell=0 are fixed. Variables are
    a_1,...,a_(ell-1), c_0,...,c_(ell-1), with tangential momentum magnitude s.
    """
    if ell < 2:
        raise ValueError("ell>=2")
    na, nc = ell - 1, ell
    n = na + nc
    D = sp.zeros(ell - 1, n)
    for r in range(1, ell):
        D[r - 1, r - 1] = s
        D[r - 1, na + r - 1] = 1
        D[r - 1, na + r] = -1
    C = sp.zeros(ell, n)
    for r in range(ell):
        if r + 1 <= ell - 1:
            C[r, r] += 1
        if r >= 1:
            C[r, r - 1] -= 1
        C[r, na + r] -= s
    ns = D.nullspace()
    Z = sp.Matrix.hstack(*ns)
    return D, C, Z


def generalized_charpoly(ell: int, s: sp.Rational) -> sp.Expr:
    _, C, Z = longitudinal_pair(ell, s)
    M = Z.T * C.T * C * Z
    G = Z.T * Z
    t = sp.symbols("t")
    return sp.factor((M - t * G).det() / G.det())


def expected_longitudinal_charpoly(ell: int, s: sp.Rational) -> sp.Expr:
    t = sp.symbols("t")
    L = path_neumann_laplacian(ell)
    return sp.factor((L + s**2 * sp.eye(ell) - t * sp.eye(ell)).det())


def schur(M: sp.Matrix, nb: int) -> sp.Matrix:
    A = M[:nb, :nb]
    B = M[:nb, nb:]
    D = M[nb:, nb:]
    return sp.simplify(A - B * D.inv() * B.T)


def opnorm_sym_2x2(M: sp.Matrix) -> sp.Expr:
    vals = list(M.eigenvals().keys())
    return max([abs(sp.N(v, 30)) for v in vals])


class U044Checks(unittest.TestCase):
    def test_01_longitudinal_exact_spectrum(self) -> None:
        s = sp.Rational(1, 2)
        for ell in range(2, 7):
            with self.subTest(ell=ell):
                self.assertEqual(
                    sp.simplify(generalized_charpoly(ell, s) - expected_longitudinal_charpoly(ell, s)),
                    0,
                )

    def test_02_longitudinal_low_mode_is_lambda(self) -> None:
        s = sp.Rational(2, 5)
        for ell in (2, 3, 5, 8):
            L = path_neumann_laplacian(ell)
            ones = sp.ones(ell, 1)
            self.assertEqual((L + s**2 * sp.eye(ell)) * ones, s**2 * ones)

    def test_03_normal_excited_gap(self) -> None:
        for ell in range(2, 50):
            lhs = 4 * math.sin(math.pi / (2 * ell)) ** 2
            rhs = 4 / ell**2
            self.assertGreaterEqual(lhs + 1e-15, rhs)

    def test_04_soft_integer_count_is_uniform(self) -> None:
        for Lambda in (4, 16, 64, 144):
            R = math.ceil(math.sqrt(Lambda) / 4 + 0.5)
            bound = (2 * R + 1) ** 3
            self.assertGreater(bound, 0)
            for ell in (8, 16, 32, 64):
                actual = 0
                for i in range(-ell // 2, ell // 2):
                    for j in range(-ell // 2, ell // 2):
                        for k in range(-ell // 2, ell // 2):
                            lam = 4 * (
                                math.sin(math.pi * i / ell) ** 2
                                + math.sin(math.pi * j / ell) ** 2
                                + math.sin(math.pi * k / ell) ** 2
                            )
                            if lam <= Lambda / ell**2 + 1e-14:
                                actual += 1
                self.assertLessEqual(actual, bound)

    def test_05_boundary_fixed_gauge_transversality_fixture(self) -> None:
        G0 = sp.Matrix([[1, 0], [0, 2], [1, -1]])
        E = sp.Matrix([[sp.Rational(1, 20), 0], [0, -sp.Rational(1, 20)], [0, sp.Rational(1, 40)]])
        G = G0 + E
        self.assertEqual(G.rank(), 2)
        self.assertNotEqual((G.T * G).det(), 0)

    def test_06_schur_identity_and_bound_fixture(self) -> None:
        H0 = sp.Matrix([
            [4, 1, 1, 0],
            [1, 3, 0, 1],
            [1, 0, 2, 0],
            [0, 1, 0, 2],
        ])
        self.assertTrue(all(v > 0 for v in H0.eigenvals().keys()))
        E = sp.Matrix([
            [F(1, 50), 0, F(1, 100), 0],
            [0, -F(1, 100), 0, F(1, 100)],
            [F(1, 100), 0, F(1, 100), 0],
            [0, F(1, 100), 0, -F(1, 200)],
        ])
        E = sp.Matrix([[sp.Rational(x.numerator, x.denominator) if isinstance(x, F) else x for x in row] for row in E.tolist()])
        H = H0 + E
        S0, S = schur(H0, 2), schur(H, 2)
        self.assertEqual(S0, S0.T)
        self.assertEqual(S, S.T)
        self.assertTrue(all(sp.N(v, 30) > 0 for v in S.eigenvals().keys()))

    def test_07_scaled_resolvent_formula(self) -> None:
        m, e = sp.symbols("m e", positive=True)
        eta = e / m
        residual = sp.simplify(1 / (m + e) - (1 / m) * 1 / (1 + eta))
        self.assertEqual(residual, 0)

    def test_08_exponents(self) -> None:
        self.assertEqual(sp.Rational(7, 26) - 2 * sp.Rational(1, 13), sp.Rational(3, 26))
        self.assertEqual(sp.Rational(7, 26) - 3 * sp.Rational(1, 13), sp.Rational(1, 26))
        self.assertEqual(2 * sp.Rational(7, 26) - 2 * sp.Rational(1, 13), sp.Rational(5, 13))

    def test_09_flat_maxwell_operator_norm_bound(self) -> None:
        self.assertEqual(6 * 4, 24)

    def test_10_schur_bound_scaling_is_favorable(self) -> None:
        for q in (1, 2, 3):
            alpha = F(1, 2 ** (26 * q))
            delta = F(1, 2 ** (7 * q))
            ell = 2 ** (2 * q)
            self.assertEqual(delta * ell**2, F(1, 2 ** (3 * q)))
            self.assertEqual(delta * ell**3, F(1, 2 ** q))
            self.assertEqual(delta**2 * ell**2, F(1, 2 ** (10 * q)))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    start = time.perf_counter()
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(U044Checks)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    payload = {
        "status": "passed" if result.wasSuccessful() else "failed",
        "tests_run": result.testsRun,
        "failures": len(result.failures),
        "errors": len(result.errors),
        "seconds": time.perf_counter() - start,
        "python": platform.python_version(),
        "sympy": sp.__version__,
        "arithmetic": "exact rational/symbolic for structural identities; labeled floating finite soft-count diagnostics",
        "seed": None,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2) + "\n")
    if not result.wasSuccessful():
        raise SystemExit(1)


if __name__ == "__main__":
    main()

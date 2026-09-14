"""Exact checks for U003; no finite test decides the Yang--Mills problem.

Run: python checks/U003_relative_gap_checks.py
Arithmetic: SymPy integers/rationals and symbolic polynomial identities.
All infinite-dimensional, all-volume, and infinite-product claims use the
written proofs, not the bounded checks in this module.
"""
from __future__ import annotations

from itertools import combinations, product
import json
import platform
import unittest

import sympy as sp

Q = sp.Rational


def two_state(eigenvalue: sp.Expr) -> sp.Matrix:
    """The exact symmetric stochastic family used only as a test fixture."""
    return sp.Matrix([[1 + eigenvalue, 1 - eigenvalue],
                      [1 - eigenvalue, 1 + eigenvalue]]) / 2


def haar_polynomial(poly: sp.Expr, x: sp.Symbol) -> sp.Expr:
    """Integrate a polynomial against the SU(2) class-coordinate Haar measure.

    Uses the exact moments E[x^(2k)] = Catalan(k)/4^k, E[x^(2k+1)]=0.
    That formula is justified in the note and independently integrated in Wolfram.
    """
    result = sp.S.Zero
    for (power,), coefficient in sp.Poly(poly, x).terms():
        if power % 2 == 0:
            k = power // 2
            result += coefficient * sp.catalan(k) / 4 ** k
    return sp.simplify(result)


def psd_two_by_two(matrix: sp.Matrix) -> bool:
    """Exact principal-minor criterion; only called with real rational entries."""
    if matrix.shape != (2, 2):
        raise ValueError("Expected a two-by-two matrix")
    return bool(matrix == matrix.T and matrix[0, 0] >= 0
                and matrix[1, 1] >= 0 and matrix.det() >= 0)


class RelativeGapChecks(unittest.TestCase):
    def test_exact_coarse_compression_misses_slow_hidden_state(self) -> None:
        j = sp.Matrix([[1, 0], [1, 0], [0, 1], [0, 1]]) / sp.sqrt(2)
        coarse = two_state(Q(1, 2))
        modes = [sp.Matrix(v) for v in (
            (1, 1, 1, 1), (1, 1, -1, -1),
            (1, -1, 1, -1), (1, -1, -1, 1))]
        self.assertEqual(j.T * j, sp.eye(2))
        for k in range(1, 13):
            epsilon = Q(1, 2 ** k)
            fine = sp.kronecker_product(coarse, two_state(1 - epsilon))
            eigenvalues = [1, Q(1, 2), 1 - epsilon, (1 - epsilon) / 2]
            self.assertEqual(j.T * fine * j, coarse)
            self.assertEqual(fine * j, j * coarse)
            self.assertTrue(all(entry > 0 for entry in fine))
            self.assertEqual(fine * sp.ones(4, 1), sp.ones(4, 1))
            for v, value in zip(modes, eigenvalues, strict=True):
                self.assertEqual(fine * v, value * v)
            self.assertEqual(max(eigenvalues[1:]), 1 - epsilon)

    def test_two_good_diagonal_blocks_do_not_control_mixing(self) -> None:
        for k in range(2, 14):
            epsilon = Q(1, 2 ** k)
            s = sp.Matrix([[Q(1, 2), Q(1, 2) - epsilon],
                           [Q(1, 2) - epsilon, Q(1, 2)]])
            self.assertTrue(psd_two_by_two(s))
            self.assertTrue(psd_two_by_two(sp.eye(2) - s))
            self.assertEqual(s * sp.ones(2, 1), (1 - epsilon) * sp.ones(2, 1))
            g = sp.eye(2) - s
            self.assertEqual(sp.simplify(g[0, 1] ** 2 / (g[0, 0] * g[1, 1])),
                             (1 - 2 * epsilon) ** 2)

    def test_schur_factorization(self) -> None:
        a, d, b, target = sp.symbols("a d b target", real=True)
        full = sp.Matrix([[a, b], [b, d]])
        left = sp.Matrix([[1, b / (d - target)], [0, 1]])
        middle = sp.diag(a - target - b ** 2 / (d - target), d - target)
        residual = left * middle * left.T - (full - target * sp.eye(2))
        self.assertEqual(residual.applyfunc(sp.factor), sp.zeros(2))

    def test_relative_mixing_is_quadratic_in_certificate(self) -> None:
        # Exactly 24 rational scalar-block instances; not arbitrary operator coverage.
        count = 0
        for a, d, b in product((Q(1, 8), Q(1, 4), Q(1, 2)),
                               (Q(1, 2), Q(3, 4)),
                               (Q(0), Q(1, 32), Q(1, 16), Q(1, 8))):
            r_squared = b ** 2 / (a * d)
            self.assertLess(r_squared, Q(1, 2))
            full = sp.Matrix([[a, b], [b, d]])
            lower = sp.diag((1 - 2 * r_squared) * a, d / 2)
            self.assertTrue(psd_two_by_two(full - lower))
            self.assertEqual((full - lower).det(), 0)
            self.assertTrue(psd_two_by_two(sp.eye(2) - full))
            count += 1
        self.assertEqual(count, 24)

    def test_missing_factor_two_is_rejected(self) -> None:
        a, d, b = Q(1, 4), Q(1, 2), Q(1, 8)
        r_squared = b ** 2 / (a * d)
        bad_lower = sp.diag((1 - r_squared) * a, d / 2)
        self.assertFalse(psd_two_by_two(sp.Matrix([[a, b], [b, d]]) - bad_lower))

    def test_exact_infinite_product_schedule_finite_identity(self) -> None:
        # Written telescoping proof covers all N and the limiting product 4/9.
        accumulated = sp.S.One
        for n in range(3, 35):
            eta = Q(1, n ** 2)
            r_squared = Q(1, 2 * n ** 2)
            accumulated *= (1 - eta) * (1 - 2 * r_squared)
            self.assertEqual(accumulated, Q(2 * (n + 1), 3 * n) ** 2)
            self.assertGreater(accumulated, Q(4, 9))
        self.assertGreater(accumulated * Q(1, 4), Q(1, 9))


class SU2Checks(unittest.TestCase):
    def test_haar_character_algebra(self) -> None:
        x = sp.Symbol("x", real=True)
        fundamental, adjoint = 2 * x, 4 * x ** 2 - 1
        integrands = [1, fundamental, adjoint, fundamental ** 2, adjoint ** 2,
                      fundamental * adjoint, fundamental ** 2 * adjoint,
                      fundamental ** 3, fundamental * adjoint ** 2]
        self.assertEqual([haar_polynomial(p, x) for p in integrands],
                         [1, 0, 0, 1, 1, 0, 1, 0, 0])
        self.assertEqual(sp.expand(fundamental ** 2 - (1 + adjoint)), 0)

    def test_centered_relative_coupling_and_physical_units(self) -> None:
        x = sp.Symbol("x", real=True)
        lam, g, a = sp.symbols("lam g a", positive=True)
        characters = (2 * x, 4 * x ** 2 - 1)
        perturbation = sp.Matrix(2, 2, lambda i, j:
            -lam / 2 * haar_polynomial(characters[i] * (2 * x) * characters[j], x))
        self.assertEqual(perturbation, sp.Matrix([[0, -lam / 2], [-lam / 2, 0]]))
        inverse_sqrt_electric = sp.diag(sp.sqrt(Q(2, 3)), Q(1, 2))
        normalized = inverse_sqrt_electric * perturbation * inverse_sqrt_electric
        self.assertEqual(sp.simplify(normalized[0, 1] ** 2), lam ** 2 / 24)
        self.assertEqual(sp.simplify((lam ** 2 / 24).subs(lam, 4 / g ** 4)),
                         2 / (3 * g ** 8))
        ef, ea, w = 3 * g ** 2 / (2 * a), 4 * g ** 2 / a, -2 / (a * g ** 2)
        self.assertEqual(sp.simplify(w ** 2 / (ef * ea)), 2 / (3 * g ** 8))

    def test_no_nonempty_small_cycle_support_on_cube(self) -> None:
        # Only a finite graph control for the general leaf/girth proof in the note.
        vertices = tuple(product((0, 1), repeat=3))
        edges = tuple((u, v) for u, v in combinations(vertices, 2)
                      if sum(abs(x - y) for x, y in zip(u, v, strict=True)) == 1)
        self.assertEqual(len(edges), 12)
        admissible_counts = []
        for size in range(1, 5):
            count = 0
            for support in combinations(edges, size):
                degrees = {v: 0 for v in vertices}
                for u, v in support:
                    degrees[u] += 1
                    degrees[v] += 1
                if all(degree != 1 for degree in degrees.values()):
                    count += 1
            admissible_counts.append(count)
        self.assertEqual(admissible_counts, [0, 0, 0, 6])
        self.assertEqual(4 * Q(1, 2) * Q(1, 2) * Q(3, 2), Q(3, 2))

    def test_vacuum_residual_cannot_be_energy_relative(self) -> None:
        # Restrict to the constant and fundamental character on one plaquette.
        lam, epsilon = sp.symbols("lam epsilon", positive=True)
        electric = sp.diag(0, Q(3, 2))
        perturbation = sp.Matrix([[0, -lam / 2], [-lam / 2, 0]])
        f = sp.Matrix([1, epsilon])
        w_form = (f.T * perturbation * f)[0]
        e_form = (f.T * electric * f)[0]
        self.assertEqual(sp.factor(-w_form / e_form), 2 * lam / (3 * epsilon))
        self.assertEqual(perturbation * sp.Matrix([1, 0]), sp.Matrix([0, -lam / 2]))


    def test_trial_dressing_residual_and_derivative_factors(self) -> None:
        x, s, lam, u = sp.symbols("x s lam u", real=True)
        psi = sp.exp(2 * s * x)
        hpsi = -Q(1, 2) * ((1 - x ** 2) * sp.diff(psi, x, 2)
                           - 3 * x * sp.diff(psi, x)) + lam * (1 - x) * psi
        residual = sp.simplify(hpsi / psi).subs(x, u / 2)
        expected = s ** 2 * u ** 2 / 2 + (3 * s - lam) * u / 2 + lam - 2 * s ** 2
        self.assertEqual(sp.expand(residual - expected), 0)
        minus = 2 * s ** 2 + lam - 3 * s + (lam - 3 * s) ** 2 / (8 * s ** 2)
        plus = 2 * s ** 2 + 3 * s - lam + (3 * s - lam) ** 2 / (8 * s ** 2)
        self.assertEqual(sp.factor(4 * s ** 3 * sp.diff(minus, s)),
                         (4 * s ** 2 - lam) * (4 * s ** 2 - 3 * s + lam))
        self.assertEqual(sp.factor(4 * s ** 3 * sp.diff(plus, s)),
                         (4 * s ** 2 + lam) * (4 * s ** 2 + 3 * s - lam))

    def test_trial_residual_optimum_on_named_rational_grid(self) -> None:
        # Bounded controls only. The derivative proof covers all lambda >= 9/4.
        for lam in (Q(9, 4), Q(4), Q(9), Q(16), Q(25)):
            lower = 2 * lam - 3 * sp.sqrt(lam) + Q(9, 8)
            optimal = sp.sqrt(lam) / 2
            for s in (Q(n, 8) for n in range(65)):
                aa, bb, cc = s ** 2 / 2, (3 * s - lam) / 2, lam - 2 * s ** 2
                values = [aa * u ** 2 + bb * u + cc for u in (Q(-2), Q(2))]
                if aa > 0:
                    vertex = -bb / (2 * aa)
                    if -2 <= vertex <= 2:
                        values.append(aa * vertex ** 2 + bb * vertex + cc)
                oscillation = max(values) - min(values)
                self.assertGreaterEqual(oscillation, lower)
                if s == optimal:
                    self.assertEqual(oscillation, lower)


def main() -> int:
    result = unittest.TextTestRunner(verbosity=2).run(
        unittest.defaultTestLoader.loadTestsFromModule(__import__(__name__)))
    print(json.dumps({
        "python": platform.python_version(),
        "sympy": sp.__version__,
        "arithmetic": "exact rationals, radicals, polynomials; no float fits",
        "tests_run": result.testsRun,
        "all_passed": result.wasSuccessful(),
        "hidden_mode_parameter_cases": 12,
        "mixed_mode_parameter_cases": 12,
        "relative_form_scalar_cases": 24,
        "product_max_N": 34,
        "cube_edges": 12,
        "trial_couplings": ["9/4", "4", "9", "16", "25"],
        "trial_parameters_per_coupling": 65,
        "cube_support_sizes_tested": [1, 2, 3, 4],
        "SU2_relative_coefficient_squared": "lambda^2/24 = 2/(3*g^8)",
        "scope": "auxiliary checks, not continuum construction or formal verification"
    }, indent=2))
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    raise SystemExit(main())

"""Exact checks for two SU(2) plaquettes sharing a link and planar curl forms.

This script verifies polynomial identities and finite graph matrices. It does
not numerically certify a nonlinear spectral gap, a volume-uniform remainder,
or a Yang--Mills continuum limit. The separate U027 proof supplies the fixed-
graph harmonic-limit argument. Requires SymPy; all assertions use exact data.

Run: python checks/U027_shared_link_checks.py --output evidence/U027_checks.json
"""
from __future__ import annotations

import argparse
from functools import lru_cache
import hashlib
import json
from pathlib import Path
import platform
import time
import unittest

import sympy as sp

A, B, S = sp.symbols("a b s", real=True)
X = sp.symbols("x0:4", real=True)
Y = sp.symbols("y0:4", real=True)
DOT = sum(X[i] * Y[i] for i in range(1, 4))


def right_derivative(expr: sp.Expr, coords: tuple[sp.Symbol, ...], axis: int) -> sp.Expr:
    """Derivative along U exp(i t sigma_axis/2), with U=x0 I+i x.sigma."""
    if axis not in (1, 2, 3) or len(coords) != 4:
        raise ValueError("one quaternion and an axis in {1,2,3} required")
    value = -coords[axis] * sp.diff(expr, coords[0])
    value += coords[0] * sp.diff(expr, coords[axis])
    value -= sum(
        sp.LeviCivita(j - 1, k - 1, axis - 1) * coords[k]
        * sp.diff(expr, coords[j])
        for j in range(1, 4) for k in range(1, 4)
    )
    return sp.expand(value / 2)


def casimir(expr: sp.Expr, coords: tuple[sp.Symbol, ...]) -> sp.Expr:
    return sp.expand(-sum(right_derivative(right_derivative(expr, coords, i),
                                           coords, i) for i in range(1, 4)))


def kinetic_quaternion(expr: sp.Expr) -> sp.Expr:
    cross = sum(right_derivative(right_derivative(expr, Y, i), X, i)
                for i in range(1, 4))
    return sp.expand(2 * (casimir(expr, X) + casimir(expr, Y)) - cross)


def kinetic_invariants(expr: sp.Expr) -> sp.Expr:
    """Same operator in a=x0,b=y0,s=x.vector dot y.vector."""
    independent = -sp.Rational(1, 2) * (
        (1 - A**2) * sp.diff(expr, A, 2)
        + (1 - B**2) * sp.diff(expr, B, 2)
        + (2 - A**2 - B**2 - 2 * S**2) * sp.diff(expr, S, 2)
        - 2 * A * S * sp.diff(expr, A, S)
        - 2 * B * S * sp.diff(expr, B, S)
        - 3 * A * sp.diff(expr, A) - 3 * B * sp.diff(expr, B)
        - 6 * S * sp.diff(expr, S)
    )
    cross = -sp.Rational(1, 4) * (
        S * sp.diff(expr, A, B)
        - B * (1 - A**2) * sp.diff(expr, A, S)
        - A * (1 - B**2) * sp.diff(expr, B, S)
        + (A * B * S - (1 - A**2) * (1 - B**2) + S**2)
        * sp.diff(expr, S, 2) + (3 * A * B + 2 * S) * sp.diff(expr, S)
    )
    return sp.expand(independent + cross)


@lru_cache(maxsize=None)
def semicircle_moment(power: int) -> sp.Expr:
    if power < 0:
        raise ValueError("power must be nonnegative")
    if power % 2:
        return sp.S.Zero
    return sp.catalan(power // 2) / 4**(power // 2)


@lru_cache(maxsize=None)
def haar_monomial(p: int, q: int, r: int) -> sp.Expr:
    if min(p, q, r) < 0:
        raise ValueError("powers must be nonnegative")
    if r % 2:
        return sp.S.Zero
    k = r // 2
    left = sum((-1)**j * sp.binomial(k, j) * semicircle_moment(p + 2*j)
               for j in range(k + 1))
    right = sum((-1)**j * sp.binomial(k, j) * semicircle_moment(q + 2*j)
                for j in range(k + 1))
    return left * right / (r + 1)


def haar_mean(expr: sp.Expr) -> sp.Expr:
    return sp.expand(sum(coeff * haar_monomial(*powers)
                         for powers, coeff in sp.Poly(expr, A, B, S).terms()))


def invariant_monomials(degree: int) -> list[sp.Expr]:
    """Weighted degree: a and b have degree 1, s has degree 2."""
    return [A**p * B**q * S**r for p in range(degree + 1)
            for q in range(degree + 1) for r in range(degree // 2 + 1)
            if p + q + 2*r <= degree]


def rectangular_complex(nx: int, ny: int) -> tuple[sp.Matrix, sp.Matrix]:
    """Vertex-to-edge gradient and oriented edge-to-face curl on an open disk."""
    if nx < 1 or ny < 1:
        raise ValueError("positive cell counts required")
    vertices = [(i, j) for j in range(ny + 1) for i in range(nx + 1)]
    edges = [((i, j), (i + 1, j)) for j in range(ny + 1) for i in range(nx)]
    edges += [((i, j), (i, j + 1)) for j in range(ny) for i in range(nx + 1)]
    vi, ei = {v: k for k, v in enumerate(vertices)}, {e: k for k, e in enumerate(edges)}
    gradient = sp.zeros(len(edges), len(vertices))
    for k, (v, w) in enumerate(edges):
        gradient[k, vi[v]], gradient[k, vi[w]] = -1, 1
    curl = sp.zeros(nx * ny, len(edges))
    for j in range(ny):
        for i in range(nx):
            row = j * nx + i
            boundary = [(((i, j), (i + 1, j)), 1),
                        (((i + 1, j), (i + 1, j + 1)), 1),
                        (((i, j + 1), (i + 1, j + 1)), -1),
                        (((i, j), (i, j + 1)), -1)]
            for edge, sign in boundary:
                curl[row, ei[edge]] = sign
    return gradient, curl


def spin_energy(n1: int, n2: int, total: int) -> sp.Expr:
    """Exact electric energy; all spins are supplied as twice their value."""
    if min(n1, n2, total) < 0 or total not in range(abs(n1 - n2), n1 + n2 + 1, 2):
        raise ValueError("invalid SU(2) triangle or parity")
    return (3 * (n1 * (n1 + 2) + n2 * (n2 + 2)) + total * (total + 2)) / sp.Integer(8)


class SharedLinkTests(unittest.TestCase):
    def test_right_fields_and_casimir(self) -> None:
        for coords in (X, Y):
            sphere = sum(z*z for z in coords)
            for axis in range(1, 4):
                self.assertEqual(right_derivative(sphere, coords, axis), 0)
            for z in coords:
                self.assertEqual(casimir(z, coords), sp.Rational(3, 4) * z)

    def test_two_independent_differential_implementations(self) -> None:
        # This is a bounded implementation audit on 22 invariant monomials.
        variables = (X[3], Y[3], *X[:3], *Y[:3])
        constraints = [sum(t*t for t in X) - 1, sum(t*t for t in Y) - 1]
        for expr in invariant_monomials(4):
            full = expr.subs({A: X[0], B: Y[0], S: DOT})
            reduced = kinetic_invariants(expr).subs({A: X[0], B: Y[0], S: DOT})
            residual = sp.reduced(sp.expand(kinetic_quaternion(full) - reduced),
                                  constraints, *variables)[1]
            self.assertEqual(residual, 0, str(expr))

    def test_mixed_action_and_eigenfunctions(self) -> None:
        self.assertEqual(kinetic_invariants(A*B), 3*A*B-S/4)
        self.assertEqual(kinetic_invariants(S), sp.Rational(5, 2)*S-3*A*B/4)
        self.assertEqual(kinetic_invariants(A*B+S), sp.Rational(9, 4)*(A*B+S))
        self.assertEqual(kinetic_invariants(3*A*B-S), sp.Rational(13, 4)*(3*A*B-S))

    def test_haar_norms_and_symmetry(self) -> None:
        self.assertEqual(haar_mean(A**2*B**2), sp.Rational(1, 16))
        self.assertEqual(haar_mean(S**2), sp.Rational(3, 16))
        self.assertEqual(haar_mean(A*B*S), 0)
        basis = invariant_monomials(3)
        for u in basis:
            for v in basis:
                self.assertEqual(haar_mean(u*kinetic_invariants(v)
                                           - kinetic_invariants(u)*v), 0)

    def test_strict_failure_of_independent_kinetic_lower_bound(self) -> None:
        state = A*B+S
        self.assertEqual(haar_mean(state**2), sp.Rational(1, 4))
        self.assertEqual(haar_mean(state*(kinetic_invariants(state)-3*state)),
                         -sp.Rational(3, 16))

    def test_individual_trace_eigenstate_obstruction(self) -> None:
        f, g = sp.Function("f")(A), sp.Function("g")(B)
        independent = f+g
        lam, energy = sp.symbols("lam energy", nonzero=True)
        equation = kinetic_invariants(independent)+(lam*(2-A-B)-energy)*independent
        self.assertEqual(sp.simplify(sp.diff(equation, A, B)
                         + lam*(sp.diff(f, A)+sp.diff(g, B))), 0)
        c, d = sp.symbols("c d")
        affine = c*(A-B)+d
        result = sp.Poly(kinetic_invariants(affine)
                         +(lam*(2-A-B)-energy)*affine, A, B)
        self.assertEqual(result.coeff_monomial(A**2), -lam*c)
        self.assertEqual(result.coeff_monomial(A).subs(c, 0), -lam*d)

    def test_exact_spin_spectrum_and_controls(self) -> None:
        self.assertEqual(spin_energy(1, 0, 1), sp.Rational(3, 2))
        self.assertEqual(spin_energy(1, 1, 0), sp.Rational(9, 4))
        self.assertEqual(spin_energy(1, 1, 2), sp.Rational(13, 4))
        energies = [spin_energy(n1, n2, total)
                    for n1 in range(5) for n2 in range(5)
                    for total in range(abs(n1-n2), n1+n2+1, 2)]
        self.assertEqual(min(e for e in energies if e > 0), sp.Rational(3, 2))
        with self.assertRaises(ValueError):
            spin_energy(1, 1, 1)

    def test_graph_chain_condition_and_counts(self) -> None:
        for nx, ny in ((1, 1), (2, 1), (2, 2), (3, 2)):
            gradient, curl = rectangular_complex(nx, ny)
            self.assertEqual(curl*gradient, sp.zeros(nx*ny, (nx+1)*(ny+1)))
            self.assertEqual(curl.rank(), nx*ny)
            self.assertEqual(gradient.rows, nx*(ny+1)+ny*(nx+1))
            self.assertEqual(gradient.rows-gradient.cols+1, nx*ny)

    def test_gram_from_faces_and_expected_adjacency(self) -> None:
        for nx, ny in ((1, 1), (2, 1), (2, 2), (3, 2)):
            _, curl = rectangular_complex(nx, ny)
            gram = curl*curl.T
            for i in range(nx*ny):
                for j in range(nx*ny):
                    dist = abs(i % nx-j % nx)+abs(i // nx-j // nx)
                    target = 4 if i == j else (-1 if dist == 1 else 0)
                    self.assertEqual(gram[i, j], target)

    def test_two_square_metric_and_orientation(self) -> None:
        _, curl = rectangular_complex(2, 1)
        gram = curl*curl.T
        self.assertEqual(gram.eigenvals(), {sp.Integer(3): 1, sp.Integer(5): 1})
        flip = sp.diag(1, -1)
        self.assertEqual(flip*gram*flip/4,
                         sp.Matrix([[1, sp.Rational(1, 4)], [sp.Rational(1, 4), 1]]))
        _, square = rectangular_complex(2, 2)
        self.assertEqual((square*square.T).eigenvals(),
                         {sp.Integer(2): 1, sp.Integer(4): 2, sp.Integer(6): 1})

    def test_oscillator_ground_and_gap(self) -> None:
        z = sp.symbols("z0:6", real=True)
        m1, m2 = sp.Rational(3, 4), sp.Rational(5, 4)
        ground = sp.exp(-sum(t*t for t in z[:3])/(2*sp.sqrt(m1))
                        -sum(t*t for t in z[3:])/(2*sp.sqrt(m2)))
        e0 = sp.Rational(3, 2)*(sp.sqrt(m1)+sp.sqrt(m2))
        excited = (sum(t*t for t in z[:3])-sp.Rational(3, 2)*sp.sqrt(m1))*ground
        for state, energy in ((ground, e0), (excited, e0+2*sp.sqrt(m1))):
            applied = -sum((m1 if i < 3 else m2)*sp.diff(state, t, 2)/2
                           for i, t in enumerate(z)) + sum(t*t for t in z)*state/2
            self.assertEqual(sp.simplify(applied-energy*state), 0)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    start = time.perf_counter()
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(SharedLinkTests)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    report = {
        "status": "passed" if result.wasSuccessful() else "failed",
        "tests_run": result.testsRun,
        "python": platform.python_version(), "sympy": sp.__version__,
        "elapsed_seconds": time.perf_counter()-start,
        "arithmetic": "exact rational and symbolic algebra",
        "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "audit_bounds": {
            "invariant_monomial_degree": 4,
            "invariant_monomials_checked": len(invariant_monomials(4)),
            "haar_symmetry_degree": 3,
            "electric_spins_twice": "0..4 on each loop; every admissible total",
            "rectangles": [[1, 1], [2, 1], [2, 2], [3, 2]],
        },
        "exact_results": {
            "T_ab": str(kinetic_invariants(A*B)), "T_s": str(kinetic_invariants(S)),
            "mixed_norm_squared": str(haar_mean(S*S)),
            "electric_block_eigenvalues": ["9/4", "13/4"],
            "quadratic_metric_eigenvalues": ["3/4", "5/4"],
        },
        "analytic_results_proved_in_note_not_by_this_run": {
            "two_square_gap_over_sqrt_lambda_limit": "sqrt(3)",
            "two_square_a_times_physical_gap_limit": "2*sqrt(3)",
            "square_patch_curl_min_eigenvalue": "8*sin(pi/(2*(N+1)))**2",
        },
        "nonclaims": [
            "finite tests do not prove eigenvalue convergence",
            "no interval certificate for the nonlinear two-plaquette spectrum",
            "no graph-size-uniform weak-coupling remainder",
            "no continuum Yang--Mills mass-gap proof",
        ],
    }
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(report, indent=2)+"\n")
    print(json.dumps(report, indent=2))
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    raise SystemExit(main())

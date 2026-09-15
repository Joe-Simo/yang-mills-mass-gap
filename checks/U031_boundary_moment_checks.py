"""Exact finite audits for U031; none is a continuum Yang--Mills certificate.

Run: python checks/U031_boundary_moment_checks.py --output evidence/U031_checks.json
Arithmetic: SymPy exact rationals/polynomials; no fitted spectra or float tests.
The all-depth and all-parameter statements require the separate written proofs.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import platform
import time
import unittest

import sympy as sp

Q = sp.Rational
Matrix = sp.MutableDenseMatrix
MomentData = tuple[tuple[sp.Rational, ...], tuple[sp.Rational, ...]]


def walsh_basis() -> tuple[Matrix, Matrix, Matrix, Matrix]:
    return tuple(sp.Matrix(v) / 2 for v in (
        (1, 1, 1, 1), (1, 1, -1, -1),
        (1, -1, 1, -1), (1, -1, -1, 1),
    ))


def markov_family(epsilon: sp.Expr) -> Matrix:
    omega, u, v, w = walsh_basis()
    return (omega * omega.T + (u * u.T + w * w.T) / 4
            + (1 - epsilon) * v * v.T
            + epsilon * (u * v.T + v * u.T) / 4)


def moment_pair(order: int, slow: sp.Rational) -> tuple[MomentData, MomentData, sp.Rational]:
    """Two positive atomic measures agreeing through the given exact order."""
    if isinstance(order, bool) or not isinstance(order, int) or order < 0:
        raise ValueError("order must be a nonnegative integer")
    if not isinstance(slow, sp.Rational) or not Q(1, 2) < slow < 1:
        raise ValueError("slow must be rational and lie strictly in (1/2, 1)")
    nodes = tuple(Q(i + 1, 2 * (order + 2)) for i in range(order + 1))
    lagrange = tuple(sp.prod((slow - xj) / (xi - xj)
                            for j, xj in enumerate(nodes) if j != i)
                     for i, xi in enumerate(nodes))
    epsilon = sp.S.One / (2 * (order + 1) * (1 + max(abs(c) for c in lagrange)))
    base_weights = tuple(Q(1, order + 1) for _ in nodes)
    new_weights = tuple(w - epsilon * c for w, c in zip(base_weights, lagrange))
    return ((nodes, base_weights),
            (nodes + (slow,), new_weights + (epsilon,)), epsilon)


def moment(data: MomentData, degree: int) -> sp.Rational:
    nodes, weights = data
    return sum((w * x ** degree for x, w in zip(nodes, weights)), sp.S.Zero)


def hankel(data: MomentData, depth: int, shift: int = 0) -> Matrix:
    return sp.Matrix(depth + 1, depth + 1,
                     lambda i, j: moment(data, i + j + shift))


def all_principal_minors_nonnegative(a: Matrix) -> bool:
    """Exact PSD criterion used only for the small matrices in this file."""
    from itertools import combinations
    if a != a.T:
        return False
    return all(a.extract(ids, ids).det() >= 0
               for k in range(1, a.rows + 1)
               for ids in combinations(range(a.rows), k))


class BoundaryMomentTests(unittest.TestCase):
    def test_markov_formula_and_actual_conditional_expectation(self) -> None:
        e = sp.Symbol("e", real=True)
        omega, u, _, _ = walsh_basis()
        t = markov_family(e)
        explicit = sp.Matrix([
            [Q(5, 8)-e/8, e/4, Q(3, 8)-e/4, e/8],
            [e/4, Q(5, 8)-3*e/8, 3*e/8, Q(3, 8)-e/4],
            [Q(3, 8)-e/4, 3*e/8, Q(5, 8)-3*e/8, e/4],
            [e/8, Q(3, 8)-e/4, e/4, Q(5, 8)-e/8],
        ])
        self.assertEqual(sp.simplify(t - explicit), sp.zeros(4))
        self.assertEqual(t * sp.ones(4, 1), sp.ones(4, 1))
        p = omega * omega.T + u * u.T
        self.assertEqual(p, sp.diag(sp.ones(2)/2, sp.ones(2)/2))
        self.assertEqual(p * p, p)
        # Entrywise positivity for every 0<e<=1/4: t_ij-e/8 is affine,
        # nonnegative at both endpoints, hence everywhere in that interval.
        for value in t:
            for endpoint in (0, Q(1, 4)):
                self.assertGreaterEqual((value-e/8).subs(e, endpoint), 0)

    def test_parameter_uniform_positive_and_contracting_blocks(self) -> None:
        e, z = sp.symbols("e z", real=True)
        block = sp.Matrix([[Q(1, 4), e/4], [e/4, 1-e]])
        self.assertEqual(sp.factor(block.det() + (e*e + 4*e - 4)/16), 0)
        self.assertEqual(sp.factor((sp.eye(2)-block).det()-e*(12-e)/16), 0)
        # Exact interval lower bounds for the first determinant and positivity
        # of diagonal entries establish 0<block<I for the stated e range.
        self.assertEqual(block.det().subs(e, Q(1, 4)), Q(47, 256))
        self.assertEqual(sp.diff(block.det(), e), -e/8-Q(1, 4))
        polynomial = (z-1)*(4*z-1)*(-e**2+16*e*z-4*e+16*z**2-20*z+4)/64
        self.assertEqual(sp.factor((z*sp.eye(4)-markov_family(e)).det()-polynomial), 0)

    def test_memory_moments_and_small_total(self) -> None:
        e = sp.Symbol("e", positive=True)
        omega, u, v, _ = walsh_basis()
        t = markov_family(e)
        p = omega*omega.T + u*u.T
        q = sp.eye(4)-p
        for k in range(7):
            actual = (u.T * t * q * (q*t*q)**k * q*t*u)[0]
            self.assertEqual(sp.factor(actual-e**2*(1-e)**k/16), 0)
        self.assertEqual(sp.cancel((e**2/16)/(1-(1-e))), e/16)
        self.assertEqual(sp.factor((u.T*t**2*u)[0]-Q(1, 16)), e**2/16)
        self.assertEqual(sp.factor((q*t*u).dot(v)), e/4)
        # Discrete recurrence, not fitted data.
        for n in range(1, 7):
            rhs = (u.T*t**n*u)[0]/4 + sum(
                e**2*(1-e)**(n-1-j)*(u.T*t**j*u)[0]/16
                for j in range(n))
            self.assertEqual(sp.factor((u.T*t**(n+1)*u)[0]-rhs), 0)

    def test_gap_bounds_and_weighted_tail_control(self) -> None:
        e, z = sp.symbols("e z", real=True)
        a, d, b = Q(1, 4), 1-e, e/4
        poly = (z-a)*(z-d)-b*b
        self.assertEqual(sp.factor(poly.subs(z, d)), -e*e/16)
        at_upper = sp.factor(poly.subs(z, d+e*e/8))
        self.assertEqual(at_upper, e*e*(e*e-8*e+2)/64)
        # e^2-8e+2 >= 1/16 on [0,1/4], decreasing there.
        self.assertEqual((e*e-8*e+2).subs(e, Q(1, 4)), Q(1, 16))
        self.assertGreaterEqual(Q(1, 4)-Q(1, 4)**2/8, 0)
        for eps in (Q(1, 4), Q(1, 16), Q(1, 256)):
            slow = 1-eps
            q = Q(1, 2)
            self.assertGreater(slow/q, 1)  # weighted memory cannot decay at q
            self.assertLessEqual(eps/16, Q(1, 64))

    def test_exact_rank_stabilization_detects_visible_slow_mode(self) -> None:
        t = markov_family(Q(1, 16))
        _, u, _, _ = walsh_basis()
        x0 = u
        x1 = u.row_join(t*u)
        x2 = x1.row_join(t*t*u)
        self.assertEqual([x0.rank(), x1.rank(), x2.rank()], [1, 2, 2])
        h, k = x1.T*x1, x1.T*t*x1
        z = sp.Symbol("z")
        expected = sp.Matrix([[Q(1, 4), Q(1, 64)], [Q(1, 64), Q(15, 16)]])
        self.assertEqual(sp.factor((k-z*h).det()/h.det()
                                   -(expected-z*sp.eye(2)).det()), 0)
        self.assertEqual(t*x1, x1*(h.inv()*k))

    def test_positive_atomic_moment_matching(self) -> None:
        for order in (0, 1, 3, 5, 9):
            for slow in (Q(3, 4), Q(63, 64)):
                base, changed, epsilon = moment_pair(order, slow)
                self.assertGreater(epsilon, 0)
                self.assertEqual(sum(changed[1]), 1)
                self.assertTrue(all(w > 0 for w in changed[1]))
                self.assertTrue(all(isinstance(w, sp.Rational) for w in changed[1]))
                self.assertLess(max(base[0]), Q(1, 2))
                self.assertEqual(max(changed[0]), slow)
                for k in range(order+1):
                    self.assertEqual(moment(base, k), moment(changed, k))
                # Independent Vandermonde cyclicity test in weighted L2.
                nodes = changed[0]
                vandermonde = sp.Matrix([[x**k for k in range(len(nodes))] for x in nodes])
                self.assertNotEqual(vandermonde.det(), 0)

    def test_finite_hankel_and_shifted_forms_are_identical(self) -> None:
        for depth in range(4):
            base, changed, _ = moment_pair(2*depth+1, Q(255, 256))
            h0, h1 = hankel(base, depth), hankel(changed, depth)
            k0, k1 = hankel(base, depth, 1), hankel(changed, depth, 1)
            self.assertEqual(h0, h1)
            self.assertEqual(k0, k1)
            self.assertTrue(all_principal_minors_nonnegative(h0/2-k0))
            self.assertGreater(h0.det(), 0)

    def test_higher_degree_polynomial_exposes_missing_atom(self) -> None:
        z = sp.Symbol("z")
        for order in (0, 1, 3, 5):
            base, changed, epsilon = moment_pair(order, Q(63, 64))
            slow = changed[0][-1]
            poly = sp.prod(z-x for x in base[0])
            localizer = sum(w*(Q(1, 2)-x)*poly.subs(z, x)**2
                            for x, w in zip(*changed))
            exact = epsilon*(Q(1, 2)-slow)*poly.subs(z, slow)**2
            self.assertEqual(localizer, exact)
            self.assertLess(localizer, 0)
            self.assertEqual(sum(w*poly.subs(z, x)**2 for x, w in zip(*base)), 0)

    def test_block_hankel_factorization_including_null_space(self) -> None:
        t = sp.Matrix([[Q(1, 4), Q(1, 16), 0],
                       [Q(1, 16), Q(1, 2), Q(1, 16)],
                       [0, Q(1, 16), Q(3, 4)]])
        j = sp.eye(3)[:, :2]
        depth = 2
        moments = [j.T*t**k*j for k in range(2*depth+2)]
        h = sp.BlockMatrix([[moments[i+k] for k in range(depth+1)]
                            for i in range(depth+1)]).as_explicit()
        k = sp.BlockMatrix([[moments[i+k+1] for k in range(depth+1)]
                            for i in range(depth+1)]).as_explicit()
        x = sp.Matrix.hstack(*(t**k*j for k in range(depth+1)))
        self.assertEqual(h, x.T*x)
        self.assertEqual(k, x.T*t*x)
        self.assertEqual(h.rank(), 3)
        self.assertEqual(h.det(), 0)  # no invalid inversion of the Hankel matrix
        # Reconstruct noncommuting matrix memory kernels from retained moments.
        kernels = []
        a, b, d = t[:2, :2], t[:2, 2:], t[2:, 2:]
        for n in range(4):
            recovered = moments[n+2] - a*moments[n+1]
            for ell in range(1, n+1):
                recovered -= kernels[n-ell]*moments[ell]
            kernels.append(recovered)
            self.assertEqual(recovered, b*d**n*b.T)
        self.assertTrue(all_principal_minors_nonnegative(t))
        self.assertTrue(all_principal_minors_nonnegative(sp.eye(3)-t))

    def test_weighted_memory_certificate_and_cyclicity(self) -> None:
        a, r, c, q = Q(1, 4), Q(1, 2), Q(1, 128), Q(3, 4)
        b = sp.Matrix([[Q(1, 16), Q(1, 16)]])
        d = sp.diag(Q(1, 4), Q(1, 2))
        s = sp.BlockMatrix([[sp.Matrix([[a]]), b], [b.T, d]]).as_explicit()
        self.assertEqual(sp.Matrix.hstack(b.T, d*b.T).rank(), 2)
        self.assertEqual((b*b.T)[0], c)
        for k in range(12):
            self.assertLessEqual((b*d**k*b.T)[0], c*r**k)
        exact_memory = (b*(q*sp.eye(2)-d).inv()*b.T)[0]
        self.assertLessEqual(exact_memory, c/(q-r))
        self.assertLessEqual(c, (q-a)*(q-r))
        self.assertTrue(all_principal_minors_nonnegative(s))
        self.assertTrue(all_principal_minors_nonnegative(q*sp.eye(3)-s))

    def test_no_strict_discarded_separation_infinite_model_controls(self) -> None:
        # These finite prefixes audit the formulas; the all-tail bound is proved
        # separately by sum n^-2<=2 and a Bernoulli inequality.
        q, a = Q(3, 4), Q(1, 4)
        nodes = [q-Q(1, 4*n) for n in range(1, 9)]
        b = sp.Matrix([[Q(1, 8*n*n) for n in range(1, 9)]])
        d = sp.diag(*nodes)
        self.assertLess((b*d.inv()*b.T)[0], Q(1, 24))
        self.assertLess((b*(q*sp.eye(8)-d).inv()*b.T)[0], Q(3, 32))
        self.assertLess(Q(3, 32), q-a)
        for m in range(11):
            tail_prefix = sum(Q(1, 16*n**3)*(1-Q(1, 3*n))**(m+1)
                              for n in range(1, 9))
            self.assertLess(tail_prefix, Q(3, 8*(m+1)))
            for n in range(1, 9):
                self.assertLessEqual((1-Q(1, 3*n))**(m+1),
                                     1/(1+Q(m+1, 3*n)))

    def test_dark_sector_and_invalid_inputs_are_not_silently_accepted(self) -> None:
        # Vanishing observable memory cannot see a disconnected slow sector.
        s = sp.diag(Q(1, 4), Q(1, 4), Q(63, 64))
        p = sp.diag(1, 0, 0)
        self.assertEqual((sp.eye(3)-p)*s*p, sp.zeros(3))
        self.assertGreater(s[2, 2], Q(3, 4))
        for order, slow in ((-1, Q(3, 4)), (True, Q(3, 4)),
                            (2, Q(1, 2)), (2, Q(1)), (2, 0.75)):
            with self.assertRaises(ValueError):
                moment_pair(order, slow)

    def test_positive_kernel_ground_state_minorization(self) -> None:
        psi, v = sp.Matrix([Q(3, 5), Q(4, 5)]), sp.Matrix([Q(4, 5), -Q(3, 5)])
        t = psi*psi.T + v*v.T/4
        kernel = 2*t  # reference measure is uniform on the two points
        lower, upper = min(kernel), max(kernel)
        eta = (lower/upper)**2
        self.assertEqual(t*psi, psi)
        pi = sp.diag(*(value**2 for value in psi))
        transition = sp.diag(*(1/value for value in psi))*t*sp.diag(*psi)
        self.assertEqual(transition*sp.ones(2, 1), sp.ones(2, 1))
        self.assertEqual(pi*transition, transition.T*pi)
        for i in range(2):
            for j in range(2):
                self.assertGreaterEqual(transition[i, j]/pi[j, j], eta)
        self.assertEqual(eta, Q(1296, 5329))
        self.assertGreaterEqual(Q(3, 4), eta)  # actual transfer deficit = 3/4


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    start = time.perf_counter()
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(BoundaryMomentTests)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    sample_base, sample_changed, sample_weight = moment_pair(3, Q(63, 64))
    output = {
        "status": "passed" if result.wasSuccessful() else "failed",
        "tests_run": result.testsRun,
        "seconds": time.perf_counter()-start,
        "python": platform.python_version(), "sympy": sp.__version__,
        "arithmetic": "exact rationals and symbolic polynomials; no floating decisions",
        "seed": None,
        "scopes": {
            "markov_parameter": "written proof: every 0<epsilon<=1/4; symbolic identities audited",
            "recurrence_powers": [1, 2, 3, 4, 5, 6],
            "moment_orders": [0, 1, 3, 5, 9],
            "moment_slow_nodes": ["3/4", "63/64"],
            "matching_hankel_depths": [0, 1, 2, 3],
            "weighted_memory_test_powers": list(range(12)),
            "boundary_infinite_model_prefix": {"nodes": 8, "tail_depths": list(range(11))},
        },
        "sample_same_first_four_moments": {
            "base_nodes": list(map(str, sample_base[0])),
            "base_weights": list(map(str, sample_base[1])),
            "changed_nodes": list(map(str, sample_changed[0])),
            "changed_weights": list(map(str, sample_changed[1])),
            "added_slow_weight": str(sample_weight),
            "moments_degree_0_through_3": [str(moment(sample_base, k)) for k in range(4)],
        },
        "nonclaims": [
            "Finite checks are not proof of all-depth identities or universal parameter claims.",
            "The measures and Markov matrices are auxiliary models, not Wilson transfer data.",
            "No continuum Yang--Mills mass, many-block bound, or formal proof is certified.",
        ],
    }
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(output, indent=2)+"\n", encoding="utf-8")
    print(json.dumps(output, indent=2))
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    raise SystemExit(main())

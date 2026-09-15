"""Exact finite checks for U035, not a continuum Yang--Mills certificate.

Run: python checks/U035_vacuum_cycle_response_checks.py --output evidence/U035_checks.json
SU(2) response coefficients are enclosed with complete positive-series tails.
The four-state and exponential-tilt fixtures audit identities, not Wilson data.
All universal operator, source-support and analyticity claims have written proofs.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
from itertools import product
import json
from pathlib import Path
import platform
import time
import unittest

import sympy as sp

from U029_exact_link_integration_checks import outward_decimal, periodic_faces
from U030_overlap_and_transfer_checks import character_ratio
from U032_conditional_memory_checks import tilted_transfer
from U034_history_variance_and_cycle_checks import conditional_projection

R = sp.Rational
Interval = tuple[Q, Q]


def add(a: Interval, b: Interval) -> Interval:
    return a[0]+b[0], a[1]+b[1]


def neg(a: Interval) -> Interval:
    return -a[1], -a[0]


def mul(a: Interval, b: Interval) -> Interval:
    ends = tuple(x*y for x in a for y in b)
    return min(ends), max(ends)


def div(a: Interval, b: Interval) -> Interval:
    if b[0] <= 0 <= b[1]:
        raise ValueError('divisor interval contains zero')
    return mul(a, (1/b[1], 1/b[0]))


def point(x: Q | int) -> Interval:
    return Q(x), Q(x)


def positive_power(a: Interval, exponent: int) -> Interval:
    if a[0] < 0 or exponent < 0:
        raise ValueError('nonnegative interval and exponent required')
    return a[0]**exponent, a[1]**exponent


def coefficient_certificate(beta: Q) -> dict[str, object]:
    """Full-tail intervals for Taylor DERIVATIVES at zero spatial coupling."""
    if beta < 0:
        raise ValueError('beta_t must be nonnegative')
    r = character_ratio(beta, 1, 52)
    u = character_ratio(beta, 2, 52)
    c = positive_power(r, 4)
    z0 = positive_power(r, 6)
    z1 = mul(z0, u)
    one = point(1)
    dc = add(one, neg(c))
    b: list[Interval] = []
    for z in (z0, z1):
        num = add(z, neg(positive_power(c, 2)))
        den = mul(positive_power(dc, 2), add(one, neg(z)))
        b.append(div(num, den))
    a_score = div(add(one, c), dc)
    orient = mul(point(Q(3, 32)), add(b[0], neg(b[1])))
    trace_cov = mul(point(Q(1, 32)), add(b[0], mul(point(3), b[1])))
    quantities = {'r_fundamental': r, 'r_adjoint': u, 'one_cycle_score': a_score,
                  'b_perimeter': b[0], 'b_adjoint_shared': b[1],
                  'mixed_orientation_expectation_derivative': orient,
                  'mixed_trace_covariance_derivative': trace_cov}
    for name, (lo, hi) in quantities.items():
        if lo > hi or hi-lo >= Q(1, 10**26):
            raise AssertionError(f'{name}: interval accuracy contract failed')
    if beta > 0 and orient[0] <= 0:
        raise AssertionError('positive mixed orientation response was not certified')
    return {'beta_t': str(beta),
            'intervals': {name: [outward_decimal(lo, 22, False),
                                 outward_decimal(hi, 22, True)]
                          for name, (lo, hi) in quantities.items()},
            'arithmetic': 'exact rational tails and interval operations; outward decimal display',
            'scope': 'derivatives at beta_s=0, not finite-beta_s values or mass gaps'}


def stationary_response(k: sp.MatrixBase, pi: sp.MatrixBase,
                        observable: sp.MatrixBase) -> tuple[sp.MatrixBase, sp.MatrixBase]:
    """Score of the actual Perron vacuum under symmetric multiplication tilt."""
    size = len(pi)
    if k.shape != (size, size) or observable.shape != (size, 1):
        raise ValueError('square Markov matrix and matching columns required')
    one = sp.ones(size, 1)
    center = one*pi.T
    centered = observable-one*(pi.T*observable)[0]
    h = (sp.eye(size)-k+center).inv()*(sp.eye(size)+k)*centered/2
    return h, 2*h


class ResponseTests(unittest.TestCase):
    def test_exact_source_equations_and_logarithm_subtraction(self) -> None:
        c, z = sp.symbols('c z')
        first = (1+c)/(2*(1-c))
        raw = (1+3*c+(3+c)*z)/(4*(1-c)*(1-z))
        rhs = first*c+(1+2*c)/4+(first+R(1, 4))*z
        self.assertEqual(sp.factor((1-z)*raw-rhs), 0)
        connected = (z-c*c)/((1-c)**2*(1-z))
        self.assertEqual(sp.factor(raw-first**2-connected), 0)
        self.assertEqual(sp.factor(connected.subs(z, c*c)), 0)
        self.assertEqual(sp.factor((1-c)*first-(1+c)/2), 0)

    def test_shared_noise_matrix_and_complete_two_channel_eigenvectors(self) -> None:
        r, u = sp.symbols('r u')
        # E h0^2=(1+3u)/4, E hi hj=(1-u)delta_ij/4.
        cmat = r**6*sp.Matrix([[1+3*u, 3*(1-u)], [1-u, 3+u]])/4
        gram = sp.diag(R(1, 16), R(3, 16))
        v0, v1 = sp.Matrix([1, 1]), sp.Matrix([3, -1])
        self.assertEqual(sp.simplify(cmat*v0-r**6*v0), sp.zeros(2, 1))
        self.assertEqual(sp.simplify(cmat*v1-r**6*u*v1), sp.zeros(2, 1))
        self.assertEqual(sp.simplify(gram*cmat-cmat.T*gram), sp.zeros(2))
        self.assertEqual((v0.T*gram*v1)[0], 0)
        self.assertEqual((v0.T*gram*v0)[0], R(1, 4))
        self.assertEqual((v1.T*gram*v1)[0], R(3, 4))
        self.assertEqual((v0+v1)/4, sp.Matrix([1, 0]))

    def test_haar_moments_and_mixed_physical_responses(self) -> None:
        b0, b1, a = sp.symbols('b0 b1 a')
        gram = sp.diag(R(1, 16), R(3, 16))
        f, orient = sp.Matrix([1, 0]), sp.Matrix([0, 1])
        log_score = (b0*sp.Matrix([1, 1])+b1*sp.Matrix([3, -1]))/2
        pi_mixed = log_score+4*a*a*f
        self.assertEqual(sp.expand((orient.T*gram*pi_mixed)[0]), 3*(b0-b1)/32)
        connected_cov = (f.T*gram*pi_mixed)[0] - a*a/4
        self.assertEqual(sp.expand(connected_cov), (b0+3*b1)/32)
        # Each single trace has variance 1/4; standardized covariance gains 4.
        self.assertEqual(sp.expand(4*connected_cov), (b0+3*b1)/8)

    def test_common_source_difference_and_positivity_identity(self) -> None:
        c, z0, z1 = sp.symbols('c z0 z1')
        b = lambda z: (z-c*c)/((1-c)**2*(1-z))
        factored = (1+c)*(z0-z1)/((1-c)*(1-z0)*(1-z1))
        self.assertEqual(sp.factor(b(z0)-b(z1)-factored), 0)
        # Exact nonzero witness to reject a product of two separate class laws.
        self.assertGreater(factored.subs({c: R(1, 16), z0: R(1, 64), z1: R(1, 256)}), 0)

    def test_large_beta_coefficients(self) -> None:
        x = sp.symbols('x', positive=True)
        # Fixed-order Bessel asymptotic input; not a fitted expansion.
        r = 1-R(3, 2)*x+R(3, 8)*x*x
        u = 1-4*x+6*x*x
        c = r**4
        z0, z1 = r**6, r**6*u
        b0 = (z0-c*c)/((1-c)**2*(1-z0))
        b1 = (z1-c*c)/((1-c)**2*(1-z1))
        checks = ((b0, R(1, 108)), (b1, -R(1, 468)),
                  (3*(b0-b1)/32, R(1, 936)),
                  ((b0+3*b1)/32, R(1, 11232)))
        for expression, expected in checks:
            self.assertEqual(sp.limit(x*x*expression, x, 0), expected)

    def test_actual_weighted_vacuum_score_identity(self) -> None:
        k, pi, gram = tilted_transfer((1, 2, 3, 5))
        w = sp.Matrix([R(1, 2), -R(2, 3), R(1, 3), -R(1, 4)])
        one = sp.ones(4, 1)
        mean = (pi.T*w)[0]
        h, score = stationary_response(k, pi, w)
        tprime = (sp.diag(*w)*k+k*sp.diag(*w))/2
        self.assertEqual((sp.eye(4)-k)*h-(tprime*one-mean*one), sp.zeros(4, 1))
        self.assertEqual((pi.T*score)[0], 0)
        kprime = -mean*k-sp.diag(*h)*k+tprime+k*sp.diag(*h)
        piprime = 2*gram*h
        self.assertEqual(kprime*one, sp.zeros(4, 1))
        self.assertEqual(piprime.T*k+pi.T*kprime-piprime.T, sp.zeros(1, 4))
        self.assertEqual(sp.diag(*piprime)*k+gram*kprime-
                         (sp.diag(*piprime)*k+gram*kprime).T, sp.zeros(4))

    def test_conditional_variance_derivative_keeps_projection_response(self) -> None:
        # Exact two-parameter change of one probability, not a Wilson replacement.
        s, t = sp.symbols('s t')
        base = sp.Matrix([R(1, 10), R(2, 10), R(3, 10), R(4, 10)])
        a, b = sp.Matrix([1, -1, 2, 0]), sp.Matrix([0, 2, -1, 1])
        f = sp.Matrix([2, -1, 3, 0])
        raw = sp.Matrix([base[i]*(1+s*a[i])*(1+t*b[i]) for i in range(4)])
        law = raw/sum(raw)
        p0 = conditional_projection(base, (0, 0, 1, 1))
        h = f-p0*f
        sa = a-sp.ones(4, 1)*(base.T*a)[0]
        sb = b-sp.ones(4, 1)*(base.T*b)[0]
        sab = -(sa.T*sp.diag(*base)*sb)[0]
        variance = 0
        for ids in ((0, 1), (2, 3)):
            mass = sum(law[i] for i in ids)
            mean = sum(law[i]*f[i] for i in ids)/mass
            variance += sum(law[i]*(f[i]-mean)**2 for i in ids)
        first = sum(base[i]*sa[i]*h[i]**2 for i in range(4))
        pa = p0*sp.diag(*sa)*h
        pb = p0*sp.diag(*sb)*h
        second = sum(base[i]*(sa[i]*sb[i]+sab)*h[i]**2 for i in range(4))
        second -= 2*(pa.T*sp.diag(*base)*pb)[0]
        self.assertEqual(sp.simplify(sp.diff(variance, s).subs({s:0,t:0})-first), 0)
        self.assertEqual(sp.simplify(sp.diff(variance, s, t).subs({s:0,t:0})-second), 0)
        self.assertNotEqual((pa.T*sp.diag(*base)*pb)[0], 0)

    def test_stationary_path_score_and_endpoint_vacuum_terms(self) -> None:
        k, pi, _ = tilted_transfer((1, 2, 3, 5))
        w = sp.Matrix([1, -1, R(1, 2), -R(1, 3)])
        mean = (pi.T*w)[0]
        h, _ = stationary_response(k, pi, w)
        f = sp.Matrix([2, 0, -1, 1])
        for n in (1, 2, 3):
            score_mean, response = R(0), R(0)
            for path in product(range(4), repeat=n+1):
                mass = pi[path[0]]
                for j in range(n):
                    mass *= k[path[j], path[j+1]]
                path_score = h[path[0]]+h[path[-1]]
                path_score += (w[path[0]]+w[path[-1]])/2
                path_score += sum((w[path[j]] for j in range(1,n)), R(0))-n*mean
                score_mean += mass*path_score
                response += mass*path_score*f[path[0]]
            self.assertEqual(score_mean, 0)
            self.assertEqual(response, 2*(f.T*sp.diag(*pi)*h)[0])

    def test_riesz_contour_constants_and_bivariate_tail(self) -> None:
        d, x = sp.symbols('d x', positive=True)
        delta = d/10
        self.assertEqual(sp.simplify(delta/(d/2-delta)), R(1, 4))
        self.assertEqual((1+R(1, 4))**2/(1-R(1, 4)), R(25, 12))
        series = 1/(1-x)**2 - 1 - 2*x - 3*x*x
        self.assertEqual(sp.factor(series-x**3*(4-3*x)/(1-x)**2), 0)
        self.assertEqual(sp.factor(1-((1-d)+delta)/(1-delta)-(d-2*delta)/(1-delta)), 0)

    def test_actual_periodic_shared_and_disjoint_plaquette_geometry(self) -> None:
        for n in (4, 6):
            faces = list(periodic_faces(3, n))
            p = set(faces[0])
            shared = next(set(q) for q in faces if len(p.intersection(q)) == 1)
            disjoint = next(set(q) for q in faces if not p.intersection(q))
            self.assertEqual(len(p.union(shared)), 7)
            self.assertEqual(len(p.union(disjoint)), 8)
            self.assertEqual(len(faces), 3*n**3)

    def test_complete_positive_series_coefficients(self) -> None:
        for beta in (Q(0), Q(1,2), Q(2), Q(8), Q(32), Q(128)):
            coefficient_certificate(beta)

    def test_invalid_interval_and_coupling_controls(self) -> None:
        with self.assertRaises(ValueError):
            div(point(1), (Q(-1), Q(1)))
        with self.assertRaises(ValueError):
            coefficient_certificate(Q(-1))
        with self.assertRaises(ValueError):
            positive_power((Q(-1), Q(2)), 2)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    start = time.perf_counter()
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(ResponseTests)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    evidence = {'status': 'passed' if result.wasSuccessful() else 'failed',
                'tests_run': result.testsRun, 'seconds': time.perf_counter()-start,
                'python': platform.python_version(), 'sympy': sp.__version__,
                'arithmetic': 'exact rational/symbolic decisions and complete positive-series tails',
                'seed': None, 'max_fixture_paths': 256,
                'certificates': [coefficient_certificate(b) for b in (Q(0),Q(1,2),Q(2),Q(8),Q(32),Q(128))],
                'nonclaims': ['No numerical vacuum eigenvector is substituted.',
                              'No four-dimensional continuum or uniform interacting-volume gap.',
                              'Finite Markov fixtures do not constitute Wilson simulations.',
                              'Taylor response is at zero spatial coupling with arbitrary finite temporal coupling.']}
    text = json.dumps(evidence, indent=2)+'\n'
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text)
    print(text)
    return 0 if result.wasSuccessful() else 1


if __name__ == '__main__':
    raise SystemExit(main())

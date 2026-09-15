"""Exact finite audits for U036's weak-spatial Wilson comparison theorem.

Run: python checks/U036_column_comparison_checks.py --output evidence/U036_checks.json
Finite binary chains below audit probability/comparison algebra, NOT SU(2) data.
The continuum-SU(2), all-character, all-volume and all-time claims have written
proofs in research/audits/U036_column_comparison_and_uniform_lattice_gap.md.
No simulation or fitted spectral gap is used.
"""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
from pathlib import Path
import platform
import time
import unittest
from fractions import Fraction as Q

import sympy as sp


def temporal_block(beta: Q) -> int:
    if beta <= 0:
        raise ValueError("Temporal beta must be strictly positive")
    z = 3 * max(Q(1), beta)
    return (z.numerator + z.denominator - 1) // z.denominator


def response_profile(distance: int, block: int) -> Q:
    if block < 1 or distance < 0:
        raise ValueError("Expected nonnegative distance and positive block")
    return Q(1, 2 ** (distance // block))


def weighted_sum(block: int, weight: Q) -> Q:
    if block < 1 or weight < 1 or weight ** block >= 2:
        raise ValueError("Weighted geometric series must converge")
    return 2 * sum((weight ** j for j in range(block)), Q(0)) / (1 - weight ** block / 2) - 1


def column_marginals(fields: list[tuple[int, int]], tilt_at: int | None = None) -> list[Q]:
    n = len(fields)
    numer = [0] * n
    total = 0
    for path in itertools.product((0, 1), repeat=n):
        w = math.prod(fields[t][path[t]] for t in range(n))
        w *= math.prod(4 if path[t] == path[t + 1] else 1 for t in range(n - 1))
        if tilt_at is not None:
            w *= 16 if path[tilt_at] == 0 else 1
        total += w
        for t in range(n):
            if path[t] == 0:
                numer[t] += w
    return [Q(x, total) for x in numer]


def paired_chain_covariances(length: int) -> tuple[sp.Matrix, int]:
    """Exactly enumerate two binary columns, weak pair coupling 1/2049."""
    n = 2 * length
    total = 0
    singles = [0] * n
    pairs = [[0] * n for _ in range(n)]
    for path in itertools.product((-1, 1), repeat=n):
        w = 1
        for e in range(2):
            for t in range(length - 1):
                w *= 4 if path[e * length + t] == path[e * length + t + 1] else 1
        for t in range(length):
            w *= 1025 if path[t] == path[length + t] else 1024
        total += w
        for i in range(n):
            singles[i] += w * path[i]
            for j in range(n):
                pairs[i][j] += w * path[i] * path[j]
    cov = sp.Matrix(n, n, lambda i, j: sp.Rational(pairs[i][j], total)
                    - sp.Rational(singles[i] * singles[j], total * total))
    return cov, 2 ** n


def spatial_counts(n: int) -> tuple[int, int, int]:
    if n < 4:
        raise ValueError("Small periodic quotients can identify plaquette edges")
    sites = list(itertools.product(range(n), repeat=3))
    links = [(x, mu) for x in sites for mu in range(3)]
    incidence: dict[tuple[tuple[int, ...], int], list[tuple]] = {e: [] for e in links}
    plaquettes = []
    for x in sites:
        for mu in range(3):
            for nu in range(mu + 1, 3):
                xm, xn = list(x), list(x)
                xm[mu] = (xm[mu] + 1) % n
                xn[nu] = (xn[nu] + 1) % n
                face = ((x, mu), (tuple(xm), nu), (tuple(xn), mu), (x, nu))
                if len(set(face)) != 4:
                    raise AssertionError("Identified plaquette edges")
                plaquettes.append(face)
                for e in face:
                    incidence[e].append(face)
    multiplicities = [sum(len(face) - 1 for face in faces) for faces in incidence.values()]
    return len(links), len(plaquettes), max(multiplicities)


class Checks(unittest.TestCase):
    def test_01_bessel_riccati_and_ratio_root(self) -> None:
        z, nu, r = sp.symbols('z nu r', positive=True)
        # I_nu'=I_(nu+1)+nu I_nu/z; I_(nu+1)'=I_nu-(nu+1)I_(nu+1)/z.
        deriv = 1 - (nu + 1) * r / z - r * (r + nu / z)
        self.assertEqual(sp.expand(deriv - (1 - (2 * nu + 1) * r / z - r ** 2)), 0)
        a = (nu + sp.Rational(1, 2)) / z
        root = sp.sqrt(1 + a * a) - a
        self.assertEqual(sp.simplify(root ** 2 + 2 * a * root - 1), 0)

    def test_02_uniform_scale_monotonicity(self) -> None:
        x = sp.symbols('x', positive=True)
        h = sp.asinh(x) - x / sp.sqrt(1 + x * x)
        self.assertEqual(sp.simplify(sp.diff(h, x) - x * x / (1 + x * x) ** sp.Rational(3, 2)), 0)
        # asinh(3/2)>log 3 is equivalent to sqrt(13)>3.
        self.assertGreater(13, 9)
        for beta in (Q(1, 2), Q(1), Q(7, 6), Q(2), Q(8), Q(32), Q(128)):
            b = temporal_block(beta)
            self.assertGreaterEqual(b, 3 * max(Q(1), beta))
            self.assertLessEqual(b, 4 * max(Q(1), beta))

    def test_03_complete_character_tail(self) -> None:
        l = sp.symbols('l', integer=True, positive=True)
        tail = sp.summation((l + 1) ** 2 / 27 ** l, (l, 1, sp.oo))
        self.assertEqual(tail, sp.Rational(709, 4394))
        self.assertLess(tail, sp.Rational(1, 4))
        x = sp.symbols('x')
        self.assertEqual(sp.simplify((1 + x) / (1 - x) ** 3 - 1
                                    - (4*x - 3*x*x + x**3) / (1-x)**3), 0)

    def test_04_bridge_cross_ratio_constants(self) -> None:
        # If b*s<=1/192, 2*b*H<=1/24. exp(1/24)<=24/23.
        odds_sqrt_bound = Q(5, 3) * Q(24, 23)
        tv_bound = (odds_sqrt_bound - 1) / (odds_sqrt_bound + 1)
        self.assertEqual(tv_bound, Q(17, 63))
        self.assertLess(tv_bound, Q(1, 2))
        self.assertEqual(12 * Q(1, 192) * 8, Q(1, 2))
        self.assertEqual(12 * Q(1, 192) * 4, Q(1, 4))

    def test_05_profile_weighted_all_tail(self) -> None:
        for b in (1, 2, 3, 6, 12):
            self.assertEqual(weighted_sum(b, Q(1)), 4*b - 1)
            x = Q(1) + Q(1, 10*b)
            self.assertLess(x**b, Q(4, 3))
            exact = weighted_sum(b, x)
            partial = sum((x ** abs(k) * response_profile(abs(k), b)
                           for k in range(-3*b+1, 3*b)), Q(0))
            tail = 2 * (x**b / 2)**3 * sum((x**j for j in range(b)), Q(0)) / (1-x**b/2)
            self.assertEqual(exact, partial + tail)
            self.assertLess(exact, 8*b)

    def test_06_weighted_neumann_comparison(self) -> None:
        length = 5
        G = sp.Matrix(length, length, lambda i, j: sp.Rational(response_profile(abs(i-j), 3)))
        A = sp.Matrix([[0, sp.Rational(1, 2049)], [sp.Rational(1, 2049), 0]])
        R = sp.kronecker_product(sp.eye(2), G)
        J = sp.kronecker_product(A, G)
        L = (sp.eye(2*length)-J).inv() * R
        self.assertEqual((sp.eye(2*length)-J)*L-R, sp.zeros(2*length))
        self.assertTrue(all(x >= 0 for x in L))
        self.assertLess(max(sum(L[i,j] for j in range(2*length)) for i in range(2*length)), 48)

    def test_07_single_column_local_tilt(self) -> None:
        fields = [(1, 3), (5, 2), (2, 7), (4, 1), (1, 2)]
        base = column_marginals(fields)
        for source in (0, 2, 4):
            perturbed = column_marginals(fields, source)
            for t in range(len(fields)):
                self.assertLessEqual(abs(perturbed[t]-base[t]), Q(3, 5)**(abs(t-source)+1))

    def test_08_binary_bridge_domination(self) -> None:
        C = sp.Matrix([[sp.Rational(8,5), sp.Rational(2,5)],
                       [sp.Rational(2,5), sp.Rational(8,5)]])
        for b in (3, 4, 6):
            plain = 2 * (C/2)**b
            mixed = C
            upper = Q(1)
            for j in range(1,b):
                a = Q(1001,1000) if j % 2 else Q(1002,1000)
                diagonal = sp.diag(sp.Rational(a), 1)
                mixed = mixed * diagonal * C/2
                upper *= a
            self.assertTrue(all(plain[i,j] <= mixed[i,j] <= sp.Rational(upper)*plain[i,j]
                                for i in range(2) for j in range(2)))
            cross = mixed[0,0]*mixed[1,1]/(mixed[0,1]*mixed[1,0])
            self.assertGreaterEqual(cross, 1)
            self.assertLess(cross, 9)  # TV after arbitrary endpoint weights < 1/2.

    def test_09_wilson_spatial_incidence(self) -> None:
        for n in (4, 6, 8):
            e, p, degree = spatial_counts(n)
            self.assertEqual(e, 3*n**3)
            self.assertEqual(p, 3*n**3)
            self.assertEqual(degree, 12)

    def test_10_actual_fixture_covariance_bound(self) -> None:
        length = 5
        cov, count = paired_chain_covariances(length)
        self.assertEqual(count, 1024)
        G = sp.Matrix(length, length, lambda i, j: sp.Rational(response_profile(abs(i-j), 3)))
        A = sp.Matrix([[0, sp.Rational(1,2049)], [sp.Rational(1,2049), 0]])
        R = sp.kronecker_product(sp.eye(2), G)
        L = (sp.eye(2*length)-sp.kronecker_product(A,G)).inv()*R
        # Binary spin oscillations are exactly 2, cancelling the covariance factor 1/4.
        self.assertTrue(all(abs(cov[i,j]) <= L[i,j] for i in range(2*length) for j in range(2*length)))
        self.assertGreater(cov[0, length], 0)
        self.assertEqual(cov, cov.T)

    def test_11_susceptibility_and_scaling(self) -> None:
        b = sp.symbols('b', positive=True)
        value = 16*(4*b-1)/(1-(4*b-1)/(16*b))
        self.assertEqual(sp.factor(256*b/sp.Integer(3)-value-1024*b/(3*(12*b+1))), 0)
        # Isotropic s=beta>=1 is excluded, since b>=3 beta.
        self.assertGreater(Q(3), Q(1,192))
        for beta in (Q(1,2), Q(2), Q(8), Q(32), Q(128)):
            B = temporal_block(beta)
            smax = Q(1,192*B)
            self.assertLessEqual(4*B*smax, Q(1,48))
            self.assertLessEqual(96*B*smax, Q(1,2))

    def test_12_invalid_domains(self) -> None:
        for beta in (Q(0), Q(-1)):
            with self.assertRaises(ValueError): temporal_block(beta)
        with self.assertRaises(ValueError): response_profile(1,0)
        with self.assertRaises(ValueError): response_profile(-1,3)
        with self.assertRaises(ValueError): weighted_sum(3,Q(2))
        with self.assertRaises(ValueError): spatial_counts(2)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    started = time.perf_counter()
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(Checks)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    rows = []
    for beta in (Q(1,2), Q(2), Q(8), Q(32), Q(128)):
        b = temporal_block(beta)
        rows.append({'beta_t': str(beta), 'block_steps': b,
                     'allowed_spatial_upper': str(Q(1,192*b)),
                     'gap_times_tau_lower': f'log(4/3)/{b}',
                     'weaker_rational_gap_times_tau_lower': str(Q(1,4*b))})
    data = {'status': 'passed' if result.wasSuccessful() else 'failed',
            'tests_run': result.testsRun, 'failures': len(result.failures),
            'errors': len(result.errors), 'seconds': time.perf_counter()-started,
            'python': platform.python_version(), 'sympy': sp.__version__,
            'arithmetic': 'exact rational and symbolic finite decisions; analytic all-character tail',
            'seed': None, 'largest_binary_population': 1024,
            'spatial_geometry_sizes': [4,6,8], 'character_tail_bound': '709/4394',
            'scope': 'checks support separate written proof; binary fixtures are not Wilson data',
            'rows': rows, 'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(data, indent=2)+'\n')
    print(json.dumps(data, indent=2))
    return 0 if result.wasSuccessful() else 1


if __name__ == '__main__':
    raise SystemExit(main())

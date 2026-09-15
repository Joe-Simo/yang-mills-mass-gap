"""Exact audits for a fixed-set Wilson-memory bound, not a Yang--Mills solution.

Run: python checks/U032_conditional_memory_checks.py --output evidence/U032_checks.json
The matrix tests use a rational product-temporal kernel with arbitrary endpoint
weights; they are NOT Wilson measurements. SU(2) tests certify only a specified
fundamental-character benchmark. The full finite-Wilson theorem is proved in
research/audits/U032_true_vacuum_local_memory_bound.md.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
from itertools import combinations
import json
from math import factorial
from pathlib import Path
import platform
import time
import unittest

import sympy as sp

from U029_exact_link_integration_checks import ratio_certificate, outward_decimal

R = sp.Rational
Matrix = sp.MatrixBase


def psd_exact(a: Matrix) -> bool:
    """All principal minors: only the 2x2 and 4x4 rational tests below."""
    if a != a.T:
        return False
    return all(a.extract(ids, ids).det() >= 0
               for size in range(1, a.rows + 1)
               for ids in combinations(range(a.rows), size))


def tilted_transfer(weights: tuple[int, int, int, int]) -> tuple[Matrix, Matrix, Matrix]:
    """Reversible K for J(x,y) proportional to h_x C_xy h_y; beta=log(2)."""
    if any(isinstance(x, bool) or not isinstance(x, int) or x <= 0 for x in weights):
        raise ValueError("four strictly positive integer endpoint weights required")
    h = sp.Matrix(weights)
    c = sp.kronecker_product(sp.Matrix([[4, 1], [1, 4]]),
                             sp.Matrix([[4, 1], [1, 4]]))
    v = c * h
    mass = (h.T * v)[0]
    pi = sp.Matrix([h[i] * v[i] / mass for i in range(4)])
    k = sp.diag(*[1 / v[i] for i in range(4)]) * c * sp.diag(*h)
    return k, pi, sp.diag(*pi)


def retained_projection(pi: Matrix) -> Matrix:
    """Actual pi-conditional expectation onto the first of two bits."""
    p = sp.zeros(4)
    for group in ((0, 1), (2, 3)):
        mass = sum(pi[i] for i in group)
        for i in group:
            for j in group:
                p[i, j] = pi[j] / mass
    return p


def exp_interval(x: Fraction, terms: int) -> tuple[Fraction, Fraction]:
    """Positive exponential series with a rigorous geometric remainder."""
    if x < 0 or terms < 0:
        raise ValueError("require x>=0 and terms>=0")
    ratio = x / (terms + 2)
    if ratio >= 1:
        raise ValueError("tail ratio must be below one")
    total = sum((x ** j / factorial(j) for j in range(terms + 1)), Fraction(0))
    nxt = x ** (terms + 1) / factorial(terms + 1)
    return total, total + nxt / (1 - ratio)


def fundamental_benchmarks() -> list[dict[str, object]]:
    """Full tails, not unqualified floating comparisons."""
    rows: list[dict[str, object]] = []
    for beta in (Fraction(1, 2), Fraction(1), Fraction(2), Fraction(6)):
        bl, bu, terms = ratio_certificate(beta, digits=24)
        el, eu = exp_interval(2 * beta, 100)
        tl, tu = (el - 1) / (el + 1), (eu - 1) / (eu + 1)
        if not bu ** 4 < tl:
            raise AssertionError("certified fundamental benchmark failed")
        rows.append({
            "beta": str(beta),
            "bessel_terms": terms,
            "exp_terms": 100,
            "fundamental_transfer_interval": [
                outward_decimal(bl ** 4, 18, False),
                outward_decimal(bu ** 4, 18, True)],
            "tanh_bound_interval": [outward_decimal(tl, 18, False),
                                    outward_decimal(tu, 18, True)],
            "strict_inequality_by_exact_rationals": True,
        })
    return rows


class ConditionalMemoryTests(unittest.TestCase):
    def test_likelihood_ratio_sharp_tv_bound(self) -> None:
        a, b = sp.symbols("a b", positive=True)
        difference = (sp.sqrt(b) - sp.sqrt(a)) ** 2 - (b - 1) * (1 - a)
        self.assertEqual(sp.expand(difference - (sp.sqrt(a * b) - 1) ** 2), 0)
        # Attaining two-point likelihood ratios a=1/4,b=4 (cross ratio=16).
        q = sp.Matrix([R(4, 5), R(1, 5)])
        p = sp.Matrix([R(1, 5), R(4, 5)])
        self.assertEqual(sum(abs(p[i] - q[i]) for i in range(2)) / 2, R(3, 5))

    def test_su2_cross_ratio_algebra(self) -> None:
        u, up, v, vp = [sp.Matrix(sp.symbols(f"{name}0:4"))
                         for name in ("u", "s", "v", "t")]
        raw = u.dot(v) + up.dot(vp) - u.dot(vp) - up.dot(v)
        self.assertEqual(sp.expand(raw - (u - up).dot(v - vp)), 0)
        north = sp.Matrix([1, 0, 0, 0])
        self.assertEqual((2 * north).dot(2 * north), 4)
        self.assertEqual((2 * north).dot(-2 * north), -4)

    def test_two_conditional_channels_and_roundtrip(self) -> None:
        # A genuinely nonsymmetric bipartite law with arbitrary endpoint factors.
        k0 = sp.Matrix([[4, 1, 2], [1, 4, 2]])
        joint = sp.diag(1, 3) * k0 * sp.diag(2, 1, 5)
        joint /= sum(joint)
        px = joint * sp.ones(3, 1)
        py = joint.T * sp.ones(2, 1)
        forward = sp.diag(*[1 / p for p in px]) * joint
        reverse = sp.diag(*[1 / p for p in py]) * joint.T
        for channel in (forward, reverse):
            delta = max(sum(abs(channel[i, k] - channel[j, k])
                            for k in range(channel.cols)) / 2
                        for i in range(channel.rows) for j in range(channel.rows))
            self.assertLessEqual(delta, R(3, 5))
        roundtrip = forward * reverse
        mean = sp.ones(2, 1) * px.T
        w = sp.diag(*px)
        self.assertEqual(w * roundtrip, roundtrip.T * w)
        self.assertTrue(psd_exact(w * (R(9, 25) * (sp.eye(2) - mean)
                                      - (roundtrip - mean))))

    def test_actual_weighted_projection_and_positive_transfer(self) -> None:
        for h in ((1, 1, 1, 1), (1, 2, 3, 5), (1000, 1, 1, 1000)):
            k, pi, w = tilted_transfer(h)
            p = retained_projection(pi)
            self.assertEqual(k * sp.ones(4, 1), sp.ones(4, 1))
            self.assertEqual(w * k, k.T * w)
            self.assertTrue(psd_exact(w * k))
            self.assertTrue(psd_exact(w * (sp.eye(4) - k)))
            self.assertEqual(p * p, p)
            self.assertEqual(w * p, p.T * w)
            self.assertTrue(all(isinstance(x, sp.Rational) for x in k))

    def test_full_conditional_variance_form(self) -> None:
        for h in ((1, 1, 1, 1), (1, 2, 3, 5), (1000, 1, 1, 1000)):
            k, pi, w = tilted_transfer(h)
            q = sp.eye(4) - retained_projection(pi)
            # Stronger than testing only inputs in range Q.
            form = w * (sp.eye(4) - k * k - R(16, 25) * q)
            self.assertTrue(psd_exact(form))
            self.assertTrue(psd_exact(R(9, 25) * q.T * w * q
                                      - (k * q).T * w * (k * q)))

    def test_discarded_compression_and_memory_powers(self) -> None:
        k, pi, w = tilted_transfer((1, 2, 3, 5))
        p = retained_projection(pi)
        q = sp.eye(4) - p
        d = q * k * q
        self.assertTrue(psd_exact(w * (R(3, 5) * q - d)))
        p0 = p - sp.ones(4, 1) * pi.T
        b, bs = p0 * k * q, q * k * p0
        n0 = b * bs
        self.assertGreater(sp.trace(n0), 0)
        for power in range(7):
            self.assertTrue(psd_exact(w * (R(3, 5) ** power * n0
                                          - b * (d ** power) * bs)))

    def test_weighted_memory_full_tail_and_finite_certificate(self) -> None:
        k, pi, w = tilted_transfer((1, 2, 3, 5))
        p = retained_projection(pi)
        qproj = sp.eye(4) - p
        p0 = p - sp.ones(4, 1) * pi.T
        d = qproj * k * qproj
        b, bs = p0 * k * qproj, qproj * k * p0
        n0 = b * bs
        target, rate = R(4, 5), R(3, 5)
        exact = b * (target * sp.eye(4) - d).inv() * bs
        a = p0 * k * p0
        self.assertTrue(psd_exact(w * (target * p0 - a - n0 / (target - rate))))
        self.assertTrue(psd_exact(w * (target * p0 - a - exact)))
        centered = k - sp.ones(4, 1) * pi.T
        self.assertTrue(psd_exact(w * (target * (sp.eye(4) - sp.ones(4, 1) * pi.T)
                                      - centered)))
        partial = sp.zeros(4)
        for m in range(6):
            partial += target ** (-m - 1) * b * (d ** m) * bs
            upper = (rate / target) ** (m + 1) * n0 / (target - rate)
            self.assertTrue(psd_exact(w * (exact - partial)))
            self.assertTrue(psd_exact(w * (upper - (exact - partial))))

    def test_memory_is_not_unprojected_time_decay(self) -> None:
        k, pi, _ = tilted_transfer((1, 2, 3, 5))
        p = retained_projection(pi)
        q = sp.eye(4) - p
        d = q * k * q
        residual = q * k * k * q - d * d
        self.assertEqual(residual, q * k * p * k * q)
        self.assertGreater(sp.trace(residual), 0)

    def test_batch_independence_shortcut_fails(self) -> None:
        t = sp.Symbol("t", positive=True)
        c = sp.kronecker_product(sp.Matrix([[4, 1], [1, 4]]),
                                 sp.Matrix([[4, 1], [1, 4]]))
        h = sp.Matrix([t, 1, 1, t])
        v = c * h
        k = sp.diag(*[1 / x for x in v]) * c * sp.diag(*h)
        f = sp.Matrix([1, 0, 0, -1])
        eigenvalue = 15 * t / (17 * t + 8)
        self.assertEqual(sp.simplify(k * f - eigenvalue * f), sp.zeros(4, 1))
        self.assertEqual(sp.factor(eigenvalue - R(3, 5)
                                   - 24 * (t - 1) / (5 * (17 * t + 8))), 0)
        self.assertEqual(sp.limit(eigenvalue, t, sp.oo), R(15, 17))
        self.assertEqual(R(15, 17), (sp.Integer(4) ** 2 - 1) / (sp.Integer(4) ** 2 + 1))

    def test_coarse_inequality_is_not_automatic(self) -> None:
        k, pi, w = tilted_transfer((1000, 1, 1, 1000))
        p = retained_projection(pi)
        q = sp.eye(4) - p
        p0 = p - sp.ones(4, 1) * pi.T
        a = p0 * k * p0
        n0 = p0 * k * q * k * p0
        self.assertFalse(psd_exact(w * (R(4, 5) * p0 - a - 5 * n0)))
        self.assertGreater(R(15000, 17008), R(4, 5))

    def test_fundamental_su2_transfer_and_rational_tails(self) -> None:
        self.assertEqual(len(fundamental_benchmarks()), 4)
        with self.assertRaises(ValueError):
            exp_interval(Fraction(10), 1)
        with self.assertRaises(ValueError):
            tilted_transfer((1, 0, 1, 1))

    def test_physical_scale_uses_small_time_not_markov_power(self) -> None:
        z = sp.Symbol("z", positive=True)
        rate = (1 - z) / (1 + z)
        self.assertEqual(sp.factor(1 - rate), 2 * z / (1 + z))
        self.assertEqual(sp.limit(-sp.log(rate) / z, z, 0, dir="+"), 2)
        # Here z=exp(-2 beta). No asymptotic-freedom construction is assumed.


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    begin = time.perf_counter()
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(ConditionalMemoryTests)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    out = {
        "status": "passed" if result.wasSuccessful() else "failed",
        "tests_run": result.testsRun,
        "seconds": time.perf_counter() - begin,
        "python": platform.python_version(),
        "sympy": sp.__version__,
        "arithmetic": "exact rational/polynomial decisions; outward-rounded displayed certificates",
        "seed": None,
        "matrix_scope": "two-bit positive product-temporal kernels, not Wilson measurements",
        "endpoint_weights": [[1, 1, 1, 1], [1, 2, 3, 5], [1000, 1, 1, 1000]],
        "single_coordinate_rate_beta_log2": "3/5",
        "batch_sharp_limit_two_coordinates": "15/17",
        "memory_powers_checked": [0, 6],
        "weighted_tail_prefixes_checked": [0, 5],
        "su2_fundamental_benchmarks": fundamental_benchmarks() if result.wasSuccessful() else [],
        "nonclaims": ["No full Yang--Mills gap", "No simulation of the true vacuum",
                      "No extensive-decimation rate independent of removed-set size",
                      "No universal proof by finite tests"],
    }
    text = json.dumps(out, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text)
    print(text)
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    raise SystemExit(main())

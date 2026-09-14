"""Exact tests for auxiliary Yang--Mills research claims, not the Clay target.

Run from the project root: python checks/U002_exact_checks.py
Uses only Python integers and fractions. No simulation, floating-point fit,
continuum-limit test, or formal proof assistant is involved.
"""
from __future__ import annotations

from dataclasses import asdict, dataclass
from fractions import Fraction as Q
from itertools import combinations, product
import json
import platform
import unittest

Point = tuple[int, ...]
Matrix = tuple[tuple[Q, Q], tuple[Q, Q]]


def markov(lam: Q) -> Matrix:
    """Symmetric two-state Markov matrix with eigenvalues 1 and lam."""
    if not Q(0) <= lam <= Q(1):
        raise ValueError("lambda must lie in [0, 1]")
    return (((1 + lam) / 2, (1 - lam) / 2),
            ((1 - lam) / 2, (1 + lam) / 2))


def subtract(a: Matrix, b: Matrix) -> Matrix:
    return ((a[0][0] - b[0][0], a[0][1] - b[0][1]),
            (a[1][0] - b[1][0], a[1][1] - b[1][1]))


def psd2(a: Matrix) -> bool:
    """Exact principal-minor criterion for a real symmetric 2 by 2 matrix."""
    return (a[0][1] == a[1][0] and a[0][0] >= 0 and a[1][1] >= 0
            and a[0][0] * a[1][1] - a[0][1] * a[1][0] >= 0)


def rayleigh_excited(a: Matrix) -> Q:
    return (a[0][0] - a[0][1] - a[1][0] + a[1][1]) / 2


def shift(x: Point, mu: int, side: int, step: int = 1) -> Point:
    return tuple((v + step) % side if j == mu else v
                 for j, v in enumerate(x))


def parity(k: int) -> int:
    return 1 if k % 2 == 0 else -1


@dataclass(frozen=True)
class FluxResult:
    dimension: int
    side: int
    amplitudes: tuple[int, ...]
    vertices: int
    links: int
    plaquettes: int
    negative_plaquettes: int
    norm_squared: int
    curl_squared: int
    divergence_squared: int
    curl_identity_verified: bool


def check_flux(dimension: int, side: int, c: tuple[int, ...]) -> FluxResult:
    """Exhaustively check one specified torus; no inference to all sizes here."""
    if dimension < 2 or len(c) != dimension:
        raise ValueError("dimension >= 2 and one amplitude per direction required")
    if side < 4 or side % 2:
        raise ValueError("use an even torus side >= 4")
    if not any(c):
        raise ValueError("the test direction must be nonzero")
    sites = tuple(product(range(side), repeat=dimension))
    z = {(x, mu): parity(sum(x[:mu])) for x in sites
         for mu in range(dimension)}
    a = {(x, mu): parity(sum(x)) * c[mu] for x in sites
         for mu in range(dimension)}
    norm2 = sum(v * v for v in a.values())
    curl2 = negative = count = 0
    identity = True
    div2 = 0
    for x in sites:
        divergence = sum(a[(x, mu)] - a[(shift(x, mu, side, -1), mu)]
                         for mu in range(dimension))
        div2 += divergence * divergence
        for mu, nu in combinations(range(dimension), 2):
            xm, xn = shift(x, mu, side), shift(x, nu, side)
            # Signs are their own inverses; each plaquette is counted once.
            holonomy = z[(x, mu)] * z[(xm, nu)] * z[(xn, mu)] * z[(x, nu)]
            negative += int(holonomy == -1)
            count += 1
            curl = a[(x, mu)] + a[(xm, nu)] - a[(xn, mu)] - a[(x, nu)]
            identity = identity and curl == 2 * parity(sum(x)) * (c[mu] - c[nu])
            curl2 += curl * curl
    return FluxResult(dimension, side, c, len(sites), len(a), count,
                      negative, norm2, curl2, div2, identity)


class TransferTests(unittest.TestCase):
    def test_lower_order_does_not_give_upper_contraction(self) -> None:
        t, s = markov(Q(1, 2)), markov(Q(3, 4))
        self.assertTrue(psd2(t) and psd2(s) and psd2(subtract(s, t)))
        self.assertFalse(psd2(subtract(t, s)))
        self.assertTrue(all(sum(row) == 1 for row in t + s))
        self.assertEqual(rayleigh_excited(t), Q(1, 2))
        self.assertEqual(rayleigh_excited(s), Q(3, 4))

    def test_summable_positive_errors_can_exhaust_gap(self) -> None:
        # Finite audit of an explicitly proved geometric sequence in the note.
        total = Q(0)
        for k in range(40):
            lam = 1 - Q(1, 2 ** (k + 1))
            next_lam = 1 - Q(1, 2 ** (k + 2))
            eps = Q(1, 2 ** (k + 2))
            self.assertTrue(psd2(subtract(markov(next_lam), markov(lam))))
            self.assertEqual(next_lam - lam, eps)
            total += eps
        self.assertEqual(total, Q(1, 2) - Q(1, 2 ** 41))
        self.assertEqual(1 - next_lam, Q(1, 2 ** 41))

    def test_upper_error_budget_at_one_time(self) -> None:
        previous = Q(1, 2)
        for k in range(40):
            previous += Q(1, 2 ** (k + 3))
        self.assertLess(previous, Q(3, 4))
        # The infinite sum is 1/4; hence the infinite upper norm stays <= 3/4.
        self.assertEqual(previous, Q(3, 4) - Q(1, 2 ** 42))

    def test_shrinking_time_gap_can_still_collapse(self) -> None:
        # a_k=2^-k; lambda_k=1-a_k^2/2. -log(lambda_k)/a_k -> 0
        # follows from the analytic bound in the note, not this finite loop.
        for k in range(40):
            a = Q(1, 2 ** k)
            lam = 1 - a * a / 2
            a_next = a / 2
            lam_next = 1 - a_next * a_next / 2
            self.assertEqual(lam_next - lam, 3 * a * a / 8)
            self.assertLessEqual(a / (2 - a * a), a)
            self.assertTrue(psd2(subtract(markov(lam_next), markov(lam))))

    def test_infinite_model_generator_bounds_on_named_pairs(self) -> None:
        # The Hilbert-space limit is proved analytically, not by this finite grid.
        eta = Q(1, 100)
        for k in range(10):
            a, next_a = eta / 2 ** k, eta / 2 ** (k + 1)
            for n in range(1, 258):
                h = max(Q(1, n), Q(1, 2 ** k))
                next_h = max(Q(1, n), Q(1, 2 ** (k + 1)))
                self.assertLessEqual(abs(h - Q(1, n)), Q(1, 2 ** k))
                self.assertGreaterEqual(a * h - next_a * next_h, 0)
                self.assertLessEqual(a * h - next_a * next_h, a)

    def test_invalid_markov_parameter_rejected(self) -> None:
        with self.assertRaises(ValueError):
            markov(Q(3, 2))


class FluxTests(unittest.TestCase):
    def test_transverse_four_dimensional_tori(self) -> None:
        for side in (4, 6):
            r = check_flux(4, side, (1, -1, 0, 0))
            self.assertEqual(r.negative_plaquettes, 6 * side ** 4)
            self.assertTrue(r.curl_identity_verified)
            self.assertEqual(r.divergence_squared, 0)
            self.assertEqual(r.curl_squared, 16 * r.norm_squared)

    def test_dimension_and_nongauge_controls(self) -> None:
        for d in (2, 3):
            r = check_flux(d, 4, (1, -1) + (0,) * (d - 2))
            self.assertEqual(r.curl_squared, 4 * d * r.norm_squared)
        r = check_flux(4, 4, (1, 0, 0, 0))
        self.assertGreater(r.divergence_squared, 0)
        self.assertEqual(r.curl_squared, 12 * r.norm_squared)

    def test_pure_gauge_amplitude_control(self) -> None:
        r = check_flux(4, 4, (1, 1, 1, 1))
        self.assertEqual(r.curl_squared, 0)
        self.assertGreater(r.divergence_squared, 0)

    def test_invalid_torus_and_zero_direction_rejected(self) -> None:
        for side in (2, 3, 5):
            with self.assertRaises(ValueError):
                check_flux(4, side, (1, -1, 0, 0))
        with self.assertRaises(ValueError):
            check_flux(4, 4, (0, 0, 0, 0))


def run() -> int:
    suite = unittest.defaultTestLoader.loadTestsFromModule(__import__(__name__))
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    evidence = {
        "python": platform.python_version(),
        "arithmetic": "unbounded Python integers and fractions.Fraction",
        "tests_run": result.testsRun,
        "tests_passed": result.wasSuccessful(),
        "flux_cases": [asdict(check_flux(4, side, (1, -1, 0, 0))) for side in (4, 6)],
        "transfer_rayleigh_values": [str(rayleigh_excited(markov(q)))
                                     for q in (Q(1, 2), Q(3, 4))],
        "scope": "auxiliary finite checks; universal statements require the written proofs",
    }
    print(json.dumps(evidence, indent=2))
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    raise SystemExit(run())

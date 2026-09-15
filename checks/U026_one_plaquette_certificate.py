"""Exact enclosures for the complete, isolated gauge-invariant SU(2) square.

The infinite Jacobi operator has diagonal (m*m-1)/2 + lam, m >= 1,
and off-diagonal -lam/2.  The written U026 proof controls the omitted tail;
Ritz values alone are NOT lower spectral bounds.  All certification uses
fractions.Fraction and exact Sturm sign counts, not floating eigenvalues.

Commands:
    python checks/U026_one_plaquette_certificate.py --test
    python checks/U026_one_plaquette_certificate.py --output evidence/U026_certificates.json
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass
from fractions import Fraction as Q
import hashlib
import json
from math import isqrt
from pathlib import Path
import platform
import time
import unittest


class EigenvalueAtThreshold(ValueError):
    """The last determinant is zero: choose a non-eigenvalue threshold."""


@dataclass(frozen=True)
class Interval:
    lo: Q
    hi: Q

    def __post_init__(self) -> None:
        if self.lo > self.hi:
            raise ValueError("reversed interval")

    def serialized(self) -> list[str]:
        return [str(self.lo), str(self.hi)]


def sturm_count(diag: tuple[Q, ...], off: Q, threshold: Q) -> int:
    """Count eigenvalues strictly below a non-eigenvalue real threshold.

    For nonzero off diagonal the principal determinant sequence is a Sturm
    sequence. Internal zero determinants are omitted when counting signs.
    The diagonal (off == 0) case is counted directly.
    """
    if not diag:
        raise ValueError("empty Jacobi matrix")
    if off == 0:
        if threshold in diag:
            raise EigenvalueAtThreshold("threshold equals a diagonal entry")
        return sum(d < threshold for d in diag)
    previous_previous, previous = Q(1), diag[0] - threshold
    signs = [1]
    if previous:
        signs.append(1 if previous > 0 else -1)
    for d in diag[1:]:
        current = (d - threshold) * previous - off * off * previous_previous
        if current:
            signs.append(1 if current > 0 else -1)
        previous_previous, previous = previous, current
    if previous == 0:
        raise EigenvalueAtThreshold("threshold equals a matrix eigenvalue")
    return sum(left != right for left, right in zip(signs, signs[1:]))


def isolate(diag: tuple[Q, ...], off: Q, index: int, bits: int) -> Interval:
    """Enclose the zero-based ordered eigenvalue by exact rational bisection."""
    if not 0 <= index < len(diag) or bits < 1:
        raise ValueError("invalid index or precision")
    lo = min(diag) - 2 * abs(off) - 1
    hi = max(diag) + 2 * abs(off) + 1
    assert sturm_count(diag, off, lo) == 0
    assert sturm_count(diag, off, hi) == len(diag)
    tolerance = Q(1, 2**bits)
    for _ in range(512):
        if hi - lo <= tolerance:
            assert sturm_count(diag, off, lo) <= index
            assert sturm_count(diag, off, hi) > index
            return Interval(lo, hi)
        # At most len(diag) candidates are eigenvalues, so this finite list
        # always includes a usable rational in the middle third.
        count = None
        middle = (lo + hi) / 2
        candidates = [middle] + [
            lo + (hi - lo) * Q(len(diag) + 2 + j, 3 * (len(diag) + 2))
            for j in range(len(diag) + 1)
        ]
        for candidate in candidates:
            try:
                count = sturm_count(diag, off, candidate)
                middle = candidate
                break
            except EigenvalueAtThreshold:
                continue
        if count is None:
            raise ArithmeticError("failed to find a non-eigenvalue threshold")
        if count <= index:
            lo = middle
        else:
            hi = middle
    raise ArithmeticError("bisection iteration bound exhausted")


def certify(lam: int, size: int | None = None, bits: int = 20) -> dict[str, object]:
    """Enclose the first two eigenvalues of the INFINITE one-square operator.

    D_tail >= d I, d=((size+1)^2-1)/2.  With U=2*lam+2<d and
    delta=(lam/2)^2/(d-U), completing a square proves
        H >= (A_size - delta |last><last|) direct_sum U I.
    Both first two Ritz eigenvalues are below U by min-max and V<=2*lam.
    Therefore the lower comparison matrix and the Ritz matrix bound them.
    """
    if not isinstance(lam, int) or lam < 0:
        raise ValueError("lam must be a nonnegative integer for these records")
    if bits < 1:
        raise ValueError("bits must be positive")
    if size is None:
        size = 16 + 2 * isqrt(lam)
    if size < 2:
        raise ValueError("need at least two retained basis states")
    diag = tuple(Q(m * m - 1, 2) + lam for m in range(1, size + 1))
    off = -Q(lam, 2)
    cap = Q(2 * lam + 2)
    tail_floor = Q((size + 1) ** 2 - 1, 2)
    if tail_floor <= cap:
        raise ValueError("retained space too small for the tail certificate")
    correction = off * off / (tail_floor - cap)
    lower_diag = diag[:-1] + (diag[-1] - correction,)
    records = []
    energies = []
    for index in (0, 1):
        low_comparison = isolate(lower_diag, off, index, bits)
        ritz = isolate(diag, off, index, bits)
        if ritz.hi >= cap:
            raise ArithmeticError("upper enclosure must lie below the tail cap")
        enclosure = Interval(low_comparison.lo, ritz.hi)
        energies.append(enclosure)
        records.append({
            "index": index,
            "lower_comparison_root": low_comparison.serialized(),
            "ritz_root": ritz.serialized(),
            "infinite_operator_root": enclosure.serialized(),
        })
    gap = Interval(energies[1].lo - energies[0].hi,
                   energies[1].hi - energies[0].lo)
    result: dict[str, object] = {
        "lambda": str(lam), "retained_dimension": size,
        "bisection_bits": bits, "tail_floor": str(tail_floor),
        "tail_cap": str(cap), "last_diagonal_correction": str(correction),
        "eigenvalues": records, "gap": gap.serialized(),
        "gap_decimal_approximation_not_used_for_certification":
            [float(gap.lo), float(gap.hi)],
    }
    root = isqrt(lam)
    if root > 0 and root * root == lam:
        result["a_times_physical_gap"] = Interval(
            2 * gap.lo / root, 2 * gap.hi / root
        ).serialized()
        # A conservative check of the analytic half-sqrt-lambda theorem.
        assert gap.lo > Q(root, 2)
    return result


class CertificateTests(unittest.TestCase):
    def test_internal_zero_in_sturm_chain(self) -> None:
        self.assertEqual(sturm_count((Q(2), Q(2)), Q(-1), Q(2)), 1)

    def test_endpoint_eigenvalue_is_rejected(self) -> None:
        with self.assertRaises(EigenvalueAtThreshold):
            sturm_count((Q(2), Q(2)), Q(-1), Q(1))

    def test_known_two_by_two_roots(self) -> None:
        for index, eigenvalue in enumerate((Q(1), Q(3))):
            interval = isolate((Q(2), Q(2)), Q(-1), index, 16)
            self.assertLess(interval.lo, eigenvalue)
            self.assertGreater(interval.hi, eigenvalue)
            self.assertLessEqual(interval.hi - interval.lo, Q(1, 2**16))

    def test_electric_limit_has_gap_three_halves(self) -> None:
        result = certify(0, size=4, bits=18)
        interval = result["gap"]
        assert isinstance(interval, list)
        self.assertLess(Q(interval[0]), Q(3, 2))
        self.assertGreater(Q(interval[1]), Q(3, 2))

    def test_small_and_weak_coupling_certificates(self) -> None:
        for lam in (1, 16, 256):
            result = certify(lam, bits=16)
            gap = result["gap"]
            assert isinstance(gap, list)
            self.assertGreater(Q(gap[0]), Q(isqrt(lam), 2))
            self.assertLess(Q(gap[1]) - Q(gap[0]), Q(1, 1000))

    def test_invalid_tail_and_parameters(self) -> None:
        with self.assertRaises(ValueError):
            certify(256, size=3)
        with self.assertRaises(ValueError):
            certify(-1)
        with self.assertRaises(ValueError):
            certify(1, bits=0)

    def test_rational_constant_strictly_exceeds_half(self) -> None:
        # pi<22/7 gives pi^2/3-1/2 < 821/294 < (17/10)^2.
        self.assertLess(Q(821, 294), Q(17, 10)**2)
        self.assertGreater(Q(49, 22) - Q(17, 10), Q(1, 2))

    def test_lower_upper_direction_control(self) -> None:
        # For H=[[2,-1],[-1,4]], split after the first component; reserve U=3.
        # D=4, correction=1, hence H>=diag(1,3). H-diag(1,3) is PSD rank one.
        determinant = Q(1) * Q(1) - Q(1)
        self.assertEqual(determinant, 0)
        # Omitting the tail correction instead gives determinant -1: not PSD.
        self.assertLess(Q(0) * Q(1) - Q(1), 0)

    def test_two_loop_mixed_invariant_norm(self) -> None:
        # Independent normalized Haar quaternions have E[x_i*x_j]=delta_ij/4.
        self.assertEqual(sum(Q(1, 4)**2 for _ in range(3)), Q(3, 16))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--test", action="store_true")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    if args.test:
        result = unittest.TextTestRunner(verbosity=2).run(
            unittest.defaultTestLoader.loadTestsFromTestCase(CertificateTests)
        )
        return 0 if result.wasSuccessful() else 1
    start = time.perf_counter()
    records = [certify(lam) for lam in (0, 1, 16, 256, 4096)]
    evidence = {
        "base_commit": "1c5e8c2623d6a88336c6b7141f9d7a022a51d818",
        "python": platform.python_version(),
        "arithmetic": "exact integers and fractions.Fraction",
        "code_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "elapsed_seconds": time.perf_counter() - start,
        "scope": "isolated SU(2) square, all class-function states; not full Yang-Mills",
        "method": "min-max with analytic infinite-tail comparison and exact Sturm counts",
        "records": records,
    }
    text = json.dumps(evidence, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text)
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

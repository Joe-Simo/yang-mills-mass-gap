"""Exact and finite audits for U043; not a continuum Yang--Mills certificate.

Run: python checks/U043_curved_horizontal_coercivity_checks.py --output evidence/U043_checks.json
The universal open-cube spectrum, leakage lemma, and smooth-locality Hessian bound
have separate written proofs in research/audits/U043_curved_horizontal_coercivity.md.
"""
from __future__ import annotations

import argparse
import json
import math
import platform
import time
import unittest
from itertools import product
from pathlib import Path

import numpy as np
import sympy as sp


def path_incidence(n: int) -> np.ndarray:
    D = np.zeros((n, n + 1), dtype=float)
    for i in range(n):
        D[i, i] = -1.0
        D[i, i + 1] = 1.0
    return D


def cubical_incidence_4d(n: int):
    d = 4
    vertices = list(product(range(n + 1), repeat=d))
    vid = {x: i for i, x in enumerate(vertices)}
    edges = []
    for x in vertices:
        for mu in range(d):
            if x[mu] < n:
                edges.append((x, mu))
    eid = {e: i for i, e in enumerate(edges)}
    faces = []
    for x in vertices:
        for mu in range(d):
            for nu in range(mu + 1, d):
                if x[mu] < n and x[nu] < n:
                    faces.append((x, mu, nu))
    d0 = np.zeros((len(edges), len(vertices)))
    for i, (x, mu) in enumerate(edges):
        y = list(x); y[mu] += 1; y = tuple(y)
        d0[i, vid[x]] = -1
        d0[i, vid[y]] = 1
    d1 = np.zeros((len(faces), len(edges)))
    for i, (x, mu, nu) in enumerate(faces):
        xmu = list(x); xmu[mu] += 1; xmu = tuple(xmu)
        xnu = list(x); xnu[nu] += 1; xnu = tuple(xnu)
        d1[i, eid[(x, mu)]] += 1
        d1[i, eid[(xmu, nu)]] += 1
        d1[i, eid[(xnu, mu)]] -= 1
        d1[i, eid[(x, nu)]] -= 1
    return d0, d1


def nu1(ell: int) -> float:
    return 4.0 * math.sin(math.pi / (2.0 * (ell + 1))) ** 2


def transverse_gap(ell: int) -> float:
    return 2.0 * nu1(ell)


def leakage_bound(delta: float, ell: int) -> float:
    sigma = math.sqrt(nu1(ell))
    return 4.0 * delta / sigma


def optimized_scales(alpha: float):
    ell = alpha ** (-1.0 / 13.0)
    delta = alpha ** (7.0 / 26.0)
    return {"ell": ell, "delta": delta, "delta_ell": delta * ell,
            "delta_ell2": delta * ell * ell}


class U043Checks(unittest.TestCase):
    def test_01_path_spectral_gap_formula(self):
        for n in range(1, 8):
            D = path_incidence(n)
            vals = np.linalg.eigvalsh(D.T @ D)
            pos = vals[vals > 1e-10]
            self.assertAlmostEqual(pos[0], nu1(n), places=11)

    def test_02_small_open_4d_hodge_spectrum(self):
        d0, d1 = cubical_incidence_4d(1)
        self.assertEqual(d0.shape, (32, 16))
        self.assertEqual(d1.shape, (24, 32))
        self.assertLess(np.linalg.norm(d1 @ d0), 1e-12)
        L1 = d1.T @ d1 + d0 @ d0.T
        vals = np.linalg.eigvalsh(L1)
        pos = vals[vals > 1e-9]
        self.assertAlmostEqual(pos[0], nu1(1), places=10)
        Q, _ = np.linalg.qr(d0)
        rank = np.linalg.matrix_rank(d0)
        Pgrad = Q[:, :rank] @ Q[:, :rank].T
        w, V = np.linalg.eigh(np.eye(32) - Pgrad)
        B = V[:, w > 0.5]
        cvals = np.linalg.eigvalsh(B.T @ (d1.T @ d1) @ B)
        self.assertAlmostEqual(cvals[0], transverse_gap(1), places=9)

    def test_03_dimension_formula_low_modes_is_bounded(self):
        for C in (6.0, 8.0, 12.0):
            counts = []
            for ell in (16, 32, 64, 128):
                count = 0
                for k0 in range(0, min(ell, 12) + 1):
                    for k1 in range(0, min(ell, 12) + 1):
                        for k2 in range(0, min(ell, 12) + 1):
                            for k3 in range(0, min(ell, 12) + 1):
                                ks = (k0, k1, k2, k3)
                                s = sum(k > 0 for k in ks)
                                if s < 2:
                                    continue
                                lam = sum(4 * math.sin(math.pi * k / (2 * (ell + 1))) ** 2 for k in ks)
                                if lam <= C * C / (ell * ell):
                                    count += s - 1
                counts.append(count)
            self.assertLessEqual(max(counts), 10000)
            self.assertGreater(max(counts), 0)

    def test_04_exact_gradient_leakage_lemma_fixture(self):
        G0 = sp.Matrix([[1, 0], [0, 2], [0, 0]])
        E = sp.Matrix([[0, 0], [0, 0], [sp.Rational(1, 10), sp.Rational(1, 20)]])
        G = G0 + E
        b = sp.Matrix([sp.Rational(-1, 10), sp.Rational(-1, 40), 1])
        self.assertEqual(G.T * b, sp.zeros(2, 1))
        P = G0 * (G0.T * G0).inv() * G0.T
        g = P * b
        lhs2 = sp.simplify((g.T * g)[0])
        b2 = sp.simplify((b.T * b)[0])
        eF2 = sp.simplify(sum(x * x for x in E))
        self.assertLessEqual(lhs2, sp.simplify(eF2 * b2))

    def test_05_adjoint_rotation_perturbation_bound(self):
        for theta in (0.0, 0.05, 0.2, 0.5, 1.0):
            op = 2.0 * abs(math.sin(theta))
            self.assertLessEqual(op, 2.0 * abs(theta) + 1e-15)

    def test_06_elementary_lower_bounds(self):
        for ell in (1, 2, 4, 16, 100):
            self.assertGreaterEqual(nu1(ell) + 1e-14, 4.0 / (ell + 1) ** 2)
            self.assertGreaterEqual(transverse_gap(ell) + 1e-14, 8.0 / (ell + 1) ** 2)

    def test_07_optimized_margin_exponents(self):
        self.assertEqual(sp.Rational(7, 26) - sp.Rational(1, 13), sp.Rational(5, 26))
        self.assertEqual(sp.Rational(7, 26) - sp.Rational(2, 13), sp.Rational(3, 26))
        for alpha in (1e-4, 1e-8, 1e-12):
            s = optimized_scales(alpha)
            self.assertLess(s["delta_ell"], 1.0)
            self.assertLess(s["delta_ell2"], 1.0)

    def test_08_horizontal_flat_curl_bound_fixture(self):
        rng = np.random.default_rng(7)
        G0 = np.array([[1., 0.], [0., 2.], [0., 0.], [0., 0.]])
        E = np.array([[0., 0.], [0., 0.], [0.03, -0.01], [0.02, 0.01]])
        G = G0 + E
        _, _, vh = np.linalg.svd(G.T)
        B = vh[2:].T
        Pgrad = G0 @ np.linalg.inv(G0.T @ G0) @ G0.T
        eps = np.linalg.norm(E, 2)
        sigma = np.linalg.svd(G0, compute_uv=False)[-1]
        for _ in range(10):
            c = rng.normal(size=B.shape[1]); b = B @ c
            grad = Pgrad @ b
            self.assertLessEqual(np.linalg.norm(grad), (eps / sigma) * np.linalg.norm(b) + 1e-12)

    def test_09_trace_corollary_algebra(self):
        ell = sp.Symbol("ell", positive=True)
        mu = sp.Rational(8) / (ell + 1) ** 2
        half = sp.simplify(mu / 2)
        self.assertEqual(1 / half, (ell + 1) ** 2 / sp.Integer(4))


def main():
    p = argparse.ArgumentParser(); p.add_argument("--output", required=True); args = p.parse_args()
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(U043Checks)
    t = time.perf_counter(); result = unittest.TextTestRunner(verbosity=2).run(suite)
    payload = {
        "status": "passed" if result.wasSuccessful() else "failed",
        "tests_run": result.testsRun, "failures": len(result.failures), "errors": len(result.errors),
        "seconds": time.perf_counter() - t, "python": platform.python_version(), "sympy": sp.__version__,
        "numpy": np.__version__, "seed": 7,
        "arithmetic": "exact symbolic/rational where stated; spectral and subspace fixtures use deterministic float linear algebra",
        "claims_checked": ["open-path scalar gap nu1", "small 4D cubical Hodge complex and transverse curl gap", "bounded low-mode count diagnostics", "gradient leakage lemma finite fixture", "SU(2) adjoint rotation perturbation bound", "optimized margins delta*ell and delta*ell^2", "horizontal subspace perturbation fixture", "O(ell^2) trace/coercivity corollary algebra"],
        "nonclaims": ["finite matrices do not replace written all-ell tensor proof", "no boundary Schur-complement stability theorem", "no continuum mass gap"]}
    Path(args.output).write_text(json.dumps(payload, indent=2))
    raise SystemExit(0 if result.wasSuccessful() else 1)

if __name__ == "__main__":
    main()

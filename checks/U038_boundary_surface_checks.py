"""Exact audits of U038's boundary construction and dense-defect estimate.

Run: python checks/U038_boundary_surface_checks.py --output evidence/U038_checks.json
The group-valued counterexample uses exact sixth roots inside continuous SU(2).
The Bernoulli and Q8 fixtures test probability/algebra, not Wilson observations.
The infinite-volume-independent statements have separate written proofs.
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass
from fractions import Fraction as F
from itertools import combinations, product
import json
from math import comb
from pathlib import Path
import platform
import time
import unittest

import sympy as sp

Vertex = tuple[int, ...]
Edge = tuple[Vertex, int]
Face = tuple[Vertex, int, int]


@dataclass(frozen=True)
class Counts:
    edges: int
    faces: int
    crossing: int
    full_stars: int


def box_counts(d: int, n: int) -> Counts:
    if d < 2 or n < 1:
        raise ValueError("Dimension >=2 and cell side >=1 required")
    return Counts(d*n*(n+1)**(d-1), comb(d, 2)*n*n*(n+1)**(d-2),
                  4*comb(d, 2)*n*(n+1)**(d-2), d*n*(n-1)**(d-1))


def shift(x: Vertex, mu: int, step: int = 1) -> Vertex:
    v = list(x)
    v[mu] += step
    return tuple(v)


def face_edges(p: Face) -> tuple[Edge, ...]:
    x, mu, nu = p
    return ((x, mu), (shift(x, mu), nu), (shift(x, nu), mu), (x, nu))


def incidence_box(d: int, n: int) -> tuple[set[Edge], set[Face], set[Face]]:
    box_counts(d, n)
    edges = {(x, mu) for x in product(range(n+1), repeat=d)
             for mu in range(d) if x[mu] < n}
    affected: set[Face] = set()
    for x, mu in edges:
        for nu in range(d):
            if nu != mu:
                lo, hi = sorted((mu, nu))
                affected.update(((x, lo, hi), (shift(x, nu, -1), lo, hi)))
    inside = {p for p in affected if all(e in edges for e in face_edges(p))}
    return edges, inside, affected - inside


def on_boundary(e: Edge, n: int) -> bool:
    x, mu = e
    return any(v in (0, n) for j, v in enumerate(x) if j != mu)


def phase_energy(phases: dict[Edge, int], faces: set[Face]) -> F:
    # 1-cos(k*pi/3), k mod 6: exact SU(2) fundamental trace deficits.
    cost = (F(0), F(1, 2), F(3, 2), F(2), F(3, 2), F(1, 2))
    total = F(0)
    for p in faces:
        a, b, c, d = face_edges(p)
        total += cost[(phases[a] + phases[b] - phases[c] - phases[d]) % 6]
    return total


def ceil_fraction(x: F) -> int:
    return -(-x.numerator // x.denominator)


def rational_threshold(alpha: F, n: int) -> dict[str, str | int]:
    """Sufficient exact parameters, not a numerical Gibbs experiment.

    delta=alpha/8 ensures 8 delta^2 <=alpha/4 for 0<alpha<=2.
    pi<22/7 gives a rational Haar-ball lower bound; v>=2^-h gives
    -log(v)<=h*log(2)<h. Only rational comparisons select beta.
    """
    if not 0 < alpha <= 2 or n < ceil_fraction(32 / alpha):
        raise ValueError("Require 0<alpha<=2 and n>=32/alpha")
    c = box_counts(4, n)
    delta = alpha / 8
    v_lower = 8*delta**3 / (3*F(22, 7)**3)
    h = 0
    while F(1, 2**h) > v_lower:
        h += 1
    beta = ceil_fraction(4*F(c.edges)*h/(alpha*c.faces))
    action = alpha*c.faces - 8*delta**2*c.faces - 2*c.crossing
    remaining = beta*action - c.edges*h
    target = beta*alpha*c.faces/4
    if remaining < target:
        raise AssertionError("Certificate inequalities failed")
    return {"alpha": str(alpha), "n": n, "delta": str(delta),
            "haar_ball_lower": str(v_lower), "entropy_upper": h,
            "beta_sufficient": beta, "M": c.faces, "L": c.edges,
            "boundary_faces": c.crossing,
            "certified_negative_log_probability": str(target)}


class SurfaceChecks(unittest.TestCase):
    def test_01_exact_incidence_counts(self) -> None:
        for d, n in product(range(2, 5), range(1, 4)):
            with self.subTest(d=d, n=n):
                edges, faces, crossing = incidence_box(d, n)
                c = box_counts(d, n)
                self.assertEqual((len(edges), len(faces), len(crossing)),
                                 (c.edges, c.faces, c.crossing))
                self.assertTrue(all(sum(e in edges for e in face_edges(p)) == 1
                                    for p in crossing))

    def test_02_complete_star_count_and_incidence(self) -> None:
        for d, n in ((2, 3), (3, 2), (4, 3)):
            edges, faces, crossing = incidence_box(d, n)
            complete = {e for e in edges
                        if not any(e in face_edges(p) for p in crossing)}
            self.assertEqual(len(complete), box_counts(d, n).full_stars)
            self.assertTrue(all(sum(e in face_edges(p) for p in faces) == 2*(d-1)
                                for e in complete))
            self.assertTrue(all(sum(e in complete for e in face_edges(p)) <= 4
                                for p in faces))

    def test_03_open_counts_and_boundary_ratios(self) -> None:
        n = sp.Symbol('n', positive=True, integer=True)
        m, ell, border = 6*n**2*(n+1)**2, 4*n*(n+1)**3, 24*n*(n+1)**2
        self.assertEqual(sp.cancel(border/m), 4/n)
        self.assertEqual(sp.cancel(ell/m), 2*(n+1)/(3*n))
        self.assertEqual(sp.expand(m - m.subs(n, n-2)),
                         48*n**3 - 72*n**2 + 72*n - 24)
        self.assertEqual(box_counts(4, 1).faces, 24)
        self.assertEqual(box_counts(4, 1).edges, 32)

    def test_04_boundary_fixed_constant_flux_counterexample(self) -> None:
        edges, faces, _ = incidence_box(2, 6)
        flux = {e: e[0][0] % 6 if e[1] == 1 else 0 for e in edges}
        flat = dict.fromkeys(edges, 0)
        self.assertTrue(all(flux[e] == flat[e] for e in edges if on_boundary(e, 6)))
        self.assertEqual(phase_energy(flux, faces), 18)
        self.assertEqual(phase_energy(flat, faces), 0)

    def test_05_four_dimensional_surface_competitor(self) -> None:
        n = 256
        total, core = box_counts(4, n).faces, box_counts(4, n-2).faces
        flux_energy, upper_competitor = F(total, 12), 2*(total-core)
        self.assertEqual(flux_energy, 2164293632)
        self.assertEqual(upper_competitor, 1601212368)
        self.assertGreater(flux_energy, upper_competitor)

    def test_06_haar_volume_and_safe_parameter_certificates(self) -> None:
        x = sp.Symbol('x', positive=True)
        v = (x-sp.sin(2*x)/2)/sp.pi
        self.assertEqual(sp.simplify(sp.diff(v,x)-2*sp.sin(x)**2/sp.pi), 0)
        self.assertEqual(sp.limit(v, x, 0), 0)
        for alpha in (F(1, 8), F(1, 2), F(1), F(2)):
            cert = rational_threshold(alpha, ceil_fraction(32/alpha))
            self.assertGreater(F(str(cert['certified_negative_log_probability'])), 0)

    def test_07_pointwise_star_action(self) -> None:
        # Q8 unit quaternions audit the exact local identity, not a measure bound.
        units = tuple(tuple(F(sign if i == j else 0) for i in range(4))
                      for j in range(4) for sign in (-1, 1))
        patterns = (units[:6], (units[0],)*6,
                    (units[0], units[1])*3, (units[2], units[4], units[6])*2)
        for staples in patterns:
            h = tuple(sum((v[i] for v in staples), F(0)) for i in range(4))
            s2 = sum(v*v for v in h)
            for u in units:
                energy = sum((1-sum(a*b for a,b in zip(u,v,strict=True))
                              for v in staples), F(0))
                scalar = sum(a*b for a,b in zip(u,h,strict=True))
                self.assertEqual(energy, 6-scalar)
                self.assertLessEqual(scalar*scalar, s2)
        n = sp.Symbol('n', positive=True, integer=True)
        star_to_face = sp.cancel(6*(4*n*(n-1)**3)/(4*(6*n**2*(n+1)**2)))
        self.assertEqual(sp.cancel(star_to_face-(n-1)**3/(n*(n+1)**2)), 0)

    def test_08_correlated_conditional_tower_fixture(self) -> None:
        # Exact correlated binary cycle. Conditional bound, NOT independence.
        states = tuple(product((0,1), repeat=4))
        weights = {x: F(1,16)**sum(x)*2**sum(x[i]*x[(i+1)%4] for i in range(4))
                   for x in states}
        z = sum(weights.values(), F(0))
        law = {x:w/z for x,w in weights.items()}
        conditional_bound = F(1, 5)
        for i in range(4):
            others = tuple(j for j in range(4) if j != i)
            for y in product((0,1), repeat=3):
                den = sum(p for x,p in law.items() if tuple(x[j] for j in others)==y)
                num = sum(p for x,p in law.items() if x[i] and tuple(x[j] for j in others)==y)
                self.assertLessEqual(num/den, conditional_bound)
        for k in range(1,5):
            for selected in combinations(range(4),k):
                joint = sum(p for x,p in law.items() if all(x[j] for j in selected))
                self.assertLessEqual(joint, conditional_bound**k)
        single = sum(p for x,p in law.items() if x[0])
        joint = sum(p for x,p in law.items() if x[0] and x[1])
        self.assertNotEqual(joint, single**2)

    def test_09_animal_bound_and_rare_projection_obstruction(self) -> None:
        vertices = tuple(product(range(3), repeat=2))
        root = (1,1)
        for size in range(1,5):
            count = 0
            for chosen in combinations(vertices, size):
                if root not in chosen:
                    continue
                visited = {root}
                while True:
                    more = {v for v in chosen if any(sum(abs(a-b) for a,b in zip(v,w,strict=True))==1
                                                    for w in visited)}
                    if more <= visited:
                        break
                    visited |= more
                count += int(len(visited)==size)
            self.assertLessEqual(count, 4**(2*(size-1)))
        p = F(1,1024)
        total_norm2 = p*(1-p)**2+(1-p)*p**2
        retained_bad_norm2 = p*(1-p)**2
        self.assertEqual(retained_bad_norm2/total_norm2, 1-p)

    def test_10_invalid_inputs(self) -> None:
        for d,n in ((1,4),(4,0),(3,-1)):
            with self.assertRaises(ValueError):
                box_counts(d,n)
        for alpha,n in ((F(0),32),(F(3),32),(F(1),1)):
            with self.assertRaises(ValueError):
                rational_threshold(alpha,n)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    start = time.monotonic()
    result = unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(SurfaceChecks))
    data = {"status":"passed" if result.wasSuccessful() else "failed",
            "tests_run":result.testsRun,"failures":len(result.failures),"errors":len(result.errors),
            "seconds":time.monotonic()-start,"python":platform.python_version(),"sympy":sp.__version__,
            "arithmetic":"exact Fraction and SymPy; analytic all-configuration proof in U038",
            "seed":None,"geometries":{"d":[2,3,4],"n":[1,2,3]},
            "flux_witness":{"dimension":2,"n":6,"angle":"pi/3","old_action":"18","competitor_action":"0"},
            "strong_coupling_certificates":[rational_threshold(a,ceil_fraction(32/a))
                                            for a in (F(1,8),F(1,2),F(1),F(2))],
            "nonclaims":["no Monte Carlo data","no full spectral gap","no continuum construction",
                         "Q8 and binary fixtures do not substitute for SU(2) probability proofs"]}
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps(data,indent=2))
    return 0 if result.wasSuccessful() else 1


if __name__ == '__main__':
    raise SystemExit(main())

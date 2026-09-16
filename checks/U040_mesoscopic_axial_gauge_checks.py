"""Exact finite audits for U040's mesoscopic axial-gauge decomposition.

Run: python checks/U040_mesoscopic_axial_gauge_checks.py --output evidence/U040_checks.json
The finite ribbon tests audit cubical geometry and the chosen maximal-tree gauge.
The nonlinear SU(2) Taylor/coercivity statements have separate written proofs.
No continuum mass-gap certificate is produced.
"""
from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction as F
from itertools import product
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


def shift(x: Vertex, mu: int, step: int = 1) -> Vertex:
    y = list(x)
    y[mu] += step
    return tuple(y)


def counts(d: int, n: int) -> tuple[int, int, int]:
    if d < 2 or n < 1:
        raise ValueError
    vertices = (n + 1) ** d
    edges = d * n * (n + 1) ** (d - 1)
    faces = comb(d, 2) * n * n * (n + 1) ** (d - 2)
    return vertices, edges, faces


def canonical_word(x: Vertex) -> list[int]:
    word: list[int] = []
    for mu in reversed(range(len(x))):
        word.extend([mu] * x[mu])
    return word


def path_edges(word: list[int], d: int) -> tuple[list[Edge], Vertex]:
    x = [0] * d
    out: list[Edge] = []
    for mu in word:
        out.append((tuple(x), mu))
        x[mu] += 1
    return out, tuple(x)


def xor_edges(edges: list[Edge]) -> set[Edge]:
    c = Counter(edges)
    return {e for e, m in c.items() if m % 2}


def face_edges_mod2(p: Face) -> set[Edge]:
    x, mu, nu = p
    return {
        (x, mu),
        (shift(x, mu), nu),
        (shift(x, nu), mu),
        (x, nu),
    }


def is_tree_edge(x: Vertex, mu: int) -> bool:
    return all(x[nu] == 0 for nu in range(mu))


def ribbon_plaquettes(x: Vertex, mu: int) -> list[Face]:
    """Plaquette ribbon obtained by commuting the appended mu-step left.

    Orientation is suppressed here; mod-2 boundary is enough to audit geometry.
    The written proof restores orientations/conjugations for the SU(2) identity.
    """
    d = len(x)
    tokens: list[tuple[int, bool]] = [(nu, False) for nu in canonical_word(x)]
    tokens.append((mu, True))
    faces: list[Face] = []
    while True:
        idx = next(i for i, token in enumerate(tokens) if token[1])
        if idx == 0:
            break
        prev = tokens[idx - 1][0]
        if prev >= mu:
            break
        y = [0] * d
        for nu, _marked in tokens[: idx - 1]:
            y[nu] += 1
        lo, hi = sorted((prev, mu))
        faces.append((tuple(y), lo, hi))
        tokens[idx - 1], tokens[idx] = tokens[idx], tokens[idx - 1]
    target = list(x)
    target[mu] += 1
    if [nu for nu, _ in tokens] != canonical_word(tuple(target)):
        raise AssertionError("swap ribbon did not reach canonical path")
    return faces


def fundamental_cycle_mod2(x: Vertex, mu: int) -> set[Edge]:
    d = len(x)
    p0, endpoint = path_edges(canonical_word(x), d)
    if endpoint != x:
        raise AssertionError
    y = list(x)
    y[mu] += 1
    y = tuple(y)
    p1, endpoint1 = path_edges(canonical_word(y), d)
    if endpoint1 != y:
        raise AssertionError
    return xor_edges(p0 + [(x, mu)] + p1)


def qmul(a: tuple[int,int,int,int], b: tuple[int,int,int,int]) -> tuple[int,int,int,int]:
    aw,ax,ay,az=a; bw,bx,by,bz=b
    return (aw*bw-ax*bx-ay*by-az*bz,
            aw*bx+ax*bw+ay*bz-az*by,
            aw*by-ax*bz+ay*bw+az*bx,
            aw*bz+ax*by-ay*bx+az*bw)


def qinv(a: tuple[int,int,int,int]) -> tuple[int,int,int,int]:
    return (a[0],-a[1],-a[2],-a[3])


Q8=((1,0,0,0),(-1,0,0,0),(0,1,0,0),(0,-1,0,0),
    (0,0,1,0),(0,0,-1,0),(0,0,0,1),(0,0,0,-1))


def edge_value(e: Edge) -> tuple[int,int,int,int]:
    x,mu=e
    idx=(mu + sum((j+2)*v for j,v in enumerate(x))) % len(Q8)
    return Q8[idx]


def path_holonomy(word: list[int], d: int) -> tuple[int,int,int,int]:
    x=[0]*d
    h=Q8[0]
    for mu in word:
        h=qmul(h, edge_value((tuple(x),mu)))
        x[mu]+=1
    return h


def plaquette_holonomy(x: Vertex, nu: int, mu: int) -> tuple[int,int,int,int]:
    # nu<mu, positive orientation nu then mu.
    a=edge_value((x,nu))
    b=edge_value((shift(x,nu),mu))
    c=qinv(edge_value((shift(x,mu),nu)))
    d=qinv(edge_value((x,mu)))
    return qmul(qmul(qmul(a,b),c),d)


def ribbon_group_product(x: Vertex, mu: int) -> tuple[int,int,int,int]:
    d=len(x)
    tokens=[(nu,False) for nu in canonical_word(x)] + [(mu,True)]
    correction=Q8[0]
    while True:
        idx=next(i for i,t in enumerate(tokens) if t[1])
        if idx==0:
            break
        nu=tokens[idx-1][0]
        if nu>=mu:
            break
        prefix=[t[0] for t in tokens[:idx-1]]
        z=[0]*d
        for k in prefix:
            z[k]+=1
        h=path_holonomy(prefix,d)
        p=plaquette_holonomy(tuple(z),nu,mu)
        correction=qmul(correction,qmul(qmul(h,p),qinv(h)))
        tokens[idx-1],tokens[idx]=tokens[idx],tokens[idx-1]
    return correction


def core_coverage_fraction(n: int, ell: int) -> F:
    if n < 1 or ell < 1:
        raise ValueError
    q = n // (ell + 1)
    if q == 0:
        return F(0)
    return F((q * ell) ** 4, n**4)


class Checks(unittest.TestCase):
    def test_01_axial_tree_count(self) -> None:
        for d, n in product(range(2, 5), range(1, 4)):
            vertices, edges, _faces = counts(d, n)
            tree = 0
            total = 0
            for x in product(range(n + 1), repeat=d):
                for mu in range(d):
                    if x[mu] < n:
                        total += 1
                        tree += int(is_tree_edge(x, mu))
            self.assertEqual(total, edges)
            self.assertEqual(tree, vertices - 1)
            self.assertEqual(edges - tree, edges - vertices + 1)

    def test_02_fundamental_ribbon_boundary(self) -> None:
        for d, n in product(range(2, 5), range(1, 4)):
            for x in product(range(n + 1), repeat=d):
                for mu in range(d):
                    if x[mu] >= n:
                        continue
                    ribbon = ribbon_plaquettes(x, mu)
                    boundary: set[Edge] = set()
                    for p in ribbon:
                        boundary ^= face_edges_mod2(p)
                    self.assertEqual(boundary, fundamental_cycle_mod2(x, mu))
                    self.assertEqual(len(ribbon), sum(x[nu] for nu in range(mu)))
                    self.assertLessEqual(len(ribbon), (d - 1) * n)
                    self.assertEqual(len(ribbon) == 0, is_tree_edge(x, mu))

    def test_03_noncommutative_ribbon_identity_q8(self) -> None:
        for d,n in ((2,2),(3,2),(4,1)):
            for x in product(range(n+1), repeat=d):
                for mu in range(d):
                    if x[mu] >= n:
                        continue
                    gx=path_holonomy(canonical_word(x),d)
                    y=list(x); y[mu]+=1; y=tuple(y)
                    gy=path_holonomy(canonical_word(y),d)
                    fundamental=qmul(qmul(gx,edge_value((x,mu))),qinv(gy))
                    self.assertEqual(fundamental,ribbon_group_product(x,mu))

    def test_04_four_dimensional_link_bound_constants(self) -> None:
        ell = sp.symbols('ell', positive=True, integer=True)
        links = 4 * ell * (ell + 1) ** 3
        self.assertEqual(sp.expand(links), 4*ell**4 + 12*ell**3 + 12*ell**2 + 4*ell)
        # ell>=1 implies L<=32 ell^4; max ribbon <=3 ell.
        for k in (1, 2, 3, 8):
            L = 4*k*(k+1)**3
            self.assertLessEqual(L, 32*k**4)
            self.assertEqual(max(sum(x[nu] for nu in range(mu))
                                 for x in product(range(k+1), repeat=4)
                                 for mu in range(4) if x[mu] < k), 3*k)

    def test_05_mesoscopic_exponent_balance(self) -> None:
        a = sp.symbols('a', positive=True)
        ell = a ** F(-1, 16)
        eps = a ** F(1, 2)
        self.assertEqual(sp.simplify(a * ell**4 / eps), a ** F(1, 4))
        self.assertEqual(sp.simplify(1 / ell), a ** F(1, 16))
        self.assertEqual(sp.simplify(sp.sqrt(ell * eps)), a ** F(7, 32))
        self.assertEqual(sp.simplify(ell**3 * sp.sqrt(eps)), a ** F(1, 16))
        self.assertEqual(sp.simplify(ell / (32/a)), a ** F(15, 16) / 32)

    def test_06_separator_coverage_bound(self) -> None:
        for ell in (2, 3, 5, 8):
            for n in (8*(ell+1), 17*(ell+1)+ell):
                covered = core_coverage_fraction(n, ell)
                missing = 1 - covered
                rhs = F(4, ell) + F(4*ell, n)
                self.assertLessEqual(missing, rhs)

    def test_07_bad_core_fraction_algebra(self) -> None:
        # M_n <=24 n^4 in d=4; bad cores each cost >eps.
        a = sp.symbols('a', positive=True)
        ell_upper = 2 * a ** F(-1, 16)
        eps = a ** F(1, 2)
        bound = sp.simplify(24 * a * ell_upper**4 / eps)
        self.assertEqual(bound, 384 * a ** F(1, 4))

    def test_08_quadratic_comparison_scales(self) -> None:
        # With ceil(a^-1/16)<=2a^-1/16, tree-gauge max angle and
        # the Taylor-remainder multiplier have these powers.
        a = sp.symbols('a', positive=True)
        ell_upper = 2 * a ** F(-1, 16)
        eps = a ** F(1, 2)
        delta_power = sp.simplify(sp.sqrt(ell_upper * eps))
        remainder_power = sp.simplify(ell_upper**3 * sp.sqrt(eps))
        self.assertEqual(delta_power / sp.sqrt(2), a ** F(7, 32))
        self.assertEqual(remainder_power / 8, a ** F(1, 16))

    def test_09_micro_macro_separation(self) -> None:
        a = sp.symbols('a', positive=True)
        ell_upper = 2 * a ** F(-1, 16)
        n_lower = 32 / a
        self.assertEqual(sp.simplify(ell_upper / n_lower), a ** F(15, 16) / 16)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument('--output', type=Path, required=True)
    args = ap.parse_args()
    start = time.perf_counter()
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(Checks)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    payload = {
        'status': 'passed' if result.wasSuccessful() else 'failed',
        'tests_run': result.testsRun,
        'failures': len(result.failures),
        'errors': len(result.errors),
        'seconds': time.perf_counter() - start,
        'python': platform.python_version(),
        'sympy': sp.__version__,
        'arithmetic': 'exact integer/Fraction/SymPy combinatorics; no floating scientific decisions',
        'finite_geometry_range': 'all edges for d=2,3,4 and n=1,2,3; additional d=4 count cases',
        'seed': None,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2) + '\n')
    if not result.wasSuccessful():
        raise SystemExit(1)


if __name__ == '__main__':
    main()

"""U030: exact overlap certificates and finite transfer-memory controls.

Run from the project root:
  python checks/U030_overlap_and_transfer_checks.py --output evidence/U030_checks.json

Rational intervals certify scalar group-integral coefficients and character tails.
The separate mpmath quadrature is corroboration, not an interval proof.
No lattice simulation, physical mass measurement, or infinite-volume test occurs.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
from itertools import product
import json
from math import ceil, factorial
from pathlib import Path
import platform
import time
import unittest

import mpmath as mp
import sympy as sp

from U029_exact_link_integration_checks import (
    haar_even, outward_decimal, periodic_faces, positive_series_interval,
    ratio_certificate, selected,
)

Point = tuple[int, ...]
Edge = tuple[Point, int]
Interval = tuple[Q, Q]


def character_ratio(z: Q, label: int, digits: int = 26) -> Interval:
    """Enclose I_(label+1)(z)/I_1(z); continuous values at z=0."""
    if z < 0 or label < 0 or digits < 1:
        raise ValueError('nonnegative argument/label and positive precision required')
    if label == 0:
        return Q(1), Q(1)
    if z == 0:
        return Q(0), Q(0)
    terms = max(1, ceil(z))
    prefactor = (z/2)**label
    while terms < 4096:
        dl, du = positive_series_interval(z, 1, terms)
        nl, nu = positive_series_interval(z, label+1, terms)
        lo, hi = prefactor*nl/du, min(Q(1), prefactor*nu/dl)
        if hi-lo < Q(1, 10**digits):
            return lo, hi
        terms += 8
    raise RuntimeError('4096-term cap exceeded')


def character_value(label: int, half_trace: Q) -> Q:
    if label < 0 or not -1 <= half_trace <= 1:
        raise ValueError('require label>=0 and half trace in [-1,1]')
    if label == 0:
        return Q(1)
    prev, cur = Q(1), 2*half_trace
    for _ in range(1, label):
        prev, cur = cur, 2*half_trace*cur-prev
    return cur


def convolution_tail(a: Q, c: Q, beta: Q, degree: int) -> Q:
    """Uniform absolute tail after degree for normalized fourfold convolution."""
    if min(a, c, beta) < 0 or degree < 0:
        raise ValueError('nonnegative inputs required')
    x = a*c*beta*beta/16
    first = x**(degree+1)*Q((degree+2)**2, factorial(degree+2)**4)
    ratio = x/Q((degree+2)**2*(degree+3)**2)
    if ratio >= 1:
        raise ValueError('degree too small for the geometric tail bound')
    return first/(1-ratio)


def convolution_certificate(a: Q, c: Q, beta: Q, half_trace: Q,
                            digits: int = 18) -> tuple[Q, Q, int, Q]:
    """Normalized integral divided by Z(a)Z(c)Z(beta)^2; no log taken."""
    if min(a, c, beta) < 0 or not -1 <= half_trace <= 1 or digits < 1:
        raise ValueError('invalid convolution certificate input')
    target = Q(1, 10**digits)
    for degree in range(512):
        try:
            tail = convolution_tail(a, c, beta, degree)
        except ValueError:
            continue
        if tail < target/8:
            break
    else:
        raise RuntimeError('512-label tail cap exceeded')
    lo, hi = Q(0), Q(0)
    for label in range(degree+1):
        al, au = character_ratio(a, label, digits+12)
        cl, cu = character_ratio(c, label, digits+12)
        bl, bu = character_ratio(beta, label, digits+12)
        wl, wu = al*cl*bl*bl, au*cu*bu*bu
        factor = (label+1)*character_value(label, half_trace)
        if factor >= 0:
            lo += factor*wl
            hi += factor*wu
        else:
            lo += factor*wu
            hi += factor*wl
    lo, hi = lo-tail, hi+tail
    if hi-lo >= target:
        raise RuntimeError('coefficient rounding budget did not meet requested width')
    return lo, hi, degree, tail


def shift(x: Point, mu: int, step: int, side: int) -> Point:
    y = list(x)
    y[mu] = (y[mu]+step) % side
    return tuple(y)


def chain_boundary(dimension: int, side: int) -> tuple[tuple[Edge, ...], dict[Edge, sp.Matrix]]:
    """Actual time-link chain, with external staple sums zero in d=4."""
    if dimension != 4 or side < 6 or side % 2:
        raise ValueError('this exact witness uses d=4, even side>=6')
    sites = tuple((0, j, 0, 0) for j in range(3))
    chain = tuple((x, 0) for x in sites)
    eye = sp.eye(2)
    minus = -eye
    # I,-I plus the exact three cube roots of I in a maximal torus.
    plus_root = sp.diag(-sp.Rational(1,2)+sp.I*sp.sqrt(3)/2,
                        -sp.Rational(1,2)-sp.I*sp.sqrt(3)/2)
    minus_root = plus_root.conjugate().T
    end_values = [eye, minus, eye, plus_root, minus_root]
    mid_values = [eye, minus, eye, minus]
    assigned: dict[Edge, sp.Matrix] = {}
    for j, x in enumerate(sites):
        external = [(shift(x, mu, step, side), 0)
                    for mu in range(1, dimension) for step in (-1,1)
                    if (shift(x, mu, step, side), 0) not in chain]
        values = mid_values if j == 1 else end_values
        if len(external) != len(values):
            raise AssertionError('wrong external-staple count')
        for edge, value in zip(external, values, strict=True):
            if edge in assigned:
                raise AssertionError('external middle edge unexpectedly shared')
            assigned[edge] = value
    return chain, assigned


def memory_example() -> tuple[sp.Matrix, sp.Matrix, sp.Matrix, sp.Matrix]:
    omega = sp.Matrix([1,1,1,1])/2
    u = sp.Matrix([1,1,-1,-1])/2
    v = sp.Matrix([1,-1,1,-1])/2
    w = sp.Matrix([1,-1,-1,1])/2
    k = omega*omega.T+(u*u.T+v*v.T+w*w.T)/4+(u*v.T+v*u.T)/8
    p = omega*omega.T+u*u.T
    return k, p, u, v


class OverlapTests(unittest.TestCase):
    def test_actual_overlapping_star_geometry(self) -> None:
        for side in (6,8):
            chain, _ = chain_boundary(4,side)
            counts = {edge: 0 for edge in chain}
            pairs: dict[tuple[int, ...], int] = {}
            for face in periodic_faces(4,side):
                hit = tuple(i for i, edge in enumerate(chain) if edge in face)
                for i in hit:
                    counts[chain[i]] += 1
                if len(hit) >= 2:
                    pairs[hit] = pairs.get(hit,0)+1
            self.assertEqual(list(counts.values()), [6,6,6])
            self.assertEqual(pairs, {(0,1):1, (1,2):1})
            self.assertTrue(selected(chain[0]) and selected(chain[2]))
            self.assertFalse(selected(chain[1]))

    def test_realizable_cancelling_boundary_staples(self) -> None:
        chain, assigned = chain_boundary(4,6)
        self.assertEqual(len(assigned),14)
        for mat in assigned.values():
            self.assertEqual(sp.simplify(mat.conjugate().T*mat),sp.eye(2))
            self.assertEqual(sp.simplify(mat.det()),1)
        for x,_ in chain:
            external = [(shift(x,mu,s,6),0) for mu in range(1,4) for s in (-1,1)
                        if (shift(x,mu,s,6),0) not in chain]
            total = sum((assigned[e] for e in external),sp.zeros(2))
            self.assertEqual(sp.simplify(total),sp.zeros(2))
        source_edges = (((0,0,1,0),0), ((0,2,1,0),0))
        self.assertTrue(all(assigned[e] == sp.eye(2) for e in source_edges))
        self.assertFalse(any(all(e in face for e in source_edges)
                             for face in periodic_faces(4,6)))
        # All transverse links are I. Each actual three-edge detour therefore
        # equals its assigned, distinct, parallel middle link (both signs).

    def test_connected_response_leading_coefficient(self) -> None:
        # Haar second moments on S^3: E[u_i u_j]=delta_ij/4.
        # For e^{beta(u.v+v.w)}, the beta^2 u0*w0 numerator is exactly 1/64.
        value = sum(Q(int(i==0),4)*Q(int(i==j),4)*Q(int(j==0),4)
                    for i,j in product(range(4),repeat=2))
        self.assertEqual(value,Q(1,64))
        beta=sp.Symbol('beta')
        z=sum(sp.Rational(haar_even(k))*beta**(2*k)/factorial(2*k) for k in range(5))
        r=sp.series(sp.diff(z,beta)/z,beta,0,6).removeO()
        self.assertEqual(sp.expand(r*r/4).coeff(beta,2),sp.Rational(1,64))
        self.assertNotEqual(value,0)  # independent endpoint marginals give 0

    def test_character_coefficients_from_haar_moments(self) -> None:
        x=sp.Symbol('x')
        for label in range(6):
            char=sp.Poly(sp.chebyshevu(label,x),x)
            for power in range(14):
                integral=sp.Rational(0)
                for (degree,), coeff in char.terms():
                    if (degree+power)%2 == 0:
                        integral += coeff*sp.Rational(haar_even((degree+power)//2))/factorial(power)
                if power>=label and (power-label)%2 == 0:
                    k=(power-label)//2
                    expected=sp.Rational(label+1,2**power*factorial(k)*factorial(k+label+1))
                else:
                    expected=0
                self.assertEqual(integral,expected)

    def test_uniform_character_tail_ratio(self) -> None:
        l,x=sp.symbols('l x',positive=True,integer=True)
        t=x**l*(l+1)**2/sp.factorial(l+1)**4
        self.assertEqual(sp.simplify(t.subs(l,l+1)/t),x/((l+1)**2*(l+2)**2))
        for h in (Q(-1),Q(0),Q(3,5),Q(1)):
            for label in range(21):
                self.assertLessEqual(abs(character_value(label,h)),label+1)

    def test_rational_connected_response_certificates(self) -> None:
        for beta in (Q(0),Q(1),Q(6),Q(24),Q(96)):
            lo,hi,_=ratio_certificate(beta,26)
            if beta:
                self.assertGreater(lo,0)
                self.assertLess(hi,1)
            self.assertLess(hi*hi-lo*lo,Q(1,10**24))
            l1,h1=character_ratio(beta,1)
            self.assertLessEqual(l1,hi)
            self.assertGreaterEqual(h1,lo)

    def test_fourfold_certificate_and_zero_sources(self) -> None:
        lo,hi,_,_=convolution_certificate(Q(0),Q(3),Q(4),Q(3,5))
        self.assertEqual((lo,hi),(Q(1),Q(1)))
        for h in (Q(-1),Q(0),Q(3,5),Q(1)):
            lo,hi,_,_=convolution_certificate(Q(2),Q(3),Q(4),h)
            self.assertGreater(lo,0)
            self.assertLess(hi-lo,Q(1,10**18))
        # Aligned fields produce a strict connected enhancement over 1.
        lo,_,_,_=convolution_certificate(Q(2),Q(3),Q(4),Q(1))
        self.assertGreater(lo,1)

    def test_aligned_boundary_covariance(self) -> None:
        # External sums are 5I,4I,5I; two shared faces make all diagonals 6.
        m=sp.Matrix([[6,-1,0],[-1,6,-1],[0,-1,6]])
        inv=m.inv()
        self.assertEqual(inv[0,0],sp.Rational(35,204))
        self.assertEqual(inv[0,2],sp.Rational(1,204))
        self.assertEqual(inv[0,2]/inv[0,0],sp.Rational(1,35))
        self.assertEqual((inv[0,2]/inv[0,0])**2,sp.Rational(1,1225))
        self.assertEqual(m.charpoly().as_expr().factor(),
                         (sp.Symbol('lambda')-6)*(sp.Symbol('lambda')**2-12*sp.Symbol('lambda')+34))

    def test_exact_positive_markov_memory_counterexample(self) -> None:
        k,p,u,v=memory_example()
        self.assertEqual(k,k.T)
        self.assertEqual(k*sp.ones(4,1),sp.ones(4,1))
        self.assertTrue(all(x>=0 for x in k))
        self.assertEqual(set(k.eigenvals()),{sp.Rational(1),sp.Rational(3,8),sp.Rational(1,4),sp.Rational(1,8)})
        self.assertEqual(p,sp.diag(sp.ones(2)/2,sp.ones(2)/2))
        q=sp.eye(4)-p
        defect=p*k*k*p-p*k*p*k*p
        self.assertEqual(defect,p*k*q*k*p)
        self.assertEqual(defect,u*u.T/64)
        self.assertEqual((u.T*k*u)[0],sp.Rational(1,4))
        self.assertEqual((u.T*k*v)[0],sp.Rational(1,8))

    def test_exact_memory_recurrence_and_schur_loss(self) -> None:
        k,p,u,_=memory_example()
        q=sp.eye(4)-p
        a,b,d=p*k*p,p*k*q,q*k*q
        moments=[p*k**n*p for n in range(8)]
        for n in range(1,7):
            rhs=a*moments[n]
            for j in range(n):
                rhs += b*(d**(n-1-j))*b.T*moments[j]
            self.assertEqual(moments[n+1],rhs)
        memory=(u.T*b*(sp.eye(4)-d).inv()*b.T*u)[0]
        self.assertEqual(memory,sp.Rational(1,48))
        self.assertEqual(1-sp.Rational(1,4)-memory,sp.Rational(35,48))
        self.assertNotEqual(moments[2],a*a)

    def test_invalid_inputs_are_rejected(self) -> None:
        for call in (lambda:character_ratio(Q(-1),1), lambda:character_value(-1,Q(0)),
                     lambda:convolution_tail(Q(100),Q(100),Q(100),0),
                     lambda:chain_boundary(4,4),lambda:convolution_certificate(Q(1),Q(1),Q(1),Q(2))):
            with self.assertRaises(ValueError):
                call()


def quadrature_cross_checks() -> list[dict[str,str]]:
    """Independent direct one-dimensional integral for aligned endpoint sources."""
    rows=[]
    with mp.workdps(50):
        def z(t):
            return mp.mpf(1) if not t else 2*mp.besseli(1,t)/t
        for a,c,beta in ((1,1,1),(2,3,4),(4,4,8)):
            integral=mp.quad(lambda th:(2/mp.pi)*mp.sin(th)**2*
                             z(mp.sqrt(a*a+beta*beta+2*a*beta*mp.cos(th)))*
                             z(mp.sqrt(c*c+beta*beta+2*c*beta*mp.cos(th))),
                             [0,mp.pi/2,mp.pi])/(z(a)*z(c)*z(beta)**2)
            lo,hi,degree,tail=convolution_certificate(Q(a),Q(c),Q(beta),Q(1))
            ml,mh=mp.mpf(lo.numerator)/lo.denominator,mp.mpf(hi.numerator)/hi.denominator
            if not ml<=integral<=mh:
                raise AssertionError('noncertified quadrature conflicts with rational enclosure')
            rows.append({'a':str(a),'c':str(c),'beta':str(beta),'degree':str(degree),
                         'lower':outward_decimal(lo,18,False),'upper':outward_decimal(hi,18,True),
                         'quadrature_noncertificate':mp.nstr(integral,42),
                         'uniform_tail_upper':outward_decimal(tail,24,True)})
    return rows


def main() -> int:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    start=time.perf_counter()
    tests=unittest.defaultTestLoader.loadTestsFromTestCase(OverlapTests)
    result=unittest.TextTestRunner(verbosity=2).run(tests)
    if not result.wasSuccessful():
        return 1
    ratios=[]
    for beta in (Q(0),Q(1),Q(6),Q(24),Q(96)):
        lo,hi,terms=ratio_certificate(beta,26)
        ratios.append({'beta':str(beta),'terms':terms,
                       'endpoint_correlation_lower':outward_decimal(lo*lo,22,False),
                       'endpoint_correlation_upper':outward_decimal(hi*hi,22,True)})
    evidence={'scope':'finite conditional-link identities and abstract transfer memory; NOT a physical Yang-Mills gap',
              'tests_run':result.testsRun,'tests_passed':True,
              'software':{'python':platform.python_version(),'sympy':sp.__version__,'mpmath':mp.__version__},
              'arithmetic':'Fraction and SymPy exact; mpmath quadrature explicitly noncertified',
              'endpoint_correlation_certificates':ratios,
              'fourfold_convolution_checks':quadrature_cross_checks(),
              'aligned_trace_correlation_limit':'1/1225 (analytic fixed-three-link Laplace limit)',
              'memory_two_step_defect':'1/64 on the normalized coarse centered vector',
              'elapsed_seconds':time.perf_counter()-start}
    text=json.dumps(evidence,indent=2)+'\n'
    print(text,end='')
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(text,encoding='utf-8')
    return 0


if __name__=='__main__':
    raise SystemExit(main())

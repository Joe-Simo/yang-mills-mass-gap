"""Exact checks for one SU(2) Wilson-link marginal, not a mass-gap proof.

Run: python checks/U029_exact_link_integration_checks.py --output evidence/U029_checks.json
The rational series tails are certificates. Decimal quadrature is a separate,
noncertified corroboration. No Monte Carlo, fitted spectrum, or RG iteration.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
from itertools import combinations, product
import json
from math import ceil, factorial
from pathlib import Path
import platform
import time
import unittest

import mpmath as mp
import sympy as sp


def haar_even(k: int) -> Q:
    if k < 0:
        raise ValueError('nonnegative moment index required')
    return Q(factorial(2*k), 4**k*factorial(k)*factorial(k+1))


def positive_series_interval(z: Q, order: int, terms: int) -> tuple[Q, Q]:
    """Enclose sum (z²/4)^k/[k!(k+order)!], k>=0, by rational tails."""
    if z < 0 or order < 1 or terms < 0:
        raise ValueError('require z>=0, order>=1, and terms>=0')
    power = z*z/4
    term = Q(1, factorial(order))
    total = term
    for k in range(terms):
        term *= power/Q((k+1)*(k+order+1))
        total += term
    nxt = term*power/Q((terms+1)*(terms+order+1))
    ratio = power/Q((terms+2)*(terms+order+2))
    if ratio >= 1:
        raise ValueError('insufficient terms for decreasing geometric tail')
    return total, total+nxt/(1-ratio)


def ratio_certificate(z: Q, digits: int = 24) -> tuple[Q, Q, int]:
    """Certify I_2(z)/I_1(z) by its convergent positive series; r(0)=0."""
    if z < 0 or digits < 1:
        raise ValueError('invalid ratio-certificate input')
    if z == 0:
        return Q(0), Q(0), 0
    terms = max(1, ceil(z))
    while terms < 4096:
        al, au = positive_series_interval(z, 1, terms)
        bl, bu = positive_series_interval(z, 2, terms)
        lower, upper = z*bl/(2*au), z*bu/(2*al)
        if upper-lower < Q(1, 10**digits):
            return lower, upper, terms
        terms += 8
    raise RuntimeError('declared 4096-term certificate cap exceeded')


def outward_decimal(q: Q, digits: int, upper: bool) -> str:
    scale = 10**digits
    scaled = q*scale
    integer = -((-scaled.numerator)//scaled.denominator) if upper else scaled.numerator//scaled.denominator
    sign = '-' if integer < 0 else ''
    integer = abs(integer)
    return f'{sign}{integer//scale}.{integer%scale:0{digits}d}'


def su2(q: tuple[Q, Q, Q, Q]) -> sp.Matrix:
    if sum(v*v for v in q) != 1:
        raise ValueError('unit quaternion required')
    a,b,c,d = map(sp.Rational, q)
    return sp.Matrix([[a+sp.I*d, c+sp.I*b], [-c+sp.I*b, a-sp.I*d]])


def periodic_faces(d: int, n: int):
    """Return underlying unoriented edges of every positively oriented face."""
    for x in product(range(n), repeat=d):
        for mu,nu in combinations(range(d), 2):
            xp=list(x); xp[mu]=(xp[mu]+1)%n
            xq=list(x); xq[nu]=(xq[nu]+1)%n
            yield ((x,mu),(tuple(xp),nu),(tuple(xq),mu),(x,nu))


def selected(edge: tuple[tuple[int, ...], int]) -> bool:
    x,mu=edge
    return mu == 0 and sum(x[1:])%2 == 0


class ExactLinkTests(unittest.TestCase):
    def test_haar_integral_series_coefficients(self) -> None:
        # Implemented range only; the all-order proof is in the research note.
        for k in range(13):
            self.assertEqual(haar_even(k)/factorial(2*k),Q(1,4**k*factorial(k)*factorial(k+1)))
        z=sp.Symbol('z')
        series=sum(sp.Rational(haar_even(k))*z**(2*k)/factorial(2*k) for k in range(5))
        self.assertEqual(sp.series(sp.log(series),z,0,10).removeO(),
                         z**2/8-z**4/384+z**6/9216-z**8/184320)

    def test_all_order_ward_identity_coefficient_formula(self) -> None:
        k=sp.Symbol('k', integer=True, nonnegative=True)
        # M_(k+1)/M_k=(2k+1)/(2k+4); this is precisely the Ward recurrence.
        ratio=sp.Rational(1,2)*(2*k+1)/(k+2)
        self.assertEqual(sp.simplify(ratio-(2*k+1)*(1-ratio)/3),0)
        for j in range(16):
            self.assertEqual(haar_even(j+1)/factorial(2*j+1),
                             (haar_even(j)-haar_even(j+1))/(3*factorial(2*j)))

    def test_quaternion_staple_and_endpoint_covariance(self) -> None:
        data=[(Q(1),Q(0),Q(0),Q(0)),(Q(3,5),Q(4,5),Q(0),Q(0)),
              (Q(0),Q(0),Q(1),Q(0)),(Q(0),Q(0),Q(0),Q(1))]
        vs=[su2(q) for q in data]
        h=sum(vs,sp.zeros(2)); s2=sp.simplify(h.det())
        pair=4+sum(sp.trace(vs[i]*vs[j].conjugate().T) for i,j in combinations(range(4),2))
        self.assertEqual(sp.simplify(s2-pair),0)
        self.assertEqual(sp.simplify(h.conjugate().T*h-s2*sp.eye(2)),sp.zeros(2))
        left,right=vs[1],vs[2]
        ht=sum([left*v*right.conjugate().T for v in vs],sp.zeros(2))
        self.assertEqual(sp.simplify(ht.det()-s2),0)
        self.assertNotEqual(vs[1]*vs[2],vs[2]*vs[1])

    def test_exact_hessian_cancels_common_gauge_direction(self) -> None:
        for m in (1,2,4,6):
            h=sp.eye(m)-sp.ones(m)/m
            self.assertEqual(h*sp.ones(m,1),sp.zeros(m,1))
            self.assertEqual(h*h,h)
            self.assertEqual(h.rank(),m-1)
            x=sp.Matrix(sp.symbols(f'x0:{m}'))
            lhs=sp.expand((x.T*h*x)[0])
            rhs=sum((x[i]-x[j])**2 for i,j in combinations(range(m),2))/m
            self.assertEqual(sp.expand(lhs-rhs),0)
        # Deliberate rejected candidate: averaging S'' alone gives identity,
        # not the centered Hessian I-11*/m.
        self.assertEqual((sp.eye(6)*sp.ones(6,1)).norm()**2,6)

    def test_nonlinear_pair_quartic_includes_commutator(self) -> None:
        t,a,b,c=sp.symbols('t a b c', real=True)
        cos_a=1-a*t**2/2+a*a*t**4/24
        cos_b=1-b*t**2/2+b*b*t**4/24
        sinc_a=t-a*t**3/6
        sinc_b=t-b*t**3/6
        deficit=sp.series(1-cos_a*cos_b-c*sinc_a*sinc_b,t,0,6).removeO()
        expected=(a+b-2*c)*t**2/2-((a+b-2*c)**2/24+(a*b-c*c)/6)*t**4
        self.assertEqual(sp.expand(deficit-expected),0)
        # For orthogonal generators this is cos(t)^2, not cos(sqrt(2)t).
        actual=sp.series(1-sp.cos(t)**2,t,0,6).removeO()
        self.assertEqual(actual,t*t-t**4/3)
        self.assertNotEqual(actual,sp.series(1-sp.cos(sp.sqrt(2)*t),t,0,6).removeO())

    def test_general_log_composition_quartic(self) -> None:
        t,A,B,m,beta,r,rp=sp.symbols('t A B m beta r rp', positive=True)
        ds=-A*t**2/(2*m)+(B/(2*m)-A*A/(8*m**3))*t**4
        g=sp.series(-r*beta*ds-rp*beta**2*ds*ds/2,t,0,6).removeO()
        target=beta*r*A*t*t/(2*m)+(-beta*r*B/(2*m)+beta*(r-m*beta*rp)*A*A/(8*m**3))*t**4
        self.assertEqual(sp.expand(g-target),0)

    def test_induced_action_is_not_one_wilson_coupling(self) -> None:
        # Two-staple variable delta=1-ReTr(V1 V2*)/2, s²=4-2delta.
        b,d=sp.symbols('b d')
        f=lambda u:b*b*u/8-b**4*u*u/384+b**6*u**3/9216
        marginal=sp.expand(f(4)-f(4-2*d))
        self.assertEqual(marginal.coeff(b,4).coeff(d,2),sp.Rational(1,96))
        self.assertEqual(marginal.coeff(b,2),d/4)
        # This endpoint second derivative is exact at every beta: u^k, k>=3,
        # has zero second derivative at u=4-2delta=0.
        self.assertEqual(sp.diff(marginal,d,2).subs(d,2),b**4/48)

    def test_exact_frustration_boundary_is_realizable(self) -> None:
        # Every detour has a distinct middle link parallel to the target edge.
        for dim in (3,4):
            x=(2,)*dim; signs={}; midpoints=[]
            for nu in range(1,dim):
                for direction in (-1,1):
                    p=list(x); p[nu]+=direction
                    midpoints.append(tuple(p))
            self.assertEqual(len(set(midpoints)),2*(dim-1))
            m=len(midpoints)
            for j,p in enumerate(midpoints): signs[(p,0)]=1 if j<m//2 else -1
            # All transverse legs set to I; their inverses are also I.
            staples=[signs[(p,0)]*sp.eye(2) for p in midpoints]
            self.assertEqual(sum(staples,sp.zeros(2)),sp.zeros(2))
            self.assertEqual(positive_series_interval(Q(0),1,0),(Q(1),Q(1)))
        # Uniform Haar cap of angle <=pi/2 has exactly probability 1/2.
        th=sp.Symbol('th',real=True)
        self.assertEqual(sp.integrate(2*sp.sin(th)**2/sp.pi,(th,0,sp.pi/2)),sp.Rational(1,2))

    def test_simultaneous_decimation_has_no_shared_faces(self) -> None:
        for d,n in ((3,4),(4,4),(4,6)):
            count=0
            for face in periodic_faces(d,n):
                self.assertLessEqual(sum(selected(e) for e in face),1)
                count+=1
            self.assertEqual(count,d*(d-1)//2*n**d)
            for x in product(range(n),repeat=d):
                reflected=(((-x[0]-1)%n,)+x[1:],0)
                self.assertEqual(selected((x,0)),selected(reflected))

    def test_geometric_tail_control_and_input_rejections(self) -> None:
        for z in (Q(0),Q(1,2),Q(2),Q(6),Q(24)):
            m=max(2,ceil(z))
            lo,hi=positive_series_interval(z,1,m)
            lo2,hi2=positive_series_interval(z,1,m+10)
            self.assertLessEqual(lo,lo2); self.assertLessEqual(hi2,hi)
            rl,ru,_=ratio_certificate(z)
            self.assertGreaterEqual(rl,0); self.assertLess(ru,1)
        with self.assertRaises(ValueError): positive_series_interval(Q(20),1,0)
        with self.assertRaises(ValueError): ratio_certificate(Q(-1))
        with self.assertRaises(ValueError): su2((Q(2),Q(0),Q(0),Q(0)))

    def test_quadratic_remainder_constant_algebra(self) -> None:
        # 1-sincos pair t² remainder via fourth derivative <= (|X|+|Y|)^4.
        m=sp.Symbol('m',integer=True,positive=True)
        constant=(m-1)/3+2*(m-1)**2/m
        self.assertEqual(sp.simplify(constant-(m-1)*(7*m-6)/(3*m)),0)
        # Used bound is C_m=(m-1)/3+2(m-1)^2/m, not an n-dependent term.


def evidence() -> dict[str,object]:
    certificates=[]; quadrature=[]
    for z in (Q(0),Q(1,2),Q(2),Q(6),Q(24),Q(96)):
        lo,hi,terms=ratio_certificate(z)
        certificates.append({'z':str(z),'r_lower':outward_decimal(lo,16,False),
                             'r_upper':outward_decimal(hi,16,True),
                             'terms_through_k':terms,'internal_width_lt':'1e-24',
                             'method':'exact positive rational series plus decreasing-ratio tail'})
    with mp.workdps(60):
        for z0 in (1,6,24,96):
            z=mp.mpf(z0)
            weight=lambda t:mp.sin(t)**2*mp.exp(z*(mp.cos(t)-1))
            norm=mp.quad(weight,[0,mp.pi/4,mp.pi/2,mp.pi])
            mean=mp.quad(lambda t:mp.cos(t)*weight(t),[0,mp.pi/4,mp.pi/2,mp.pi])/norm
            perp=mp.quad(lambda t:mp.sin(t)**2*weight(t)/3,[0,mp.pi/4,mp.pi/2,mp.pi])/norm
            bessel=mp.besseli(2,z)/mp.besseli(1,z)
            residual=z*perp-mean
            if abs(residual)>mp.mpf('1e-45') or abs(mean-bessel)>mp.mpf('1e-45'):
                raise RuntimeError('noncertified quadrature cross-check disagrees')
            quadrature.append({'z':z0,'mean':mp.nstr(mean,30),'ward_residual':mp.nstr(residual,8),
                               'naive_action_hessian':mp.nstr(z*mean,30),
                               'covariance_subtraction':mp.nstr(z*z*perp,30),
                               'scope':'60-digit numerical corroboration, not a certificate'})
    return {'arithmetic':'integers/Fraction and SymPy symbolic; separate mpmath corroboration',
            'python':platform.python_version(),'sympy':sp.__version__,'mpmath':mp.__version__,
            'seed':None,'certificates':certificates,'quadrature_cross_checks':quadrature,
            'nonclaims':['No momentum-shell integration','No interacting vacuum or spectral gap computation',
                         'No infinite RG iteration or continuum construction']}


def main() -> int:
    parser=argparse.ArgumentParser(); parser.add_argument('--output',type=Path)
    args=parser.parse_args(); started=time.monotonic()
    result=unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(ExactLinkTests))
    if not result.wasSuccessful(): return 1
    record=evidence(); record['tests_passed']=result.testsRun; record['elapsed_seconds']=time.monotonic()-started
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps(record,indent=2))
    return 0


if __name__=='__main__':
    raise SystemExit(main())

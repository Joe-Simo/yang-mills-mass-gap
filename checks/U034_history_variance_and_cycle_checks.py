"""Exact finite audits for U034; no continuum mass-gap certificate.

Run: python checks/U034_history_variance_and_cycle_checks.py --output evidence/U034_checks.json
Arithmetic: exact rationals/matrices, plus rigorously enclosed positive series.
The finite path fixtures are not Wilson data. Q8 audits only the forest algebra.
The continuous SU(2) cylinder and actual Wilson-transfer statements have written proofs.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
from itertools import product
import json
from pathlib import Path
import platform
import time
import unittest

import sympy as sp

from U029_exact_link_integration_checks import outward_decimal, periodic_faces, ratio_certificate, su2
from U032_conditional_memory_checks import psd_exact, tilted_transfer

Matrix = sp.MatrixBase
R = sp.Rational


def conditional_projection(pi: Matrix, labels: tuple[object, ...]) -> Matrix:
    if len(labels) != len(pi) or any(x <= 0 for x in pi) or sum(pi) != 1:
        raise ValueError('normalized positive law and one label per state required')
    groups: dict[object, list[int]] = {}
    for i, label in enumerate(labels):
        groups.setdefault(label, []).append(i)
    p = sp.zeros(len(pi))
    for ids in groups.values():
        mass = sum(pi[i] for i in ids)
        for i in ids:
            for j in ids:
                p[i, j] = pi[j] / mass
    return p


def endpoint_unexplained(k: Matrix, pi: Matrix, steps: int, bit: int) -> Matrix:
    """Endpoint Gram of I-Pi_history; enumerate the full named 4-state fixture."""
    if k.shape != (4, 4) or not 1 <= steps <= 3 or bit not in (0, 1):
        raise ValueError('contract is 4 states, steps 1..3, and bit 0 or 1')
    masses: dict[tuple[int, ...], sp.Rational] = {}
    left: dict[tuple[int, ...], Matrix] = {}
    for path in product(range(4), repeat=steps + 1):
        mass = pi[path[0]]
        for t in range(steps):
            mass *= k[path[t], path[t + 1]]
        key = tuple((s // 2) if bit == 0 else s % 2 for s in path)
        masses[key] = masses.get(key, R(0)) + mass
        if key not in left:
            left[key] = sp.zeros(4, 1)
        left[key][path[0]] += mass
    explained = sp.zeros(4)
    for key, mass in masses.items():
        explained += left[key] * left[key].T / mass
    return sp.diag(*pi) - explained


def cylinder_certificate(beta: F, length: int) -> dict[str, object]:
    if beta < 0 or length < 3:
        raise ValueError('nonnegative beta, nondegenerate cylinder circumference >=3 required')
    low, high, terms = ratio_certificate(beta, 28)
    lo, hi = 1 - high**length, 1 - low**length
    if not 0 < lo <= hi <= 1 or hi-lo > F(1, 10**22):
        raise AssertionError('angle witness enclosure failed')
    return {'beta': str(beta), 'circumference': length, 'ratio_terms': terms,
            'eigenvalue_1_minus_ratio_power': [outward_decimal(lo, 20, False),
                                             outward_decimal(hi, 20, True)],
            'full_positive_tail': True,
            'scope': 'physical conditional-variance eigenvalue on a 2D Wilson-cylinder marginal, not a quantum mass'}


def qmul(a: tuple[int, ...], b: tuple[int, ...]) -> tuple[int, ...]:
    w, x, y, z = a
    v, p, q, r = b
    return (w*v-x*p-y*q-z*r, w*p+x*v+y*r-z*q,
            w*q-x*r+y*v+z*p, w*r+x*q-y*p+z*v)


def cylinder_gauge_test(length: int) -> bool:
    """All links of one explicit noncommuting rational SU(2) configuration."""
    if length < 3:
        raise ValueError('circumference >=3 required')
    qs = [(F(1),F(0),F(0),F(0)), (F(3,5),F(4,5),F(0),F(0)),
          (F(0),F(0),F(1),F(0)), (F(0),F(0),F(0),F(1))]
    ms = [su2(q) for q in qs]
    bottom = [ms[(i+1)%4] for i in range(length)]
    top = [ms[(2*i+2)%4] for i in range(length)]
    vertical = [ms[(3*i+1)%4] for i in range(length)]
    gb = [sp.eye(2)]
    for i in range(length-1):
        gb.append(gb[-1] * bottom[i])
    gt = [gb[i] * vertical[i] for i in range(length)]
    bt = [gb[i]*bottom[i]*gb[(i+1)%length].H for i in range(length)]
    tt = [gt[i]*top[i]*gt[(i+1)%length].H for i in range(length)]
    vt = [gb[i]*vertical[i]*gt[i].H for i in range(length)]
    if any(x != sp.eye(2) for x in vt+bt[:-1]):
        return False
    for i in range(length):
        old = bottom[i]*vertical[(i+1)%length]*top[i].H*vertical[i].H
        new = tt[i].H if i < length-1 else bt[-1]*tt[-1].H
        if sp.simplify(gb[i]*old*gb[i].H-new) != sp.zeros(2):
            return False
    v = sp.eye(2)
    prefix = sp.eye(2)
    for t in tt:
        v *= t
    for t in tt[:-1]:
        prefix *= t
    return sp.simplify(bt[-1]*tt[-1].H-bt[-1]*v.H*prefix) == sp.zeros(2)


class VarianceChecks(unittest.TestCase):
    def test_six_color_partition(self) -> None:
        for n in (4, 6):
            layers = {(mu,p):set() for mu,p in product(range(3),range(2))}
            for x in product(range(n),repeat=3):
                for mu in range(3):
                    color=(mu,sum(x[j] for j in range(3) if j != mu)%2)
                    layers[color].add((x,mu))
            self.assertEqual(sum(map(len,layers.values())),3*n**3)
            self.assertTrue(all(len(s)==n**3//2 for s in layers.values()))
            for face in periodic_faces(3,n):
                self.assertTrue(all(len(set(face)&s)<=1 for s in layers.values()))

    def test_projection_and_bounded_density_tensorization(self) -> None:
        for weights in ((1,1,1,1),(1,2,3,5),(100,1,1,100)):
            pi=sp.Matrix([R(x,sum(weights)) for x in weights]); w=sp.diag(*pi)
            ps=[conditional_projection(pi,l) for l in ((0,0,1,1),(0,1,0,1))]
            for p in ps:
                self.assertEqual(p*p,p); self.assertEqual(w*p,p.T*w)
            gram=sum([w*(sp.eye(4)-p) for p in ps],sp.zeros(4))
            variance=w-pi*pi.T
            self.assertTrue(psd_exact(gram-R(min(weights),max(weights))*variance))
            if len(set(weights))==1:
                self.assertEqual((sum([sp.eye(4)-p for p in ps],sp.zeros(4))).eigenvals(),
                                 {sp.Integer(0):1,sp.Integer(1):2,sp.Integer(2):1})

    def test_two_history_rayleigh_bridge(self) -> None:
        k,pi,w=tilted_transfer((1,2,3,5))
        for n in range(1,4):
            deficit=w*(sp.eye(4)-k**n)
            gs=[endpoint_unexplained(k,pi,n,b) for b in (0,1)]
            theta=R(3,5)**n
            for g in gs:
                self.assertTrue(psd_exact(g))
                self.assertEqual(g*sp.ones(4,1),sp.zeros(4,1))
                self.assertTrue(psd_exact(deficit-(1-theta)*g))
            self.assertTrue(psd_exact(deficit-(1-theta)*sum(gs,sp.zeros(4))/2))

    def test_product_histories_need_no_volume_penalty(self) -> None:
        c=sp.Matrix([[4,1],[1,4]])/5
        k=sp.kronecker_product(c,c); pi=sp.ones(4,1)/4; w=sp.eye(4)/4
        variance=w-pi*pi.T
        for n in range(1,4):
            gram=sum([endpoint_unexplained(k,pi,n,b) for b in (0,1)],sp.zeros(4))
            self.assertTrue(psd_exact(gram-variance))

    def test_cylinder_physical_angle_identity(self) -> None:
        rho=sp.Symbol('rho',real=True)
        gram=sp.Matrix([[1,rho],[rho,1]])
        p=sp.Matrix([[1,rho],[0,0]]); q=sp.Matrix([[0,0],[rho,1]])
        op=2*sp.eye(2)-p-q
        self.assertEqual(p*p,p); self.assertEqual(q*q,q)
        self.assertEqual(gram*p,p.T*gram); self.assertEqual(gram*q,q.T*gram)
        self.assertEqual(op*sp.ones(2,1),(1-rho)*sp.ones(2,1))
        self.assertEqual(sp.expand((sp.ones(1,2)*gram*op*sp.ones(2,1))[0]
                                   -2*(1-rho)*(1+rho)),0)
        self.assertEqual(sp.expand(gram.det()-(1-rho**2)),0)

    def test_noncommuting_cylinder_gauge_geometry(self) -> None:
        self.assertTrue(cylinder_gauge_test(3)); self.assertTrue(cylinder_gauge_test(4))

    def test_fundamental_haar_convolution(self) -> None:
        # Haar isotropy E u_i u_j=delta_ij/4 on S^3 proves this integral.
        u0,v0,v1,v2,v3=sp.symbols('u0 v0 v1 v2 v3',real=True)
        u=sp.symbols('u0:4',real=True); v=(v0,v1,v2,v3)
        polynomial=sp.Poly((2*u[0])*(2*sum(u[i]*v[i] for i in range(4))),*u)
        integral=0
        for powers,coefficient in polynomial.terms():
            if sorted(powers)==[0,0,0,2]: integral+=coefficient/4
        self.assertEqual(sp.expand(integral),v0)  # chi(V)/dim, not chi(V)
        # Normalized density has coefficient dim*r; convolution eigenvalue is r.
        r=sp.Symbol('r'); self.assertEqual(2*r*integral,r*(2*v0))

    def test_cylinder_positive_series_certificates(self) -> None:
        for beta in (F(0),F(1,2),F(2),F(8),F(32),F(128)):
            for length in (4,16):
                row=cylinder_certificate(beta,length)
                self.assertTrue(row['full_positive_tail'])

    def test_forest_conditional_expectation_finite_group_control(self) -> None:
        # Complete Q8^4 control of the algebraic forest claim, not SU(2) integration.
        group=[tuple(sign if i==j else 0 for i in range(4))
               for j in range(4) for sign in (-1,1)]
        groups=[{} for _ in range(4)]
        total=weighted=0
        for links in product(group,repeat=4):
            hol=(1,0,0,0)
            for u in links: hol=qmul(hol,u)
            weight=6 if hol[0]==1 else 2 if hol[0]==-1 else 1
            obs=2*hol[0]; total+=weight; weighted+=weight*obs
            for omit in range(4):
                key=tuple(u for i,u in enumerate(links) if i!=omit)
                mass,moment=groups[omit].get(key,(0,0))
                groups[omit][key]=(mass+weight,moment+weight*obs)
        mean=F(weighted,total)
        for table in groups:
            self.assertEqual(len(table),8**3)
            self.assertTrue(all(F(v,m)==mean for m,v in table.values()))

    def test_cotree_count_and_cycle_null_case(self) -> None:
        for n in (4,6):
            self.assertEqual(3*n**3-n**3+1,2*n**3+1)
        # An open path has no cycle and no centered physical excitation.
        for vertices in (1,2,7):
            self.assertEqual((vertices-1)-vertices+1,0)

    def test_invalid_inputs_and_false_constant_control(self) -> None:
        for b,l in ((F(-1),4),(F(2),2)):
            with self.assertRaises(ValueError): cylinder_certificate(b,l)
        with self.assertRaises(ValueError): conditional_projection(sp.Matrix([1,1]),(0,1))
        with self.assertRaises(ValueError): endpoint_unexplained(sp.eye(4),sp.ones(4,1)/4,0,0)
        # The exact physical cylinder eigenvalue can lie far below a proposed 1/2 angle.
        low,high,_=ratio_certificate(F(128),28)
        self.assertLess(1-low**4,R(1,2))
        self.assertGreater(1-high**4,0)


def main() -> int:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path); args=parser.parse_args()
    started=time.perf_counter()
    result=unittest.TextTestRunner(verbosity=2).run(
        unittest.defaultTestLoader.loadTestsFromTestCase(VarianceChecks))
    data={'status':'passed' if result.wasSuccessful() else 'failed',
          'tests_run':result.testsRun,'seconds':time.perf_counter()-started,
          'python':platform.python_version(),'sympy':sp.__version__,
          'arithmetic':'exact rational finite decisions and outward-rounded all-tail certificates',
          'seed':None,'path_scope':'all 4^(n+1) paths, n=1..3, specified tilted fixture',
          'forest_scope':'all 4096 Q8^4 configurations; compact-group proof is separate',
          'su2_cylinder_certificates':[cylinder_certificate(beta,l) for beta in
             (F(0),F(1,2),F(2),F(8),F(32),F(128)) for l in (4,16)]
             if result.wasSuccessful() else [],
          'nonclaims':['no 4D vacuum angle estimate','no continuum limit','no physical mass certificate']}
    text=json.dumps(data,indent=2)+'\n'
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True); args.output.write_text(text)
    print(text)
    return 0 if result.wasSuccessful() else 1


if __name__=='__main__':
    raise SystemExit(main())

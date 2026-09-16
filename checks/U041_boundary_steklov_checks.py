"""Exact finite audits for U041; not a Yang--Mills mass-gap certificate.

Run: python checks/U041_boundary_steklov_checks.py --output evidence/U041_checks.json
Finite algebra checks support the written proofs in the U041 audit.
"""
from __future__ import annotations
import argparse, json, math, platform, time, unittest
from fractions import Fraction as F
from pathlib import Path
import sympy as sp

def M(l: int) -> int:
    return 6*l*l*(l+1)*(l+1)

def collar_faces(l: int) -> int:
    if l < 2:
        return M(l)
    return M(l)-M(l-2)

def dtN_rational(l: int, lam: F) -> F:
    if l < 1 or lam < 0:
        raise ValueError
    if l == 1:
        return F(1) + lam
    d0, d1 = F(1), F(2) + lam
    ds=[d0,d1]
    for _k in range(2,l):
        ds.append((F(2)+lam)*ds[-1]-ds[-2])
    return F(1)+lam - ds[l-2]/ds[l-1]

def slab_min_energy(l: int, lam: F, a: F=F(1)) -> F:
    if l==1:
        return F(1,2)*(F(1)+lam)*a*a
    A=sp.zeros(l-1)
    rhs=sp.zeros(l-1,1)
    diag=sp.Rational(2*lam.denominator+lam.numerator,lam.denominator)
    for i in range(l-1):
        A[i,i]=diag
        if i>0: A[i,i-1]=-1
        if i<l-2: A[i,i+1]=-1
    rhs[0,0]=sp.Rational(a.numerator,a.denominator)
    u=A.LUsolve(rhs)
    vals=[sp.Rational(a.numerator,a.denominator)]+[u[i,0] for i in range(l-1)]+[sp.Rational(0)]
    E=sp.Rational(0)
    for r in range(l):
        E += (vals[r+1]-vals[r])**2/2
    for r in range(l+1):
        E += sp.Rational(lam.numerator,lam.denominator)*vals[r]**2/2
    return F(int(sp.numer(E)), int(sp.denom(E)))

def soft_boundary_norm_sq(l: int, t2: F) -> F:
    return t2 * F((l+1)*(l+1)*(2*l+1),6)

def soft_action_upper(l: int, t2: F) -> F:
    return t2 * F((l+1)*(l+1),2)

def low_mode_count(l: int, C: int) -> int:
    lo=-(l//2)
    hi=(l-1)//2
    count=0
    threshold=(C/l)**2
    for i in range(lo,hi+1):
        for j in range(lo,hi+1):
            for k in range(lo,hi+1):
                lam=4*(math.sin(math.pi*i/l)**2+math.sin(math.pi*j/l)**2+math.sin(math.pi*k/l)**2)
                if lam <= threshold+1e-14:
                    count += 1
    return count

class U041Checks(unittest.TestCase):
    def test_01_optimized_exponents(self):
        s=F(1,13); t=F(8,13)
        self.assertEqual(s, 1-4*s-t)
        self.assertEqual(s, (t-6*s)/2)
        self.assertEqual((t-s)/2, F(7,26))
        self.assertEqual(1-s, F(12,13))

    def test_02_maximin_upper_identity(self):
        m,s=sp.symbols('m s')
        self.assertEqual(sp.expand((3*m+10*s).subs(s,m)),13*m)

    def test_03_exact_collar_count(self):
        x=sp.symbols('x', integer=True, positive=True)
        expr=sp.expand(6*x**2*(x+1)**2-6*(x-2)**2*(x-1)**2)
        self.assertEqual(expr,48*x**3-72*x**2+72*x-24)
        for l in (2,3,4,9):
            self.assertEqual(collar_faces(l),48*l**3-72*l**2+72*l-24)

    def test_04_soft_boundary_norm_formula(self):
        for l in (1,2,5,12):
            t2=F(7,19)
            direct=F(0)
            for x1 in range(l+1):
                for _x2 in range(l):
                    for _x3 in range(l+1):
                        direct += t2*F(x1*x1,l*l)
            self.assertEqual(direct,soft_boundary_norm_sq(l,t2))

    def test_05_soft_ratio_bound(self):
        for l in (1,2,3,8,31):
            t2=F(5,17)
            ratio=soft_action_upper(l,t2)/soft_boundary_norm_sq(l,t2)
            self.assertEqual(ratio,F(3,2*l+1))

    def test_06_dtn_exact_minimization(self):
        for l in range(1,8):
            for lam in (F(0),F(1,4),F(1),F(7,3)):
                q=dtN_rational(l,lam)
                E=slab_min_energy(l,lam)
                self.assertEqual(E,F(1,2)*q)

    def test_07_dtn_lower_bounds_finite(self):
        for l in range(1,12):
            for lam in (F(0),F(1,100),F(1,4),F(1),F(4),F(9)):
                q=dtN_rational(l,lam)
                self.assertGreaterEqual(q,F(1,l))
                self.assertGreaterEqual(q*q,lam)

    def test_08_low_mode_count_bound(self):
        for l in (8,16,32,64):
            for C in (1,4,8,12):
                count=low_mode_count(l,C)
                bound=(2*(C//4)+1)**3
                self.assertLessEqual(count,bound)

    def test_09_surface_oscillation_toy(self):
        x=F(1,2); B=3
        z0=z1=F(0)
        for u in range(8):
            inner=(u%3)
            c0=(u//2)%4
            c1=(u//3)%4
            self.assertLessEqual(abs(c0-c1),2*B)
            z0 += x**(inner+c0)
            z1 += x**(inner+c1)
        ratio=z0/z1
        self.assertGreaterEqual(ratio,x**(2*B))
        self.assertLessEqual(ratio,x**(-2*B))

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--output",required=True)
    args=p.parse_args()
    suite=unittest.defaultTestLoader.loadTestsFromTestCase(U041Checks)
    t=time.perf_counter()
    result=unittest.TextTestRunner(verbosity=2).run(suite)
    payload={
        "status":"passed" if result.wasSuccessful() else "failed",
        "tests_run":result.testsRun,
        "failures":len(result.failures),
        "errors":len(result.errors),
        "seconds":time.perf_counter()-t,
        "python":platform.python_version(),
        "sympy":sp.__version__,
        "arithmetic":"exact rational/symbolic except finite Fourier iterator classification",
        "seed":None,
        "claims":[
            "optimized U040 exponent balance",
            "exact collar-face count",
            "exact soft boundary trace norm and O(1/ell) quotient",
            "exact rational slab Dirichlet-to-Neumann Schur complement",
            "finite low-mode-count diagnostics",
            "surface-oscillation toy inequality"
        ],
        "nonclaims":[
            "no continuum Yang-Mills theorem",
            "no nonabelian quantum boundary effective-action coercivity",
            "finite Fourier counts do not prove the universal count bound"
        ]
    }
    Path(args.output).write_text(json.dumps(payload,indent=2))
    raise SystemExit(0 if result.wasSuccessful() else 1)
if __name__=="__main__":
    main()

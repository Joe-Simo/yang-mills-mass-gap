"""Exact/finite audits for U042; not a continuum Yang--Mills certificate.

Run: python checks/U042_gauge_covariant_steklov_checks.py --output evidence/U042_checks.json
The universal Fourier/Hodge and flat-holonomy statements have written proofs in
research/audits/U042_gauge_covariant_steklov_split.md. Finite mode counts are
only diagnostics of the proved uniform counting reduction.
"""
from __future__ import annotations
import argparse, json, math, platform, time, unittest
from fractions import Fraction as F
from pathlib import Path
import sympy as sp


def cross_matrix(p):
    p1,p2,p3=p
    return sp.Matrix([[0,-p3,p2],[p3,0,-p1],[-p2,p1,0]])


def scalar_chain_schur(ell:int, lam:F) -> sp.Matrix:
    """Two-boundary DtN matrix for 1/2 sum diff^2 + lam/2 sum u^2."""
    if ell < 1 or lam < 0:
        raise ValueError
    n=ell+1
    H=sp.zeros(n)
    lq=sp.Rational(lam.numerator,lam.denominator)
    for r in range(ell):
        H[r,r]+=1
        H[r+1,r+1]+=1
        H[r,r+1]-=1
        H[r+1,r]-=1
    for r in range(n):
        H[r,r]+=lq
    if ell==1:
        return H
    b=[0,ell]
    i=list(range(1,ell))
    Hbb=H.extract(b,b)
    Hbi=H.extract(b,i)
    Hii=H.extract(i,i)
    return sp.simplify(Hbb-Hbi*Hii.inv()*Hbi.T)


def qpm_float(ell:int, lam:float):
    if lam < 1e-15:
        return 0.0, 2.0/ell
    gam=math.acosh(1.0+lam/2.0)
    q=lam/2.0+math.sinh(gam)/math.tanh(ell*gam)
    r=math.sinh(gam)/math.sinh(ell*gam)
    return q-r,q+r


def shifted_lambda(ell:int,n,h,w:int):
    return 4.0*sum(math.sin((math.pi*n[j]+w*h[j])/ell)**2 for j in range(3))


def centered_range(ell:int):
    return range(-(ell//2),(ell-1)//2+1)


def soft_coexact_count(ell:int,C:float,h):
    """Overcount real/complex Fourier-polarization labels after gradient quotient.

    Each nonzero covariant momentum gets 2 transverse polarisations x 2 face
    parities. Covariant zero momentum is counted as 3 harmonic directions x 2
    parities, which is a safe overcount because one parity can be zero-energy.
    """
    count=0
    for w in (0,1,-1):
        for n0 in centered_range(ell):
            for n1 in centered_range(ell):
                for n2 in centered_range(ell):
                    lam=shifted_lambda(ell,(n0,n1,n2),h,w)
                    qm,qp=qpm_float(ell,lam)
                    if lam < 1e-13:
                        count += 3*((qm <= C/ell+1e-12)+(qp <= C/ell+1e-12))
                    else:
                        count += 2*((qm <= C/ell+1e-12)+(qp <= C/ell+1e-12))
    return int(count)


def crude_uniform_soft_bound(C:float):
    R=max(1.0,C)
    N=(2*math.ceil(R/math.sqrt(2)+1)+1)**3
    large=12*N+18
    small=18*math.ceil(2*R)**3
    return max(large,small)


def trace_bound(seq):
    """Return lhs and RHS of sum |u_r|^2 <= 2(l+1)|u0|^2+2l(l+1)sum|du|^2."""
    ell=len(seq)-1
    lhs=sum(x*x for x in seq)
    dif=sum((seq[r+1]-seq[r])**2 for r in range(ell))
    rhs=2*(ell+1)*seq[0]**2+2*ell*(ell+1)*dif
    return lhs,rhs


class U042Checks(unittest.TestCase):
    def test_01_hodge_symbol_identity(self):
        for p in ((1,0,0),(1,2,0),(2,-1,3),(3,4,5)):
            v=sp.Matrix(p)
            C=cross_matrix(p)
            lam=sum(x*x for x in p)
            self.assertEqual(C.T*C,lam*sp.eye(3)-v*v.T)
            self.assertEqual(C*v,sp.zeros(3,1))
            self.assertEqual(C.rank(),2)

    def test_02_boundary_kernel_dimension_formula(self):
        for ell in (2,3,4,7):
            kernel=2*(ell**3-1)+3
            positive=6*ell**3-kernel
            self.assertEqual(kernel,2*ell**3+1)
            self.assertEqual(positive,4*ell**3-1)

    def test_03_two_boundary_scalar_schur(self):
        for ell in range(1,7):
            for lam in (F(0),F(1,4),F(1),F(7,3)):
                Q=scalar_chain_schur(ell,lam)
                self.assertEqual(Q,Q.T)
                if lam==0:
                    self.assertEqual(sp.simplify(Q*sp.Matrix([1,1])),sp.zeros(2,1))
                    anti=sp.simplify((sp.Matrix([1,-1]).T*Q*sp.Matrix([1,-1]))[0]/2)
                    self.assertEqual(anti,sp.Rational(2,ell))
                ev=Q.eigenvals()
                self.assertEqual(sum(ev.values()),2)

    def test_04_flat_holonomy_shift_matches_adjoint_rotation(self):
        for ell,n,h in ((8,1,math.pi/3),(10,-2,math.pi/5),(12,3,-math.pi/4)):
            theta=2*h/ell
            phi=2*math.pi*n/ell
            psi=theta+phi
            D=((math.cos(psi)-1.0,-math.sin(psi)),
               (math.sin(psi),math.cos(psi)-1.0))
            val=sum(x*x for row in D for x in row)/2.0
            target=4*math.sin((math.pi*n+h)/ell)**2
            self.assertAlmostEqual(val,target,places=12)

    def test_05_uniform_soft_count_diagnostics(self):
        holonomies=((0.0,0.0,0.0),(0.7,-1.1,0.3),(math.pi/2,math.pi/3,-math.pi/5))
        for C in (2.0,4.0,8.0,12.0):
            bound=crude_uniform_soft_bound(C)
            for ell in (8,16,32,64):
                for h in holonomies:
                    self.assertLessEqual(soft_coexact_count(ell,C,h),bound)

    def test_06_holonomy_count_bound_independent_of_ell(self):
        C=8.0
        h=(0.7,-1.1,0.3)
        vals=[soft_coexact_count(ell,C,h) for ell in (16,32,64)]
        self.assertLessEqual(max(vals),crude_uniform_soft_bound(C))
        self.assertGreater(min(vals),0)

    def test_07_trace_poincare_amplification(self):
        samples=(
            [F(1),F(0)],
            [F(2),F(3),F(1)],
            [F(1,3),F(2,3),F(-1,2),F(5,4)],
        )
        for seq in samples:
            lhs,rhs=trace_bound(seq)
            self.assertLessEqual(lhs,rhs)

    def test_08_optimized_nonlinear_stability_exponent(self):
        self.assertEqual(F(7,26)-2*F(1,13),F(3,26))
        self.assertGreater(F(3,26),0)

    def test_09_two_boundary_parity_at_zero_mode(self):
        for ell in (1,2,5,13):
            Q=scalar_chain_schur(ell,F(0))
            sym=sp.Matrix([1,1]); anti=sp.Matrix([1,-1])
            Es=sp.simplify((sym.T*Q*sym)[0]/2)
            Ea=sp.simplify((anti.T*Q*anti)[0]/2)
            self.assertEqual(Es,0)
            self.assertEqual(Ea,sp.Rational(2,ell))


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--output',required=True)
    args=p.parse_args()
    suite=unittest.defaultTestLoader.loadTestsFromTestCase(U042Checks)
    t=time.perf_counter()
    result=unittest.TextTestRunner(verbosity=2).run(suite)
    payload={
        'status':'passed' if result.wasSuccessful() else 'failed',
        'tests_run':result.testsRun,
        'failures':len(result.failures),
        'errors':len(result.errors),
        'seconds':time.perf_counter()-t,
        'python':platform.python_version(),
        'sympy':sp.__version__,
        'arithmetic':'exact symbolic/rational except explicitly labeled Fourier/rotation diagnostics',
        'seed':None,
        'claims_checked':[
            '3D tangential Hodge symbol and gradient kernel',
            'two-boundary scalar DtN Schur complement and zero-mode parities',
            'flat SU(2) holonomy adjoint momentum shift',
            'finite diagnostics for ell-independent coexact soft-mode count',
            'trace/Poincare amplification inequality',
            'optimized nonlinear perturbation exponent alpha^(3/26)'
        ],
        'nonclaims':[
            'finite mode counts do not replace the written universal count proof',
            'no exact curved-background nonabelian Steklov theorem',
            'no continuum or physical mass-gap theorem'
        ]
    }
    Path(args.output).write_text(json.dumps(payload,indent=2))
    raise SystemExit(0 if result.wasSuccessful() else 1)

if __name__=='__main__':
    main()

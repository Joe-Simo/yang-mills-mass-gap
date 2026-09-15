"""Exact finite audits for U039; no continuum Yang--Mills certificate.

Run: python checks/U039_interior_transfer_badblock_checks.py --output evidence/U039_checks.json
The binary Markov fixture audits the interior-event transfer inequality, not Wilson data.
Universal Wilson and asymptotic statements have separate written proofs.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
import json
from pathlib import Path
import platform
import time
import unittest

import sympy as sp


def counts4(n: int) -> tuple[int, int]:
    if n < 1:
        raise ValueError
    return 6*n*n*(n+1)**2, 4*n*(n+1)**3


class Checks(unittest.TestCase):
    def test_01_adaptive_parameter_identities(self) -> None:
        b,t,n = sp.symbols('b t n', positive=True)
        alpha = 16*t/b
        M = 6*n**2*(n+1)**2
        self.assertEqual(sp.simplify(32/alpha - 2*b/t), 0)
        self.assertEqual(sp.simplify(b*alpha*M/4 - 4*M*t), 0)

    def test_02_exact_haar_safety_margin(self) -> None:
        # beta>=32 and log(beta)>=3 reduce the Haar lower-bound check
        # to this exact rational margin (>1).
        margin = F(4096*32*27, 192) / F(22, 7)**3
        self.assertEqual(margin, F(790272, 1331))
        self.assertGreater(margin, 1)

    def test_03_box_ratio(self) -> None:
        for n in (2, 3, 19, 100):
            M,L = counts4(n)
            self.assertLessEqual(F(L,M), 1)
            self.assertEqual(F(L,M), F(2*(n+1),3*n))

    def test_04_balanced_large_plaquette_fraction(self) -> None:
        a = sp.symbols('a', positive=True)
        eps2 = sp.sqrt(a)
        rational_pi2_over2 = F(242,49)
        frac = rational_pi2_over2 * a/eps2
        self.assertEqual(sp.simplify(frac-rational_pi2_over2*sp.sqrt(a)),0)
        self.assertEqual(sp.simplify(eps2/12-sp.sqrt(a)/12),0)

    def test_05_union_exponent_lower_bound(self) -> None:
        # n >= 2 beta/log beta and M>=6 n^4 imply
        # -log p = 4 M log beta >= 384 beta^4/log(beta)^3.
        b,t = sp.symbols('b t', positive=True)
        nlower = 2*b/t
        lower = sp.expand(4 * 6 * nlower**4 * t)
        self.assertEqual(lower, 384*b**4/t**3)

    def test_06_binary_interior_event_transfer_fixture(self) -> None:
        # Symmetric two-state chain, event is middle state=1 in a two-step path.
        P = sp.Matrix([[F(3,4),F(1,4)],[F(1,4),F(3,4)]])
        E = sp.diag(0,1)
        R = P*E*P
        P2 = P*P
        # Conditional probabilities Pr(Y=1|X=x,Z=z).
        cond=[]
        for x in range(2):
            for z in range(2):
                cond.append(sp.cancel(P[x,1]*P[1,z]/P2[x,z]))
        p=max(cond)
        self.assertEqual(p,F(9,10))
        # In uniform stationary L2, R is symmetric; its norm is largest eigenvalue.
        eig=max(R.eigenvals().keys())
        self.assertEqual(eig,F(5,8))
        self.assertLessEqual(eig,p)

    def test_07_joint_event_tower_identity(self) -> None:
        # Exact correlated binary law from U038: verify conditioning can be iterated.
        states=[(a,b,c) for a in (0,1) for b in (0,1) for c in (0,1)]
        weights={x:F(2**(x[0]*x[1]+x[1]*x[2]), 3**sum(x)) for x in states}
        z=sum(weights.values(),F(0))
        law={x:w/z for x,w in weights.items()}
        p=F(0)
        for i in range(3):
            others=[j for j in range(3) if j!=i]
            for vals in ((0,0),(0,1),(1,0),(1,1)):
                den=sum(q for x,q in law.items() if tuple(x[j] for j in others)==vals)
                num=sum(q for x,q in law.items() if x[i] and tuple(x[j] for j in others)==vals)
                p=max(p,num/den)
        joint=sum(q for x,q in law.items() if all(x))
        self.assertLessEqual(joint,p**3)


def main() -> None:
    ap=argparse.ArgumentParser()
    ap.add_argument('--output',type=Path,required=True)
    args=ap.parse_args()
    start=time.perf_counter()
    suite=unittest.defaultTestLoader.loadTestsFromTestCase(Checks)
    result=unittest.TextTestRunner(verbosity=2).run(suite)
    payload={
        'status':'passed' if result.wasSuccessful() else 'failed',
        'tests_run':result.testsRun,
        'failures':len(result.failures),
        'errors':len(result.errors),
        'seconds':time.perf_counter()-start,
        'python':platform.python_version(),
        'sympy':sp.__version__,
        'arithmetic':'exact Fraction/SymPy decisions; no floating scientific decisions',
        'seed':None,
    }
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(payload,indent=2)+'\n')
    if not result.wasSuccessful():
        raise SystemExit(1)

if __name__=='__main__':
    main()

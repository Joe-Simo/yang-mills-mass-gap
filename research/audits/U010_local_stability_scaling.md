# U010 — gauge-quotiented local stability scaling around a block minimizer

Date: 2026-09-14.

**We have not solved the Yang–Mills problem yet.**

This unit executes U009's next step in the abelianized small-field model. It derives the spectral scaling of the quadratic Wilson Hessian after gauge directions are removed and tests whether that scaling is compatible with the U007 entropy criterion. It is an auxiliary linearized result, not a nonabelian Yang–Mills mass-gap theorem.

## 1. Quadratic form

Let A be a real lattice 1-cochain describing a small fluctuation around a boundary-compatible commuting minimizer. To quadratic order the Wilson excess has the form

    Q(A) = (beta/2) ||d A||_2^2

up to a background-dependent positive cosine factor when all background plaquette angles stay inside a fixed convexity window. Gauge variations A -> A+d phi lie in ker d and must be quotiented or gauge-fixed.

On the orthogonal complement of gradients, the relevant Hessian is d* d. With standard relative/Dirichlet-type boundary conditions on an n-cell box, its first positive eigenvalue has the same n^-2 scaling as the discrete scalar Laplacian. A separated one-dimensional mode gives the explicit lattice eigenvalue

    lambda_1(n) = 4 sin^2(pi/(2n))
                = pi^2/n^2 - pi^4/(12 n^4)+O(n^-6).

Wolfram 15.0.1 independently returned this expression and `lim n^2 lambda_1(n)=pi^2`.

The exact constant depends on the chosen cochain boundary conditions and on whether harmonic/topological modes remain. The n^-2 scaling is the point used below. Any harmonic modes must be included in the minimizer/background manifold rather than falsely assigned coercivity.

## 2. Stability inequality in the linear model

After projecting away gradients and harmonic zero modes, the discrete Poincare/Hodge estimate has the form

    ||d A||_2^2 >= c_H n^-2 ||A||_2^2,                 (H)

with c_H>0 independent of n for the specified family of boxes/boundary conditions. Therefore

    Q(A) >= (beta c_H/2) n^-2 ||A||_2^2.

This confirms the expected softening: the smallest nonzero curvature of the action landscape decays as n^-2 in lattice units.

## 3. Does n^-2 destroy the U007 action/entropy mechanism?

No, provided the bad event enforces an extensive L2 displacement from the minimizer manifold. Suppose

    ||A||_2^2 >= c_A n^4

for a four-dimensional block. Then (H) yields

    Q(A) >= (beta c_H c_A/2) n^2.                       (S)

Thus the effective collective cost grows as n^2 despite the n^-2 soft mode. In U007 notation this corresponds to sigma=2, which is more than enough to beat polynomial block-count entropy for any block scaling n(a)~a^-alpha with alpha>0.

Using lambda_1(n) above directly, a model displacement c n^4 has quadratic cost asymptotic to

    pi^2 c n^2.

Wolfram independently verified `lambda_1(n) c n^4 / n^2 -> pi^2 c`. With n(a)=a^-alpha this grows as pi^2 c a^-2alpha before the additional beta(a)~log(1/a) factor.

Therefore the **spectral softening itself is not fatal**. The crucial question becomes whether a geometrically meaningful bad event relative to the minimizer manifold really forces ||A||^2 of order n^4 after quotienting gauge and harmonic/background directions.

## 4. A weaker displacement threshold

More generally, if the event only forces

    ||A||_2^2 >= c n^gamma,

then the quadratic action cost scales as

    beta n^(gamma-2).

- gamma>2 gives a growing collective cost and passes U007's first entropy test.
- gamma=2 gives only beta times an O(1) cost, the marginal logarithmic regime analyzed in U007.
- gamma<2 is too weak for this architecture without additional structure.

So the next target is not merely a Poincare inequality; it is a **distance lemma** proving gamma>2 for the chosen bad event modulo the complete minimizer/gauge/harmonic manifold.

## 5. Nonabelian convexity restriction

For SU(2) around a background plaquette with class angle theta_p^*, the second variation of 1-cos(theta) carries a cosine-type coefficient. Uniform positive quadratic control requires the background and fluctuation to stay in a convex normal neighborhood bounded away from the point where the local Hessian changes sign/degenerates. U009 showed arbitrary boundary data can impose large background curvature, so no global uniform c_H can be inferred from the abelianized calculation.

A valid nonlinear lemma must therefore split:

1. a **good-background sector**, where all relevant background plaquettes lie in a fixed convexity window and the gauge-fixed Hessian has a controlled Hodge lower bound;
2. a **bad-background sector**, whose weight must be suppressed by a separate collective estimate.

This is a recursive-looking decomposition, but it need not be circular if the bad-background suppression is derived directly from Wilson action/entropy rather than from the desired mass gap.

## 6. Consensus status

A requested fresh Consensus literature search for lattice gauge Poincare/Hodge weak-coupling estimates could not execute because the connected Consensus account has exhausted its 30 monthly searches and reports a reset on October 1. No literature conclusion is drawn from that failure. Earlier fetched literature remains available, but this unit does not import a new external theorem.

Mathbox was explicitly requested as well. Plugin discovery returned no installable/available Mathbox plugin in this conversation, so no Mathbox verdict or ledger operation is claimed. The mathematical audit was performed directly and checked with Wolfram where applicable.

## 7. What is established

- In the abelianized gauge-fixed box model, the first positive Hessian eigenvalue scales as n^-2.
- If distance squared from the minimizer manifold is volume-order n^4, the resulting quadratic action excess is order beta n^2, which passes U007's entropy scaling test.
- Therefore the n^-2 soft mode does not by itself kill the localized weak-coupling route.
- The first unproved implication is now a nonlinear, gauge-invariant **distance-to-minimizer lemma** with exponent gamma>2, together with control of backgrounds outside the convexity window.

## 8. Next executable step

Construct a concrete relative bad event in the linearized model and prove its distance exponent. A natural candidate is a positive density of links/plaquettes whose gauge-fixed fluctuation exceeds a fixed threshold after projection onto the orthogonal complement of gradients and harmonic modes. Determine whether this forces ||A||^2 >= c n^4 or whether sparse low-frequency modes can realize the event with only n^2-scale norm. An exact counterexample would reject the event; a proof would provide the first quantitatively viable local stability ingredient for the correlated route.

# U008 — positive-density bad-block action/entropy criterion

Date: 2026-09-14.

**We have not solved the Yang–Mills problem yet.**

This unit executes U007's next deterministic/combinatorial step. It proves an action deficit and derives the entropy coefficient that a genuine interacting-measure estimate would have to overcome. It does **not** prove the needed probability bound for Wilson Yang–Mills.

## 1. Block counts

Consider an open four-dimensional hypercubic block with n elementary cells per coordinate direction. It contains exactly

    N_p(n)=6 n^4

oriented-positive elementary plaquettes internal to its cells. A convenient open-block link count is

    N_e(n)=4(n+1)n^3 = 4n^4+4n^3.

Thus N_p/N_e -> 3/2. Wolfram 15.0.1 independently returned these formulas and the ratio 3/2.

## 2. Gauge-invariant positive-density event

For SU(2), let theta_p in [0,pi] be the class angle of plaquette holonomy U_p, so (1/2)Re Tr U_p=cos theta_p. Fix epsilon in (0,pi) and rho in (0,1]. Define a block to be bad when at least rho N_p of its plaquettes satisfy

    theta_p >= epsilon.

This event is gauge invariant because the plaquette trace/class angle is conjugation invariant.

For the standard Wilson deficit relative to the identity,

    A_B(U)=sum_(p in B) [1-(1/2)Re Tr U_p]
          =sum_p [1-cos theta_p],

any bad block obeys the deterministic inequality

    A_B(U) >= rho N_p(n) [1-cos epsilon]
           = 6 rho [1-cos epsilon] n^4.                    (A)

No independence assumption is used. Gauge transformations do not change either side. For small epsilon the leading cost is

    A_B >= 3 rho epsilon^2 n^4 + O(rho epsilon^4 n^4).

This establishes the volume-scale **action deficit** anticipated in U007.

## 3. Why the deterministic cost is not yet a probability estimate

The Wilson probability of the bad event is a ratio of two high-dimensional link integrals. Inequality (A) bounds the Boltzmann weight pointwise on the bad set, but the denominator also contains an exponentially small Haar volume of a low-action neighborhood. Bounding the numerator merely by total Haar volume 1 and the denominator by a product neighborhood produces an entropy penalty proportional to N_e=O(n^4), the same scale as the action gain.

This is the correct next competition: volume action versus volume link entropy. The previous U006 polynomial block-count entropy is no longer dominant once positive-density blocks are used.

## 4. Explicit crude link-neighborhood denominator

Choose a geodesic ball C_delta around the identity in SU(2) such that every link in C_delta. If all links of the block lie in C_delta, each plaquette product lies within a class-angle bound at most 4delta by the bi-invariant triangle inequality (for 4delta<pi). Therefore

    A_B(U) <= N_p [1-cos(4delta)].

Let v(delta)=Haar(C_delta). For SU(2)~=S^3 with class-angle density (2/pi)sin^2 theta,

    v(delta)=(delta/pi)-sin(2delta)/(2pi).

Restricting the partition function denominator to this link neighborhood gives the crude lower bound

    Z_B(beta) >= v(delta)^(N_e)
                 exp[-beta_W N_p (1-cos(4delta))]

when the Wilson weight is written exp[-beta_W A_B] up to the irrelevant vacuum constant.

On the positive-density bad set, (A) gives numerator at most

    exp[-beta_W rho N_p(1-cos epsilon)]

because normalized Haar volume is at most one. Hence, provided

    rho(1-cos epsilon) > 1-cos(4delta),

the crude ratio obeys

    P(B bad)
      <= exp{-N_p beta_W [rho(1-cos epsilon)-(1-cos4delta)]
               + N_e [-log v(delta)]}.                    (P)

This inequality is valid for an isolated block with free link integration under the stated Wilson weight. It is not yet a conditional estimate uniform in arbitrary boundary links, nor a transfer-kernel estimate.

## 5. Weak-coupling consequence of the crude bound

Since beta_W(a)~K log(1/a) diverges while -log v(delta) is fixed for fixed delta, any fixed epsilon,rho for which the bracket

    q(delta)=rho(1-cos epsilon)-(1-cos4delta)

is positive eventually makes the action term dominate the O(n^4) link entropy. More explicitly, using N_p/N_e ->3/2, a sufficient large-n condition is approximately

    beta_W q(delta) > (2/3)[-log v(delta)].                (C)

For every fixed epsilon,rho>0 one can choose delta>0 sufficiently small so q(delta)>0. Then (C) holds for sufficiently weak bare coupling because beta_W->infinity.

Thus the positive-density event passes the **isolated-block volume action-versus-Haar-entropy test**. This is materially stronger than U006's one-bad-plaquette event.

There is a tradeoff: as delta->0, -log v(delta)~ -3 log delta + constant grows, so the threshold beta_W required by (C) increases. But for fixed delta it remains finite.

## 6. Boundary-condition obstruction remains

The preceding denominator neighborhood pins every internal link near identity. With arbitrary fixed boundary links, the block may have no compatible near-identity interior configuration, and the denominator lower bound can deteriorate. Gauge transformations can move some boundary disorder but cannot generally make arbitrary boundary holonomies trivial. Therefore (P) does not provide the uniform conditional bad-block probability needed for a contour expansion.

A contour/RG proof must either:

1. define blocks with collars and condition only on suitably controlled boundary data;
2. compare to a local minimizer/flat connection compatible with boundary holonomy rather than identity;
3. integrate boundary variables jointly so the denominator gain is recovered globally; or
4. prove a chessboard/reflection-positive or other collective estimate that avoids arbitrary-boundary conditional probabilities.

This boundary issue is now the first unresolved implication. It is not legitimate to call (P) a uniform polymer activity bound.

## 7. Connection to U003

Even a successful uniform probability estimate must be upgraded to the fixed-physical-time transfer quadratic form. The desired chain remains:

    collective bad-block suppression
      -> small large-field contribution to coarse loss eta_j and mixing kappa_j
      -> sum(eta_j+kappa_j^2)<infinity
      -> U003 full-space fixed-time gap transport
      -> OS limit and physical Hamiltonian gap.

Every arrow after the first remains unproved for Yang–Mills.

## 8. Next executable step

Attack the boundary obstruction in the simplest nontrivial setting. Formulate a block with a one-cell collar and compare its Wilson action to the minimum action compatible with fixed boundary links. Determine whether a positive density of interior plaquettes with theta>=epsilon forces an **excess action above the boundary-compatible minimum** of order n^4 or whether boundary/topological configurations can reduce the excess to surface order or O(1). A counterexample would invalidate this volume-cost contour definition; a proof would justify attempting a uniform conditional measure bound.

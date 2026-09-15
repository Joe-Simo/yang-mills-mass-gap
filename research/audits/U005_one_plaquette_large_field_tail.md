# U005 — exact one-plaquette SU(2) large-field tail bound

Date: 2026-09-14.

**We have not solved the Yang–Mills problem yet.**

This unit tests the first U004 localization ingredient in the simplest exactly reducible setting. It proves a one-plaquette concentration inequality only; it does not extend it to the interacting four-dimensional lattice.

## Setup

For SU(2), write a group element by class angle theta in [0,pi], so (1/2)Tr U=cos theta. Normalized Haar class measure is

    dmu(theta)=(2/pi) sin^2(theta) dtheta.

For one Wilson plaquette with weight exp(beta Tr U)=exp(2 beta cos theta), beta>0, the partition function is

    Z(beta)=int exp(2 beta cos theta) dmu(theta)
           = I_1(2 beta)/beta.

Wolfram 15.0.1 independently simplified the exact Haar integral to `Hypergeometric0F1Regularized[2,beta^2]` and verified that this equals `BesselI[1,2 beta]/beta`.

## Elementary exponential tail bound

Fix 0<epsilon<pi. On the large-field event theta>=epsilon,

    cos theta <= cos epsilon,

so its unnormalized weight is at most exp(2 beta cos epsilon).

For a lower bound on Z, restrict to 0<=theta<=epsilon/2. Since cos theta>=cos(epsilon/2),

    Z(beta) >= exp(2 beta cos(epsilon/2))
              * (2/pi) int_0^(epsilon/2) sin^2(theta) dtheta.

Define

    c(epsilon)=(2/pi)[epsilon/4 - sin(epsilon)/4]
              =(epsilon-sin epsilon)/(2 pi)>0.

Therefore the normalized one-plaquette tail satisfies

    P_beta(theta>=epsilon)
      <= c(epsilon)^(-1)
         exp[-2 beta (cos(epsilon/2)-cos epsilon)].          (T)

The exponent is strictly positive for 0<epsilon<pi. This is an exact finite-beta inequality using only monotonicity and normalized Haar measure.

A slightly different denominator window delta in (0,epsilon) gives the family

    P_beta(theta>=epsilon)
      <= h(delta)^(-1)
         exp[-2 beta(cos delta-cos epsilon)],

where h(delta)=(delta/2-sin(2delta)/4)*2/pi. Optimizing delta can improve constants but is irrelevant to the qualitative obstruction below.

## What (T) does and does not establish

The result confirms that a single SU(2) plaquette is exponentially concentrated near the identity at weak coupling. However, a four-dimensional box contains O(a^-4) plaquettes at fixed physical volume. A union bound would multiply the right side by the plaquette count. Along asymptotic freedom beta grows only logarithmically in 1/a at leading order, so whether the resulting exponent beats the entropy/volume factor depends on the precise coefficient and on the event scale epsilon(a). For fixed epsilon this simple estimate may or may not beat a^-4 depending on constants; for a shrinking localization window the exponent itself weakens.

More importantly, plaquettes are constrained and correlated, and the U003 theorem needs a **transfer-form** fine-sector and mixed estimate in the true vacuum, not merely a one-plaquette probability tail under a scalar marginal. Thus (T) is a valid local ingredient but is far from the required continuum bridge.

## Next step

Quantify the competition between weak-coupling action suppression and four-dimensional entropy along the one-loop asymptotically free trajectory. Determine whether any localization window epsilon(a)->0 can make a naive plaquette union bound summable while still being large enough to support a controlled quadratic/local expansion. If not, reject independent-plaquette/union-bound localization and require a genuinely correlated contour/polymer estimate.

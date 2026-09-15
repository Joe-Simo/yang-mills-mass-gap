# U006 — entropy versus one-plaquette localization along asymptotic freedom

Date: 2026-09-14.

**We have not solved the Yang–Mills problem yet.**

This unit tests whether the exact U005 one-plaquette tail can, by a naive union bound, control all plaquettes in a fixed physical four-volume as the lattice spacing a tends to zero.

## 1. U005 input

For a single SU(2) Wilson plaquette and any fixed 0<epsilon<pi,

    P_beta(theta>=epsilon)
      <= C(epsilon) exp[-2 beta d(epsilon)],

where

    d(epsilon)=cos(epsilon/2)-cos(epsilon)>0,
    C(epsilon)=2 pi/(epsilon-sin epsilon).

For small epsilon,

    d(epsilon)=(3/8)epsilon^2+O(epsilon^4),
    C(epsilon)=12 pi epsilon^(-3)(1+O(epsilon^2)).

## 2. Four-dimensional entropy factor

At fixed physical four-volume V, a hypercubic lattice has N_p(a)=O(V a^-4) plaquettes. A union bound therefore gives

    P(any bad plaquette)
      <= const * a^-4 * C(epsilon)
         * exp[-2 beta(a) d(epsilon)].                     (U)

This is only a formal use of the one-plaquette bound because the actual interacting lattice marginal is not the isolated one-plaquette measure. The calculation below is therefore a scaling diagnostic, not a theorem for the Wilson lattice measure.

## 3. One-loop SU(2) scaling diagnostic

For pure SU(N), the universal one-loop coefficient is

    b0 = 11 N/(48 pi^2)

in dg/dlog(mu)=-b0 g^3+... . Hence

    1/g0(a)^2 = 2 b0 log(1/a Lambda)+lower-order terms.

With the standard Wilson inverse coupling beta_W=2N/g0^2, for SU(2)

    beta_W(a) = (11/(3 pi^2)) log(1/a Lambda)+lower-order terms.

If U005's beta is the coefficient in exp(beta Tr U), then beta=beta_W/2, so

    2 beta(a) = beta_W(a)
              = K log(1/a Lambda)+o(log(1/a)),
    K=11/(3 pi^2) approximately 0.3715.

For fixed epsilon, the exponential part of (U) behaves like

    a^(K d(epsilon)+o(1)).

But d(epsilon)<=2 for all epsilon, so

    K d(epsilon) <= 22/(3 pi^2) approximately 0.743 < 4.

Therefore even the **best possible fixed-angle exponent available from this elementary U005 denominator bound cannot beat the a^-4 plaquette count**. The prefactor C(epsilon) only worsens the estimate.

This proves a no-go statement for this particular union-bound architecture under the stated one-loop normalization: U005's elementary isolated-plaquette tail, inserted independently at every plaquette, is too weak by its exponent to give a vanishing all-plaquette bad-event probability in a fixed four-volume.

## 4. Shrinking windows are worse

If epsilon(a)->0, then d(epsilon)~3 epsilon^2/8 and C(epsilon)~12 pi epsilon^-3. The action exponent in (U) becomes

    K d(epsilon(a)) log(1/a)
      ~ (3K/8) epsilon(a)^2 log(1/a).

Because epsilon(a)^2->0, its coefficient of log(1/a) tends to zero, while the entropy term contributes 4 log(1/a) and the Haar prefactor contributes 3 log(1/epsilon). Thus no shrinking localization window can rescue this naive union bound.

This conclusion is about the U005 inequality plus a plaquette union bound. It does not prove that weak-coupling fields fail to localize. Correlations, gauge constraints, collective action costs, contour geometry and improved large-deviation estimates can change the entropy balance dramatically.

## 5. Consequence for the research route

The U004/U005 program has now falsified the cheapest localization bridge. A proof must exploit correlated structure rather than control every plaquette independently. Candidate mechanisms include a gauge-invariant contour/polymer decomposition of large-field defects, a multiscale small-field/large-field partition with collective action cost, or a rigorous RG estimate whose bad blocks pay an action proportional to their boundary/volume while their combinatorial entropy is controlled.

Any such mechanism must still be noncircular: its suppression estimate cannot assume the desired mass gap or uniform clustering, and it must preserve reflection positivity/OS reconstruction sufficiently to feed the U003 fixed-physical-time gap theorem.

## 6. Next executable obligation

Formulate a bad-block event at scale ell(a) rather than a bad-plaquette event, and derive the required entropy-versus-action inequality symbolically. Determine the minimum collective action cost per bad block needed to overcome the number of blocks in fixed physical volume. This will specify the exact large-deviation estimate a correlated contour/RG method would have to prove before any further construction is attempted.

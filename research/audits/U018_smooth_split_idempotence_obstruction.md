# U018 — smooth split: idempotence obstruction to a two-sector U003 decomposition

Date: 2026-09-14.

**We have not solved the Yang–Mills problem yet.**

This bounded attempt executes U017's cheapest falsification test before a full IMS estimate. It finds a structural obstruction: a smooth low-pass operator P=f(L) with a transition of O(1) amplitude cannot be treated as an approximate orthogonal projector with small operator-norm idempotence defect. For the explicit U017 tanh window, ||P^2-P|| is asymptotically at least 1/4 whenever the lattice spectrum samples the transition. Thus the proposed two-sector bound with a small term ||P^2-P|| cannot close. The smooth-window route survives only if the transition band is promoted to an explicit third/overlap sector or if the decomposition is formulated as a partition of unity rather than approximate projections.

## 1. Exact scalar defect

U017 uses

    f_c(lambda)=1/2[1-tanh((lambda-lambda_c)/(gamma lambda_c))].

Pointwise,

    f_c(1-f_c)
      = 1/4 sech^2((lambda-lambda_c)/(gamma lambda_c)).

Wolfram 15.0.1 independently simplified this identity and returned value 1/4 at lambda=lambda_c.

For the self-adjoint operator P=f_c(L), functional calculus gives

    P-P^2 = [f_c(1-f_c)](L) >= 0,

and

    ||P-P^2|| = max_(lambda in spec L) f_c(lambda)[1-f_c(lambda)].

If the spectrum contains a mode at lambda_c, the norm is exactly 1/4. If it contains a mode within o(lambda_c) of lambda_c, the norm tends to 1/4 for fixed gamma.

## 2. The four-dimensional box does sample the transition

For the U013/U017 box, lambda_c=n^-q with q<1. Low eigenvalues correspond to momentum radius

    k_c ~ n^(1-q/2).

Changing one momentum coordinate by one changes lambda by order

    delta lambda_mode ~ k_c/n^2
                      ~ n^(-1-q/2).

The smooth transition width is O(lambda_c)=n^-q. Their ratio is

    delta lambda_mode/lambda_c
      ~ n^(-1+q/2) -> 0

for q<2. Therefore many eigenvalues lie inside the transition, and in particular the distance of some spectral values from the transition center is negligible compared with its width (up to the standard lattice-point radial discretization). Hence

    ||P-P^2|| -> 1/4

along the scaling sequence in the scalar model, modulo an inessential shift of the chosen center to a nearby eigenvalue if exact centering is desired.

This is not a numerical accident. Any continuous spectral cutoff taking values from near 1 to near 0 must pass through 1/2; if the spectrum densely samples that transition, its operator-norm idempotence defect cannot be small.

## 3. Consequence for U017's proposed estimate

U017 proposed targeting

    kappa^2 <= C R/n + C||P^2-P|| + C err^2.

The middle term is O(1), not summable. Therefore **that particular two-sector estimate cannot establish U003 mixing summability** for a smooth transition.

This does not show the physical coarse/fine coupling is O(1). It shows that measuring smoothness error by global operator-norm idempotence is the wrong architecture: transition modes are deliberately neither coarse nor fine and cannot be hidden as a small approximation defect.

## 4. Corrected architecture: three sectors

Promote the transition band to an explicit overlap sector. Choose bounded spectral functions c(lambda), t(lambda), f(lambda) satisfying a quadratic partition of unity

    c(lambda)^2+t(lambda)^2+f(lambda)^2=1,

with:

- c supported on low/coarse energies;
- f supported on high/fine energies;
- t supported only in the transition band.

Then no small idempotence assumption is needed. The transition sector dimension is already controlled by U015/U017:

    N_transition = Theta(n^(4-2q))

for balanced width, and at q=1/2 it is boundary-order Theta(n^3).

A polynomial approximation can make c,t,f finite range up to polynomially small error. The U003 framework would need to be generalized from a 2x2 coarse/fine block to a 3x3 block, or the transition sector can be merged into the coarse sector. Merging it into coarse preserves the U013 count exponent because coarse and transition have the same order in the balanced case.

The simplest correction is therefore:

    enlarged coarse = low + transition,
    fine = high,

with a smooth separator chosen so that the fine operator is finite-range/local but no claim that the enlarged-coarse map is an approximate projection in operator norm.

## 5. New bottleneck

Once transition modes are explicitly coarse, the dangerous cross term is spatial localization of the **fine** high-pass functional calculus and interactions/background variation, not spectral idempotence. The collar fraction R/n remains available geometrically, but a relative form estimate still cannot follow from counting alone.

The next adversarial state should be a low-energy/coarse state whose mass is concentrated in the R-collar. For the pure scalar Laplacian, uncertainty/Poincare considerations constrain how strongly a mode with lambda<=lambda_c can concentrate in a collar of width R << lambda_c^-1/2. At q=1/2,

    coarse wavelength scale ~ lambda_c^-1/2 = n^(1/4),
    R ~ n^(1/4) log n.

Notably R is actually larger than the coarse wavelength by a logarithm. Thus a collar of width R can accommodate low modes; naive uncertainty may not yield an extra small factor. This is a warning that the desired kappa^2~R/n estimate must exploit normalization across the full four-dimensional block or a more careful IMS partition, not merely wavelength exclusion.

## 6. Outcome classification

Outcome: **refuted for the proposed approximate-idempotence two-sector architecture**.

Proved in the scalar model:

    f(1-f)=1/4 sech^2(...),
    sup transition defect=1/4,

and the lattice transition is densely sampled relative to its width for q<1.

Therefore ||P-P^2|| is not a small RG error.

Surviving route: explicit transition sector / partition-of-unity decomposition, with the transition merged into coarse if desired.

Not proved: any U003 relative mixing estimate, nonlinear gauge-covariant split, reflection positivity, OS construction, or mass gap.

## 7. Next bounded attempt

Generalize U003's abstract gap certificate to an **enlarged coarse sector** that contains the full smooth transition band, so no idempotence defect enters. Then derive the exact Schur-complement condition needed between enlarged coarse and fine sectors. This is purely operator-theoretic and can be settled before returning to Yang–Mills localization. If the required relative mixing coefficient still demands a power of R/n, attack that estimate with an IMS partition; if the generalized certificate tolerates an O(1) transition coupling inside the coarse sector, the spectral-smoothing route remains viable.
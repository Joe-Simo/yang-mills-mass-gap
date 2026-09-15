# U015 — smooth spectral window: simultaneous locality and transition-count scaling

Date: 2026-09-14.

**We have not solved the Yang–Mills problem yet.**

This bounded attempt follows U014 by replacing the sharp low-mode projector with a smooth spectral transition. It derives a nonempty exponent region in which a polynomial functional calculus can be sub-block local and the transition sector remains no larger than the coarse sector. The polynomial degree estimate is presently a scaling argument, not yet a fully sourced approximation theorem with constants; accordingly the result is classified as conditional at that step.

## 1. Spectral scales

Use the four-dimensional scalar box model from U013. Let

    lambda_c = n^(-q),      1/2 <= q < 1,

and let the smooth transition width be

    Delta lambda = n^(-s).

The low momentum radius satisfies

    k_c ~ n sqrt(lambda_c) = n^(1-q/2).

Because lambda~|k|^2/n^2 near the spectral bottom,

    d lambda/dk ~ k_c/n^2 ~ n^(-1-q/2).

Therefore a spectral transition width Delta lambda corresponds to momentum-shell thickness

    Delta k ~ n^(1+q/2-s).

The number of four-dimensional modes in that shell is surface area k_c^3 times Delta k, hence

    N_transition ~ n^(4-q-s).                            (T)

Wolfram 15.0.1 independently simplified this exponent to 4-q-s.

For comparison, U013's total coarse count is

    N_coarse = Theta(n^(4-2q)).

Thus the transition sector is no larger in exponent than the coarse sector exactly when

    s >= q.                                               (C)

For q>=1/2 this also makes N_transition at most boundary-order n^3.

## 2. Polynomial locality scaling

A bounded smooth cutoff f(lambda) changing over width Delta lambda can be approximated by a polynomial after mapping the fixed Laplacian spectrum to a compact interval. Near a transition separated from the endpoint by lambda_c, the relevant spectral resolution of a degree-R polynomial is expected on the scale R^-2 near the endpoint (Chebyshev angular variable), rather than R^-1 in lambda. This suggests

    R ~ Delta lambda^(-1/2) log(1/err)
      ~ n^(s/2) log n                                    (P)

for polynomial error n^-p.

Because a degree-R polynomial in a nearest-neighbor Laplacian has graph range R, sub-block locality R=o(n) requires

    s < 2.                                                (L)

Combining (C) and (L) gives the nonempty window

    1/2 <= q < 1,
    q <= s < 2.                                           (W)

Wolfram independently solved these exponent inequalities and returned exactly this region.

**Important evidence qualification:** formula (P) is not yet promoted to a proved approximation theorem in this project. The exact degree dependence for a chosen smooth cutoff, including constants and dependence on derivatives/analyticity, must be established or sourced. The exponent region (W) is therefore conditional on (P).

## 3. Particularly balanced choice

Taking s=q makes the transition width comparable to the cutoff itself:

    Delta lambda ~ lambda_c.

Then

    N_transition ~ n^(4-2q),
    R ~ n^(q/2) log n.

At q=1/2:

    N_coarse ~ N_transition ~ n^3,
    R ~ n^(1/4) log n.

This is substantially more local than U013's inverse approximation range n^(1/2)log n because approximating a bounded smooth cutoff is easier than approximating 1/lambda. Near q=1, counts approach n^2 while the proposed range approaches n^(1/2)log n.

## 4. Why smoothing addresses U014

U014's leakage arose from the discontinuous sharp spectral symbol, whose Fourier kernel has an algebraic Dirichlet tail. A polynomial f_R(L) is strictly finite range R. Therefore for two regions separated by more than R its kernel is exactly zero, and block-boundary leakage is confined to an R-cell collar.

For an n^4 block, such a collar contains O(R n^3) sites. Its volume fraction is

    O(R/n) ~ n^(s/2-1) log n,

which tends to zero whenever s<2. This is the same locality condition (L).

This gives a concrete geometric small parameter absent from the sharp projector:

    delta_boundary ~ R/n.

Whether U003's **relative quadratic-form** mixing coefficient kappa inherits sqrt(delta_boundary), delta_boundary, or no such gain depends on normalization/coercivity and remains unproved.

## 5. Candidate U003 summability

Suppose, as a target lemma, that

    kappa^2 <= C R/n + C err^2.

Then with n_j growing geometrically along RG steps and s<2,

    R/n ~ n^(s/2-1) log n

is geometrically summable, and err=n^-p can also be made summable. Under that specific relative estimate, U003's sum kappa_j^2<infinity would close at the scalar-linearized level.

But this inequality is precisely the next load-bearing statement. Counting collar volume does not prove it: low-energy states may concentrate near the collar, and the relevant transfer deficit weights modes by energy. A relative trace/IMS-type localization estimate is required.

## 6. Outcome classification

Outcome: **conditional scaling window established**.

Proved from lattice dispersion/counting:

    N_transition exponent = 4-q-s,
    N_transition <= N_coarse when s>=q,
    collar fraction = O(R/n) once a degree-R polynomial is chosen.

Conditional input requiring proof/source verification:

    degree R=O(n^(s/2) log n) for polynomially accurate approximation of the selected smooth spectral cutoff.

Not established:

- U003 relative mixing estimate;
- nonlinear gauge-covariant cutoff;
- background-uniform functional calculus;
- reflection positivity;
- continuum OS construction or mass gap.

## 7. Next bounded attempt

Remove the conditional approximation step. Choose an explicit cutoff, preferably one expressible through Chebyshev polynomials or an analytic sigmoid on the rescaled spectral variable, and prove a uniform degree/error bound on the lattice spectral interval. If the true required degree scales as Delta lambda^-1 rather than Delta lambda^-1/2, the allowed locality window changes to s<1 and conflicts with s>=q only mildly (still leaving q<=s<1 for q<1); if worse, the route may close. This approximation theorem is the cheapest decisive check before attempting the harder IMS/relative-mixing lemma.
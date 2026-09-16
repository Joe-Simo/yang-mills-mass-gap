# U045 — determinant locality: rank reduction alone does not close the weak-coupling scaling

Date: 2026-09-16. Base: U044 status head.

**We have not solved the Yang–Mills problem yet.**

Evidence: self-reviewed finite-regulator scaling/linear-algebra obstruction following U044. No determinant-locality theorem, nonlinear integration theorem, continuum construction, or physical mass-gap theorem.

## 1. Target

U044 proved quadratic boundary-fixed Schur stability but left the Gaussian determinant and nonlinear Wilson remainder uncontrolled. The first proposed repair was to use locality so that only boundary-sensitive degrees of freedom contribute to the boundary-dependent determinant.

This unit tests whether a mere reduction from bulk rank O(ell^4) to boundary rank O(ell^3) would be enough on the optimized U041 scales.

## 2. Naive determinant estimate

For the high block Dbar and perturbation E_D, U044 has

    ||Dbar^(-1/2) E_D Dbar^(-1/2)|| = O(delta ell^2).

Calling this dimensionless perturbation F, the elementary finite-dimensional bound

    |log det(I+F)| <= rank(F) * O(||F||)

holds when ||F|| is bounded away from 1.

The full high block has rank O(ell^4), giving the already-recorded loss

    O(delta ell^6).

On

    delta = O(alpha^(7/26)),
    ell   = O(alpha^(-1/13)),

this scales as

    alpha^(7/26-12/26)=alpha^(-5/26),

which diverges rather than vanishes.

## 3. Surface-rank reduction is still insufficient

Suppose locality were used only to prove that the boundary-dependent determinant perturbation had effective rank O(ell^3), the natural one-cell collar size. The same trace-norm argument would then give

    O(ell^3 * delta ell^2)=O(delta ell^5).

On the optimized scale,

    delta ell^5 = O(alpha^(7/26-10/26))
                = O(alpha^(-3/26)),

again divergent.

Therefore **surface rank alone cannot close U044's determinant problem**. Any successful locality theorem must gain additional decay in propagation from the boundary into the high interior, exploit cancellations/normalization of local determinant densities, or reorganize the determinant as a convergent local/connected expansion whose boundary-dependent coefficients carry more powers than the worst-case inverse-gap norm.

Wolfram 15.0.1 independently returned the exponents -5/26 and -3/26 for the bulk-rank and surface-rank estimates.

## 4. Why this is a useful obstruction

U044's Schur bound uses the worst global high-mode resolvent norm O(ell^2). That norm is attained by the lowest retained high modes, but most high modes are substantially stiffer. Multiplying the worst inverse gap by every boundary degree of freedom discards spectral information.

Thus the next determinant estimate should be spectral rather than rank-only. In the flat periodic slab the high modes are explicitly labeled by tangential momentum and normal mode number, with eigenvalues of the form

    lambda(n) + 4 sin^2(pi k/(2 ell)).

A determinant variation localized near the boundary should therefore be estimated by sums of Green-function diagonal/off-diagonal terms, not by rank times the smallest eigenvalue inverse.

The candidate object is the boundary-layer trace

    Tr[ chi_boundary Dbar^(-1) chi_boundary ],

and, for higher determinant terms,

    Tr[(Dbar^(-1/2) E Dbar^(-1/2))^m]

with E localized to the collar. The decisive question is the exact ell-scaling of these traces after the bounded soft package is removed.

## 5. Next bounded attempt

Compute the flat four-dimensional slab boundary Green trace mode-by-mode after the U044 soft removal. Determine whether

    Tr[chi_boundary Dbar^(-1) chi_boundary]

scales as O(ell^3), O(ell^3 log ell), O(ell^4), or worse, and then combine that result with the actual local coefficient size O(delta), rather than O(delta ell^2). If the first determinant variation is O(delta ell^3 log ell) or smaller, its optimized exponent is still not automatically favorable and the relevant quantity must be normalized per coarse boundary cell or shown to cancel between boundary data. If a difference of two boundary conditions gains additional inverse-distance decay, quantify that directly.

Outcome classification: **surface-rank-only repair refuted; spectral/local Green-function estimate required.**

Not proved: boundary-dependent determinant smallness, nonlinear Wilson integration, transfer-gap recursion, continuum Yang–Mills, or mass gap.
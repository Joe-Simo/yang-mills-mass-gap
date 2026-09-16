# U046 — flat boundary Green trace is surface order and restores a positive scaling exponent

Date: 2026-09-16. Depends on U044-U045.

**We have not solved the Yang–Mills problem yet.**

Evidence: self-reviewed flat-model spectral estimate/scaling lemma. This is not yet a nonlinear determinant theorem.

## 1. Target

U045 showed that replacing bulk rank O(ell^4) by surface rank O(ell^3) is still useless if every boundary mode is charged the worst inverse gap O(ell^2). The correct first determinant variation is instead a local Green trace, which weights every mode by its actual eigenvalue.

## 2. Flat four-dimensional scaling

After Fourier transform in the three tangential directions, a boundary-local Green kernel for a massless four-dimensional Laplace/Maxwell high sector has the same infrared power counting as

    integral d^3 q / |q|.

The three-dimensional measure contributes q^2 dq, hence near q=0

    integral_(1/ell)^1 q^2 dq / q
      = 1/2 - 1/(2 ell^2),

which is uniformly finite. Wolfram 15.0.1 independently returned this exact integral and its limit 1/2.

Therefore the boundary Green diagonal has no infrared ell^2 amplification after the bounded U044 soft package is separated. Summing over O(ell^3) boundary sites gives the natural first-order trace scaling

    Tr[chi_boundary Dbar^(-1) chi_boundary] = O(ell^3),       (G)

up to fixed color/polarization/collar constants in the flat periodic slab.

This is the spectral improvement U045 required: O(ell^3), not O(ell^5).

## 3. Optimized phase-cell exponent

If a boundary-local Hessian perturbation has coefficient size O(delta), its first log-determinant variation is therefore expected/bounded at the flat quadratic level by

    O(delta ell^3).

Using U041's optimized scales

    delta=O(alpha^(7/26)),
    ell=O(alpha^(-1/13)),

we obtain

    delta ell^3 = O(alpha^(7/26-6/26))
                = O(alpha^(1/26)) -> 0.                      (S)

This is the first favorable determinant scaling found after U044.

## 4. Scope and missing rigor

Equation (G) is a flat spectral/Green estimate, not yet the full Yang-Mills determinant statement. To turn it into a theorem for the curved high block one must establish:

1. the collar-supported boundary dependence of the Hessian/determinant after normalization;
2. a uniform local Green bound for the curved high block, not just its global inverse norm;
3. trace-ideal control of higher terms in log det(I+F), not merely the first variation;
4. treatment of cubic and higher Wilson action terms under the same local covariance bounds.

The important point is that there is no longer a scaling contradiction at first determinant order: locality plus the actual spectral density produces the positive exponent 1/26.

## 5. Next bounded attempt

Prove the finite-lattice version of (G) exactly for the flat periodic slab using the explicit tangential Fourier and normal Dirichlet spectra from U042-U044. Bound the discrete sum uniformly in ell after removing the fixed soft package. Then test whether a resolvent identity transports that local Green bound to curved regular backgrounds with relative error O(delta ell^2)=o(1). If so, expand the normalized log determinant by trace ideals and identify the first higher-order summability threshold.

Outcome classification: **favorable flat first-order determinant scaling established; curved/all-orders determinant control remains unproved.**
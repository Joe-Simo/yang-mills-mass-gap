# Yang–Mills Existence and Mass Gap Research

Private working repository. **No complete verified solution.**

The target is the full Jaffe–Witten/Clay assertion: a nontrivial four-dimensional quantum Yang–Mills theory for every compact simple gauge group in scope, with the required axioms, Yang–Mills identification, continuum/infinite-volume setting, and strictly positive finite physical mass gap.

## Latest checkpoint — U044, 2026-09-16

Read `research/audits/U044_boundary_fixed_schur_stability.md`.

On U042's periodic SU(2) phase-cell slab, the boundary-fixed interior gauge problem now has an explicit perturbative solution at quadratic order. Gauge parameters vanish on both boundary faces, their flat Dirichlet gauge map has singular gap at least `2/ell`, and the flat Coulomb slice remains transverse to curved interior gauge orbits whenever `delta ell` is small. Boundary links and representation channels are not changed or projected away.

After exact Fourier/Hodge separation, the only interior physical modes that can fall below `c/ell^2` are one longitudinal-normal `k=0` mode for each tangential covariant momentum with `lambda<=Lambda_*/ell^2`. U042's shifted-momentum counting makes this a bounded-dimensional package, uniformly in cell size and flat commuting holonomy. Removing that package leaves a high interior Hessian block `Dbar>=c_*/ell^2`.

For a curved background within link distance `delta` of the flat reference, locality gives `||H_U-Hbar||<=K_H delta`. A scaled-resolvent Schur argument then yields an absolute retained-form error `||S_U-Sbar||=O(delta ell^2)`. On every flat coexact boundary mode with Steklov stiffness at least `C/ell`, the relative error is `O(delta ell^3)`. U041's optimized scales give `delta ell^2=O(alpha^(3/26))` and `delta ell^3=O(alpha^(1/26))`, both tending to zero.

Ten new focused checks and all nine U043 checks passed. The exact longitudinal-normal spectrum was audited against a shifted path-Neumann operator, and a clean Wolfram rerun corroborated the characteristic-polynomial, resolvent and exponent identities. The result is self-reviewed quadratic finite-regulator mathematics, not formal/expert verification or a novelty claim.

Next target: control the **boundary-dependent high-mode determinant and nonlinear Wilson remainder** without paying the full `O(ell^4)` high-mode rank. The naive determinant bound costs `O(delta ell^6)` and is not small on the optimized scale. No centered physical-transfer recursion, continuum construction, or Yang-Mills mass bound is established.

## Earlier checkpoint — U043, 2026-09-16

Read `research/audits/U043_curved_horizontal_coercivity.md`.

For every sufficiently small U041-regular SU(2) open phase cell, a fluctuation orthogonal to the actual gauge orbit has flat-gradient leakage at most `4 delta/sigma_ell`, where `sigma_ell=2 sin(pi/[2(ell+1)])`. The exact flat transverse curl gap is `mu_ell=8 sin^2(pi/[2(ell+1)])`. Locality and smoothness give a cell-size-independent Wilson-Hessian error `O(delta)||b||^2`.

On U041's optimized scales, `delta ell=O(alpha^(5/26))` and `delta ell^2=O(alpha^(3/26))`. Hence for sufficiently small `alpha` the curved magnetic Hessian on the actual gauge-horizontal tangent space obeys `Hess_U S[b,b] >= 4/(ell+1)^2 ||b||^2`, and every partial boundary trace satisfies `||Tr b||^2 <= (ell+1)^2 Hess_U S[b,b]/4`.

This closes the curved bulk horizontal trace/coercivity estimate anticipated in U042 without constructing a nonlinear Coulomb gauge or projecting a phase cell to a singlet. Boundary gauge representation data remain explicit.

The first unresolved implication is boundary-fixed: minimizing with fixed tangential boundary data uses gauge transformations that are identity on boundary vertices. A boundary-fixed gauge-equivariant slice must be compared with the flat Steklov coordinates before one can claim nonlinear high-boundary-mode integration or a Schur-complement estimate.

Nine focused U043 checks and all nine U042 checks passed. Results are self-reviewed, not formal/expert verification or a novelty claim.

Next target: construct the boundary-fixed curved gauge slice and compare its minimized boundary quadratic form with the flat U042 Steklov form while retaining boundary representation data. No continuum construction or physical Yang-Mills mass bound is established.

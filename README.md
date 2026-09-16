# Yang–Mills Existence and Mass Gap Research

Private working repository. **No complete verified solution.**

The target is the full Jaffe–Witten/Clay assertion: a nontrivial four-dimensional quantum Yang–Mills theory for every compact simple gauge group in scope, with the required axioms, Yang–Mills identification, continuum/infinite-volume setting, and strictly positive finite physical mass gap.

## Latest checkpoint — U043, 2026-09-16

Read `research/audits/U043_curved_horizontal_coercivity.md`.

For every sufficiently small U041-regular SU(2) open phase cell, a fluctuation orthogonal to the **actual** gauge orbit has flat-gradient leakage at most `4 delta/sigma_ell`, where `sigma_ell=2 sin(pi/[2(ell+1)])`. The exact flat transverse curl gap is `mu_ell=8 sin^2(pi/[2(ell+1)])`. Locality and smoothness give a cell-size-independent Wilson-Hessian error `O(delta)||b||^2`.

On U041's optimized scales, `delta ell=O(alpha^(5/26))` and `delta ell^2=O(alpha^(3/26))`. Hence for sufficiently small `alpha` the curved magnetic Hessian on the actual gauge-horizontal tangent space obeys

`Hess_U S[b,b] >= 4/(ell+1)^2 ||b||^2`,

and every partial boundary trace satisfies

`||Tr b||^2 <= (ell+1)^2 Hess_U S[b,b]/4`.

This closes the **curved bulk horizontal trace/coercivity** estimate anticipated in U042 without constructing a nonlinear Coulomb gauge or projecting a phase cell to a singlet. Boundary gauge representation data remain explicit.

The first unresolved implication is now boundary-fixed: minimizing with fixed tangential boundary data uses gauge transformations that are identity on boundary vertices. A boundary-fixed gauge-equivariant slice must be compared with the flat Steklov coordinates before one can claim nonlinear high-boundary-mode integration or a Schur-complement estimate.

Nine focused U043 checks and all nine U042 checks passed. The initial U043 low-mode diagnostic used cutoff `C=4`, below the asymptotic first transverse threshold `sqrt(2) pi`; that diagnostic was corrected to `C=6,8,12` without changing the theorem. Wolfram corroborated the gap formulas and exponents. Results are self-reviewed, not formal/expert verification or a novelty claim.

Next target: construct the **boundary-fixed curved gauge slice**, prove that its minimized boundary quadratic form differs from the flat U042 Steklov form by `O(delta ell^2)` relatively on the stiff sector (or `o(1/ell)` absolutely), and retain the exact boundary gauge representation data plus bounded coexact/cycle soft sector. No continuum construction or physical Yang–Mills mass bound is established.

## Preserved nearest dependencies

- U042: `research/audits/U042_gauge_covariant_steklov_split.md` — exact flat-holonomy SU(2) Hodge/Steklov split; surface-sized boundary gauge kernel; bounded coexact soft sector after gauge-gradient separation.
- U041: `research/audits/U041_boundary_steklov_soft_modes.md` — optimized phase-cell scaling `ell=alpha^(-1/13)`, `eps=alpha^(8/13)` and the boundary-soft-mode obstruction.
- U040: `research/audits/U040_mesoscopic_axial_gauge_coercivity.md` — deterministic regular-core/skeleton decomposition and local nonlinear small-field control.
- U039: `research/audits/U039_interior_defect_transfer_suppression.md` — dense-defect probability converted to an operator-norm-small interior transfer remainder.
- U038: `research/audits/U038_boundary_surface_correction_and_defect_tail.md` — corrected arbitrary-boundary defect estimate and historical U008/U009 correction.
- U029–U037, U026–U028 and U003 remain preserved as restricted earlier results and obstructions; none is a joint-limit Yang–Mills construction.

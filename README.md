# Yang–Mills Existence and Mass Gap Research

Private working repository. **No complete verified solution.**

The target is the full Jaffe–Witten/Clay assertion: a nontrivial four-dimensional quantum Yang–Mills theory for every compact simple gauge group in scope, with the required axioms, Yang–Mills identification, continuum/infinite-volume setting, and strictly positive finite physical mass gap.

## Latest checkpoint — U046, 2026-09-16

Read `research/audits/U045_determinant_locality_obstruction.md` and `research/audits/U046_boundary_green_trace_scaling.md`.

U045 shows that a rank-only determinant repair fails even if locality reduces the relevant rank from bulk `O(ell^4)` to surface `O(ell^3)`: charging every boundary variable the worst inverse high-mode gap still costs `O(delta ell^5)=O(alpha^(-3/26))`. A successful determinant theorem must use the actual high-mode spectral density/Green kernel, not rank times the smallest eigenvalue.

U046 then identifies favorable first-order spectral power counting. For the flat four-dimensional slab, the boundary-local Green diagonal has infrared behavior `integral d^3q/|q|`, which is finite at zero momentum after the bounded U044 soft package is separated. Thus the natural boundary Green trace is surface order `O(ell^3)`, and a local Hessian perturbation of coefficient size `O(delta)` has first determinant variation `O(delta ell^3)=O(alpha^(1/26))->0` on the optimized U041 scale.

This removes the first-order scaling contradiction but is not yet a determinant theorem. The next target is an exact finite-lattice discrete Green-trace bound, transport to curved regular backgrounds by a local resolvent estimate, and trace-ideal control of higher log-determinant terms together with nonlinear Wilson remainders.

No centered physical-transfer recursion, continuum construction, or Yang–Mills mass bound is established.

## Preserved nearest dependencies

- U044: boundary-fixed quadratic Schur stability; bounded interior soft package; stiff boundary relative error `O(alpha^(1/26))`.
- U043: curved horizontal coercivity and `O(ell^2)` trace estimate.
- U042: flat-holonomy gauge-covariant Hodge/Steklov split and bounded coexact soft sector after gauge separation.
- U041: optimized phase-cell scaling `ell=alpha^(-1/13)`, `eps=alpha^(8/13)`.
- U040-U038: regular-core decomposition and dense-defect suppression.
- Earlier U003-U037 results and obstructions remain preserved; none is a joint-limit Yang–Mills construction.

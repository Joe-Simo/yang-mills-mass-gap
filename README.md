# Yang–Mills Existence and Mass Gap Research

Private working repository. **No complete verified solution.**

The target is the full Jaffe–Witten/Clay assertion: a nontrivial four-dimensional quantum Yang–Mills theory for every compact simple gauge group in scope, with the required axioms, Yang–Mills identification, continuum/infinite-volume setting, and strictly positive finite physical mass gap.

## Latest checkpoint — U042, 2026-09-16

Read `research/audits/U042_gauge_covariant_steklov_split.md`.

On the periodic phase-cell slab, the linearized SU(2) Wilson Hessian around an arbitrary flat commuting holonomy now has an exact gauge-covariant Hodge/Steklov decomposition. Before gauge separation its boundary Steklov form has a surface-sized exact zero kernel: at the identity background the kernel dimension is `6 ell^3+3`. Thus U041's bounded-soft-mode picture is false on the unreduced boundary connection space; boundary gauge representation data must be retained rather than projected away.

After separating exact boundary gauge gradients, each adjoint Fourier/color mode has two coexact polarizations with the exact two-face stiffnesses `q_-(lambda)=lambda/2+sinh(gamma)tanh(ell gamma/2)` and `q_+(lambda)=lambda/2+sinh(gamma)coth(ell gamma/2)`, where `cosh(gamma)=1+lambda/2` and the flat holonomy shifts the adjoint momenta. For every fixed `C`, the real coexact/harmonic sector with stiffness at most `C/ell` has dimension bounded independently of both `ell` and the flat holonomy. Global cycle modes remain explicit.

The nonlinear scaling is favorable but not closed: in a fixed logarithmic chart the Wilson Hessian differs from the flat Hessian by an absolute `O(delta)||a||_2^2` term, while the natural slab trace/Poincare amplification is `O(ell^2)`. U041's optimized regular-core scales give `delta ell^2=O(alpha^(3/26))->0`. The missing theorem is the curved-core gauge-equivariant trace/coercivity estimate that carries every boundary representation and permits this perturbation argument in the centered physical transfer.

Nine new focused checks and all nine U041 checks passed. A recorded checker repair replaced one missing-numpy diagnostic implementation without changing any formula or test population; a clean Wolfram rerun corroborated the Hodge, parity, zero-mode and exponent identities. Results are self-reviewed, not formal/expert verification or a novelty claim.

Next target: prove the curved regular-core boundary trace/Poincare estimate on the complement of the bounded flat Steklov-soft sector, then combine it with the `O(alpha^(3/26))` nonlinear perturbation while retaining boundary gauge representation data. No continuum construction or physical Yang-Mills mass bound is established.

## Earlier checkpoint — U041, 2026-09-16

Read `research/audits/U041_boundary_steklov_soft_modes.md`.

U040's two-scale exponents are now optimized within that proof template: `ell=ceil(alpha^(-1/13))`, `eps=alpha^(8/13)`. Separator density, bad-core density, and nonlinear curl error all become `O(alpha^(1/13))`; no stronger common power is possible within the same three-constraint balance.

Unrestricted integration of one cell interior produces a gauge-invariant boundary effective action whose dependence is confined to a one-cell collar: with `B_ell=48ell^3-72ell^2+72ell-24`, its oscillation is at most `2 beta B_ell`. This is surface order and independent of exterior volume, but it is not small at weak coupling and does not automatically survive a hard regular-core truncation.

A continuous-SU(2) commuting family inside the regular small-field regime has classical boundary stiffness at most `3/(2ell+1)`. Thus a uniform positive boundary coercivity constant is impossible even after U040 localization. The correct linear companion is a Steklov/Dirichlet-to-Neumann operator. On a periodic slab, `q_ell(lambda)=lambda/2+sinh(gamma)coth(ell gamma)`, `cosh(gamma)=1+lambda/2`; `q<=C/ell` forces tangential momentum `O(1/ell)`, so only a bounded number of scalar Fourier modes per cell are that soft.

Nine new focused checks and all nine U040 checks passed. Wolfram independently corroborated the optimized exponents, collar count, soft quotient and exact slab identity. Results are self-reviewed, not formal/expert verification or a novelty claim.

Next target: construct the analogous **gauge-covariant nonabelian Steklov/Hodge split** on each regular core, retain the bounded soft boundary/cycle sector, and integrate the high boundary modes in the centered physical transfer form. No continuum construction or physical Yang–Mills mass bound is established.

## Earlier checkpoint — U040, 2026-09-16

Read `research/audits/U040_mesoscopic_axial_gauge_coercivity.md`.

Every U039-good four-dimensional macroblock now has a deterministic two-scale decomposition. With `ell=ceil(alpha^(-1/16))` and mesoscopic action threshold `eps=alpha^(1/2)`, one-cell separators plus internally bad mesoscopic cores occupy only `O(alpha^(1/16))` of the block. No probability or independence assumption is used.

On every remaining regular core an explicit maximal-tree/axial gauge gives an exact noncommutative plaquette-ribbon representation. All tree-gauge links then lie in one exponential chart with radius `O(alpha^(7/32))`. A local Taylor argument yields `||F-dA|| <= O(alpha^(1/16)) ||F||`, and the exact Wilson magnetic action is asymptotic to `||dA||^2/2`. A crude but explicit nonlinear core coercivity bound is `S_C >= (1-kappa)||A||^2/(192 ell^5)`. Independent core gauges are not glued; separator links, bad cores, topology and low collective modes remain explicit.

On U039's diagnostic `alpha=16 log(beta)/beta`, the mesoscopic cores grow in lattice units but are much smaller than the macroblock: `ell/n=O((log beta/beta)^(15/16))`. Under the same conditional logarithmic `beta(a)` diagnostic, their physical diameter tends to zero. This is not a continuum construction.

Nine exact new checks and all seven U039 checks passed. The new checker audits every tested axial-tree ribbon in dimensions 2-4, including an exact noncommutative Q8/SU(2)-subgroup ribbon identity. Wolfram independently corroborated the scale exponents. The result is self-reviewed and not formal/expert verification or a novelty claim.

Next target: condition on the separator/bad-core skeleton, integrate disjoint regular cores while retaining every boundary gauge representation, and prove that the induced skeleton interaction is surface-controlled and compatible with the centered physical transfer form. No continuum construction or physical Yang–Mills mass bound is established.

## Earlier checkpoint — U039, 2026-09-15

Read `research/audits/U039_interior_defect_transfer_suppression.md`.

U038's uniform bad-block probability now has a direct transfer-form use: when a defective four-dimensional block lies strictly inside a stationary Euclidean time slab, arbitrary endpoint states are exterior variables. Conditioning on the block exterior therefore gives an operator insertion bound `||R_bad||<=p`, rather than the norm-one endpoint-indicator obstruction. Finite unions cost only the sum of their conditional probabilities.

For `beta>=32`, the adaptive choice `alpha=16 log(beta)/beta` and `n>=2 beta/log(beta)` gives `p<=beta^(-4M)` with `M=6n^2(n+1)^2`. At the minimum scale the exponent is at least `384 beta^4/log(beta)^3`. On the standard logarithmic weak-coupling diagnostic this makes the entire interior dense-defect contribution to a fixed-physical-time transfer vanish in operator norm even after a crude `O(a^-4)` union bound. This is a diagnostic conditional on the stated beta(a) behavior, not a continuum construction.

On every surviving good block, the mean squared plaquette angle is `O(log beta/beta)`; all but `O(sqrt(log beta/beta))` of the plaquettes have vanishing angle, and on that overwhelming fraction the Wilson action is quadratic up to relative `O(sqrt(log beta/beta))` error. Sparse exceptional plaquettes and collective gauge modes are retained, not discarded.

Seven exact new checks and all ten U038 checks passed. Run `python checks/U039_interior_transfer_badblock_checks.py --output evidence/U039_checks.json`. Wolfram independently corroborated the adaptive identities and scaling limits. The result is self-reviewed finite-regulator mathematics, not formal/expert verification or a novelty claim.

Next target: prove a gauge-covariant coercive/background-field estimate for the all-good interior transfer while retaining sparse exceptional plaquettes, boundary representations and low collective modes. No continuum construction or physical Yang–Mills mass bound is established.

## Earlier checkpoint — U038, 2026-09-15

Read `research/audits/U038_boundary_surface_correction_and_defect_tail.md`.

**Historical correction:** U009's claimed arbitrary-boundary obstruction to volume-density action excess is withdrawn. A permitted identity-interior configuration pays only surface action, so a fixed positive density of large plaquette deficits has volume-order excess for sufficiently large blocks, uniformly in boundary links. U008's exact complete open-box counts were also wrong; the four-dimensional counts are `M=6n^2(n+1)^2` and `L=4n(n+1)^3`. Older files are preserved unchanged; this correction supersedes those claims, not all of their downstream auxiliary mathematics.

For the original finite Euclidean SU(2) Wilson measure with a common inverse coupling beta, conditioning on every exterior link gives `Pr(A_block>=alpha M | exterior)<=exp(-beta alpha M/4)` under the explicit sufficient thresholds in U038. Strong interfaces and arbitrary surrounding fields are allowed. The proof pays both a surface action cost and the Haar-volume denominator cost; it does not assume independent plaquettes or a Gaussian vacuum.

Uniform conditional bounds also control joint bad-block events and connected clusters without independence. A positive density of strongly frustrated link stars implies the required volume action, providing another concrete event covered by the estimate. These are defect probabilities, not a bound on the complete centered quantum transfer or a proof that all remaining fields are perturbatively small.

Ten exact new checks and all ten U037 checks passed. Run `python checks/U038_boundary_surface_checks.py --output evidence/U038_checks.json`. The checker includes a continuous-SU(2) compact-flux boundary witness, exact geometry and conservative parameter certificates; binary/Q8 fixtures are explicitly not Wilson samples. One symbolic structural-equality assertion was repaired, with its initial outputs retained. Wolfram corroborated finite algebra without warnings; compilation and indentation checks passed. Static lint/typecheck and Lean were unavailable. Self-review only, with no independent expert/formal verification or novelty claim.

Next target: convert the corrected defect-probability input into an energy-relative boundary/transfer estimate while retaining all physical sectors and controlling the collective modes on its complement. A rare event still has an indicator operator of norm one; the required relative estimate remains unproved. No continuum construction or scale-uniform physical mass bound is established.

## Preserved nearest dependencies

- U037: `research/audits/U037_interacting_blocks_and_boundary_sectors.md` — internally interacting blocks with weak interfaces, complete boundary representations, and the unresolved strong-interface response.
- U036: `research/audits/U036_column_comparison_and_uniform_lattice_gap.md` — volume-uniform gap only in the restricted small-spatial-coupling domain.
- U029–U035: unchanged exact integration, true-vacuum response, temporal-memory and history-variance records.
- U008–U009: historical records in Git; their stated boundary obstruction and complete-box counts are corrected by U038.
- U026–U028 and U003: unchanged restricted small-graph results and conditional gap transport; not a joint-limit construction.

# Yang–Mills Existence and Mass Gap Research

Private working repository. **No complete verified solution.**

The target is the full Jaffe–Witten/Clay assertion: a nontrivial four-dimensional quantum Yang–Mills theory for every compact simple gauge group in scope, with the required axioms, Yang–Mills identification, continuum/infinite-volume setting, and strictly positive finite physical mass gap.

## Latest checkpoint — U038, 2026-09-15

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

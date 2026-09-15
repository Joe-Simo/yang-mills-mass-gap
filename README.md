# Yang–Mills Existence and Mass Gap Research

Private working repository. **No complete verified solution.**

The target is the full Jaffe–Witten/Clay assertion: a nontrivial four-dimensional quantum Yang–Mills theory for every compact simple gauge group in scope, with the required axioms, Yang–Mills identification, continuum/infinite-volume setting, and strictly positive finite physical mass gap.

## Latest checkpoint — U037, 2026-09-15

Read `research/audits/U037_interacting_blocks_and_boundary_sectors.md`.

U036's time-column comparison extends to internally interacting link blocks without approximating their internal Wilson action. If every complete block kernel obeys `d(T_B^b)<=2log(5/3)` and the crossing-interface incidence obeys `bD<=1/16`, the full centered physical gap is at least `log(4/3)/(b tau)`, independent of the number of blocks. Here D sums crossing plaquette couplings with their block multiplicities; internal couplings are absent from D. A complete positive-kernel certificate permits arbitrary finite internal couplings, but its b grows exponentially with block size times temporal coupling.

An explicit periodic cubical tiling has influence count `12m^2+6m` per block of side m; uniform crossing coupling must be at most `1/[16b(12m^2+6m)]`. This covers an extensive strongly interacting interior with weak connections, not isotropic weak coupling. The susceptibility bound is independent of total volume but retains block-size dependence. No all-order complex expansion or continuum construction is proved.

The gluing audit retains every necessary boundary gauge representation: separate regional singlet projections can delete globally physical Wilson-loop states. An exact circle diagnostic identifies a lost fundamental-character channel. A necessary anisotropic coefficient match gives `beta_t beta_s -> 16/g^4`; temporal refinement alone cannot rescue U036's small-product condition. These diagnostics are not four-dimensional mass-gap counterexamples.

Ten new exact checks and all twelve U036 checks passed on their first local runs. Run `python checks/U037_interacting_block_checks.py --output evidence/U037_checks.json`. Binary and Q8 fixtures test finite algebra, not Wilson measurements. The proof, complete-state-space restrictions, source dictionary, actual commands and hashes are in the U037 note and manifest. Compilation and indentation checks passed; static lint/typecheck and Lean are unavailable. The initial Wolfram symbol warning and clean rerun are preserved. Self-review only, with no novelty or independent/formal verification claim.

Next target: control the connected boundary response in the full boundary-representation space, improving the product of block mixing time and interface influence for strong interfaces. An isolated block's singlet gap or an increasing fraction of strong internal plaquettes cannot replace that estimate. No scale-uniform physical continuum mass bound is established.

## Preserved nearest dependencies

- U036: `research/audits/U036_column_comparison_and_uniform_lattice_gap.md` — the homogeneous small-spatial-coupling benchmark and complete character-tail/comparison proof.
- U035: `research/audits/U035_true_vacuum_cycle_response.md` — true-vacuum responses and connected shared-loop terms.
- U032–U034: unchanged actual-vacuum memory, full-history and physical-cycle records.
- U029–U031: unchanged integration, temporal-memory and boundary-time records.
- U026–U028 and U003: unchanged restricted small-graph results and conditional gap transport; not a joint-limit Yang–Mills construction.

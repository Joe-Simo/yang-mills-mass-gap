# Yang–Mills Existence and Mass Gap Research

Private working repository. **No complete verified solution.**

The target is the full Jaffe–Witten/Clay assertion: a nontrivial four-dimensional quantum Yang–Mills theory for every compact simple gauge group in scope, with the required axioms, Yang–Mills identification, continuum/infinite-volume setting, and strictly positive finite physical mass gap.

## Latest checkpoint — U033, 2026-09-15

Read `research/audits/U033_history_conditioned_sparse_slabs.md`.

For an extensive spatial link set I with no two links on one plaquette, conditioning on the ENTIRE retained time history makes the discarded interior links factor into separate time chains. Actual correlated vacuum endpoint weights are preserved. Birkhoff contraction gives endpoint maximal correlation at most `theta_n=tanh(sum_e atanh(tanh(beta_e)^n))`, hence at most `|I| r^n` with `r=max_e tanh(beta_e)`. At fixed coupling, slab depth sufficient for fixed conditional accuracy grows logarithmically in |I|. This is not an improved one-step U032 projection bound.

On the true stationary path space, let Pi_n retain that history and J_t embed endpoint functions. Then `K^n=H_n+E_n`, where `H_n=J_0* Pi_n J_n` and `||E_n||<=theta_n`. There is an explicit all-time weighted remainder bound. The history operators H_n are not asserted to be powers of a reduced transfer. A full gap would still require a uniform bound on the entire centered physical retained-history contribution; an exact slow-retained-state example shows why that term cannot be deleted.

Twelve new exact checks and all twelve U032 checks passed. The checker `checks/U033_history_conditioned_slab_checks.py` includes actual spatial selection geometry, exact weighted path enumeration, arbitrary correlated endpoint factors, and ten continuous-SU(2) two-step cross-ratio certificates with complete rational series tails. Wolfram corroborated finite identities. Compilation and indentation checks passed; ruff/mypy/pyright/Lean are unavailable. Evidence, commands, domains and hashes are in `evidence/U033_manifest.json`. This is self-reviewed restricted mathematics, not formal/expert verification or a novelty claim.

Next target: bound the overlap of retained-history conditional-expectation ranges for multiple spatial color layers in the same Wilson vacuum, and connect it to the centered operator H_n. Exact intersection at constants is insufficient without a quantitative angle/variance estimate. No continuum construction or physical Yang–Mills mass bound is established.

## Preserved nearest dependencies

- U032: `research/audits/U032_true_vacuum_local_memory_bound.md` — fixed-set true-vacuum contraction, all-time Schur-memory tail, and non-tensorization control.
- U031: `research/audits/U031_boundary_time_and_weighted_memory.md` — finite Wilson slabs and finite-moment limitations.
- U030: `research/audits/U030_overlapping_decimation_and_transfer_memory.md` — overlapping integration and temporal-memory identities.
- U029: `research/audits/U029_exact_link_marginal_and_gauge_cancellation.md` — exact link integration, gauge cancellation, and generated interactions.
- U026–U028: unchanged small-graph results and limitations; not a joint-limit or volume-uniform physical mass theorem.
- U003: conditional full-space gap transport, not an established Yang–Mills construction.

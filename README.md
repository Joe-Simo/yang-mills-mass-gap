# Yang–Mills Existence and Mass Gap Research

Private working repository. **No complete verified solution.**

The target is the full Jaffe–Witten/Clay assertion: a nontrivial four-dimensional quantum Yang–Mills theory for every compact simple gauge group in scope, with the required axioms, Yang–Mills identification, continuum/infinite-volume setting, and strictly positive finite physical mass gap.

## Latest checkpoint — U035, 2026-09-15

Read `research/audits/U035_true_vacuum_cycle_response.md`.

The exact vacuum score under a local spatial source is `(I-K)^(-1)(I+K) w_centered` at every finite background. Differentiating the actual conditional variances retains a second-order projection-response term, and the slab score includes both true-vacuum endpoint contributions. These are response identities, not volume-uniform bounds on their connected correlations.

At ZERO spatial coupling, two shared plaquettes generate two exact temporal representation channels, with eigenvalues `r^6` and `r^6 u`, where `r=I_2(beta_t)/I_1(beta_t)` and `u=I_3(beta_t)/I_1(beta_t)`. Their connected logarithmic-vacuum coefficient is `b(z)=(z-r^8)/[(1-r^4)^2(1-z)]`. The mixed loop-orientation response is nonzero for every beta_t>0. Disconnected source supports cancel at every order by exact tensor factorization; this does not bound all connected coefficients.

For a FIXED FINITE set of small spatial sources with all exterior spatial couplings zero, a contour proof gives an exterior-volume-independent analyticity radius, an explicit all-order expectation remainder, and a complete physical-space transfer bound. The radius shrinks as `1/beta_t`; homogeneous activation loses volume through the sum of source sizes. Neither an interacting-exterior uniform bound nor the isotropic weak-coupling/continuum regime is covered.

Twelve new exact checks and all eleven U034 checks passed. Run `python checks/U035_vacuum_cycle_response_checks.py --output evidence/U035_checks.json`. Six named SU(2) response coefficients use complete rational series tails; weighted finite Markov fixtures test identities, not Wilson data. The manifest records preserved inputs, commands, ranges, outward rounding, and warning/clean Wolfram results. Compilation and indentation checks passed; static lint/typecheck and Lean were unavailable. Self-review only, with no novelty claim.

Next target: an all-order bound on the surviving connected source-support coefficients, independent of the total active volume and with explicit temporal-coupling dependence. Alternatively, bound the arbitrary-background susceptibility directly in the same vacuum. The entire centered history-variance estimate, continuum construction, nontrivial finite physical mass, and all-group target remain unproved.

## Preserved nearest dependencies

- U034: `research/audits/U034_history_variance_and_physical_cycles.md` — exact history-variance target, finite density comparison, physical cylinder diagnostic, forest bound.
- U033: `research/audits/U033_history_conditioned_sparse_slabs.md` — extensive sparse-column memory conditional on retained histories.
- U032: `research/audits/U032_true_vacuum_local_memory_bound.md` — fixed-set actual-vacuum contraction and all-time memory.
- U029–U031: unchanged exact integration, connected-memory, and boundary-time records in `research/audits/`.
- U026–U028 and U003: unchanged restricted small-graph results and conditional gap transport; not a joint-limit Yang–Mills construction.

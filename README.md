# Yang–Mills Existence and Mass Gap Research

Private working repository. **No complete verified solution.**

The target is the full Jaffe–Witten/Clay assertion: a nontrivial four-dimensional quantum Yang–Mills theory for every compact simple gauge group in scope, with the required axioms, Yang–Mills identification, continuum/infinite-volume setting, and strictly positive finite physical mass gap.

## Latest checkpoint — U032, 2026-09-15

Read `research/audits/U032_true_vacuum_local_memory_bound.md`.

For the actual finite Wilson transfer and conditional expectation in its TRUE vacuum measure, discarding a fixed link set I gives `||K Q_I|| <= tanh(sum_(e in I) beta_(t,e))`. The coefficient is independent of the retained lattice volume and spatial coupling, not of the number of discarded links or their temporal couplings. The proof uses conditional cross ratios: unknown positive vacuum weights cancel, without replacing the vacuum by Haar or a Gaussian.

This yields an all-time weighted-memory tail. With `r=tanh(sum beta_t)`, `N_k=B D^k B*`, and `r<q<1`, the tail after k=0,...,m is at most `(r/q)^(m+1) N_0/(q-r)`. Consequently `A+(M_2-A^2)/(q-r)<=qI` on the ENTIRE centered retained algebra is a sufficient full-transfer certificate. That retained inequality remains unproved uniformly in volume and regulator. Powers of D are not unprojected physical-time powers.

An exact correlated-endpoint example shows why independent temporal factors do not give an unchanged single-link coefficient for many discarded links. The example belongs to the broader positive-kernel class, not pure Wilson Yang–Mills. No extensive-block gap, continuum construction, or physical mass estimate is claimed.

Run `python checks/U032_conditional_memory_checks.py --output evidence/U032_checks.json`. Twelve exact tests passed, and all thirteen U031 checks were rerun. The new note and `evidence/U032_manifest.json` record domains, rational Bessel/exponential tails for four named SU(2) benchmarks, the repaired structural-equality checker defect, clean Wolfram algebra corroboration, and limitations. Compilation and indentation checks passed; static lint/typecheck and Lean were unavailable. This is self-reviewed auxiliary mathematics, not formal/expert verification or a novelty claim.

Next target: a retained-algebra Schur bound or a Wilson-specific collective conditional-variance estimate that improves the discarded-set dependence, in the same vacuum and physical-time representation. Local contraction alone does not protect slow collective retained states.

## Preserved nearest dependencies

- U031: `research/audits/U031_boundary_time_and_weighted_memory.md` — finite Wilson slabs, finite-moment and unweighted-memory obstructions, and the conditional all-time certificate.
- U030: `research/audits/U030_overlapping_decimation_and_transfer_memory.md` — exact overlapping integration and the projection-memory identity.
- U029: `research/audits/U029_exact_link_marginal_and_gauge_cancellation.md` — exact first link layer, gauge cancellation, non-Wilson generated interactions.
- U026–U028: complete small-graph results, shared-link/cubic constraints, and the failed global Gaussian small-field hypothesis; see their unchanged files in `research/audits/`.
- U003: `research/audits/U003_relative_gap_certificate.md` — conditional centered full-space gap transport, not an established Yang–Mills construction.

All older mathematical notes and checkers are preserved. The longer prior status entries remain in the parent revision's README at commit `aee6a18c4ccdb392fcfc412b128e36b545c92cf2`; this current-status view is compacted rather than duplicating those entries indefinitely. An earlier status label is not automatic validation of its proof. U032 does not rely on the disputed older scalar-localization sequence.

## Normalizations and non-claims

The Euclidean Wilson transfer uses spatial and temporal inverse couplings beta_s and beta_t. The earlier Hamiltonian parameter `lambda=4/g^4` is distinct. In the U002 curvature notation, `beta_W=4 beta_S`, so `beta_W=4/g0^2` corresponds to `beta_S=1/g0^2`; the direction `1-32 beta_S` is not in beta_W units.

No public posting, prize submission, researcher contact, paid computation, or unattended process is authorized by this repository status. A commit, a finite test, and a self-review are not a complete Yang–Mills proof.

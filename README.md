# Yang–Mills Existence and Mass Gap Research

Private working repository. **No complete verified solution.**

The target is the full Jaffe–Witten/Clay assertion: a nontrivial four-dimensional quantum Yang–Mills theory for every compact simple gauge group in scope, with the required axioms, Yang–Mills identification, continuum/infinite-volume setting, and strictly positive finite physical mass gap.

## Latest checkpoint — U036, 2026-09-15

Read `research/audits/U036_column_comparison_and_uniform_lattice_gap.md`.

For the actual finite SU(2) Wilson transfer, complete conditional time-column comparison gives a gap independent of spatial lattice size in an explicit SMALL-SPATIAL-COUPLING regime. With `b=ceil(3 max(1,beta_t))` and all spatial plaquette couplings `0<=s_p<=s0`, the sufficient condition is `b s0<=1/192`; the full centered physical gap is at least `log(4/3)/(b tau)`. The proof uses the complete character tail, coupled column updates, a block Gibbs-comparison theorem, and an actual-vacuum limit. The auxiliary update sampler is not identified with physical time.

Throughout that domain, the absolute sum of connected plaquette correlations over all plaquettes and all times is less than `256b/3` for a fixed plaquette. This controls U035's real susceptibility alternative without a factor equal to the total active volume, including homogeneous nonzero spatial backgrounds. It does NOT prove the all-order complex logarithmic-vacuum coefficient bound.

The allowed spatial coupling is of order `1/beta_t` at large temporal coupling. The isotropic continuum trajectory instead has `s0=beta_t` growing large and lies outside this theorem. No continuum construction, infinite-volume state construction, all-group theorem, or finite continuum mass is claimed. Restricted lattice gap and block-comparison mechanisms are established mathematics; no novelty claim is made.

Twelve exact new checks and all twelve U035 checks passed. Run `python checks/U036_column_comparison_checks.py --output evidence/U036_checks.json`. The proof, checker, exact results, repaired expected-denominator error, source dictionary and hashes are recorded in the U036 note and manifest. Binary-chain fixtures are not Wilson data; the all-character and all-volume arguments are written proofs. Compilation and indentation checks passed; ruff/mypy/pyright/Lean are unavailable. Self-review only, not independent expert or formal verification.

Next target: a conditional transfer comparison for an interacting spatial block retaining physical cycle variables, with constants controlled at physical scales rather than by the entire boundary action. Improving only the conservative constants or extrapolating the product-column smallness condition cannot justify the weak-coupling continuum passage.

## Preserved nearest dependencies

- U035: `research/audits/U035_true_vacuum_cycle_response.md` — exact vacuum scores, connected shared-loop response, finite-source analyticity and its limitations.
- U032–U034: unchanged actual-vacuum conditional-memory, retained-history and physical-cycle records in `research/audits/`.
- U029–U031: unchanged exact integration, connected-memory and boundary-time records in `research/audits/`.
- U026–U028 and U003: unchanged restricted small-graph results and conditional gap transport; not a joint-limit Yang–Mills construction.

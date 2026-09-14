# Yang–Mills Existence and Mass Gap Research

Private working repository for a rigorous attempt to resolve the Clay Yang–Mills existence and mass gap problem.

## Status

**No complete verified solution.**

The project targets the Jaffe–Witten/Clay assertion: construction of a nontrivial four-dimensional quantum Yang–Mills theory for every compact simple gauge group in the official scope, satisfying the required axioms and possessing a strictly positive physical mass gap.

## Latest checkpoint — U003, 2026-09-14

Read `research/audits/U003_relative_gap_certificate.md` for the conditional full-space gap-transport theorem, its proof, exact SU(2) initialization tests, source locators, and remaining obligations. This is self-reviewed partial research, not a complete candidate or formal/expert verification.

The new estimate controls retained states, all discarded states, and their mixed quadratic form at one fixed physical time. Relative errors with a summable squared mixing coefficient preserve a positive product margin under the explicitly stated hypotheses. Those hypotheses have not been established for a continuum Yang–Mills construction.

The raw Haar/electric reference fails a concrete small-relative-magnetic-perturbation test already on two gauge-invariant SU(2) plaquette characters. A follow-up positive one-plaquette trial state also fails a small global residual-oscillation test; weighted or energy-relative estimates remain possible. Neither failure is a counterexample to Yang–Mills.

Run `python checks/U003_relative_gap_checks.py` in an environment with SymPy. The actual Python 3.13.5 / SymPy 1.14.0 output is in `evidence/U003_checks.log`: **12 tests passed**. The preceding U002 tests also passed when rerun. Finite tests do not establish the infinite-dimensional or continuum claims; the conditional theorems use the written proofs.

Next executable step: derive a weighted or energy-relative residual estimate for the positive trial state, then test the shared-link terms for two adjacent plaquettes without assuming independent plaquettes or a pre-existing infinite-volume gap.

### Correction to the inherited coupling notation

The initial record below used `beta` for two different conventions. For exponent `2 beta_S Tr(U_p)` versus ordinary SU(2) Wilson exponent `(beta_W/2) Tr(U_p)`, one has `beta_W=4 beta_S`. Thus `beta_W=4/g0^2` corresponds to `beta_S=1/g0^2`. The curvature direction is `1-32 beta_S`, with failure of strict global positivity at `beta_S>=1/32`. Both inverse couplings diverge along the proposed weak-coupling continuum trajectory. This correction was derived in U002 and is retained in U003; the original wording below is historical, not the current normalization.

## Initial research state — preserved historical wording

1. Strong-coupling lattice results are relevant partial inputs but do not directly reach the continuum scaling trajectory.
2. A direct SU(2), d=4 calculation gives a configuration/direction where the Bakry–Émery curvature of the Wilson lattice measure equals `1 - 32 beta`; hence any proof requiring globally positive Bakry–Émery curvature of this standard form fails for `beta > 1/32`, while the Wilson continuum trajectory has `beta = 4/g0^2 -> infinity`.
3. A 2026 published/arXiv claim of a complete reflection-positive construction (Faizal–Shabir, arXiv:2606.19362) is under audit. A concrete internal inconsistency has been identified: several sections simultaneously require a compactly supported spectral cutoff and a positive heat-kernel/Laplace representation, which is impossible for a nonzero completely monotone function. Other sections of the same manuscript explicitly acknowledge this impossibility and switch to non-compact completely monotone profiles. This must be resolved before the paper can be treated as a valid proof.

See `research/checkpoints/checkpoint-2026-09-14.md` for the historical derivations and source details, and `research/audits/U002_transfer_limit_audit.md` for subsequent corrections and the conditional physical-time bridge.

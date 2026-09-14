# Yang–Mills Existence and Mass Gap Research

Private working repository for a rigorous attempt to resolve the Clay Yang–Mills existence and mass gap problem.

## Status

**No complete verified solution.**

The project targets the Jaffe–Witten/Clay assertion: construction of a nontrivial four-dimensional quantum Yang–Mills theory for every compact simple gauge group in the official scope, satisfying the required axioms and possessing a strictly positive physical mass gap.

## Current research state

1. Strong-coupling lattice results are relevant partial inputs but do not directly reach the continuum scaling trajectory.
2. A direct SU(2), d=4 calculation gives a configuration/direction where the Bakry–Émery curvature of the Wilson lattice measure equals `1 - 32 beta`; hence any proof requiring globally positive Bakry–Émery curvature of this standard form fails for `beta > 1/32`, while the Wilson continuum trajectory has `beta = 4/g0^2 -> infinity`.
3. A 2026 published/arXiv claim of a complete reflection-positive construction (Faizal–Shabir, arXiv:2606.19362) is under audit. A concrete internal inconsistency has been identified: several sections simultaneously require a compactly supported spectral cutoff and a positive heat-kernel/Laplace representation, which is impossible for a nonzero completely monotone function. Other sections of the same manuscript explicitly acknowledge this impossibility and switch to non-compact completely monotone profiles. This must be resolved before the paper can be treated as a valid proof.

See `research/checkpoints/checkpoint-2026-09-14.md` for derivations and source details.

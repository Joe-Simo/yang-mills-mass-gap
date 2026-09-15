# Yang–Mills Existence and Mass Gap Research

Private working repository for a rigorous attempt to resolve the Clay Yang–Mills existence and mass gap problem.

## Status

**No complete verified solution.**

The project targets the Jaffe–Witten/Clay assertion: construction of a nontrivial four-dimensional quantum Yang–Mills theory for every compact simple gauge group in the official scope, satisfying the required axioms and possessing a strictly positive physical mass gap.

## Latest checkpoint — U029, 2026-09-15

Read `research/audits/U029_exact_link_marginal_and_gauge_cancellation.md`. Exact SU(2) Wilson-link integration gives `Z(z)=2 I_1(z)/z`, with the regular value `Z(0)=1`, and a gauge-invariant generated-loop action. For every surrounding link configuration, that action is bounded above and below by sums of retained loop deficits, with coefficients independent of lattice size. An extensive noncofacial first elimination layer factorizes exactly; this is a coordinate marginal, NOT a momentum-shell integration or a true-vacuum Hamiltonian comparison.

The marginal Hessian is `E[S'']-Var(S')`. Along a common endpoint-gauge variation the covariance cancels the entire positive averaged curvature, so dropping it would create a spurious gauge mass. Exact noncommutative quartic terms are retained. For two staples the induced action is not linear in the retained Wilson-loop deficit at any positive coupling; further integrations cannot be represented exactly by a single updated Wilson coupling. Frustrated boundary stars can have an exactly Haar conditional law even as the bare coupling parameter grows.

Eleven focused new tests and all thirteen U028 tests passed. Run `python checks/U029_exact_link_integration_checks.py --output evidence/U029_checks.json`. Exact rational positive-series tails enclose the Bessel-ratio coefficients at six nonnegative arguments; separate quadrature and Wolfram results are corroboration only. Compilation and indentation checks passed; static lint/typecheck and Lean were unavailable. No prior research note or checker was modified; only this README changes an older manifest-covered file, whose earlier version remains in Git and the supplied archive.

Next executable target: control overlapping generated-loop interactions in a second elimination and establish a centered physical-time transfer comparison in the actual vacuum. No mass-gap estimate, repeated-RG bound, continuum construction, or novelty claim follows from this exact first-layer action result.

## Earlier checkpoint — U028, 2026-09-15

Read `research/audits/U028_cubic_constraints_and_small_field_test.md`. The three-dimensional cubical complex retains Bianchi constraints: one cube has five independent curl directions, with positive eigenvalues 4 (three times) and 6 (twice). A tensor proof gives the full transverse spectrum on every open rectangular box. For each fixed N-cube, the full physical weak-coupling gap satisfies `lim_{g->0} a Delta_N=4sqrt(2)sin(pi/[2(N+1)])`; no joint coupling/size limit is inferred.

An exact nonlinear Wilson-potential comparison has constants independent of support size on a specified, compactly supported linear-Coulomb slice: with `alpha=(32/sqrt(3))||Q||_3<1`, the potential lies between `(1-alpha)^2||curl A||^2/2` and `(1+alpha)^2||curl A||^2/2`. This is not a global nonlinear gauge choice, a kinetic estimate, or a true-vacuum gap bound.

The next probability test rejects treating that global bare small-norm region as a dominant Gaussian sector: in the transverse quadratic vacuum, its probability tends to zero when `g_N N` grows without bound, including the defined test sequence `g_N^2=1/log(N+1)`. The proof treats correlated link fields through independent normal coordinates; it makes no probability claim for the true interacting vacuum.

Thirteen new exact tests, all eleven U027 tests and all nine U026 tests passed. Run `python checks/U028_cubic_and_small_field_checks.py --output evidence/U028_checks.json`; the derivations, test scopes, Wolfram corroboration and hashes are recorded in `evidence/U028_manifest.json`. Earlier manifest-covered files were preserved. Compilation and indentation checks passed; no static lint/typecheck or Lean success is claimed. Results are self-reviewed auxiliary mathematics, not formal or independent expert verification.

Next executable target: integrate short modes conditional on a retained low background and check gauge constraints on induced terms, with explicit remainder/volume control. A globally small bare field, a fixed-graph oscillator gap, or classical potential coercivity cannot substitute for a centered true-vacuum estimate in the joint limit.

## Earlier checkpoint — U027, 2026-09-15

Read `research/audits/U027_shared_link_and_patch_scaling.md`. The full two-square physical space retains simultaneous-conjugation mixed states. An exact three-path reduction gives `T=2(C_U+C_V)+R_U.R_V`; the separate-trace subspace contains no nonzero Hamiltonian eigenstate at positive magnetic coupling. The complete fixed-graph weak-coupling gap is `(2sqrt(3)+o(1))/a`, agreeing with the known leading result and smaller than the independent-square gap.

A fixed-rectangle extension gives `lim_{g->0} a Delta_(N,N)=4sqrt(2)sin(pi/[2(N+1)])`, which tends to zero as the planar square patch grows. The proof keeps the weak-coupling and graph-size limits separate; no joint-limit or four-dimensional continuum conclusion is claimed. This rules out an unchanged, graph-size-uniform cell-gap coefficient for these planar models.

Eleven new exact symbolic tests and all nine U026 tests passed. The new checker is `checks/U027_shared_link_checks.py`, with output/provenance in `evidence/U027_checks.json` and `evidence/U027_manifest.json`. Wolfram independently confirmed the shared-link polynomial action. All U026 manifest hashes were preserved. The results are self-reviewed auxiliary proofs, not formal or independent expert verification.

Remaining target: a true-vacuum centered comparison on growing spatial three-dimensional blocks, retaining collective mixed-loop states and controlling weak coupling and size uniformly. Finite-cell gaps, oscillator asymptotics, and Ritz upper bounds cannot replace that estimate.

## Earlier checkpoint — U026, 2026-09-15

Read `research/audits/U026_one_plaquette_true_vacuum_gap.md`. On the COMPLETE physical Hilbert space of an isolated SU(2) square, a comparison proof gives a true-vacuum gap at least `max(1,g^2/2)/a`; its weak-coupling value is `(4+o(1))/a`. This is a cutoff-scale gap, not a finite continuum mass. The radial reduction and leading asymptotic are known after normalization translation; no novelty claim is made.

The unit also proves that independent-square refinement loses bounded-norm positive-time finite-energy content, and exhibits a nonzero mixed two-loop invariant omitted by tensor products of individual class functions. No many-plaquette lower bound follows from the one-square result.

Run `python checks/U026_one_plaquette_certificate.py --test` and `python checks/U026_one_plaquette_certificate.py`. Nine focused tests passed; `evidence/U026_certificates.json` records exact rational enclosures at five couplings, with the omitted infinite tail controlled analytically. Wolfram and a separate tridiagonal computation corroborated the results. A conflicting SciPy Mathieu output at the largest coupling was rejected and retained in the evidence. Compilation and indentation checks passed; static lint/typecheck tools were unavailable. Historical suites were not rerun in U026.

Next executable target: derive and test the complete shared-link kinetic form for two adjacent squares, including simultaneous-conjugation mixed states. Do not multiply independent-plaquette gaps or infer lower gaps from Ritz eigenvalues alone. U026 does not validate the entire older scalar-localization chain; previous records remain preserved for audit.

## Earlier checkpoint — U003, 2026-09-14

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

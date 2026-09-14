# Checkpoint 2026-09-14 — lattice curvature obstruction and 2026-claim audit

Status: partial research only. The Yang–Mills existence and mass gap problem is not solved.

## 1. Exact target

The target is the Clay/Jaffe–Witten four-dimensional quantum Yang–Mills existence and mass-gap problem, including construction of the nontrivial continuum theory and a positive gap in the physical Hamiltonian spectrum. Finite-lattice or fixed-cutoff gaps are partial results only.

## 2. Strong-coupling lattice input

H. Shen, R. Zhu, X.-C. Zhu, *A Stochastic Analysis Approach to Lattice Yang–Mills at Strong Coupling*, Commun. Math. Phys. 400 (2023), 805–851, arXiv:2204.12737, proves a positive mass gap for infinite-volume lattice SU(N) Yang–Mills when

    |beta| < 1 / (16(d-1)).

For d=4 this is `|beta| < 1/48`.

This does not overlap the Wilson continuum limit: for SU(2), `beta = 4/g0^2`, while asymptotic freedom requires `g0 -> 0`, hence `beta -> infinity` as the lattice spacing tends to zero.

## 3. Exact no-go calculation for global Bakry–Émery curvature at weak coupling

Work with SU(2) and the bi-invariant metric induced by

    <X,Y> = Re Tr(X Y*)

so a unit Cartan generator is

    H = diag(i,-i)/sqrt(2).

For the Wilson Gibbs exponent in the Shen–Zhu–Zhu convention,

    S(U) = beta N sum_p Re Tr(U_p),   N=2.

On an even periodic four-dimensional lattice choose a center-valued Z2 gauge configuration whose plaquettes all equal `-I` (the constant Z2 2-cocycle has zero plane flux when the linear size is even, hence is exact). Perturb links in the commuting Cartan direction:

    U_e(t) = z_e exp(t a_e H).

Then for every plaquette

    U_p(t) = -I exp(t (da)_p H)

and

    Re Tr(U_p(t)) = -2 cos(t (da)_p/sqrt(2)).

Therefore

    d^2/dt^2 S(U(t))|_{t=0}
      = 2 beta ||da||^2.

For a transverse 1-cochain at Fourier momentum `(pi,pi,pi,pi)`, the top eigenvalue of `d* d` is 16, so

    ||da||^2 = 16 ||a||^2

and hence

    Hess S[a,a] = 32 beta ||a||^2.

The SU(2) Ricci curvature in this normalization is 1, so the Bakry–Émery quadratic form `Ric - Hess S` in this direction is

    (1 - 32 beta) ||a||^2.

Thus the global Bakry–Émery curvature cannot be positive for all configurations once

    beta > 1/32.

This is stronger than merely observing that the published sufficient estimate stops at `1/48`: it exhibits an explicit obstruction to any continuum proof that requires a global positive Bakry–Émery lower bound for the unmodified Wilson measure in this normalization. It does **not** rule out localized, gauge-reduced, multiscale, hypocoercive, or other non-global-convexity methods.

A Wolfram exact check of the chosen mode returned `||da||^2/||a||^2 = 16` and the resulting curvature direction `1 - 32 beta`.

## 4. Audit of Faizal–Shabir 2026 claimed construction

Source: M. Faizal, A. Shabir, *Reflection-Positive Construction of a Four-Dimensional SU(N) Yang-Mills Theory with Mass Gap and Confinement*, Fortschritte der Physik 74 (2026), e70097; arXiv:2606.19362v1.

The manuscript makes a complete-solution-level claim. It cannot presently be treated as a verified solution because of at least the following concrete inconsistency.

### 4.1 Impossible compact-support + positive-Laplace requirement

Several sections define a smooth/Gevrey spectral cutoff `chi_sigma` satisfying

    chi_sigma(lambda) = 1 for 0 <= lambda <= sigma,
    chi_sigma(lambda) = 0 for lambda >= 2 sigma,

and simultaneously assert a positive heat-kernel representation

    chi_sigma(D) = integral_0^infinity exp(-t D) dnu_sigma(t)

with `dnu_sigma` a finite positive measure.

This is impossible. If

    f(lambda) = integral_0^infinity exp(-t lambda) dnu(t),   dnu >= 0,

and `f(lambda0)=0` for any finite `lambda0>0`, then the integrand is strictly positive for every finite `t`, so the integral can vanish only if `nu=0`; then `f(0)=0`, contradicting `f(0)=1`. Equivalently, a nonzero completely monotone function cannot have compact support.

The contradiction occurs, for example, around the paper's equations (7.7)–(7.8) and analogous later definitions.

### 4.2 The manuscript itself acknowledges the contradiction elsewhere

Other parts of the same arXiv manuscript explicitly state that compact support and complete monotonicity cannot simultaneously hold and replace the sharp/compact cutoff by a rapidly decaying, non-compact completely monotone profile such as `exp(-lambda/sigma^2)`.

Therefore the document contains mutually incompatible definitions for a load-bearing auxiliary operator used in reflection-positivity/locality arguments. Until every theorem is checked under one consistent definition and the dependent estimates are re-proved, the claimed construction is not verified.

### 4.3 Separate proposition-level error

Proposition 8.8 in one section claims that exponential decay of the two-point function of a **fixed nonzero** local observable implies a lower bound on the full Hamiltonian spectral gap. This implication is false without a cyclicity/density statement covering a sufficiently rich family of observables.

Abstract counterexample: take

    H = diag(0, epsilon, m)

on `span{Omega,e1,e2}`, with `0 < epsilon < m`, and choose an observable A with `A Omega = e2`. Then

    <Omega, A exp(-tH) A Omega> = exp(-m t)

although the true spectral gap is `epsilon`. Decay for one observable only controls the spectral measure seen by that observable.

Elsewhere the manuscript gives a density-based argument for **all** local observables, which is a different and potentially repairable statement. Proposition 8.8 as written remains incorrect and is used later for a robustness claim, so those downstream uses require re-audit.

## 5. Current conclusion

- The global Bakry–Émery route is structurally blocked before the continuum regime for standard SU(2) Wilson lattice Yang–Mills.
- The 2026 Faizal–Shabir claimed complete construction contains explicit internal mathematical inconsistencies and cannot presently revise the Clay open-problem status.
- The next viable route should avoid global convexity and should demand a consistent reflection-positive multiscale construction with a genuinely uniform physical-unit gap along the asymptotically free trajectory.

## 6. Sources

- Clay Mathematics Institute, Yang–Mills and Mass Gap: https://www.claymath.org/millennium/yang-mills-the-maths-gap/
- Jaffe–Witten official problem description: https://www.claymath.org/wp-content/uploads/2022/06/yangmills.pdf
- Shen–Zhu–Zhu: https://arxiv.org/abs/2204.12737
- Faizal–Shabir: https://arxiv.org/abs/2606.19362

# U014 — sharp low-mode projector boundary leakage

Date: 2026-09-14.

**We have not solved the Yang–Mills problem yet.**

This bounded attempt tests U013's first localization question in the simplest exactly analyzable model: a one-dimensional periodic sharp Fourier projector cut by a spatial half-block. The result is a warning/no-go for using a **sharp** spectral projector as a local coarse/fine splitter: its boundary commutator does not acquire power-law decay with block size. This does not rule out smooth spectral windows or finite-range decompositions.

## 1. Exact model

On the periodic lattice Z/NZ, let P_m project onto Fourier modes |k|<=m, with 1<<m<<N. Its translation-invariant kernel is the Dirichlet kernel divided by N:

    K_m(r)= sin((2m+1) pi r/N) / [N sin(pi r/N)].

Let chi be multiplication by the indicator of a half-circle block. Then

    [chi,P_m](x,y) = [chi(x)-chi(y)] K_m(x-y).

The Hilbert-Schmidt norm therefore counts only pairs crossing the spatial cut:

    ||[chi,P_m]||_HS^2
      = sum_(x,y) |chi(x)-chi(y)|^2 |K_m(x-y)|^2.

For separations r much smaller than N, the number of crossing pairs is proportional to r. This turns the problem into a weighted Dirichlet-kernel tail.

## 2. Two-scale kernel bound

Elementary sine bounds give, up to absolute constants,

    |K_m(r)| <= min((2m+1)/N, 1/r)

for 1<=r<=N/2. The crossover is

    r0 ~ N/(2m+1).

Consequently the crossing-pair sum has the upper-bound structure

    sum_(r<=r0) r (m/N)^2
      + sum_(r0<r<=N/2) r (1/r^2).

The first term is O(1). The second is

    O(log(N/r0)) = O(log m).

A continuous proxy checked by Wolfram 15.0.1 gives exactly the same structure: 1/2 plus (1/4)log(m+1/2), modulo the irrelevant normalization constants of the bound.

The logarithm is not the main problem. The key fact is that this estimate has **no negative power of N**. A sharp low-pass projector has a long algebraic Dirichlet-kernel tail, so cutting it spatially creates nonvanishing boundary leakage.

## 3. Lower-bound mechanism

The lack of decay is structural, not merely an artifact of the upper bound. Around the crossover r~N/m, the kernel magnitude is generically of order m/N on a positive fraction of separations away from its zeros. There are order N/m such separations in a crossover band, and each has order N/m crossing pairs. Hence their combined squared contribution is order

    (N/m)*(N/m)*(m/N)^2 = O(1).

Making this into a uniform numerical constant requires excluding the Dirichlet-kernel zero locations carefully; the present note records the mechanism rather than claiming a sharp universal lower constant. It is enough to reject any expectation of automatic surface/volume power suppression from a sharp cutoff.

## 4. Four-dimensional implication

For a tensor/product Fourier box, localizing one coordinate already inherits the one-dimensional leakage mechanism. Additional tangential low modes multiply the number of leaking channels rather than cure the nonlocal tail. Therefore a sharp spectral split is a poor candidate for the U003 mixed-form coefficient: favorable coarse dimension from U013 does not imply a small commutator with spatial block localization.

This is an auxiliary scalar-model obstruction. A Yang–Mills transfer-form norm is not identified with this Hilbert-Schmidt norm, so no direct failure of U003 is claimed.

## 5. Direction change: smooth windows

The obstruction comes from the discontinuity of the spectral symbol. Replace the sharp indicator 1_{lambda<=lambda_cut} by a smooth cutoff f(lambda/lambda_cut), equal to one below a lower threshold and zero above a higher threshold. Smooth functional calculus can have much faster spatial kernel decay than the Dirichlet kernel. The transition band becomes an overlap sector assigned explicitly to the coarse/fine coupling.

This changes the research question to a quantitative uncertainty tradeoff:

- spectral transition width Delta lambda;
- spatial decay/range of f(L);
- number of transition modes;
- resulting mixed-form coefficient.

A polynomial cutoff of degree R is strictly finite range R. Unlike U012, it need not approximate 1/lambda near zero; it only approximates a bounded smooth step. This may avoid the n^2 condition-number obstruction entirely.

## 6. Outcome classification

Outcome: **sharp-cutoff route obstructed in the scalar periodic model**.

Established:

- exact Dirichlet-kernel representation;
- commutator support on crossing pairs;
- O(1)+O(log m) Hilbert-Schmidt upper structure with no power decay;
- a structural O(1) crossover contribution mechanism.

Not established:

- a sharp constant lower bound uniform in all N,m;
- the corresponding operator norm asymptotic;
- a direct U003 transfer-form bound;
- any nonlinear/nonabelian conclusion.

## 7. Next bounded attempt

Use a smooth spectral cutoff with transition width comparable to lambda_cut. Construct a polynomial approximation of the smooth cutoff and derive degree/range versus error using the spectral interval [0,lambda_max]. Count transition-band modes for lambda_cut=n^-q. The route is promising only if one can obtain simultaneously: range o(n), polynomially small approximation error, and transition-sector dimension no worse than the U013 coarse sector. This directly addresses the sharp-projector leakage mechanism rather than reopening the failed uniform inverse approximation.
# U022 — ultrasoft global sector: polylog count proved, dimension does not protect its gap

Date: 2026-09-14.

**We have not solved the Yang–Mills problem yet.**

This bounded attempt executes U021's next task. The four-dimensional scalar lattice box has only polylogarithmically many modes below the strengthened-collar localization threshold, but an exact abstract counterexample shows that this dimension bound alone gives no spectral-gap protection. The global ultrasoft sector therefore needs a genuine inter-scale inheritance/isometry estimate; it cannot be dismissed as small merely because it has few coordinates.

## 1. Ultrasoft threshold

Fix epsilon>0 and use the strengthened shell collar

    w(lambda,n)=lambda^(-1/2) log^(1+epsilon)n.

A shell ceases to fit locally when w is comparable to the block side n. The threshold is

    lambda_g(n)=C_g n^(-2) log^(2+2epsilon)n,

up to a fixed geometric constant C_g. Modes below lambda_g are left in the global ultrasoft sector.

## 2. Rigorous four-dimensional count up to constants

For the Dirichlet scalar Laplacian on an n^4 box,

    lambda(k)=4 sum_(mu=1)^4 sin^2[pi k_mu/(2(n+1))],
    1<=k_mu<=n.

For 0<=x<=pi/2,

    (2/pi)x <= sin x <= x.

Therefore, for low modes, lambda(k)<=lambda_g implies

    |k|^2 <= C n^2 lambda_g
           <= C' log^(2+2epsilon)n.

Thus

    |k| <= C'' log^(1+epsilon)n.

The number of positive integer 4-tuples in such a ball is at most the number in a containing four-dimensional cube, giving

    N_global(n)
      <= C log^(4+4epsilon)n.                            (G)

A matching lower-order exponent follows by placing a positive-orthant cube inside the ball, so away from floor effects the count is Theta(log^(4+4epsilon)n) for thresholds with a sufficiently large fixed constant. The upper bound (G) is all the route needs.

Wolfram 15.0.1 independently simplified the radius power to log^(1+epsilon)n and its fourth power to log^(4+4epsilon)n; for epsilon=1 it also returned the ratio to n^3 tending to zero.

Hence the global ultrasoft sector is sub-boundary by an enormous margin.

## 3. Dimension-only gap protection is false

Let m_j be any positive integer sequence, even m_j=1. On

    H_j = span{Omega} direct-sum C^(m_j)

define a positive transfer deficit

    G_j Omega=0,
    G_j|_(Omega-perp)=delta_j I,

with delta_j>0 and delta_j->0. Then S_j=I-G_j is a positive self-adjoint contraction whenever delta_j<=1, with a unique vacuum Omega at every finite j, but its centered gap is delta_j->0.

Thus even a **one-dimensional** ultrasoft sector can carry a collapsing gap. Polylogarithmic dimension provides no lower spectral bound.

This is an abstract operator counterexample, not a Yang–Mills counterexample.

## 4. What inheritance must mean

The global ultrasoft modes must be compared from scale j-1 to scale j by an actual vacuum-preserving map J_j whose image contains the inherited ultrasoft states. A sufficient condition is the same relative coarse inheritance structure used in U003/U019:

    A_j >= (1-eta_j) J_j G_(j-1) J_j*,
    sum_j eta_j < infinity,                              (I)

with all newly appearing global modes either:

1. included in a fine/new-mode sector with a uniform lower deficit; or
2. matched to previous-scale modes by an enlarged J_j and controlled by a separate relative estimate.

Merely noting that only polylog many new modes appear does not establish either alternative.

## 5. New-mode counting per scale

Because the global threshold radius is

    r_g(n)~log^(1+epsilon)n,

under geometric block growth n_j~b^j we have

    r_g(n_j)=Theta(j^(1+epsilon)),
    N_global(n_j)=O(j^(4+4epsilon)).

The number of additional global coordinates from one RG step to the next is polynomial in j, not uniformly bounded. A finite-rank perturbation theorem with constants proportional to rank would therefore accumulate badly unless accompanied by strong per-mode decay. This again favors an explicit inter-scale mode matching rather than treating new ultrasoft coordinates perturbatively.

## 6. Scalar mode matching suggests a clean auxiliary map

In the free scalar box model, low Fourier/sine modes have canonical momentum labels. Under geometric blocking, a physical long-wavelength mode can be identified with the corresponding lower-resolution mode, modulo discretization and boundary conventions. This provides a natural candidate J_j at the linearized level.

However, the target Yang–Mills problem has no fixed global Fourier basis in arbitrary gauge backgrounds. A useful nonabelian analogue would need gauge-covariant block variables or covariant-Laplacian eigenmodes, whose dependence on the background can itself be nonlocal and spectrally unstable. Therefore the scalar matching is a guide, not a transferred theorem.

## 7. Interaction with U021

The strengthened-collar architecture now has the following scalar obligations:

- localized shells: candidate aggregate mixing is summable if the required l2 output estimate holds;
- ultrasoft global sector: dimension is only polylogarithmic, but its gap must be inherited through (I);
- high fine sector: requires uniform coercivity relative to the transported gap.

This separates the two problems cleanly. No further improvement in mode counting can substitute for inheritance.

## 8. Outcome classification

Outcome: **count proved; dimension-only inheritance route refuted**.

Proved:

    N_global=O(log^(4+4epsilon)n)

for the four-dimensional scalar Dirichlet box under the strengthened-collar threshold.

Refuted:

- any inference from small/polylog dimension alone to a positive ultrasoft spectral gap.

Required next input:

- an explicit inter-scale matching J_j with summable relative inheritance loss for ultrasoft modes.

Not proved:

- shell-output l2 aggregation in the spatially localized model;
- transfer-deficit mode matching;
- gauge-covariant/nonabelian inheritance;
- reflection positivity, OS construction, or Yang–Mills mass gap.

## 9. Next bounded attempt

Test inheritance in the free scalar model where exact Fourier/sine modes are available. Choose nested periodic lattices with blocking factor b and compare the fixed-physical-time transfer deficits of matched low momentum modes under a specified discretization. Derive the relative error between coarse and fine dispersion relations for |k| below the ultrasoft threshold. If that error is O((k/n)^2) or another summable power along geometric scales, the scalar ultrasoft inheritance obligation closes. If it remains O(1), the current blocking architecture fails even before the nonabelian problem.
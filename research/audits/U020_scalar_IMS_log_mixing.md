# U020 — scalar IMS commutator gives the logarithmic mixing scale

Date: 2026-09-14.

**We have not solved the Yang–Mills problem yet.**

This bounded attempt executes U019's scalar localization test. In the nearest-neighbor scalar lattice Laplacian model, a spatial cutoff varying on width w yields a commutator estimate whose natural relative size on modes of energy scale lambda_c is O((w sqrt(lambda_c))^-1 + (w^2 lambda_c)^-1). Choosing

    w = lambda_c^(-1/2) log n

therefore gives O(1/log n). This proves the desired logarithmic scaling for the scalar quadratic localization commutator under explicit spectral-energy hypotheses. It does not yet prove the U019 mixing bound for the Yang–Mills transfer deficit.

## 1. Discrete scalar setup

Let L be the standard positive graph Laplacian on a bounded-degree nearest-neighbor lattice,

    <u,Lu> = (1/2) sum_(x~y) |u(x)-u(y)|^2

(up to a fixed convention factor irrelevant to scaling). Let chi be a real multiplication function with

    |chi(x)-chi(y)| <= C_chi/w

on every edge and second-difference scale O(w^-2), as supplied by a fixed smooth profile rescaled across a collar of width w.

For multiplication by chi,

    [L,chi]u(x)
      = sum_(y~x) [chi(x)-chi(y)] u(y)

up to the chosen sign convention for L. Rewriting u(y)=u(x)+[u(y)-u(x)] separates a first-difference term and a discrete-Laplacian-of-chi term. Cauchy–Schwarz and bounded degree give

    ||[L,chi]u||
      <= C1 w^-1 ||L^(1/2)u|| + C2 w^-2 ||u||.          (C)

The constants depend only on lattice degree and the fixed cutoff profile, not on n,w.

This is the discrete analogue of the continuum identity

    [-Delta,chi]u = -2 grad chi . grad u - (Delta chi)u.

No probability or Yang–Mills input enters.

## 2. Relative low-energy estimate

Suppose x lies in a low spectral sector

    <x,Lx> <= c0 lambda_c ||x||^2.

Then (C) gives

    ||[L,chi]x||
      <= [C1 sqrt(c0 lambda_c)/w + C2/w^2] ||x||.

Relative to the natural low-energy quadratic scale lambda_c ||x||, this is

    ||[L,chi]x|| / [lambda_c ||x||]
      <= C1 sqrt(c0)/(w sqrt(lambda_c))
         + C2/(w^2 lambda_c).                            (R)

Choose

    w = A lambda_c^(-1/2) log n,

with fixed A>0. Then

    1/(w sqrt(lambda_c)) = 1/(A log n),
    1/(w^2 lambda_c) = 1/(A^2 log^2 n).

Wolfram 15.0.1 independently simplified these three dimensionless combinations to Log[n]^-1, Log[n]^-2, Log[n]^-1 under A=1.

Therefore

    relative commutator = O(1/log n).                    (L)

## 3. Bilinear coarse/fine consequence in the scalar model

Let x be low energy as above and let y be a fine vector with

    <y,Ly> >= c1 lambda_c ||y||^2,

where c1>c0>0 is a fixed spectral separation. A localization-generated cross term of the form

    |<y,[L,chi]x>|

obeys, using ||y|| <= (c1 lambda_c)^(-1/2)<y,Ly>^(1/2),

    |<y,[L,chi]x>|
      <= C [1/(w sqrt(lambda_c)) + 1/(w^2 lambda_c)]
         <x,Lx>^(1/2)<y,Ly>^(1/2),                       (M)

provided the low sector also has a lower energy scale comparable to lambda_c on the particular component being mixed. If x includes arbitrarily lower modes down to zero, replacing ||x|| by <x,Lx>^(1/2)/sqrt(lambda_c) is invalid. Thus (M) is proved for a **spectral shell/coarse-transition component** with c_- lambda_c <= L <= c0 lambda_c, not for the entire low sector including the vacuum/ultrasoft modes.

This qualification is load-bearing. The transition shell can satisfy it, but the full enlarged coarse sector from U019 also contains modes below c_- lambda_c. Those modes require separate treatment.

## 4. Ultrasoft-mode obstruction to the naive full-coarse estimate

For an eigenvector x with eigenvalue mu<<lambda_c, (C) gives a first term w^-1 sqrt(mu)||x|| and a second term w^-2||x||. Relative to sqrt(<x,Lx>)=sqrt(mu)||x||, the second term contributes

    1/(w^2 sqrt(mu)),

which worsens as mu->0. Therefore a uniform relative estimate normalized by the **actual** coarse energy cannot be obtained from (C) alone all the way to zero energy.

This is not surprising: spatial localization mixes an almost-constant mode through the curvature of chi even though its original Dirichlet energy is arbitrarily small. The exact vacuum is excluded in the centered Hilbert space, but finite boxes contain nonzero modes with eigenvalues O(n^-2), far below lambda_c=n^-q for q<1.

At q=1/2 and w~n^(1/4)log n, the smallest nonzero mu~n^-2 gives

    w^-2/sqrt(mu)
      ~ n^(1/2)/(log n)^2 * n

in unnormalized units if compared incorrectly; more directly the dimensionless ratio w^-2/mu is ~n^(3/2)/(log n)^2, huge. Thus the full-low-sector relative estimate fails by this route.

## 5. Correct structural interpretation

The logarithmic IMS gain is **proved for modes near the coarse/fine spectral interface**, exactly where smoothing creates overlap. It is not a uniform estimate for all coarse modes.

This suggests a multiscale shell decomposition rather than one giant coarse sector:

    lambda ~ lambda_0,
    lambda ~ lambda_1,
    ...,
    lambda ~ lambda_c,

with each shell localized on a width proportional to its own wavelength times log n. Then every shell has a relative O(1/log n) commutator at its own energy scale. The ultrasoft modes are not localized using the lambda_c collar; they receive larger collars appropriate to their wavelength or remain global coarse variables.

The number of logarithmic/dyadic shells between n^-2 and n^-q is O(log n). If each shell incurred O(1/log n) amplitude mixing independently, a crude sum could be O(1), so orthogonality/square-function structure is needed to retain a square-summable total. This is the next mathematical issue.

## 6. RG summability for a single shell

For geometric block sizes n_j~b^j,

    1/log n_j = O(1/j),

so a shellwise coefficient

    kappa_j=O(1/log n_j)

has

    sum_j kappa_j^2 < infinity.

Thus U019's desired mixing summability is achieved **for a fixed relative spectral shell** in the scalar model.

## 7. Outcome classification

Outcome: **proved after an explicit spectral-shell restriction**.

Proved:

- discrete commutator estimate (C);
- O(1/log n) relative mixing scale for vectors whose energies are comparable to lambda_c;
- square summability across geometric RG scales for that shell.

Refuted/blocked:

- using the same collar to obtain the relative estimate uniformly for the entire low sector down to the smallest nonzero eigenvalue.

Not proved:

- orthogonal aggregation over O(log n) spectral shells;
- transfer-deficit rather than scalar-Laplacian mixing;
- gauge-covariant/nonabelian version;
- reflection positivity, OS construction, or Yang–Mills mass gap.

## 8. Next bounded attempt

Build a dyadic spectral-shell partition between n^-2 and lambda_c and test whether the shellwise commutator estimates combine in l2 rather than l1. The target is a Littlewood–Paley/square-function inequality showing total squared relative leakage is controlled by O(1/log n) or O(1/log^2 n) after summing shells. If only an l1 sum is available, O(log n) shells erase the logarithmic gain and this multiscale localization architecture fails.
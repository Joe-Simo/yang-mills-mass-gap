# U021 — dyadic shell aggregation: orthogonality saves one logarithm, but not enough for RG summability

Date: 2026-09-14.

**We have not solved the Yang–Mills problem yet.**

This bounded attempt executes U020's dyadic-shell aggregation test in the scalar lattice model. Exact spectral orthogonality does improve the naive l1 accumulation, but with O(log n) shells and O(1/log n) leakage per shell it yields total squared leakage O(1/log n), not O(1/log^2 n). Along geometrically growing RG blocks n_j~b^j, this behaves like 1/j and is not summable. Therefore plain orthogonal square-function aggregation is **not sufficient** to close U019's infinite-scale mixing budget. A stronger per-shell decay or weighted shell estimate is required.

## 1. Dyadic shells

Let the nonzero scalar Laplacian spectrum between the box infrared scale n^-2 and the coarse/fine threshold lambda_c=n^-q, q<1, be decomposed into dyadic bands

    I_r = [2^r n^-2, 2^(r+1)n^-2]

until reaching lambda_c. The number J(n) of shells satisfies

    J(n) = Theta(log n),

more precisely

    J(n) ~ (2-q) log_2 n.

Wolfram 15.0.1 independently simplified this asymptotic shell count.

Let P_r be the exact spectral projection of L onto I_r. The P_r are mutually orthogonal and commute with L. Hence

    ||x||^2 = sum_r ||P_r x||^2,
    <x,Lx> = sum_r <P_r x,L P_r x>.

This is exact finite-dimensional spectral orthogonality; no harmonic-analysis theorem is needed for this part.

## 2. Shellwise U020 estimate

For shell r with characteristic energy lambda_r, choose its own localization width

    w_r = A lambda_r^-1/2 log n.

U020's commutator estimate gives a relative shell leakage coefficient

    kappa_r <= C/log n

with constants uniform in r, provided the spatial cutoff profile can be chosen with the stated width and remains geometrically admissible.

For the very lowest shells, w_r may approach or exceed the block size n. Those modes cannot be localized inside the block and must remain global coarse variables. This only reduces the number of localized shells; it does not worsen the negative conclusion below for the shells that are localized.

## 3. Best-case orthogonal aggregation

Suppose optimistically that cross-shell outputs are orthogonal enough that squared leakage adds:

    kappa_total^2 <= sum_r kappa_r^2.

With J=Theta(log n) and each kappa_r^2=O(1/log^2 n),

    kappa_total^2 = O(1/log n),
    kappa_total   = O(1/sqrt(log n)).                     (A)

Wolfram independently returned

    J/log^2 n ~ (2-q)/(log 2 * log n),

whereas the naive l1 amplitude sum is O(1).

Thus l2 aggregation **does** preserve a vanishing mixing coefficient, but only at square-root-log amplitude scale.

## 4. RG summability failure

For geometrically increasing block sizes n_j~b^j,

    log n_j = Theta(j).

Equation (A) gives

    kappa_j^2 = O(1/j).

The harmonic series diverges. Therefore the sufficient U003/U019 condition

    sum_j kappa_j^2 < infinity

is not established by shellwise O(1/log n) leakage plus unweighted l2 aggregation.

This corrects the optimistic possibility stated at the end of U020. Square-function structure alone saves one logarithm relative to l1, but one additional positive power/logarithm is still needed.

## 5. What strength would suffice?

If each shell obeyed

    kappa_r = O(1/log^(1+epsilon) n)

for any epsilon>0, then

    kappa_total^2
      = O(log n / log^(2+2epsilon)n)
      = O(1/log^(1+2epsilon)n).

Along n_j~b^j this is summable exactly when

    1+2epsilon > 1,

so every epsilon>0 suffices.

Alternatively, retain the O(1/log n) shell bound but prove shell weights decay with energy index, e.g.

    kappa_r <= C a_r/log n,
    sum_r a_r^2 <= C

uniformly in n. Then kappa_total^2=O(1/log^2 n), which is summable across RG scales.

The problem is therefore sharply quantified: we need either a tiny extra logarithmic gain per shell or a uniform l2 weight across shells.

## 6. Candidate source of an extra gain

U020 chose w_r exactly proportional to wavelength times log n. Increase the collar to

    w_r = lambda_r^-1/2 log^(1+epsilon)n.

Then the same commutator calculation gives

    kappa_r = O(1/log^(1+epsilon)n).

For all shells whose wavelength times this factor is o(n), localization remains possible. The lowest modes for which w_r>=n are left global coarse. Thus an extra logarithmic collar may solve the summability issue without changing the spectral algebra.

At the q=1/2 upper interface, the polynomial smoothing range is only

    R=O(lambda_c^-1/2 log n).

A collar with log^(1+epsilon)n is larger than R by log^epsilon n but remains o(n). This is geometrically compatible at the upper shells.

The tradeoff is that more ultrasoft shells become nonlocal/global coarse. We must count the dimension of those unlocalized modes and ensure it remains boundary-order or otherwise controllable.

## 7. Threshold for global ultrasoft modes

A shell can be localized only if

    lambda^-1/2 log^(1+epsilon)n << n,

or approximately

    lambda >> n^-2 log^(2+2epsilon)n.

Thus the unlocalized global sector consists of eigenvalues below

    lambda_global ~ n^-2 log^(2+2epsilon)n.

In four dimensions, the number of modes below lambda_global scales as

    n^4 lambda_global^2
      ~ log^(4+4epsilon)n.

This is merely polylogarithmic, dramatically smaller than the boundary-order n^3 coarse sector. The lattice-point counting can be made rigorous by the same sine/lattice-ball comparison as U013.

This is a promising correction: leave only polylogarithmically many ultrasoft modes global, and localize every higher coarse shell with the enlarged logarithmic collar.

## 8. Outcome classification

Outcome: **plain l2 aggregation insufficient; strengthened logarithmic collar yields a viable scaling candidate**.

Proved in the scalar spectral model:

- J=Theta(log n) dyadic shells;
- best-case unweighted l2 aggregation of O(1/log n) shell leakage gives kappa_total^2=O(1/log n);
- this is not summable over geometric RG scales.

Derived candidate correction:

- choose w_r=lambda_r^-1/2 log^(1+epsilon)n;
- then shell leakage is O(log^-(1+epsilon)n);
- l2 aggregate squared leakage is O(log^-(1+2epsilon)n), summable across RG scales for every epsilon>0;
- modes too soft to localize number only polylogarithmically in four dimensions.

The corrected aggregate estimate remains conditional on controlling cross-shell outputs in l2 after spatial localization and on treating the polylog global sector without hidden gap loss.

No Yang–Mills transfer estimate, nonabelian construction, reflection positivity, OS convergence, or mass gap is proved.

## 9. Next bounded attempt

Make the strengthened-collar scaling rigorous at the counting level and test the global ultrasoft sector. Prove N_global=O(log^(4+4epsilon)n) for the four-dimensional lattice box, then ask whether keeping those modes entirely global can be incorporated into the enlarged coarse Schur recurrence without accumulating a dimension-dependent loss. The smallest adversarial test is an abstract transfer deficit with a polylog-dimensional ultrasoft block whose minimum eigenvalue tends to zero: dimension control alone will not suffice, so an inheritance mechanism for these global modes must be identified.
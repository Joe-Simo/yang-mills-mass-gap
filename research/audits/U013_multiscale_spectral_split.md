# U013 — multiscale spectral split: exact exponent tradeoff

Date: 2026-09-14.

**We have not solved the Yang–Mills problem yet.**

This bounded research attempt executes U012's proposed spectral split. It makes the low-mode counting exponent rigorous up to constants for the scalar box model and identifies a nonempty parameter window where the fine inverse is sub-block local while the retained coarse sector is subextensive and even at most boundary-order. It does not prove U003 estimates for Yang–Mills.

## 1. Setup and target

Take the standard discrete Dirichlet Laplacian on a four-dimensional n-by-n-by-n-by-n box. Its eigenvalues are

    lambda(k)=4 sum_(mu=1)^4 sin^2[pi k_mu/(2(n+1))],
    1<=k_mu<=n.

Choose

    lambda_cut(n)=n^(-q),   0<q<1.

Retain all modes lambda<=lambda_cut as coarse. Approximate the inverse only on the fine spectrum lambda>=lambda_cut using the U012 Neumann polynomial.

Success criterion for this scaling attempt:

- fine approximation range R=o(n);
- coarse dimension=o(n^4);
- preferably coarse dimension no larger than boundary order O(n^3), giving a plausible block-interface interpretation.

## 2. Low-mode count

For 0<=x<=pi/2,

    (2/pi)x <= sin x <= x.

For low modes the eigenvalue condition is therefore comparable, with constants independent of n, to

    |k|^2 / n^2 <= C n^(-q).

Equivalently,

    |k| <= C' n^(1-q/2).

The number of integer 4-tuples in the positive orthant inside such a ball is bounded above and below by constant multiples of its four-dimensional volume once the radius tends to infinity. Since 0<q<1, the radius n^(1-q/2) does tend to infinity. Hence

    N_coarse(n;q) = Theta(n^(4-2q)).                     (C)

This is not merely heuristic Weyl notation; the exponent follows from elementary sine comparison and lattice-point volume comparison. Boundary conventions change constants, not this exponent.

Wolfram 15.0.1 independently simplified the exponent to 4-2q and the coarse fraction to n^(-2q).

## 3. Fine inverse range

On lambda>=n^-q, the Neumann residual obeys

    err_R <= exp[-c R n^-q]

for a fixed normalization constant c>0. To obtain polynomial error n^-p it suffices to take

    R = O(n^q log n).                                    (R)

Because q<1,

    R/n = O(n^(q-1) log n) -> 0.

Thus the fine inverse is genuinely sub-block local for every q in (0,1).

## 4. A useful window: q >= 1/2

By (C), the coarse dimension is at most boundary order n^3 exactly when

    4-2q <= 3,

that is

    q >= 1/2.

Therefore

    1/2 <= q < 1                                         (W)

is a nonempty scaling window with both:

- coarse sector dimension O(n^3) or smaller;
- fine inverse range o(n).

For q>1/2 the coarse dimension is strictly o(n^3). At q=1/2, N_coarse=Theta(n^3) and R=O(n^(1/2) log n). Near q=1, N_coarse is approximately n^2 while R approaches n^(1-epsilon) log n, so locality becomes weaker. This exposes a genuine tradeoff rather than a contradiction.

## 5. Why this is real progress but not a gap theorem

U012 showed that approximating the inverse uniformly down to lambda~n^-2 forces super-block range. U013 shows that removing the soft modes first eliminates that obstruction: there is a broad q-window where the retained low sector is only boundary-order/sub-boundary-order while the remaining inverse is sub-block local.

However, dimension alone does not control U003's coarse loss or mixing. The low modes are precisely long-wavelength modes, and a mass gap proof cannot simply assume they are harmless. A coarse sector with n^3 coordinates can still contain arbitrarily soft physical excitations. The next theorem must extract **energy/transfer information**, not just count them.

## 6. Candidate next discriminating estimate

For the fine approximation error choose p>0. If blocks have n(a)=a^-alpha, then

    err_fine <= n^-p = a^(alpha p).

Across geometric RG scales a_j, such errors can be summable if alpha p is positive and the scale ratio is fixed. This part can be made cheap by choosing polynomial accuracy p sufficiently large.

The hard term is coarse/fine coupling. A spectral projector would make the linearized quadratic form exactly block diagonal, but its projector is nonlocal. The approximate local split reintroduces coupling near the cutoff. The decisive quantity is therefore a commutator/localization estimate of the form

    || [chi_B, P_low] ||

or its quadratic-form analogue, where chi_B localizes to a block. If this boundary leakage scales like surface/volume and gains a power of n, it may fit U003's kappa_j budget. If it stays O(1), the route fails despite the favorable dimension count.

## 7. Outcome classification

Outcome: **proved as written for the scalar box scaling model**.

Established:

    N_coarse=Theta(n^(4-2q)),
    R=O(n^q log n),

and the simultaneous window 1/2<=q<1.

Not established:

- nonabelian background-uniform spectral decomposition;
- gauge-covariant finite-range implementation;
- reflection positivity of the split;
- U003 relative coarse-loss/mixing bounds;
- OS convergence or a physical mass gap.

## 8. Next bounded attempt

Analyze block-localization leakage of the low spectral projector. Start with the scalar periodic/Dirichlet model and estimate the kernel of P_{lambda<=n^-q}. Determine the scaling of the Hilbert-Schmidt/operator norm of [chi_B,P_low] for an interior block/collar. The route succeeds only if the leakage can be converted to a relative mixed-form coefficient kappa whose square is summable over RG scales. This is the first place where the favorable q-window can either become a usable multiscale mechanism or collapse.
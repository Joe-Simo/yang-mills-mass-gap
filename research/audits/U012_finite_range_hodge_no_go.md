# U012 — finite-range approximate Hodge projection: spectral locality obstruction

Date: 2026-09-14.

**We have not solved the Yang–Mills problem yet.**

This bounded Mathbox-style research attempt executes U011's proposed finite-range approximate Hodge route. Outcome: the simplest polynomial/heat-kernel approximations to the inverse lattice Laplacian cannot achieve polynomially small uniform error on all nonzero block modes while retaining range o(n). This is a no-go for that approximation architecture, not for every possible quasi-local decomposition.

## 1. Target contract

On an n-cell block, the transverse Hodge projection involves an inverse Laplacian on the nonzero spectrum. The first positive eigenvalue scales as

    lambda_min(n)=4 sin^2(pi/(2n)) ~ pi^2/n^2.

Seek an approximation to L^{-1} whose induced projection error is at most n^{-p}, p>0, while its spatial range R satisfies R=o(n), so that block events remain genuinely local compared with the block diameter.

Success: exhibit such an approximation with proved error/range bounds.
Failure for a candidate architecture: prove that the required R is at least order n (or worse).

## 2. Neumann-polynomial inverse

Normalize the scalar lattice Laplacian spectrum to [lambda_min,4] for the one-dimensional discriminating mode; higher-dimensional bounded-degree Laplacians change constants, not the small-eigenvalue mechanism. Consider

    q_R(x)=(1/4) sum_(j=0)^R (1-x/4)^j.

Then

    1-x q_R(x)=(1-x/4)^(R+1).

Because L is nearest-neighbor, q_R(L) has graph range at most R. The worst relative inverse residual occurs at lambda_min:

    err_R(n)=(1-lambda_min/4)^(R+1)
            = cos(pi/(2n))^(2(R+1)).

To demand err_R<=n^{-p}, one needs exactly

    R+1 >= p log n / [-2 log cos(pi/(2n))].

Since

    -2 log cos(pi/(2n)) ~ pi^2/(4n^2),

we obtain

    R >= (4p/pi^2) n^2 log n (1+o(1)).                 (N)

Wolfram 15.0.1 independently returned the same limit:

    R/(n^2 log n) -> 4p/pi^2.

Thus this finite-range Neumann architecture is dramatically nonlocal: the required polynomial degree/range exceeds the block diameter n by a factor of order n log n.

## 3. Heat-kernel representation has the same diffusive obstruction

The exact inverse on positive modes has

    L^{-1}=integral_0^infinity exp(-tL) dt.

Truncating at time T leaves relative residual exp(-T lambda). To make the worst-mode residual at most n^{-p} requires

    T >= p log n / lambda_min
      ~ (p/pi^2)n^2 log n.                               (H)

Wolfram independently returned T/(n^2 log n)->p/pi^2.

The heat kernel itself is not finite range. Its typical propagation distance at time T is diffusive, of order sqrt(T), hence approximately

    n sqrt(log n)

at the required T. Even before controlling rigorous off-diagonal tails, this exceeds the block diameter by sqrt(log n). A polynomial truncation of exp(-tL) that is strictly finite range inherits an additional degree/range burden.

The diffusive statement is used here as a structural interpretation; the rigorous no-go (N) applies to the explicit Neumann-polynomial architecture.

## 4. What this proves and what it does not

**Proved as written for the Neumann-polynomial candidate:** polynomially small uniform error on the entire positive spectrum requires R=Omega(n^2 log n), so R=o(n) is impossible.

**Conditional/structural for heat-kernel localization:** suppressing the softest n^-2 mode requires time Omega(n^2 log n), making sub-block localization implausible without a different mechanism. A full theorem about spatial heat-kernel truncation would need explicit off-diagonal estimates and is not claimed here.

**Not ruled out:**

- rational approximations implemented with auxiliary local fields;
- multigrid/wavelet decompositions that separate low modes rather than approximating L^{-1} uniformly;
- local gauges that avoid a global Hodge inverse;
- a finite-range decomposition of covariance/resolvent across scales;
- blockwise projections that place the dangerous low modes into the coarse sector instead of approximating them locally.

The last option directly addresses the obstruction: the modes causing (N) are precisely the wavelength-O(n) modes. They should probably be treated as coarse variables, not forced through a local inverse.

## 5. Research direction change

U011's proposal of a single finite-range approximate projector with uniformly small error is rejected in its simplest polynomial form. The evidence favors a **multiscale spectral split**:

1. put modes with lambda <= Lambda_R into an explicit coarse subspace;
2. approximate L^{-1} only on lambda >= Lambda_R, where the condition number is bounded by 1/Lambda_R;
3. choose Lambda_R so the resulting inverse approximation has range R=o(n);
4. feed the retained low modes into U003's coarse block rather than treating them as projection error.

For the Neumann polynomial, if lambda>=lambda_cut, residual is <=exp[-(R+1)lambda_cut/4]. Taking R~log n and a fixed lambda_cut gives polynomial error with logarithmic range. More generally R lambda_cut must dominate log n.

This converts the locality obstruction into a concrete coarse-mode-count problem: how many eigenmodes lie below lambda_cut, and can their transfer deficit be controlled without the dimension/entropy of the coarse sector exploding?

## 6. Next bounded attempt

Choose a cutoff lambda_cut(n)=n^{-q}. Then a Neumann approximation needs roughly

    R ~ n^q log n.

Locality R=o(n) requires q<1. In four dimensions the number of Laplacian modes below lambda_cut scales heuristically like n^4 lambda_cut^2 = n^(4-2q) by Weyl counting. The next attempt is to make this lattice counting exact enough for the box model and determine whether any 0<q<1 gives a useful balance between coarse-sector dimension and local inverse range. That spectral split is materially different from the failed uniform-projector route.

# U016 — correction: interior smooth spectral transitions require degree Omega(1/Delta lambda)

Date: 2026-09-14.

**We have not solved the Yang–Mills problem yet.**

Corrects the conditional degree assumption in U015. The hoped-for endpoint-Chebyshev scaling R~Delta lambda^-1/2 is not applicable to a transition centered at lambda_c=n^-q with transition width Delta lambda<=lambda_c and lambda_c tending to the spectral endpoint only on a scale much larger than the transition. A direct Bernstein-inequality argument gives the necessary degree R=Omega(Delta lambda^-1) in the interior angular regime relevant when s>=q. This narrows but does not eliminate the viable exponent window.

## 1. Why U015's square-root law was suspect

U015 treated spectral resolution as if the transition lived directly at the endpoint, where the Chebyshev coordinate lambda~theta^2 can indeed convert degree R angular resolution 1/R into endpoint lambda resolution 1/R^2.

But the proposed cutoff changes near

    lambda_c=n^-q

with width

    Delta=n^-s,   s>=q.

When s>q, Delta/lambda_c=n^{q-s}->0: the transition is narrow compared with its distance from the endpoint. Locally the Chebyshev angular map is approximately linear across that transition. Even at s=q the transition occupies a fixed fraction of lambda_c, and a uniform bounded polynomial must traverse an O(1) change over a lambda interval of order Delta.

Thus the endpoint R^-2 intuition cannot simply be applied to the transition width.

## 2. Bernstein lower bound

Map the fixed Laplacian spectral interval [0,lambda_max] affinely to x in [-1,1]. Let p_R be a degree-R polynomial intended to approximate a cutoff that changes from approximately 1 to approximately 0 across an x-interval of width delta comparable to Delta/lambda_max.

Assume |p_R|<=1+epsilon on [-1,1], with epsilon<1/2, and that across the transition its values differ by at least 1-2epsilon. By the mean value theorem, at some point xi in the transition,

    |p_R'(xi)| >= (1-2epsilon)/delta.

Bernstein's polynomial inequality gives

    |p_R'(xi)| <= R(1+epsilon)/sqrt(1-xi^2).

Therefore

    R >= [(1-2epsilon)/(1+epsilon)]
        sqrt(1-xi^2) / delta.                             (B)

For an interior transition whose mapped location stays away from +/-1 by more than its own width in the local angular sense, sqrt(1-xi^2) contributes the endpoint-distance factor. Near the lower endpoint corresponding to lambda_c, this factor is of order sqrt(lambda_c). Hence the sharper local lower bound is

    R = Omega( sqrt(lambda_c) / Delta )
      = Omega( n^(s-q/2) ).                              (D)

This is the correct interpolation between endpoint and interior behavior. A crude Markov inequality would only give R=Omega(Delta^-1/2); Bernstein retains the location information and is stronger here.

Wolfram 15.0.1 independently simplified the abstract Bernstein lower bound to

    R >= (1-2epsilon)sqrt(1-x0^2)/[(1+epsilon) delta]

for a transition centered at x0.

## 3. Corrected locality condition

A matching Chebyshev construction is expected to require the same resolution exponent, up to logarithms for error:

    R ~ n^(s-q/2) log n.                                 (A)

This upper bound still requires an explicit construction/source check and is not claimed proved here. But (D) is a necessary lower bound, so U015's smaller exponent s/2 cannot be generally correct when s>q.

Sub-block locality R=o(n) under (A) requires

    s - q/2 < 1,

or

    s < 1 + q/2.                                         (L)

The transition-count condition from U015 remains

    s >= q.                                               (C)

For every q<1, the interval

    q <= s < 1+q/2                                       (W)

is nonempty. Intersecting with U013's boundary-order choice 1/2<=q<1 still leaves a broad window.

## 4. Balanced choice s=q survives

If s=q, then

    R ~ n^(q/2) log n,

exactly the exponent U015 quoted for its balanced example. Thus the attractive point q=s=1/2 survives:

    N_coarse ~ N_transition ~ n^3,
    R ~ n^(1/4) log n,
    R/n ~ n^(-3/4) log n.

The correction matters primarily for choosing transition widths much narrower than lambda_c. There is no reason at this stage to do that; s=q is both spectrally natural and more local.

## 5. Evidence classification

**Proved:** the Bernstein necessary degree bound (B), and its scaling lower bound R=Omega(n^(s-q/2)) for the stated mapped transition geometry.

**Corrected:** U015's general conditional law R~n^(s/2)log n is not justified and is too optimistic for s>q.

**Still conditional:** a matching polynomial upper construction R=O(n^(s-q/2) log n) for an explicit smooth cutoff with polynomially small uniform error.

**Survives:** the balanced s=q scaling candidate, including q=s=1/2.

No Yang–Mills mass gap or U003 mixing estimate is proved.

## 6. Next bounded attempt

Construct the upper bound explicitly in the balanced case Delta=lambda_c. Work in Chebyshev angular coordinate. Choose a fixed smooth profile in the rescaled variable lambda/lambda_c and estimate its Chebyshev coefficients after composition with the affine spectral map. The target is a degree

    R=O(lambda_c^-1/2 log n)=O(n^(q/2)log n)

for uniform error n^-p. If an explicit analytic profile cannot achieve this because its complex singularities approach the interval faster than sqrt(lambda_c), quantify the true rate and revise the route again. This is now the cheapest decisive approximation check.
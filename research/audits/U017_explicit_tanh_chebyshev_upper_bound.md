# U017 — explicit tanh window closes the balanced Chebyshev degree estimate

Date: 2026-09-14.

**We have not solved the Yang–Mills problem yet.**

This bounded research attempt executes U016's cheapest decisive check. In the scalar lattice-box model, for the balanced transition width Delta lambda comparable to the cutoff lambda_c, an explicit analytic tanh window admits a polynomial approximation of degree

    R = O(lambda_c^(-1/2) log(1/epsilon))

up to the expected additional logarithm from the shrinking Bernstein-ellipse prefactor. For lambda_c=n^(-q) and target error n^(-p), this gives

    R = O(n^(q/2) log n).

Thus the balanced scaling candidate q=s survives with a proved upper construction in this auxiliary model. This does not yet establish the U003 relative mixing estimate or the nonlinear Yang–Mills theorem.

## 1. Explicit smooth window

Fix a spectral interval [0,Lambda] with Lambda>0 independent of n, and a fixed width parameter gamma>0. For 0<lambda_c<<Lambda define

    f_c(lambda)
      = 1/2 [1 - tanh((lambda-lambda_c)/(gamma lambda_c))].

The transition occurs on spectral width O(lambda_c). The function is bounded and smooth on the real spectral interval. It need not equal exactly 1 or 0 outside the transition; fixed gamma can make the real plateaux as sharp as desired at fixed multiples of lambda_c. The approximation theorem below concerns f_c itself.

Map lambda in [0,Lambda] to x in [-1,1] by

    x = 2 lambda/Lambda - 1,
    lambda = (Lambda/2)(x+1).

Let F_c(x)=f_c(lambda(x)).

## 2. Complex singularities and the Chebyshev angular distance

The poles of tanh z are

    z = i pi(k+1/2),  k in Z.

Hence the nearest singularities of f_c occur at

    lambda_* = lambda_c +/- i (pi gamma/2) lambda_c.

Their mapped x-locations are

    x_* = -1 + (2 lambda_c/Lambda)
                +/- i (pi gamma lambda_c/Lambda).

Write lambda_c=t^2. Near the lower Chebyshev endpoint x=-1, use x=cos theta. The standard local expansion

    arccos(-1+z) = pi - sqrt(2z) + O(z^(3/2))

for a fixed branch gives

    theta_* = pi - sqrt[2(2+i pi gamma)/Lambda] t + O(t^3)

for the upper singularity. Therefore

    |Im theta_*| = c_gamma,Lambda sqrt(lambda_c)
                   + O(lambda_c^(3/2)),

where

    c_gamma,Lambda
      = sqrt[(sqrt(4+pi^2 gamma^2)-2)/Lambda] > 0.

Wolfram 15.0.1 independently simplified the imaginary-part coefficient to exactly this constant.

Consequently, for all sufficiently small lambda_c there is a fixed a>0 such that F_c(cos theta) is analytic in the strip

    |Im theta| < a sqrt(lambda_c).

Equivalently F_c is analytic in every Bernstein ellipse E_rho with

    log rho <= a sqrt(lambda_c).

Choose, for definiteness,

    rho_c = exp[(a/2) sqrt(lambda_c)].

This ellipse remains a fixed fraction of the angular distance from the nearest pole.

## 3. Uniform bound on the chosen ellipse

Inside a strip staying a fixed fraction away from the tanh poles, tanh is uniformly bounded. More explicitly, if z=u+iv and |v|<=pi/4 then

    |tanh z|^2
      = [cosh(2u)-cos(2v)]/[cosh(2u)+cos(2v)]

and the denominator stays positive; on any stricter strip |v|<=pi/4-delta the modulus is bounded by a constant depending only on delta. Because rho_c was chosen at a fixed fraction of the nearest singularity distance, the tanh argument of points in E_rho_c stays in such a fixed pole-free strip after shrinking a if needed.

Therefore there is M<infinity independent of lambda_c such that

    sup_(z in E_rho_c) |F_c(z)| <= M.                    (M)

The constant depends on gamma,Lambda and the chosen fractional safety margin, not on n.

## 4. Self-contained Chebyshev truncation bound

If a function F is analytic in E_rho and |F|<=M there, its Chebyshev coefficients obey

    |a_k| <= 2 M rho^(-k).

A short derivation: set x=(w+w^(-1))/2. Then F((w+w^(-1))/2) is analytic in the annulus rho^(-1)<|w|<rho. Its Laurent coefficients are bounded by Cauchy's estimate on |w|=rho; pairing the +/-k coefficients gives the displayed Chebyshev bound.

Hence the degree-R Chebyshev truncation p_R satisfies

    ||F-p_R||_infinity
      <= 2M sum_(k>R) rho^(-k)
      <= [2M/(rho-1)] rho^(-R).                          (E)

Apply this with rho=rho_c. Since

    rho_c-1 ~ (a/2) sqrt(lambda_c),
    log rho_c = (a/2) sqrt(lambda_c),

we obtain

    ||F_c-p_R||_infinity
      <= C lambda_c^(-1/2)
           exp[-c R sqrt(lambda_c)]                      (A)

for constants C,c>0 independent of lambda_c.

## 5. Degree for polynomially small error

Set lambda_c=n^(-q), q>0, and require error <=n^(-p). From (A), it is sufficient that

    c R n^(-q/2)
      >= (p+q/2) log n + log C.

Thus

    R >= C_(p,q,gamma,Lambda) n^(q/2) log n             (D)

suffices. Since U016 already gave the Bernstein necessary lower scaling

    R = Omega(lambda_c^(-1/2))

for balanced width Delta~lambda_c, the construction is optimal in the power of n, with only the logarithmic factor needed for polynomially small uniform error.

## 6. Finite-range operator consequence

For a nearest-neighbor lattice Laplacian L_lat, a degree-R polynomial p_R(L_lat) has graph range at most R. Therefore at the balanced choice q=s,

    range = O(n^(q/2) log n).

For every q<2 this is o(n); in the U013 boundary-order window 1/2<=q<1 it is strongly sub-block local.

At the particularly simple point q=1/2,

    lambda_c=n^(-1/2),
    N_coarse=Theta(n^3),
    N_transition=Theta(n^3),
    R=O(n^(1/4) log n),
    R/n=O(n^(-3/4) log n).

Thus the locality/counting part of the smooth spectral split is now supported by an explicit approximation construction rather than a heuristic degree law.

## 7. What is and is not proved

**Proved in the scalar fixed-spectral-interval model:**

- explicit tanh window with nearest singularity angular distance Theta(sqrt(lambda_c));
- uniform analyticity in a Bernstein ellipse with log rho=Theta(sqrt(lambda_c));
- Chebyshev truncation error

      <= C lambda_c^(-1/2) exp[-c R sqrt(lambda_c)];

- polynomial error n^-p with degree O(n^(q/2)log n) for lambda_c=n^-q;
- finite graph range of the polynomial functional calculus.

**Not proved:**

- that this scalar cutoff lifts gauge-covariantly around arbitrary nonabelian Yang–Mills backgrounds;
- that the resulting coarse/fine decomposition preserves reflection positivity;
- the U003 relative mixing estimate kappa_j^2 <= C R_j/n_j + ...;
- control of the retained long-wavelength coarse modes;
- OS convergence or a physical Yang–Mills mass gap.

## 8. Research-state consequence

U015's balanced q=s scaling is promoted from a conditional polynomial-degree heuristic to a proved auxiliary approximation statement. U016's correction remains important for narrower transitions s>q; U017 only closes the balanced case Delta~lambda_c.

The first unresolved implication has now moved forward: **does the finite-range smooth split produce a small relative coarse/fine quadratic-form coupling?** Counting the collar fraction R/n is not enough by itself.

## 9. Next bounded attempt

Attack an IMS-type relative mixing estimate in the scalar quadratic model. Let P_R=p_R(L_lat) be the finite-range smooth low-pass operator and Q_R=I-P_R. For a spatial block cutoff chi with a collar wider than R, estimate cross terms generated by localization and by the imperfect idempotence P_R^2-P_R. The target form is

    |<u, G_mix v>|
      <= kappa [<u,G_c u><v,G_f v>]^(1/2)

with

    kappa^2 <= C(R/n) + C||P_R^2-P_R|| + C err^2.

The cheapest falsification test is a normalized low-frequency state concentrated in the collar. If such a state keeps the relative cross term O(1), the collar-volume heuristic fails and a different coarse variable construction is required.
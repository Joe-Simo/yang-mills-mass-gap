# U019 — enlarged-coarse Schur certificate after explicit transition absorption

Date: 2026-09-14.

**We have not solved the Yang–Mills problem yet.**

This bounded attempt executes U018's operator-theoretic correction. The transition band is absorbed completely into the coarse sector, so no approximate-idempotence defect appears. The resulting gap certificate is exactly a two-block Schur-complement statement between the enlarged coarse sector and the genuinely high-energy fine sector. The theorem clarifies which mixing estimate is actually required and shows that O(1) mixing is not automatically fatal if the fine coercivity is parametrically stronger than the coarse target; however, if coarse and fine coercivities are comparable, the relative mixing coefficient must tend to zero for asymptotically lossless transport.

## 1. Enlarged decomposition

Let G=I-S be a bounded positive transfer-deficit operator on the centered Hilbert space. After the smooth spectral construction, define

    H = H_C direct-sum H_F,

where H_C contains **all** low and transition modes and H_F contains only modes safely above the smooth transition. This is an abstract orthogonal decomposition for the certificate; constructing it gauge-covariantly and locally in Yang–Mills remains separate.

Write

    G = [[A,B],[B*,D]].

There is no P^2-P term: transition modes are not treated as projection error.

## 2. Exact Schur certificate

For any delta with 0<delta<inf spec(D), completing the square gives

    G>=delta I

if and only if

    A-delta I - B(D-delta I)^(-1)B* >= 0.               (S)

This is the same exact algebraic mechanism proved in U003, now applied to the enlarged coarse sector. Thus a sufficient scalar condition is

    A>=a I,
    D>=d I,
    ||B||<=b,

with 0<delta<min(a,d) and

    (a-delta)(d-delta) >= b^2.                           (C)

For the 2x2 scalar model the exact smallest eigenvalue is

    delta_exact = [a+d-sqrt((a-d)^2+4b^2)]/2.

Wolfram 15.0.1 independently returned this formula and the same Schur condition.

## 3. Relative mixing formulation

Assume the form bound

    |<x,B y>| <= kappa sqrt(<x,A x><y,D y>),
    0<=kappa<1.

In the scalar extremal model b=kappa sqrt(a d), so

    delta_exact(a,d,kappa)
      = [a+d-sqrt((a-d)^2+4ad kappa^2)]/2.               (E)

This formula exposes two regimes.

### Comparable coercivities

If d=a, then

    delta_exact=a(1-kappa).

So an O(1) kappa<1 still leaves a positive gap, but every RG step loses a fixed fraction. Repeating infinitely many such steps drives a multiplicative transport bound to zero unless the cumulative loss is summable. For U003-style asymptotic transport one therefore needs kappa_j->0 sufficiently fast (or a different nonmultiplicative renormalization argument).

### Strong fine coercivity

If d>>a, expand (E):

    delta_exact = a(1-kappa^2) + O(a^2/d)

for fixed kappa. Thus the fine sector can absorb an O(1) relative coupling while the coarse loss is only the factor 1-kappa^2. This is still a fixed loss if kappa is fixed; summable transport again requires either kappa_j^2 summable or a mechanism that resets/improves the coarse reference rather than multiplying the same loss indefinitely.

Therefore absorbing the transition sector removes the false idempotence obstruction but does **not** remove the need for quantitative decay of the coarse/fine coupling across infinitely many RG scales.

## 4. Improved recurrence allowing scale-dependent fine coercivity

Suppose at RG step j the enlarged coarse block obeys

    A_j >= (1-eta_j) d_(j-1) I,

and the fine block obeys

    D_j >= rho_j I.

Let the mixed form coefficient be kappa_j. The exact scalar lower envelope from (E) gives the valid bound

    d_j >= F(a_j,rho_j,kappa_j),

where

    a_j=(1-eta_j)d_(j-1),

and

    F(a,rho,kappa)
      = [a+rho-sqrt((a-rho)^2+4a rho kappa^2)]/2.         (R)

This recurrence is sharper than U003's universal reserve-half estimate. It should be used for future quantitative tests because it retains the actual fine/coarse ratio.

For rho>>a,

    F/a = 1-kappa^2+O(a/rho).

Hence a sufficient asymptotic condition for a positive infinite product is schematically

    sum_j [eta_j + kappa_j^2 + a_j/rho_j] < infinity,     (A)

with the last term recording finite fine/coarse separation. A rigorous product theorem can be obtained by bounding the Taylor remainder once rho_j/a_j is uniformly large. The exact recurrence (R), rather than this schematic expansion, is the durable statement.

## 5. Consequence for the q=1/2 smooth split

At q=1/2, enlarged coarse dimension remains Theta(n^3) after transition absorption, while the finite-range smoothing scale is

    R=O(n^(1/4) log n).

The certificate does not care about that dimension directly. It asks for three quantitative facts in the **actual transfer deficit**:

1. coarse inheritance: eta_j summable;
2. fine coercivity rho_j bounded away from the transported coarse edge, preferably rho_j/d_(j-1)->infinity or at least uniformly >1;
3. relative mixed coefficient kappa_j with square-summable effective loss.

Thus the next Yang–Mills/scalar localization test is correctly focused on kappa_j, not on P^2-P.

## 6. Cheapest adversarial test for collar-volume mixing

The tempting estimate remains

    kappa_j^2 ?<= C R_j/n_j.

But this cannot follow from collar volume for arbitrary vectors: choose normalized x and y supported entirely inside the collar. Their L2 mass fraction there is one, not R/n. Any proof of a relative form gain must use **spectral restrictions/coercivity**, not raw spatial measure.

The enlarged coarse sector includes modes lambda<=O(lambda_c); those vectors obey a low-energy gradient bound. The fine sector starts above a separated multiple of lambda_c. A promising scalar inequality is therefore an IMS/commutator estimate involving a slowly varying spatial cutoff chi with gradient scale 1/w:

    ||[L,chi]x|| controlled by w^-1 sqrt(<x,Lx>) + w^-2||x||.

Choose collar width w larger than the polynomial range R but smaller than n. The low-energy scale lambda_c^-1/2=n^(q/2) and R=n^(q/2)log n differ only logarithmically, so w must be at least R. This makes w^-1/sqrt(lambda_c) approximately 1/log n if w~R, suggesting a possible logarithmic small parameter rather than R/n.

This observation materially changes the next target: the natural mixing decay may be

    kappa = O(1/log n)

rather than sqrt(R/n). Its square is still summable over **geometrically growing n_j** because 1/(log n_j)^2 behaves like 1/j^2. Therefore a logarithmic gain would be enough for U003/U019 transport.

## 7. Outcome classification

Outcome: **proved operator-theoretic certificate; new viable logarithmic target identified**.

Proved:

- transition absorption eliminates the approximate-idempotence term entirely;
- exact Schur recurrence (R);
- fixed O(1) relative mixing produces fixed multiplicative loss and is not enough for infinite-scale transport;
- collar-volume counting alone cannot bound arbitrary-vector relative mixing.

Promising but unproved:

- an IMS spectral estimate yielding kappa=O(1/log n) when w~R~lambda_c^-1/2 log n.

Not proved:

- that the actual Yang–Mills transfer deficit has the scalar spectral structure assumed here;
- coarse inheritance/fine coercivity/mixing bounds;
- reflection positivity, OS construction, or mass gap.

## 8. Next bounded attempt

Prove or refute the logarithmic IMS mixing estimate in the scalar lattice model. Use a Lipschitz cutoff chi varying across width w=C lambda_c^-1/2 log n. For x spectrally below c lambda_c and y spectrally above C lambda_c, derive an explicit bound on cross terms created by spatial localization. The target is kappa<=C'/log n (or better). Since n_j grows geometrically, this would make sum kappa_j^2 finite and would close the **mixing** obligation of the auxiliary scalar gap-transport model. A counterexample with O(1) relative coupling would reject this localization mechanism.
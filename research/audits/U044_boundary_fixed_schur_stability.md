# U044 — boundary-fixed curved Schur stability and a finite interior soft package

Date: 2026-09-16. Base: private `Joe-Simo/yang-mills-mass-gap` commit `5f947b893b361a597a86d586460d16f2300cd289` (U043).

**We have not solved the Yang–Mills problem yet.**

Evidence: self-reviewed finite-regulator quadratic/Hessian theorem on a periodic SU(2) phase-cell slab, exact mode decomposition, finite exact audits, and symbolic corroboration. No nonlinear functional-integral determinant estimate, no full transfer-RG step, no continuum construction, and no physical mass-gap theorem.

## 1. Target and outcome

U043 closed the curved **bulk horizontal** coercivity estimate but left the boundary-fixed Schur/Steklov comparison unresolved. The obstruction was structural: the interior gauge group must be fixed without changing either boundary face, while the surface-sized boundary gauge representation channels must remain available for gluing.

This unit solves the quadratic part of that problem in the periodic phase-cell slab of U042. The result is deliberately phrased as conditional high-mode elimination, not as a completed quantum integration.

The main statements are:

1. gauge transformations that are identity on both boundary faces have a Dirichlet gauge gap `~1/ell`, so the flat boundary-fixed Coulomb slice remains transverse to the curved gauge orbits when `delta ell` is small;
2. after removing those interior gauge directions, only a **bounded** package of near-harmonic longitudinal/normal modes can have interior Hessian stiffness below `c/ell^2`;
3. the remaining interior Hessian block has a uniform lower bound `m_ell >= c/ell^2`;
4. a local Wilson-Hessian perturbation of size `O(delta)` therefore changes the boundary/retained Schur complement by only `O(delta ell^2)` in operator norm;
5. on every flat coexact boundary mode with Steklov stiffness at least `C/ell`, the relative Schur error is only `O(delta ell^3)`;
6. U041's optimized scales give

       delta ell^2 = O(alpha^(3/26)) -> 0,
       delta ell^3 = O(alpha^(1/26)) -> 0.

Thus the flat U042 high-boundary sector survives the curved small-field perturbation at the **quadratic Schur-complement level**, while all boundary gauge channels and the bounded soft physical package are retained.

The first new obstruction appears one level later: a Gaussian determinant has rank `O(ell^4)`, so operator-norm smallness alone does not control the boundary-dependent log determinant. That determinant/locality problem, together with nonlinear remainders, is now the first missing integration step.

## 2. Geometry and flat commuting reference

Use U042's slab

    Lambda_ell = {0,1,...,ell} x (Z/ell Z)^3,                (1)

with two boundary faces `r=0` and `r=ell`. Tangential links on both faces are retained boundary variables. All normal links and tangential links at `1<=r<=ell-1` are interior variables.

Let the reference connection be an arbitrary flat commuting SU(2) background

    Ubar_0=I,
    Ubar_j=exp[i h_j sigma_3/ell],  j=1,2,3,                 (2)

with the holonomy representatives chosen as in U042. Complexify adjoint color into weights `w=0,+1,-1`. At tangential Fourier label `n`, write

    lambda=lambda_w(n)
      =4 sum_(j=1)^3 sin^2([pi n_j+w h_j]/ell).              (3)

The flat Wilson Hessian is the covariant Maxwell form

    Qbar(a)=||D_Ubar a||_2^2.                                (4)

No boundary gauge transformation is fixed or projected to a singlet in (1)-(4).

## 3. Boundary-fixed interior gauge group and its Dirichlet gap

Let an infinitesimal interior gauge parameter `phi(r,x)` obey

    phi(0,x)=phi(ell,x)=0.                                    (5)

Its flat covariant gauge map is `Gbar_D phi=D_Ubar phi`. For one Fourier/color mode, the normal Dirichlet profile has eigenvalues

    nu_D(k)=4 sin^2[pi k/(2ell)],  k=1,...,ell-1.            (6)

Tangential covariant momentum contributes the nonnegative `lambda`, so the smallest singular value of `Gbar_D` satisfies

    sigma_D >= 2 sin[pi/(2ell)] >= 2/ell.                    (7)

Now let `U` be a curved connection in the same fixed link chart, with

    max_e dist(U_e,Ubar_e) <= delta.                          (8)

Exactly as in U043, locality of the adjoint action gives

    ||G_U^D-Gbar_D|| <= 4 delta.                              (9)

Hence when `4 delta < sigma_D`, the curved interior gauge map is injective on the same Dirichlet parameter space and the flat Coulomb slice

    Kbar_D=(ran Gbar_D)^perp                                  (10)

remains transverse to the curved interior gauge orbits. The angle defect is `O(delta ell)`. Importantly, every gauge transformation in (5) is the identity on both boundary faces, so using (10) does **not change the retained boundary links or their representation data**.

On U041's optimized scales,

    delta ell = O(alpha^(5/26)) -> 0.                        (11)

Thus the boundary-fixed slice itself has no scaling obstruction.

## 4. Exact flat interior spectrum after Dirichlet gauge separation

Fix a Fourier/color mode and rotate its tangential symbol to a real magnitude

    s=sqrt(lambda).                                          (12)

The flat interior physical modes split into two kinds.

### 4.1 Tangential transverse modes

There are two tangential polarizations orthogonal to the covariant momentum. Their endpoint tangential values belong to the retained boundary variables, so an interior variation has zero endpoint values. The normal profile therefore has the Dirichlet spectrum

    lambda + 4 sin^2[pi k/(2ell)],
    k=1,...,ell-1.                                           (13)

Every such eigenvalue is at least `4/ell^2`.

### 4.2 Longitudinal-normal physical mode

Write the tangential longitudinal variables as `a_1,...,a_(ell-1)` and the normal-edge variables as `c_0,...,c_(ell-1)`, with `a_0=a_ell=0`. Flat Dirichlet-Coulomb horizontality is

    s a_r + c_(r-1)-c_r=0,  r=1,...,ell-1.                  (14)

The normal-tangential curl is

    f_r=a_(r+1)-a_r-s c_r.                                   (15)

The divergence-free subspace has dimension `ell`. Directly, it is the image of the adjoint of (15), and the induced generalized eigenvalue problem is exactly the path-Neumann operator shifted by `lambda`. Therefore its complete spectrum is

    lambda + 4 sin^2[pi k/(2ell)],
    k=0,...,ell-1.                                           (16)

The checker verifies the exact characteristic polynomial identity behind (16) for `ell=2,...,6`; the all-ell proof is the one-dimensional incidence identity `C_I C_I^*=L_N+lambda I`.

The `k=0` mode has eigenvalue exactly `lambda`. At `lambda=0` it is the constant normal holonomy/relative-face gauge mode. It is **not** to be integrated as a uniformly stiff variable.

## 5. A bounded interior soft package

Fix a numerical threshold `Lambda_*>0`. Call a tangential Fourier/color mode soft when

    lambda_w(n) <= Lambda_*/ell^2.                            (17)

For each such mode retain the one longitudinal-normal `k=0` mode from (16). All boundary gauge-gradient channels remain retained separately, as do U042's bounded coexact/harmonic boundary-soft modes.

The number of tangential labels satisfying (17) is bounded independently of `ell` and of the flat commuting holonomy. Indeed U042's distance estimate gives

    lambda_w(n)
      >= 16/(pi^2 ell^2) sum_j d_j^2,                        (18)

so (17) implies

    sum_j d_j^2 <= pi^2 Lambda_*/16.                          (19)

After choosing `|h_j|<=pi/2`, each wrapped integer coordinate obeys the crude bound

    |m_j| <= sqrt(Lambda_*)/4 + 1/2.                         (20)

Thus a uniform finite overcount per adjoint weight is

    N_*(Lambda_*)
      =[2 ceil(sqrt(Lambda_*)/4+1/2)+1]^3.                  (21)

Only one interior `k=0` longitudinal-normal mode is retained for each such tangential label. Consequently the **physical interior soft package has bounded dimension per phase cell**. This count excludes the surface-sized boundary gauge-gradient representation channels, which are retained algebraically rather than relabeled as physical soft modes.

## 6. Uniform `ell^-2` gap on the high interior block

Let `H_hi` be the flat Dirichlet-Coulomb interior space after removing exactly the soft `k=0` modes described in Section 5.

For a tangentially soft label, every remaining normal excitation has `k>=1`, hence by (13),(16) has eigenvalue at least `4/ell^2`. For a tangentially nonsoft label, even the `k=0` longitudinal-normal mode has eigenvalue greater than `Lambda_*/ell^2`.

Therefore

    Dbar := Qbar|_(H_hi)
      >= m_ell I,

    m_ell = c_*/ell^2,
    c_* = min(4,Lambda_*).                                   (22)

This is a complete flat high-interior spectral bound, not a fitted finite-size observation.

## 7. Curved Wilson Hessian keeps the high block invertible

On a fixed small link chart, the four-link Wilson plaquette Hessian is Lipschitz. Since each four-dimensional link belongs to at most six plaquettes, there is a universal finite `K_H` such that

    ||H_U-H_Ubar|| <= e,
    e=K_H delta,                                             (23)

in link `L2` operator norm, independently of `ell` and of the enclosing lattice volume.

Let `D_U` be the compression of `H_U` to the **same fixed flat high subspace** `H_hi`. From (22)-(23),

    D_U >= (m_ell-e)I.                                       (24)

Put

    eta = e/m_ell.                                           (25)

If `eta<=1/2`, then

    D_U >= m_ell I/2,
    ||D_U^(-1)|| <= 2/m_ell = O(ell^2).                      (26)

On U041's optimized scales,

    eta = O(delta ell^2)
        = O(alpha^(3/26)) -> 0.                              (27)

Thus the complete high interior block is perturbatively integrable at the Hessian level while all gauge and physical soft data remain outside it.

## 8. Schur-complement perturbation without an `ell^4` loss

Split the flat Hessian according to retained variables `R` and high interior variables `H_hi`:

    Hbar = [[A,C],[C*,Dbar]],                                 (28)

where `R` contains the two boundary faces, all boundary gauge representation variables, and the bounded interior soft package. Let

    H_U = Hbar + E
        = [[A+E_A, C+E_C], [C*+E_C*, Dbar+E_D]],             (29)

with `||E||<=e`.

The flat Maxwell Hessian is positive semidefinite. Moreover the four-dimensional incidence bound gives

    ||Hbar||=||D_Ubar||^2 <= 24,                              (30)

because each plaquette has four links and each link belongs to at most six plaquettes. Hence

    a:=||A|| <=24.                                           (31)

Flat positivity also gives the standard Schur inequality

    C Dbar^(-1) C* <= A,

so

    ||C Dbar^(-1/2)|| <= sqrt(a).                            (32)

This is what prevents the naive resolvent estimate from losing `ell^4`.

Define the flat and curved retained Schur complements

    Sbar=A-C Dbar^(-1) C*,

    S_U=A+E_A-(C+E_C)D_U^(-1)(C+E_C)*.                       (33)

Write

    F=Dbar^(-1/2) E_D Dbar^(-1/2),

so `||F||<=eta` and

    D_U^(-1)
      =Dbar^(-1/2)(I+F)^(-1)Dbar^(-1/2).                    (34)

Using (32), `||(I+F)^(-1)||<=1/(1-eta)`, and

    ||(I+F)^(-1)-I||<=eta/(1-eta),                           (35)

one obtains the explicit operator bound

    ||S_U-Sbar|| <= Theta(e,m_ell,a),                         (36)

where

    Theta(e,m,a)
      = e + [ a(e/m)
              +2 sqrt(a)e/sqrt(m)
              +e^2/m ]/[1-e/m].                             (37)

For fixed `Lambda_*` and `eta<=1/2`, (22),(31),(37) imply

    ||S_U-Sbar|| <= C_S delta ell^2                          (38)

with a finite constant `C_S` independent of `ell`, the number of phase cells, and the exterior lattice volume.

Equation (38) is the main boundary-fixed quadratic result of this checkpoint.

## 9. Relative stability of U042's flat stiff boundary sector

Take a flat coexact boundary vector `y` in a U042 Steklov sector satisfying

    <y,Sbar y> >= (C_B/ell)||y||^2,                          (39)

with fixed `C_B>0`. Set the retained interior soft coordinates to zero when evaluating this conditional boundary block; the flat Hodge split makes them orthogonal to the coexact boundary minimizer.

Equations (38)-(39) give

    |<y,(S_U-Sbar)y>|
      <= (C_S/C_B) delta ell^3 <y,Sbar y>.                   (40)

Under the optimized U041 scales,

    delta ell^3
      = O(alpha^(7/26-6/26))
      = O(alpha^(1/26)) -> 0.                               (41)

Therefore every flat boundary mode with stiffness `>=C_B/ell` remains stiff under the curved perturbation, with relative error tending to zero. U042's exact boundary gauge-gradient kernel and its bounded `O(1/ell)` coexact/cycle sector are **not integrated by this statement**; they remain part of `R`.

This is precisely the safe alternative to assigning a false mass to gauge or collective boundary variables.

## 10. What has and has not been integrated

At quadratic order, U044 supplies the missing boundary-fixed high-mode mechanism:

* interior gauge transformations vanish on the boundary faces;
* their flat Coulomb slice stays transverse to curved gauge orbits;
* all potentially sub-`ell^-2` physical interior modes form a bounded package;
* the remaining high interior Hessian has inverse norm `O(ell^2)`;
* eliminating it changes the retained boundary/soft Hessian by only `O(delta ell^2)`;
* on the flat `1/ell`-stiff boundary sector the relative change is `O(delta ell^3)=o(1)`.

This is **not yet a nonlinear functional integral**. Two important pieces remain.

First, a Gaussian determinant involves `O(ell^4)` high variables. The crude estimate

    |log det(I+F)| <= rank(F) O(||F||)                       (42)

would cost `O(ell^4 delta ell^2)=O(delta ell^6)`, which is not small on the optimized scale. Boundary-independent determinant pieces may normalize away and locality should improve the boundary-dependent part, but (38) alone does not prove that cancellation.

Second, cubic and higher Wilson remainders must be controlled under the same retained/high split. A positive Hessian does not itself justify replacing the nonlinear core integral by its Gaussian Schur complement.

Thus no quantum transfer gap is claimed here.

## 11. Checks and self-audit

`checks/U044_boundary_fixed_schur_checks.py` contains ten focused checks.

They verify:

* the exact longitudinal-normal generalized characteristic polynomial (16) against a shifted path-Neumann Laplacian for `ell=2,...,6`;
* the exact `k=0` eigenvalue `lambda`;
* the elementary normal excitation bound `4 sin^2(pi/[2ell])>=4/ell^2` on a finite diagnostic range;
* the `ell`-independent tangential soft-count mechanism;
* an exact boundary-fixed gauge-transversality matrix fixture;
* exact rational Schur-complement algebra on a positive block matrix;
* the scaled resolvent identity (34);
* the exponents `3/26`, `1/26`, and `5/13`;
* the four-dimensional incidence norm bound `24`;
* an exact dyadic scaling fixture for `delta ell^2`, `delta ell^3`, and `delta^2 ell^2`.

All ten new checks pass. The full U043 suite is rerun as the nearest regression dependency. The universal results (6)-(41) are written proofs; the finite loops do not substitute for their quantifiers.

Primary self-audit verdict: **proved after the explicit finite-SU(2), periodic-slab, small-curved-background, quadratic-Hessian, boundary-fixed-interior-gauge restrictions.** The bounded soft-package count and Schur estimate are uniform in `ell` and exterior volume inside that contract. No determinant, nonlinear integration, continuum, or physical mass-gap statement follows.

No external theorem is load-bearing; the proof uses the explicit U042 Fourier/Hodge decomposition, U043's local Hessian perturbation mechanism, path incidence algebra, and elementary positive block-matrix identities.

## 12. Next executable target

Control the **boundary-dependent high-mode determinant and nonlinear remainder** without paying the full `O(ell^4)` rank:

1. differentiate the high-mode log determinant with respect to retained collar/boundary variables;
2. use locality plus the `O(ell^2)` high resolvent to show only a boundary layer contributes at leading order;
3. seek a surface-order or summable bound compatible with `ell=alpha^(-1/13)`;
4. combine it with the Schur estimate (38)-(41) and U039's bad-block transfer remainder.

Only after the determinant/remainder estimate is available should the high-mode elimination be inserted into the centered physical transfer recursion. A stable quadratic Schur complement is not the Yang-Mills mass gap.

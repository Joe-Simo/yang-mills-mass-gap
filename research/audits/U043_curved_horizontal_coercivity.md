# U043 — curved regular-core horizontal coercivity and an O(ell^2) trace bound

Date: 2026-09-16. Base: private `Joe-Simo/yang-mills-mass-gap` commit `fb1f9ef783591eb71a1bb235828b6327177f9691` (U042).

**We have not solved the Yang–Mills problem yet.**

Evidence: self-reviewed finite-regulator geometric/operator proof on one U041-regular SU(2) phase cell, exact tensor-spectrum derivation, deterministic finite audits, and symbolic corroboration. No independent expert/formal verification, boundary Schur-complement theorem, continuum construction, or physical mass-gap theorem.

## 1. Target and outcome

U042 proved the exact gauge-covariant Hodge/Steklov split around arbitrary **flat** commuting SU(2) holonomy, and isolated the missing implication: a curved regular-core trace/coercivity estimate that preserves the boundary gauge representation data.

This unit proves the coercive part of that implication directly on every sufficiently small U041-regular core. The key point is that one need not first construct a nonlinear Coulomb gauge. Instead, use the tangent space orthogonal to the **actual** gauge orbit and compare it with the flat Coulomb space.

The result is:

* actual-gauge-horizontal vectors have only `O(delta ell)` leakage into flat gradient directions;
* the exact open-cube transverse curl gap is `O(ell^-2)`;
* the Wilson Hessian differs from the identity-background Hessian by `O(delta)` in operator norm, with a constant independent of the cell size;
* U041's optimized scales satisfy both `delta ell -> 0` and `delta ell^2 -> 0`;
* therefore the curved Wilson Hessian is positive on the actual horizontal tangent space with a quantitative lower bound `c/ell^2`;
* consequently the boundary trace of a horizontal fluctuation is controlled by the magnetic Hessian with an `O(ell^2)` loss.

This closes the **bulk horizontal trace/coercivity** obligation left in U042. It does **not** yet compare the curved and flat boundary Dirichlet-to-Neumann/Steklov Schur complements with fixed boundary representation data. That boundary-fixed comparison is now the first unresolved step.

## 2. Open four-dimensional cell and tangent gauge map

Let `C_ell={0,...,ell}^4` be the vertex set of an open four-dimensional cubical phase cell, with positively oriented nearest-neighbor links `E_ell`. A U041-regular core has, after its explicit local tree gauge,

    U_e = exp(i A_e.sigma),       max_e |A_e| <= delta,       (1)

where on the optimized U041 scales

    ell = O(alpha^(-1/13)),
    delta = O(alpha^(7/26)).                                  (2)

Equip link and vertex Lie-algebra fields with counting-measure Euclidean norms. For an oriented link `e=(x,y)`, use the right-trivialized infinitesimal gauge map

    (G_U phi)_e = phi(x) - Ad_(U_e) phi(y).                   (3)

At the identity connection,

    G_0 = d_0 tensor I_3.                                     (4)

The full gauge orbit also contains global conjugations. We do **not** delete their representation data by a separate cell-singlet projection; U037 showed why that would be unsafe. For the comparison below it suffices to test (3) on the mean-zero vertex fields

    V_0 = {phi : sum_x phi(x)=0}.                             (5)

A vector horizontal to the full actual gauge orbit is automatically orthogonal to `G_U V_0`.

## 3. Exact flat scalar gauge gap

For the path with `ell` cells the vertex graph Laplacian has eigenvalues

    nu(k)=4 sin^2[pi k/(2(ell+1))],   k=0,...,ell.            (6)

Tensoring four such paths gives the scalar graph spectrum on `C_ell`. Therefore, on mean-zero vertex fields,

    ||G_0 phi||_2 >= sigma_ell ||phi||_2,

    sigma_ell = 2 sin[pi/(2(ell+1))].                         (7)

The elementary bound `sin x >= 2x/pi` on `[0,pi/2]` gives

    sigma_ell >= 2/(ell+1).                                  (8)

This is the correct gap after quotienting only the constant scalar kernel. Pinning a single root instead would give a poorer Poincare constant and is not used here.

## 4. The actual gauge map is a local perturbation of d0

For SU(2), if `U=exp(i A.sigma)` with `|A|<=delta<=pi/2`, the adjoint action is an SO(3) rotation through angle `2|A|`. Hence

    ||Ad_U-I||_op = 2 sin |A| <= 2|A| <= 2delta.              (9)

Using (3)-(4),

    [(G_U-G_0)phi]_e = (I-Ad_(U_e)) phi(y).                  (10)

Each vertex is the head of at most four positively oriented links, so

    ||(G_U-G_0)phi||_2^2
       <= 16 delta^2 ||phi||_2^2.                             (11)

Thus

    ||G_U-G_0||_(V_0 -> E) <= 4delta.                        (12)

No cell-volume factor appears.

## 5. Exact gradient-leakage lemma

Let `P_grad` be the orthogonal projection onto `ran G_0`, equivalently onto the flat gradient link fields. Let `b` be orthogonal to the **actual** gauge orbit `ran G_U`; in particular

    <b,G_U phi>=0       for every phi in V_0.                (13)

Put

    g = P_grad b = G_0 phi

with the unique mean-zero minimum-norm `phi`. By (7),

    ||phi|| <= sigma_ell^(-1) ||g||.                         (14)

Since `P_grad` is orthogonal,

    ||g||^2 = <b,G_0 phi>
            = <b,(G_0-G_U)phi>.                              (15)

Equations (12),(14) imply

    ||P_grad b|| <= eta ||b||,

    eta = 4delta/sigma_ell
        <= 2delta(ell+1).                                    (16)

This is the required comparison between the true curved horizontal space and the flat Coulomb space. It does not construct or fix a nonlinear gauge and therefore does not discard boundary gauge transformations.

On the optimized scales (2),

    eta = O(alpha^(5/26)) -> 0.                              (17)

## 6. Exact flat transverse curl gap on the open 4-cube

Let `d_1` be the edge-to-plaquette coboundary. The same tensor/Koszul argument used in U028 works in four dimensions.

For a multi-index `k=(k_1,...,k_4)` let `s(k)` be the number of positive entries and

    Lambda(k)=sum_i nu(k_i).                                 (18)

The one-form block has dimension `s(k)`. Its gradient direction has one dimension and the flat transverse space has dimension `s(k)-1`. On every transverse vector the curl Laplacian is exactly multiplication by `Lambda(k)`.

There is no transverse mode with `s=1`. Hence the smallest positive transverse curl eigenvalue is attained by two first path modes:

    mu_ell
      = 2 nu(1)
      = 8 sin^2[pi/(2(ell+1))].                              (19)

In particular

    mu_ell >= 8/(ell+1)^2.                                  (20)

Write

    b = b_T + P_grad b,       d_0^* b_T=0.                  (21)

Because `d_1 d_0=0`,

    ||d_1 b||^2 = ||d_1 b_T||^2
       >= mu_ell ||b_T||^2
       >= mu_ell(1-eta^2)||b||^2.                            (22)

Thus actual curved horizontality already forces a nearly transverse **flat** curl cost before any Wilson-Hessian perturbation is used.

## 7. Locality gives a volume-independent Wilson-Hessian perturbation

Let

    S(U)=sum_(p subset C_ell) [1-(1/2)ReTr U_p]              (23)

be the internal Wilson magnetic action. Use the product bi-invariant Riemannian metric and right-trivialized link tangent vectors. At the identity connection,

    Hess_I S[b,b] = ||d_1 b||_2^2.                           (24)

Fix a universal logarithmic chart radius `delta_0>0`. A single plaquette term is a smooth function of four SU(2) links. On the compact four-link chart `max|A_e|<=delta_0`, its Hessian is Lipschitz. Therefore there is a universal finite `K_p` such that

    |Hess_U S_p[b,b]-Hess_I S_p[b,b]|
       <= K_p delta sum_(e in p)|b_e|^2.                    (25)

Each four-dimensional link belongs to at most six internal plaquettes. Summing (25) yields a universal

    K_H = 6 K_p < infinity                                  (26)

independent of `ell` and the cell location, with

    |Hess_U S[b,b]-||d_1 b||^2|
       <= K_H delta ||b||^2.                                (27)

This is an absolute local Hessian estimate. It is not yet a boundary effective-action estimate.

Combining (22),(27), every actual-gauge-horizontal `b` obeys

    Hess_U S[b,b]
       >= [mu_ell(1-eta^2)-K_H delta] ||b||^2.              (28)

The action is gauge invariant, and the gauge action is isometric for the product metric. On a regular orbit-type stratum, the Riemannian Hessian of the descended action on configuration space modulo gauge is exactly (28) on horizontal lifts; vertical O'Neill terms are orthogonal to the horizontal gradient. At stabilizer points (28) is simply read as the ambient horizontal inequality and extends by continuity. No regional singlet projection is involved.

## 8. Optimized U041 scales make the curved Hessian coercive

From (2),

    delta ell     = O(alpha^(5/26)) -> 0,
    delta ell^2   = O(alpha^(3/26)) -> 0.                   (29)

The first limit controls the subspace angle `eta`; the second controls the absolute Hessian error relative to `mu_ell~ell^-2`.

Indeed, for sufficiently small `alpha`, simultaneously

    eta^2 <= 1/4,
    K_H delta <= mu_ell/4.                                  (30)

Then (28) gives

    Hess_U S[b,b] >= (mu_ell/2)||b||^2
                   >= 4/(ell+1)^2 ||b||^2.                 (31)

Equation (31) is a genuine curved-background magnetic coercivity theorem on every U041-regular core, uniform in the core's position and in the exterior lattice volume. The threshold in `alpha` depends only on the universal local chart/Hessian constants, not on the number of cells in the enclosing lattice.

It is a Hessian theorem, not a statement that the full interacting measure is Gaussian and not a physical mass-gap estimate.

## 9. The O(ell^2) curved trace/Poincare estimate

Let `Tr_partial b` denote any subset of the link tangent variables on the cell boundary, in particular the tangential boundary links used in U041-U042. Trivially

    ||Tr_partial b||^2 <= ||b||^2.                           (32)

Combining with (31),

    ||Tr_partial b||^2
       <= (ell+1)^2/4  Hess_U S[b,b].                        (33)

Thus the missing **curved horizontal trace/Poincare loss is at most O(ell^2)**.

This is exactly the scaling anticipated in U042. It is also why the optimized phase-cell exponents were important: a local `O(delta)` coefficient error amplified by `(ell+1)^2` still tends to zero as `alpha^(3/26)`.

There is, however, a crucial scope restriction. Equation (33) is on the actual gauge-horizontal quotient directions. Boundary gauge-orbit directions are not assigned an artificial magnetic cost; their representation data must still be carried through phase-cell gluing. This is compatible with U037's boundary-charge warning.

## 10. What this does and does not do for the Steklov split

U042 separated the flat boundary space into:

1. exact gauge gradients (large zero kernel),
2. bounded-dimensional `O(1/ell)` coexact/harmonic modes,
3. a stiff coexact sector.

U043 proves that the **curved bulk quotient form** stays coercive and supplies the required `O(ell^2)` trace control. This removes the feared scaling obstruction to perturbing the high boundary sector.

It does **not yet** prove that the curved boundary Schur complement preserves U042's flat high/soft splitting. The reason is structural, not numerical: minimizing the curved form with fixed tangential boundary data requires a boundary-fixed gauge slice. The actual interior horizontal projection can change normal/interior edge variables, and one must show that the resulting quotient identification preserves the boundary representation coordinates while perturbing the Schur complement by `o(1/ell)` (or an equivalent relative form bound).

That is now the first unresolved implication.

## 11. Verification, repair, and self-audit

`checks/U043_curved_horizontal_coercivity_checks.py` has nine focused tests. They cover:

- the exact path scalar gap formula;
- a complete `ell=1` four-dimensional cubical incidence/Hodge audit (`16` vertices, `32` links, `24` plaquettes), including `d_1 d_0=0`, full one-form Hodge gap `2`, and transverse curl gap `4`;
- finite tensor low-mode count diagnostics;
- an exact rational gradient-leakage fixture;
- the SU(2) adjoint-rotation perturbation inequality;
- the elementary lower bounds (8),(20);
- the exponents `5/26` and `3/26` in (29);
- a deterministic horizontal-subspace perturbation fixture;
- the algebraic trace constant in (33).

One initial finite diagnostic used `C=4` for a nonempty transverse low-mode test. It correctly returned zero modes because the asymptotic first transverse threshold is `sqrt(2) pi > 4`. The diagnostic was repaired to use `C=6,8,12`; no theorem, formula, or universal range was changed. The initial output and repair record are preserved.

All nine U042 tests were rerun. Compilation and indentation checks pass. Static lint/typecheck and Lean are unavailable. Wolfram 15.0.1 independently returned the exact formulas

    nu_1 = 4 sin^2[pi/(2(ell+1))],
    mu_T = 8 sin^2[pi/(2(ell+1))],
    eta <= 2 delta(ell+1),
    7/26-1/13 = 5/26,
    7/26-2/13 = 3/26,

with the `ell=1` values `{2,4}`. The lower bounds themselves use the elementary sine inequality written above, not a CAS positivity oracle.

Primary self-audit verdict: **proved for the magnetic Hessian on the actual gauge-horizontal tangent space of a sufficiently small U041-regular SU(2) open phase cell; boundary Schur-complement stability and quantum integration remain unproved.**

No external theorem is load-bearing in (1)-(33); the proof is finite-dimensional lattice geometry, SU(2) adjoint rotation, tensor Hodge spectrum, and local smoothness.

## 12. Next executable target

Construct a **boundary-fixed gauge-equivariant slice** for the regular core:

1. allow gauge transformations that are identity on boundary vertices so tangential boundary links/representations remain fixed;
2. compare its curved interior-horizontal space with the flat boundary-fixed Coulomb space;
3. prove the quotient identification changes the minimized boundary quadratic form by `O(delta ell^2)` relatively on the U042 stiff sector (or by `o(1/ell)` absolutely);
4. conclude that the curved Steklov high sector remains integrable while the exact gauge representation data and bounded coexact/cycle soft sector are retained.

Only after that comparison is established should the project return to the centered physical transfer/RG recursion. A local magnetic Hessian gap is not itself the Yang-Mills mass gap.

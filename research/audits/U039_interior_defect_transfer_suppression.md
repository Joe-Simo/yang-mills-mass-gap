# U039 — interior bad-block probabilities become transfer-operator bounds

Date: 2026-09-15. Base: private `Joe-Simo/yang-mills-mass-gap` commit `39545b5bae0af2280b6108826cc4551914a10763` (U038).

**We have not solved the Yang–Mills problem yet.**

Evidence: self-reviewed finite-regulator operator proof plus exact symbolic/rational checks. No independent expert/formal verification, novelty claim, continuum construction, or physical mass-gap theorem.

## 1. Why this step is different from the failed endpoint-indicator argument

U038 proved a uniform conditional probability bound for a dense-defect event in a four-dimensional Wilson block, but also correctly observed that multiplication by a rare event at one time still has operator norm one. The next question was whether the rarity can nevertheless enter the physical transfer form.

It can, provided the defective block is strictly **inside** a Euclidean time slab rather than at an endpoint. Endpoint wavefunctions then belong to the exterior sigma-algebra of the block. The U038 conditional bound can be applied after multiplying by arbitrary endpoint states. This turns a probability estimate into an operator-norm estimate for the corresponding interior insertion.

This is the first result in this route that removes U038's specific `indicator has norm one` obstruction without assuming that low-energy states are pointwise bounded or that the desired gap already exists.

## 2. Finite Wilson transfer and stationary slab law

Specialize the finite-regulator transfer construction of U031–U032 to isotropic SU(2) Wilson coupling `beta>0`. Let `K` be the positive self-adjoint ground-state-transformed one-step transfer on `L2(pi)`, where `pi` is its actual Perron-vacuum measure. Thus

    K 1 = 1,  0 <= K <= I.

For an integer slab depth `T`, let `P_T` denote the stationary path law of

    U_0,U_1,...,U_T.

Then for endpoint functions `f,g in L2(pi)`,

    E_T[conj(f(U_0)) g(U_T)] = <f,K^T g>_pi.               (1)

Undoing the ground-state transform in the path density gives the ordinary finite Euclidean Wilson weight in the interior, multiplied by positive factors depending only on the global endpoints. Therefore, if a four-dimensional block `B` and every plaquette touching its integrated links are strictly between times 0 and T, then conditioning on all variables outside `B` gives exactly the same local Wilson conditional law used in U038. The unknown Perron eigenfunction appears only in exterior factors and cancels from the conditional distribution.

No replacement of `pi` by Haar, a Gaussian, or a product vacuum is made.

## 3. Interior-insertion lemma

Let `E_B` be any event depending only on the interior variables of such a block and suppose

    P_T(E_B | outside B) <= p                                  (2)

almost surely, with the bound uniform in the exterior configuration.

Define the bounded operator `R_B^(T)` by the bilinear form

    <f,R_B^(T) g>_pi
      = E_T[conj(f(U_0)) g(U_T) 1_(E_B)].                     (3)

Because both endpoint factors are measurable with respect to the exterior of `B`, conditioning gives

    |<f,R_B^(T) g>|
      <= p E_T[|f(U_0) g(U_T)|]
      <= p ||f||_2 ||g||_2.                                  (4)

Hence

    ||R_B^(T)|| <= p.                                         (5)

This elementary argument is the key bridge. It would be false for endpoint multiplication by `1_(E_B)`, because then the state itself can be supported on the event. Moving the event into the slab makes the arbitrary endpoint states part of the conditioning exterior.

The proof uses no pre-existing spectral gap.

### Finite unions

For interior blocks `B_1,...,B_N`, not necessarily disjoint,

    1_(union_i E_i) <= sum_i 1_(E_i).

Applying (4) termwise gives an operator `R_union` satisfying

    ||R_union|| <= sum_i p_i.                                (6)

For the disjoint block family of U038 Section 5, its stronger joint conditional estimate additionally gives

    ||R_(intersection_(i in S) E_i)|| <= p^|S|.               (7)

Thus the rooted bad-cluster estimate from U038 also has an operator-insertion analogue whenever the cluster lies strictly inside the slab.

## 4. Apply U038 with an adaptive weak-coupling threshold

For `beta>=32`, set

    alpha_beta = 16 log(beta)/beta.                            (8)

This is below 2 and decreases to zero. U038 chooses `delta=alpha/8` and requires

    n >= 32/alpha.

Here that becomes

    n >= 2 beta/log(beta).                                    (9)

The Haar-ball lower bound in U038 is

    v(delta) >= alpha^3/[192(22/7)^3].                        (10)

For `beta>=32`, `log beta>3`, so

    beta^4 v(delta)
      >= 4096 beta (log beta)^3/[192(22/7)^3]
      >= 790272/1331 > 1.                                    (11)

Therefore

    log(1/v(delta)) <= 4 log beta.                            (12)

The exact open-box ratio is

    L/M = 2(n+1)/(3n) <= 1  (n>=2).

Since `beta alpha_beta=16 log beta`, (12) verifies U038's entropy threshold

    beta alpha_beta >= 4(L/M) log(1/v).                       (13)

Hence every such block satisfies, uniformly in all exterior link values,

    P_T(A_B >= alpha_beta M | outside B)
       <= exp[-beta alpha_beta M/4]
       = beta^(-4M).                                          (14)

Here

    M=6 n^2(n+1)^2

is the corrected four-dimensional plaquette count.

Combining (5) and (14): the transfer-form contribution of one interior dense-action block has operator norm at most `beta^(-4M)`.

## 5. Many interior blocks and a fixed-physical-time diagnostic

Let `Bad_int` be the event that at least one block in a chosen collection of `N_B` interior blocks violates the action-density bound. The corresponding transfer insertion obeys

    ||R_Bad_int|| <= N_B beta^(-4M).                          (15)

At the minimum admissible scale in (9),

    M >= 6 n^4,
    n >= 2 beta/log beta,

so

    4M log beta >= 384 beta^4/(log beta)^3.                  (16)

Thus

    ||R_Bad_int||
      <= N_B exp[-384 beta^4/(log beta)^3].                  (17)

Suppose only as a scaling diagnostic that a lattice spacing `a->0` is accompanied by

    beta(a) ~ K log(1/a), K>0,

and choose `n(a)=ceil[2 beta/log beta]`. Then

    a n(a) -> 0,                                             (18)

while even the crude choice `N_B=O(a^-4)` satisfies

    N_B exp[-384 beta^4/(log beta)^3] -> 0.                  (19)

More generally, (19) follows whenever

    beta(a)^4/[log^3 beta(a) log(1/a)] -> infinity.

Equation (19) is a **conditional continuum-scaling diagnostic**, not a construction of the asymptotically free trajectory.

For a fixed physical transfer time `t0`, blocks can be placed only in the middle of the slab, leaving exact microscopic boundary collars. Writing schematically

    K^T = K^m [middle transfer] K^m,

and replacing only the middle transfer by its all-good-history restriction changes the full operator by at most (15), because the outer factors are contractions. Thus endpoint large-field states need not themselves be projected away.

## 6. Deterministic structure on every good block

The same adaptive choice also turns the complement into a quantitative small-field/large-field decomposition without requiring every plaquette to be small.

On a good block,

    A_B < alpha M.

Let `theta_p in [0,pi]` be the SU(2) plaquette class angles. Since

    1-cos theta >= 2 theta^2/pi^2,

we have

    sum_p theta_p^2 <= (pi^2/2) alpha M.                     (20)

Set the local angle threshold

    epsilon_beta = alpha^(1/4).

The number `N_large` of plaquettes with `theta_p>=epsilon_beta` satisfies

    N_large/M
      <= alpha/[1-cos epsilon_beta]
      <= (pi^2/2) sqrt(alpha)
      < (242/49) sqrt(alpha).                                (21)

With (8), the rational upper coefficient becomes

    N_large/M < (968/49) sqrt[log beta/beta] -> 0.           (22)

On every remaining plaquette,

    0 <= theta^2/2-(1-cos theta) <= theta^4/24,

so its relative deviation from the quadratic action obeys

    [theta^2/2-(1-cos theta)]/(theta^2/2)
      <= sqrt(alpha)/12
      = (1/3) sqrt[log beta/beta] -> 0.                      (23)

Thus, on the all-good interior histories selected above:

- the mean squared curvature angle tends to zero;
- all but an `O(sqrt(log beta/beta))` fraction of plaquettes have vanishing angle;
- on that overwhelming fraction the Wilson action is uniformly quadratic up to relative `O(sqrt(log beta/beta))` error.

The exceptional plaquettes are not deleted. They may form sparse connected sheets, carry topology, or couple to boundary representations.

## 7. What has and has not been closed

U038's statement that a rare endpoint indicator has norm one remains correct. U039 bypasses it only for **interior Euclidean insertions**, where arbitrary endpoint states are exterior variables.

This provides a genuine large-field transfer-form estimate:

    full fixed-time transfer
      = all-good-interior contribution + operator-norm-small remainder        (24)

under the explicit finite-regulator/adaptive-block hypotheses, and the remainder can vanish extremely fast on the logarithmic weak-coupling diagnostic.

What remains unproved is now concentrated in the all-good contribution. Equations (20)–(23) do NOT imply a gauge-fixed potential is uniformly small, do not exclude sparse topological/extended defects, and do not give a positive centered spectral edge. A critical four-dimensional gauge-fixing/background-field estimate must retain the exceptional plaquettes and every boundary representation.

This is structurally close to the small-field/large-field split used in rigorous lattice-gauge renormalization programs, but no Balaban/Federbush theorem is imported here and no novelty claim is made. Existing rigorous RG literature establishes substantial ultraviolet control, not the Clay mass gap.

## 8. Checks and evidence

`checks/U039_interior_transfer_badblock_checks.py` contains seven exact tests:

1. adaptive-parameter identities;
2. the exact rational Haar safety margin `790272/1331>1`;
3. corrected open-box `L/M` ratios;
4. balanced exceptional-fraction algebra;
5. the explicit `384 beta^4/log^3 beta` exponent;
6. a reversible binary stationary-path fixture checking that an interior-event insertion norm is below its worst conditional probability;
7. an exact correlated tower-property fixture.

The binary fixtures audit the operator/probability algebra, not Wilson data. All ten U038 checks were rerun separately. Compilation and indentation checks pass. Wolfram 15.0.1 independently returned zero residuals for the adaptive identities, the same exact Haar margin, the same balanced coefficients, the continuum exponent ratio `Infinity`, and the physical block-side limit zero.

Primary self-audit verdict: **proved under the explicit finite isotropic Wilson, strictly-interior block, U038 threshold restrictions**. The scaling passage is a diagnostic conditional on the stated beta(a) behavior.

## 9. Next executable obligation

Analyze the **all-good interior transfer** rather than spending more effort on dense large-field probability. The immediate target is a gauge-covariant background-field decomposition on one good block that:

1. keeps the `O(sqrt(alpha))` exceptional plaquettes as an explicit defect set;
2. proves a quadratic/coercive estimate for the regular plaquettes modulo gauge and low collective modes;
3. places those low collective modes into a retained coarse/boundary sector rather than assuming they are massive;
4. yields a relative fixed-time form estimate that can be combined with the operator-small remainder (24).

A failure should be exhibited by an explicit good-block configuration satisfying (20)–(23), not by reverting to the withdrawn U009 boundary argument.

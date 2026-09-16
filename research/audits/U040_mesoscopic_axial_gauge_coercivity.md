# U040 — mesoscopic axial-gauge regular cores and local nonlinear coercivity

Date: 2026-09-16. Base: private `Joe-Simo/yang-mills-mass-gap` commit `9fd62dca961fc6ca9f3fe4eb3113fa248d50f01e` (U039 status head).

**We have not solved the Yang–Mills problem yet.**

Evidence: self-reviewed finite-regulator deterministic gauge decomposition, exact cubical ribbon checks, and a local smooth-coordinate coercivity proof. No independent expert/formal verification, novelty claim, continuum construction, or physical mass-gap theorem.

## 1. Target and research decision

U039 split the fixed-physical-time transfer into an all-good interior contribution plus an operator-norm-small dense-defect remainder. Its remaining obligation was to control the all-good contribution without demanding that the entire growing block lie in one globally small gauge chart.

This unit attacks exactly that implication. The main result is a two-scale deterministic decomposition of every U039-good four-dimensional block:

1. a vanishing-density skeleton containing one-cell separators and mesoscopic cores whose TOTAL Wilson action is not small;
2. disjoint regular mesoscopic cores covering the remaining fraction;
3. on each regular core, an explicit maximal-tree/axial gauge in which every link lies in a single small exponential chart;
4. on each such core, the exact Wilson magnetic action is asymptotically equivalent to the quadratic linear-curl action, with a relative error tending to zero.

The independent core gauges are deliberately NOT glued. Gauge transition data, topology spanning several cores, and all modes living on the separators are retained in the skeleton. Thus the result does not assume away the collective infrared sector that U034-U039 repeatedly identified as the dangerous part.

## 2. Starting macroblock estimate from U039

Let `B_n` be an open four-dimensional block with `n` cells per coordinate direction. Its exact positive-orientation plaquette count is

    M_n = 6 n^2 (n+1)^2.                                      (1)

On the U039 all-good event,

    S_B := sum_(p in B_n) [1-(1/2) Re Tr U_p] < alpha M_n,    (2)

with `0<alpha<=1` and, on the adaptive U039 choice,

    alpha = 16 log(beta)/beta,
    n >= 32/alpha = 2 beta/log(beta).                         (3)

We use only (2) until the final scaling paragraph.

## 3. Mesoscopic cores separated by one-cell corridors

Set

    ell = ceil(alpha^(-1/16)),
    eps = alpha^(1/2).                                        (4)

Tile the block by disjoint `ell`-cell cores separated in every coordinate direction by a one-cell corridor. Put

    q = floor[n/(ell+1)].

The union of the regular core cell sets occupies fraction `(q ell/n)^4`. Since

    q >= n/(ell+1)-1,

we have

    q ell/n >= ell/(ell+1)-ell/n.

For `0<=x<=1`, `1-x^4<=4(1-x)`, so the cell fraction in the separator/uncovered region obeys

    f_sep <= 4[1/(ell+1)+ell/n]
          <= 4[1/ell+ell/n].                                 (5)

Under (3) and `alpha<=1`, `ell<=2 alpha^(-1/16)`, hence

    ell/n <= alpha^(15/16)/16,
    f_sep <= (17/4) alpha^(1/16).                            (6)

Call a mesoscopic core `C` internally bad when its own Wilson action satisfies

    S_C > eps.                                                (7)

The cores have disjoint plaquette interiors, so

    N_bad eps < sum_C S_C <= S_B < alpha M_n.

Since `M_n<=24 n^4` for `n>=1`, the four-cell fraction occupied by bad cores satisfies

    f_bad <= N_bad ell^4/n^4
          < 24 alpha ell^4/eps
          <= 384 alpha^(1/4).                                (8)

Therefore the union of separators and internally bad cores has cell fraction

    f_exceptional <= (17/4) alpha^(1/16)+384 alpha^(1/4)
                  = O(alpha^(1/16)).                         (9)

This is a deterministic statement on EVERY U039-good macroblock; no probability, independence, or Gaussian approximation is inserted.

## 4. Exact axial-tree ribbon identity on one regular core

Fix one core `C={0,...,ell}^4` with `S_C<=eps`. For a vertex

    x=(x_0,x_1,x_2,x_3),

let `P_x` be the canonical path from the origin to `x` that takes all direction-3 steps first, then direction 2, then 1, then 0. Let `g(x)` be its ordered link holonomy. Use the local frame

    V_(x,mu) = g(x) U_(x,mu) g(x+e_mu)^(-1).                 (10)

A link `(x,mu)` is in the canonical maximal tree exactly when

    x_nu=0 for every nu<mu.                                  (11)

For such links `P_(x+e_mu)=P_x e_mu`, hence `V_(x,mu)=I`.

For a non-tree link, compare the path word `P_x e_mu` with `P_(x+e_mu)`. The extra `mu` step is moved left across precisely

    N_e = sum_(nu<mu) x_nu <= 3 ell                           (12)

lower-direction steps. Every adjacent exchange `nu mu -> mu nu` is the boundary of one elementary `(nu,mu)` plaquette. Peeling the corresponding plaquettes in that swap order gives the nonabelian ribbon identity

    V_e = product_(j=1..N_e) h_j U_(p_j)^(sigma_j) h_j^(-1), (13)

where `sigma_j=+/-1` and the `h_j` are partial path holonomies. This is an exact group identity; commutativity is not assumed.

Let `theta_p in [0,pi]` be the SU(2) class angle of `U_p`, and use the bi-invariant geodesic distance. Conjugation and inversion preserve this angle, while the triangle inequality applied to (13) gives

    theta(V_e) <= sum_(j=1..N_e) theta_(p_j)
               <= sqrt(3 ell) ||theta||_(2,C).               (14)

The checker verifies the canonical tree size and, for every edge of every box with `d=2,3,4` and `ell=1,2,3`, verifies that the mod-2 boundary of the explicit swap ribbon is exactly the fundamental tree cycle and that its length is the formula in (12). The written peeling argument supplies orientations and conjugations for (13).

## 5. A single small exponential chart on every regular core

The elementary SU(2) scalar inequality

    1-cos(theta) >= 2 theta^2/pi^2,  0<=theta<=pi,

and `S_C<=eps` imply

    ||theta||_(2,C)^2 <= (pi^2/2) eps.                       (15)

Combining (14)-(15), every tree-gauge link has a principal logarithm

    V_e = exp(A_e),  A_e in su(2),

once `alpha` is sufficiently small, and

    delta := max_e |A_e|
       <= pi sqrt(3 ell eps/2)
       <= pi sqrt(3) alpha^(7/32).                           (16)

The last inequality uses `ell<=2 alpha^(-1/16)`.

The exact link count of the four-dimensional core is

    L_ell = 4 ell(ell+1)^3 <= 32 ell^4.                      (17)

Using (14) before substituting (15) gives the useful norm bound

    ||A||_2 <= sqrt(96) ell^(5/2) ||theta||_2
             = 4 sqrt(6) ell^(5/2) ||F||_2,                 (18)

where `F_p=log V_p` is the principal plaquette logarithm and `|F_p|=theta_p`.

Equation (18) is deliberately crude but uniform in the core location and exterior field. It already gives a nonlinear local coercivity relation because the tree gauge removes every flat link degree of freedom on this contractible core.

## 6. Noncommutative quadratic comparison with the linear curl

Let `d_1 A` denote the signed linear edge-to-plaquette coboundary. We now compare it with the exact plaquette logarithm `F`.

Choose a fixed `delta_0>0` so small that a product of four SU(2) exponentials with each input norm at most `delta_0` remains in the principal logarithm chart. For one oriented plaquette define the smooth finite-dimensional map

    Phi(X_1,...,X_4)
      = log[exp(s_1 X_1) exp(s_2 X_2) exp(s_3 X_3) exp(s_4 X_4)],

with the orientation signs absorbed into `s_j=+/-1`. Its derivative at the origin is the signed sum. Because the closed input ball is compact and the logarithm is smooth there, Taylor's theorem supplies a UNIVERSAL finite constant `C_1` such that, whenever `max_j |X_j|<=delta_0`,

    |Phi(X)-sum_j s_j X_j|
       <= C_1 delta sum_j |X_j|.                             (19)

No expansion coefficient is dropped; `C_1` is the supremum of the relevant second derivative on the fixed chart.

For our core, (16) eventually makes `delta<=delta_0`. Each edge belongs to at most six plaquettes, so Cauchy-Schwarz in (19) yields

    ||F-d_1 A||_2 <= 2 sqrt(6) C_1 delta ||A||_2.            (20)

Using (18),

    ||F-d_1 A||_2 <= rho ||F||_2,
    rho := 48 C_1 delta ell^(5/2)
         <= 192 pi sqrt(6) C_1 alpha^(1/16).                 (21)

Thus `rho->0` despite `ell->infinity`. In particular for sufficiently small `alpha`, `rho<1/2` and

    (1-rho)||F||_2 <= ||d_1 A||_2 <= (1+rho)||F||_2.         (22)

This is the desired local gauge-covariant coercive/background-field statement on each regular core: after an explicitly constructed local frame, the exact nonabelian curvature is asymptotically the linear curl on a core whose lattice diameter itself diverges.

## 7. Exact Wilson action versus the quadratic core action

For `0<=theta<=pi`,

    theta^2/2-theta^4/24 <= 1-cos(theta) <= theta^2/2.

On a regular core, each `theta_p^2<= (pi^2/2)eps`, so with

    kappa = pi^2 eps/24 = pi^2 alpha^(1/2)/24,               (23)

we obtain

    (1-kappa) ||F||_2^2/2 <= S_C <= ||F||_2^2/2.             (24)

Combining (22) and (24),

    (1-kappa) ||d_1 A||_2^2/[2(1+rho)^2]
      <= S_C
      <= ||d_1 A||_2^2/[2(1-rho)^2].                        (25)

Both coefficients converge to `1/2` as `alpha->0`.

Equation (18) additionally gives a fully nonlinear tree-gauge lower bound

    S_C >= (1-kappa) ||A||_2^2/[192 ell^5].                 (26)

This constant is not claimed optimal; the purpose is to show genuine coercivity on each regular core without a global bare-field norm hypothesis.

## 8. Why this avoids U028's failed global-small-norm event

U028 proved a useful nonlinear comparison in a global linear Coulomb slice but then showed that its global norm condition becomes atypical in the growing quadratic reference vacuum. U040 does not reopen that failed route unchanged.

Instead:

- no global gauge is selected;
- the macroblock may contain arbitrarily large link holonomies before local framing;
- only the TOTAL action of a mesoscopic core is required to be `<=eps`;
- internally bad cores are retained explicitly rather than assumed absent;
- one-cell corridors retain inter-core transition functions and all global/topological data;
- the regular-core coverage tends to one by (9), while the core size itself tends to infinity.

Thus the new input is a genuine multiscale localization of the gauge chart, not another global-small-field hypothesis.

## 9. Weak-coupling scale diagnostic

On U039's adaptive choice,

    alpha_beta = 16 log(beta)/beta,

we have

    ell_beta ~ (beta/log beta)^(1/16),
    n_beta ~ beta/log beta,
    ell_beta/n_beta = O[(log beta/beta)^(15/16)] -> 0.       (27)

Hence each U039 macroblock contains a diverging number of mesoscopic cores in every direction, while the exceptional cell fraction tends to zero.

If, only as the same diagnostic used in U039,

    beta(a) ~ K log(1/a),  K>0,

then

    a ell_beta -> 0.                                         (28)

So the local gauge cells shrink in physical diameter while growing in lattice units. No claim is made that (27)-(28) construct the renormalized trajectory.

## 10. Relation to verified literature

The official Jaffe-Witten problem description was checked again on 2026-09-16. In its discussion of Balaban's program it emphasizes that gauge choices are central, that gauges are defined in local "phase cells" and vary both in space-time and across scales, and that four-dimensional work obtains quantitative control of large gauge fields; it separately states that new ideas are still needed for a volume-uniform mass gap. Source: Jaffe-Witten, `Quantum Yang-Mills Theory`, Clay Mathematics Institute, Section 6.5, pp.11-12 in the PDF, `https://www.claymath.org/wp-content/uploads/2022/06/yangmills.pdf`.

Balaban's primary four-dimensional small-field paper metadata was also rechecked: T. Balaban, *Renormalization group approach to lattice gauge field theories. I: Generation of effective actions in a small field approximation and a coupling constant renormalization in four dimensions*, Commun. Math. Phys. 109 (1987), 249-301, DOI `10.1007/BF01215223`. U040 does NOT import any theorem from that paper. The overlap is methodological context only.

No novelty claim is made. The maximal-tree gauge, local small-field expansion, and multiscale phase-cell philosophy are established ideas; the present record only establishes the explicitly written restricted lemmas for this project.

## 11. Checks and self-audit

Checker: `checks/U040_mesoscopic_axial_gauge_checks.py`.

Nine focused exact tests pass:

1. canonical axial tree has exactly `V-1` edges for all tested `d=2,3,4`, `ell=1,2,3` boxes;
2. every tested non-tree edge's explicit swap ribbon has exactly the fundamental-cycle boundary, with ribbon length `sum_(nu<mu)x_nu`;
3. an exact noncommutative Q8 assignment verifies the ordered conjugated-plaquette ribbon product, not only its abelianized boundary;
4. exact four-dimensional link counts and the `3 ell` ribbon bound;
5. all mesoscopic exponent balances in (4), (8), (16), (21), and (27);
6. separator coverage inequality (5) on independent integer cases;
7. exact bad-core fraction constant `384 alpha^(1/4)` under the conservative `M_n<=24n^4` and ceiling bound;
8. exact link-angle/Taylor scaling powers;
9. exact micro/macro scale separation.

All seven U039 tests were rerun and passed. Python compilation and indentation checks passed. Wolfram 15.0.1 independently returned the same powers: `alpha^(1/4)` for bad-core density, `alpha^(1/16)` for collars and nonlinear relative error, `alpha^(7/32)` for the link chart radius, and `alpha^(15/16)` for mesoscopic-to-macro scale. Its first limit-oriented call emitted the expected `0^(-1/16)` warning; a clean algebra-only rerun had no warnings. These computations corroborate algebra, not the universal written proof.

Primary self-audit verdict: **proved after the explicit U039-good-macroblock, separated-core, sufficiently-small-alpha restrictions**.

Not established: a spectral gap for the all-good transfer, an integration theorem for the regular-core fluctuations, a quantitative transfer/Dirichlet estimate on the separator skeleton, control of sparse bad-core networks beyond their deterministic density, a continuum/infinite-volume construction, a finite physical Yang-Mills mass, or compact simple groups beyond the current SU(2) route.

## 12. Next executable obligation

The large-field remainder is operator-small (U039), and U040 now makes almost all of every surviving macroblock locally quadratic/coercive in explicit gauge cells. The next load-bearing task is therefore the skeleton coupling:

1. condition on the complete separator/bad-core variables and integrate one family of disjoint regular cores;
2. derive the exact induced interaction on the skeleton without projecting boundary gauge representations to singlets;
3. test whether the induced core-to-core response is bounded by a summable surface term rather than the full core volume;
4. preserve low collective modes on the skeleton and connect the resulting bound to the centered physical transfer form.

A positive result would finally combine U039's operator-small large-field remainder with a controlled small-field interior. A failure would identify whether sparse core defects or inter-core transition variables are the next genuine obstruction.

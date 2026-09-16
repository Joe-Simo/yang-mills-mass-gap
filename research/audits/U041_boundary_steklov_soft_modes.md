# U041 — optimized phase-cell scaling and boundary Steklov soft modes

Date: 2026-09-16. Base: private `Joe-Simo/yang-mills-mass-gap` commit `b4ddd1b0a3130e1865207970b29f0f9c712f2752` (U040).

**We have not solved the Yang–Mills problem yet.**

Evidence: self-reviewed finite-regulator deterministic estimates, an exact continuous-SU(2) commuting boundary family, and exact finite algebra checks. No independent expert/formal verification, novelty claim, continuum construction, or physical mass-gap theorem.

## 1. Target and outcome

U040 proved that every U039-good macroblock can be decomposed into disjoint regular phase cells plus a vanishing-density exceptional skeleton, and that each regular cell has a local gauge in which the exact Wilson action is asymptotically quadratic.

The next proposed step was to integrate the regular cells and show that the induced interaction on the separator/bad-core skeleton is both local and quantitatively harmless. This unit obtains three results:

1. the U040 two-scale exponents can be improved and are optimal within the same elementary balance template;
2. unrestricted integration of a regular-cell interior produces a gauge-invariant boundary effective action whose dependence is supported in a surface collar and whose oscillation is bounded by a surface term;
3. a genuine continuous-SU(2) small-field family shows that no volume-uniform positive boundary coercivity constant can follow from this surface control: physical boundary modes can have stiffness `O(1/ell)`.

A separate exact linear slab calculation identifies the correct replacement for the failed "boundary interaction is uniformly stiff" hope: the boundary operator has a Steklov/Dirichlet-to-Neumann spectrum. Modes with stiffness `O(1/ell)` occupy only a bounded number of tangential Fourier modes per phase cell in the linear companion. This does not prove the corresponding nonabelian statement, but it isolates a precise next object to construct gauge-covariantly.

## 2. Optimal exponents inside the U040 proof template

Generalize U040's phase-cell choice to

    ell = ceil(alpha^(-s)),     eps = alpha^t,

with `0<s,t<1` and the same macroblock lower bound `n>=32/alpha`.

The deterministic estimates of U040 become, up to absolute constants,

    separator fraction       = O(alpha^s),
    bad-core fraction        = O(alpha^(1-4s-t)),
    max tree-gauge link size = O(alpha^((t-s)/2)),
    nonlinear curl error     = O(alpha^((t-6s)/2)),
    ell/n                    = O(alpha^(1-s)).

The Wilson-vs-angle Taylor error is `O(alpha^t)` and is never dominant in the range below.

Let

    m(s,t)=min{s, 1-4s-t, (t-6s)/2}.                         (1)

This is the common decay exponent controlling the separator density, bad-core density, and nonlinear curl error.

If `m<=s`, `m<=1-4s-t`, and `2m<=t-6s`, then `t>=2m+6s`, so

    m <= 1-4s-(2m+6s),
    3m+10s <= 1.

Since `s>=m`, this gives

    13m <= 1.                                                (2)

Therefore `m<=1/13` for every choice in this proof template. Equality is attained at

    s=1/13,       t=8/13.                                    (3)

Thus the balanced phase-cell choice is

    ell = ceil(alpha^(-1/13)),
    eps = alpha^(8/13).                                      (4)

It gives

    separator fraction       = O(alpha^(1/13)),
    bad-core fraction        = O(alpha^(1/13)),
    max tree-gauge link size = O(alpha^(7/26)),
    nonlinear curl error     = O(alpha^(1/13)),
    Wilson Taylor error      = O(alpha^(8/13)),
    ell/n                    = O(alpha^(12/13)).              (5)

This strictly improves U040's unoptimized `1/16,1/2` balance, without changing the proof architecture.

## 3. Exact surface support of one-cell integration

Let `C_ell` be the four-dimensional open cube of `ell` cells per side. Its exact plaquette count is

    M_ell=6 ell^2(ell+1)^2.

Let `C_ell^-` be the concentric subcube obtained by removing one cell from each side, so it has `ell-2` cells per side. The number of plaquettes in the one-cell collar is

    B_ell = M_ell-M_(ell-2)
          = 48 ell^3-72 ell^2+72 ell-24.                     (6)

Split the link variables into the links of `C_ell^-` and all remaining shell links. For fixed shell configuration `b`, define the ordinary, UNRESTRICTED interior partition function

    Z_ell(b)=int exp[-beta S_ell(u,b)] du,

with normalized product Haar measure over interior links.

Every plaquette wholly contained in `C_ell^-` is independent of `b`; only the `B_ell` collar plaquettes can change when `b` changes. Since every Wilson plaquette deficit lies in `[0,2]`, for all interior `u` and all shell data `b,b'`,

    |S_ell(u,b)-S_ell(u,b')| <= 2 B_ell.

Therefore

    exp(-2 beta B_ell)
      <= Z_ell(b)/Z_ell(b')
      <= exp( 2 beta B_ell),                                (7)

and for the induced effective action `Gamma_ell=-log Z_ell`,

    |Gamma_ell(b)-Gamma_ell(b')| <= 2 beta B_ell.            (8)

This is an exact surface-order bound, independent of the surrounding lattice volume. Haar invariance also makes `Gamma_ell` gauge invariant under boundary gauge transformations, after the corresponding change of integration variables.

Important restriction: (7)-(8) are for the unrestricted interior integral. If one inserts the hard U040 event `S_C<=eps`, the admissible interior domain depends on the boundary data and can even be empty for some shell configurations. A uniform ratio such as (7) does NOT automatically survive that hard truncation. This is one reason the regular/bad-core label cannot simply be absorbed into a smooth effective action.

## 4. Exact continuous-SU(2) soft boundary family

The surface bound (8) does not imply that the induced boundary dynamics is uniformly coercive. This can be seen inside the regular small-field regime itself.

On `C_ell`, use the commuting maximal torus of SU(2) and set all links to the identity except direction-2 links,

    U_2(x)=exp[i t x_1 sigma_3/ell],                         (9)

with `0<t<=pi/2`. Only `(1,2)` plaquettes are nontrivial. Every such plaquette has angle `t/ell`, and there are exactly

    ell^2(ell+1)^2

of them. Hence the exact Wilson action is

    S_ell(t)=ell^2(ell+1)^2 [1-cos(t/ell)]
            <= t^2(ell+1)^2/2.                              (10)

Now measure the logarithmic boundary trace only on the face `x_0=0`, using the direction-2 links there. Its squared norm is exactly

    ||A_boundary||^2
      = sum_(x_1=0)^ell sum_(x_2=0)^(ell-1) sum_(x_3=0)^ell
          t^2 x_1^2/ell^2
      = t^2 (ell+1)^2(2ell+1)/6.                            (11)

Therefore

    S_ell(t)/||A_boundary||^2 <= 3/(2ell+1).                 (12)

Let `E_ell(b)` be the minimum Wilson action over all extensions of boundary data `b`. Taking `b=b(t)` from (9),

    E_ell(b(t))/||A_boundary(t)||^2 <= 3/(2ell+1).           (13)

Thus no lower bound

    E_ell(b) >= c ||b||^2

with a fixed `c>0` can hold uniformly in `ell`, even when restricted to arbitrarily small commuting boundary data.

This family lies inside the U040 regular regime. Indeed, with any regularity threshold `eps>0`, choosing

    t=sqrt(2 eps)/(ell+1)                                    (14)

makes `S_ell(t)<=eps`, while (12) is unchanged. Under the optimized choice (4),

    t = O(alpha^(9/26)),
    ||A_boundary||^2 = O(alpha^(7/13)),
    3/(2ell+1)=O(alpha^(1/13)).                              (15)

The vanishing boundary stiffness is therefore not caused by leaving the local chart or by a large-field defect. It is a genuine long-wavelength mode.

Equation (13) is a CLASSICAL minimum-action obstruction. It does not by itself compute the exact quantum boundary free energy `Gamma_ell` in (8), and it does not prove that the full Yang-Mills transfer is gapless.

## 5. Exact scalar slab Dirichlet-to-Neumann companion

The soft family above indicates that the correct boundary object is a Dirichlet-to-Neumann (Steklov) operator, not a uniformly positive scalar constant. The following finite calculation is exact and self-contained.

For `ell>=1` and tangential Laplacian eigenvalue `lambda>=0`, minimize

    E(u)=1/2 sum_(r=0)^(ell-1) (u_(r+1)-u_r)^2
         +lambda/2 sum_(r=0)^ell u_r^2                       (16)

subject to `u_0=a`, `u_ell=0`.

The interior Euler equation is

    (2+lambda)u_r-u_(r-1)-u_(r+1)=0.

Write

    cosh(gamma)=1+lambda/2.

The minimizer is

    u_r=a sinh[(ell-r)gamma]/sinh(ell gamma),

with the `gamma=0` value understood by continuity. Substitution gives

    E_min = a^2 q_ell(lambda)/2,                             (17)

where

    q_ell(lambda)
      =1+lambda-sinh[(ell-1)gamma]/sinh(ell gamma)
      =lambda/2+sinh(gamma)coth(ell gamma).                 (18)

At `lambda=0`, `q_ell(0)=1/ell`.

Because `x coth x>=1` for `x>=0`, `sinh gamma>=gamma`, and

    sinh^2(gamma)=lambda+lambda^2/4,

we obtain the universal lower bounds

    q_ell(lambda) >= 1/ell,
    q_ell(lambda) >= sqrt(lambda).                           (19)

So if a boundary mode has stiffness at most `C/ell`, then necessarily

    lambda <= C^2/ell^2.                                    (20)

## 6. Only boundedly many `O(1/ell)` modes in the periodic slab companion

Take a three-dimensional tangential torus of side `ell`. Its scalar Fourier eigenvalues are

    lambda(n)=4 sum_(j=1)^3 sin^2(pi n_j/ell),

with representatives `|n_j|<=ell/2`.

For `|n_j|<=ell/2`,

    sin(pi |n_j|/ell) >= 2|n_j|/ell,

hence

    lambda(n) >= 16 |n|^2/ell^2.                            (21)

Combining (20)-(21), every mode with `q_ell(lambda(n))<=C/ell` satisfies

    |n| <= C/4.                                             (22)

Therefore the number of such tangential modes is bounded by

    [2 floor(C/4)+1]^3,                                     (23)

independently of `ell`.

For the linearized Maxwell field in a fixed transverse gauge on a periodic slab, each tangential transverse polarization obeys the same scalar normal recurrence, so (18)-(23) give the same stiffness scaling for each polarization. This sentence is a linearized companion statement, not a theorem about the exact nonabelian boundary Hilbert space.

The important structural point is that the `1/ell` obstruction is low-dimensional: the extremely soft trace sector need not grow with the phase-cell volume.

## 7. Research consequence

The proposed next step after U040 should NOT be:

    regular core -> integrate everything -> uniformly stiff skeleton.

That implication is refuted at the classical level by (9)-(13).

A viable refinement is instead:

    regular core
      -> gauge-covariant boundary Steklov/Hodge decomposition
      -> retain finitely many soft trace/cycle modes per phase cell
      -> integrate the high boundary modes using U040 coercivity
      -> couple the retained modes on the next coarse lattice.

This is a materially different multiscale route from the rejected global-small-field strategy of U028 and from the sharp-projector route of U014. The soft modes are identified by a boundary variational form tied to the locally gauge-fixed core, while large-field cores and separator variables remain explicit.

The first unproved implication is now precise:

**Construct, for the actual nonabelian regular core with its full boundary representation content, a gauge-covariant Steklov quadratic form whose high sector has an `ell`-scaled lower bound and whose soft sector has dimension bounded independently of `ell`, up to the U040 `O(alpha^(1/13))` nonlinear errors.**

Even such a theorem would still be an RG input rather than a mass-gap proof; one would then have to control the coarse soft-mode dynamics over many scales and reconstruct the continuum true vacuum.

## 8. Sources and checks

The derivations (1)-(23) are internal and do not rely on an external spectral theorem.

Context checked 2026-09-16:
- Jaffe-Witten, *Quantum Yang-Mills Theory*, Clay Mathematics Institute, Section 6.5: Balaban's gauges are organized in local phase cells and across scales; the same source states that a volume-uniform mass gap still requires new ideas.
- T. Balaban, *Renormalization group approach to lattice gauge field theories. I*, Commun. Math. Phys. 109 (1987), 249-301, is contextual precedent for four-dimensional small-field effective actions; no theorem from it is imported here.
- A. Girouard, M. Karpukhin, M. Levitin, I. Polterovich, arXiv:2102.06594, surveys the relation between Dirichlet-to-Neumann spectra and the boundary Laplacian. It is context only; equations (16)-(23) are proved directly for the discrete slab above.

Checker: `checks/U041_boundary_steklov_checks.py`.

Nine focused tests pass. Exact rational/SymPy tests cover the optimized exponents, exact collar count, boundary norm, the `3/(2ell+1)` soft quotient, exact rational Schur complements for slab sizes `1..7`, finite exact checks of the lower bounds, and a positive-weight surface-oscillation fixture. A finite Fourier iterator checks the mode-count inequality for selected `ell,C`; the universal count is the written proof (21)-(23), not the finite sweep.

The Python environment emits an unrelated `artifact_tool` spreadsheet warmup warning before the checker when launched through the notebook runtime; the checker itself exits zero and all nine tests pass. No random sampling is used.

Primary self-audit verdict: **proved after the explicit finite-cell/classical-boundary and linear-slab restrictions**.

Not established: a nonabelian quantum Steklov theorem, a uniform high-mode transfer gap in the actual vacuum, bounded soft-sector dimension after exact gauge constraints, iteration across scales, continuum existence, or a positive finite physical Yang-Mills mass gap.

# U023 — free scalar ultrasoft inheritance has summable dispersion error

Date: 2026-09-14.

**We have not solved the Yang–Mills problem yet.**

This bounded attempt executes U022's scalar inheritance test. For canonically matched physical momentum modes on nested periodic lattices, the standard nearest-neighbor dispersion differs from the continuum dispersion by relative O(a^2 |p|^2). Consequently the relative discrepancy between two successive lattice scales is also O(a^2 |p|^2). On the U021/U022 ultrasoft window this is polylogarithmic times a positive power of the lattice spacing and is summable along geometric refinement. Thus the **free scalar dispersion-inheritance obligation closes**. This does not transfer automatically to interacting Yang–Mills.

## 1. Physical normalization

Take a periodic d-dimensional lattice with physical spacing a and fixed physical box side L_phys. For a Fourier mode with physical momentum p, the standard nearest-neighbor positive Laplacian has eigenvalue

    omega_a(p)^2
      = (4/a^2) sum_(mu=1)^d sin^2(a p_mu/2).

The continuum eigenvalue is |p|^2.

For |a p_mu| sufficiently small, Taylor expansion gives

    (4/a^2) sin^2(a p_mu/2)
      = p_mu^2 - (a^2/12)p_mu^4
        + (a^4/360)p_mu^6 + O(a^6 p_mu^8).

Wolfram 15.0.1 independently returned these coefficients and the one-dimensional relative series

    1 - a^2 p^2/12 + a^4 p^4/360 - ... .

Summing coordinates,

    omega_a(p)^2
      = |p|^2 - (a^2/12) sum_mu p_mu^4
        + O(a^4 |p|^6).

Therefore, for p!=0 in a fixed small-dispersion regime,

    |omega_a(p)^2/|p|^2 - 1|
      <= C a^2 |p|^2.                                   (D)

The constant is uniform in dimension d fixed and in all momenta satisfying max_mu |a p_mu|<=c<pi.

## 2. Successive-scale matching

Let the next finer lattice have spacing a/b with fixed integer blocking factor b>1. Match the same physical momentum p on both lattices. Applying (D) twice gives

    |omega_a(p)^2 - omega_(a/b)(p)^2|
       / omega_(a/b)(p)^2
      <= C_b a^2 |p|^2                                  (I)

for sufficiently small a|p|, after absorbing the denominator comparison into the constant.

Thus the canonical Fourier-mode matching J is asymptotically isometric for the quadratic energy with relative loss

    eta(a,p)=O(a^2 |p|^2).

This is the desired scalar analogue of U022's inheritance condition.

## 3. Ultrasoft window

Translate U022's dimensionless n-box threshold into physical variables. If the physical box scale is held fixed while n~L_phys/a, the largest global-ultrasoft lattice eigenvalue was

    lambda_g ~ n^-2 log^(2+2epsilon)n.

Multiplying by a^-2 converts to a physical momentum-squared threshold of order

    |p|^2 <= C log^(2+2epsilon)(1/a)

(up to the fixed physical-box normalization). Therefore on every matched ultrasoft mode,

    eta(a,p)
      <= C a^2 log^(2+2epsilon)(1/a).                    (U)

This tends to zero faster than any inverse logarithm.

For geometric refinement a_j=a_0 b^-j,

    eta_j <= C b^(-2j) j^(2+2epsilon),

so

    sum_j eta_j < infinity.                              (S)

Hence the free scalar ultrasoft dispersion inheritance is not merely vanishing but summably accurate.

## 4. Fixed-physical-time transfer deficit

For a free mode with Hamiltonian frequency E_a(p) (for a massless scalar, E_a=omega_a up to the chosen temporal discretization), the fixed-time transfer deficit is

    g_a(p)=1-exp[-t0 E_a(p)].

On momentum ranges where E_a and E_(a/b) are relatively close, the mean-value theorem gives

    |g_a-g_(a/b)|
      <= t0 |E_a-E_(a/b)|.

For small E, g(E)~t0 E, so relative deficit error is of the same order as relative energy error. For E bounded away from zero the denominator is even safer. Thus matched nonzero scalar modes inherit the fixed-time transfer deficit with summable relative discretization error under the same window, provided the temporal discretization itself has a comparable summable consistency estimate.

The exact zero mode is the vacuum/constant mode and is excluded from the centered sector. This statement does not address a scalar theory's own infrared masslessness; it only establishes consistency of matched mode energies across discretizations.

## 5. Important conceptual limitation

This result does **not** prove a mass gap for the free scalar model. Indeed the massless scalar continuum has no positive mass gap in infinite volume. What closes is only the U022 **inheritance-error** obligation: discretization does not introduce an O(1) mismatch for the matched ultrasoft modes.

This is an important sanity check for the architecture. A perfect inheritance map can faithfully transport a gapless spectrum. Therefore U019 still requires an independent positive starting/coarse deficit and a mechanism ensuring that the inherited physical Yang–Mills modes do not themselves approach zero energy in the infinite-volume/continuum limit.

The scalar calculation separates two logically different tasks:

1. **inheritance:** does coarse graining preserve the energy of an existing long mode? — yes, summably accurately here;
2. **mass generation:** is that long mode bounded away from zero physical energy? — no for the massless scalar, and still unproved for Yang–Mills.

## 6. Relation to the Yang–Mills target

A nonabelian analogue would need a canonical family of gauge-invariant or gauge-covariant long-wavelength degrees of freedom whose transfer energies can be compared between scales with a bound analogous to (I). Perturbative gluon Fourier modes are not physical gauge-invariant asymptotic states and, by themselves, cannot establish the Clay mass gap. Background-dependent covariant-Laplacian modes also raise spectral-stability and locality issues.

Thus U023 validates the **numerical scaling feasibility** of ultrasoft inheritance but simultaneously exposes the deeper unresolved question: where does a positive physical infrared energy scale enter nonperturbatively?

## 7. Outcome classification

Outcome: **proved for the free scalar dispersion model**.

Established:

    relative successive-scale dispersion error
      = O(a^2 |p|^2),

and on the U022 ultrasoft window

    eta_j = O(b^-2j j^(2+2epsilon)),
    sum eta_j < infinity.

Not established:

- a positive scalar mass gap (false for the massless model);
- Yang–Mills gauge-invariant mode matching;
- a nonperturbative positive coarse deficit;
- shell-output l2 aggregation in the interacting transfer form;
- reflection positivity, OS construction, or Yang–Mills mass gap.

## 8. Next bounded attempt

Return to the actual physical bottleneck rather than further optimizing scalar discretization. Identify a gauge-invariant finite-volume quantity whose positive lower transfer energy could serve as the initial/coarse infrared scale and is not forced to zero by perturbation theory. The cheapest candidate test is the smallest nontrivial Wilson-loop/plaquette sector in the Hamiltonian formulation: determine whether any rigorous finite-volume lower bound survives weak coupling in **physical units** after accounting for magnetic mixing. U003 already ruled out a global electric-relative perturbation, so the next attempt must use a localized/variational or representation-theoretic bound rather than treating the magnetic term as small.
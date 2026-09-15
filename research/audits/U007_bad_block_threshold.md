# U007 — correlated bad-block entropy threshold

Date: 2026-09-14.

**We have not solved the Yang–Mills problem yet.**

This unit turns the U006 failure into a quantitative target for a correlated large-deviation/RG estimate. It is a scaling theorem about a hypothetical bad-block bound, not a proof that Yang–Mills satisfies that bound.

## 1. Block geometry

Work in a fixed physical four-volume. Let the lattice spacing be a and choose a block with n(a) lattice sites per side, so its physical side is

    ell(a)=a n(a).

Parameterize

    n(a) ~ a^(-alpha),   0<=alpha<1,

so ell(a)~a^(1-alpha)->0 while the number of blocks scales as

    N_block(a) ~ ell(a)^(-4) ~ a^(-4(1-alpha)).

The endpoints have clear meanings: alpha=0 is essentially microscopic blocking; alpha approaching one gives blocks containing many lattice cells while their physical diameter shrinks very slowly.

## 2. Hypothetical collective action cost

Suppose a rigorous correlated estimate could prove for one bad block B that

    P(B bad) <= A(a) exp[-beta_W(a) E_B(a)],

where A(a) is sub-power in 1/a (or otherwise explicitly controlled), beta_W(a)=K log(1/a Lambda)+o(log(1/a)), and for SU(2)

    K=11/(3 pi^2).

Assume the collective dimensionless action cost grows like

    E_B(a) >= c n(a)^sigma

for some c>0 and sigma>=0. Then

    beta_W E_B >= K c a^(-alpha sigma) log(1/a)(1+o(1)).

If alpha>0 and sigma>0, this beats every fixed power of 1/a. Consequently a union bound over O(a^-4(1-alpha)) blocks tends to zero, provided the prefactor A(a) is not exponentially worse on the same scale.

Thus **any genuinely growing collective cost per bad block is qualitatively sufficient against polynomial block entropy**. The difficult mathematical task is proving such a cost for a useful gauge-invariant bad event under the interacting Wilson measure/transfer form.

## 3. Marginal logarithmic-cost case

The most delicate case is when the action cost does not grow as a positive power of n but only as

    E_B(a) >= c alpha

in the exponent coefficient after blocking, equivalently when the bad-block suppression has the form

    P(B bad) <= a^(K c alpha+o(1)).

Then the all-block union bound behaves as

    a^[-4(1-alpha)+K c alpha+o(1)].

It vanishes exactly when

    K c alpha > 4(1-alpha),

or

    alpha > 4/(4+K c).                                      (B)

Wolfram 15.0.1 independently simplified the exponent to `-4 + alpha (4+c K)`. For SU(2), if c=1 the threshold is

    alpha > 4/(4+11/(3 pi^2)) ~= 0.9150154.

If c=2 it is

    alpha > 6 pi^2/(11+6 pi^2) ~= 0.8433442.

So a merely logarithmic collective gain requires very large lattice blocks: n(a) grows almost as fast as 1/a, while their physical diameter ell(a)=a^(1-alpha) shrinks extremely slowly. This makes locality and OS control correspondingly harder.

## 4. Surface- and volume-cost regimes

For a four-dimensional block of n cells per side:

- a surface-type defect cost has sigma=3;
- a volume-type defect cost has sigma=4.

Either would dominate polynomial entropy for every fixed alpha>0. Even a linearly growing cost sigma=1 would suffice at the scaling level. Therefore the central question is no longer the raw number of blocks; it is whether a gauge-invariant definition of a bad block forces a collective action cost that grows with block size after accounting for gauge transformations, Bianchi constraints, flat/topological sectors, and boundary freedom.

A bad event defined as "there exists one bad plaquette inside the block" does **not** force growing collective cost; it reduces to U006. The event must encode a coherent obstruction—e.g. a positive density of large plaquette angles, a nontrivial contour of bad plaquettes, or a block holonomy/curvature norm that cannot be repaired by gauge choice without paying collective Wilson action.

## 5. Required estimate for U003 compatibility

Probability suppression alone still does not feed the U003 gap theorem. The actual target should be a transfer-form estimate. A useful bad-block decomposition must yield, at one fixed physical time t0,

    fine coercivity >= rho > 0,
    relative mixed coefficient kappa_j,
    coarse relative loss eta_j,

with

    sum_j (eta_j+kappa_j^2) < infinity,

and with the large-field contribution to these quantities bounded by the bad-block weight. The estimate must be proved independently of the desired mass gap or uniform clustering.

This identifies a concrete bridge: a contour/RG theorem must turn collective Wilson-action suppression into **quadratic-form** suppression of the coarse/fine transfer coupling, not merely a Gibbs probability statement.

## 6. Falsification criterion for the next route

Reject a proposed correlated localization mechanism if, after all gauge and boundary freedoms are included, its minimal action cost for a bad block remains O(1) as n->infinity and its entropy is polynomial in a with coefficient no better than U006. Such a mechanism cannot improve the continuum scaling enough.

Conversely, a proved cost c n^sigma with any sigma>0 would pass this first entropy test and justify deeper work on reflection positivity, transfer-form estimates and OS convergence.

## 7. Next executable step

Test a specific gauge-invariant bad-block definition: require at least a fixed fraction rho of plaquettes in a block to have class angle >=epsilon. At the purely deterministic level this forces Wilson action deficit at least rho N_p(B) [1-cos epsilon], i.e. a volume cost O(n^4). The next task is to determine whether the measure/entropy of configurations realizing that event can be bounded sharply enough, without treating plaquettes as independent and without losing the volume action gain to link-variable entropy or boundary conditions. That is the first concrete contour/large-deviation lemma to attempt.

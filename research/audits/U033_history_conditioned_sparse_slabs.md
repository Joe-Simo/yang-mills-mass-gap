# U033 — extensive sparse-link slabs conditioned on retained histories

Date: 2026-09-15. Base: private `Joe-Simo/yang-mills-mass-gap` commit `e2203c32d70fa7d227e2214c985991ca0399ba94` (U032).

**We have not solved the Yang–Mills problem yet.**

Evidence: self-reviewed finite-Wilson path-measure proof, a checked Birkhoff-contraction theorem, exact finite rational checks, and separately recorded Wolfram corroboration. No formal verification, independent expert review, novelty claim, unconditioned mass bound, or continuum construction.

## 1. Target and change of route

U032 proves an actual-vacuum one-step estimate with rate `tanh(sum_{e in I} beta_e)` for a discarded set I. Its extensive-set dependence is poor; arbitrary endpoint weights prevent replacing the sum by a maximum. U033 does NOT assert such a replacement for the U032 projection.

Instead, retain the entire history of the complementary spatial links through a slab, and choose I so that no spatial plaquette contains two of its links. Conditional on this history, the interior discarded variables split into separate one-dimensional time chains. The actual vacuum weights at the two endpoints can still couple all discarded links. They are retained exactly, not assumed independent.

The resulting theorem is complementary to U032: it bounds endpoint dependence CONDITIONAL ON THE FULL RETAINED HISTORY, not `||K^n Q_I||`, not `(Q_I K Q_I)^n`, and not the unconditioned transfer gap. A second theorem identifies precisely how its remainder sits inside the actual physical-time correlation operator.

The archive `Yang_Mills_U032_Research_Package.zip` was inspected and 73 missing files restored only within `/mnt/data/yang-mills-mass-gap`; two pre-existing files matched and none conflicted. All eight U032 manifest hashes matched before changing the current README. The remote head and raw U032 note/blob were checked. There is no local Git checkout or executable proof-assistant runtime; earlier mathematical and checker files are preserved. The supplied Yang–Mills prompt fixes the original universal target, private-write authority, and zero-spend boundary. No sibling project was used.

## 2. Exact Wilson path law

Keep U032's finite periodic spatial cubic graph, normalized product Haar measure mu, and conventions

    m(U)=exp[-beta_s W(U)/2],
    W(U)=sum_spatial_p [1-(1/2)ReTr U_p],
    K0(U,V)=m(U)m(V) product_e exp[-beta_e(1-u_e.v_e)].       (1)

All beta_e>0 and beta_s>=0 are finite, and u_e,v_e are unit quaternions. Let lambda0,psi be the actual positive Perron eigenpair, with integral psi^2 dmu=1. The stationary ground-state transformed transfer K acts on L2(pi), pi=psi^2 mu, and is positive, self-adjoint, Markov. Its gauge-invariant restriction is the physical transfer from U031–U032.

For n>=1, its EXACT stationary path measure is

    dP_n = lambda0^-n psi(U_0)psi(U_n)
           product_{t=0}^{n-1} K0(U_t,U_{t+1})
           product_{t=0}^n mu(dU_t).                         (2)

This follows by telescoping the ground-state transform; normalization is `lambda0^-n <psi,K0^n psi>=1`. No approximation to psi enters.

Take a spatial-link set I such that each spatial plaquette contains at most one member of I. Write R=E\I, l=|I|, and condition on

    Y_n=(U_{0,R},U_{1,R},...,U_{n,R}).

For each fixed retained history y and each interior time t, the spatial weight factorizes as

    exp[-beta_s W(U_t)] = c_t(y) product_{e in I} w_{e,t}^y(U_{t,e}),  (3)

where w is positive and continuous. Each plaquette involving e contributes only to that link's w; plaquettes involving no I link contribute to c_t. The no-two-in-a-plaquette hypothesis is exactly what justifies (3). Temporal factors of retained links are also constants under this conditioning.

Define the one-link kernel and the n-step conditional bridge kernel

    C_e(u,v)=exp[beta_e u.v],
    T_{e,n}^y=C_e M_{w_{e,1}^y} C_e ... M_{w_{e,n-1}^y} C_e.       (4)

There are n factors C_e. For n=1, T=C_e. M_w means multiplication by w. Constants exp(-beta_e) cancel from all normalized expressions.

After integrating all discarded INTERIOR-time links, the conditional joint law of the two discarded endpoints X=U_{0,I}, Z=U_{n,I} has density

    j_y(X,Z) proportional to a_y(X) b_y(Z)
                              product_{e in I} T_{e,n}^y(X_e,Z_e), (5)

with endpoint weights

    a_y(X)=psi(X,y_0)m(X,y_0),
    b_y(Z)=psi(Z,y_n)m(Z,y_n).

These weights generally do not factor over e. Formula (5) keeps that dependence. At every fixed regulator they are continuous and strictly positive.

## 3. Uniform conditional endpoint-contraction theorem

Set

    r_e=tanh(beta_e),
    theta_{I,n}=tanh(sum_{e in I} atanh(r_e^n)).                 (6)

For every retained history y and every square-integrable endpoint functions f(X),g(Z),

    |Cov_y(f,g)| <= theta_{I,n} sqrt(Var_y(f) Var_y(g)).         (7)

The bound is independent of beta_s and of the retained volume, but it still depends on l and beta_e through (6). In the uniform case beta_e=beta,

    theta_{I,n}=tanh(l atanh(r^n)) <= min(1,l r^n), r=tanh beta. (8)

For n=1 the coefficient is `tanh(l beta)`. The coefficient agrees numerically with U032 at one step, but the conditioning here includes BOTH retained endpoints and, for n>1, every intermediate retained slice. This is not an inequality comparing two identical U032 projections.

### Proof: one-column Hilbert diameter

For positive continuous functions on SU(2), use Hilbert's metric

    d_H(f,g)=log sup(f/g)-log inf(f/g).

Positive multiplication M_w is an isometry in this metric. The logarithmic cross ratio of C_e is

    log[C_e(u,v)C_e(u',v')/(C_e(u,v')C_e(u',v))]
          =beta_e (u-u').(v-v').                             (9)

Its maximum is 4 beta_e; antipodal aligned quaternions attain it.

For a continuous strictly positive kernel on a compact space with full-support measure, its projective diameter equals its maximum logarithmic cross ratio. The upper bound follows by integrating the cross-ratio inequality against positive functions. The reverse bound follows by concentrating positive continuous test functions near the two maximizing input points. Compactness and strict positivity allow the limit, including pointwise kernel ratios.

Birkhoff's exact contraction formula gives

    tau(C_e)=tanh(diam_H(C_e)/4)=r_e,
    tau(T_{e,n}^y) <= r_e^n.

Here tau is the Lipschitz coefficient in d_H; coefficients multiply under composition, and every M_w has coefficient one. Applying the SAME exact diameter/contraction relation to the composite positive kernel gives

    diam_H(T_{e,n}^y) <= 4 atanh(r_e^n).                     (10)

Using only a one-sided inequality `tau<=tanh(diam/4)` would not justify this inversion; the exact equality is a load-bearing source hypothesis, checked below. The cones here are the normal positive cones in C(SU(2)), with strictly positive functions as their interiors, which meet that theorem's hypotheses.

### Proof: correlated endpoints and L2 correlation

The endpoint multipliers in (5) cancel from every cross ratio, even when they correlate the discarded links. The log cross ratio of the product kernel is a sum, bounded by `4 sum_e atanh(r_e^n)` using (10).

U032 Section 3 proves the following compact-positive-kernel lemma: cross-ratio diameter Delta bounds maximal L2 correlation by tanh(Delta/4). Briefly, the likelihood-ratio bound gives that coefficient for both conditional Markov channels. Their roundtrip is a positive compact self-adjoint operator; its oscillation contraction bounds every nonconstant eigenvalue by the squared coefficient. The spectral theorem then bounds the centered conditional-expectation norm. This is why the coefficient in (7) is theta, not sqrt(theta).

Applying the lemma gives (7). The last inequality in (8) follows by iterating `tanh(a+b)=(tanh a+tanh b)/(1+tanh a tanh b)<=tanh a+tanh b` for nonnegative a,b. No tensorization of the unknown endpoint measure has been used.

### Extensive admissible geometry

On an even periodic spatial N^3 lattice, N>=4, choose direction-0 links based at x with x_1+x_2 even. A spatial (0,nu)-plaquette has its two direction-0 links at opposite transverse parity; other plaquettes contain none. Thus I is admissible and

    |I|=N^3/2=(1/6)|E|.

The construction includes a fixed positive fraction of the lattice links. It works at every time slice and is stable under reversal of the time interval. Selecting all direction-0 links would violate the spatial hypothesis. No claim that different color layers remain independent after integration is made.

## 4. Actual physical-time decomposition: what the bound does control

Let J_t map an endpoint function f in L2(pi) to f(U_t) in L2(P_n). Stationarity makes J_0,J_n isometries. Let Pi_n be conditional expectation in that path space onto sigma(Y_n). Define

    H_n=J_0* Pi_n J_n,
    E_n=J_0* (I-Pi_n) J_n.

The exact full correlation transfer decomposes as

    K^n=H_n+E_n.                                          (11)

For arbitrary endpoint f,g, the bilinear form of E_n is

    <f,E_n g>=E[Cov(f(U_0),g(U_n) | Y_n)]

with complex conjugation on f when necessary. Applying (7) history by history, then Cauchy–Schwarz over histories, gives

    ||E_n|| <= theta_{I,n} <= l r_*^n,
    r_*=max_{e in I} r_e<1.                               (12)

This is a full L2 operator-norm error bound, not a finite list of tested observables. It includes the true vacuum via (2). Both operators preserve the centered space: H_n 1=1 and H_n*1=1, while E_n 1=E_n*1=0. H_n is positivity preserving and a contraction, being a composition of such conditional-expectation/isometry maps. Reversal of the stationary reversible path fixes Y_n as an algebra and exchanges J_0 with J_n; hence H_n is self-adjoint. Positive semidefiniteness of H_n is NOT needed or claimed.

The stationary path law in (2) is that of the ungauge-averaged temporal-gauge kernel K0. It is invariant under the same spatial gauge transformation on every slice, and sigma(Y_n) is stable under this action. Consequently H_n and E_n preserve endpoint gauge-invariant functions. Equation (11) restricted to these functions refers to the physical K^n. This does not claim independent time-slice gauge invariance of the raw conditional kernel or replace it by a gauge-averaged product kernel.

Crucially, `H_n` changes with n and uses the FULL retained path. It has not been identified with powers of a single reduced Markov transfer. Also E_n need not be positive, unlike U030's kernels B D^k B*. No replacement of `Q K^n Q` by `(Q K Q)^n` occurs.

### All-time weighted remainder

For fixed graph/couplings and r_*<q<1, (12) gives

    sum_{n=M+1}^infinity q^-n ||E_n||
       <= l (r_*/q)^(M+1)/(1-r_*/q), M>=0.                (13)

This is a sum of errors in the sequence (11), not a Schur resolvent of an invented common D. It remains valid without computing any finite-time correlation prefix.

### The retained-history obligation

Write H_n^0 for H_n restricted to the entire centered physical space. If a separate argument proves

    ||H_n^0||+theta_{I,n} <= q0 < 1,                       (14)

then `||K^n|1-perp||<=q0` and the finite-regulator physical Hamiltonian gap at microscopic time step tau is at least

    -log(q0)/(n tau).

For a continuum conclusion one would still need a useful bound at fixed physical n tau, regulator/volume uniformity, the required reconstruction and Yang–Mills identification, and nontrivial finite-energy limiting states. None of those follows from (12). The unresolved term in (14) contains the retained collective dynamics, not merely a numerical integration error.

## 5. How slab depth changes the discarded-set dependence

For 0<epsilon<1, a sufficient depth for theta_{I,n}<=epsilon is

    n >= ceil[ log(l/epsilon)/(-log r_*) ].                (15)

At fixed temporal coupling, this grows logarithmically with l. This statement is about a HISTORY-CONDITIONED slab error; it does not improve U032's one-step norm on its original projection.

For large uniform beta, `-log(tanh beta)=2 exp(-2beta)(1+o(1))`, so this sufficient depth is of order `exp(2beta) log(l/epsilon)`. The sum-coupling estimate applied to a whole set as one undifferentiated column would instead involve exp(2l beta). Exact spatial factorization under retained-history conditioning is the new input, not an unproved independent-vacuum assumption.

As a scaling diagnostic ONLY, suppose tau=a, l<=C a^-d, and beta(a)=kappa log(1/a)+o(log(1/a)), with kappa>0. The sufficient physical depth is then

    a n=O(a^(1-2kappa+o(1)) log(1/a))

for fixed target epsilon. If kappa<1/2, this depth tends to zero. Equivalently, at any fixed positive physical time the bound `l r^n` tends to zero. This is not proof of an asymptotically free Wilson trajectory, nor evidence that H_n^0 contracts. For kappa>=1/2 this simple sufficient-depth estimate need not shrink; failure of an upper estimate is not a counterexample to physical decay.

## 6. Two executable controls

### Continuous SU(2), two time steps

For a single interior potential `w(z)=exp(h.z)`, h in R^4, direct Haar integration gives

    T_2(u,v)=Z(|beta u+beta v+h|),
    Z(s)=2 I_1(s)/s, Z(0)=1.                              (16)

This uses precisely U029's group integral and remains regular when the source vanishes. The checker encloses all four entries of selected cross ratios by positive rational series in the SQUARED source norm; no irrational square-root evaluation is necessary. Nine collinear cases use beta=1/2,2,6 and h0=0,beta,4beta; a tenth has non-collinear rational unit quaternions and h=(1/2,1,0,-1). Both a ratio and its reciprocal are certified below `[(1+tanh(beta)^2)/(1-tanh(beta)^2)]^2`, using rigorous exponential and Bessel tails. These are finite normalization/adversarial checks, not the all-history proof.

### Exact binary kernels with arbitrary weights

Use `c=[[4,1],[1,4]]`, whose projective coefficient is r=3/5. With one interior weight diag(t,1),

    T_2=[[16t+1,4t+4],[4t+4,t+16]],
    (17/8)^2 - T11 T22/(T12 T21)
       =225(t-1)^2/[64(t+1)^2]>=0.                       (17)

Equal interior weights attain the two-step single-column coefficient r^2=9/25. Two such columns have diameter coefficient `tanh(2 atanh(9/25))=225/353`, not 9/25, when arbitrary correlated endpoint weights are allowed. The checker verifies composition, product cross ratios, cancellation of correlated endpoint weights, and exact path conditional expectations. The binary model is a stress test of the positive-kernel machinery, not a Wilson theory.

## 7. Why conditioning cannot be dropped

Law of total covariance gives exactly

    Cov(f(U0),g(Un))
      = E Cov(f(U0),g(Un)|Y_n)
        + Cov(E[f(U0)|Y_n],E[g(Un)|Y_n]).                 (18)

Only the first term is controlled by (7). The second is precisely the explained-history contribution H_n. It can be large.

An all-parameter counterexample to discarding that second term is a product of two symmetric binary Markov transfers: retained coordinate rate sigma in (0,1), discarded coordinate rate r=3/5, both with uniform stationary measures. Then, writing J for averaging the discarded bit,

    H_n=K_retained^n tensor J,
    E_n=K_retained^n tensor [K_discarded^n-J],
    ||E_n||=r^n,
    ||H_n^0||=sigma^n.

The hidden error is small while sigma can approach one arbitrarily closely. Every finite sigma<1 has a unique vacuum and a strictly positive transfer spectrum. Thus history-conditioned decay alone does not imply a uniform full gap. The code also verifies (11)-(12) in a genuinely correlated, vacuum-weighted four-state example from U032, not only this independent example.

This is NOT a counterexample to Yang–Mills. It shows why (14) remains a real physical/mathematical obligation, and why shrinking the hidden error cannot be advertised as mass generation.

## 8. Source verification and computation provenance

- S. Gaubert and Z. Qu, *Dobrushin's ergodicity coefficient for Markov operators on cones*, arXiv:1307.4649v3, version 2014-11-01, Definition 5.5, Theorem 5.6 and Corollary 5.7. Exact HTML https://arxiv.org/html/1307.4649v3 was checked on 2026-09-15, including the exact equality in Theorem 5.6. The dictionary is the Banach space C(SU(2)), its normal cone of nonnegative functions, positive-kernel maps, and the log-cross-ratio diameter (9). The transfer-product use is an application of established Birkhoff machinery, not a new contraction theorem.
- U032 Section 3, pinned at the base above, supplies the direct compact-positive-kernel maximal-correlation proof. Its finite-regulator continuity/strict-positivity conditions remain valid for (5); its uniform constants do not require a uniform lower bound for the actual vacuum density.
- U029, unchanged in this project, supplies Z and positive-series tails. The external formula is the normalized SU(2) Haar integral, not a newly imported spectral estimate.
- CMI's Yang–Mills problem page was rechecked on 2026-09-15 and remains marked unsolved: https://www.claymath.org/millennium/yang-mills-the-maths-gap/ . This checkpoint neither proposes a complete candidate nor makes a prize claim.

The search for overlap used projective-metric positive-kernel and hidden-Markov terminology, followed by the exact Gaubert–Qu source. This is not a global novelty search. No claim of novelty is made for the proof mechanism or its Wilson application. The previously documented Consensus quota failure was not repeatedly reinvoked. Mathbox workflow instructions are not an independent review.

`checks/U033_history_conditioned_slab_checks.py` uses Python 3.13.5, SymPy 1.14.0 and exact integers/Fraction/rational matrices. Twelve focused tests passed. Geometry checks enumerate periodic N=4,6 spatial boxes. Positive binary-chain comparisons use 1..6 time steps, and product-kernel diameters use 1..3 columns at n=1,2,4. The path-space check enumerates all 4^(n+1) paths of the named four-state fixture at n=1..4; it does not sample or assert coverage beyond this fixture. Correlated endpoint weights and a deliberately invalid cofacial set are included.

The continuous-SU(2) two-step certificates use 160 terms of positive series with explicit remaining tails. Decimal endpoints are rounded outward from exact rational intervals. Binary slab-depth examples use l=1,2,16,256,4096, r=3/5 and epsilon=1/100; these are coefficient examples, not Wilson numerical measurements. All twelve prior U032 tests were rerun into NEW U033 evidence files. No earlier evidence was overwritten.

Wolfram 15.0.1 independently returned (17), six exact equal-weight power residuals zero, coefficient 225/353, the nonnegative aggregation residual a b(a+b)/(1+a b), and six zero weighted-tail residuals in a clean 20-second-cap algebra call. This checks the submitted finite identities, not the entire Wilson theorem.

Compilation and indentation checks passed. No ruff, mypy, pyright, or Lean executable/module was available; no static-analysis or formal-verification success is claimed. The main and prior suites had 45-second wall caps with cooperative single-thread settings and both exited successfully. Hashes, test output and commands are in `evidence/U033_manifest.json` and companion files.

## 9. Self-audit and next mathematical obligation

Primary verdict: **proved after the explicit finite-Wilson, spatially noncofacial-set, full-retained-history restriction**.

Passed: exact stationary path law and true vacuum; extensive admissible geometry; interior-time conditional factorization; preservation of correlated endpoint weights; projective contraction with the correct inverse equality; L2 endpoint correlation; full-operator remainder (11)-(12); gauge-invariant endpoint restriction; all-time weighted remainder; arbitrary-slow retained-sector control example; microscopic/physical unit distinction.

Unproved: a useful estimate of `||H_n^0||` uniformly in cutoff and volume; repeated elimination of additional spatial color layers after integrating the histories used in this proof; a finite-dimensional or short-memory state replacing the full retained path; reconstruction and nontriviality in the joint limits; the mass gap and group-universal target.

Next executable question: apply the decomposition to two different noncofacial color layers and estimate the angle/overlap between their retained-history conditional-expectation ranges in the same stationary Wilson path measure. A single history range can carry all slow retained motion; showing that several such ranges have no common almost-invariant CENTERED physical mode would be a genuinely new input. Do not infer this from the fact that their exact intersection contains only constants, from link count, or from U033's one-layer error alone. A conditional-variance/angle bound must be proved in this actual path measure and then connected to (14).

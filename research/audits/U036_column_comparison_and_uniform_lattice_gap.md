# U036 — resummed time-column comparison and a volume-uniform restricted Wilson gap

Date: 2026-09-15. Base: private `Joe-Simo/yang-mills-mass-gap` commit `1ce1ba4174db4f9dc568bd14cdb7ad95f0f1e6d4` (U035).

**We have not solved the Yang–Mills problem yet.**

Evidence: self-reviewed finite-regulator proof using an established block-comparison theorem, with an explicit continuous-SU(2) dictionary and exact finite algebra checks. No formal verification, independent expert review, novelty claim, weak-coupling continuum result, or full all-group construction.

## 1. Decision and exact scope

U035 cancelled disconnected source supports at every order but did not bound all surviving connected coefficients. A direct Cauchy estimate in its sum-of-source-size ball loses the active volume. This unit pursues the alternative explicitly allowed there: bound the actual connected susceptibility at a nonzero, possibly homogeneous, spatial background. The method sums complete conditional time chains and repeated spatial influences; it is NOT a truncation of the source expansion and does NOT prove analyticity of the logarithmic vacuum in a volume-uniform complex polydisc.

The resulting sufficient domain contains arbitrarily many active spatial plaquettes. Its bound no longer worsens with the number of plaquettes, but the spatial coupling must be small compared with the inverse temporal coupling. This is a restricted small-spatial-coupling regime, not the isotropic weak-bare-coupling trajectory. Volume-uniform lattice gap results in restricted regimes are established mathematical territory; no priority claim is made for this proof or its conservative constants.

Only the assigned folder was used. The U035 archive restored 107 missing files; the two existing mathematical files matched, and nothing was overwritten. All seven U035 primary manifest files matched before work. The remote head was pinned above; the standalone Yang–Mills prompt was retrieved from the conversation. No local Git checkout, AGENTS file, or executable Mathbox ledger was present. Prior mathematical files, checkers, and evidence remain unchanged; README is intentionally updated, with its prior bytes retained in Git and the supplied archive.

## 2. The restricted theorem

Let E be the links of a finite periodic spatial cubic lattice of side N>=4 (the inherited even-N family is included). Each elementary spatial plaquette has four distinct links; each link is on four plaquettes. Open subgraphs with the same degree bounds also satisfy the estimates. Use normalized product Haar measure on SU(2)^E and the U035 convention

    w_p(U) = ReTr(U_p)/2,               |w_p| <= 1,
    V_s(U) = sum_p s_p w_p(U),          0 <= s_p <= s0,
    C_beta = tensor_e C_beta,e,         beta=beta_t>0,
    T_s = exp(V_s/2) C_beta exp(V_s/2).

On one link, C_beta has Markov density

    k_beta(U,V) = exp[beta ReTr(U V*)/2] / Z(beta),
    Z(beta) = 2 I_1(beta)/beta.

Let lambda_s, psi_s>0 be the top eigenpair of T_s, with ||psi_s||_2=1. Set pi_s=psi_s^2 mu and let K_s be the ground-state transformed normalized transfer. At the specified microscopic time tau>0, its physical restriction defines H_s=-log(K_s)/tau. The kernel is continuous, strictly positive and symmetric. Its operator positivity follows from its strictly positive character-convolution eigenvalues and positive multiplication congruence. The top eigenfunction is unique, strictly positive and gauge invariant. These facts cover the actual finite vacuum, not a trial state.

Define

    b = ceil(3 max(1,beta)),
    alpha = log(4/3)/b.

**Theorem.** If

    b s0 <= 1/192,                                             (1)

then on the ENTIRE centered physical Hilbert space,

    ||K_s||_centered <= exp(-alpha),
    Delta_s >= log(4/3)/(b tau).                               (2)

The constants do not depend on N or the number of active plaquettes. In fact the covariance proof also controls the centered full link-coordinate transfer, prior to restriction to gauge-invariant functions. For every fixed plaquette p the exact stationary connected correlations obey the absolute-susceptibility bound

    sum_q sum_(t in Z) |Cov_pi,path(w_p(U_0),w_q(U_t))|
       <= 16(4b-1)/[1-12 s0(4b-1)] < 256b/3.                 (3)

The last strict inequality can be weakened to <= without affecting the theorem. Bound (3) holds at the nonzero backgrounds in (1), not only at s=0. Proofs follow. Neither (1) nor (2) is asserted outside its domain.

## 3. A complete temporal-kernel bound, without a representation cutoff

For integer l>=0, the spin-l/2 convolution multiplier is

    a_l(beta) = I_(l+1)(beta)/I_1(beta),       a_0=1.

The kernel of b convolution steps is

    k_beta^[b](U,V) = sum_(l>=0) (l+1) a_l(beta)^b chi_(l/2)(UV*).

To bound the whole series, put R_nu=I_(nu+1)/I_nu for nu>=1. The normalized integral with density proportional to exp(beta cos theta) sin(theta)^(2nu) gives

    R_nu = E_nu cos theta > 0,
    R_nu' = Var_nu(cos theta) > 0.

The Bessel derivative recurrences give, independently,

    R_nu' = 1 - (2nu+1)R_nu/beta - R_nu^2.

Consequently

    R_nu < sqrt[1+((nu+1/2)/beta)^2]-(nu+1/2)/beta
          = exp[-asinh((nu+1/2)/beta)].                       (4)

This upper bound uses positivity of the derivative, not a large-order or large-beta asymptotic. For a>0, the function beta asinh(a/beta) is increasing in beta: its derivative is h(a/beta), where

    h(x)=asinh(x)-x/sqrt(1+x^2),
    h(0)=0,  h'(x)=x^2/(1+x^2)^(3/2)>0.

Since asinh(3/2)=log[(3+sqrt(13))/2]>log 3, the definition of b gives

    b asinh(3/(2beta)) > log 27

both for beta>=1 and for 0<beta<=1. Multiplying (4) for nu=1,...,l proves

    a_l(beta)^b <= 27^(-l),        l>=1.                     (5)

Using |chi_(l/2)|<=l+1, the full, uniformly convergent character tail is bounded by

    |k_beta^[b](U,V)-1|
      <= sum_(l>=1) (l+1)^2/27^l
       = 709/4394 < 1/4.                                    (6)

The equality follows from sum_(l>=0)(l+1)^2 x^l=(1+x)/(1-x)^3. This is an analytic all-character bound, not extrapolation from finite character checks. In particular 3/4 <= k_beta^[b] <= 5/4 for every U,V and every beta>0.

## 4. Conditional columns with the actual spatial interactions

First work on an arbitrary finite OPEN time interval t=-M,...,M. Its probability is

    dnu_(M,s) proportional to
      exp[sum_(t=-M)^M V_s(U_t)]
      product_(t=-M)^(M-1) product_e k_beta(U_(e,t),U_(e,t+1))
      product_t dmu(U_t).                                    (7)

There is no correlated, postulated vacuum boundary density in (7). Its true-vacuum limit is taken only after uniform-in-M estimates are proved below. The equal endpoint spatial weights in (7) are convenient: in transfer notation its endpoint vectors are exp(V_s/2), not the vacuum.

Condition on all columns except a fixed spatial link e. Its exact conditional law is a one-dimensional Markov chain with positive one-site factors exp(h_t(U)), where

    h_t(U) = sum_(p containing e) s_p w_p(U; fixed neighboring links),
    |h_t(U)| <= H0 := 4s0.                                  (8)

This holds for every surrounding configuration, including frustrated ones. It uses no independent-plaquette assumption, saddle expansion, gauge fixing of the spatial links, or Gaussian approximation.

A b-step unnormalized column kernel, including only its b-1 internal site factors, satisfies pointwise

    exp[-(b-1)H0] k_beta^[b](U,V)
       <= M_h(U,V)
       <= exp[(b-1)H0] k_beta^[b](U,V).                       (9)

Positive factors at its two endpoints can be separated and do not change cross ratios. Any remaining past/future message has this endpoint-factor form, even if it is large or sharply concentrated.

### Normalized-tilt lemma and the bridge contraction

If a probability is reweighted by exp(f), with osc(f)<=d, its total variation distance from the original probability is <=tanh(d/4). One direct proof bounds the likelihood ratio between its minimum and maximum and maximizes the resulting two-endpoint expression; its maximum is (sqrt(R)-1)/(sqrt(R)+1), R=exp(d).

If a positive kernel lies between m and M pointwise, two rows after multiplication by ANY common positive endpoint weight have logarithmic likelihood-ratio oscillation at most 2log(M/m). Their total variation distance is therefore at most (M/m-1)/(M/m+1).

Apply this to (6) and (9). Here

    M/m <= (5/3) exp[2(b-1)H0]
         <= (5/3) exp(1/24)
         <= (5/3)(24/23) = 40/23,

where (1), H0=4s0 and exp(x)<=1/(1-x) for 0<=x<1 were used. Thus every b-step conditional forward or backward column transition has contraction at most

    (40/23-1)/(40/23+1) = 17/63 < 1/2.                       (10)

The arbitrary endpoint messages are not deleted: they cancel from the likelihood oscillation used by the normalized-tilt lemma. This is stronger than repeatedly using the microscopic worst-case coefficient tanh(beta), whose useful time scale can be exponentially large in beta.

## 5. A joint path coupling, not just marginal mixing

Suppose only the site factor at time u in a conditional column is changed by delta h, with osc(delta h)<=d. The marginal at u is tilted by precisely exp(delta h); conditional past and future GIVEN its value at u are unchanged. Couple the two values at u maximally. The initial mismatch probability is at most tanh(d/4).

Starting there, couple successive b-step endpoint transitions using (10), in each time direction. Once equal, use the identical conditional path thereafter. Fill the intermediate sites with the corresponding Markov bridges. If the two states at the start of a block agree, these bridges and their continuations can also be identical. If they differ, bound intermediate mismatches by one. This constructs ONE coupling of the complete two paths for which, simultaneously at every t,

    P(U_t != U'_t) <= tanh(d/4) g_b(t-u),
    g_b(v) := 2^(-floor(|v|/b)).                             (11)

The floor and the unsuppressed first b-1 sites are intentional. Replacing (11) with an unjustified microscopic exponential would improve the constants falsely. Endpoint partial blocks also satisfy (11).

Now change one OTHER spatial link f at a single time u. Each common plaquette changes h_u by a function of oscillation <=4s_p. Therefore (11) and tanh(x)<=x give a coupled update of column e with mismatch bounded by

    A_ef g_b(t-u),
    A_ef := sum_(p containing both e,f) s_p,  A_ee=0.          (12)

Changing a coordinate inside the updated column does not affect its conditional law. Since each e is on four plaquettes, each with three other links,

    A_ef=A_fe>=0,             sup_e sum_f A_ef <= D:=12s0.    (13)

This bound retains all shared-plaquette interactions. It is not a product-vacuum argument.

## 6. Sum repeated influences at all orders in the real measure

Index individual sites by i=(e,t), even though an update replaces an ENTIRE finite time column. Define nonnegative matrices

    G_(e,t),(f,u) = 1_(e=f) g_b(t-u),
    J_(e,t),(f,u) = A_ef g_b(t-u),
    L = (I-J)^(-1) G = sum_(k>=0) J^k G.                    (14)

These are influence majorants, not physical transfer matrices or a finite-memory model.

The block-comparison theorem of Rebeschini–van Handel, Theorem 2.4, applies with: sites E times the finite time interval; discrete site metric 1_(x!=y); blocks equal to the complete columns; weights w_J=1; W=I; their R bounded entrywise by our J. Finite continuous conditional densities give the required kernels and locality. Their coupled-update hypotheses are provided by the single changed-site path coupling (11)-(12). The convergence condition follows from ||J||_infinity<1, shown below. This also avoids any unsupported assumption that separately chosen one-site marginal couplings form a joint path coupling.

For clarity, the finite comparison can also be seen by random-scan column updates. Starting with any coupling of the two invariant probabilities, its coordinate mismatch vector z after an update satisfies

    z_next <= (1-1/|E|)z + (J z + b_source)/|E|.

Iterate and use ||J||_infinity<1 to obtain the bound (I-J)^(-1)b_source. This auxiliary sampling argument compares probabilities; its update time is NOT the physical Euclidean time tau.

Let F,G0 be bounded real observables, each supported at a single time, with arbitrary finite spatial support. Let osc_i F denote the maximum change under changing coordinate i alone. Reweight (7) by exp(eta G0). For an updated column e, this changes just its factor at the source time, with oscillation <=|eta| osc_e G0. Therefore its source mismatch vector is <=|eta| G osc(G0)/4. Applying the comparison theorem, dividing by |eta| and differentiating the finite compact integral at eta=0 proves

    |Cov_(nu_(M,s))(F,G0)|
       <= (1/4) sum_(i,j) osc_i(F) L_ij osc_j(G0).             (15)

There is no Taylor truncation in the background s. Inhomogeneous small s_p are allowed on arbitrarily many spatial plaquettes. The Neumann series in (14) bounds repeated influence paths at all lengths; it is not an identification with the individual logarithmic-vacuum Taylor coefficients of U035.

### Time weights and convergence

For alpha=log(4/3)/b,

    W0 := sum_(v in Z) g_b(v) = 4b-1,
    Walpha := sum_(v in Z) exp(alpha|v|) g_b(v)
      = 2 [sum_(u=0)^(b-1) exp(alpha u)]/[1-exp(alpha b)/2]-1
      <= 8b.                                                (16)

On any finite interval these sums only decrease. Since weighted row-sum norms with exp(alpha|t-u|) are submultiplicative,

    ||J||_(alpha,row) <= D Walpha <= 1/2,
    ||L||_(alpha,row) <= Walpha/(1-D Walpha) <= 16b.           (17)

In particular ||J||_infinity<=12s0(4b-1)<1/4. This establishes all convergence hypotheses of the comparison step rather than assuming them.

For F at time zero and G0 at time n, (15)-(17) imply

    |Cov(F(U_0),G0(U_n))|
      <= 4b ||osc F||_1 ||osc G0||_infinity exp(-alpha n).     (18)

All constants are independent of temporal interval length M and spatial volume, apart from the explicitly displayed observable support. That support dependence does not weaken the common exponential rate.

For a fixed elementary plaquette p, sum (15) over every spatial plaquette q and every source time. Each link is in four plaquettes, and osc_e w_q<=2. Summing source oscillations gives at most 8 per link-time site. Since ||osc w_p||_1<=8,

    sum_(q,u) |Cov(w_p(U_0),w_q(U_u))|
       <= 16 W0/(1-D W0).                                  (19)

The right side is at most its value at D=1/(16b), and

    256b/3 - 16(4b-1)/[1-(4b-1)/(16b)]
       = 1024b/[3(12b+1)] > 0.

This proves the asserted susceptibility constant, including absolute values. No ferromagnetic sign assumption is used.

## 7. Passage to the actual vacuum and the entire physical spectrum

Fix the spatial graph FIRST. In (7) the endpoint vector in transfer notation is m_s=exp(V_s/2)>0. For example its normalization over 2M steps is <m_s,T_s^(2M)m_s>. Because <m_s,psi_s>>0 and the finite positive compact transfer has a simple top eigenvalue, sending both endpoints to infinity gives the actual stationary path law of K_s and pi_s for every fixed finite collection of central times.

This uses only finite-graph Perron isolation to identify the limit. No uniform gap is assumed in taking it. Bounds (18)-(19) were already uniform in M, so they pass to these true-vacuum correlations. For the absolute time sum use finite sums first and then monotone convergence/Fatou. Arbitrary correlated true-vacuum endpoints were never replaced by a product measure inside a stationary formula; instead the stationary formula is obtained as the exact central limit of finite free-end slabs.

For any bounded centered real gauge-invariant f on the finite spatial configuration space,

    <f,K_s^n f>_pi <= C_f exp(-alpha n),
    C_f=4b ||osc f||_1 ||osc f||_infinity < infinity.           (20)

The left side has positive spectral measure on [0,1] because K_s is a positive self-adjoint operator. If this measure assigned nonzero weight above exp(-alpha), (20) would fail for large n. Thus its support lies in [0,exp(-alpha)]. Bounded gauge-invariant functions are dense in the physical L2 space, and the same conclusion holds for the entire centered physical space. Equivalently one can use the bounded continuous eigenfunctions of the compact finite-graph transfer. Taking -log at the stated physical time tau proves (2).

This is an energy gap ABOVE THE TRUE GROUND STATE. It is not a Ritz lower bound, a Hessian eigenvalue, or a spectral gap of the auxiliary column-update sampler. No physical states have been omitted by imposing separate-plaquette class functions. Gauge invariance of T_s, its vacuum and the physical restriction is unchanged.

At each finite graph the U035 susceptibility identity now has an absolutely summable right side throughout (1). Therefore (19) controls the response of <w_p> to homogeneous spatial activation, as well as to bounded inhomogeneous source changes, without a factor equal to the total active volume. This discharges a restricted version of U035's arbitrary-background response alternative. It does NOT prove its requested volume-uniform complex analyticity or an all-order bound on each connected vacuum-potential coefficient.

## 8. Sharp scope audit and the obstruction that remains

A simple, slightly weaker version of the domain and gap is

    s0 <= 1/[768 max(1,beta_t)],
    Delta >= log(4/3)/[4 max(1,beta_t) tau].                   (21)

It follows from 3max(1,beta)<=b<=4max(1,beta). The sharper integer-b statement is (1)-(2). At beta_t=1/2,2,8,32,128 the respective b are 3,6,24,96,384, and the allowed spatial upper bounds are 1/576,1/1152,1/4608,1/18432,1/73728.

This improves the DOMAIN SCALING of a raw one-step total-variation estimate. That simpler estimate uses g(v)=tanh(beta_t)^|v| and demands 12s0 exp(2beta_t)<1. The blocked proof replaces that exponential loss by a condition of order s0 beta_t small. It does not remove the required smallness.

On the isotropic Wilson weak-coupling sequence, s0=beta_t=beta tends to infinity. Then b s0>=3beta^2, which violates (1). A positive fixed-regulator, volume-uniform bound in (1) cannot be extrapolated along that trajectory. Also, if tau or the spatial lattice spacing is varied, (2) must be converted using the actual regulator/coupling dictionary; holding a favorable parameter fixed is not a continuum construction.

No nontrivial four-dimensional continuum limit, required short-distance Yang–Mills identification, or all-compact-simple-group result has been proved. An infinite-volume lattice limiting construction could be developed from these estimates, but it would still be a fixed-cutoff restricted-coupling result. No such limiting construction is claimed here without its separate state/observable audit.

The remaining physics is not a small correction to a completed solution: the controlled domain has to be connected to a nonperturbative weak-coupling continuum regime. A meaningful next attempt is a block-version of (9)-(13) for an INTERACTING spatial reference, retaining physical cycle variables, with a fluctuation/influence budget at physical scales. Simply changing b, deleting the connected terms, or improving the displayed numerical constants cannot justify that passage.

## 9. Sources and exact verification

Primary sources checked 2026-09-15:

- Patrick Rebeschini and Ramon van Handel, *Comparison Theorems for Gibbs Measures*, arXiv:1308.4117v1, 2013-08-19, subsequently J. Stat. Phys. 157 (2014), 234-281, DOI 10.1007/s10955-014-1087-7. Theorem 2.4, Definitions 2.2-2.3, and Sections 3.2-3.3 were read in the author preprint HTML. The source permits finite blocks, coupled updates, and nonnegative matrix influence majorants; it is not a Yang–Mills theorem. The exact dictionary and verification of its hypotheses are in Section 6 above. Source: https://arxiv.org/html/1308.4117v1 . The core comparison is known mathematics; the scalar matrix series in (14) should not be represented as a new theorem.
- NIST DLMF 10.32.2 and 10.29.1-2: normalized I_nu integral and derivative recurrences. These are used in Section 3 for nu>=1 and beta>0. Positivity, the Riccati bound, the all-character estimate, and constants (4)-(6) have the direct displayed derivations; no uniform asymptotic expansion is imported. Sources: https://dlmf.nist.gov/10.32 ; https://dlmf.nist.gov/10.29 .
- The current CMI Yang–Mills page was checked and still labels the problem unsolved: https://www.claymath.org/millennium/yang-mills-the-maths-gap/ . No external contact, submission, public repository change, purchase, or asynchronous execution was initiated.

Discovery also located weakly interacting quantum-lattice stability papers and anisotropic/linked-cluster work. Their abstracts were not substituted for a theorem about this finite-temporal Wilson transfer. No broad novelty search is claimed. Consensus's documented quota failure was not repeated. Mathbox provides a workflow, not an independent mathematical authority.

The focused checker has 12 tests with exact SymPy/Fraction decisions. The all-character geometric tail is summed exactly, with no finite representation cutoff. The real-space count covers N=4,6,8; the universal incidence argument is four plaquettes times three other edges. Binary time chains with arbitrary positive site factors test local-tilt propagation, not SU(2) physics. A 1024-configuration two-column binary fixture tests the covariance comparison with nonzero spatial interaction; it is explicitly not Wilson data. Exact finite matrices verify the inverse influence identity and weighted time-tail formula. Boundary/invalid-domain controls reject zero beta and divergent weighted tails.

The initial run passed 11 tests; one expected susceptibility-identity denominator in test 11 was mistyped as 48b+1 rather than 12b+1. Its unmodified log and hash are retained, the exact identity was recomputed, and the checker was corrected. The bound 256b/3 and the proof were not changed by this repair. The rerun passes all 12. Wolfram separately corroborated the zero Riccati and monotonicity residuals, tail 709/4394, bridge coefficient 17/63, weighted influence 1/2, and susceptibility slack 1024b/[3(1+12b)], without warnings. Agreement on these inputs is not independent expert verification of the theorem.

All twelve U035 checks were rerun successfully into new evidence without changing prior files. Compilation and indentation checks passed. Executable and module checks found no ruff, mypy, pyright, or Lean; static type/lint and formal checks could not be run. Exact commands and exit codes are recorded in the manifest and validation log.

## 10. Self-review verdict and handoff

Primary verdict: **proved after the explicit SU(2), fixed-regulator, small-spatial-coupling restriction (1)**; self-review only.

Passed: entire temporal representation tail; beta-dependent block scale; pointwise interacting-column bridge bounds; preservation of arbitrary endpoint messages; a joint full-path coupling; correct multi-site block-comparison hypotheses; summation at all influence lengths; actual-vacuum limit without a presumed uniform gap; dense physical-observable spectral inference; absolute susceptibility without a volume factor; correct distinction between sampler time and physical time.

Not proved: the all-order complex logarithmic-vacuum coefficient norm originally proposed in U035; a comparison about a strong spatially interacting reference; a route into isotropic weak coupling; the joint continuum/infinite-volume construction with nontrivial finite physical excitations; every group in the official target.

Next executable check: retain an interacting finite spatial block as a reference, and identify whether its physical-cycle conditional transfer admits an analogue of (6) on a physical time scale without paying its whole boundary action. Track the covariance/response term and compare to the connected-cycle channels in U035. A product-column proof with s0 beta_t small is now available as a benchmark, not as permission to extrapolate it.

# U032 — true-vacuum conditional contraction and a fixed-set Wilson memory bound

Date: 2026-09-15. Base: private `Joe-Simo/yang-mills-mass-gap` commit `aee6a18c4ccdb392fcfc412b128e36b545c92cf2` (U031).

**We have not solved the Yang–Mills problem yet.**

Evidence: self-reviewed finite-regulator operator proof, an established positive-kernel contraction mechanism with an explicit Wilson dictionary, exact rational/polynomial checks, and separately labeled Wolfram corroboration. No formal verification, independent expert review, novelty claim, continuum construction, or scale-uniform physical mass bound.

## 1. Target and what changes

U031 isolated a weighted long-time memory condition but did not derive its tail from the Wilson dynamics. This unit proves such a tail for a specified projection: discard a fixed set of spatial link coordinates and retain every other coordinate, with conditional expectation taken in the ACTUAL finite-volume vacuum measure. The coefficient depends on the total temporal coupling on the discarded links, not the number of retained links or the spatial coupling. This is not a momentum-shell projection, an extensive-decimation estimate independent of discarded-set size, or a full spectral-gap bound.

The route is different from fitting a finite correlation list: the positive temporal kernel bounds conditional cross ratios at every surrounding configuration, so its all-time consequence has a structural proof. Unknown positive vacuum weights cancel from those ratios. They are not approximated by Haar, Gaussian, or isolated-plaquette weights.

The assigned folder and supplied U031 archive were inspected; 60 missing files were restored without overwriting existing files, two existing entries matched, and all eight U031 manifest hashes matched before work. The remote head was pinned above. No local Git checkout, applicable AGENTS file, or executable Mathbox ledger was found. Earlier proof/checker files remain unchanged; README is the sole older manifest-covered file intentionally updated for continuity. Its current-status view is compacted; the full prior entries remain in the pinned parent revision and their unchanged mathematical records. No sibling project was accessed. The original Yang–Mills prompt, private-write authorization, zero-spend boundary, and full existence-and-gap target are unchanged.

## 2. Exact finite-regulator setup and projection

Use the finite periodic spatial cubic graph and complete link configuration space from U031 Section 2. Put X=SU(2)^E with normalized product Haar measure mu. For beta_s>=0 and beta_(t,e)>0, set

    m(U)=exp[-beta_s W(U)/2],
    W(U)=sum_spatial_p [1-(1/2)ReTr U_p],
    K0(U,V)=m(U)m(V) product_e exp[-beta_(t,e)(1-u_e.v_e)].       (1)

Here u_e,v_e are unit quaternions in R^4 and u_e.v_e=(1/2)ReTr(U_e V_e*). Uniform beta_(t,e)=beta_t recovers U031. All parameters and the graph are finite in this theorem.

The continuous strictly positive symmetric kernel K0 is also positive as an operator: the temporal character-convolution coefficients are positive and multiplication by m gives a positive congruence. As established directly in U031, its unique normalized top eigenfunction psi is continuous, strictly positive, and gauge invariant. Its eigenvalue is lambda0>0. Define

    pi(dU)=psi(U)^2 mu(dU),
    (Kcal f)(U)=[lambda0 psi(U)]^-1 int K0(U,V)psi(V)f(V)mu(dV).

Then Kcal is a positive self-adjoint Markov contraction on L2(pi). Its restriction to gauge-invariant functions is the physical transfer after the ground-state transform. The ungauge-averaged K0 is deliberately used in (1): it commutes with the gauge action, so its restriction agrees with the gauge-projected physical transfer, while its product temporal factorization is still visible. We do not assume that a gauge-averaged integral kernel itself has the cross-ratio factorization below.

Let I be a nonempty subset of spatial links to be discarded, R=E\I, and define

    P_I f = E_pi[f(U) | U_R],       Q_I=I_operator-P_I,
    b_I=sum_(e in I) beta_(t,e),    r_I=tanh(b_I)<1.             (2)

P_I is the actual vacuum-weighted conditional expectation, not a Haar average. It is an orthogonal projection preserving constants. Gauge transformations act separately on retained coordinates and preserve pi; conditional expectation therefore commutes with the gauge action. In particular P_I and Q_I preserve the physical subspace. On invariant functions its range is precisely the square-integrable invariant retained-coordinate algebra.

### Fixed-set contraction theorem

For every f in L2(pi),

    <f,(I_operator-Kcal^2)f>_pi
       >= (1-r_I^2) ||Q_I f||_pi^2.                            (3)

Consequently

    ||Kcal Q_I|| <= r_I,
    0 <= Q_I Kcal Q_I <= r_I I_(range Q_I).                     (4)

These constants are independent of total graph size and beta_s. In the uniform case they depend on |I| beta_t; for one discarded link r_I=tanh(beta_t). Their deterioration as beta_t or |I| grows must be retained.

## 3. Positive-kernel correlation lemma: direct proof

Let (X,Y) have a strictly positive continuous joint density on compact spaces of the form

    j(x,y) proportional to a(x)b(y)k(x,y),

with positive continuous factors. Suppose the logarithmic cross ratio obeys

    |log[k(x,y)k(x',y')/(k(x,y')k(x',y))]| <= Delta           (5)

for all arguments. Set c=tanh(Delta/4). Then, for every square-integrable h(X),

    Var(E[h(X)|Y]) <= c^2 Var(h(X)).                           (6)

Here variances use the normalized marginals of j. The same bound holds after exchanging X and Y.

**Likelihood-ratio step.** For probability laws P,Q with likelihood l=dP/dQ satisfying 0<a0<=l<=b0 and E_Q l=1, assume a0<1<b0; equality endpoints are handled by continuity. Convexity of |l-1| gives

    TV(P,Q) <= (b0-1)(1-a0)/(b0-a0)
             <= (sqrt(b0)-sqrt(a0))/(sqrt(b0)+sqrt(a0)).      (7)

The second inequality follows from the exact nonnegative difference

    (sqrt(b0)-sqrt(a0))^2-(b0-1)(1-a0)
       = (sqrt(a0 b0)-1)^2.

If the oscillation of log l is at most Delta, b0/a0<=exp(Delta), so the last bound is c. Identical laws have TV zero.

For two conditional Y-laws given x and x', the endpoint factor b(y) cancels from their likelihood ratio, and conditional normalizations contribute only a y-independent constant. Equation (5) bounds its log oscillation by Delta. The forward channel therefore has Dobrushin coefficient at most c. The reverse channel has the same bound, by the same argument; no marginal lower-density constant is needed.

**From oscillation to L2.** A Markov channel with Dobrushin coefficient delta contracts the oscillation sup h-inf h by delta, by integrating against the difference of two conditional laws. The roundtrip X->Y->X therefore contracts oscillation by c^2. On L2 of the X marginal this roundtrip is T* T, where Th=E[h(X)|Y]. It is compact, positive and self-adjoint. Every eigenfunction with nonzero eigenvalue is continuous, since its kernel is continuous on a compact set and the fixed-regulator marginal density is positive. For a nonconstant real eigenfunction h with eigenvalue z, the oscillation estimate gives z<=c^2. Its only constant direction has eigenvalue one; the same estimate excludes another eigenfunction at one when c<1. The compact self-adjoint spectral theorem now gives ||T|| on centered functions <=c. This proves (6). Complex functions follow by applying the quadratic estimate to real and imaginary parts.

Compactness is used only at each fixed regulator to justify this elementary spectral proof. No uniform lower bound on a, b, or the marginals is claimed. The numerical constant in (6) is c^2, not c: bounding BOTH conditional channels is essential to this derivation.

## 4. Application to the actual Wilson vacuum

The stationary two-slice joint law for Kcal has density

    J(U,V)=[psi(U)K0(U,V)psi(V)]/lambda0
           proportional to h(U)h(V) product_e exp[beta_(t,e)u_e.v_e],
    h(U)=m(U)psi(U).                                        (8)

Fix Z=U_R, the retained coordinates on the CURRENT slice only. Under this conditioning, let X=U_I and Y=V, the ENTIRE following slice. The density has the form of Section 3, with all unknown spatial and vacuum dependence assigned to positive endpoint factors. Its only X-Y coupling is

    k_I(X,V)=product_(e in I) exp[beta_(t,e)u_e.v_e].

The exact logarithmic cross ratio is

    sum_(e in I) beta_(t,e)(u_e-u'_e).(v_e-v'_e).             (9)

Since unit quaternions have chordal distance at most two, its absolute value is at most 4b_I. Thus (6) holds conditionally on EVERY Z with c=r_I, independent of Z, beta_s, and the retained volume.

Conditional variance decomposition first in the pair law, then at fixed Z, gives

    E Var(f(U)|V)
       >= E Var(f(U)|V,Z)
       >= (1-r_I^2) E Var(f(U)|Z).                          (10)

Reversibility identifies the left side with ||f||_pi^2-||Kcal f||_pi^2, and the right side with (1-r_I^2)||Q_I f||_pi^2. This is (3). The argument is immediate for bounded functions and extends by L2 density. No pointwise value of psi was estimated.

Taking f in range Q_I proves the first inequality in (4). The second follows by compression and positivity of Kcal. Restriction to gauge-invariant centered functions preserves all these estimates. This includes ALL discarded states in that subspace, not only states visible to a finite observable list.

## 5. Rigorous all-time memory and a retained-algebra certificate

On the entire centered physical space write S=Kcal|1-perp, and use the orthogonal decomposition supplied by P_I and Q_I:

    S=[[A,B],[B*,D]],     M_j=P_I S^j P_I,     N_k=B D^k B*.

The preceding theorem gives D<=r_I I without assuming a discarded-sector gap. In particular

    0<=N_k<=r_I^k N_0,       N_0=M_2-A^2.                    (11)

For any target edge q with r_I<q<1, the weighted series converges in norm, and

    W(q):=sum_(k>=0) q^(-k-1)N_k
          =B(qI-D)^(-1)B* <= N_0/(q-r_I).                  (12)

After retaining terms k=0,...,m, its full omitted tail satisfies

    0<=W(q)-sum_(k=0)^m q^(-k-1)N_k
       <= [(r_I/q)^(m+1)/(q-r_I)] N_0.                     (13)

This is a genuine all-time bound, not an extrapolation from the finitely checked powers. The proof is the spectral ordering of D and an ordinary convergent geometric series.

Completion of the square therefore gives the sufficient full-centered-space certificate

    A + (M_2-A^2)/(q-r_I) <= q I_retained
          implies S<=q I_centered.                        (14)

A sharper version uses the computed prefix in (13) plus its explicit upper tail. The discarded dark sector is already controlled by (4); no cyclicity or observability assumption is needed for this particular projection.

**What (14) does not give automatically.** It is an operator inequality on the COMPLETE retained physical L2 algebra in the TRUE vacuum. A finite matrix of selected Wilson loops does not establish it. No bound on its left side uniform along the continuum/infinite-volume trajectory is proved here. Thus U031's finite-moment obstruction is not contradicted: (11) adds previously unavailable structural tail information, and (14) still quantifies over every retained state.

The kernel powers in (11) are powers of the discarded compression D=Q_I S Q_I. They are NOT unprojected long-time transfers:

    Q_I S^2 Q_I-D^2=Q_I S P_I S Q_I.                        (15)

That term generally does not vanish. Neither (4) nor (11) licenses replacing Q_I S^j Q_I by D^j or raising r_I to a number of microscopic steps in a new coarse transfer without a separate argument.

## 6. Extension test: fixed-size constants do not tensorize automatically

The proof applies to every finite I, but gives tanh(sum beta_(t,e)), not max_e tanh(beta_(t,e)). Product temporal kernels do not justify the latter improvement when endpoint weights are correlated.

Here is an exact stress test in the larger positive-kernel class used by the proof; it is NOT a Wilson or Yang–Mills counterexample. On two binary coordinates let

    c=[[4,1],[1,4]],    C=c tensor c,    h=(t,1,1,t), t>0,
    v=C h,             K_ij=C_ij h_j/v_i,
    pi_i=h_i v_i/(h* C h).

K is reversible and row stochastic; it is also positive as a self-adjoint operator on L2(pi), by congruence to C. It is a true-ground-state transform: with multiplication M_i=sqrt(h_i/v_i), the symmetric positive matrix M C M has positive Perron eigenvector sqrt(h_i v_i) and Perron eigenvalue one.

The factor c corresponds, up to a positive scalar, to exp[beta x y] with beta=log 2 and x,y in {+1,-1}. Its single-coordinate bound is tanh(beta)=3/5. However the centered vector (1,0,0,-1) is an exact eigenvector of the two-coordinate K with eigenvalue

    z(t)=15t/(17t+8),
    z(t)-3/5=24(t-1)/[5(17t+8)],
    lim_(t->infinity) z(t)=15/17=tanh(2beta).                (16)

For t>1 the entire two-coordinate contraction is already larger than 3/5. The single-coordinate bounds proved above continue to hold; the slow collective vector has retained components when only one coordinate is discarded. With more coordinates, endpoint weights concentrated on the two fully aligned binary configurations similarly approach a two-state channel with eigenvalue tanh(|I|beta). This last limit follows directly from the ratio exp(2|I|beta) of aligned versus opposite temporal weights.

This makes the obstruction precise: the sum-coupling dependence is sharp for unrestricted positive endpoint factors. Additional structure of the actual Wilson vacuum could improve it, but such structure must be proved. No estimate of the probability of correlated surroundings or claim of sharpness in the pure Wilson family is inferred from the binary example.

The exact checker also uses t=1000. Its centered eigenvalue 15000/17008 exceeds 4/5, and the retained certificate (14) at q=4/5 correctly FAILS. Thus the new theorem does not silently turn local discarded relaxation into a full gap.

## 7. Physical units and remaining scaling loss

For uniform temporal beta_t and a fixed set of l discarded links,

    1-r_I=2/[exp(2l beta_t)+1],
    -log r_I=2 exp(-2l beta_t)(1+o(1))

as beta_t tends to infinity. If, strictly as a scaling diagnostic, tau=a and

    beta_t(a)=kappa log(1/a)+o(log(1/a)),

then

    [-log r_I]/a=2 a^(2l kappa-1+o(1)).                    (17)

For 2l kappa<1 this sufficient discarded-memory rate grows; for 2l kappa>1 it tends to zero; equality requires subleading information. This is not an established asymptotically free trajectory or a Hamiltonian excitation mass. It only determines whether a proposed physical target q=exp(-a M) can fall above our proved r_I for small a. The retained inequality (14) and the full QFT construction remain separate.

If l grows proportionally to the number of links, r_I tends rapidly to one even at fixed beta_t. Thus this work removes total-volume dependence only for a FIXED-size discarded set; it has not solved the extensive-block tail problem. Successive one-link eliminations change the effective action and vacuum representation, and must not be assigned the original temporal factorization without proof.

## 8. A restricted actual SU(2) benchmark

When beta_s=0, psi is Haar-constant and the normalized transfer is a product of central temporal convolutions. For one link its fundamental-representation eigenvalue is

    r_fund(beta_t)=I_2(beta_t)/I_1(beta_t).

For a fundamental character of a simple elementary four-edge Wilson loop the exact transfer eigenvalue is r_fund(beta_t)^4. If one of those four links is discarded, that character has P_I expectation zero by Haar integration. It must therefore satisfy the bound in (4).

Using the unchanged U029 positive-series routines, exact rational enclosures verify r_fund(beta)^4<tanh(beta) at beta in {1/2,1,2,6}. Every Bessel tail and exponential tail is bounded before division; displayed decimal endpoints are rounded outward. These four cases corroborate normalization for a named physical observable. They are not the proof for arbitrary beta, beta_s>0, other states, or the continuum; Sections 3–4 give that fixed-regulator proof without a character truncation.

## 9. Sources, checks, and self-audit

Primary sources checked 2026-09-15:

- Stephane Gaubert and Zheng Qu, *Dobrushin's ergodicity coefficient for Markov operators on cones*, arXiv:1307.4649v3, version dated 2014-11-01. Introduction equations (1)–(4) relate total variation and oscillation; Theorem 5.6 and Corollary 5.7 give the tanh(projective diameter/4) contraction. Exact versioned HTML, theorem and adjacent proof were read: https://arxiv.org/html/1307.4649v3 . Our Delta in (5) is the positive-kernel cross-ratio diameter; endpoint multipliers cancel. This is known contraction machinery after translation, not a source claiming the Wilson theorem (3).
- Yury Polyanskiy and Yihong Wu, *Strong data-processing inequalities for channels and Bayesian networks*, arXiv:1508.06025v4, version dated 2016-07-28. Section 2.1, equations (7)–(9) and Theorem 1 discuss total-variation contraction and the L2/conditional-expectation interpretation of maximal correlation. Versioned HTML was read: https://arxiv.org/html/1508.06025v4 . This provides terminology/overlap. The compact continuous-space roundtrip proof in Section 3 is written explicitly instead of silently importing a finite-alphabet assertion.
- U031, pinned base above, Section 2 defines the actual finite Wilson transfer, vacuum and gauge restriction; Section 6 supplies the weighted-memory/Schur framework. No new claim of novelty or externally verified pure Yang–Mills result is made. The current CMI Yang–Mills page was rechecked and still labels the problem unsolved: https://www.claymath.org/millennium/yang-mills-the-maths-gap/ .

No broad novelty search, publication, external correspondence, paid computation, or background job was initiated. The documented Consensus quota failure was not repeated. Mathbox supplied workflow guidance, not an independent mathematical verdict.

`checks/U032_conditional_memory_checks.py` ran under Python 3.13.5 / SymPy 1.14.0: TWELVE tests passed. Matrix data are exact rationals, with all principal minors checked for the stated small matrices. The explicit endpoint weights are (1,1,1,1), (1,2,3,5), and (1000,1,1,1000). Tests cover the weighted true conditional projection, full conditional-variance form, D<=3/5, memory powers k=0,...,6, weighted tail prefixes m=0,...,5, a positive and a deliberately failing coarse certificate, the noncommuting-time-power control, symbolic batch obstruction, likelihood algebra, and the four all-tail SU(2) benchmarks. No random seed or fitted spectrum is used.

The first twelve-test run had one checker failure: SymPy structural equality compared differently expanded but algebraically identical rational expressions. Replacing it with the exact simplified zero residual repaired the check without changing the mathematical assertion; the original log, hashes and repair are preserved. All THIRTEEN U031 tests were then rerun with outputs in new U032 files, without overwriting U031 evidence. Compilation and indentation checks passed. Static ruff/mypy/pyright and Lean are unavailable in this runtime, so no static-type/lint or formal-verification success is claimed.

Wolfram 15.0.1 independently corroborated the rational batch eigenvector, exact rates 3/5 and 15/17, weighted reversibility and the nonzero memory discrepancy. Its initial broader call returned the expected expressions but emitted indeterminate/infinite warnings, so those outputs are marked non-certifying. A bounded algebra-only rerun was clean. Submitted expressions and actual returned outputs are preserved; neither call is an independent derivation of (3).

Primary verdict: **proved after the explicit finite-Wilson, true conditional-projection, fixed-set restriction**. Passed: exact vacuum law; physical projection/gauge compatibility; both conditional-channel bounds; all-vector variance inequality; all-discarded-state bound; all-time weighted tail; units; deliberate non-tensorization and coarse-failure controls. Not proved: the retained inequality (14) on the entire physical algebra uniformly in regulator/volume; an extensive second-elimination bound with acceptable constants; preservation of the temporal product form after repeated decimation; continuum/volume limits; nontrivial finite physical mass; the full target for all compact simple groups.

## 10. Executable next question

The next substantive target is the retained Schur deficit, not another finite-time fit. For a geometrically specified retained boundary algebra in the Wilson vacuum, test whether

    qI-A >= [1/(q-r_I)] (M_2-A^2)

can be proved with constants useful under enlargement, or whether a larger discarded block admits a Wilson-specific improvement over tanh(|I|beta_t). The binary endpoint example identifies the additional dependency: control of collective correlations in the actual conditional vacuum, not independence of the temporal factors alone. Any proposed conditional-variance tensorization must be established in that measure and connected to physical time; a spatial heatbath gap is not a substitute. The new local theorem is a usable tail component, not the missing positive infrared mass mechanism.

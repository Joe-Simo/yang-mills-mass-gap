# U034 — history-layer variance, physical cycle obstructions, and a forest bound

Date: 2026-09-15. Base: private `Joe-Simo/yang-mills-mass-gap` commit `8f76fad21d6c07fd391f1393f46d96a4915aa37b` (U033).

**We have not solved the Yang–Mills problem yet.**

Evidence: self-reviewed finite-regulator operator proofs, a separately identified two-dimensional Euclidean Wilson-cylinder calculation, and exact finite checks. No independent expert review, formal verification, novelty claim, or continuum mass-gap theorem.

## 1. Target and preserved dependencies

U033 controls discarded-column endpoint correlations conditional on the complete retained history. The unproved implication was whether several such history algebras collectively exclude every slow centered physical state. This unit (A) derives the precise variance-to-transfer implication, (B) proves a finite but quantitatively inadequate Wilson variance comparison, (C) tests the proposed uniform-angle intuition on genuine gauge-invariant Wilson-loop observables, and (D) executes the alternative of retaining an acyclic graph at one time.

The supplied U033 archive was inspected: 84 missing files were restored inside `/mnt/data/yang-mills-mass-gap`, two existing entries matched, and no file conflicted or was overwritten. All seven U033 manifest entries matched before new work. The remote branch was checked at the base above. The full standalone Yang–Mills prompt was recovered through current-conversation file search; its universal target, private-write permission and zero-spend boundary remain unchanged. There is no local Git checkout, AGENTS file, or executable Mathbox ledger in this workspace. No sibling project was accessed. The README alone is intentionally updated among earlier manifest-covered files; earlier mathematical records and checkers remain unchanged.

The essential dependencies are U032's actual-vacuum fixed-set contraction and U033's exact stationary path law and history-conditioned maximal-correlation bound. Their measures and projections are not replaced with Haar averages. Standard product-variance and group-integration arguments below are proved directly; sources are recorded in Section 8.

## 2. Several history layers: the exact missing coefficient

Use the finite spatial periodic cubic graph and positive physical transfer `K` of U032–U033, acting in the actual vacuum `L2(pi)`. Its microscopic time step is `tau>0`; `K=exp(-tau H)` on the physical Hilbert space after the ground-state transform. Work separately on the centered gauge-invariant subspace `H_phys^0`.

Partition spatial edges into noncofacial sets `I_1,...,I_k`. For the even periodic N-cube, N>=4, an explicit six-color partition is

    I_(mu,p) = {(x,mu): sum_(nu != mu) x_nu = p mod 2},
    mu=0,1,2, p=0,1.

Each plaquette has at most one edge in any fixed color, each color has N^3/2 edges, and all 3N^3 edges are covered. This is the geometry needed by U033, not an independence assertion about the resulting history algebras.

At slab depth n>=1, use U033's SAME stationary path probability P_n, endpoint isometries `J_t f=f(U_t)`, and conditional expectations `Pi_c` onto the full history of all edges outside I_c. Set

    theta_c = tanh(sum_(e in I_c) atanh(tanh(beta_e)^n)) < 1,
    V_c(f) = ||(1-Pi_c) J_0 f||_(P_n)^2,
    gamma_n^phys = inf_(0 != f in H_phys^0)
                    [sum_c V_c(f)] / ||f||_pi^2.                (1)

This is an endpoint-restricted conditional-variance coefficient. A variance inequality on ALL path functions is sufficient, but stronger than needed. In particular, a gauge-dependent path counterexample would not alone refute (1).

### Variance-to-transfer theorem

For every centered physical f,

    <f,(1-K^n)f>_pi >= (1-theta_c) V_c(f)    for each c.        (2)

Consequently, with

    D_n = sum_c 1/(1-theta_c),

one has

    0 <= K^n|H_phys^0 <= [1-gamma_n^phys/D_n] I.                (3)

Any proved lower estimate `gamma_n^phys >= gamma>0` therefore gives

    Delta_phys >= -log(1-gamma/D_n)/(n tau),                   (4)

provided the centered space is nonzero and the stated scalar bound is used in its valid range. Formula (4) is a physical-time statement, not an auxiliary heatbath-time gap.

**Proof of (2).** Put u=J_0 f and v=J_n f. Time reversal of the stationary reversible path preserves the history algebra, so

    ||Pi_c u||^2=||Pi_c v||^2=||f||^2-V_c(f),
    ||(1-Pi_c)u||^2=||(1-Pi_c)v||^2=V_c(f).

The two orthogonal components give

    <f,K^n f> = <Pi_c u,Pi_c v> + <(1-Pi_c)u,(1-Pi_c)v>.

Cauchy–Schwarz bounds the first term in real part by `||f||^2-V_c(f)`. U033's conditional maximal-correlation theorem bounds the absolute value of the second by `theta_c V_c(f)`. Subtraction proves (2). Summing `V_c(f)<=<f,(1-K^n)f>/(1-theta_c)` proves (3). Positivity and the spectral theorem give (4).

No independence, commutation of Pi_c, finite observable list, or memoryless reduced transfer was used. In the common-rate case, (3) reads

    1-K^n >= [(1-theta)/k] gamma_n^phys I.

Thus U033's unresolved retained-history term has a precise sufficient replacement, but the required useful lower estimate of gamma is not supplied merely by intersecting the ranges of Pi_c.

## 3. An actual-vacuum finite estimate and its quantitative failure

Let P_s be the number of spatial plaquettes, `b=sum_e beta_e`, `W(U)=sum_p(1-ReTr U_p/2)`, and `s_psi=osc(log psi)`, where psi is the actual strictly positive Perron eigenfunction. Then `0<=W<=2P_s`.

Construct a reference path probability nu_n by taking independent stationary SU(2) temporal chains for EVERY spatial edge, with normalized one-link transition

    c_e(u,v)=exp(beta_e u.v)/Z(beta_e),
    Z(z)=2 I_1(z)/z, Z(0)=1.

This reference has independent color-column blocks. It is only a comparison measure; it is not asserted to equal the interacting vacuum path law.

U033's exact path density implies, up to a constant independent of the configuration,

    dP_n/dnu_n = psi(U_0)psi(U_n)
       exp[-beta_s W(U_0)/2-beta_s W(U_n)/2
                    -beta_s sum_(t=1)^(n-1) W(U_t)].          (5)

Therefore

    osc log(dP_n/dnu_n) <= A_n := 2 s_psi + 2 n beta_s P_s.    (6)

### Direct bounded-density variance comparison

For a product probability nu on k blocks, the Efron–Stein inequality is

    Var_nu(F) <= sum_c inf_(h measurable outside c) E_nu |F-h|^2.

For completeness, in the product L2 space the commuting block-averaging projections give an orthogonal ANOVA decomposition indexed by subsets S of blocks. The variance is the sum of squared norms over nonempty S. The c-th unexplained variance includes exactly the terms with c in S. Summing counts each nonempty S at least once; density extends the result from finite sums.

If `a<=dP/dnu<=A`, each conditional distance in P is at least a times its counterpart in nu, whereas `Var_P(F)<=A Var_nu(F)`, by minimizing over constants. Thus

    sum_c E_P Var_P(F|outside c) >= (a/A) Var_P(F).

Applying this to (5) gives, for all path functions and hence for J_0 f,

    gamma_n^phys >= exp(-A_n) > 0.                           (7)

The reference ratio does not require computing psi. For explicit finite constants, the Perron equation and

    exp(-2b) <= product_e exp[-beta_e(1-u_e.v_e)] <= 1

give `s_psi<=beta_s P_s+2b`: compare psi(U)/m(U) and psi(U')/m(U') inside the same positive integral, with `m=exp(-beta_s W/2)`. Hence

    gamma_n^phys >= exp[-2(n+1) beta_s P_s-4b].                (8)

This is a valid finite Wilson inequality. It is NOT the wanted scale-uniform estimate: its certified value deteriorates exponentially with space-time volume and coupling. A finite positive result cannot be promoted to a continuum lower bound. Conversely, deterioration of this lower estimate does not prove gamma itself is small.

### Product control

At beta_s=0, the actual psi is constant and P_n=nu_n, so gamma_n^phys>=1. In this case the discarded endpoint laws also factor across edges; their L2 correlation coefficient tensorizes as a MAXIMUM, not a sum. Each single-column coefficient is bounded by `tanh(beta_e)^n`, so theta can be replaced by `max_e tanh(beta_e)^n`, independent of |I_c|. The tensorization follows by decomposing product L2 into constant/centered factors and multiplying the channel norms. This gives a volume-independent finite-coupling check of the bridge in the zero-spatial-coupling case. It is not the interacting weak-coupling continuum regime.

## 4. Gauge-invariant angle deterioration in an exact Wilson cylinder

The following is an actual TWO-DIMENSIONAL EUCLIDEAN Wilson measure with a specified boundary-loop marginal. It is neither the 3+1-dimensional true vacuum pi nor a claimed realization of the six history projections. Its role is to test whether gauge invariance and exact intersection at constants are enough for a coupling-independent angle. They are not.

Take a square-lattice cylinder with two rows y=0,1 and circumference L>=3. Let b_i and t_i be bottom/top horizontal links and v_i vertical links, i modulo L. The L elementary plaquettes are

    P_i=b_i v_(i+1) t_i^(-1) v_i^(-1).

All links are integrated with Haar measure and the weight is `product_i exp[beta ReTr(P_i)/2]`, beta>=0. There are 2L vertices, 3L edges, and a tree of 2L-1 edges. Gauge-fix every vertical edge and b_0,...,b_(L-2) to I. This is a genuine spanning-tree gauge; Haar invariance integrates out the tree gauge coordinates exactly. No kinetic operator or Hamiltonian is being simplified here.

Let `U=b_(L-1)` and let `V=t_0 ... t_(L-1)` be the top holonomy parallel transported to the bottom root by the vertical tree. Residual gauge transformations conjugate U and V simultaneously. In this gauge

    P_i=t_i^(-1) (i<L-1),     P_(L-1)=U t_(L-1)^(-1).

Writing `q_beta(A)=exp[beta ReTr A/2]/Z(beta)`, the normalized joint marginal of U,V is

    dmu_(beta,L)(U,V) = q_beta^{*L}(UV^(-1)) dU dV.            (9)

Here * is central group convolution. To check the exact order, put `T=t_0...t_(L-2)` and `t_(L-1)=T^(-1)V`; the final plaquette is `UV^(-1)T`. Integrating the L-1 other top links against the inversion-symmetric central q_beta gives (9) by successive convolutions. Both U and V marginals are Haar. The connector is retained in the parallel-transport convention; averaging it away instead would separately conjugate the boundary matrices, but does not change the trace correlations used below.

Let `chi(A)=Tr A=2a_0` be the fundamental character. Haar normalization gives `E chi=0`, `E chi^2=1`. Conjugation and inversion symmetry imply

    integral q_beta(A) A dA = r(beta) I,
    r(beta)=E_(q_beta) a_0=I_2(beta)/I_1(beta), r(0)=0.

Thus each convolution multiplies the conditional first character by r, giving

    E[chi(U)|V]=rho chi(V),  E[chi(V)|U]=rho chi(U),
    rho=r(beta)^L,  E[chi(U)chi(V)]=rho.                       (10)

For finite beta>0, `0<rho<1`. Define the conditional expectations P_U,P_V onto their respective boundary variables. On the two-dimensional invariant span of chi(U),chi(V),

    Gram = [[1,rho],[rho,1]],
    P_U  = [[1,rho],[0,0]],
    P_V  = [[0,0],[rho,1]],
    (1-P_U)+(1-P_V) = [[1,-rho],[-rho,1]].                     (11)

These matrices are self-adjoint with respect to the Gram matrix, not the ordinary Euclidean matrix inner product. In particular the NONZERO centered GAUGE-INVARIANT observable

    F=chi(U)+chi(V),  ||F||^2=2(1+rho),

is an exact eigenvector with conditional-variance eigenvalue

    1-rho = 1-[I_2(beta)/I_1(beta)]^L.                        (12)

The density in (9) is strictly positive on the whole compact product. Therefore functions simultaneously measurable in U alone and V alone are constants modulo null sets. This exact intersection fact coexists with an arbitrarily small positive eigenvalue (12).

For fixed L, the checked positive-axis fixed-order Bessel asymptotic gives

    r(beta)=1-3/(2beta)+O(beta^-2),
    1-r(beta)^L=3L/(2beta)+O_L(beta^-2) -> 0.                 (13)

No limit exchange with L or a four-dimensional scaling trajectory is made. This refutes a universal inference from gauge invariance/full support/trivial exact intersection to a coupling-independent variance coefficient, even among simple Wilson measures. It does NOT refute a useful, correctly scaled estimate of gamma_n^phys for the actual four-dimensional vacuum. It also does not assert that (12) is the smallest eigenvalue of the whole physical conditional-variance operator; one explicit eigenvector is sufficient for the upper obstruction.

The checker encloses (12) with complete rational Bessel-series tails at beta=0,1/2,2,8,32,128 and L=4,16. These are conditional-variance eigenvalue certificates, not physical mass measurements.

## 5. Execute the alternative: retain a forest at one time

There is an exact gauge-theoretic way to eliminate retained physical excitations, but its cost again grows with the graph.

Let pi be ANY gauge-invariant probability with positive density on a finite graph's link configurations. Let R be a forest, and let `P_R=E_pi[ . | U_R]` at ONE TIME SLICE. For every gauge-invariant f,

    P_R f = E_pi f.                                          (14)

**Proof.** Gauge invariance of pi makes conditional expectation equivariant under the induced action on retained coordinates. Thus P_R f is itself an invariant function of forest links. Vertex gauge transformations act transitively on forest-link assignments: choose a root in each component, then solve the gauge transformations recursively along the unique paths. Every invariant measurable forest function is constant; its expectation fixes that constant. This proof does not assume a product vacuum.

On a connected graph with at least one cycle, choose a spanning tree T and discard `I=E\T`. Equation (14) makes U032's Q_I act as the identity on the ENTIRE centered physical space. Its actual-vacuum contraction consequently gives

    ||K|H_phys^0|| <= tanh(sum_(e notin T) beta_e),
    Delta_phys >= -log[tanh(sum_(e notin T) beta_e)]/tau.      (15)

This is a full finite-regulator physical-space lower bound, not a Ritz compression. It retains every physical state through the use of the full K; only the conditional-expectation proof tests a forest algebra. To optimize (15) over trees, retain a maximum-weight spanning tree with edge weights beta_e. With uniform beta_t, the omitted count is the cycle rank `|E|-|V|+1`. On a periodic spatial N-cube, N>=4, it equals `2N^3+1`.

Therefore the displayed bound has size

    -log tanh[(2N^3+1)beta_t]/tau
       ~ 2 exp[-2(2N^3+1)beta_t]/tau                         (16)

when that argument is large. It does not survive the required growing-volume/refinement regime as a useful certified lower bound. No conclusion that the actual gap has this small size is drawn. A tree graph has no centered physical states; the empty-cotree case is not advertised as a nontrivial infinite gap.

Crucially, (14) is a ONE-TIME forest statement. It does NOT apply to U033's entire retained history: link values at different times contain gauge-invariant relative information under the common temporal-gauge transformation. Silently replacing Pi_c by P_R would undo the temporal-memory distinction proved in U030–U033.

## 6. What the three routes decided

- History overlap: a lower coefficient gamma_n^phys controls the actual transfer through (3)-(4). The finite bounded-density lower estimate (7)-(8) is proved, but loses exponentially in the wrong parameters.
- Gauge-invariant adversary: the exact Wilson cylinder provides a physical loop eigenfunction whose variance coefficient tends to zero even though the conditional ranges intersect only at constants. This is not a gauge-direction counterexample and is not the four-dimensional vacuum.
- Complete acyclic retention: (14)-(15) removes the remaining physical algebra exactly at one time, but the fixed-set contraction cost is exponential in cycle rank. It does not solve the collective scaling problem.

These statements preserve, rather than replace, U033. No earlier universal small-field, scalar-localization, or independent-plaquette claim is promoted as an input.

## 7. Verification and computation limits

`checks/U034_history_variance_and_cycle_checks.py` uses exact Python fractions and SymPy rational/polynomial algebra, reusing the unchanged certified Bessel series in U029. Eleven focused tests passed. Exact scope: the full six-color geometry at N=4,6; all paths of the specified positive four-state reversible fixture at n=1,2,3; weighted-projection and bounded-density tests for three positive laws; two noncommuting rational SU(2) cylinder configurations at L=3,4; twelve complete-tail scalar certificates; and all 4096 Q8^4 configurations for a finite-group forest-algebra control. The finite Q8 test is not an SU(2) integral. General statements are proved above, not extrapolated from these populations.

The first two checker runs each failed one structural-equality assertion because differently factored identical polynomials were compared literally. Both were replaced with expanded zero-residual checks. The identities and theorem constants did not change; the failures and repair hashes are preserved. No failed test is hidden as a successful run.

All twelve U033 checks were rerun separately into new U034 evidence. Compilation and indentation checks were also run. Static ruff/mypy/pyright and Lean are unavailable in the inspected environment; these tools are not claimed to have passed. The record is self-review, not an independently checked proof.

A separate 20-second-cap Wolfram call corroborated projection idempotence, Gram-weighted adjoints, eigenvector (12), the ratio coefficients supplied from the fixed-order asymptotic, and the cycle count. It did not derive the full Wilson path theorem or certify an infinite-dimensional mass.

## 8. Source scope and notation dictionary

- NIST DLMF 10.32.2 and 10.29: the normalized SU(2) integral Z=2I_1(beta)/beta and its derivative r=I_2/I_1, with continuous beta=0 extension. DLMF 10.40.1: fixed orders 1 and 2 on the positive real axis, used only for the fixed-L asymptotic (13). Checked 2026-09-15. URLs: https://dlmf.nist.gov/10.32 ; https://dlmf.nist.gov/10.29 ; https://dlmf.nist.gov/10.40 . The finite certificates use convergent positive series instead of asymptotics.
- M. Fukuma, D. Kadoh, N. Matsumoto, *Tensor network approach to 2D Yang-Mills theories*, arXiv:2107.14149v1, 2021-07-29. HTML Section 2.2 equations (2.15)-(2.16) and Appendix A equations (A.1)-(A.9) were read: Wilson character coefficients, normalized Haar measure, and the character-convolution factor 1/d_R. Our q_beta removes the constant exp(-beta) and divides by the trivial-representation coefficient; the fundamental normalized coefficient is r. The cylinder geometry and angle implication are derived here. The paper's finite tensor approximations and numerical estimates are not imported as rigorous continuum inputs. URL: https://arxiv.org/html/2107.14149v1 .
- M. Mathur and T. P. Sreeraj, *Canonical Transformations and Loop Formulation of SU(N) Lattice Gauge Theories*, arXiv:1509.04033v2, 2015-12-06. Section III, especially the one-plaquette string/Gauss-law reduction, was read as context for tree versus physical loop degrees of freedom. We use only our direct transitivity proof (14), not an approximation to the full Hamiltonian or the paper's weak-coupling interpretation. URL: https://arxiv.org/html/1509.04033v2 .
- The Caputo–Menz–Tetali approximate-tensorization paper, arXiv:1405.0608, was found as a terminology lead. Requested HTML versions were unavailable, so no theorem from it is used. The product-variance and density-comparison proof in Section 3 is self-contained.
- The official CMI Yang–Mills page was checked on 2026-09-15 and remains marked unsolved. URL: https://www.claymath.org/millennium/yang-mills-the-maths-gap/ . No prize, publication, contact, or acceptance claim is made.

These are established mechanisms or their elementary applications; no global novelty search or novelty claim is made. Consensus's already recorded quota failure was not repeatedly invoked. Mathbox supplies workflow instructions, not an independent mathematical reviewer. No paid work or asynchronous process was initiated.

## 9. Self-audit and executable continuation

Primary verdict: **proved after the stated finite-regulator and diagnostic-model restrictions**.

Passed: one common actual Wilson path measure for all layers; true-vacuum centering; time reversal and conditional covariance; complete endpoint-algebra inequality rather than selected moments; explicit finite coefficient and its bad scaling; noncommuting cylinder gauge reduction with the connector accounted for; normalized continuous SU(2) correlation; physical rather than gauge-variant adverse observable; full-support/trivial-intersection distinction; the forest proof and its one-time restriction; finite physical-unit conversion.

The open obligation is now the explicitly defined `gamma_n^phys` in (1), or a weaker direct estimate with the same effect on centered physical endpoint vectors. A sufficient continuum-useful scaling would keep the right side of (4) positive in physical units on the chosen joint volume/coupling/time sequence. Neither (8) nor (16) does that. Such a spectral estimate would still need the actual continuum construction, compatible axioms and Yang–Mills identification, finite nontrivial limiting states, and all eligible groups.

Next discriminating calculation: work with two overlapping gauge-invariant cycle algebras in the actual finite Wilson vacuum, not a static cylinder or arbitrary endpoint-weight model. Derive their conditional-variance response from a common slab kernel retaining the shared links, and determine whether a centered comparison can be controlled by connected plaquette/cycle cumulants with constants independent of external volume. Before a large computation, check the exact one- and two-cycle limiting cases and identify every factor involving the unknown vacuum. A beta-independent angle, or replacing all histories by a forest at each time, is not an admissible shortcut.

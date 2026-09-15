# U037 — interacting-block comparison with boundary charge sectors retained

Date: 2026-09-15. Base: private `Joe-Simo/yang-mills-mass-gap` commit `2bcf36ad370b7ca2392da001d284e5dd9434e1ac` (U036).

**We have not solved the Yang–Mills problem yet.**

Evidence: self-reviewed finite-regulator proof, using the established block Gibbs-comparison mechanism, with exact finite algebra/geometry checks. No independent expert or formal verification, novelty claim, homogeneous weak-coupling result, or continuum construction.

## 1. Question, outcome, and preserved state

U036 controlled a homogeneous interacting lattice only when every spatial coupling was small. This unit tests its proposed replacement of individual time columns by internally interacting spatial blocks. The result is a full-space, exterior-volume-independent comparison in a larger, but still restricted, domain: internal plaquette couplings may be arbitrarily strong, whereas crossing plaquettes must satisfy an explicit interface smallness budget. A better intrinsic block-kernel estimate can improve the allowed time scale; a complete but expensive estimate is provided without assuming a block spectral gap.

A second check identifies which Hilbert space this block estimate must control. Projecting separately onto gauge singlets at all block boundary vertices loses globally gauge-invariant states. The proof therefore keeps the complete boundary charge sectors until the global gauge restriction. Finally, an anisotropic-time diagnostic shows why changing only the temporal spacing cannot move U036 into its missing weak-coupling regime.

The assigned folder was inspected. The U036 archive restored 121 missing files; two existing files matched and none was overwritten. All eight U036 primary manifest hashes matched before new work. The remote head was read and pinned above. The standalone project prompt was retrieved from current-conversation file search and its target, isolation, private-write, and zero-spend constraints retained. No sibling project was read. Earlier proof/checker/evidence files are unchanged; README is intentionally updated with its old version preserved in the parent commit and supplied archive. No local Git checkout or executable formal-proof environment was present. Current plugin discovery returned no Mathbox entry; no new Mathbox execution or independent verdict is claimed. The previously supplied audit principles were applied directly. The documented Consensus quota failure was not retried merely to repeat it.

## 2. Actual Wilson transfer and a partition of link coordinates

Use U036's finite spatial cubic graph and temporal normalization. All links are SU(2), Haar measure is normalized, and

    w_p(U) = Re Tr(U_p)/2,                    |w_p| <= 1,
    V(U) = sum_p s_p w_p(U),                  0 <= s_p < infinity,
    C = tensor_e C_(beta_e),                  0 < beta_e < infinity,
    C_(beta_e)(u,v) = exp(beta_e u.v)/Z(beta_e),
    T = exp(V/2) C exp(V/2).

Here u,v are unit quaternions and Z(beta)=2 I_1(beta)/beta. The parameters beta_e are temporal Wilson couplings, not the Hamiltonian lambda=4/g^4 used in earlier notes. Each finite T is a positive, strictly positive-kernel, compact self-adjoint operator. Its unique top eigenpair is (lambda0,psi), psi>0, ||psi||_2=1. The ground-state transformed normalized transfer K acts on L2(pi), pi=psi^2 mu, and preserves the gauge-invariant physical subspace. At microscopic time tau, its physical Hamiltonian is -log(K)/tau.

Partition E into finitely many nonempty DISJOINT link blocks B. There is no separate quotient at shared boundary vertices. A plaquette is internal if all its links belong to one block; otherwise it is crossing. Let J(p) be the distinct blocks touched by p, and r_p=|J(p)|. Thus 2 <= r_p <= 4 for crossing plaquettes. Set

    V_B = sum_(p internal to B) s_p w_p,
    T_B = exp(V_B/2) C_B exp(V_B/2),
    C_B = tensor_(e in B) C_(beta_e),
    S_B = sum_(p crossing, B in J(p)) s_p,
    A_BC = sum_(p crossing, B,C in J(p)) s_p  for B != C,
    A_BB = 0,
    D = max_B sum_C A_BC
      = max_B sum_(p crossing, B in J(p)) (r_p-1)s_p.          (1)

In particular S_B <= D. The internal couplings do not occur in D. If D=0, the blocks have no crossing interaction and the formulas below remain valid.

## 3. Intrinsic block-kernel criterion and the theorem

For a continuous strictly positive integral kernel L on a compact state space, define its logarithmic cross-ratio diameter

    d(L) = sup_(x,x',y,y') log[L(x,y)L(x',y')/(L(x,y')L(x',y))].

Multiplication by any positive function at either endpoint leaves d unchanged. This is a pointwise, all-boundary kernel quantity. A gap on only the gauge-singlet part of a block is NOT a substitute for it.

Choose one integer b >= 1 such that, for every block,

    d(T_B^b) <= 2 log(5/3).                                  (2)

**Theorem.** If (2) and

    b D <= 1/16                                              (3)

hold, the ENTIRE centered physical transfer satisfies

    ||K||_phys,centered <= exp[-log(4/3)/b],
    Delta_phys >= log(4/3)/(b tau).                           (4)

For bounded single-time observables F,G (physical or unrestricted), define osc_B F as the supremum of |F(x)-F(x')| when only block B is changed. Their true stationary covariance satisfies

    |Cov(F(U_0),G(U_n))|
       <= 4b ||osc F||_1 ||osc G||_infinity (3/4)^(n/b).       (5)

The rate is independent of the number of blocks. Observable support enters the explicitly displayed prefactor. The theorem is unconditional once the finite parameters and a verified (2) are specified; Section 6 provides a universal choice of b, valid for arbitrary internal couplings. Better choices of b require better block-kernel information, not an extrapolation of (4).

## 4. Conditional interacting-block bridge

First work on a finite open time interval, using the exact finite Wilson path law

    dnu proportional to exp[sum_t V(U_t)]
                        product_(e,t) k_(beta_e)(U_(e,t),U_(e,t+1))
                        product_t dmu(U_t).

Condition on the full histories of all blocks other than B. The remaining block is a single Markov chain on SU(2)^B with arbitrary internal potential V_B and an external time-dependent factor exp(h_t^B), where

    h_t^B(x_B) = sum_(p crossing, B in J(p)) s_p w_p(x_B;outside_t),
    |h_t^B| <= S_B.                                          (6)

No link inside B is assumed independent. No internal plaquette interaction is expanded. In particular the mixed cycle degrees of freedom of U027 remain present.

Delete endpoint multipliers from a b-step bridge, since they cancel from its diameter. Its reference kernel is then T_B^b with the corresponding endpoint halves removed. The b-1 internal factors exp(h_t^B) give the pointwise sandwich

    exp[-(b-1)S_B] M_B <= M_(B,h) <= exp[(b-1)S_B] M_B,
    d(M_(B,h)) <= d(T_B^b) + 4(b-1)S_B.                      (7)

Past and future messages, and boundary-time factors, are arbitrary positive endpoint multipliers and are preserved in this statement.

A kernel of diameter d has total-variation distance at most tanh(d/4) between any two rows normalized after ANY common positive terminal weight. To see this directly, the two conditional likelihood ratios have range quotient at most exp(d). Among positive likelihood ratios with that range and mean one, the largest total variation is (exp(d/2)-1)/(exp(d/2)+1). This follows by maximizing the convex absolute-value function on the two range endpoints. No knowledge of the vacuum weights is needed.

By (2)-(3), exp(d(M_(B,h))/2) is at most

    (5/3) exp[2(b-1)S_B] <= (5/3) exp(1/8) <= 40/21.

Here exp(1/8) <= 8/7 follows by comparison of its positive series with the geometric series. The conditional b-step forward or backward bridge coefficient is therefore at most

    (40/21-1)/(40/21+1) = 19/61 < 1/2.                      (8)

This proves bridge contraction even with arbitrarily strong V_B. The paid smallness is ONLY in the perturbing interface fields, not the full internal action. It is nevertheless a real interface restriction, not the desired continuum estimate for strongly coupled interfaces.

## 5. All influence lengths, true vacuum, and physical spectrum

Changing an external block C at one time u changes the B-chain site factor at u by logarithmic oscillation at most 4 A_BC. Its marginal at u is tilted by that same factor. The normalized-tilt lemma bounds the initial mismatch by tanh(A_BC) <= A_BC.

Conditional on its value at u, the past and future laws are unchanged. Couple the two block values at u maximally. In both time directions, couple successive b-step transitions using (8); after coalescence use identical futures. Fill the intermediate times by their Markov bridges, bounding mismatch within a block by the mismatch at its first endpoint. This is ONE joint full-path coupling, not an assembly of incompatible marginal couplings. It gives simultaneously

    Pr[X_B(t) != X'_B(t)] <= A_BC g_b(t-u),
    g_b(v) = 2^(-floor(|v|/b)).                              (9)

A source eta G at one time instead gives mismatch at most |eta| osc_B G/4 times g_b, since its conditional change is confined to one block state at one time. This remains true when G depends on several spatial blocks: all other blocks are fixed in each update.

Apply the block Gibbs comparison theorem to sites (B,t), site state SU(2)^B, and update blocks consisting of each entire finite time column. Its metric is the indicator of unequal block states, the update weights are one, and W=I. The hypotheses concerning joint update couplings are (9). All spaces are compact with continuous positive finite densities; finite-volume conditional expectations provide the invariant update rules. For the cited theorem, the influence R is bounded entrywise by J below:

    G_(B,t),(C,u) = 1_(B=C) g_b(t-u),
    J_(B,t),(C,u) = A_BC g_b(t-u),
    L = (I-J)^(-1)G.                                       (10)

The existence and convergence of this inverse are not assumed. With alpha=log(4/3)/b,

    W0 = sum_v g_b(v) = 4b-1,
    Walpha = sum_v exp(alpha|v|)g_b(v) <= 8b,
    ||J||_(alpha,row) <= 8bD <= 1/2,
    ||L||_(alpha,row) <= 16b.                              (11)

The time-weighted row norm is submultiplicative by the triangle inequality for time differences. Bounds on finite intervals are no larger than the displayed infinite sums. The norm condition verifies the comparison theorem's convergence hypothesis.

Compare nu with its normalized tilt exp(eta G)nu, divide the comparison inequality by |eta|, and take eta to zero in a finite compact integral. The source part of (9) gives

    |Cov_nu(F,G)| <= (1/4) osc(F)^T L osc(G).                 (12)

Consequently (5) holds on every finite open time interval, with constants independent of its length. This is a bound on the actual background measure; its repeated spatial influences have been summed in (10), not deleted.

Fix the full spatial graph. The free-end path law converges in its central finite-time marginals to the actual stationary vacuum path law: write its partition function and observables using T, its strictly positive endpoint vector exp(V/2), and the simple compact Perron eigenpair. Finite-graph Perron isolation identifies the limit; a uniform physical gap is not assumed in this step. The estimates are already uniform in time-interval length and thus pass to the limit.

For a bounded centered physical f, (5) bounds <f,K^n f> by C_f exp(-alpha n), with C_f finite on each spatial graph. Positivity and self-adjointness give a positive spectral measure on [0,1]. Any spectral mass above exp(-alpha) would contradict that all-n bound. Bounded invariant functions are dense in the physical L2 space, proving (4) for the entire centered physical space. This uses physical Euclidean time, not the iteration count of a Gibbs sampler. No static compression is asserted to be an exact reduced transfer.

The same proof yields an operator-valued connected-response estimate (12) for single-time observables. If a spatial block has at most M links, at most 4M plaquettes touch it. Hence sum_p osc_B w_p <= 8M, while ||osc w_p||_1 <= 8. Summing (12) over every plaquette and every time gives the restricted actual-vacuum susceptibility bound

    sum_p sum_t |Cov(w_q(U_0),w_p(U_t))|
       <= 16 M W0/(1-D W0) <= (256/3) M b.                 (13)

This is independent of total spatial volume, not of block size M. It holds for internal strongly coupled plaquettes too. It is not an all-order complex analyticity theorem.

## 6. Certify an intrinsic time without assuming a block gap

Condition (2) is not empty, even at arbitrarily strong internal coupling. Here is a complete, conservative certificate.

For the positive cone in C(X), define d_H(f,g)=osc log(f/g). For any continuous strictly positive compact kernel L,

    contraction_H(L) = tanh(d(L)/4).                        (14)

A brief proof keeps this input explicit. For f=g exp(h), interpolate g exp(th). The derivative of log L[g exp(th)] is the expectation of h under a normalized kernel row. The likelihood-ratio argument from Section 4 bounds the difference of those derivatives at two output points by tanh(d(L)/4) osc(h), proving the upper Lipschitz bound. For the reverse bound, select two input and two output points approaching a maximizing cross ratio. Concentrate positive input functions near the two input points, choose their relative weights to maximize the two-row likelihood difference, and differentiate along a function with values zero and one on those two neighborhoods. The resulting infinitesimal ratio approaches tanh(d(L)/4). Compactness, continuity, full-support Haar measure and strict positivity justify the approximations. The degenerate diameter-zero case is rank one and has zero coefficient. Thus (14) is an equality here, not an unjustified reversal of a one-sided inequality.

Positive multiplication is an invertible Hilbert-metric isometry. Set

    beta_B = sum_(e in B) beta_e,
    r_B = tanh(beta_B),    r_* = max_B r_B < 1.

The temporal product kernel has diameter exactly 4 beta_B: its logarithmic cross ratio is sum_e beta_e (u_e-u'_e).(v_e-v'_e), maximized by aligned antipodal quaternions. Endpoint internal-potential factors cancel. Therefore contraction_H(T_B)=r_B and, by composition,

    contraction_H(T_B^b) <= r_B^b,
    d(T_B^b) <= 4 atanh(r_B^b).                             (15)

In particular the explicit choice

    b = max(1, ceil[log(4)/(-log r_*)])                      (16)

proves (2) for EVERY finite collection of internal Wilson couplings. It is independent of their magnitudes. It can depend on the maximum block size and temporal coupling, not the number of blocks.

At large beta_B, (16) grows as (log 4/2) exp(2 beta_B). This poor bound is recorded, not hidden. It arises because the certificate controls all endpoint fields, including rare and gauge-variant boundary data. Strong internal interactions can permit a better intrinsic (2), but no such improvement is asserted from a block's singlet spectral gap alone.

For singleton blocks with no internal plaquette, U036's COMPLETE character estimate supplies the much better b=ceil(3 max(1,beta_t)). Its pointwise 3/4-to-5/4 kernel bound implies d<=2log(5/3), while D<=12s0. Thus (3) reduces EXACTLY to U036's b s0<=1/192. The new theorem is a block extension containing that benchmark, not a replacement by the worse (16) in the singleton case.

## 7. Explicit extensive strong-interior family and the remaining cost

For an even periodic N^3 lattice, partition the base vertices into cubes of side m dividing N, with N>=max(4,2m). Assign a positive oriented link to the cube containing its base vertex, even when its other endpoint is in the next cube. Blocks then contain M=3m^3 links.

For each plane, a plaquette whose base vertex is not at a cube boundary in either of its two directions is internal. The numbers per block are

    internal plaquettes = 3m(m-1)^2,
    crossing plaquette incidences = 12m^2-3m,
    sum of crossing (r_p-1) incidences = 12m^2+6m.            (17)

Proof: per cube of base vertices there are 3m(m-1)^2 plaquettes meeting one block, 6m(m-1) meeting two, and 3m meeting three. Translation symmetry and double counting give crossing incidence 2[6m(m-1)]+3[3m] and influence incidence 2[6m(m-1)]+6[3m]. The link assignment uses only three different plaquette base vertices; there is no fourth diagonal block. These are general counting arguments, not an extrapolation of the checked sizes.

Give every internal plaquette any finite nonnegative coupling, including one equal to an arbitrarily large beta_t. Give crossing plaquettes coupling epsilon. Then D=(12m^2+6m)epsilon, and (3) is satisfied when

    epsilon <= 1/[16b(12m^2+6m)].                           (18)

This is a NONEMPTY, volume-uniform finite-Wilson family with extensive strong interactions. For example m=2 gives six internal plaquettes per block, 42 crossing incidences and influence count 60; epsilon<=1/(960b) suffices. Arbitrarily many such blocks are covered by the same constants.

But this is not an isotropic weak-coupling result: the connected interfaces have deliberately small couplings. Even granting the unattainably optimistic b=1, (18) demands epsilon=O(m^-2), not epsilon tending to infinity. The complete rough certificate (16) is much worse. Sending the fraction of internal plaquettes (1-1/m)^2 to one does not remove the weak interfaces or prove their irrelevance to physical propagation. This theorem cannot be used to silently alter the target's action.

## 8. Why separate physical block gaps are not enough for gluing

The block-kernel condition was imposed on COMPLETE block coordinates for a reason. Let B and its complement share boundary vertices but no links. First impose gauge invariance only at vertices internal to each region. The boundary group G_boundary still acts. Writing the resulting regional spaces as representations,

    H_B = direct_sum_rho M_B^rho tensor V_rho,
    H_ext = direct_sum_sigma M_ext^sigma tensor V_sigma,

the actual glued physical space is

    (H_B tensor H_ext)^(G_boundary)
      = direct_sum_rho M_B^rho tensor M_ext^(rho*).           (19)

For a product of boundary SU(2) groups, rho is a tuple of irreducibles. Formula (19) follows by averaging the shared boundary group and Schur orthogonality. Keeping only the trivial rho in each region keeps only one summand and need not be complete. No new matter field has been added: these labels describe how the original link functions transform at an artificial cut.

A minimal exact control uses a spatial circle split into two paths. Each path is a tree. If every vertex of a path, INCLUDING both boundary vertices, is gauged independently as for an isolated system, its invariant configuration functions are constants: successive vertex transformations gauge every tree link to I. Tensoring the two isolated singlet spaces therefore predicts only a vacuum.

In the glued circle, however, the two path holonomies A,B transform as

    A -> g0 A g1^-1,        B -> g1 B g0^-1,

and f=chi_(1/2)(AB) is invariant, nonconstant, Haar-centered and has norm one. Indeed AB is Haar under independent Haar A,B, so character orthogonality gives its mean and norm. Averaging independent regional boundary transformations annihilates this state, whereas the diagonal shared gauge group preserves it.

At zero spatial coupling on a circle of L links, the EXACT temporal transfer gives

    K f = [I_2(beta_t)/I_1(beta_t)]^L f.                     (20)

This follows by integrating each link's fundamental representation against the central temporal convolution. More generally the character chi_j of the full holonomy has multiplier [I_(2j+1)(beta_t)/I_1(beta_t)]^L. The gauge-reduced circle space is exactly the class-function space, so this also identifies its nonvacuum spectrum. Since successive Bessel ratios are below one, the fundamental character has the largest nonvacuum multiplier. Its gap is

    Delta_circle = -(L/tau) log[I_2(beta_t)/I_1(beta_t)].      (21)

At fixed L, large beta_t gives Delta_circle=(3L/(2 beta_t tau))(1+O(beta_t^-1)). Thus physically slow states can sit ENTIRELY in the summands lost by a separate block-singlet projection. This is a gluing obstruction, not a counterexample to four-dimensional Yang–Mills. The circle/cylinder convolution is established mathematics and closely related to U034; the new use here is to audit the domain of the proposed strong-block certificate.

It follows that a future improvement of (2) must retain the necessary boundary representations or provide a separate uniform coercivity estimate for every omitted sector. A computation of only the isolated closed-block glueball gap is not such a certificate.

## 9. Temporal anisotropy does not rescue U036 by itself

For clarity this is a NECESSARY COEFFICIENT-MATCHING diagnostic, not a construction of the Hamiltonian limit. For fixed spin j, the positive-axis Bessel expansion gives

    I_(2j+1)(beta_t)/I_1(beta_t)
      = 1 - 2j(j+1)/beta_t + O_j(beta_t^-2).

To match the inherited Hamiltonian electric coefficient g^2/(2a), and magnetic coefficient 4/(g^2 a), temporal refinement must have

    beta_t tau -> 4a/g^2,       beta_s/tau -> 4/(g^2 a),
    beta_t beta_s -> 16/g^4.                                (22)

U036 requires beta_t beta_s<=1/576 when beta_t>=1. Under (22) this would require g^4>=9216. Therefore taking a smaller tau cannot, by itself, turn that sufficient domain into a weak-g domain. This is not an upper bound on where the actual theory can be gapped, and no conclusion about renormalized anisotropy or the four-dimensional continuum follows. It only removes a possible parameter-rescaling loophole in our particular estimate.

## 10. Sources, tests, and self-audit

Primary sources inspected on 2026-09-15:

- Rebeschini and van Handel, *Comparison Theorems for Gibbs Measures*, arXiv:1308.4117v1, Definitions 2.2-2.3, Theorem 2.4, Corollary 2.8, and the coupled-update proof in Section 3.2. Source https://arxiv.org/html/1308.4117v1 . Our dictionary is sites=(spatial link block,time), update regions=whole finite time columns, indicator metric, W=I, R<=J in (10). The joint couplings and convergence hypotheses are proved in Sections 4-5; the source is not imported as a Yang–Mills theorem. This is an established comparison method, not a novelty claim.
- Donnelly, *Decomposition of entanglement entropy in lattice gauge theory*, arXiv:1109.0036v2, Phys. Rev. D 85, 085004 (2012), DOI 10.1103/PhysRevD.85.085004. Source https://arxiv.org/html/1109.0036v2 . Section II, equations (8)-(9), (13)-(14), and (18), was checked: regional states obey interior constraints while boundary representations remain available for gluing. The regional boundary-charge structure is contextual overlap; our split-at-vertices formula (19) and circle test are derived directly, not identified without translation with the paper's split-link entropy construction.
- NIST DLMF 10.40.1, source https://dlmf.nist.gov/10.40 . Used only for FIXED representation and positive beta_t tending to infinity in (21)-(22), not for any all-representation spectral-tail claim. U036's all-character estimate remains separately preserved.
- CMI's current Yang–Mills page was read and still labels the problem unsolved: https://www.claymath.org/millennium/yang-mills-the-maths-gap/ . No publication, submission, new spending, or external contact was initiated.

The Birkhoff/Hilbert-metric mechanism is established mathematics; Section 6 includes a direct proof of the equality actually needed. No new external Birkhoff theorem is assumed from a search snippet.

Checker: `checks/U037_interacting_block_checks.py`. Ten focused tests pass in exact Fraction/SymPy arithmetic. They check tilings (N,m)=(4,1),(4,2),(6,3),(8,4); strong internal weights 1,16,10000 in a four-state binary reference; all-entry cross ratios at powers 1,2,4,12; correlated terminal messages; an exact interface sandwich; a 1024-path local-tilt control; comparison constants; Q8 boundary-gluing algebra; coefficient matching; and deliberate invalid inputs. Binary and Q8 populations are not Wilson measurements. They neither replace continuous SU(2) integration nor certify the all-volume theorem. Those claims have the written proofs above. The source of the smallness constant is (8)-(11), not a fitted spectrum.

All twelve U036 checks were rerun into NEW `evidence/U037_previous_checks.json` and its log; no earlier evidence was overwritten. Both suites passed on the first local run, with Python 3.13.5 and SymPy 1.14.0, exact arithmetic and 45-second wall caps. Compilation and indentation checks passed. The ruff, mypy, pyright and Lean executable/module checks were negative; no static-analysis or formal-verification success is claimed.

Wolfram 15.0.1 corroborated cross-ratio powers, the bridge coefficient 19/61, the four boundary/incidence counts and the weighted-influence value 1/2 in a clean stateless 20-second call. An initial call emitted an undefined-symbol warning concerning a localized matrix symbol while returning the expected expressions; that warning is preserved in `evidence/U037_wolfram_cross_checks.json`, and a symbol-safe rerun returned four true power checks without warnings. Its finite submitted algebra does not independently verify the universal theorem. Neither test counts nor the commit hash establish a mathematical proof; the claim remains self-reviewed with the explicit external comparison-theorem dependency above.

Audit verdict: **proved after the finite-SU(2), complete-block-kernel and weak-interface restrictions (2)-(3)**; self-review only. The universal choice (16) discharges (2) for any finite internal couplings, with explicitly poor size/coupling scaling. The theorem includes U036 as a special case and enlarges the allowed internal spatial backgrounds, but it does not close the weak-coupling problem.

Passed: preservation of the true vacuum and all physical sectors; explicit all-boundary kernel condition; exact treatment of internal interactions; joint full-path coupling; correct comparison-theorem dictionary; all-time influence summation; full-centered spectral inference; strong-interior example; explicit interface deterioration; boundary-singlet falsification; temporal-unit audit.

Still unproved: a useful intrinsic block estimate retaining boundary charge sectors at physical scales; a covariance-sensitive interface influence smaller than its worst-case oscillation; strong-interface overlap control in the actual vacuum; the joint continuum/infinite-volume construction and all-group mass gap.

Next executable target: replace A_BC in (1) by a rigorously controlled boundary-response operator in the full boundary-charge decomposition (19). Test an interface carrying the fundamental boundary representation before discarding any channels. To advance toward isotropic weak coupling, the estimate must improve the product of block mixing time and interface influence—not merely the internal block gap or the fraction of strong plaquettes.

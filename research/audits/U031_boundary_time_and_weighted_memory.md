# U031 — boundary-time data, invisible slow tails, and a weighted-memory certificate

Date: 2026-09-15. Base: private `Joe-Simo/yang-mills-mass-gap` commit `c6b168b768ed1a10947ad3ace50e24c1672b8b1b` (U030).

**We have not solved the Yang–Mills problem yet.**

Evidence: self-reviewed proofs for bounded positive transfers and an explicitly defined finite SU(2) Wilson transfer; exact rational/polynomial checks. No formal verification, independent expert review, novelty claim, scale-uniform physical mass estimate, or continuum construction.

## 1. Target, scope, and the first unproved implication

U030 left the task of retaining boundary-time information while controlling memory of discarded states, without assuming a discarded-sector gap. This unit tests three distinct implications: whether a finite list of exact time correlations can exclude arbitrarily slow states; whether small integrated memory can do so; and what complete, correctly weighted boundary criterion would actually suffice. It also constructs the full finite-regulator Wilson slab kernel and derives an elementary true-vacuum bound to expose its volume dependence.

The answer is not a new Yang–Mills mass bound: finite moment data are insufficient in general, and even a vanishing total unweighted memory can miss a collapsing gap. A weighted all-time criterion, with a condition excluding completely unobserved states, does give a precise replacement. Its hypotheses remain unproved uniformly for the interacting Yang–Mills vacuum.

The assigned folder and U030 archive were inspected before work. Forty-eight missing files were restored without replacement, two existing files matched, and all nine U030 manifest hashes matched. There is no local Git checkout, applicable AGENTS file, or executable Mathbox ledger in this workspace. The dedicated remote head was pinned. The supplied Yang–Mills prompt was retrieved; isolation, private-write authorization, zero-spend limit, and the full existence-and-gap target are unchanged. No older disputed scalar-localization claim is an input here.

Conventions: the physical time step is tau>0. A normalized transfer T preserves a normalized vacuum Omega; S denotes its restriction to the ENTIRE centered space H0=Omega-perp. Thus 0<=S<=I. When T comes from a Hamiltonian, T=exp[-tau(H-E0)], and an upper edge S<=qI with q<1 gives a physical gap at least -log(q)/tau. Operator positivity and entrywise/kernel positivity are different properties; where both are used below they are proved separately.

## 2. A full finite Wilson boundary kernel, not a static-cluster proxy

Fix a finite periodic spatial cubic graph with side N>=4, with Ne links and Np spatial plaquettes. Put X=SU(2)^Ne with normalized product Haar measure mu. The physical space is the invariant subspace of L2(X,mu) under vertex gauge transformations. For beta_s>=0 and beta_t>0 define

    W(U)=sum_spatial_p [1-(1/2)ReTr U_p],
    K0(U,V)=exp[-beta_s W(U)/2]
             * product_e exp[-beta_t(1-(1/2)ReTr(U_e V_e*))]
             * exp[-beta_s W(V)/2].                       (1)

The isotropic Wilson choice is beta_s=beta_t=beta. The unequal parameters only display the spatial/temporal normalization separately; no altered continuum theory is asserted. Let P_G be Haar averaging over vertex gauge transformations. K0 commutes with the simultaneous gauge action, and its restriction to the invariant space is equivalently represented by the gauge-averaged kernel

    K(U,V)=integral_Gvertices K0(U,g.V) dg.                (2)

All integrations here retain COMPLETE spatial boundary configurations. Multiplying these kernels and integrating complete intermediate slices is exactly operator composition. Hence retaining every boundary variable across a slab of m time steps gives T^m, not (P T P)^m for a further spatial projection P. This distinction is the one U030 identified.

For completeness, the elementary operator facts needed here can be checked directly. The one-link function exp[(beta_t/2)chi_1(U)] has strictly positive character coefficients: expand the exponential uniformly, decompose tensor powers of the fundamental character with nonnegative integral multiplicities, and note that every SU(2) irrep occurs in some such power. Convolution therefore has strictly positive eigenvalues by Peter–Weyl orthogonality. The field-independent factor exp(-beta_t) is harmless. Products of those convolutions and multiplication by the bounded positive function exp[-beta_s W/2] give a bounded, compact, self-adjoint, injective positive operator before gauge projection. Its restriction to the physical space remains injective and positive. Gauge projection has a kernel on the nonphysical space, so the logarithm is taken only AFTER restriction.

The kernel is continuous and pointwise strictly positive, and

    c := exp[-2 beta_s Np-2 beta_t Ne] <= K(U,V) <= C:=1. (3)

These estimates follow from 0<=W<=2Np and the corresponding temporal deficit bound, and survive the gauge average. Compactness supplies a positive top eigenvalue lambda0. Replacing an eigenfunction by its modulus cannot lower its top Rayleigh quotient; strict positivity of the kernel excludes two independent top eigenfunctions or a varying complex phase. Thus there is a unique normalized positive ground eigenfunction psi. Its eigenvalue equation makes psi continuous and strictly positive everywhere. Uniqueness and gauge covariance make it gauge invariant. In particular, psi has a positive minimum at each FIXED finite graph and finite coupling. No uniform lower minimum in graph size or beta is inferred.

The positive self-adjoint physical transfer normalized by lambda0 defines H-E0=-tau^-1 log(T/lambda0), generally UNBOUNDED above, by spectral calculus. No assumption that this logarithm is bounded is used.

### A finite-regulator lower bound and its actual deterioration

For any symmetric positive kernel satisfying 0<c<=K<=C on a probability space, normalize ||psi||2=1 and write M=int psi dmu. The eigenvalue equation implies

    psi(U) <= C M/lambda0,    lambda0>=c,    M<=1.

The ground-state transformed Markov kernel has stationary law pi=psi^2 mu and density relative to pi

    k_psi(U,V)=K(U,V)/(lambda0 psi(U)psi(V)).

Consequently

    k_psi(U,V) >= c lambda0/(C^2 M^2) >= (c/C)^2=:eta.  (4)

It is reversible and preserves constants. Write its Markov operator as eta Pi+(1-eta)R, where Pi is expectation in pi and R is another reversible Markov contraction. On centered functions its norm is at most 1-eta. Applying (3) gives the valid, but very weak, finite-regulator physical bound

    Delta_finite >= -log(1-eta)/tau,
    eta=exp[-4 beta_s Np-4 beta_t Ne].                    (5)

This controls the true vacuum and all physical states, not a trial compression. For a periodic N^3 spatial lattice, Ne=Np=3N^3. In the isotropic case eta=exp[-24 beta N^3]. At fixed positive physical side ell=N a and tau=a, this lower BOUND tends to zero under refinement even for fixed positive beta, and also along beta tending to infinity. The deterioration of a lower bound is NOT a proof that the actual gap tends to zero. Formula (5) is included precisely to prevent promoting compact finite-volume positivity to a continuum mass estimate.

### Completeness of the full boundary algebra

At a fixed regulator, continuous gauge-invariant functions are dense in the physical L2 space: approximate by continuous functions and apply the compact gauge average, which is a contraction. Equivalently one may use gauge-averaged finite Peter–Weyl polynomials. Since multiplication by psi is boundedly invertible at that fixed regulator, vectors O psi from the full continuous invariant boundary algebra are dense. Centering those vectors gives a dense subspace of H0.

This proves completeness for the FULL boundary algebra, not for finitely many Wilson loops, a compressed coordinate algebra, or the time translates of one selected observable. Keeping the full algebra can retain the full problem rather than simplify it. No uniform conditioning or continuum density theorem follows from this finite-regulator observation.

## 3. Exact boundary-time Gram criterion

Let P be any orthogonal projection on H0, K=range(P), Q=I-P, and

    M_k=P S^k P restricted to K,    M_0=I_K.

Define X_N:K^(N+1)->H0 by

    X_N(f_0,...,f_N)=sum_(j=0)^N S^j f_j.

The block Hankel and shifted block Hankel operators are

    H_N=[M_(i+j)]_(i,j=0)^N=X_N* X_N,
    K_N=[M_(i+j+1)]_(i,j=0)^N=X_N* S X_N.              (6)

Here the symbol K_N is a block operator, not the configuration-space kernel (2). Both are positive and K_N<=H_N. No inverse of H_N is assumed; it may have a nontrivial null space.

Let H_cyc be the closure of the linear span of all S^j K. It is reducing for bounded self-adjoint S. For every fixed q in (0,1),

    q H_N-K_N>=0 for EVERY N
       iff S restricted to H_cyc <= q I.               (7)

Proof: the left quadratic form is exactly <X_N f,(qI-S)X_N f>. Its positivity on all finite sums extends by continuity to H_cyc. The converse is immediate. If H_cyc=H0, this gives the full centered spectral edge. Without that hypothesis it leaves the orthogonal reducing space untreated. Mere absence of a visibly missing eigenvector in a computation is not a density proof.

The finite-depth generalized Rayleigh values

    r_N=sup_{f:<f,H_N f> >0} <f,K_N f>/<f,H_N f>

satisfy r_N increasing to ||S|H_cyc||. This follows from the nested ranges of X_N and their dense union. Therefore r_N is a LOWER estimate of the upper transfer edge, and -log(r_N)/tau, when defined, is an UPPER estimate of the gap on the cyclic space. Finite moment matrix calculations naturally have the same direction as Ritz approximations. They cannot be reported as positive lower mass certificates without a separate upper-edge argument.

### A finite exception: exact closure, not numerical stabilization

When K is finite dimensional and rank H_(N+1)=rank H_N exactly, range X_(N+1)=range X_N. Since S range X_N is contained in range X_(N+1), this finite-dimensional subspace is invariant and hence reducing. It equals H_cyc; the generalized eigenvalues of (K_N,H_N) on its nonnull quotient are exact there. A separate assertion H_cyc=H0, or a bound on the complement, is still required. Small singular values or apparently stable decimal eigenvalues do not establish the exact rank equality.

## 4. Every prescribed finite moment horizon can hide a slow, observable state

The following construction refutes the general claim that sufficiently many finite exact two-time moments must certify a strictly positive mass edge. It does not say that EVERY moment list is ambiguous; the exact finite-closure exception above remains valid.

Fix any integer M>=0 and rational s in (1/2,1). Set

    x_i=(i+1)/[2(M+2)],  i=0,...,M,
    mu0=(1/(M+1)) sum_i delta_(x_i).

Every x_i lies strictly between zero and 1/2. Define the exact rational Lagrange interpolation coefficients

    ell_i(s)=product_(j!=i) (s-x_j)/(x_i-x_j),
    epsilon=1/[2(M+1)(1+max_i |ell_i(s)|)],
    w_i=1/(M+1)-epsilon ell_i(s),
    mu1=sum_i w_i delta_(x_i)+epsilon delta_s.           (8)

The empty product for M=0 is one. Each w_i>=1/[2(M+1)]>0. Since sum ell_i(s)=1, mu1 is a probability measure. Polynomial interpolation gives, for every k=0,...,M,

    sum_i ell_i(s) x_i^k=s^k,
    integral x^k dmu0=integral x^k dmu1.                (9)

Thus all those moments are EXACTLY equal, not merely close within error bars. Nevertheless sup supp(mu0)<1/2 while sup supp(mu1)=s can be arbitrarily close to one.

Realization: on L2(mu_i), let S_i multiply by x and let f=1. The vector f is cyclic because all nodes are distinct and all weights are positive; polynomial interpolation reaches every function on the finite support. Adjoin a separate one-dimensional vacuum with transfer eigenvalue one. All eigenvalues are positive, so these are valid finite positive self-adjoint quantum transfers with unique vacua. The Hermitian observable O=|f><Omega|+|Omega><f| is centered and has two-time correlator <Omega,O T^k O Omega>=integral x^k dmu_i. Its cyclic subspace contains the slow state. These are auxiliary quantum models, not asserted Wilson measures, Markov realizations, or Yang–Mills counterexamples.

Taking M=2N+1 makes both H_N and K_N in (6) identical in the two models, despite arbitrarily different lower mass edges. The difference is detected at larger depth by the explicit polynomial

    p(x)=product_(i=0)^M (x-x_i).

For q=1/2,

    integral (q-x)|p(x)|^2 dmu0=0,
    integral (q-x)|p(x)|^2 dmu1
      =epsilon(q-s) product_i(s-x_i)^2 <0.              (10)

This supplies a concrete missing higher-time test. Small weight on a slow state is not the same as absence of the state. No finite-data algorithm can uniformly guarantee a positive edge for all positive transfers from these ambiguous data alone.

## 5. Even total UNWEIGHTED memory can vanish while the physical gap collapses

This second example has the stronger entrywise Markov property and uses an ACTUAL conditional-expectation projection. In the Walsh basis from U030, with Euclidean-normalized vectors

    Omega=(1,1,1,1)/2, u=(1,1,-1,-1)/2,
    v=(1,-1,1,-1)/2, w=(1,-1,-1,1)/2,

put, for every 0<e<=1/4,

    T_e=Omega Omega*+(u u*+w w*)/4+(1-e)v v*
             +(e/4)(u v*+v u*),
    P_full=Omega Omega*+u u*.                            (11)

In the original state coordinates the matrix is

    [5/8-e/8,   e/4,       3/8-e/4,   e/8      ]
    [e/4,       5/8-3e/8,  3e/8,      3/8-e/4  ]
    [3/8-e/4,   3e/8,      5/8-3e/8,  e/4      ]
    [e/8,       3/8-e/4,   e/4,       5/8-e/8  ].

It is symmetric, all row sums are one, and every entry is at least e/8. The projection averages the two pairs {1,2} and {3,4}. On the centered span of u,v the transfer is

    [[a,b],[b,d]],   a=1/4, b=e/4, d=1-e,

and on w it is 1/4. Both this 2x2 block and its complement to I are strictly positive:

    ad-b^2=(4-4e-e^2)/16>0,
    (1-a)(1-d)-b^2=e(12-e)/16>0.

Thus T_e is also strictly positive as an operator, and has a unique vacuum. Let lambda_+ be its largest centered eigenvalue. Then

    lambda_+=(a+d+sqrt((d-a)^2+4b^2))/2,
    e-e^2/8 <= 1-lambda_+ <= e.                         (12)

For the lower estimate, lambda_+-d=b^2/(lambda_+-a)<=b^2/(d-a)<=e^2/8; d-a>=1/2. The physical gap -log(lambda_+)/tau therefore tends to zero as e tends to zero.

Retain only u in the centered space. The other centered block is D=diag(1-e,1/4) and B=(e/4,0). The exact memory kernels are

    N_k=B D^k B*=e^2(1-e)^k/16,
    M_2-A^2=e^2/16,
    sum_(k>=0) N_k=e/16 ->0.                            (13)

The coarse transfer A remains exactly 1/4. Hence even the ENTIRE unweighted integrated memory and the one-step mixing norm can be arbitrarily small while the full gap collapses. The slow state is not completely dark: b>0, and span{u,S u}=span{u,v}. The unused w direction has fixed transfer eigenvalue 1/4.

For any fixed q<1, eventually d=1-e>q, and the exponentially weighted series sum q^(-k-1)N_k diverges. Its long duration matters even when its total unweighted amplitude is small. The exact shifted Schur condition in U030 required q>||D||; one cannot delete that restriction by evaluating only at q=1.

## 6. A gap certificate using observable weighted memory, without assuming a discarded-sector gap

Continue with an arbitrary bounded positive centered transfer

    S=[[A,B],[B*,D]],   0<=S<=I.

Define the discarded space reachable from the retained variables as

    H_B=closure span{D^j B* x : j>=0, x in K}.

It is reducing for D. Its orthogonal complement is annihilated by B and is consequently a reducing, completely unobserved part of S. To cover the entire physical space, require H_B=range Q; alternatively bound this dark complement separately. This is an observability/density hypothesis, not a gap assumption.

**Weighted-memory criterion.** Under H_B=range Q, for fixed 0<q<1 the following are equivalent:

    S<=q I;

    for EVERY m>=0,
    sum_(k=0)^m q^(-k-1) B D^k B* <= q I-A.            (14)

Unlike the inverse formula in U030, (14) does not assume q-||D||>0 or a bounded inverse at q. It remains valid at the boundary ||D||=q.

Proof of sufficiency: all summands are positive. Let E_D be the spectral resolution of D. For every retained x, the positive measure nu_x(J)=||E_D(J)B*x||^2 has moments <x,B D^k B*x>. Boundedness of the partial sums in (14) implies each kth summand is bounded by the same finite form. On [q+epsilon,1] this forces nu_x to be zero, by letting k tend to infinity in ((q+epsilon)/q)^k. Observability then gives D<=q I on all of range Q. For every h>0, the resolvent at q+h is bounded and its positive expansion obeys

    B[(q+h)I-D]^-1 B*
      =sum_(k>=0)(q+h)^(-k-1) B D^k B*
      <= q I-A <= (q+h)I-A.

Completion of the square now proves S<=(q+h)I. Let h decrease to zero to obtain S<=qI. This limiting argument does not invert qI-D.

Proof of necessity: S<=qI implies D<=qI. Apply the ordinary Schur identity to (q+h)I-S for h>0. The resolvent memory is at most (q+h)I-A. Each finite partial sum with weights (q+h)^(-k-1) is bounded by that positive resolvent series. Sending h down to zero for a fixed finite m gives (14). Necessity does not require observability.

A convenient sufficient all-tail input is

    A<=a I,   0<r<q<1,
    B D^k B* <= C r^k I for EVERY k>=0,
    a+C/(q-r)<=q,                                      (15)

together with observability. The geometric sum proves (14). For a split after m terms its remaining weighted tail is at most

    C (r/q)^(m+1)/(q-r).                                (16)

The all-k estimate in (15) also proves D<=r on H_B by the same spectral-measure argument, rather than assuming it. These are conditional sufficient criteria, not automatic decay from positivity. Establishing a cutoff-and-volume-uniform r<1 for the ACTUAL memory is a substantive part of the mass-gap problem.

### An infinite-dimensional example where the weighted criterion is stronger

The boundary case is not merely formal. Take q=3/4, K=C, QH=ell2(N),

    A=1/4, D e_n=(3/4-1/(4n))e_n,
    B*1=sum_(n>=1) (1/(8n^2))e_n.                       (17a)

Then D>=1/2, ||D||=q, and qI-D has no bounded inverse. Nevertheless

    B D^-1 B* <= (1/32)sum n^-4 <=1/24 < A,
    sum_(k>=0) q^(-k-1) B D^k B*
      =sum_(n>=1) [1/(64n^4)]/[1/(4n)]
      =(1/16)sum n^-3 <=3/32 < q-A.                    (17b)

The bounds use sum n^-p <=1+integral_1^infinity x^-p dx for p>1. The first Schur inequality proves S>0; the second and (14) give S<=q. Observability holds: every isolated diagonal eigenvalue d_n can be selected by a continuous function on the compact spectrum, then uniformly approximated by polynomials; all components of B*1 are nonzero. Their finite linear combinations are dense in ell2. Conversely, vectors (0,e_n) have Rayleigh quotient d_n tending to q, so ||S||=q exactly. Adjoining a separate vacuum therefore gives gap -log(3/4)/tau on this auxiliary infinite-dimensional model.

Its weighted memory after m terms has an explicit full-tail bound:

    R_m=(1/16)sum_(n>=1) n^-3 (1-1/(3n))^(m+1)
       <=3/[8(m+1)].                                    (17c)

Indeed (1-u)^k<=1/(1+ku)<=1/(ku) for 0<u<1,k>=1, by Bernoulli's inequality applied to (1-u)^-k. Use u=1/(3n) and sum n^-2<=2. Thus a finite memory computation PLUS a proved all-tail estimate can certify the bound without a strict separation ||D||<q. No estimate N_k<=C r^k with r<q can hold here: each d_n>r with nonzero coupling would eventually violate it. This distinguishes the general weighted criterion (14) from the stronger geometric sufficient condition (15), and from the finite-data-only impossibility in Section4. The model is not a lattice gauge theory or a proposed QFT.

### How the memory is recoverable from boundary correlations

U030's exact recurrence implies, with N_k=B D^k B*,

    N_0=M_2-A^2,
    N_n=M_(n+2)-A M_(n+1)-sum_(j=1)^n N_(n-j) M_j.     (17)

This formula preserves the displayed multiplication order; retained matrices need not commute. Thus boundary correlations determine finite memory kernels exactly, but (14)-(16) still require an all-time theorem or certified tail, not extrapolation of those kernels. The checker verifies (17) for a noncommuting two-dimensional retained compression.

Without observability a one-dimensional dark block with eigenvalue 63/64 defeats a proposed q=3/4 certificate even when every N_k is zero. The observable bound alone makes no claim about that block. In the family (11), the coupled slow direction instead defeats (14) itself; both failure modes are kept distinct.

## 7. What these results do and do not settle

The finite Wilson construction shows exactly where a complete boundary-time algebra lives and why retaining all of it keeps valid dynamics. Its elementary true-vacuum gap (5) has explicit bad volume/coupling dependence. The abstract criteria (7) and (14) identify what an improved retained description must establish: all-time control and coverage of all potentially slow states. Equations (8)-(13) rule out replacing those obligations by a long but finite list of exact correlations or by a small unweighted memory norm.

None of this proves a useful scale-uniform bound for the interacting four-dimensional theory. We have not bounded the memory coefficients of an actual spatially compressed Wilson slab, proved observability for the proposed restricted block algebra, or controlled the repeated generated interactions from U029-U030. No continuum/infinite-volume reconstruction, finite nonzero physical mass witness, or extension to every compact simple gauge group is supplied.

The next useful estimate should therefore be sought directly for centered physical slab observables: construct a gauge-invariant retained algebra rich enough to detect slow modes, then derive an exponential WEIGHTED tail such as (15), or a more flexible bound in (14), in its true vacuum. Integrate discarded slab interiors while keeping both boundary algebras and the covariance/memory terms; do not replace that operation by a tangent Wilson coupling. Any argument using typical rather than worst boundaries must separately control the probability and contribution of adverse boundaries in the full measure. The full boundary algebra provides a benchmark, not a computational reduction.

## 8. Source checks, finite evidence, and self-audit

**Primary source scope.**

- M. Luescher, *Construction of a selfadjoint, strictly positive transfer matrix for Euclidean lattice gauge theories*, DESY 76/54 (1976), institutional scan `https://bib-pubdb1.desy.de/record/396349/files/7611148.pdf?version=1`; subsequent publication Commun. Math. Phys. 54 (1977), 283-292, DOI 10.1007/BF01614090. The title, Section II B, Proposition 1, equations (20)-(23), printed pp.8-9, and Section II C, Proposition 2, printed pp.10-11 were read in rendered pages (PDF indices6-7). They supply classical context for the finite Wilson transfer and reconstruction, not a continuum gap theorem. The scan treats a broader quark/gluon setup; our pure-gauge construction is given directly in (1)-(3). The scan's sentence calling H bounded is NOT adopted: the logarithm of an injective compact infinite-dimensional transfer is generally unbounded above. The properties imported as context are those of T, not a bound on H.
- J. B. Lasserre, *Bounding the support of a measure from its marginal moments*, arXiv:1011.0138v1, 31 October2010; `https://arxiv.org/pdf/1011.0138v1`. Proposition3.2, equation(3.2), printed p.3, and Section3.2/Theorem3.3, printed p.5 were checked in parsed text and screenshots. Versioned-PDF screenshot calls first failed; the unversioned endpoint displayed the same v1 and rendered successfully. The scalar compact-support version of (7) is known after translation: x is a transfer eigenvalue in [0,1], and q H_N-K_N is the localizing matrix for q-x. The finite largest-support estimates are inner/Ritz estimates, not certified upper support bounds. The v1 p.5 display(3.8) omits the minus used in (3.2) and its own following explicit matrix; and Theorem3.3(ii) prints a* where the upper-endpoint context requires b*. We rely on the directly proved compact-support statements above, not those typographical inconsistencies or an unrestricted noncompact moment-determinacy claim.
- CMI current Yang–Mills page was checked in this run and still lists the problem as unsolved: `https://www.claymath.org/millennium/yang-mills-the-maths-gap/`. The official full target is unchanged; no publication, submission, acceptance, or prize assertion is made.

The Schur, moment, positive-kernel, and transfer constructions are established mathematical mechanisms. No global or scoped novelty claim is made. These sources authenticate context and the named notation translations; the new assembled criteria and examples have the explicit proofs here. Mathbox is workflow guidance, not an independent mathematical reviewer. Consensus's documented quota failure was not repeated. No paid jobs, external contacts, or background execution were initiated.

**Exact finite checks.** `checks/U031_boundary_moment_checks.py` uses Python3.13.5 and SymPy1.14.0, rational arithmetic and polynomial residuals. Thirteen focused tests pass. Tests cover parameter-symbolic matrix identities, actual conditional-expectation geometry, memory recurrence powers1-6, atomic moment orders M in {0,1,3,5,9} with s in {3/4,63/64}, matching Hankel depths0-3 with s=255/256, higher-polynomial witnesses, an exactly rank-stabilizing cyclic space, noncommuting block moments, a weighted-memory certificate and an explicitly dark negative control, a positive-kernel minorization example, and eight-node / eleven-tail-depth controls for the separately proved infinite-dimensional boundary example. These are neither Wilson-lattice numerical measurements nor universal proofs by finite enumeration; equations(1)-(17), including (17a)-(17c), supply the mathematical arguments and their restrictions.

Before promotion, tests caught and fixed three checker defects: an empty interpolation product caused Python floating division at M=0; structurally different but equal polynomials were compared as expression trees; and a characteristic-polynomial helper replaced a real-assumed symbol by an unassumed namesake. Exact SymPy division, zero-residual comparisons and det(zI-T) with the same symbol repaired them. Initial failure logs and code hashes are preserved. The new rational-type check includes the empty-product case. No theorem was changed to accommodate a failed example.

A stateless Wolfram15.0.1 call separately returned the characteristic polynomial, six zero memory residuals, four zero moment residuals, positive perturbed weights, the exact added weight 8192/13348707 for M=3,s=63/64, and zero finite-geometric-tail residual. The first call emitted internal singular-matrix/infinite-power warnings despite expected outputs; it is retained as nondecisive. A second call used direct repeated matrix multiplication and a finite geometric identity and returned without warnings. Neither is an independent proof of the whole argument.

All eleven U030 tests were rerun into a NEW log. Compilation and indentation checks of the new script pass. Ruff, mypy, pyright, Bun and Lean are not installed in this environment; no successful static lint/typecheck or formal verification is claimed. Manifest hash verification uses the existing project convention, not an unavailable Mathbox runtime validator.

**Self-audit verdict: proved after the stated finite-regulator / bounded-transfer restrictions.** Passed: sign and physical-time normalization; complete finite Wilson boundary space; strict operator versus kernel positivity; unique true finite vacuum; explicit minorization dependence; all-depth Gram identity with null spaces; correct direction of finite generalized eigenvalue estimates; arbitrary-horizon positive moment construction with a cyclic observable; positive reversible memory counterexample; shifted/weighted Schur condition including the boundary without a bounded inverse; and explicit dark-sector limitation. Open: the actual reduced Yang–Mills observability and weighted-tail estimates uniformly in cutoff and volume, repeated RG control, and the complete continuum target. No complete candidate exists.

# U028 — three-dimensional cube constraints and a nonlinear small-field test

Date: 2026-09-15. Base: `Joe-Simo/yang-mills-mass-gap`, private commit `8c03d35c20d265e0259c4c8e2be1d48b60e8a8c3` (U027).

**We have not solved the Yang–Mills problem yet.**

Status: self-reviewed auxiliary proofs, exact finite checks, and an explicitly identified Gaussian reference test. No formal verification, independent expert review, novelty claim, or continuum Yang–Mills theorem.

## 1. Target and scope

U027 established fixed planar-graph results and required a size-and-coupling-uniform estimate on actual spatial three-dimensional blocks. This unit executes three discriminating steps: (A) retain cube/Bianchi constraints and compute the complete free transverse spectrum; (B) derive a genuinely nonlinear Wilson-potential comparison with a size-independent constant in a specified small-field slice; (C) test the probability of that slice's norm condition in the quadratic vacuum. Step C does NOT assume that this vacuum approximates the true growing-volume interacting vacuum.

The assigned local folder and remote head were inspected. Missing U026/U027 files were restored from the supplied U027 archive without replacing existing files. U027's seven manifest hashes were rechecked. The original Yang–Mills prompt was retrieved from this conversation; the full existence-and-gap target, private-write permission and zero-spend boundary are unchanged. The workspace has no local Git checkout or executable Mathbox ledger. No sibling project was accessed. The current derivations do not rely on the older disputed scalar-localization sequence U009–U023.

Use the inherited normalization

    H(g,a)=(g^2/a) Hhat_lambda,
    Hhat_lambda=(1/2)sum_e C_e + lambda V(U),
    V(U)=sum_p[1-(1/2)Tr U_p],   lambda=4/g^4.

Here C_e has spectrum j(j+1). Every excitation gap is above the actual ground energy. Open box means all internal graph links are integrated, all vertex gauge transformations are imposed, and no external links/periodic twists are added.

## 2. Cubes are not independent plaquettes

Take an open product of paths with N1,N2,N3 cells. Let d0, d1=C, d2=B be vertex-to-edge, edge-to-face, and face-to-cube coboundaries, with orthonormal cell bases and their standard oriented incidence signs. Direct boundary cancellation gives

    C d0=0,   B C=0.

For a cubic N-by-N-by-N block the exact counts are

    vertices=(N+1)^3,
    edges=3N(N+1)^2,
    faces=3N^2(N+1),
    cubes=N^3.

The ranks are rank(d0)=vertices-1, rank(B)=N^3 and

    rank(C)=edges-vertices+1=faces-cubes=2N^3+3N^2.       (1)

The tensor proof below supplies exactness and these ranks; Euler counting alone would not suffice. In particular a single cube has six faces but only FIVE independent curl directions. Its face matrix has spectrum

    spec(CC*)={0 (once), 4 (three times), 6 (twice)}.      (2)

The zero vector direction is a Bianchi constraint, im(B*), not a physical zero-energy oscillator. Since im(C)=ker(B), one must restrict face fields to ker(B). Treating all faces as independent, or retaining this constraint direction as a physical state, both give the wrong model. BC=0 is the linearized constraint; exact nonabelian face relations require parallel transport and ordered products, not an unqualified sum of face logarithms.

## 3. Complete transverse spectrum on every rectangular box

For a path with Ni edges, its vertex Laplacian has eigenvalues

    nu_i(k)=4sin^2(pi k/[2(Ni+1)]),   k=0,...,Ni.

The k=0 vector is constant. For every k>0, applying the incidence matrix to the normalized vertex eigenvector and dividing by sqrt(nu_i(k)) gives a normalized edge eigenvector. These form all edge modes. The vertex modes can be checked by the cosine recurrence, and their gradients by the sine recurrence.

Tensor these paired vertex/edge modes. For a tuple k, let s be the number of positive k_i, let p_i=sqrt(nu_i(k_i)) on active directions, and let Lambda_k=sum_i nu_i(k_i). In the corresponding s-dimensional one-form block, d0 is the vector p and d1 is exterior multiplication by p. Hence

    d1* d1=Lambda_k I-p p*,
    (d1* d1)|_(p-perp)=Lambda_k I.                       (3)

For s=1 there is no transverse mode. For s>=2 the positive curl eigenvalue Lambda_k has multiplicity s-1. The associated Koszul complex is exact for every nonzero p, which also proves (1) and im(C)=ker(B); the only degree-zero exception is the constant vertex mode.

Thus the complete positive spectrum is

    mu(k)=sum_i nu_i(k_i), multiplicity s(k)-1,
    k_i in {0,...,Ni},   s(k)>=2.                        (4)

There are no omitted harmonic one-forms on these contractible boxes. The minimum is

    mu_min=min_(i<j)[nu_i(1)+nu_j(1)].                   (5)

For equal sides N,

    mu_min=8sin^2(pi/[2(N+1)]), with multiplicity three.

This agrees in value, but not multiplicity or constraint structure, with U027's square planar patch. It is not the smallest scalar Neumann eigenvalue: a mode with just one positive momentum is a gradient and is removed.

## 4. Fixed-graph physical weak-coupling consequence

Write a small link as exp(i A_e.sigma). At identity the electric operator has principal part -(1/8)Delta_A and the magnetic quadratic form is (lambda/2)||C A||_2^2. Quotient infinitesimal vertex gradients using the Euclidean orthogonal slice ker(d0*). Singular-value decomposition of C gives one three-component color oscillator for each eigenvalue in (4). Its frequency in Hhat is sqrt(lambda mu)/2.

Residual simultaneous SU(2) conjugation acts as SO(3) on every color vector. A single oscillator quantum is not invariant. Two quanta in a lowest-frequency color vector have an invariant scalar component. Thus the singlet oscillator excitation gap is sqrt(lambda mu_min), not half that value.

This is also the leading gap of the COMPLETE physical Hamiltonian for each fixed finite box. The justification is the fixed-dimensional argument used in U027, with its hypotheses checked here:

* A rooted maximal-tree gauge fixing leaves r=edges-vertices+1 SU(2) loop variables with product Haar measure and residual common conjugation. Keeping that invariant subspace retains mixed-loop states. Non-tree link derivatives provide an elliptic kinetic form on the compact product group.
* The filled cube complex is simply connected; identity holonomy on every face makes every loop trivial. Consequently V has only the identity tuple as a zero in tree coordinates. Its Hessian is positive on the r loop directions by (3). Smoothness, compactness and the nondegenerate minimum give V>=c_graph dist^2 globally, with c_graph>0 allowed to depend on the graph.
* Put h=lambda^(-1/4). Compactly supported invariant oscillator trial functions, pulled back in the h-scaled logarithmic chart, give the min-max upper bounds. Haar density and kinetic coefficients converge on each fixed scaled compact set.
* Those upper bounds and V>=c_graph dist^2 give a uniform second moment for the rescaled low eigenfunctions at each fixed graph. A chart cutoff has vanishing scaled localization error. Ellipticity gives local H1 bounds; local compactness and the second-moment tail bound give strongly L2-convergent orthonormal subsequences. Weak lower semicontinuity and min-max in their invariant span give the matching lower bounds.

The comparison involves actual ground and first excited energies; it is not a lower-gap inference from a finite Ritz matrix. It proves

    lim_(g->0) a Delta_N(g,a)=2sqrt(mu_min)
      =4sqrt(2)sin(pi/[2(N+1)]) ~ 2sqrt(2)pi/(N+1).      (6)

For N=1 the coefficient is 4, and for N=2 it is 2sqrt(2). Constants in the convergence proof are NOT uniform in N. Equation (6) rules out a fixed positive coefficient c in a Delta_N>=c holding for every N and all sufficiently small g. It does not rule out a finite physical mass: a physical mass m corresponds to a Delta approximately a m, which itself tends to zero. Substitution N=ell/a into an uncontrolled fixed-N remainder is invalid.

## 5. An exact nonlinear small-field comparison with no box-size constant

This next lemma concerns the FULL Wilson magnetic potential, not its Taylor truncation. Its hypotheses are restrictive and must be stated precisely.

Let A_mu(x) in R^3 have finite support on positively oriented links of Z^3. Set U_mu(x)=exp(i A_mu(x).sigma). Write Q(x)=(sum_mu |A_mu(x)|^2)^(1/2), and use counting-measure norms. Assume the linear Coulomb condition

    d0* A=0.

This is a specified Lie-algebra slice, not an asserted global nonabelian gauge choice. For a finite-box application all nonzero links must lie in an interior collar so that zero extension introduces no extra magnetic faces. Arbitrary boundary data are not covered.

Define

    alpha=(32/sqrt(3)) ||Q||_3.

Then, whenever alpha<1,

    (1-alpha)^2 ||C A||_2^2/2 <= V(U)
       <= (1+alpha)^2 ||C A||_2^2/2.                     (7)

All constants are independent of support size. Here is a proof with explicit normalization and constants.

### 5.1 Exact product remainder

For a face p write its four signed edge matrices X_j=i(plus or minus A_e).sigma and P(t)=product_(j=1..4)exp(t X_j). Every factor is unitary. In normalized Frobenius norm |M|_F/sqrt(2), each term of P''(t) is bounded by the product of the corresponding |A_e|. Thus

    |P(1)-I-sum_j X_j|_F/sqrt(2)
       <= (1/2)(sum_(e in p)|A_e|)^2
       <= 2sum_(e in p)|A_e|^2.

For SU(2), |U-I|_F^2=4[1-(1/2)Tr U]. Combining the reverse triangle inequality on the direct sum of face matrix spaces with Cauchy-Schwarz therefore gives

    |sqrt(2V(U))-||C A||_2|
       <= 4sqrt(nu) (sum_e |A_e|^4)^(1/2)
       <= 8 ||Q||_4^2,                                 (8)

because an edge in Z^3 belongs to at most nu=4 faces. No smallness was used to obtain (8), and the product order/noncommutativity was retained.

### 5.2 Discrete Sobolev estimate, proved here

For nonnegative finitely supported v, bound v(x) by its total variation along each coordinate line. If a(y,z), b(x,z), c(x,y) denote those three line variations, then v(x,y,z)^(3/2)<=sqrt(abc). Two applications of Cauchy-Schwarz give

    sum_(x,y,z)sqrt(a(y,z)b(x,z)c(x,y))
       <= [(sum a)(sum b)(sum c)]^(1/2).

For example first sum in x, obtaining sqrt(B(z)C(y)), and then apply Cauchy-Schwarz in (y,z). Consequently

    ||v||_(3/2) <= (1/3)sum_i ||D_i v||_1.

Apply this to v=Q^4. For a,b>=0,

    |a^4-b^4| <= 2(a^3+b^3)|a-b|,

since 2(a^3+b^3)-(a+b)(a^2+b^2)=(a+b)(a-b)^2. Cauchy-Schwarz and translation invariance give ||D_i Q^4||_1<=4||Q||_6^3||D_i Q||_2. Dividing by ||Q||_6^3 (the zero field is immediate) proves

    ||Q||_6 <= (4/sqrt(3)) ||D Q||_2
             <= (4/sqrt(3)) ||D A||_2.

The discrete Hodge identity on finitely supported link fields is

    ||D A||_2^2=||C A||_2^2+||d0* A||_2^2.

It follows by expanding and summing by parts, or by the complex exterior-product identity at each Fourier frequency. The assumed divergence condition removes its second term. Finally Holder gives ||Q||_4^2<=||Q||_3||Q||_6. Substitution into (8) and squaring proves (7).

At ||Q||_3<=sqrt(3)/64, alpha<=1/2, so the explicit comparison is

    ||C A||_2^2/8 <= V(U) <= 9||C A||_2^2/8.             (9)

This is a nonlinear potential estimate, not a true-vacuum Poincare inequality or an excitation-gap comparison. It supplies no bound on the probability of the indicated field region and no control of the kinetic/vacuum errors. A local coefficient being uniform does not make its hypotheses typical.

## 6. Executed adversarial test: the norm condition is rare in the quadratic vacuum

Consider ONLY the exact Gaussian ground state of the transverse quadratic Hamiltonian on the open N-cube graph. There are D=3r real normal coordinates with r=2N^3+3N^2. In a mode with curl eigenvalue mu the ground wavefunction is proportional to exp(-sqrt(lambda mu) q^2). Its probability variance is

    v_mu=1/[4sqrt(lambda mu)]=g^2/[8sqrt(mu)].

By (4), mu<=12, hence v_mu>=v_min=g^2/(8sqrt(12)). This describes the invariant oscillator vacuum without discarding color-angle measure. The local coordinates are correlated; no independent-link assumption is made.

Let A be the orthogonal reconstruction from the normal coordinates. For Vtx=(N+1)^3 base vertices, Holder implies

    ||A||_2 <= Vtx^(1/6)||Q||_3.

Therefore ||Q||_3<=delta implies ||A||_2^2<=(N+1)delta^2. Coupling the independent normal coordinates to standard Gaussians Z_i gives pointwise ||A||_2^2=sum_i v_i Z_i^2>=v_min sum_i Z_i^2. Put

    tau=(N+1)delta^2/(D v_min)
        =16sqrt(3)(N+1)delta^2/[3r g^2].                 (10)

For 0<tau<1 the elementary negative-exponential Chernoff bound yields

    Prob_Gaussian(||Q||_3<=delta)
       <= (tau exp(1-tau))^(D/2).                       (11)

Indeed E exp(-s sum Z_i^2)=(1+2s)^(-D/2), and minimizing exp(s D tau)(1+2s)^(-D/2) gives s=(1/tau-1)/2. Since -log(tau)-1+tau>=(1-tau)^2/2, (11) is at most exp[-D(1-tau)^2/4]. In particular tau<=1/2 gives an upper bound exp(-D/16).

For fixed delta, if g_N N tends to infinity then tau tends to zero. This includes the explicitly DEFINED test sequence g_N^2=1/log(N+1); that definition is not a claim to have constructed the Yang–Mills renormalized trajectory. Thus the norm-only condition needed by (7) has probability tending to ZERO, not one, in this growing-graph Gaussian reference. The norm-only event is larger than the collar-supported slice, so boundary restrictions cannot rescue this particular probability argument.

This refutes using this global small-norm region as a dominant Gaussian reference sector on those joint scales. It does NOT establish its probability in the true interacting vacuum, prove a gapless nonabelian continuum, or invalidate (7). It identifies a concrete obstacle: a useful proof must integrate short-wavelength quantum fluctuations rather than demand a globally small bare field before applying the comparison.

## 7. Verification and interpretation

The focused checker uses exact integers, rationals and symbolic expressions in Python 3.13.5 / SymPy 1.14.0. All 13 tests passed. Complete cubical incidence matrices were checked for exactly (1,1,1), (2,1,1), (2,2,1), (2,2,2); their characteristic polynomials agree with the tensor formula, including gauge kernels and Bianchi ranks. Other tests cover orientation reversal, planar controls, invalid geometry, the exact curl symbol, a compactly supported transverse field, scalar oscillator eigenfunctions/variance, a noncommuting Wilson plaquette, and the Sobolev/Chernoff algebra. Universal conclusions use the written proofs, not finite extrapolation.

Wolfram 15.0.1 corroborated the supplied cube incidence matrix's rank five and polynomial t(t-4)^3(t-6)^2, the Bianchi and curl-symbol identities, Gaussian variance 1/(4z), and constants. It did not independently construct the graph, prove a spectral limit, or verify the nonlinear theorem. No warning was returned in this call.

The U027 suite (11 tests) and U026 suite (9 tests) were rerun. Compilation and indentation checks were run on the new checker. Static Python lint/typecheck tools and Lean were not installed; these checks are not claimed. See evidence/U028_validation.log and evidence/U028_manifest.json for actual commands, results and hashes. Mathbox supplies research/self-audit workflows, not independent expert approval. No additional Consensus result is claimed; its documented quota issue is not evidence about the literature.

External-source scope: the inherited planar Hamiltonian conventions and leading two-plaquette result were checked against Ale et al., arXiv:2410.14580v1, Sections II–IV, at https://arxiv.org/html/2410.14580v1 . That paper is a planar-model input, not a source proving (4), (7), or the continuum problem. The official status page https://www.claymath.org/millennium/yang-mills-the-maths-gap/ was checked on 2026-09-15 and continues to list the problem as unsolved. The present cubic tensor and nonlinear estimates were derived above; no literature-wide novelty assertion is made. No paper was published, no outside party contacted, no money spent and no asynchronous work started.

## 8. Self-audit and next mathematical dependency

Primary verdict: correct only under the explicit finite-graph, fixed-graph-limit, specified-slice, and Gaussian-reference restrictions above.

Passed: full transverse mode count; removal of constraint rather than physical states; fixed-graph singlet min-max limit; normalized Wilson remainder; discrete Sobolev/Hodge steps; exact Gaussian probability bound. Not established: uniformity of the nonlinear spectral remainder in N; nonlinear gauge-slice coverage; true-vacuum concentration; a centered kinetic/magnetic comparison after short-mode integration; continuum reconstruction and finite positive mass.

The strongest surviving new input is (7): a size-independent nonlinear magnetic comparison on a precisely controlled local fluctuation slice. Its first missing use in a mass-gap proof is NOT another spectral count: it is a true-vacuum, background-relative estimate after high modes are integrated, retaining the slow loop sector. Equation (11) rules out filling that gap by declaring the entire bare Gaussian field small.

Next executable test: conditional Gaussian integration of high modes around a retained low field, with the lowest nonabelian commutator interaction kept. Determine which induced quadratic terms are forbidden by gauge symmetry and which gauge-invariant effective terms remain; specify remainder and volume dependence before interpreting any apparent generated mass. The object must ultimately be compared to the centered interacting transfer/ground-state form, not just to a classical Hessian or Gaussian coefficient.

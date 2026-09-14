# U003 — Relative full-space gap transport and SU(2) initialization tests

**We have not solved the Yang–Mills problem yet.**

Date: 2026-09-14. Written proofs, self-review and exact auxiliary computations only. No complete candidate, formal verification, independent expert verification, or global novelty claim. This compact remote checkpoint records the mathematical content of the expanded local note `research/audits/U003_relative_gap_and_SU2_test.md`; the two presentations are not byte-identical.

## 1. Preserved state and scope

Resumed from private remote commit `99698a0c45c12a19e419cdd7fc1b7998ce6d4980`. Inspected the supplied U002 archive, expanded note, README and source records before restoring missing local files. No existing file was overwritten. Reran all ten U002 tests successfully. Repository privacy and the unchanged remote head were checked immediately before writing.

The exact Clay/Jaffe–Witten target remains a nontrivial four-dimensional Yang–Mills theory for every compact simple gauge group, including the required axioms, short-distance identification, infinite-volume continuum setting, and finite positive physical mass. Clay's current Yang–Mills page still lists it as unsolved. Sections 3–4 of the official description were re-read in rendered pages.

U002 rejected summable additive errors as sufficient for gap persistence. This run instead proves a conditional *relative* estimate on the entire centered state space, then tests a concrete Haar/electric starting point and a positive one-plaquette trial dressing. These are auxiliary results, not a continuum construction.

## 2. Coarse compression misses two independent obligations

Let S be a positive self-adjoint contraction representing one fixed physical time t0>0, with normalized vacuum Omega and S Omega=Omega. On Omega-perp put G=I-S; G is a transfer-deficit operator, not the Hamiltonian. Decompose the centered space as Hc direct-sum Hf, retaining the whole complement, and write

    G = [[A,B],[B*,D]].

An estimate on A alone says nothing about D or the mixed block B.

### Exact hidden-sector counterexample

Define M(r)=[[1+r,1-r],[1-r,1+r]]/2 and, for 0<epsilon<=1/2,

    S_epsilon=M(1/2) tensor M(1-epsilon).

This is a symmetric strictly positive-entry Markov matrix and a positive self-adjoint contraction. Its eigenvalues are 1, 1/2, 1-epsilon, (1-epsilon)/2. It has a unique vacuum at every positive epsilon. For Jf=f tensor (1,1)/sqrt(2),

    J*J=I, J*S_epsilon J=M(1/2), S_epsilon J=J M(1/2).

Thus the coarse compression is exact, with zero mixing error and fixed centered norm 1/2, but the full centered norm is 1-epsilon. At t0=1 its full Hamiltonian gap tends to zero as -log(1-epsilon). This finite example's limit has a degenerate vacuum; U002 separately supplied a unique-vacuum infinite-dimensional example. Neither is a Yang–Mills counterexample.

### Exact mixed-sector counterexample

On a two-dimensional centered space take S_epsilon=[[1/2,1/2-epsilon],[1/2-epsilon,1/2]], with 0<epsilon<1/2, and adjoin a separate vacuum eigenvalue one. Both diagonal compressions have norm 1/2, yet the centered eigenvalues are 1-epsilon and epsilon. For G=I-S,

    |B|^2/(A D)=(1-2epsilon)^2 -> 1.

This is an abstract positive contraction, not asserted to have a Markov or Yang–Mills interpretation. It shows that two good diagonal bounds still require a mixed-block estimate.

## 3. Block certificate and quadratic mixing loss

If D-delta I is boundedly invertible and positive, completing the square proves

    G>=delta I
      iff A-delta I-B(D-delta I)^(-1)B*>=0.

Indeed the quadratic form of G-delta I at (x,y) is

    <x,[A-delta I-B(D-delta I)^(-1)B*]x>
      + ||(D-delta I)^(1/2)[y+(D-delta I)^(-1)B*x]||^2.

This gives both directions, taking y=-(D-delta I)^(-1)B*x for necessity. It applies to bounded operators on infinite-dimensional spaces under the stated inverse bound. In particular, A>=alpha I, D>=rho I, ||B||<=b certify any 0<delta<min(alpha,rho) satisfying (alpha-delta)(rho-delta)>=b^2.

The Schur/Feshbach mechanism is standard, not a new claimed method. Dusson–Sigal–Stamm, arXiv:2105.02058v1, Theorem 1.2 and equations (1.10),(1.15)–(1.16), were inspected in text and rendered printed pages 4–5. Our positive bounded-operator statements are proved here rather than importing their discrete perturbation theorem as a continuum Yang–Mills result.

Now assume for every coarse x and fine y that

    |<x,B y>| <= kappa sqrt(<x,A x><y,D y>),
    0<=kappa^2<1/2.

This is equivalent to ||A^(-1/2) B D^(-1/2)||<=kappa when A,D have positive lower bounds, but the form statement does not require using inverse notation. The square

    [sqrt(d/2)-sqrt(2) kappa sqrt(a)]^2>=0

implies 2kappa sqrt(ad)<=2kappa^2 a+d/2. Therefore

    G >= diag((1-2kappa^2)A, D/2).                       (R)

The factor two cannot simply be removed; a deliberate two-by-two failure is in the checker. Reserving half the fine-sector bound makes the loss on the coarse sector quadratic rather than linear in kappa. Positivity of the full G supplies at most kappa=1 by Cauchy–Schwarz for its form; strict quantitative control is not automatic.

## 4. Conditional transport theorem

Let S_j be normalized positive contractions at the same fixed physical time t0, with actual vacua Omega_j. Write G_j=I-S_j on the entire centered spaces H_j^0. Fix 0<d0<=1/2 with G_0>=d0 I. At each j>=1 let J_j:H_(j-1)^0 -> H_j^0 be an isometry with closed coarse range, extended in a vacuum-preserving way on the full spaces. Include every omitted state in the fine complement. Suppose the blocks of G_j obey

    A_j >= (1-eta_j) J_j G_(j-1) J_j*, 0<=eta_j<1;
    D_j >= 2d0 I;
    |<x,B_j y>| <= kappa_j sqrt(<x,A_j x><y,D_j y>),
        0<=kappa_j^2<1/2;
    sum_j(eta_j+kappa_j^2)<infinity.

Then

    G_j >= d_j I,
    d_j=d0 product_(i=1..j)(1-eta_i)(1-2kappa_i^2),
    d_infinity>0.

Proof: apply (R). The coarse lower bound is (1-eta_j)(1-2kappa_j^2)d_(j-1), and the fine lower bound is d0. Since the first is at most d0, induction gives the finite product. Every factor is positive. Eventually eta_j and 2kappa_j^2 are at most 1/2, so -log(1-u)<=2u and the summability assumption show the infinite product is positive; keep the nonzero finite prefix in any quantitative bound.

Illustrative coefficient data, not Yang–Mills measurements: for n=j+2 let eta_j=1/n^2, kappa_j^2=1/(2n^2), d0=1/4. Telescoping gives

    product_(n=3..N)(1-1/n^2)=2(N+1)/(3N),
    d_infinity=(1/4)(2/3)^2=1/9.

Here sum kappa_j diverges while sum kappa_j^2 converges. If the operator hypotheses and a valid continuum reconstruction held, the mass lower bound would be log(9/8)/t0. This example is only coefficient data demonstrating the theorem, not a constructed family of Yang–Mills transfer operators.

Given genuine OS-form and norm convergence on a dense algebra of centered renormalized observables, U002's bridge yields

    exp(-t0 H)|Omega-perp <= (1-d_infinity) I,
    mass >= -log(1-d_infinity)/t0 > 0.

A bounded norm and nonzero positive-time correlation for at least one limiting observable are still needed for nontrivial finite-mass content. All volume, cutoff, renormalization, density and axiom obligations remain. These are sufficient hypotheses, not consequences of summable absolute errors, and assuming them is not constructing Yang–Mills.

## 5. Temporal interpretation in the true vacuum

For a symmetric nonnegative normalized transfer kernel T(U,V) with positive top eigenfunction psi, define

    pi(dU)=psi(U)^2 dU,
    K(U,dV)=T(U,V) psi(V)/psi(U) dV.

The eigenfunction equation gives K1=1; symmetry gives detailed balance. Multiplication by psi is the unitary ground-state transform. For the appropriate number of time steps, the deficit form is

    E(f,h)=<f,(I-K)h>_pi
      =(1/2) integral conjugate[f(U)-f(V)] [h(U)-h(V)] pi(dU)K(U,dV).

Let P be conditional expectation onto a specified coarse gauge-invariant sigma-algebra, for example one generated by block Wilson loops. It is an orthogonal projection preserving constants. For centered u in its range and v in its kernel, the block forms are E(u,u), E(v,v), E(u,v). Thus the fine-sector and mixed estimates are temporal energy bounds, not just equal-time correlations or Langevin inequalities.

The measure pi is fixed by the actual transfer vacuum; it is generally neither product Haar nor the Gibbs measure on all four-dimensional links. The coarse marginal also need not equal the Wilson measure at another coupling. Obtaining that identification with eta_j control remains part of the unproved construction.

## 6. Executed SU(2) initialization test

Use a cubic spatial torus (Z/LZ)^3, L>=4, and the gauge-invariant subspace of product-Haar L2(SU(2)^E). In the convention of Spriggs–Greplova–Carrasquilla–Nys, arXiv:2509.12323v1, Section II.1 equation (1),

    H=(g^2/a) Hhat,
    Hhat=Hhat_E+Vhat,
    Hhat_E=(1/2)sum_e E_e^2,
    Vhat=lambda sum_p[1-(1/2)chi_(1/2)(U_p)],
    lambda=4/g^4.

Each plaquette is counted once. E_e^2 has eigenvalues j(j+1). This Casimir normalization is not U002's Hilbert–Schmidt metric Laplacian. Only this source's operator convention and gauge transformation were used; its numerical variational results are not proof certificates.

### Pure-electric reference gap

The constant Haar state is the unique zero state of Hhat_E. Peter–Weyl decomposition and gauge invariance give spin networks with energy (1/2)sum j_e(j_e+1). A support vertex of degree one cannot admit an invariant intertwiner in a nontrivial representation. A nonempty finite support therefore contains a cycle. The cubic graph has girth four for L>=4; each nontrivial edge costs at least 3/8. A fundamental plaquette character attains the resulting bound:

    gap(Hhat_E)=3/2, gap(H_E)=3g^2/(2a).

This is an electric-only reference result, not a gap theorem for the full Hamiltonian.

### Centered gauge-invariant pair

For one plaquette take f=chi_(1/2)(U_p), h=chi_1(U_p). A Haar class coordinate x has density (2/pi)sqrt(1-x^2) on [-1,1], with f=2x and h=4x^2-1. The density is the coordinate marginal of uniform measure on S^3, and its even moments are Catalan(n)/4^n. Exact integration gives

    E[f]=E[h]=E[fh]=0,
    E[f^2]=E[h^2]=1,
    E[f^2 h]=1,
    E[f^3]=E[f h^2]=0.

A plaquette holonomy is Haar distributed. Every different plaquette has an edge outside p; integrating that link annihilates its fundamental character, even when the two plaquettes share other links. With Q0 the Haar-centered projection and

    W=Vhat-lambda N_p=-(lambda/2)sum_q chi_(1/2)(U_q),

the compression to the ordered pair (f,h) is

    W_pair=[[0,-lambda/2],[-lambda/2,0]],
    E_pair=diag(3/2,4).

Consequently

    ||Hhat_E^(-1/2) Q0 W Q0 Hhat_E^(-1/2)||
       >= lambda/(2sqrt(6)) = 2/(sqrt(6)g^4),             (SU2)

with squared coefficient lambda^2/24=2/(3g^8). The inverse is on Q0, where the electric gap is positive. The normalized two-by-two compression has eigenvalues plus and minus this coefficient, proving the full-operator lower bound without truncating its Hilbert space.

The bound already diverges on one gauge-invariant pair, independently of volume. Restoring physical units gives off-diagonal coefficient -2/(a g^2) and electric energies 3g^2/(2a),4g^2/a; a cancels from the same relative ratio.

Distinct fundamental plaquette characters are orthonormal. For N_p=3L^3,

    W Omega_Haar=-(lambda/2)sum_p chi_(1/2)(U_p),
    ||Q0 W Omega_Haar||=(lambda/2)sqrt(N_p).

Thus the Haar state is not the full vacuum at lambda>0; subtracting an energy constant does not fix the eigenvector. A relative quadratic bound on the entire space fails for every finite constant: with u=Omega_Haar+epsilon f,

    <u,Wu>=-lambda epsilon,
    <u,Hhat_E u>=(3/2)epsilon^2.

Their absolute ratio diverges as epsilon tends to zero. Centering correctly avoids this kernel problem but does not avoid (SU2) at weak coupling.

Reject only the attempted initialization that treats the centered magnetic term as uniformly small relative to electric energy while keeping the raw Haar vacuum. The coefficient (SU2) is for W relative to Hhat_E; it is not identified with kappa_j for actual I-S_j blocks. No conclusion about the full Yang–Mills gap follows.

## 7. Executed follow-up: positive one-plaquette trial dressing

This follow-up uses only the one-plaquette graph, not the full three-dimensional spatial lattice. Its physical states are SU(2) class functions. Write u=chi_(1/2)=2x in [-2,2], choose psi_s=exp(su), s>=0, and use

    Hhat_E F=-(1/2)[(1-x^2)F''-3xF'].

The characters U_(2j)(x) have eigenvalues 2j(j+1), matching the four-link electric sum. Direct differentiation yields

    R_s(u)=Hhat psi_s/psi_s
      =(s^2/2)u^2+((3s-lambda)/2)u+lambda-2s^2.

For every lambda>=9/4,

    min_(s>=0) osc_(u in [-2,2]) R_s(u)
      =2lambda-3sqrt(lambda)+9/8,
    minimizing s=sqrt(lambda)/2.                         (D)

This optimizes global residual oscillation, not ground-state energy, and does not make the trial state an eigenfunction.

Proof: let A=s^2/2, B=(3s-lambda)/2. For |B|>=4A the quadratic is monotone and its oscillation is 4|B|. Otherwise its minimum is at the vertex and its maximum at an endpoint, giving

    F(s)=2s^2+|3s-lambda|+(3s-lambda)^2/(8s^2).

For lambda>=9/4 the initial monotone branch ends at s_b=(-3+sqrt(9+16lambda))/8 and has decreasing oscillation 2lambda-6s. In the vertex branch s<=lambda/3, the derivative multiplied by 4s^3 is

    (4s^2-lambda)(4s^2-3s+lambda).

The second factor is positive, and sqrt(lambda)/2 lies between s_b and lambda/3. For s>=lambda/3 the derivative numerator is (4s^2+lambda)(4s^2+3s-lambda)>0. This proves the global minimum, including s=0 separately. Energy shifts do not alter the oscillation.

With lambda=4/g^4, the minimizing s is 1/g^2, and the physical residual oscillation is

    (1/a)[8/g^2-6+(9/8)g^2].

Thus this trial dressing does not yield a small global absolute residual-oscillation error near g=0. Configurations causing that oscillation may have tiny trial weight; weighted or energy-relative residual control is not excluded. No full-lattice vacuum or mass-gap assertion follows from this single-plaquette result.

## 8. Computation, audit, and source scope

New checker: `checks/U003_relative_gap_checks.py`. Actual commands completed:

    python -m compileall -q checks/U003_relative_gap_checks.py
    python checks/U003_relative_gap_checks.py

Python 3.13.5, SymPy 1.14.0: 12 new tests passed, using exact integers, rationals, radicals, and symbolic identities. Coverage: 12 hidden-mode parameter choices; 12 mixed-mode choices; 24 scalar-block certificates; products through N=34; SU(2) character moments and matrix elements; support subsets of sizes 1–4 on a 12-edge cube, counts 0,0,0,6; exact trial-residual derivatives; five named couplings times 65 rational trial parameters. Infinite products, all-volume graph bounds and infinite-dimensional implications use the written proofs, not these finite grids. The previous ten U002 tests also passed when rerun.

Two stateless Wolfram 15.0.1 calls, each limited to 30 seconds, returned no reported warnings. The first returned character moments {1,0,0,1,1,0,1,0,0}, normalized eigenvalues +-lambda/(2sqrt(6)), coefficient squared lambda^2/24, zero Schur and Young-identity residuals, and ten true finite-product identities. The second returned the stated R_s, a zero residual identity, derivative factors (4s^2-lambda)(4s^2-3s+lambda) and (4s^2+lambda)(4s^2+3s-lambda), and stationary oscillation 9/8-3sqrt(lambda)+2lambda. Inputs and outputs are in the supplied local package. This is independent algebra evaluation, not independent expert review.

Self-review covered operator order, complete complements, adjoints, inverse bounds, the factor two, nonzero product margins, fixed physical time, actual-vacuum centering, finite-mass witnesses, finite-volume gauge invariance, Casimir normalization, character orthogonality, and the distinction between residual oscillation and variational energy. A nonnegative magnetic term does not itself bound the excitation gap E1-E0 by the electric-only gap.

No Lean/Bun/Ruff/mypy/pyright executable was found in this runtime. Native syntax checks and focused tests ran; no external lint/typecheck or formal build is claimed. No public posting, paid job, researcher contact, prize submission or background process was initiated.

Sources inspected, 2026-09-14:

- Clay current status: https://www.claymath.org/millennium/yang-mills-the-maths-gap/
- Jaffe–Witten, official description, Sections 3–4, printed pages 5–6: https://www.claymath.org/wp-content/uploads/2022/06/yangmills.pdf
- Genevieve Dusson, Israel Michael Sigal, Benjamin Stamm, The Feshbach–Schur map and perturbation theory, arXiv:2105.02058v1, 5 May 2021, Theorem 1.2 and equations (1.10),(1.15)–(1.16): https://arxiv.org/abs/2105.02058v1
- Thomas Spriggs, Eliska Greplova, Juan Carrasquilla, Jannes Nys, Accurate ground states of SU(2) lattice gauge theory in 2+1D and 3+1D, arXiv:2509.12323v1, 15 September 2025, Section II.1 equation (1), lambda=4/g^4 and gauge definitions: https://arxiv.org/html/2509.12323v1 — operator convention only, no numerical proof imported.
- Kogut–Susskind, Hamiltonian formulation of Wilson's lattice gauge theories, Phys. Rev. D 11,395 (1975), DOI 10.1103/PhysRevD.11.395 — publisher abstract opened for bibliography; full original paper not audited.

The Schur method and strong-coupling representation arguments are standard. No global novelty claim is made for these specializations.

## 9. Next executable mathematical obligation

The conditional operator implication is proved; its Wilson/Yang–Mills inputs are not. The raw Haar initialization fails the proposed relative-smallness test, and the first positive trial dressing has now failed a global absolute-residual test. Next derive a *weighted or energy-relative* residual estimate for the positive trial state, then test the shared-link terms on two adjacent plaquettes without assuming independent plaquettes or an infinite-volume gap. The ultimate construction still needs actual physical-time forms, control of every discarded state, a renormalization trajectory, all limits/axioms, and a nonzero positive-time witness. No complete candidate exists.
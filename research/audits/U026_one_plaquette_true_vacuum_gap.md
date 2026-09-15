# U026 — complete one-plaquette gap bounds, exact tail certificates, and the two-loop obstruction

Date: 2026-09-15. Base: private `Joe-Simo/yang-mills-mass-gap` commit `1c5e8c2623d6a88336c6b7141f9d7a022a51d818` (U025).

**We have not solved the Yang–Mills problem yet.**

Evidence status: self-reviewed auxiliary proofs and exact-arithmetic certificates for an explicitly restricted model; not formal verification, independent expert review, or a continuum Yang–Mills construction. The radial reduction and leading weak-coupling asymptotic are known results after translating conventions. No novelty claim is made for the comparison bound or certificate method.

## 1. Target, preserved state, and conventions

U025's next task was to obtain a lower gap in the actual ground state of an isolated SU(2) square, rather than infer one from a finite Wilson-loop trial space. This unit completes that task, then tests the proposed extension to independent cells and to two connected loops.

The project prompt was read in full, and the existing local archives, remote tree, README, and U025 were inspected before new work. No previous research record was overwritten. The remote tree has no `AGENTS.md` or executable `.mathbox/` ledger. This unit does not rely on the disputed boundary or scalar-localization claims in U009–U023.

Retain U003's Hamiltonian normalization, with positive coupling g and lattice spacing a:

    H_square(g,a) = (g^2/a) Hhat_lambda,   lambda = 4/g^4.

There are four links, electric Casimir j(j+1) on each link, and a factor 1/2 in the dimensionless electric Hamiltonian. On a single isolated square Gauss's law reduces the COMPLETE physical space to conjugation-invariant functions of its holonomy. In class angle theta in [0,pi],

    Hphys = L2([0,pi], (2/pi) sin^2(theta) dtheta),
    Hhat_lambda = -(1/2)(d^2/dtheta^2 + 2 cot(theta) d/dtheta)
                  + lambda(1-cos(theta)).                         (1)

Characters chi_j(theta)=sin((2j+1)theta)/sin(theta), j=0,1/2,1,..., form a complete orthonormal basis, with electric energies 2j(j+1). This is the full isolated-square problem, NOT a subspace claimed invariant inside the many-plaquette Hamiltonian.

Ale et al., arXiv:2410.14580v1, equations (2), (15)–(21), independently identify this normalization and reduction. Their weak-coupling oscillator result is used for an overlap check, not as the proof of the lower bound below.

## 2. Unitary radial reduction and domain

Put

    u(theta)=sqrt(2/pi) sin(theta) psi(theta).

This is unitary to ordinary L2(0,pi). The Friedrichs realization selected by the group kinetic form becomes

    Htilde_lambda = -(1/2)d^2/dtheta^2 - 1/2
                   + lambda(1-cos(theta)),
    form domain = H0^1(0,pi).                                   (2)

In particular the boundary conditions are Dirichlet, not a freely chosen alternative extension. To check the kinetic part, set lambda=0: the normalized sine basis sin(m theta), m>=1, has energies (m^2-1)/2, exactly 2j(j+1) with m=2j+1.

Let e_0<e_1<... be the eigenvalues and Dhat_lambda=e_1-e_0. The interval is compact and the potential bounded; the resolvent is compact. The lowest Dirichlet eigenfunction is strictly positive in the interior and simple. These statements follow from the one-dimensional variational/Sturm–Liouville problem, and apply at every finite lambda>=0.

For comparisons write K_lambda=Htilde_lambda+1/2. The constant disappears from gaps.

## 3. A uniform lower bound on the full one-square gap

For every theta in [0,pi],

    2 theta^2/pi^2 <= 1-cos(theta) <= theta^2/2.                  (3)

The lower inequality follows from sin(theta/2)>=theta/pi and the upper one from sin(theta/2)<=theta/2.

### 3.1 Lower bound on the first excited eigenvalue

By (3), K_lambda is bounded below in quadratic-form order by the harmonic oscillator potential 2 lambda theta^2/pi^2 on (0,pi). Extend Dirichlet functions by zero to (0,infinity). Min–max and domain inclusion then compare every ordered eigenvalue from below with the half-line Dirichlet oscillator

    -(1/2)d^2/dtheta^2 + (2 lambda/pi^2) theta^2.

The full-line oscillator frequency is 2 sqrt(lambda)/pi. The half-line Dirichlet eigenfunctions are the odd full-line modes, with energies (2k+3/2) times that frequency, k=0,1,... . Therefore

    e_1 + 1/2 >= (7/pi) sqrt(lambda).                          (4)

This bound covers all physical states of the isolated square; no representation cutoff has been made.

### 3.2 An upper bound on the true ground energy

Use u_ell(theta)=sqrt(2/ell) sin(pi theta/ell) for 0<theta<ell and zero for ell<=theta<pi. This is an admissible H0^1 trial function for ell<=pi. Its derivative can jump at ell; membership in the form domain, not in H2, is what the variational upper bound needs.

Direct integration gives

    kinetic Rayleigh value = pi^2/(2 ell^2),
    <theta^2> = c_s ell^2,
    c_s=1/3-1/(2 pi^2).

Thus (3) gives

    e_0+1/2 <= pi^2/(2 ell^2) + lambda c_s ell^2/2.

Taking ell^4=pi^2/(lambda c_s), which has ell<=pi for lambda>=1, proves

    e_0+1/2 <= C_0 sqrt(lambda),
    C_0=sqrt(pi^2/3-1/2).                                    (5)

Subtracting the ground UPPER bound (5) from the excited LOWER bound (4) is the correct variational direction. Combining them,

    Dhat_lambda >= c_* sqrt(lambda),   lambda>=1,
    c_* = 7/pi-sqrt(pi^2/3-1/2)
        = 0.55787936804941248... > 1/2.                       (6)

The last decimal is not the positivity certificate: pi<22/7 implies 7/pi>49/22 and C_0^2<821/294<(17/10)^2, while 49/22-17/10=29/55>1/2.

For 0<=lambda<=1, nonnegativity of the magnetic potential gives e_1>=3/2. The constant class function is a ground trial with energy lambda, so e_0<=lambda. Consequently

    Dhat_lambda >= 3/2-lambda >= 1/2.

Together these yield the simple all-coupling bound

    Dhat_lambda >= (1/2) max(1,sqrt(lambda)),  lambda>=0,
    Delta_square(g,a) >= max(g^2/2,1)/a >= 1/a,  g,a>0.       (7)

At lambda=0 the exact dimensionless gap is 3/2; (7) is deliberately conservative.

## 4. Poincare inequality in the actual vacuum

Let u_0 be the normalized positive ground state from (2) and let dnu_lambda=u_0(theta)^2 dtheta. The product rule and the ground-state equation give, initially on a smooth form core,

    <u_0 f,(Htilde_lambda-e_0)u_0 f>
      = (1/2) integral |f'|^2 dnu_lambda.                    (8)

The transformed differential expression is -(1/2)f''-(u_0'/u_0)f'. The identity extends by closing the weighted quadratic form. Orthogonality to u_0 is exactly integral f dnu_lambda=0. Hence

    (1/2) integral |f'|^2 dnu_lambda
      >= Dhat_lambda Var_nu_lambda(f).                      (9)

This is a true-vacuum inequality, not an inequality in a guessed Gibbs density or a variational substitute for the vacuum. Equation (6) or (7) supplies an explicit lower constant without requiring a closed elementary expression for u_0.

## 5. Leading weak-coupling limit, with a compactness proof

Rescale theta=lambda^(-1/4)x. The unitarily rescaled K_lambda/sqrt(lambda) is

    A_lambda = -(1/2)d^2/dx^2 + W_lambda(x),
    W_lambda(x)=sqrt(lambda)[1-cos(lambda^(-1/4)x)],
    0<x<pi lambda^(1/4), with Dirichlet endpoints.

Its potential converges locally uniformly to x^2/2, and (3) supplies the uniform confinement

    W_lambda(x) >= 2x^2/pi^2.                               (10)

Here are both min–max directions, so the result is not inferred from a Taylor expansion alone.

Upper direction: approximate the first k+1 half-line Dirichlet oscillator eigenfunctions by compactly supported H0^1 functions. For sufficiently large lambda these trial functions lie inside the expanding interval, and local potential convergence gives the corresponding eigenvalue limsup bound.

Lower direction: the preceding upper bounds bound the first k+1 eigenvalues. Their normalized eigenfunctions, extended by zero, have uniformly bounded H1 norms and second moments by (10). Local compactness and the tail bound integral_(x>R)|u|^2<=C/R^2 give strong L2 subsequences. The k+1 limits remain orthonormal. For every fixed linear combination, lower semicontinuity of the kinetic form and local uniform convergence of W_lambda, first on finite intervals and then as R tends to infinity, bound the half-line oscillator form by the limiting kth eigenvalue times the squared norm. Min–max on this k+1 dimensional limit space gives the converse liminf bound.

The half-line oscillator eigenvalues are 2k+3/2. Thus, for every fixed k,

    (e_k+1/2)/sqrt(lambda) -> 2k+3/2,
    Dhat_lambda/sqrt(lambda) -> 2.                          (11)

Restoring the original convention, for any path with g(a)->0,

    a Delta_square(g(a),a) -> 4,
    Delta_square(g(a),a) = (4+o(1))/a.                      (12)

This leading asymptotic is known after translation from Ale et al., equation (21); the self-contained compactness argument records why it is valid in the complete isolated-square problem. It is not a finite continuum Yang–Mills mass.

## 6. Exact-arithmetic enclosures that control the infinite tail

In the complete sine/character basis the operator (2) is the infinite Jacobi matrix

    diagonal d_m=(m^2-1)/2+lambda, m>=1,
    neighboring off-diagonal entries = -lambda/2.           (13)

Let A_N be its first N rows and columns. Split off the remaining infinite tail D. Because the compressed magnetic potential stays nonnegative,

    D >= d I,   d=((N+1)^2-1)/2.

The single coupling between retained and omitted spaces has magnitude b=lambda/2. Fix U=2lambda+2 and choose N with d>U. Completing a square gives the quadratic-form lower comparison

    Htilde_lambda >= (A_N-delta |N><N|) direct_sum U I,
    delta=b^2/(d-U).                                        (14)

For example, the leftover boundary part is bounded below by the square of sqrt(d-U) times the tail component minus b/sqrt(d-U) times the last retained component. This explicitly controls the discarded physical states.

By V<=2lambda and min–max, the first two Ritz eigenvalues of A_N are at most 2lambda+3/2<U. The first two eigenvalues of its lowered matrix are no larger. It follows that for k=0,1,

    eigenvalue_k(A_N-delta |N><N|)
       <= e_k <= eigenvalue_k(A_N).                        (15)

Both finite spectra in (15) are enclosed with rational Sturm determinant counts and rational bisection. The checker uses only unbounded integers and `fractions.Fraction` for its certificates. A finite numerical matrix alone would not give the lower half of (15); the analytic infinite-tail inequality is essential.

The generated JSON contains exact rational endpoints. For orientation ONLY, its gap intervals lie inside the following outward-rounded decimal intervals:

| lambda | retained N | dimensionless gap enclosure |
|---:|---:|---:|
| 0 | 16 | [1.4999995, 1.5000005] |
| 1 | 18 | [1.7131435, 1.7131450] |
| 16 | 24 | [7.3270999, 7.3271008] |
| 256 | 48 | [31.3645821, 31.3645835] |
| 4096 | 144 | [127.3724725, 127.3724737] |

The finite cases validate the certificate implementation and sample different coupling regimes. They are not the proof of (6), (7), or (11), whose uniform arguments are above.

### Independent computation and a rejected numerical output

Wolfram 15.0.1 exactly checked the radial conjugation (residual zero), the trial norm/second moment/kinetic integrals, and the rational positivity comparisons. Its 50-digit Mathieu characteristic-value calculations agree with the rational enclosures for lambda=1,16,256,4096. The identity used is

    e_k = lambda-1/2 + b_(2k+2)(-4lambda)/8.                (16)

It follows by theta=2z in the Dirichlet equation; the allowed solutions are se_(2k+2)(z,-4lambda). NIST DLMF 28.2.28 also gives b_(2k+2)(-q)=b_(2k+2)(q).

A separate SciPy tridiagonal eigensolver agrees with all five exact certificates. However, the installed `scipy.special.mathieu_b` routine's double-precision output at parameter -16384 (lambda=4096) returned candidate energies approximately 5563.5372 and 475.9422, outside the certified intervals for e_0 approximately 95.34347 and e_1 approximately 222.71595. These special-function outputs are rejected as evidence, not averaged into a conclusion. The root cause was not investigated. This observation is limited to the recorded routine, version, and parameters; it is not a claim that all SciPy or Mathieu evaluations fail.

## 7. Executed lifting test: independent cells and connected loops

### 7.1 Independent squares lose finite-energy positive-time content

A tensor sum of any finite number M(a) of independent copies, after subtracting the actual total vacuum energy, has gap Delta_square: excite one factor for the upper bound, and use the sum of nonnegative gapped factor Hamiltonians for the lower bound. Equation (7) then implies, for centered vectors v_a with uniformly bounded norms and fixed physical t>0,

    0 <= <v_a,exp[-t(H_a-E_0,a)]v_a>
       <= exp(-t/a) ||v_a||^2 -> 0.                        (17)

Thus this independent-cell refinement does not supply the nonzero positive-time witness needed for nontrivial finite-energy content. This is a conclusion about this product construction only, not about the interacting lattice.

### 7.2 Independent class functions omit legitimate two-loop states

On a connected graph with two based loop holonomies U,V, tree gauge fixing leaves simultaneous conjugation, (U,V)->(hUh^-1,hVh^-1), rather than independent conjugation of each matrix. Write

    U=x0 I+i x.vector sigma,   V=y0 I+i y.vector sigma.

The mixed observable

    F(U,V)=(1/2)Tr(UV)-(1/4)Tr(U)Tr(V)=-x.vector y          (18)

is invariant under this residual gauge group. Given x0,y0 under product Haar measure, the two directions are independent and isotropic, so the conditional mean of F is zero. Therefore F is orthogonal to EVERY function of the two individual class angles, not just to a finite list of characters. Yet Haar symmetry on S3 gives E[x_i x_j]=delta_ij/4 and hence

    ||F||^2_(Haar x Haar)=3/16 > 0.                         (19)

Consequently the tensor product of the individual single-square class-function spaces is a proper subspace of the two-loop gauge-invariant space. A factorwise use of (7) misses a whole physical sector. The argument is kinematic: it does not say how low the mixed sector's true interacting energies are.

Two adjacent squares have seven links and six vertices; a maximal tree removes five links, leaving two holonomies and the residual simultaneous conjugation. Their shared-link electric terms must be retained as well. A proof that replaces them by independent singlet squares is not a bound on the full two-plaquette Hamiltonian.

## 8. Verification record, scope, and source checks

Commands run from the project folder:

    python checks/U026_one_plaquette_certificate.py --test
    python checks/U026_one_plaquette_certificate.py --output evidence/U026_certificates.json
    python -m compileall -q checks/U026_one_plaquette_certificate.py
    python -m tabnanny checks/U026_one_plaquette_certificate.py

Nine focused tests passed, including internal zeros in the Sturm chain, eigenvalue-threshold rejection, known 2x2 roots, the exact electric limit, tail-correction direction controls, invalid inputs, rational constants, and the two-loop variance arithmetic. The run used Python 3.13.5. Floating-library versions and the rejected special-function outputs are in `evidence/U026_floating_cross_checks.json`; mathematical certificates use neither library. Compilation and indentation checks passed. No Python static linter/typechecker was installed; no successful run of one is claimed. Previous U002/U003 suites were not rerun in this unit.

The self-review checked normalization at lambda=0, form versus operator domains, min–max directions, the infinite-tail inequality, preservation of orthogonality in the asymptotic compactness step, true-vacuum centering, and the distinction between product and simultaneous gauge invariance. No independent expert or formal proof-assistant review occurred.

Primary-source checks on 2026-09-15, using HTML rather than a PDF or a secondary summary:

1. Ale, Bauer, Jha, Ringer, Siopsis, *Quantum computation of SU(2) lattice gauge theory with continuous variables*, arXiv:2410.14580v1, equations (2), (15)–(21), and the opening two-plaquette construction of Section IV. The version label is pinned; a different date in the HTML title block is not used to infer revision history. https://arxiv.org/html/2410.14580v1
2. Jakobs et al., *A comprehensive stress test of truncated Hilbert space bases against Green's function Monte Carlo in U(1) lattice Gauge theory*, EPJ C 86, 637 (2026), DOI 10.1140/epjc/s10052-026-15753-6. Despite its U(1) title, Section 4.2 treats SU(2); equations (43), (46)–(51) confirm the l=0 radial/Mathieu dictionary. Nonzero-angular-sector formulas were not imported into this proof. https://link.springer.com/article/10.1140/epjc/s10052-026-15753-6
3. NIST Digital Library of Mathematical Functions, equations 28.2.24 and 28.2.28 (zero-parameter characteristic values and sign symmetry), and 28.8.1 (known large-parameter behavior). The comparison bound and leading asymptotic proof above do not require an unverified remainder constant from that expansion. https://dlmf.nist.gov/28.2 and https://dlmf.nist.gov/28.8

Overlap classification: radial reduction and weak-coupling leading gap are known after translating normalization; the derivations and rational whole-tail checks here provide an auditable project-local verification. The search was not a comprehensive novelty search. Consensus's earlier recorded quota failure was not treated as a negative literature result; primary web sources were used instead.

## 9. Research outcome and executable handoff

Completed: a full-space lower spectral-gap bound and actual-vacuum Poincare inequality for an isolated SU(2) square; uniform lower physical gap >=1/a; leading weak-coupling physical gap (4+o(1))/a; five infinite-spectrum interval certificates; and a nonzero two-loop mixed invariant that independent class functions omit.

Not completed: a many-plaquette complement bound, a volume-uniform finite physical mass, a nonabelian renormalization construction, reflection-positive continuum limits, or the full Clay/Jaffe–Witten theorem. No continuum mass was generated by this unit.

Next bounded target: the exact seven-link graph of two adjacent squares, with the complete simultaneous-conjugation invariant space. Derive the shared-link kinetic form and its action on mixed-loop invariants such as (18), then seek a true-ground-state/complement comparison with controlled constants. The decisive test is whether a putative factorwise lower bound actually holds on the mixed sector; do not substitute another Ritz truncation or multiply independent-square gaps. Any eventual gap-persistence argument must still control increasing physical volume and retain nonzero finite-energy positive-time correlations.

# U027 — shared-link dynamics, complete two-plaquette weak-coupling gap, and patch-size dependence

Date: 2026-09-15. Base: private `Joe-Simo/yang-mills-mass-gap` commit `09cc3efaad3b139a605b4032c7fcb7909ae997ab` (U026).

**We have not solved the Yang–Mills problem yet.**

Evidence: self-reviewed exact reductions and fixed-graph analytic arguments, with bounded exact symbolic checks. No formal verification, independent expert review, global novelty claim, or four-dimensional continuum construction. The leading two-plaquette asymptotic agrees with a known result after convention translation.

## 1. Contract, scope, and preserved inputs

U026 supplied a full-space one-square gap theorem and showed that independent class functions omit physical two-loop states. This unit executes three follow-ups: derive the exact shared-link operator; determine its first physical excitation at weak coupling without discarding the mixed states; test whether the resulting coefficient remains uniform as a planar patch grows.

The actual workspace is `/mnt/data/yang-mills-mass-gap`, backed by the existing dedicated private repository. The supplied U026 archive was inspected, and only missing files were restored. Its seven mathematical/code/evidence hashes were checked against the prior manifest and remain unchanged. The remote head and README were read. The remote tree contains no `AGENTS.md` or executable `.mathbox` ledger. The research prompt was retrieved from this conversation; its full universal target, status headings, private-write authorization, and zero-spend boundary are retained. The current work does not depend on the disputed U009–U023 localization arguments.

Use the U003/U026 convention on a finite graph:

    H(g,a) = (g^2/a) Hhat_lambda,
    Hhat_lambda = (1/2) sum_e C_e + lambda sum_p (1-W_p),
    lambda=4/g^4,   C_e has eigenvalues j(j+1),   W_p=(1/2)Tr U_p.

All spectral gaps below are excitation energies ABOVE THE ACTUAL GROUND ENERGY. A constant energy subtraction is not used to replace the true vacuum. The seven-link, two-square graph and the later planar patches are restricted Hamiltonian models, not the full spatial three-dimensional lattice of the Clay problem.

## 2. Exact seven-link reduction

View the two adjacent squares as three edge-disjoint paths between two vertices: outer paths A and B have length three, and their shared path C has length one. Orient all three from the same endpoint to the other. Write their ordered holonomies as A,B,C. Define

    U=A C^{-1},   V=B C^{-1}.

The two plaquette traces are Tr U and Tr V, regardless of reversing one plaquette orientation. Interior-vertex gauge transformations collapse the three paths to their products. Endpoint gauge transformations act by common left and right multiplication. Fixing C=I leaves precisely simultaneous conjugation:

    (U,V) -> (h U h^{-1}, h V h^{-1}).

Normalized Haar integration on the original links becomes normalized product Haar integration on U,V, for gauge-invariant functions: integrate successively along each path, then change (A,B,C) to (U,V,C). Haar invariance gives no Jacobian weight. Thus the COMPLETE physical space is

    H_phys = L2(SU(2) x SU(2), dU dV)^{Ad SU(2)}.             (1)

Let R_U^i and R_V^i be the self-adjoint generators of right multiplication by exp(i t sigma_i/2). Put C_U=sum_i (R_U^i)^2, and similarly C_V. A link on outer path A contributes C_U; invariance of the Casimir removes its intermediate parallel transport. All three A links therefore contribute 3C_U, and B contributes 3C_V. Varying the shared link moves U and V by the SAME right multiplication, so its Casimir is sum_i(R_U^i+R_V^i)^2. Consequently

    T = (1/2)[3C_U+3C_V+(R_U+R_V)^2]
      = 2(C_U+C_V) + R_U . R_V,
    Hhat_lambda = T + lambda(2-x0-y0).                    (2)

Here U=x0 I+i x.sigma and V=y0 I+i y.sigma. Right generators on different group factors commute. Equation (2) preserves (1), is symmetric in its Haar form, and its Friedrichs extension is the physical Hamiltonian.

If T_ind=2(C_U+C_V), Cauchy–Schwarz on the three derivative components gives the full-space form comparison

    (3/4)T_ind <= T <= (5/4)T_ind.                         (3)

The factor 3/4 is sharp, as shown below. This proves uniform ellipticity on the compact product group, not a comparison between excitation gaps after different ground energies have been subtracted. The compactness of the configuration manifold and boundedness of the potential give compact resolvent. The ground eigenfunction of the extended elliptic operator is unique and strictly positive; averaging its symmetry orbit, or simplicity and positivity, makes it simultaneous-conjugation invariant. It is therefore also the physical ground state. No unknown gauge sector was discarded to obtain that ground.

## 3. Exact mixed-state calculation

Put

    a=x0,  b=y0,  s=x.y.

The invariant s is not determined by a and b. Its allowed interval at fixed a,b is

    |s| <= sqrt((1-a^2)(1-b^2)).

The right derivative along U exp(i t sigma_i/2) satisfies

    D_i a=-x_i/2,
    D_i x_j=[a delta_ij - sum_k epsilon_(jki) x_k]/2,
    R_i=-i D_i.

Acting with (2) gives the exact identities

    T(ab)=3ab-s/4,
    T(s)=(5/2)s-(3/4)ab.                                 (4)

Product Haar moments are

    <a^2 b^2>=1/16,   <s^2>=3/16,   <ab s>=0.

Thus in the orthonormal ordered basis (4ab,4s/sqrt(3)), the electric matrix is

    [[3, -sqrt(3)/4],[-sqrt(3)/4,5/2]],

with eigenvalues 9/4 and 13/4. Explicit eigenfunctions are

    T(ab+s)=(9/4)(ab+s),
    T(3ab-s)=(13/4)(3ab-s).                               (5)

The perimeter observable ab+s=(1/2)Tr(UV^{-1}) traverses six exterior links. Its electric energy is independently 6(1/2)(3/4)=9/4. This checks the shared-link sign and normalization without the differential-coordinate implementation.

Both factors in ab+s have fundamental representation degree, so T_ind(ab+s)=3(ab+s). Since ||ab+s||^2=1/4,

    <ab+s,(T-T_ind)(ab+s)>=-3/16.                         (6)

Therefore T>=T_ind is false even on a valid gauge-invariant state; the lower factor 3/4 in (3) is attained. Reversing one loop changes signs of some cross terms but not the spectrum or this obstruction.

### Exact electric spectrum on the entire physical space

Peter–Weyl decomposition identifies a fixed (j1,j2) block with matrix coefficients of V_(j1) tensor V_(j2). Its diagonal SU(2) decomposition contains spins

    J=|j1-j2|, |j1-j2|+1, ..., j1+j2,

each once. An invariant matrix coefficient is Tr[P_J(D^(j1)(U) tensor D^(j2)(V))], where P_J is the spin-J projection. Haar orthogonality makes different triples orthogonal. These triples are complete in (1), because the commutant of this multiplicity-free decomposition is spanned by the P_J.

The three-path electric formula therefore has eigenvalues

    E_E(j1,j2,J)
      = (3/2)[j1(j1+1)+j2(j2+1)] + (1/2)J(J+1).         (7)

Its ground is the constant function; its first positive value is 3/2, attained by (j1,j2,J)=(1/2,0,1/2) and its interchange. If both j1,j2 are nonzero, the first term alone is at least 9/4. Formula (7) is an exact infinite-basis statement, not inferred from a finite spin cutoff. The checker samples j1,j2<=2 only to test the implementation.

## 4. No nonzero eigenstate can depend only on the two separate traces at lambda>0

This is stronger than showing that the separate-class-function subspace is not invariant. Suppose an energy eigenfunction at lambda>0 has the form psi=f(a,b), with no s dependence. Elliptic regularity makes it smooth in the interior coordinate region. From (2),

    T f = -(1/2)[(1-a^2)f_aa+(1-b^2)f_bb-3a f_a-3b f_b]
          -(s/4) f_ab.                                  (8)

The potential and the right side E f are independent of s. At each |a|,|b|<1 the s interval has positive length, so the eigenfunction equation forces f_ab=0. Therefore f=A(a)+B(b).

Differentiate that equation once in a and once in b. All separate-variable kinetic terms vanish, leaving

    -lambda[A'(a)+B'(b)]=0.

It follows that A'=c and B'=-c; hence f=c(a-b)+d. Substituting again, the coefficient of a^2 is -lambda c, so c=0. The coefficient of a is then -lambda d, so d=0. This contradicts a nonzero eigenfunction.

Thus for every lambda>0 the true ground state, and indeed every nonzero energy eigenfunction, necessarily involves the relative loop orientation s. This statement concerns the complete seven-link model and smooth energy eigenstates, not arbitrary trial functions. Separate-trace trial states are still allowed variational vectors; they are simply not exact eigenstates.

## 5. Complete two-plaquette weak-coupling limit

Use conjugation-equivariant logarithmic coordinates U=exp(i u.sigma), V=exp(i v.sigma) near (I,I). At the identity R_U=-i partial_u/2 and R_V=-i partial_v/2. Also

    2-x0-y0=(|u|^2+|v|^2)/2 + O((|u|+|v|)^4).

With h=lambda^{-1/4}, set (u,v)=h(z1,z2), and divide Hhat by sqrt(lambda). The frozen quadratic operator is

    K0 = (1/2)[p1^2+p2^2+(1/2)p1.p2]
         +(1/2)(z1^2+z2^2),
    p_i=-i partial_(z_i),                                (9)

on L2(R3 x R3) invariant under simultaneous SO(3) rotation. The 2x2 kinetic matrix has diagonal 1 and off-diagonal 1/4, with eigenvalues

    m_s=3/4,  m_f=5/4.

Each eigenmode is a three-vector. The two oscillator frequencies, in the scaled operator, are

    omega_s=sqrt(3)/2,   omega_f=sqrt(5)/2.

The ground energy is e0^osc=(3/2)(omega_s+omega_f). A one-quantum excitation transforms as a vector under the residual gauge group, not as a singlet, and is inadmissible. Two slow quanta have a scalar component, obtained by the radial polynomial

    (|z_s|^2-(3/2)sqrt(m_s)) Psi0.

No excited singlet can have energy below 2omega_s: every nonvacuum oscillator state either has one quantum (not invariant), or at least two quanta, each costing at least omega_s. Therefore the exact singlet oscillator gap is

    Delta_osc=2omega_s=sqrt(3).                           (10)

### Why (9) controls the full eigenvalues, not just a Taylor model

Let e_k(lambda) be the ordered physical eigenvalues of (2). The following min–max/compactness argument justifies the harmonic approximation for each fixed k.

1. **Localization and coercivity.** The only zero of V0=2-x0-y0 on the product group is (I,I). Class-angle distances obey 1-cos(theta)>=2theta^2/pi^2. Thus V0 controls squared distance to that point globally. Equation (3) controls the full group-gradient energy uniformly. The group manifold is kept intact; no singular orbit-space boundary condition is introduced.

2. **Upper direction.** Take the first k+1 invariant oscillator eigenfunctions, approximate them in oscillator form norm by compactly supported smooth invariant functions, and pull them back by the h-scaled logarithmic chart. The cutoffs can be chosen rotation invariant. Haar density and the differential coefficients converge uniformly on every fixed scaled compact set to their Euclidean values. The finite-dimensional Gram and energy matrices converge, proving limsup e_k(lambda)/sqrt(lambda)<=e_k^osc.

3. **No escape of mass.** For any of the first k+1 normalized eigenfunctions, the upper bounds imply lambda times its V0 expectation is O(sqrt(lambda)), hence its expected squared group distance is O(h^2). Outside any fixed chart neighborhood its mass is O(h^2). In scaled coordinates, the potential bound gives a uniform second moment, so mass outside a ball of radius R is at most C/R^2. A fixed smooth chart cutoff changes the scaled kinetic energy by an O(h^2) localization term. This follows directly from the sum-of-squares form; no conjectured physical gap is used.

4. **Lower direction.** In every scaled bounded region the form coercivity gives bounded H1 norm. Local Rellich compactness and the preceding tail bound give strongly convergent L2 subsequences of the first k+1 rescaled eigenfunctions. Their limits remain orthonormal and invariant. Smooth convergence of the local kinetic tensor to (9), weak lower semicontinuity, and the nonnegative potential give the limiting oscillator form bound for every linear combination of these limits. Min–max in this (k+1)-dimensional invariant subspace gives the converse liminf inequality.

Consequently

    e_k(lambda)/sqrt(lambda) -> e_k^osc,
    [e_1(lambda)-e_0(lambda)]/sqrt(lambda) -> sqrt(3).       (11)

This also gives an actual lower gap for all sufficiently large lambda: for some finite lambda0, Delta_hat>=sqrt(3lambda)/2 when lambda>=lambda0. This unit does not give a numerical value of lambda0 or certified finite-lambda two-plaquette intervals.

Restoring U026's physical units yields

    lim_(g->0) a Delta_two(g,a) = 2sqrt(3),
    Delta_two(g,a)=(2sqrt(3)+o(1))/a.                      (12)

The remainder statement is for this fixed graph. No O(1) remainder or uniformity in the number of plaquettes is asserted. Combining (12) with U026,

    Delta_two / Delta_square -> sqrt(3)/2 < 1.            (13)

Thus an unchanged one-square gap cannot be inherited merely by adjoining a shared square. The conservative U026 bound 1/a is NOT refuted by (12); it was proved for one square, and its extension remains a separate question.

## 6. Executed follow-up: fixed planar patches reveal nonuniform size dependence

To distinguish a two-square accident from a collective mechanism, take an open Nx-by-Ny rectangular array of square faces. Let C be its oriented face-edge incidence matrix: every row has four entries +/-1. It satisfies C grad=0. The faces are independent because the filled rectangle is a disk, so C has full row rank. Two distinct faces share either one edge with opposite orientations or no edge. Hence

    C C^T = 4I - adjacency_(rectangular face grid).         (14)

This is a derived graph identity, not a copied source matrix. After linearizing the link holonomies, each color component has electric energy (1/8)|p_edges|^2 and magnetic energy (lambda/2)|C q_edges|^2. Removing vertex gradients leaves the nonzero curl modes. Equivalently, using face coordinates b=Cq gives the kinetic matrix (C C^T)/4 and potential |b|^2/2 in the sqrt(lambda)-scaled oscillator.

### Extension of the fixed-graph limit

For any fixed finite rectangle, a maximal tree gives finitely many independent SU(2) loop variables with residual simultaneous conjugation. The electric form contains the Casimir of each non-tree link and is elliptic in these variables. Vanishing plaquette deficit makes every contractible holonomy trivial, so the only minimum in the gauge-fixed loop configuration space is the identity tuple. Near it, the independent face-log coordinates are nonsingular and their frozen tensor is (14)/4. The four steps in Section 5 therefore apply with dimension 3 Nx Ny; constants may depend on the graph. Each normal oscillator mode is again an adjoint three-vector, so the first invariant excitation has two quanta in a lowest-frequency mode.

For every FIXED rectangle,

    Delta_hat(lambda)/sqrt(lambda) -> sqrt(mu_min),
    lim_(g->0) a Delta_(Nx,Ny)(g,a) = 2sqrt(mu_min),        (15)

where mu_min is the first eigenvalue of (14). This is an iterated/fixed-graph asymptotic, not a simultaneous continuum-and-volume result.

Separation of variables gives the whole face matrix spectrum:

    mu_(k,l)=4-2cos(k pi/(Nx+1))-2cos(l pi/(Ny+1)),
    1<=k<=Nx, 1<=l<=Ny.                                  (16)

It follows directly by applying the one-dimensional nearest-neighbor recurrence to sin(k pi i/(Nx+1)) sin(l pi j/(Ny+1)); boundary values vanish. These products form an orthogonal basis, so the list is complete. The minimum has k=l=1.

For an N-by-N patch,

    mu_min=8sin^2(pi/[2(N+1)]),
    c_N := lim_(g->0) a Delta_(N,N)(g,a)
         =4sqrt(2)sin(pi/[2(N+1)])
         ~2sqrt(2)pi/(N+1).                              (17)

Thus c_N tends to zero. This is already a rigorous obstruction to a proposed lower bound a Delta_(N,N)>=c>0 that is simultaneous in ALL patch sizes and all sufficiently small g: for each fixed N take g->0, then let N grow. Such a bound would force c_N>=c, contradicting (17).

For contrast, a one-row ladder has mu_min=4-2cos(pi/(Nx+1)), whose limit is 2 rather than zero. Thin-ladder results cannot be used as a proxy for increasing transverse size. Equations (16)–(17) are only planar-model results, not a claim about the four-dimensional Yang–Mills mass gap.

**Limit warning:** substituting N approximately 1/a into a fixed-N o(1) term is unjustified. This work does not prove a joint limit, a gapless interacting continuum theory, or the nonexistence of an admissible gapped Yang–Mills theory. It shows precisely why fixed-cell weak-coupling constants do not supply the missing uniform bound.

## 7. Verification, provenance, and source interpretation

Commands run in the assigned project folder:

    python checks/U027_shared_link_checks.py --output evidence/U027_checks.json
    python checks/U026_one_plaquette_certificate.py --test
    python -m compileall -q checks/U027_shared_link_checks.py
    python -m tabnanny checks/U027_shared_link_checks.py

All 11 U027 tests passed; all 9 U026 tests passed again. The new suite uses Python 3.13.5 and SymPy 1.14.0, exact rational arithmetic and symbolic polynomial identities. It independently implements right-invariant quaternion derivatives and the reduced invariant differential operator, comparing them on all 22 monomials of weighted degree <=4. Haar symmetry is checked on all pairs of monomials of degree <=3. The declared graph cases are 1x1, 2x1, 2x2, and 3x2; no unexecuted sweep is claimed. Electric triples up to j1,j2=2 audit the representation formula, but its completeness and all-spin proof are written above.

The oscillator eigenfunctions, sharp failure (6), invalid spin parity, chain condition, rank and edge counts are checked separately. Wolfram 15.0.1 re-derived (4)–(5) from quaternion vector fields and independently diagonalized both 2x2 matrices. The square-patch eigenvalue formula is proved by the sine recurrence; the finite graph checks are corroboration, not a universal certificate. The nonlinear spectral limit uses the written compactness proof, not the finite tests or a high-precision eigenvalue fit.

Compilation and indentation checks passed. No static Python linter/typechecker or Lean runtime was installed; no such successful check is claimed. Mathbox provides the research, literature and self-audit workflow, not an independent mathematical authority. No new Consensus result was obtained or claimed; its previously documented quota limit was not treated as evidence about the literature. No spending, public posting, outside contact or asynchronous job was initiated.

### Primary-source check and overlap

Source: Ale, Bauer, Jha, Ringer, Siopsis, *Quantum computation of SU(2) lattice gauge theory with continuous variables*, arXiv:2410.14580v1, checked 2026-09-15 at https://arxiv.org/html/2410.14580v1 . Equations (30)–(33) describe two-loop gauge reduction and the coupled quadratic operator; (37)–(38) give the same leading gap sqrt(3lambda). Our path variables differ from their tree choice. We derive (2) directly and do not import their finite-coupling variational gap as a lower bound. The leading two-plaquette result is known after convention translation, not a claimed new discovery.

There is a visible normalization inconsistency in the displayed ladder matrix (48): its off-diagonal entries 2/4 do not give the eigenvalues stated immediately afterward in (49). Our incidence construction gives absolute off-diagonal entries 1/4, consistent with the two-square operator (33) and those stated eigenvalues. Loop orientation can change their sign, not their magnitude. We use the derived matrix, not the inconsistent display. No conclusion about the entire paper follows from that local correction.

Official scope/status was checked at https://www.claymath.org/millennium/yang-mills-the-maths-gap/ . This unit makes no prize-eligibility or award claim. The problem remains the full Jaffe–Witten existence-and-gap target, not the finite planar models.

### Self-audit outcome

- Full simultaneous-conjugation state space and Haar measure: passed by path reduction.
- Shared-link coefficient and sign: passed by vector fields, perimeter loop and orientation reversal.
- Exact electric-sector completeness: passed by the multiplicity-free SU(2) tensor decomposition.
- No separate-trace eigenfunction at lambda>0: passed by the coefficient-of-s and mixed-derivative argument.
- True-vacuum centering and physical singlet restriction: passed; one-quantum gauge vectors are excluded, not all mixed states.
- Fixed-graph spectral-limit proof: self-reviewed using both min–max directions, localization and no-loss-of-mass compactness.
- Uniformity as graph size grows: NOT PROVED and deliberately not inferred.
- Four-dimensional continuum existence and mass gap: NOT ADDRESSED by these finite-model theorems.

## 8. Durable outcome and next discriminating target

Established: exact shared-link Hamiltonian and electric spectrum; a valid state saturating the 3/4 kinetic comparison; necessity of relative-orientation dependence in every positive-coupling eigenstate; the complete fixed two-square weak-coupling gap (2sqrt(3)+o(1))/a; and a fixed-rectangle extension whose leading square-patch coefficient falls as 1/N.

This unit makes the shared-state obstruction in U026 quantitative. It also rules out replacing a volume estimate by an unchanged cell gap. Neither positivity of the single cell nor accurate local oscillator asymptotics controls collective low-energy modes as a patch grows.

The next target is an actual-vacuum, centered Schur-complement estimate that retains these collective mixed-loop states on a growing spatial three-dimensional block. Its decisive missing quantity is the renormalized coarse-sector lower energy after integrating the complement, with error uniform in both weak coupling and block size. A finite-graph oscillator coefficient or an upper variational eigenvalue cannot substitute for it. Before any large computation, specify a joint scale and show which nonperturbative term could give such a lower energy rather than merely reproduce the vanishing face-matrix edge.

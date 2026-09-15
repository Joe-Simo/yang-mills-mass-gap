# U035 — true-vacuum cycle response, connected shared-link terms, and a local analyticity bound

Date: 2026-09-15. Base: private `Joe-Simo/yang-mills-mass-gap` commit `bbc252a65a7156fe8c40b721c1794d5a85e594a7` (U034).

**We have not solved the Yang–Mills problem yet.**

Evidence: self-reviewed finite-regulator identities, an exact response calculation at zero spatial coupling, and a convergent finite-source perturbation bound. Exact rational/symbolic tests corroborate specified algebra and scalar coefficients. No formal verification, independent expert review, novelty claim, homogeneous weak-coupling theorem, or continuum mass-gap bound.

## 1. Research decision, scope, and preserved state

U034's next obligation was an actual-vacuum conditional-variance response for overlapping physical cycle algebras. This unit does not substitute a static cylinder or an arbitrary boundary law. It differentiates the positive Wilson TRANSFER and its own Perron vacuum, derives the change in the conditional projections, and calculates the first connected shared-plaquette response exactly. A subsequent contour argument bounds all omitted Taylor orders when only finitely many spatial plaquette couplings are switched on sufficiently weakly.

There are two distinct scopes:

- The response identities in Sections 2–3 hold at any finite background of spatial couplings in the finite Wilson transfer. Their constants are not proved uniform in the interacting volume.
- The explicit coefficients and uniform exterior-volume analyticity bound in Sections 4–7 are about ZERO spatial coupling as the reference, followed by a fixed finite set of small spatial sources. Exterior spatial plaquette couplings remain zero. They are not estimates around a general interacting exterior or along the four-dimensional continuum trajectory.

This distinction is essential: deriving local Taylor coefficients does not establish convergence of the homogeneous linked-cluster expansion at a useful coupling.

The assigned folder was inspected. The supplied U034 archive restored 96 missing files; two existing entries matched; none was overwritten. All eight current U034 manifest hashes were checked before work. The remote head was pinned above and the original standalone Yang–Mills instructions were retrieved from current-conversation files. No local Git checkout, AGENTS file, or executable Mathbox ledger is present. Only the current README is intentionally changed among prior mathematical/evidence files; prior notes and checkers are preserved. No sibling project was accessed. The existing private-write and zero-additional-spend limits are unchanged.

## 2. Exact vacuum response at an arbitrary finite background

Let the spatial graph be a finite periodic even cubic lattice, side N>=4, as in U032–U034. All link variables are in SU(2). Write the normalized temporal convolution on every link as

    q_beta(U V*) = exp[beta ReTr(U V*)/2]/Z(beta),
    Z(beta)=2 I_1(beta)/beta,
    C_beta = tensor_product_e q_beta,        beta=beta_t>0.

The Hilbert space is product-Haar L2, restricted to gauge-invariant functions for physical statements. For nonnegative spatial plaquette couplings s_p, let

    w_p(U)=(1/2)ReTr U_p,        |w_p|<=1,
    V_s(U)=sum_p s_p w_p(U),
    T_s=exp(V_s/2) C_beta exp(V_s/2).                       (1)

This differs from the prior Wilson kernel only by field-independent positive factors, which change its Perron eigenvalue but neither its vacuum nor its NORMALIZED transfer. There is no new mass term or Hamiltonian convention. Let

    T_s psi_s=lambda_s psi_s,    psi_s>0,    integral psi_s^2 dmu=1,
    pi_s(dU)=psi_s(U)^2 dmu(U),
    K_s f=(lambda_s psi_s)^(-1) T_s(psi_s f).

At every fixed graph and finite real couplings the continuous strictly positive symmetric kernel has a simple positive top eigenvector. Its restriction to the gauge-invariant subspace contains that vacuum. The normalized K_s is a positive self-adjoint Markov contraction on L2(pi_s). Finite-regulator spectral isolation, not a conjectured volume-uniform gap, justifies differentiation and the reduced resolvent below.

Differentiate one spatial coupling s_p, keeping the observable w_p fixed. Define

    w_p^c=w_p-E_pi w_p,
    h_p=partial_p log psi,       E_pi h_p=0,
    sigma_p=partial_p log(dpi/dmu)=2h_p.

The Perron equation and T'_p=(w_p T+T w_p)/2 give

    partial_p log lambda = E_pi w_p,
    (I-K)h_p=(I+K)w_p^c/2,
    sigma_p=(I-K)^(-1)(I+K)w_p^c
           =w_p^c+2 sum_(k>=1) K^k w_p^c.                (2)

The inverse acts on the centered physical subspace only. The series converges in L2 for each fixed regulator. No finite-horizon extrapolation is used.

For a bounded fixed observable f,

    partial_p E_pi f
      =Cov_pi(f,w_p)+2 sum_(k>=1)<f^c,K^k w_p^c>_pi.      (3)

This is an exact susceptibility/linear-response identity in the same vacuum as U034. At an arbitrary interacting background, it is NOT a local formula: a local plaquette source can have a long response through the powers of K.

If r_*=||K|H_phys^0||<1, the direct estimate from (2) is

    ||sigma_p||_2 <= [(1+r_*)/(1-r_*)] ||w_p^c||_2.        (4)

Using a scale-uniform r_*<1 to prove the desired mass gap would be circular. Equation (4) is a finite-regulator check, not the sought bound. The useful missing input is a connected-response estimate stronger than this full resolvent norm.

## 3. Response of the actual conditional variances and histories

Let nu_s be any one of these positive smooth finite-regulator probabilities: pi_s at a time slice or the actual stationary slab law below. Fix a coordinate sigma-algebra R; its definition does not depend on the coupling. Put

    P_s f=E_nu_s[f|R],
    h_f=f-P_s f,
    D_R(s;f)=E_nu_s[h_f^2],
    Sigma_p=partial_p log(dnu_s/dreference).

For real bounded f, differentiating the conditional density gives

    partial_p P_s f=E_nu_s[h_f Sigma_p|R],
    partial_p D_R(s;f)=E_nu_s[Sigma_p h_f^2].             (5)

The derivative of the minimizing conditional function drops out of the FIRST variance derivative by conditional orthogonality. It does not disappear at second order. With Sigma_pq=partial_p partial_q log density,

    partial_p partial_q D_R(s;f)
      = E[(Sigma_p Sigma_q+Sigma_pq) h_f^2]
        -2 E[E(h_f Sigma_p|R) E(h_f Sigma_q|R)].          (6)

Proof: differentiate the first identity in (5) or the squared residual. Since h'_p=-E[h_f Sigma_p|R], the two differentiated residuals give the last term. These identities extend bilinearly; unbounded observables require their stated integrability/differentiability conditions and are not silently included.

For the stationary slab of depth n, the exact law from U033 is

    dP_(s,n)=lambda_s^(-n) psi_s(U_0)psi_s(U_n)
       exp[V_s(U_0)/2+sum_(t=1)^(n-1)V_s(U_t)+V_s(U_n)/2]
       product_(t=0)^(n-1) C_beta(U_t,U_(t+1)) product_t dmu(U_t).

Its source score is

    Sigma_(p,n)=h_p(U_0)+h_p(U_n)
       +(w_p(U_0)+w_p(U_n))/2
       +sum_(t=1)^(n-1)w_p(U_t)-n E_pi w_p.              (7)

Both vacuum endpoint terms are retained. Its mean is zero, and testing (7) against f(U_0) reproduces (3), independently of n. Formulae (5)–(7) apply directly to the retained-history projections Pi_c of U034, with f replaced by J_0 f. Centering f by its changing vacuum expectation does not change the conditional residual.

Thus the history-variance coefficient now has an exact response formula in the true measure. A uniform bound for these forms for EVERY centered physical endpoint observable remains unproved. No differentiation of an infimum over observables or replacement of the history projection by a one-time projection is made.

## 4. Exact zero-spatial-coupling reference and its complete physical gap

At s_p=0 for every plaquette, psi_0=1 and pi_0 is product Haar EXACTLY; this is not an approximation to a nonzero-spatial-coupling vacuum. Let

    r=I_2(beta)/I_1(beta),
    u=I_3(beta)/I_1(beta),
    c=r^4.                                                (8)

A matrix coefficient of spin j on one link is an eigenfunction of C_beta with eigenvalue I_(2j+1)(beta)/I_1(beta). This follows from the normalized character convolution, not from a finite representation cutoff. Every nontrivial single-link coefficient is <=r<1: DLMF's integral for I_nu and derivative recurrence imply

    I_(nu+1)(beta)/I_nu(beta)
      = E_nu[cos theta],
    density_nu(theta) proportional to exp(beta cos theta) sin(theta)^(2nu),

which lies strictly between zero and one for beta>0, nu>=1. Multiplying these ratios proves the assertion for all integer character labels.

In a gauge-invariant spin network, a vertex cannot meet just one nontrivial edge representation. Hence the nontrivial support has a cycle. On the stated simple bipartite cubic graph its support has at least four edges. Each nontrivial edge contributes a temporal coefficient at most r; therefore

    ||C_beta|H_phys^0|| <= r^4=c.

A fundamental plaquette trace attains c, so equality holds. Peter–Weyl completeness and projection to invariant intertwiners cover the entire physical space. A nontrivial support that branches is not omitted; it still contains a cycle and satisfies the same bound. Graphs with shorter cycles require their own girth in this argument.

For every elementary plaquette,

    C_beta w_p=c w_p,
    integral w_p=0,       integral w_p^2=1/4,
    partial_p psi|0=a w_p,    a=(1+c)/(2(1-c)),
    sigma_p|0=[(1+c)/(1-c)] w_p.                           (9)

These coefficients are independent of the number of additional lattice edges. At beta=0 the coefficient formula has its continuous value c=r=u=0; it is used as a boundary algebra check, not as a claim of a nontrivial finite-energy Hamiltonian for a rank-one transfer.

## 5. Two overlapping cycles: keep the shared representation

Choose two distinct elementary plaquettes p,q sharing precisely one edge. View their union as two exterior three-edge paths A,B and a common one-edge path C, all oriented between the same pair of vertices. Set

    U=A C^(-1)=x0 I+i x.sigma,
    V=B C^(-1)=y0 I+i y.sigma,
    w_p=x0,       w_q=y0,
    F=x0 y0,      G=x.y.

Haar reduction gives independent Haar U,V, with residual simultaneous conjugation. In particular G is gauge invariant. It is the difference between a normalized perimeter-loop trace and the product of the two individual normalized traces:

    v_0=F+G=(1/2)Tr(UV^(-1)),
    v_1=3F-G,         F=(v_0+v_1)/4.                     (10)

The temporal transfer acts on this whole degree-(1,1) physical sector, not just on separate traces. Integrating the six exterior fundamental link coefficients contributes r^6. The remaining shared quaternion h has

    E h0^2=(1+3u)/4,
    E h_i h_j=(1-u)delta_ij/4,
    E h0 h_i=0.

Common right multiplication of U,V consequently gives

    C_beta F=(r^6/4)[(1+3u)F+(1-u)G],
    C_beta G=(r^6/4)[3(1-u)F+(3+u)G].                    (11)

Therefore

    C_beta v_0=z_0 v_0,       z_0=r^6,
    C_beta v_1=z_1 v_1,       z_1=r^6 u.                  (12)

The z_0 mode has shared-link spin zero; the z_1 mode has shared-link spin one. They are the complete two channels produced when the two fundamental factors on the common link are multiplied. Their norms are

    ||F||^2=1/16, ||G||^2=3/16, <F,G>=0,
    ||v_0||^2=1/4, ||v_1||^2=3/4, <v_0,v_1>=0.           (13)

This is a group-convolution derivation. U027's Hamiltonian mixed-state calculation is a useful convention check, but its continuous-time Casimir spectrum is not substituted for the finite-temporal Wilson transfer.

### Mixed true-vacuum derivative

Set all spatial couplings to zero after differentiating p and q. Since E(F)=0, lambda'_p=lambda'_q=lambda''_pq=0, and normalization gives E psi''_pq=0. Differentiate the full equation T_s psi_s=lambda_s psi_s twice. With a from (9),

    (I-C_beta) psi''_pq
       = [a c+(1+2c)/4]F+(a+1/4)C_beta F.                (14)

The terms on the right come respectively from T'_p psi'_q + T'_q psi'_p and T''_pq 1. None is deleted. On an eigencomponent z of F,

    psi''_pq coefficient k(z)
       =[1+3c+(3+c)z]/[4(1-c)(1-z)].

Taking the logarithm subtracts psi'_p psi'_q=a^2 F. The resulting connected coefficient simplifies exactly to

    b(z)=k(z)-a^2=(z-c^2)/[(1-c)^2(1-z)],
    partial_p partial_q log psi|0
       =[b(z_0)v_0+b(z_1)v_1]/4,
    partial_p partial_q log pi|0
       =[b(z_0)v_0+b(z_1)v_1]/2.                         (15)

For link-DISJOINT plaquettes, C_beta F=c^2 F and the connected mixed derivative is zero. This cancellation is exact. For the shared plaquettes, z_0>z_1 and

    b(z_0)-b(z_1)
       =[(1+c)/(1-c)] (z_0-z_1)/[(1-z_0)(1-z_1)]>0.      (16)

Thus the logarithm of the true vacuum has a nonzero mixed-orientation term for every beta>0 at this response order. A product of two individual class-function vacua misses it. This is not a fit of a trial wavefunction.

### Observable response and a directly physical loop correlation

Using (13) and differentiating pi=psi^2 gives

    partial_p partial_q E_pi G|0
       =(3/32)[b(z_0)-b(z_1)] > 0,                       (17)

    partial_p partial_q Cov_pi(w_p,w_q)|0
       =[b(z_0)+3b(z_1)]/32.                             (18)

The subtraction of the product of the changing means is necessary in (18). At the reference each variance is 1/4, so the mixed derivative of the standardized trace correlation is [b(z_0)+3b(z_1)]/8. Only this two-observable matrix element is calculated; it is NOT the smallest eigenvalue of a complete conditional-variance operator.

Equation (17) gives a positive mixed-loop witness without requiring a separate all-beta sign theorem for (18). The checker supplies certified intervals for both responses at the six named beta values; their observed signs are not extrapolated into an unproved general inequality.

## 6. All-order remainder control for finitely many active plaquettes

The preceding coefficients are derivatives of an analytic eigenstate, not an assumed asymptotic series. Here is an explicit exterior-volume-independent domain, with its scope kept visible.

Switch on only p,q, or another fixed finite set J, with all other spatial couplings ZERO. Write S=sum_(p in J)|s_p|, allowing complex s_p for analyticity, and let

    d=1-c=1-r^4>0,       delta=exp(S)-1.

Since ||C_beta||=1 and ||exp(V_s/2)||<=exp(S/2),

    ||T_s-C_beta|| <= exp(S)-1=delta.                     (19)

On the physical-space contour |z-1|=d/2, the unperturbed resolvent has norm <=2/d. If delta<=d/10, Neumann inversion gives a well-defined analytic Riesz projection E_s and

    ||E_s-E_0|| <= delta/(d/2-delta) <= 1/4.               (20)

Proof of the constant: integrate the resolvent identity around this circle; its radius d/2 multiplies (2/d)delta/(d/2-delta). The analytic projection has constant rank one because its distance from E_0 is below one.

The kernels T_s and E_s are symmetric under transposition for the complex bilinear Haar pairing. Let v_s=E_s 1 and q_s=integral v_s dmu. Then integral v_s^2=q_s, |q_s-1|<=1/4, and ||v_s||_2<=5/4. Choose the analytic square-root branch at one and put

    psi_s=v_s/sqrt(q_s).

For real small sources this is exactly the normalized positive vacuum. For complex sources it is its bilinearly normalized analytic continuation, not a claim of positivity. Its norm obeys

    ||psi_s||_2^2 <= 25/12.                               (21)

For every bounded observable O with ||O||_infinity<=1,

    F_O(s)=integral O psi_s^2 dmu

is holomorphic and |F_O|<=25/12 in the domain (19)-(20). This is an EXPECTATION remainder bound; no volume-uniform sup norm of log psi is inferred.

For the two-source case let

    rho=(1/2)log[1+d/10].

The polydisc |s_p|,|s_q|<=rho lies in that domain. Cauchy's formula bounds every coefficient of s_p^i s_q^j by (25/12)rho^(-i-j). If both source moduli are at most x rho, 0<=x<1, the sum of ALL terms of total degree at least three is bounded by

    |F_O-Taylor_(total degree<=2) F_O|
      <= (25/12) x^3(4-3x)/(1-x)^2.                      (22)

This follows by summing sum_(k>=3)(k+1)x^k, not by comparing a few truncated matrices. It is independent of inactive exterior volume. In fact with only J active, (1) tensorizes between the union of J's edge supports and all inactive exterior edges. This makes the limited kind of exterior independence transparent: the exterior has NO nonzero spatial action. The same conclusion must not be asserted for an interacting exterior.

For real sources in this domain, min-max also gives the complete physical normalized-transfer estimate

    ||K_s|H_phys^0|| <= (c+delta)/(1-delta)<1,
    Delta_s >= -log[(c+delta)/(1-delta)]/tau.              (23)

Here tau is the specified microscopic physical time. This is a true-vacuum finite-source stability bound including all physical states, not a Ritz lower-bound inference. It is not a homogeneous many-plaquette theorem. The finitely many local interactions and the zero-spatial-coupling exterior are explicit restrictions.

## 7. What happens as temporal coupling increases

Fixed-order positive-real Bessel asymptotics, or the recurrence u=1-4r/beta together with those asymptotics, give

    r=1-3/(2beta)+3/(8beta^2)+O(beta^-3),
    u=1-4/beta+6/beta^2+O(beta^-3).

Consequently

    d=6/beta+O(beta^-2),
    (1+c)/(1-c)=beta/3+O(1),
    b(z_0)=beta^2/108+O(beta),
    b(z_1)=-beta^2/468+O(beta),
    partial_p partial_q E_pi G|0=beta^2/936+O(beta),
    partial_p partial_q Cov_pi(w_p,w_q)|0=beta^2/11232+O(beta). (24)

These are fixed response coefficients; no exchange with volume, source order or a continuum limit occurs. They identify a growing susceptibility, not an actual divergence of bounded observable values: the Taylor domain shrinks at the same time. Specifically rho=3/(10beta)+O(beta^-2). Holding nonzero sources fixed and extrapolating (24) outside this domain would be invalid.

### Structural follow-up: disconnected source supports cancel at EVERY order

Form the graph on a finite set J of active plaquette sources by joining two sources precisely when their plaquettes share a spatial LINK. Suppose this graph has components J_1,...,J_m. Their edge unions are pairwise disjoint, although their vertices may overlap. Since all exterior spatial sources are zero, both the temporal convolution and the multiplication factors split across these edge unions:

    T_s = tensor_product_(alpha=1)^m T_(s restricted to J_alpha)
          tensor C_(inactive edges).

On the full product-Haar Hilbert space the unique normalized positive top eigenvector and eigenvalue consequently obey

    psi_s = product_alpha psi_(s restricted to J_alpha),
    lambda_s = product_alpha lambda_(s restricted to J_alpha).

Each factor is gauge invariant, so these are also the physical vacuum and eigenvalue. Taking logarithms proves that any mixed source derivative of log psi or log lambda vanishes whenever its distinct-source support is disconnected. Repeated derivatives at a source do not change the conclusion. The finite-graph positive kernel gives smooth eigenfunctions and their logarithms near the reference; no volume-uniform sup-norm analyticity radius for log psi is required for this factorization identity.

This is an exact all-order LINKED-SUPPORT selection rule, not an all-order magnitude estimate. It follows from tensor factorization, not from extrapolating the two-source computation. The connected shared-link term (15) is the smallest nonzero instance. On an interacting exterior these factors no longer separate, so this proof must not be transplanted unchanged.

For homogeneous s_p=s on P_s plaquettes, the crude norm estimate (19) contains S=P_s|s|. It would require |s| of order d/P_s, losing volume again. The all-order disconnected cancellation identifies which coefficients can occur, but does NOT bound the sum of connected coefficients as their order and spatial extent grow. A summable connected norm remains unproved.

In particular, the isotropic sequence s=beta_t->infinity is outside the present perturbative domain. Neither (22) nor (23) is a continuum-useful estimate for that sequence. This is a limitation of the certified method, not proof of a vanishing Yang–Mills mass.

## 8. Sources, exact checks, and self-audit

Primary sources checked 2026-09-15:

- NIST DLMF 10.32.2 and 10.29.1-2: normalized Haar/Bessel integral, character ratios, derivative recurrence. DLMF 10.40.1: fixed-order positive-axis asymptotics used only for orders 1,2,3 in (24). The representation-order inequality after (8) has the displayed integral proof. URLs: https://dlmf.nist.gov/10.32 ; https://dlmf.nist.gov/10.29 ; https://dlmf.nist.gov/10.40 . Finite certificates use positive convergent series, not large-beta asymptotics.
- Anne Greenbaum, Ren-cang Li, Michael L. Overton, *First-order Perturbation Theory for Eigenvalues and Eigenvectors*, arXiv:1903.00785v2, 2019-06-03; Theorem 2, equations (7)-(8), and Section 3.3 contour/eigenprojector construction were read in HTML. Their theorem is for matrices. We use it for method/attribution context, NOT as an unexplained infinite-dimensional implication. The compact-operator contour estimate (19)-(22) and differentiated Perron equation are supplied directly here. URL: https://arxiv.org/html/1903.00785v2 . Published version DOI 10.1137/19M124784X.
- M. Fukuma, D. Kadoh, N. Matsumoto, *Tensor network approach to 2D Yang-Mills theories*, arXiv:2107.14149v1, Section 2.2 and Appendix A (A.7)-(A.12): normalized character convolution and Peter-Weyl dictionary. These group identities, not its tensor-network approximations or a two-dimensional spectrum, underlie the transfer eigenvalues in (8)-(12). URL: https://arxiv.org/html/2107.14149v1 .
- The search also found the classical coupled-cluster/linked-cluster vacuum literature, including hep-lat/9212025 and DOI 10.1016/0550-3213(84)90218-9. The former's requested HTML was unavailable; only discovery abstracts were checked. No convergence theorem from those papers is imported. No broad novelty search or novelty claim is made.
- The current CMI Yang–Mills page was checked and remains marked unsolved: https://www.claymath.org/millennium/yang-mills-the-maths-gap/ . No contact, submission, publication or payment action was taken.

`checks/U035_vacuum_cycle_response_checks.py` passed 12 focused exact tests with Python 3.13.5/SymPy 1.14.0. The tests audit: the differentiated source equations and logarithm subtraction; shared-noise eigenchannels and their Gram adjoint; Haar response moments; disjoint cancellation and the positive orientation difference; the fixed-order large-beta constants; an actual weighted Perron-response identity in a four-state non-Wilson fixture; both conditional-variance derivatives including the nonzero projection-response term; complete stationary-path score enumeration at depths 1,2,3 (at most 256 paths); contour and full-tail algebra; two periodic cubic support geometries N=4,6; all-tail SU(2) coefficient intervals for beta=0,1/2,2,8,32,128; and deliberate invalid-input controls.

The SU(2) coefficient intervals reuse the unchanged U029 positive-series implementation and U030 character-ratio routine with a 4096-term cap and 52-digit rational width target. All interval operations are rational; 22-place decimal endpoints are rounded outward. The reported coefficients are derivatives at zero spatial coupling, not measurements at positive spatial coupling. No floating-point vacuum eigenvector or spectral fit enters a proof.

Wolfram 15.0.1 separately corroborated the two eigenchannels, Haar adjoint, connected-coefficient subtraction, disjoint zero, positive-difference factorization, constants {1/108,-1/468,1/936,1/11232}, contour coefficient 1/4 and the bivariate-tail identity. Its first asymptotic-limit call emitted divide-by-zero warnings; a clean rerun canceled the exact rational expressions before evaluating their removable limits. Both the warning record and clean result are retained. This is corroboration of submitted algebra, not an independent derivation of the complete argument.

The previous U034 suite is rerun into new U035 evidence. Compilation and indentation checks are run. Static lint/typecheck and formal-proof tools are only reported when actually present; they are not inferred from a successful compile. Commands, versions, outputs and preserved-source hashes are in the new manifest. No earlier note/checker is rewritten. Mathbox supplies workflow guidance, not a separate expert judgment; Consensus's documented quota failure was not invoked again merely to repeat it.

### Audit verdict and next action

Primary verdict: **proved after the finite-regulator and zero-spatial-reference/finitely-many-small-sources restrictions explicitly stated above**.

Passed: true-vacuum differentiation, the exact full-time susceptibility, history endpoint scores, differentiation of the conditional measure and projection, complete shared-link representation channels, mean subtraction in the connected covariance, fixed-source analytic continuation with an explicit all-order expectation tail, all-order cancellation of disconnected source supports, and a complete physical-space finite-source stability estimate.

Not proved: a useful uniform response bound at a nonzero homogeneous spatial background; a summable connected-cluster expansion as the number of active plaquettes grows; the endpoint-history variance coefficient required by U034 in the joint limit; four-dimensional continuum existence/axioms/nontriviality/mass gap; the general group target.

The next discriminating step is an ALL-ORDER connected-support estimate, not another unqualified finite Taylor table. In (15), disjoint supports cancel exactly and a shared link creates explicit perimeter/adjoint channels. Test whether the logarithmic-vacuum expansion can be organized with a norm such as sup_e sum_(X containing e) exp(alpha |X|) ||Phi_X||, retaining representation labels and the small denominators from C_beta. The necessary new input is a recursive connected-coefficient bound that remains independent of the total number of active plaquettes; its temporal-coupling dependence must be tracked before any proposed continuum use. The arbitrary-background identities (2), (5)-(7) remain the alternative route if expansion at the zero-spatial reference cannot reach a useful regime.

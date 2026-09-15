# U030 — overlapping Wilson-link integration and the missing temporal memory

Date: 2026-09-15. Base: private `Joe-Simo/yang-mills-mass-gap` commit `e18b3ece3daaa5d4427d800d67af1262b424c8d6` (U029).

**We have not solved the Yang–Mills problem yet.**

Evidence: self-reviewed restricted finite-lattice proofs, exact rational group-integral certificates, and an abstract positive-transfer counterexample. No formal verification, independent expert verification, global novelty claim, physical mass-gap bound, or continuum construction.

## 1. Research contract and preservation

U029's first elimination layer was exact but its generated interactions share retained links. This unit executes its next local test, then checks the separate implication from a coordinate marginal to a temporal transfer operator. Three questions are addressed:

1. Can two first-layer stars followed by their common retained link be integrated without discarding connected terms? Yes: an exact three-link formula and, for vanishing central external source, a uniformly convergent character expansion are obtained.
2. Is their normalized connected conditional response automatically small at weak bare coupling? No: realizable boundary links give an exact response approaching one; even completely aligned boundary links leave a nonzero normalized response in the fixed-cluster weak-coupling limit.
3. Does an exact static marginal automatically give an exact memoryless transfer on the retained coordinates? No: the two-step defect is a positive square, and an exact four-state example demonstrates the failure. A temporal memory/Schur estimate remains necessary for that proposed closure.

All work is confined to `/mnt/data/yang-mills-mass-gap`. The supplied U029 archive was inspected; 38 missing files were restored without replacing the two already present. All nine U029 manifest hashes matched before changes. The remote head and root were read; no root AGENTS.md, local Git checkout, or executable mathematical ledger was found. The project's supplied Yang–Mills prompt, including the zero-spend and private-write permissions, was retrieved and read across its complete sections. Prior notes/checkers are left unchanged. Updating the README intentionally changes one historical manifest-covered file; its old bytes remain in the prior Git revision and archive.

The full target remains the Jaffe–Witten assertion for every compact simple group on four-dimensional spacetime, with the required axioms, identification, nontriviality, and finite positive physical mass. Our new calculations are SU(2) finite conditional marginals, not a construction satisfying that target. The older U009–U023 scalar chain is not a dependency here.

## 2. An actual three-link geometry, not independent plaquettes

Use U029's Euclidean convention

    S_beta = beta sum_p [1 - ReTr(U_p)/2], beta >= 0.

Beta is the Wilson inverse coupling, not the Hamiltonian parameter lambda=4/g^4. Work on a periodic four-dimensional lattice of even side L>=6. Choose direction-0 links U,V,W based at spatial positions 0, e_1, 2e_1, all at the same time and the same other coordinates. Set the transverse connectors between these three links to the identity. Their two common plaquettes have normalized traces

    ReTr(U V*)/2 = u.v,   ReTr(V W*)/2 = v.w,

where U=u0 I+i u_vec.sigma, and u=(u0,u_vec) is a unit vector in R^4; similarly for v,w. A dot now denotes the Euclidean R^4 product.

Each of the three links belongs to six plaquettes. The endpoint links U,W each have five other three-edge detours; V has four other detours. U and W do not share a plaquette. They belong to the same even-spatial-parity elimination layer of U029, while V is retained by that layer. Their generated factors share V. No plaquette contains all three.

Write A,B,C for the quaternion sums of the external detours for U,V,W, respectively. With all other links conditioned on, the part of the normalized measure involving these variables is proportional to

    exp{beta[u.v + v.w + u.A + v.B + w.C]} dU dV dW.     (1)

All plaquettes not meeting U,V,W contribute only a conditional normalization constant. The vectors A,B,C are not assumed independently distributed. This is a conditional identity, not a claim that stars are independent in the full measure. Nonidentity connecting paths on a chain can be absorbed by Haar-preserving parallel-transport changes of variables; the explicit identity-connector geometry alone suffices for the examples below.

## 3. Exact second elimination

Retain U029's entire scalar function

    Z(z) = 2 I_1(z)/z,  Z(0)=1.

Integrating U and W first, conditionally on V, gives

    I_beta(A,B,C)
      = integral_SU(2) exp(beta B.v)
          Z(beta |A+v|) Z(beta |C+v|) dV.                (2)

This is the exact next integration, including the overlap. The product is inside the V integral. Replacing it by the product of two V integrals is not an identity. Formula (2) remains regular when A+v or C+v vanishes, since Z is entire in the square of its argument.

If A=B=C=0, the integral is Z(beta)^2. This special constant partition value does not make the response to boundary/source changes independent; the mixed derivatives computed below are nonzero.

### Character expansion when the central source B vanishes

For alpha=beta|A|, eta=beta|C|, choose unit quaternions Ahat,Chat in their directions when nonzero, and set Q=Ahat Chat*. Let l=0,1,... label the spin-l/2 representation,

    d_l=l+1,
    chi_l(Q)=sin((l+1)theta)/sin(theta),
    t_l(z)=I_(l+1)(z)/I_1(z).

Use t_0(0)=1 and t_l(0)=0 for l>0; no unit direction is needed when its amplitude is zero. Then (2) has the exact expansion

    I_beta(A,0,C) / [Z(alpha) Z(eta) Z(beta)^2]
      = sum_(l>=0) d_l t_l(alpha)t_l(eta)t_l(beta)^2 chi_l(Q).  (3)

Derivation: the central weight w_z(G)=exp(z ReTr G/2) has character coefficient

    integral w_z(G) chi_l(G)dG = 2(l+1)I_(l+1)(z)/z.

The Haar class integral follows by writing sin(theta)sin((l+1)theta) as the difference of two cosines and applying I_l-I_(l+2)=2(l+1)I_(l+1)/z. Thus w_z=Z(z)sum_l d_l t_l(z)chi_l. Haar matrix orthogonality gives chi_l*chi_k=delta_lk chi_l/d_l. Applying this to the four weights with arguments alpha,beta,beta,eta proves (3). All orientations agree because SU(2) characters are real and central.

This is a standard compact-group convolution calculation after translating notation, not a newly claimed representation-theoretic principle.

### Uniform, explicit truncation error

The positive Bessel series gives the all-order bound

    0 <= t_l(z) <= (z/2)^l/(l+1)!   (z>=0),              (4)

and also t_l(z)<=1. For (4), divide the positive series for I_(l+1) by that for I_1; termwise (k+1)!/(k+l+1)! <= 1/(l+1)!. The bound by one follows by integrating |chi_l|<=d_l against the positive normalized weight.

Put X=alpha eta beta^2/16. Since |chi_l|<=d_l, the absolute l-th summand of (3) is at most

    T_l = (l+1)^2 X^l / [(l+1)!]^4.

These terms satisfy exactly

    T_(l+1)/T_l = X/[(l+1)^2(l+2)^2].

Therefore truncation after l=M has uniform absolute error at most

    T_(M+1)/(1-r_M),
    r_M=X/[(M+2)^2(M+3)^2] < 1.                         (5)

The uniformity in (5) is over the retained relative holonomy Q at the specified finite parameters. It is NOT an error uniform over an arbitrarily large network or an infinite sequence of integrations. For large beta the degree needed by this elementary certificate also increases.

The checker encloses every coefficient with exact rational positive-series tails, applies signs of the exact rational character values, and adds (5). Thus it controls the entire infinite character tail rather than interpreting a truncation as the original integral. Example normalized integral enclosures at Q=I:

    (alpha,eta,beta)=(1,1,1):
      [1.013335255186407790, 1.013335255186407791], M=5;
    (2,3,4):
      [1.461133778593301856, 1.461133778593301857], M=9;
    (4,4,8):
      [2.580261641528957091, 2.580261641528957092], M=13.

All displayed endpoints are rounded outward from rational bounds. They are scalar integral certificates, not mass measurements. Independent 50-digit one-dimensional Haar quadrature at these aligned-source inputs agreed, but is only noncertified corroboration. Additional certificate tests use half traces -1,0,3/5,1; the all-holonomy error bound is the written inequality (5).

## 4. Realizable boundary cancellation and an exact connected response

The external detours can be made to sum to zero for ALL THREE selected links simultaneously using actual neighboring links. Set every transverse link to I. Each detour then equals its middle direction-0 link. The endpoint external lists each have five distinct middle links; assign

    I, -I, I, R_+, R_-,
    R_+ = diag(-1/2+i sqrt(3)/2, -1/2-i sqrt(3)/2),
    R_- = R_+*.

Their sum is zero. For V's four external middle links assign I,-I,I,-I. For L>=6 these 14 external links are distinct and outside U,V,W, so the assignments do not conflict. The test explicitly enumerates the actual plaquettes and assignments for L=6,8. The geometric argument supplies the stated all-L result.

With these boundary links, the exact conditional law is

    dmu_beta = exp{beta(u.v+v.w)} dU dV dW / Z(beta)^2.  (6)

Each marginal is Haar. Given V, U and W are independent, but their conditional means are

    E[u|v]=r(beta)v,  E[w|v]=r(beta)v,
    r(beta)=I_2(beta)/I_1(beta).

To see the first identity, rotate v to the north pole of S^3. Orthogonal coordinates have zero mean by reflection, and the parallel coordinate has mean Z'/Z=r. Haar isotropy gives E[v_i v_j]=delta_ij/4. Consequently

    E[u_i]=E[w_i]=0,
    E[u_i u_j]=E[w_i w_j]=delta_ij/4,
    Cov(u_i,w_j)=r(beta)^2 delta_ij/4.                  (7)

In particular, for the closed plaquette-trace observables formed from an I-valued external detour, Phi_U=ReTr(U)/2=u0 and Phi_W=w0,

    Corr(Phi_U,Phi_W)=r(beta)^2.                         (8)

These traces are closed-loop observables using fixed surrounding paths, not open-link color coordinates presented as physical states. If the surrounding paths are gauge transformed as well, the loop traces remain invariant.

The same response is visible after both stages of integration. Introduce linear diagnostic sources h.u+k.w into (6). The mixed Hessian of the log integral at h=k=0 is r(beta)^2 I_4/4. The full source Hessian is

    (1/4) [[I_4, r(beta)^2 I_4],
           [r(beta)^2 I_4, I_4]].                       (9)

A product of separate source integrals would give zero off-diagonal blocks, contradicting (7). These sources differentiate the conditional partition function; they are not new matter fields or a modification proposed as a Yang–Mills solution. For actual retained-link variations, vary the I-valued direction-0 external link at transverse positions e_2 and 2e_1+e_2 in the endpoint lists by exp(i t sigma_3) and exp(i s sigma_3), respectively. They share no elementary plaquette for L>=6. The mixed second derivative of the negative log integral is -beta^2 r(beta)^2/4 at t=s=0; plaquettes meeting neither integrated link give no direct mixed derivative for this pair. Thus this connected term is genuinely produced by the two overlapping stars. Diagonal retained-link derivatives also include second derivatives of the source paths; they must not be confused with the pure covariance Hessian (9).

For every beta>0, 0<r(beta)<1. At large beta, fixed-order positive-axis Bessel asymptotics give

    r(beta)=1-3/(2 beta)+O(beta^-2),
    Corr(Phi_U,Phi_W)=1-3/beta+O(beta^-2).               (10)

An elementary concentration proof also gives r(beta)->1: under exp(beta u0)dU the mass outside any fixed neighborhood of u0=1 tends to zero by the same numerator/denominator comparison as U005. No asymptotic series is needed for the limiting obstruction.

Exact rational enclosures for (8), not fitted correlations:

    beta=1:  [0.0576930249865809182773, 0.0576930249865809182774]
    beta=6:  [0.5817510666277618748399, 0.5817510666277618748400]
    beta=24: [0.8801812786757984635944, 0.8801812786757984635945]
    beta=96: [0.9690750970406779063868, 0.9690750970406779063869].

Thus a uniformly vanishing normalized connected response over arbitrary surrounding configurations is FALSE. Even a fixed contraction factor strictly below one, uniform as beta->infinity over these conditionals, is impossible. The checker independently verifies the leading mixed-source coefficient beta^2/64 by three Haar second moments and by the Bessel series.

This is a worst-boundary statement. It neither estimates how often such surroundings occur under the full Wilson measure nor proves failure of an averaged cluster/RG estimate. At each finite beta, continuity makes neighboring boundary configurations have nearby responses; no positive beta-uniform probability of those neighborhoods is inferred.

## 5. A nonfrustrated comparison: the response need not vanish even at alignment

To distinguish a rare frustrated obstruction from ordinary coupling, set ALL surrounding links to I. Then

    A=5 I, B=4 I, C=5 I.

The unique minimum of the corresponding three-link action is U=V=W=I. Write u_vec=xi/sqrt(beta), v_vec=zeta/sqrt(beta), w_vec=omega/sqrt(beta) in its local chart. For each color component, the rescaled Gaussian precision matrix is

    M = [[6,-1,0],[-1,6,-1],[0,-1,6]],
    M^-1 = [[35/204,1/34,1/204],
            [1/34,3/17,1/34],
            [1/204,1/34,35/204]].                        (11)

This follows directly from the five, four, five external one-link deficits and the two differences |xi-zeta|^2 and |zeta-omega|^2. The eigenvalues are 6,6-sqrt(2),6+sqrt(2), all positive.

Here the finite-dimensional Laplace limit can be justified rather than merely asserted: outside any fixed small product neighborhood of I the continuous action exceeds its unique minimum by a positive constant; inside it the Hessian (11) supplies two-sided quadratic bounds. The Haar chart density is smooth and positive near I. Rescaling, dominated Gaussian bounds give convergence of polynomial moments through fourth order. The outside contribution is exponentially smaller than the beta^(-9/2) partition scale. No bound uniform in the number of links is asserted.

Consequently the component correlation tends to 1/35. For the actual scalar trace loops, beta(1-u0) converges in moments to |xi|^2/2. Wick's identity for the three independent color components gives

    lim_(beta->infinity) Corr(u0,w0) = (1/35)^2 = 1/1225.  (12)

Thus even completely aligned boundaries do not force this normalized connected scalar response to vanish. This fixed positive limit is small and may be absorbed in a valid nonperturbative scheme; it is NOT by itself a no-go for repeated RG. Equation (12) is an analytic fixed-three-link limit, not a certified finite-beta numerical enclosure and not a claim about a physical long-distance correlation.

## 6. The distinct temporal question: exact marginals need not be Markovian

There is another independent gap in interpreting a static decimation as an energy-gap argument. Suppose a genuine normalized positive self-adjoint transfer S at one specified physical time has already been constructed, with S Omega=Omega. Let P be a vacuum-preserving orthogonal projection onto retained observables in that TRUE vacuum Hilbert space, and Q=I-P. On the retained space define

    M_n = P S^n P,  M_0=I_retained,  A=P S P.

These are the exact retained two-time matrices/forms. Direct multiplication gives

    M_2-A^2 = P S Q S P = (Q S P)* (Q S P) >= 0.        (13)

Thus marginalizing coordinates is not the same as inserting P after every time step. For self-adjoint S, equality in (13) holds exactly when QSP=0, which also implies PSQ=0 and makes P reducing. In that case and only then M_n=A^n for every n. Otherwise the retained correlations retain memory of discarded variables.

Reflection positivity of a reflection-stable coordinate marginal can still hold, as U029 showed. It does NOT force a nearest-neighbor-in-time Markov description using only its current retained coordinates. Reconstruction from a suitable full positive-time algebra and replacement by a one-step compressed transfer are different operations. None of this says reflection-positive non-Markov measures are inadmissible QFT inputs.

### Exact bounded-operator memory recurrence

Write the full transfer in orthogonal blocks

    S = [[A,B],[B*,D]].

Starting from a retained vector with no Q component, solve its discarded component recursively. This gives, for n>=1,

    M_(n+1)=A M_n + sum_(j=0)^(n-1) B D^(n-1-j) B* M_j. (14)

The kernels B D^k B* are positive when S>=0. If D<=1-rho for rho>0, their sum converges in norm to

    sum_(k>=0) B D^k B* = B(I-D)^(-1)B*.                (15)

If rho tends to zero, a bound on B alone need not control this memory. Positivity of S does not remove it. This is a bounded discrete-time derivation; no unbounded generator domain is hidden in (14).

For the gap comparison now restrict S and the decomposition to Omega-perp, removing the vacuum separately; P preserves this centered space. The centered gap question consequently returns to the exact Schur condition. For 0<delta<1-||D||,

    I-S >= delta I
      iff I-A-delta I - B[(1-delta)I-D]^(-1)B* >= 0.    (16)

The equivalence is completion of the square, under the stated inverse bound. Equation (16) is the standard U003 Schur mechanism expressed as a quantitative temporal-memory obligation, not a new mass-gap theorem.

### Fully valid positive four-state counterexample

Let the following Euclidean-normalized vectors be orthonormal:

    Omega=(1,1,1,1)/2,
    u=(1,1,-1,-1)/2,
    v=(1,-1,1,-1)/2,
    w=(1,-1,-1,1)/2.

Set

    S=Omega Omega* +(u u*+v v*+w w*)/4 +(u v*+v u*)/8,
    P=Omega Omega*+u u*.

S is symmetric, entrywise nonnegative, row-stochastic and strictly positive as a self-adjoint matrix, with spectrum {1,3/8,1/4,1/8}. P is the ACTUAL conditional-expectation projection averaging states {1,2} and {3,4}, not an arbitrary invented coarse map. Its centered compression has eigenvalue 1/4, but

    M_2-A^2 = u u*/64.

The full centered transfer norm is 3/8 rather than 1/4. Treating the compressed matrix as exact would overstate the Hamiltonian gap at unit time: log(4) rather than log(8/3). All these statements are exact rationals/eigenvalues, checked symbolically; this is an abstract Markov example, not a Wilson-lattice counterexample. It can be assigned the finite self-adjoint Hamiltonian -log S because all its eigenvalues are positive.

In this example the integrated memory (15) is 1/48 on u. The zero-energy Schur deficit is 3/4-1/48=35/48, which must NOT itself be mistaken for the full operator gap; the shifted condition (16) is needed to certify a positive edge.

## 7. What this checkpoint changes

This local second integration, not an entire extensive second layer, is no longer just a proposed step: equations (2)-(5) give an exact overlapping local calculation and a reproducible all-tail certificate in a specified source subfamily. Equations (7)-(12) show precisely why neglecting the generated correlations cannot be justified merely by large beta. Equation (13) separately rules out identifying a static marginal with a memoryless temporal compression without an invariant-subspace or memory estimate.

The remaining viable direction is NOT to replace these interactions by one effective Wilson coupling or appeal to positive local Hessians. It is to retain connected interactions and temporal memory, then prove the volume/scale estimates actually needed. Strong local conditional correlation does not logically forbid that.

A concrete next task is to formulate a block/slab elimination that retains its boundary-time algebra, and estimate

    B[(1-delta)I-D]^(-1)B*

relative to I-A-delta in the same true-vacuum representation. This combines, rather than confuses, the generated-action and physical-time obligations. For a bounded preliminary test, derive the two-time boundary kernel of the three-link cluster and compare exact two-step correlations with a memory-retaining reduction; do not insert a Wilson ansatz or assume a volume-uniform gap for D. If a many-block argument needs suppression of cancelling surroundings, that suppression must be proved in the full measure, not deduced from their conditional behavior.

## 8. Sources, checks, and limitations

Sources checked 2026-09-15:

- NIST DLMF 10.32.1-2 and 10.29.1-2: the real-axis class integrals and Bessel recurrence used in (3), with nu=l+1. NIST DLMF 10.40.1: fixed-order positive-axis asymptotics used only for (10), not uniformly in l. URLs: https://dlmf.nist.gov/10.32 ; https://dlmf.nist.gov/10.29 ; https://dlmf.nist.gov/10.40 . The bounds/certificates also have direct positive-series proofs here and in U029.
- A. J. Chorin, O. H. Hald, R. Kupferman, *Optimal prediction with memory*, Physica D 166 (2002), 239-257, DOI 10.1016/S0167-2789(02)00446-3. The author-hosted published PDF was read, with rendered printed pp.241-242: Section 2 gives conditional-expectation projection and the memory identity (6)-(7). Source: https://math.huji.ac.il/~razk/Publications/PDF/CHK02.pdf . This is contextual overlap: its continuous Hamiltonian/Liouville setup is NOT imported as a Yang–Mills transfer theorem. Our bounded discrete-time identities are proved directly. The earlier PMC access attempt returned a browser check; the legitimate author copy was used instead.
- Jaffe-Witten official target, Sections 3-4, printed pp.5-6, read in rendered pages: https://www.claymath.org/wp-content/uploads/2022/06/yangmills.pdf . The current CMI problem page was checked and still lists it unsolved: https://www.claymath.org/millennium/yang-mills-the-maths-gap/ . No public submission, payment or acceptance claim is made.

No broad novelty search is claimed. The group convolution and projection-memory mechanisms are established mathematics. Mathbox supplies workflow guidance, not an independent mathematical verdict. The known Consensus quota failure was not retried just to repeat it. No paid jobs, outside contacts, publication, or asynchronous execution were initiated.

Checker: `checks/U030_overlap_and_transfer_checks.py`, using Python 3.13.5, SymPy 1.14.0, mpmath 1.3.0, and the unchanged exact positive-series routines in `checks/U029_exact_link_integration_checks.py`. Eleven focused tests passed. The exact geometry test covers (d,L)=(4,6),(4,8); the universal extension has the geometric proof above. Character coefficient tests cover l=0,...,5 and exponential powers 0,...,13, and character magnitude checks l=0,...,20; neither finite loop substitutes for the written all-order proofs. Memory recurrence powers n=1,...,6 are checked in the exact four-state example; (14) has the general proof above.

Rational tails use a 4096-term Bessel-series cap, a 512-character-label cap, and explicitly checked error budgets. Coefficients and signed character sums stay rational; only final displayed endpoints are rounded outward. Separate 50-digit quadrature is not certification. Wolfram 15.0.1 independently returned the r^2 series through beta^6, inverse (11), correlations 1/35 and 1/1225, the four-state spectrum, zero residual in (13), and zero residual in the tail-ratio identity. Those submitted expressions do not amount to an independent derivation of the whole research note.

Primary audit verdict: **proved after the explicit finite-conditional-cluster and bounded-operator restrictions**. The new identities and counterexamples are self-reviewed. Not established: probability of adverse surroundings in the true full measure; uniform overlapping-cluster expansion over successive scales; a gauge-invariant physical-time dictionary for coordinate decimation; a uniform actual-vacuum Schur/memory bound; continuum/infinite-volume convergence; nontrivial finite physical mass; groups beyond SU(2). There is no complete candidate.

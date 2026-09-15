# U029 — exact Wilson-link integration, gauge cancellation, and a non-Wilson coarse action

Date: 2026-09-15. Base: private `Joe-Simo/yang-mills-mass-gap` commit `85c188d2e2d966d9471f815146495cb15bdb20ad` (U028).

**We have not solved the Yang–Mills problem yet.**

Evidence: self-reviewed finite-lattice identities and comparison proofs; exact rational scalar-function enclosures; separately labeled numerical corroboration. No formal verification, independent expert review, global novelty claim, quantum mass estimate, or continuum construction.

## 1. Target, route decision, and preserved state

U028 proved a support-size-independent nonlinear magnetic comparison, then showed that its global small-field hypothesis is rare in the growing Gaussian reference. Its next dependency is integration of short fluctuations conditional on retained fields, without inventing a gauge-breaking mass.

This unit takes a deliberately exact companion route: integrate an actual link of the finite Euclidean Wilson measure, and then an extensive set of links which never share a plaquette. These are coordinate marginals, NOT spectral high-momentum shells. Nor is the conditional link distribution the spatial true-ground-state measure. A dictionary from this decimation to the Hamiltonian/physical-time bridge remains unproved. The reason for this choice is to test the fluctuation integration and gauge cancellations before trusting a Gaussian or cumulant approximation.

The supplied U028 archive was inspected and its missing contents restored only within `/mnt/data/yang-mills-mass-gap`; no existing file was replaced. All nine U028 manifest entries were checked before work. The original research prompt was read in full. The remote head was checked and pinned; no sibling project or external account data was used. Existing research notes and checkers remain unchanged. The README is the only historical manifest-covered file intentionally updated below to point to this new checkpoint; its old bytes remain in Git and the supplied archive.

Three executed questions:

1. Does exact local integration preserve gauge invariance and permit a global action bound without a small-field restriction? **Yes, for the explicitly defined one-layer marginal.**
2. Does averaging the positive action Hessian give the marginal Hessian? **No: a covariance term cancels the entire common gauge direction.**
3. Does this marginal close on one Wilson coupling, or have a uniformly narrow conditional Gaussian at large bare coupling? **Neither, under the unrestricted statements tested.**

## 2. Wilson conventions and one-link integral

Use a finite hypercubic Euclidean lattice in dimension d, link variables in SU(2), normalized Haar measure, and Wilson action

    S_beta(U)=beta sum_p [1-(1/2)Re Tr U_p], beta>=0.

Here beta is the ordinary Wilson inverse coupling beta_W (beta_W=4/g0^2 in four dimensions). It is NOT U028's Hamiltonian parameter lambda=4/g^4. No identification of these two couplings or of their probability measures is made.

Fix an oriented link e from x to y. There are m=2(d-1) adjacent plaquettes for an interior link. Write their three-edge detours from x to y as V_1,...,V_m, reversing products when necessary. The part of the weight depending on U_e is, up to a field-independent factor,

    exp[(beta/2)Re Tr(U_e H*)], H=sum_r V_r.

A real quaternion sum has the form H=h0 I+i h.sigma, so

    H*H=s^2 I, s^2=det H=h0^2+|h|^2, 0<=s<=m.

If s>0, H/s belongs to SU(2); right invariance of Haar measure reduces the integral to

    Z(beta s)=integral_SU(2) exp[z ReTr U/2] dU,
    Z(z)=(2/pi)integral_0^pi exp(z cos theta) sin^2 theta dtheta
        =2 I_1(z)/z,    Z(0)=1.                         (1)

The zero-staple case is included by the integral or its convergent series, not by dividing by zero. NIST DLMF 10.32.2 at nu=1 verifies this normalization. An independent derivation expands the exponential and uses the Haar moments

    E_Haar[u0^(2k)]=(2k)!/[4^k k!(k+1)!],
    Z(z)=sum_(k>=0) (z^2/4)^k/[k!(k+1)!].              (2)

This is a convergent exact integral at every finite beta, not a perturbative approximation. The one-link heatbath/group-integral mechanism is classical; no novelty is claimed.

Define F(z)=log Z(z), r(z)=F'(z). For z>0,

    r(z)=I_2(z)/I_1(z),  r(0)=0,
    F''(z)=Var_z(u0)>=0,  0<=r(z)<1.                  (3)

The derivative follows either from DLMF 10.29 or direct differentiation of (1). Positivity of r follows by pairing u0 with -u0, and the upper bound follows from |u0|<=1. Differentiation under the integral is legitimate on the compact group.

## 3. Exact retained-loop action and a global comparison

The staple norm depends only on retained closed loops:

    s^2=m+sum_(r<s) ReTr(V_r V_s*)
       =m^2-2 sum_(r<s) delta_rs,
    delta_rs=1-(1/2)ReTr(V_r V_s*)>=0.                 (4)

Here the symbol s in a summation index is only an index; elsewhere s denotes the nonnegative staple norm. Each V_r V_s* is the holonomy of a six-edge loop for distinct elementary detours. These loops need not lie in one plane.

Normalize the induced action to zero when all staples agree:

    Gamma_beta(V_1,...,V_m)=F(m beta)-F(beta s)>=0.      (5)

All generated loop dependence is retained. Under endpoint transformations

    V_r -> g_x V_r g_y^(-1), U_e -> g_x U_e g_y^(-1),

H transforms the same way and s is unchanged. Thus (5) is exactly gauge invariant, including at H=0. No independent-plaquette measure or deletion of Bianchi constraints has been assumed.

There is a useful global, non-small-field comparison. Convexity of F with F(0)=0 gives

    F(beta s)<=(s/m)F(beta m),

and r<=1 gives F(beta m)-F(beta s)<=beta(m-s). Since

    m-s=2 sum delta_rs/(m+s),

we obtain, for every m>=1, beta>=0 and every set of SU(2) staples,

    [F(m beta)/m^2] sum_(r<s) delta_rs
      <= Gamma_beta
      <= [2 beta/m] sum_(r<s) delta_rs.                 (6)

For m=1 both sides vanish. For m=0 there is no incident action and the integral is one; (6), which divides by m, is not used.

For an interior four-dimensional link, m=6, the coefficients in (6) are F(6beta)/36 and beta/3. They depend on beta but not on the lattice size. The lower coefficient is positive when beta>0. This is a comparison of classical effective ACTIONS, not of centered Hamiltonian gaps or spectral measures. Different ground energies and measures cannot be ignored.

## 4. Integrate an extensive layer without approximation

Let E_dec be any set of links such that no plaquette contains two members. Conditional on the remaining links, the integrations factor exactly:

    exp[-S_eff(U_ret)] proportional to
      exp[-S_out(U_ret)] product_(e in E_dec) Z(beta s_e).

Equivalently, after subtracting the constant sum_e[m_e beta-F(m_e beta)],

    S_eff^norm=S_out+sum_(e in E_dec) Gamma_beta(V_(e,1),...,V_(e,m_e)).  (7)

Here S_out includes precisely the plaquettes meeting no eliminated link. It is not a sum over all old plaquettes. Formula (6) can be summed in (7), giving a global bound with constants unchanged by the number of eliminated links. Shared retained links may couple many Gamma terms; their weights are not independent after the remaining integration.

An explicit extensive choice on an even periodic four-dimensional lattice with side at least four is: eliminate direction-0 links at vertices whose three spatial coordinates have even sum. A (0,nu) plaquette has two direction-0 edges with opposite spatial parity, and other plaquettes have none. Hence the no-two-in-a-plaquette condition holds. Exactly half of the direction-0 links, or one eighth of all links, are eliminated.

This set is stable under time reflection: a direction-0 link based at (t,x) reflects, with reversed orientation, to the link based at (-t-1,x); its spatial parity is unchanged. More generally, if an original measure is reflection positive and a retained coordinate set is reflection stable, its marginal is reflection positive on the inherited positive-time algebra. Proof: lift each retained observable to the original configuration space; its reflection form is the same integral before and after marginalization. This is a conditional preservation theorem, not a new proof of all Wilson reconstruction hypotheses, and does not establish locality of a new transfer Hamiltonian or the continuum limit.

A second decimation does NOT generally have the original linear-in-one-link Wilson form: the logarithms in (7) contain products of loop invariants. Iteration requires control of these generated interactions.

## 5. A Ward cancellation which an averaged Hessian misses

For any differentiable finite integral with action S(U,t), define Gamma(t)=-log integral exp[-S(U,t)]dU. Then exactly

    Gamma''(t)=E_t[S''(U,t)]-Var_t[S'(U,t)].             (8)

The negative covariance is load-bearing. It is not a small remainder merely because the integral is concentrated.

Take all m staples along the same path V_r(t)=exp(i t sigma_3). With z=m beta and U=u0 I+i u.sigma,

    S(U,t)=-z[u0 cos t+u3 sin t],
    S'(U,0)=-z u3, S''(U,0)=z u0.

Haar invariance shows Gamma is constant on this common endpoint-gauge path. Directly, in the density proportional to exp(z u0),

    E_z u0=r(z), E_z u3=0, E_z u3^2=r(z)/z.            (9)

To prove the last identity without relying on a Bessel simplifier: condition on u0. The three remaining coordinates are uniform on a sphere of radius sqrt(1-u0^2), so E[u3^2|u0]=(1-u0^2)/3. Integration by parts of

    d/du0[(1-u0^2)^(3/2) exp(z u0)]

has vanishing endpoint contribution and gives z E(1-u0^2)=3 E u0. At z=0 use the continuous limit r(z)/z=1/4.

Consequently

    E S''=z r(z), Var S'=z^2[r(z)/z]=z r(z),
    Gamma''=0.                                        (10)

For large z, both terms are of order z. Keeping only the positive averaged curvature would invent a mass-like quadratic cost in a pure gauge direction. This is an exact counterexample to that averaging procedure, not a proof that gauge-invariant glueball masses cannot arise. Such physical masses are not bare link-coordinate gauge masses.

### All retained staple directions

Let V_r(t)=exp(i t X_r.sigma), X_r in R^3, and keep m,beta finite. Put A2=sum_(r<s)|X_r-X_s|^2. Applying (8)-(9) at t=0 gives

    Gamma''(0)=beta r(m beta)[sum_r |X_r|^2-|sum_r X_r|^2/m]
              =[beta r(m beta)/m] A2.                 (11)

In staple-label space the Hessian is beta r(m beta)(I-11*/m), separately for each of the three color coordinates. It has three common-gauge zero directions and 3(m-1) positive relative directions for beta>0, m>=2. For m=6 its rank is 15, not 18. The code verifies the normalized projector algebra; it does not infer a Hamiltonian spectrum from this Hessian.

## 6. Keep the lowest noncommutative terms and expose the error scale

For two vectors X,Y, writing a=|X|^2, b=|Y|^2, c=X.Y gives exactly

    (1/2)Tr[exp(i t X.sigma)exp(-i t Y.sigma)]
      =cos(t sqrt(a))cos(t sqrt(b))
       + c sin(t sqrt(a))sin(t sqrt(b))/sqrt(ab),

with the continuous extensions when a or b vanishes. Taylor expansion is

    delta_XY(t)=t^2|X-Y|^2/2
        -t^4[|X-Y|^4/24+|X cross Y|^2/6]+O(t^6).       (12)

The cross-product term measures noncommutativity: [iX.sigma,iY.sigma]=-2i(X cross Y).sigma. It is missed by replacing the product of exponentials by exp(i t(X-Y).sigma). For orthogonal unit vectors the exact relative trace is cos(t)^2 and the deficit is t^2-t^4/3+O(t^6), not t^2-t^4/6.

Let

    A4=sum_(r<s)[|X_r-X_s|^4/12+|X_r cross X_s|^2/3].

Then s(t)^2=m^2-t^2 A2+t^4 A4+O(t^6). Substituting into the EXACT integral (5) yields

    Gamma(t)= [beta r/(2m)] A2 t^2
       + {-[beta r/(2m)] A4
           + beta[r-m beta r'] A2^2/(8m^3)} t^4
       + O_(beta,m,X)(t^6),                             (13)

where r and r' are evaluated at m beta. This last O(t^6) is at fixed parameters; no uniform weak-coupling or volume claim is attached to it.

A nonasymptotic QUADRATIC-remainder bound is also available. Put epsilon=|t|max_r |X_r| and

    C_m=(m-1)/3+2(m-1)^2/m.

Then

    |Gamma(t)-[beta r(m beta)/(2m)] A2 t^2|
       <= [beta C_m+2 beta^2(m-1)^2] epsilon^4.          (14)

Derivation: the fourth derivative of each relative trace is at most (|X_r|+|X_s|)^4 in absolute value, using unitary matrix products and the normalized trace norm. It is an even function of t. Thus |2sum delta_rs-t^2 A2|<=(2/3)m(m-1)epsilon^4 and 0<=D:=2sum delta_rs<=2m(m-1)epsilon^2. The identity

    (m-s)-D/(2m)=D^2/[2m(m+s)^2]

then gives |m-s-t^2 A2/(2m)|<=C_m epsilon^4 and m-s<=2(m-1)epsilon^2. Finally Taylor-expand F only to first order between beta s and beta m and use F''=Var(u0)<=1. This proves (14) without needing to approximate the group integral.

For many eliminated stars these absolute remainders ADD. With a common epsilon the bound is proportional to |E_dec|(beta+beta^2)epsilon^4 for fixed d. It is therefore not a volume-uniform small relative transfer error. The exact expression (7) avoids a Taylor remainder but still requires a controlled interacting analysis.

## 7. Wilson-coupling closure fails, even after exact integration

For just two adjacent plaquettes, m=2, let delta=1-(1/2)ReTr(V_1 V_2*). Then 0<=delta<=2 and

    Gamma_beta(delta)=F(2beta)-F(beta sqrt(4-2delta)).     (15)

The exact small-argument expansion of F is

    F(z)=z^2/8-z^4/384+z^6/9216-z^8/184320+... .

At the frustrated endpoint delta=2 the power series is in u=4-2delta. Terms u^k with k>=3 have zero second derivative at u=0. Hence, for EVERY fixed beta>0,

    Gamma_beta''(2)=beta^4/48>0.                         (16)

Thus the marginal is not exactly another Wilson action beta_eff delta+constant for ANY positive beta. This is not just a finite-order claim in small beta.

Near alignment the tangent coefficient is

    beta_eff,tangent=Gamma_beta'(0)=(beta/2)r(2beta).

DLMF large-positive-argument asymptotics give r(z)=1-3/(2z)+O(z^-2), so this coefficient is beta/2-3/8+O(beta^-1) as beta tends to infinity. At small beta it is beta^2/4+O(beta^4). Matching this one derivative discards (16) and all higher loop couplings; it is not an exact renormalization trajectory or a mass-gap estimate.

## 8. Arbitrary boundaries need not support a Gaussian saddle

For m even choose half the staples I and half -I. These are realizable by actual neighboring link values: each elementary three-edge detour has a distinct middle edge parallel to e. Set those middle links to the prescribed signs, all transverse legs to I, and all other unspecified boundary links to I. Their sum H is zero.

Then the conditional law of U_e is EXACTLY Haar for every beta. In particular, the probability outside the class-angle pi/2 ball around any fixed group element is 1/2. Large beta alone cannot imply a uniformly narrow conditional distribution around a boundary-dependent minimizer.

This is not only a measure-zero conditional issue. Neighborhoods with beta s<=1 have conditional density at least exp(-2) relative to Haar, so their outside-hemisphere probability is at least exp(-2)/2. Such neighborhoods are attainable and open for each finite beta. Their weight in the full interacting measure is NOT bounded here; frustration can be suppressed globally even though a worst-boundary conditional bound is false.

For comparison, when z=beta s>=1, (1) and elementary sine bounds imply

    c z^(-3/2) <= exp(-z)Z(z) <= C z^(-3/2),
    c=8 exp(-1/2)/(3 pi^3), C=pi^(5/2)/2^(5/2).          (17)

For the lower bound integrate 0<=theta<=z^-1/2 and use sin theta>=2theta/pi, 1-cos theta<=theta^2/2. For the upper bound use sin theta<=theta and 1-cos theta>=2theta^2/pi^2, then extend the Gaussian integral to infinity. Thus the saddle logarithm F(z)=z-(3/2)log z+O(1) is controlled when beta s is large, not uniformly as s approaches zero. The exact integral is regular at zero, where F(z)=z^2/8+O(z^4).

## 9. Source verification and provenance

- NIST DLMF 10.32.2, 10.29, and 10.40, checked 2026-09-15: normalized Bessel integral, derivative relations, and asymptotics for fixed order on the positive real axis. The notation dictionary is z=beta s and nu=1; the asymptotic formula is not applied at s=0. Sources: https://dlmf.nist.gov/10.32 ; https://dlmf.nist.gov/10.29 ; https://dlmf.nist.gov/10.40 . These special-function inputs are known after normalization translation. Equations (2), (8)-(14), and (16) also have the displayed direct proofs.
- Martin Luescher and Peter Weisz, *Background field technique and renormalization in lattice gauge theory*, hep-lat/9504006, April 11, 1995 version (26-page author PDF): Section 2.2, printed p.3 explicitly treats the generating functional as a formal perturbation series; Section 3.2, equations (3.8)-(3.12), printed pp.6-7, gives background gauge invariance; Section 6.2, equations (6.13)-(6.16), printed p.17, gives lattice shift transformations. Parsed p.3 and rendered pp.6,7,17 were inspected. The p.3 screenshot failed twice, so its scope statement was checked in extracted text. Source https://arxiv.org/pdf/hep-lat/9504006 . This is contextual overlap and a warning to preserve all fluctuation terms, NOT an imported nonperturbative RG/mass-gap theorem, and its background effective action is not identified with our partial link marginal.
- Kennedy-Pendleton (1985), DOI 10.1016/0370-2693(85)91632-6, and Creutz (1980), DOI 10.1103/PhysRevD.21.2308, were found as historical SU(2) heatbath references. Only publisher abstracts were read; they are discovery/attribution leads, not proof dependencies.
- CMI's current Yang-Mills page was checked 2026-09-15 and still labels the problem unsolved: https://www.claymath.org/millennium/yang-mills-the-maths-gap/ . No submission or prize claim was made.

No broad novelty search is claimed. Consensus was not reinvoked merely to repeat its documented quota error; primary sources were used. Mathbox provided workflow instructions, not an independent expert verdict. No external computation beyond existing tool allowances was purchased.

The checker `checks/U029_exact_link_integration_checks.py` uses Python 3.13.5, SymPy 1.14.0 and rational arithmetic, plus separately marked mpmath 1.3.0 quadrature. Eleven focused tests passed, including the actual noncofacial elimination geometry for periodic (d,n)=(3,4),(4,4),(4,6), reflection stability of that selection, exact noncommuting matrix examples, all-parameter symbolic Hessian and quartic identities, finite Haar-moment controls, and deliberate invalid-input/false-closure controls. The universal geometry and algebra are proved above, not inferred by extrapolating these cases.

For z in {0,1/2,2,6,24,96}, the output encloses r(z) using exact positive-series sums and a decreasing geometric tail. If a_k=(z^2/4)^k/[k!(k+nu)!], the tail after M is at most a_(M+1)/(1-q), q=(z^2/4)/[(M+2)(M+nu+2)]<1. Apply this separately for nu=1,2 and divide positive intervals; r(z)=(z/2)S_2/S_1. The emitted decimal endpoints are rounded OUTWARD from exact rationals. These certificates check scalar integral coefficients, not any spectral gap.

Four independent 60-digit Haar quadratures at z=1,6,24,96 corroborated the Ward cancellation; they are not interval certificates. Wolfram 15.0.1 separately returned the Bessel derivative residual zero, quartic residual zero, six Ward-coefficient residuals zero, and normalized six-staple Hessian eigenvalues {1,1,1,1,1,0}. Its submitted formulas do not constitute an independent derivation of the entire theorem. The prior U028 suite was rerun separately. Compilation and indentation checks passed. Static ruff/mypy/pyright and Lean are not installed, so no static-analysis or formal-verification success is claimed.

## 10. Self-audit and next dependency

Primary verdict: **proved after the explicit finite-lattice, one-layer coordinate-marginal restriction**.

Passed: exact integration including H=0; endpoint gauge covariance; positive action comparison for all boundary links; extensive first-layer factorization without independent-plaquette assumptions; exact covariance cancellation; noncommutative quartic term; explicit quadratic remainder with volume dependence; no-Wilson-closure proof; realizable failure of worst-boundary saddle concentration; conditional reflection-positivity preservation.

Unproved: identifying a gauge-covariant low/high momentum decomposition with this coordinate marginal; integrating further layers with uniform connected-interaction estimates; suppressing frustrated boundary stars in the true measure; a centered physical-time transfer comparison for the retained observables; the joint ultraviolet/infinite-volume limit; nontrivial finite physical mass; groups beyond SU(2).

The next executable question is no longer whether an averaged quadratic term appears. It is whether the EXACT generated-loop action (7), including covariance effects and bad staple regions, admits a controlled second elimination and a centered transfer-form comparison. Start with two neighboring elimination stars whose generated six-link loops overlap; compute the connected conditional response rather than discarding it or replacing (15) by its tangent Wilson coupling. Preserve the physical Hilbert-space/true-vacuum requirement throughout.

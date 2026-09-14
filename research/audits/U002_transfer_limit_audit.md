# U002 — transfer-limit audit and physical-time gap bridge

Date: 2026-09-14.

**We have not solved the Yang–Mills problem yet.**

This is partial research and self-review, not a complete candidate, formal proof or independent expert verification. The target remains the full Jaffe–Witten assertion for every compact simple gauge group, including existence, nontriviality, correct Yang–Mills identification, and a finite positive physical mass gap.

## Preserved state and normalization correction

Before writing, the existing README and `research/checkpoints/checkpoint-2026-09-14.md` were read at tree `01259e056583192e4c062abaafc5f84800ef9dec`. They are preserved untouched. The prior checkpoint already contains the curvature direction `1 - 32 beta`; this run re-derived and checked it rather than treating it as a distinct discovery.

The earlier checkpoint uses beta both for the Shen–Zhu–Zhu exponent coefficient and for the usual SU(2) Wilson inverse coupling. Distinguish them: if the exponent coefficients are `2 beta_S` and `beta_W/2`, respectively, then `beta_W = 4 beta_S`. Therefore the convention `beta_W = 4/g0^2` gives `beta_S = 1/g0^2`, not `4/g0^2`. The curvature threshold is in beta_S units. This does not change the divergence of the inverse coupling along that proposed continuum trajectory. Other prior-checkpoint claims remain preserved leads, not automatically verified dependencies.

## 1. A local inference in a 2026 claimed construction fails

Source: Mir Faizal and Arshid Shabir, arXiv:2606.19362v1, combined PDF, printed pp.128–129, Theorem11.1. Equation11.3 supplies a lower operator bound but equation11.5 uses an upper quadratic-form bound. The signs were checked in rendered pages, not only extracted text. AppendixD.2, printed pp.193–194, uses a stronger additive norm-controlled comparison; that conditional triangle-inequality argument can supply an upper bound. The failure below concerns the inference as stated, not every argument in the 593-page manuscript.

Let

    T = [[3/4, 1/4], [1/4, 3/4]],
    S = [[7/8, 1/8], [1/8, 7/8]].

Both are symmetric Markov matrices and positive self-adjoint contractions. Their common normalized vacuum is Omega=(1,1)/sqrt(2), and v=(1,-1)/sqrt(2) is an orthogonal unit vector. The eigenvalues seen by v are 1/2 and 3/4. Also

    S-T = (1/8) [[1,-1],[-1,1]] >= 0.

Thus S>=T with zero negative remainder does not imply <v,Sv> <= <v,Tv>. The transfer gap decreases from 1/2 to 1/4. At physical time step one the Hamiltonian gap decreases from log(2) to log(4/3). No floating-point approximation is involved.

## 2. Summability does not supply a positive margin

Write P(lambda) for the preceding symmetric Markov family, with eigenvalues 1 and lambda. Put

    lambda_k = 1 - 2^(-k-1),
    T_k = P(lambda_k),
    E_k = T_(k+1)-T_k = 2^(-k-2) |v><v|.

Then E_k>=0, E_k Omega=0, and sum ||E_k|| = 1/2, but the transfer gap tends to zero. The finite error sum exhausts the initial margin. This example's limiting identity operator has a degenerate vacuum; it is not described as a Yang–Mills counterexample.

For contrast, errors 2^(-k-3) total 1/4. Starting at lambda_0=1/2 leaves an upper norm at most 3/4, hence a fixed-time Hamiltonian gap at least log(4/3). A strict budget, not just a finite sum, is needed.

## 3. An infinite-dimensional counterexample with a unique limiting vacuum

On ell^2({0,1,2,...}), define

    H_inf e_0 = 0;  H_inf e_n = (1/n)e_n for n>=1,
    H_k e_0 = 0;    H_k e_n = max(1/n, 2^-k)e_n.

Fix any eta>0 and let a_k=eta*2^-k and T_k=exp(-a_k H_k). Each H_k is bounded, nonnegative and self-adjoint, with unique vacuum e_0 and positive gap exactly 2^-k. Moreover ||H_k-H_inf|| <= 2^-k.

All these operators commute. Since a_(k+1)H_(k+1)<=a_k H_k, their exponential eigenvalues give

    E_k := T_(k+1)-T_k >= 0,
    E_k e_0 = 0,
    ||E_k|| <= ||a_k H_k-a_(k+1) H_(k+1)|| <= a_k.

The first norm bound uses the scalar 1-Lipschitz property of exp(-u) for u>=0 on this common diagonal basis. Thus sum ||E_k|| <= 2 eta, arbitrarily small in absolute units.

For t>=0 and n_k=floor(t/a_k), the same scalar estimate gives

    ||T_k^n_k-exp(-t H_inf)||
      <= t ||H_k-H_inf|| + |n_k a_k-t| ||H_k||
      <= t*2^-k+a_k -> 0.

The limiting H_inf nevertheless has unique vacuum and positive eigenvalues 1/n accumulating at zero. Hence it has no positive spectral gap. Positivity, common vacuum, summable positive additive defects and convergence at every fixed physical time do not by themselves prove gap persistence. This is an abstract operator example, not a Yang–Mills theory or a counterexample to its existential target.

## 4. Physical units cannot be dropped

For T_k=exp(-a_k H_k), if m_k is the positive Hamiltonian spectral edge, the dimensionless transfer gap is

    g_k = 1-exp(-a_k m_k).

A finite positive physical mass requires g_k of order a_k, not a fixed positive transfer gap as a_k tends to zero. Further, c_k=exp(a_k m_k)/a_(k+1) >= 1/a_(k+1) when m_k>=0. Such coefficients cannot stay bounded along a shrinking time step; weighted error summability must be demonstrated separately. Even finite weighted sums must be strictly smaller than the starting physical margin.

An exact time blocking from a to b*a compares with T^b. It cannot automatically compare with T while treating both as the same physical time.

## 5. Conditional physical-time bridge

Assume an actual OS reconstruction supplies H>=0 self-adjoint on a Hilbert space, a normalized vacuum Omega, and a strongly continuous semigroup exp(-tH). Let F label a vector space of observable combinations and let v(F) have dense linear range in Omega-perp.

For regulated positive contractions T_j with a_j -> 0 and centered vectors v_j(F), fix t0>0 and integers n_j a_j -> t0. Require for every F:

    ||v_j(F)||^2 -> ||v(F)||^2,
    <v_j(F),T_j^n_j v_j(F)> -> <v(F),exp(-t0 H)v(F)>.

Suppose uniformly over the relevant regulators and volumes, for every F,

    <v_j(F),T_j^n_j v_j(F)> <= q ||v_j(F)||^2,
    0<q<1.

Passing to the limit and using density gives

    0 <= exp(-t0 H)|Omega-perp <= q I.

The spectral theorem then gives a gap at least -log(q)/t0: a nonzero spectral vector below that energy would violate the operator inequality.

To guarantee finite, nonzero excited spectral content, it is enough to find one label F and constants B<infinity and b>0 with

    limsup ||v_j(F)||^2 <= B,
    liminf <v_j(F),T_j^n_j v_j(F)> >= b.

The limiting spectral measure then implies

    0 < -log(q)/t0 <= m <= log(B/b)/t0 < infinity.

This prevents a vacuum-only limit or all excitations escaping to infinite energy. If q=0, injectivity of exp(-t0 H) forces Omega-perp to be zero, so that variant fails nontriviality.

Existence of the full Schwinger family, sufficient OS regularity, density, the uniform physical-time contraction and this positive-time witness are unproved for the target theory. A lemma assuming them is not a construction. A finite list of tested observables can miss an orthogonal sector with energies 1/n.

## 6. Independent re-derivation of the lattice obstruction

Use S=2 beta_S sum_p Re Tr(U_p) and the Hilbert-Schmidt Lie algebra metric. On a periodic d-dimensional torus with even L>=4 set

    z_mu(x)=(-1)^(sum_(nu<mu) x_nu),
    U_mu(x)=z_mu(x) I_2,
    s(x)=(-1)^(sum_mu x_mu),
    A_mu(x)=s(x)c_mu,  sum_mu c_mu=0, c nonzero,
    X=diag(i,-i)/sqrt(2).

Every plaquette of U is -I_2. Along U_mu(t,x)=exp(t A_mu(x) X)U_mu(x), commutativity gives

    U_(mu,nu)(t,x)=-exp(t D_(mu,nu)(x) X),
    D_(mu,nu)(x)=2 s(x)(c_mu-c_nu).

Since the trace is -2 cos(tD/sqrt(2)), its second derivative is D^2. Using

    sum_(mu<nu)(c_mu-c_nu)^2
      = d sum_mu c_mu^2 - (sum_mu c_mu)^2,

one obtains ||dA||^2=4d||A||^2 and Hess(S)[A,A]=8d beta_S ||A||^2. SU(2) Ricci is one in this normalization: the orthonormal Pauli basis has commutator squared norms 2,2,0 with X, and Ricci equals their sum divided by four. Consequently the curvature ratio is 1-8d beta_S, or 1-32 beta_S in d=4.

No globally strictly positive product-metric Bakry–Emery lower bound exists for beta_S>=1/32. This is not claimed to be the exact global minimum. It leaves the SZZ sufficient strong-coupling interval |beta_S|<1/48 intact. The chosen direction has zero discrete divergence but nonzero curl; this does not compute curvature on the gauge quotient or exclude averaged inequalities. Langevin time is not physical time.

Exact finite audits with c=(1,-1,0,0):

    L=4: links1024, plaquettes1536 all negative,
         norm^2=512, curl^2=8192, divergence^2=0.
    L=6: links5184, plaquettes7776 all negative,
         norm^2=2592, curl^2=41472, divergence^2=0.

The all-L statement follows from the displayed algebra, not finite enumeration. No novelty claim is made.

## 7. Checks and limitations

The focused checker is `checks/U002_exact_checks.py`:

    python -m compileall -q checks/U002_exact_checks.py
    python checks/U002_exact_checks.py

The same code ran locally under Python3.13.5 using only integers and fractions.Fraction: 10 tests passed. Controls include incorrect matrix order, exhausted versus strict error budgets, odd/degenerate torus sizes, zero direction, longitudinal modes, dimensions2 and3, and the infinite-model generator inequalities for k=0,...,9 and n=1,...,257. The last finite grid does not prove the infinite-dimensional limit; the proof above does.

Wolfram15.0.1 also returned exact eigenvalues {1/4,0} for S-T, Rayleigh values {1/2,3/4}, unit SU(2) generator norm1, Ricci1, plaquette second derivative q^2, and zero residual for the four-amplitude identity. A field displaying 1-32 beta was merely an input formula; it is not counted as an independent curvature derivation. Later Wolfram limit/sum calls returned expected expressions with a Power::infy warning. Those outputs are not certificates; written product-rule, logarithm and geometric-series arguments are used instead. No external linter/typechecker or Lean runtime was available; no such successful build is claimed. No independent expert review was performed.

## 8. Next mathematical action

Pursue a uniform upper quadratic-form contraction at one fixed physical time on the full centered OS algebra of renormalized gauge-invariant observables, along one specified Wilson scaling trajectory and infinite-volume limit. Require a simultaneous nonzero positive-time witness. A lower operator bound, a fixed-spacing result, or an auxiliary Langevin gap cannot substitute for that estimate. The initial state construction and these estimates remain open obligations.

## Sources and review scope

- Clay current status: https://www.claymath.org/millennium/yang-mills-the-maths-gap/ — checked2026-09-14; still listed unsolved.
- Jaffe–Witten, official description, Sections3–4: https://www.claymath.org/wp-content/uploads/2022/06/yangmills.pdf
- Clay rules, Sections2,4,5(c),5(e),6–7: https://www.claymath.org/wp-content/uploads/2022/03/millennium_prize_rules_0.pdf — $1million, qualifying publication, two years, community acceptance, no direct submission, discretionary counterexample treatment; no award inferred.
- Shen, Zhu, Zhu, arXiv:2204.12737v1: https://arxiv.org/abs/2204.12737 — equations1.1–1.3,2.3, Lemma4.1 and Theorem4.2 checked; fixed-spacing strong-coupling input only.
- Faizal, Shabir, arXiv:2606.19362v1: https://arxiv.org/abs/2606.19362 — Theorem11.1 and AppendixD.2 inspected; not a complete audit of the combined593pages and not imported as a verified solution.
- Mondal, arXiv:2301.06996v7: https://arxiv.org/abs/2301.06996v7 — abstract explicitly assumes quantization and conditional regularized curvature; Hamiltonian-route lead only.

All new work is confined to this Yang–Mills project. No other project's mathematics is used. No public posting, researcher contact, prize submission, paid job or asynchronous process was initiated.
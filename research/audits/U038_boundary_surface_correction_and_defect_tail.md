# U038 — boundary surface repair, corrected U009 verdict, and conditional dense-defect tails

Date: 2026-09-15. Base: private `Joe-Simo/yang-mills-mass-gap` commit `2b75c79208a48eb8f4cd2770b1b279afc586fdbc` (U037).

**We have not solved the Yang–Mills problem yet.**

Evidence: self-reviewed elementary finite-lattice proofs, a correction to an older claimed obstruction, and exact finite checks. No formal verification, independent expert review, novelty claim, physical gap improvement, or continuum construction.

## 1. Route decision and correction record

U037's remaining target is control of strongly coupled interfaces without deleting physical boundary representations. Its worst-case interface estimate is a surface-sized action cost, which is too large to regard as a small perturbation. This unit tests a different use of that cost: pay it explicitly when bounding an event whose minimum internal action is volume-sized. This works for a positive density of large plaquette defects, but it does NOT control all fluctuations within the complementary event.

The relevant earlier record is U009, `research/audits/U009_boundary_excess_counterexample.md`, Git blob `4bb4365a829726e13b33377bb5d291f8921eda5e`, read at the pinned base. Its asserted asymptotic boundary obstruction is WITHDRAWN. It did not exhibit a global constrained SU(2) minimizer with volume-density curvature. Its constant-flux Jensen argument also silently constrained real lifted flux, although compact link boundary data do not impose that lift. In the ordinary compact Wilson configuration space, one can keep the prescribed boundary links and set all other links to identity. Only a collar can then have nonzero plaquette action. Sections 2–3 prove the correct surface bound and give exact checks against the proposed flux argument.

U008, `research/audits/U008_positive_density_action_entropy.md`, blob `0741088236012afdb97120899d1e1a4354abe435`, also used incorrect EXACT open-box counts. The correct four-dimensional numbers for n cells per side are `6 n^2(n+1)^2` plaquettes and `4 n(n+1)^3` links, not `6 n^4` and `4(n+1)n^3`. Their leading orders and limiting ratio agree, but boundary estimates need the exact counts.

The older files remain unchanged as historical evidence. This correction supersedes U009's route rejection and U008's exact counting statements, not every auxiliary result in U010–U025. Any downstream assertion using that rejection as a mathematical fact must be re-audited. The present proof does not rely on the scalar-projection chain; U026–U037's separately stated restrictions are not removed by this correction.

Workspace: `/mnt/data/yang-mills-mass-gap`. The supplied U037 archive restored 132 missing files; two present files matched; none conflicted or was overwritten. All ten U037 manifest hashes matched before work. The remote branch was read at the base above. The standalone project prompt was recovered through current-conversation file search; the original all-group existence-and-gap target, project isolation, private-write permission, and zero-spend boundary are unchanged. No sibling folder was accessed. No new Mathbox runtime or independent review is claimed; the previously supplied audit workflow was applied directly.

## 2. Geometry and the conditional measure — no independence assumption

Work first in a finite d-dimensional Euclidean hypercubic Wilson lattice, d>=2, with ordinary SU(2) link integration and a common inverse coupling beta>=0. A box and its one-cell neighborhood are assumed to embed without periodic identification. Define

    Lambda_n = {0,...,n}^d,  n>=1,
    E_n = links with both endpoints in Lambda_n,
    P_n = plaquettes with all four boundary links in E_n,
    C_n = plaquettes meeting E_n but not in P_n.

Each unoriented cell is counted once using positive coordinate orientations. Let L=|E_n|, M=|P_n|, B=|C_n|. Direct counting gives

    L = d n(n+1)^(d-1),
    M = binom(d,2) n^2(n+1)^(d-2),
    B = 4 binom(d,2) n(n+1)^(d-2),
    B/M = 4/n.                                             (1)

For a fixed coordinate plane, an internal face has n choices in both active directions and n+1 in the others. A crossing face lies beyond either of the two ends of one of its active coordinates; this gives four sides, n choices in the tangential active coordinate, and n+1 in the other d-2 directions. Each such crossing face contains exactly one E_n link. Faces beyond two sides contain no E_n link and are not counted. This proves (1) for every n and d in scope; finite enumeration only checks it.

Put

    a_p(U)=1-Re Tr(U_p)/2,          0<=a_p<=2,
    A_n(U)=sum_(p in P_n) a_p(U).

Fix EVERY exterior link U_(E_n complement)=eta, with no smoothness, small-field, or weak-interface hypothesis. Constants depending only on eta cancel. The conditional law of U_E is exactly

    d mu_beta^eta(U_E) = Z_eta^(-1)
        exp[-beta {A_n(U_E)+sum_(p in C_n) a_p(U_E,eta)}]
        product_(e in E_n) dHaar(U_e).                     (2)

These are the original interacting link variables. No plaquette variables are independently sampled; all group products and lattice identities remain intact. No regional singlet sector is selected. The result is a Euclidean conditional-probability statement, not the conditional law of a spatial quantum wavefunction.

## 3. Surface cost above arbitrary compact boundary data

Set every link in E_n to I, keeping eta fixed. Then every internal plaquette is I, and every crossing plaquette has deficit at most two. Hence

    inf_(U_E) {A_n+sum_C a_p} <= 2B.                        (3)

If A_n>=alpha M, with 0<alpha<=2, the same total affected action is at least alpha M because all crossing terms are nonnegative. Consequently

    inf_(A_n>=alpha M) A_affected - inf A_affected
         >= alpha M-2B = M(alpha-8/n).                    (4)

For n>=16/alpha, this is at least alpha M/2. The constants are uniform in eta. This is precisely a volume-sized excess action once the box is sufficiently large for a FIXED positive density/angle threshold.

For the alternative convention used in U009, all links ON the outer boundary of the open box are fixed. Leave those untouched and set every non-boundary link to I. The inner vertex cube `{1,...,n-1}^d` (n-2 cells per side) then has flat plaquettes. Writing M_d(n)=binom(d,2)n^2(n+1)^(d-2), for n>=3,

    min A_open <= 2[M_d(n)-M_d(n-2)] = O(n^(d-1)).           (5)

Therefore an event with action at least alpha M_d(n-2) has excess at least that quantity minus the right-hand side of (5), which is positive and volume-order for all sufficiently large n. The same conclusion holds if the density is measured on all plaquettes. No assertion that the TRUE minimizer is flat is needed; (5) is only an admissible trial upper bound on its action.

In four dimensions,

    M_4(n)-M_4(n-2)=48n^3-72n^2+72n-24.                    (6)

This is not an assumption of dynamical screening or a quantum mass gap. It is a variational construction allowed by the bounded compact-group Wilson energy. It could be excluded by an additional hard admissibility condition, a fixed real-flux lift, or a restricted chart, but those are not the unrestricted Wilson model being tested.

### Exact failure of U009's lifted-flux minimization step

On a two-dimensional n-by-n square choose an integer q>=5, take n a multiple of q, and set

    U_1(x)=I,  U_2(x)=exp[2 pi i x_1 sigma_3/q].

Every plaquette has class angle 2pi/q<pi/2, yet all outer boundary links are I. The completely identity configuration has the SAME compact boundary values and action zero, whereas the constant-flux action is n^2[1-cos(2pi/q)]>0. Thus convexity on a chosen branch does not justify minimizing over the full compact domain with a fixed lifted total flux.

At q=n=6 these actions are exactly 18 and 0. This is a continuous-SU(2) configuration, not a replacement of SU(2) by a finite group.

The original four-dimensional conclusion is separately contradicted at the level of the proposed family by (5): fixed-angle curvature in the (1,2) plane costs `[1-cos(phi)] n^2(n+1)^2`, while the identity-interior competitor costs at most the surface bound (6) times two. For every fixed phi>0 the latter eventually wins. At phi=pi/3 and n=256 the two values are respectively

    2,164,293,632   and   at most 1,601,212,368.

This comparison preserves every fixed boundary link. It does not assert either trial configuration is the minimizer; the strict inequality is enough to exclude the constant-flux minimizer claim at that size.

## 4. Conditional probability: pay the Haar entropy as well

For 0<delta<=pi/4, let C_delta be the class-angle ball about identity. Its normalized Haar volume is

    v(delta)=(2/pi) integral_0^delta sin^2(t) dt
            =[delta-sin(2delta)/2]/pi >0.                 (7)

When every free link belongs to C_delta, the bi-invariant metric triangle inequality bounds each internal plaquette angle by 4delta. Thus

    A_n <= M[1-cos(4delta)] <= 8M delta^2,
    A_affected <= 8M delta^2+2B.

This gives a lower bound on the actual conditional denominator, for EVERY exterior configuration:

    Z_eta >= v(delta)^L exp[-beta(8M delta^2+2B)].           (8)

On A_n>=alpha M the numerator is at most exp(-beta alpha M), since Haar volume is at most one. Combining yields the exact usable estimate

    mu_beta^eta(A_n>=alpha M)
      <= min{1, exp[-beta{M(alpha-8delta^2)-2B}
                       + L log(1/v(delta))]}.             (9)

No approximation of eta, gauge fixing, independence, saddle expansion, or reference-vacuum substitution enters this proof. The positive Haar neighborhood repairs the zero-volume defect of using the identity point alone in a partition function bound.

A concrete sufficient parameter choice is

    delta=alpha/8,           n>=ceil(32/alpha),
    beta >= 4L log(1/v(delta))/(alpha M).                  (10)

Because 8delta^2=alpha^2/8<=alpha/4 and 2B/M=8/n<=alpha/4, the braces in (9) are at least alpha M/2. The entropy in (10) costs at most beta alpha M/4. Therefore

    SUP_eta mu_beta^eta(A_n>=alpha M)
          <= exp[-beta alpha M/4].                       (11)

In d=4, L/M=(2/3)(1+1/n)<=1 for n>=2. Thus the simpler beta threshold `4 log(1/v(delta))/alpha`, independent of both n and the external volume, suffices throughout (10). Large beta means weak bare coupling in the ordinary Wilson convention. The threshold is conservative; none of the displayed numbers is a measured probability.

If at least rho M plaquettes have theta_p>=epsilon, put alpha=rho[1-cos(epsilon)]. This positive-density event implies A_n>=alpha M and therefore satisfies (9)–(11). Fixed rho and epsilon are essential to the fixed constants. No result about every individual plaquette being small is inferred.

If only the outer boundary-surface links are prescribed, condition additionally on the intervening collar and apply (9) to the inner subbox, then remove that extra conditioning by the tower property. Thus the fixed-boundary convention of U009 also admits the bound for its core event, with the core's own side/counts; it is not silently identified with E_n above.

For exact finite parameter certificates, sin(t)>=2t/pi on [0,pi/2] gives

    v(delta)>=8delta^3/(3pi^3)>8delta^3/[3(22/7)^3].         (12)

For rational alpha, delta=alpha/8 and the last bound are rational. Choose integer h with 2^(-h) no greater than that rational bound. Then log(1/v)<=h log 2<h. Taking integer beta>=ceil[4Lh/(alpha M)] certifies (11) using only rational comparisons. The checker records four such conservative parameter sets and symbolic negative logarithms of their probability bounds; it does not enumerate their huge configurations.

## 5. Execute the next step: correlated joint events and connected clusters

Tile the vertex lattice by disjoint translates `(n+1)z+Lambda_n`, and let E_z be their internal edge sets. Distinct E_z are disjoint. Crossing plaquettes can still couple different boxes; NO factorization of their law is asserted.

Let Bad_z depend only on E_z and imply the event used in (11), and set p=exp(-beta alpha M/4). For any finite set S of distinct boxes,

    mu_beta(intersection_(z in S) Bad_z) <= p^|S|.          (13)

Proof: condition on all links outside one E_z. Every other Bad event is measurable there. Use the uniform conditional bound (11), remove this event, and repeat. This is the conditional-expectation tower property, not a claim of independence. It works under arbitrary exterior conditions on the enclosing finite lattice as well.

Declare two boxes adjacent when their labels are nearest neighbors in Z^d. The maximum degree is D=2d. A connected k-box set containing a specified root admits a deterministic spanning-tree depth-first walk of length 2(k-1). The walk visits exactly that set, so distinct sets yield distinct chosen walks. Hence there are at most D^(2(k-1)) such sets. If the root's bad cluster has at least k vertices, it contains one of those k-vertex rooted sets. Therefore

    Pr(|cluster_bad(root)|>=k) <= D^(2(k-1)) p^k
                              = p (D^2 p)^(k-1).          (14)

In d=4, D=8. When 64p<1, (14) gives exponential decay in the NUMBER OF BAD BLOCKS, uniformly in enclosing volume. This is a defect-cluster estimate, not temporal correlation decay for arbitrary physical observables and not a convergent full renormalization expansion.

## 6. A concrete link to U029's frustrated surroundings

An edge e has m=2(d-1) incident plaquettes. Their detours V_1,...,V_m share its endpoints; put s_e=|sum_r V_r| in quaternion norm. The exact action identity gives

    sum_(p contains e) a_p
       = m-Re Tr[U_e(sum_r V_r)*]/2 >= m-s_e.              (15)

Consider only edges whose ENTIRE plaquette star lies in P_n. There are

    L_star = d n(n-1)^(d-1)

such edges: their coordinates transverse to the edge direction must be strictly interior. Call a star frustrated when s_e<=(1-eta)m, with fixed 0<eta<=1. If at least f L_star stars are frustrated, sum (15) over them. Each plaquette is counted at most four times, so

    A_n >= m eta f L_star/4.                              (16)

In d=4 this is alpha_n M, with

    alpha_n = eta f (n-1)^3/[n(n+1)^2] -> eta f.            (17)

For fixed positive eta,f and sufficiently large n, (9)–(11) apply with alpha_n (or any fixed lower bound, for example eta f/2 once n is sufficiently large). These block events also depend only on E_n, so (13)–(14) apply. This establishes suppression of a POSITIVE DENSITY of highly frustrated stars in the ORIGINAL interacting Euclidean Wilson measure, including homogeneous strong interfaces.

It does not prove a sharp probability for one cancelling star, remove the adverse conditional example of U029, or control all sparse defective arrangements. Those distinctions prevent upgrading (17) into the still-missing full boundary-response estimate.

## 7. Scope relative to the true vacuum and the mass gap

The estimates above hold for every enclosing finite Euclidean lattice, not only for independent cells or a Gaussian reference. On a finite spatial graph, a gauge-invariant cylinder event deep inside a long open Euclidean time interval has a limit given by the usual finite Wilson transfer and its true Perron vacuum. Gauge fixing the temporal links for that identification changes no gauge-invariant event. Since (9), (13), and (14) hold BEFORE that gauge fixing and are uniform in the enclosing interval length, they pass to these bounded cylinder-event limits. This uses the finite-regulator transfer construction already specified in U031–U032; it is not a new continuum or arbitrary-state norm theorem.

This result improves a probability input, not U037's spectral inequality. In particular a rare-event estimate alone cannot bound the operator norm of multiplication by its indicator: for any event E of probability 0<p<1, that multiplication operator still has norm one on L2(mu). Even for the centered vector `f=1_E-p`,

    ||1_E f||^2 / ||f||^2 = 1-p,                         (18)

which tends to one as E becomes rare. Controlling the vacuum probability of a bad event is not the same as controlling all low-energy states or their relative transfer forms.

The complement of our dense-defect event may contain many long-wavelength collective states, sparse large plaquettes, nontrivial loop holonomies, and fields not lying in U028's global small-norm slice. The nonlinear small-field estimate of U028 therefore cannot simply be applied on this complement. Nor are boundary gauge representations removed: the probability proof integrated complete link variables.

A continuum scaling diagnostic can be made only conditionally: if beta(a)>=K log(1/a), K>0, and n,alpha are fixed satisfying (10) and `K alpha M/4>4`, a union bound over O(a^-4) such boxes in a fixed physical four-volume tends to zero. This algebraic diagnostic neither constructs that continuum trajectory nor proves a physical mass; no perturbative asymptotic-freedom formula is imported as a rigorous construction.

## 8. Source checks, computation, and self-audit

New proofs (1)–(18) use direct counting, the bounded Wilson energy, the SU(2) Haar integral, and elementary conditional probability; no external mass-gap, mixing, or cluster-expansion theorem is assumed. NIST DLMF 10.32.2, checked 2026-09-15, agrees with the class-angle normalization at nu=1 used in U029; (7) follows directly by integrating the Haar density. Locator: https://dlmf.nist.gov/10.32 . CMI's current page still labels the Yang–Mills problem unsolved: https://www.claymath.org/millennium/yang-mills-the-maths-gap/ . No publication, contact, spending, or prize claim was made.

A limited search using variants of lattice-gauge large-field/boundary estimates did not supply an exact new theorem to import. The finite-group weak-coupling paper arXiv:2202.10375 appeared as a discovery lead only: its finite-group scope is not a continuous-SU(2) comparison input. There is NO novelty claim. The elementary action-versus-entropy and rooted-cluster counting methods are not presented as newly discovered methods.

`checks/U038_boundary_surface_checks.py` uses exact Fraction/SymPy decisions. Ten focused tests pass: complete finite incidence enumeration for d=2,3,4 and n=1,2,3; full-star counts; corrected polynomial formulas; the continuous-SU(2) sixth-root boundary witness; the four-dimensional analytical competitor inequality; rational sufficient thresholds; exact local star algebra; a correlated binary tower-property fixture; rooted-set enumeration and the rare-event norm test; and invalid inputs. The binary and Q8 fixtures are algebra/probability controls, not Wilson samples. The universal configuration, volume, and cluster bounds are the written proofs above, not extrapolations from these finite cases.

An initial test compared expanded and factored equal symbolic rational functions structurally. Nine tests passed and one failed; the checker was repaired to compare the exact simplified difference to zero. The initial outputs and repair record are preserved. No formula, hypothesis, or test population was relaxed. All ten prior U037 tests were rerun into new U038 output files. Compilation and indentation checks passed; ruff/mypy/pyright/Lean were not available. Wolfram 15.0.1 corroborated the count ratios, collar polynomial, star ratio, Haar derivative, exact sixth-root identity, action 18, and positive four-dimensional margin 563081264 without warnings; submitted formula checks are not independent full-proof verification.

Primary self-audit verdict: **proved under the explicit compact finite-Wilson, positive-density and sufficiently-large-block/large-beta restrictions**. U009's contrary asymptotic route rejection is withdrawn; U008's exact open-box counts are corrected. All historical files remain preserved.

Not established: a mass gap, uniform connected boundary susceptibility on the low-energy physical subspace, a conversion of defect rarity into the needed energy-relative estimate, control of every sparse/topological sector, a continuum construction, or the all-group target.

## 9. Next executable obligation

Use the corrected dense-defect bound to split the actual boundary-response calculation WITHOUT dropping rare-state vectors or boundary representations. The first required new estimate is a relative transfer/Dirichlet-form bound on the defective contribution, plus control of collective motion on the complement. Test its proposed normalization against (18), U028's global-norm failure, and U037's boundary-charge example before attempting iteration. Rarity alone cannot discharge that obligation; a bounded-energy restriction must be justified in the same actual vacuum, not inserted as an assumption of the desired gap.

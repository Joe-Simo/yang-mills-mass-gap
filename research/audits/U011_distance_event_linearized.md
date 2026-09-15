# U011 — positive-density distance event in the linearized gauge-fixed model

Date: 2026-09-14.

**We have not solved the Yang–Mills problem yet.**

This unit follows the Mathbox research-attempt protocol for one bounded route. It tests whether a concrete positive-density event forces volume-order L2 distance from the minimizer/gauge/harmonic manifold in the linearized model, which is the missing input identified in U010.

## Target and route contract

Target statement (linearized model only): after fixing gauge and projecting away harmonic/background modes, suppose at least a fraction rho>0 of the retained fluctuation coordinates have absolute value at least epsilon>0. Does this force

    ||A||_2^2 >= c n^4

on a four-dimensional n-cell block, uniformly in n?

Success criterion: prove an explicit c(rho,epsilon)>0 independent of n.
Failure criterion: exhibit a projected fluctuation satisfying the positive-density event with norm squared o(n^4).

This is a finite-dimensional Euclidean statement about coordinates after projection. It is not yet a gauge-invariant nonlinear Yang–Mills event.

## 1. Coordinate-count lemma

Let M_n be the number of retained fluctuation coordinates. On a four-dimensional block, after removing only lower-dimensional gauge/harmonic subspaces, M_n is still of volume order:

    M_n >= c0 n^4

for some c0>0 for all sufficiently large n.

If at least rho M_n coordinates obey |A_j|>=epsilon, then trivially

    ||A||_2^2 = sum_j |A_j|^2
               >= rho M_n epsilon^2
               >= rho c0 epsilon^2 n^4.                 (D)

Thus the desired exponent is gamma=4 for this **coordinate-level event**.

No spectral estimate is needed for (D); it is simple counting. The substantive issue is whether the event is invariant/meaningful after the projection and whether the nonlinear gauge theory supplies an analogous condition.

## 2. Combining with U010 soft-mode coercivity

U010 gives the gauge-quotiented linearized Hodge estimate

    ||dA||_2^2 >= c_H n^-2 ||A||_2^2.

Combining with (D) yields

    ||dA||_2^2 >= c_H rho c0 epsilon^2 n^2.

Hence the quadratic Wilson action excess satisfies

    Q(A) >= (beta/2) c_H rho c0 epsilon^2 n^2.           (Q)

This is a collective cost with U007 exponent sigma=2 and therefore beats polynomial block entropy for any n(a)~a^-alpha with alpha>0 at the scaling level.

Wolfram 15.0.1 independently reconfirmed the soft eigenvalue `4 Sin[Pi/(2 n)]^2` with n^2 limit pi^2, and that a volume-order norm c n^4 yields asymptotic cost pi^2 c n^2. A separate symbolic check confirmed the counting-to-soft-scale ratio grows like n^2.

## 3. Why this does not yet solve the nonlinear distance lemma

The coordinate-level event is basis dependent. In the full gauge theory, a statement such as "a positive fraction of gauge-fixed link coordinates exceed epsilon" can change under:

- a different gauge representative;
- a different orthonormal basis of the transverse subspace;
- nonabelian exponential coordinates and chart changes;
- motion along the minimizer/background manifold;
- topological/harmonic modes.

Therefore (D) is proved as written only for a fixed projected coordinate system. It does not yet provide the gauge-invariant nonlinear bad-block event required by the program.

## 4. Basis-free replacement

A natural basis-free event is to require a positive density of local cells/links to carry a lower bound on the norm of the **projected transverse fluctuation field** in a chosen local decomposition. If P_T is the orthogonal projection away from gradients and harmonics, define a local energy density e_x(P_T A) and require

    #{x : e_x(P_T A) >= epsilon^2} >= rho |B|.

Whenever the local energies sum exactly to ||P_T A||^2, the same counting proof gives a volume-order distance. The challenge is locality: the Hodge projection P_T is generally nonlocal, so e_x(P_T A) may not be suitable for a contour event or reflection-positive block decomposition.

This isolates a new bottleneck more sharply than U010:

> Find a **local or quasi-local gauge-covariant transverse decomposition** whose positive-density local norm controls global distance from the minimizer/gauge/harmonic manifold with only summable tails.

A completely nonlocal projection may prove coercivity but destroy the locality needed for polymer/RG and OS reflection arguments.

## 5. Outcome classification

Outcome: **proved after an explicit restriction**.

Proved: for any fixed projected orthonormal coordinate system with volume-order dimension, a positive density of coordinates above epsilon forces ||A||^2>=c n^4; combined with U010, this yields a beta n^2 quadratic action cost.

Not proved: a gauge-invariant, local/quasi-local nonlinear event with the same distance consequence.

No counterexample was found to the restricted coordinate statement because it is an immediate counting inequality. The route does not close the original Yang–Mills problem.

## 6. Tool provenance

- Mathbox research-program and research-attempt skills were read and followed for route scoping and evidence classification.
- Mathbox computation-audit guidance was read before interpreting the Wolfram checks.
- Wolfram 15.0.1 was used only for exact symbolic cross-checks of the n^-2 soft mode and asymptotic n^2 cost; the proof of the coordinate counting lemma is written above and does not depend on the CAS.
- Consensus was explicitly invoked, but the connected account remains at its monthly search limit (30/30, reset October 1), so no new literature result is claimed.
- GitHub preserves this record in the private project repository.

## 7. Next bounded attempt

Test quasi-local transverse projections. A promising candidate is a finite-range approximate Hodge projector built from a polynomial/rational approximation to the inverse lattice Laplacian on the block, with range R. The decisive question is whether one can obtain simultaneously:

1. approximation error small enough to preserve the U003 relative mixing budget;
2. locality range R=o(n) so bad-block events remain contour-compatible;
3. a lower bound showing positive-density local projected amplitude still forces gamma>2 distance scaling.

If finite-range approximation error cannot be made summable without R comparable to n, this route conflicts with locality and should be rejected.
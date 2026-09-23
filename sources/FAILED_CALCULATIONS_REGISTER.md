# Failed Calculations & Refuted Claims Register: Yang–Mills Existence & Mass Gap

Authoritative register of disproved claims, retracted papers, bugged functional integral strategies, and non-working computational heuristics in 4D Quantum Yang–Mills theory and the Clay Millennium Mass Gap Problem.

The purpose of this register is to ensure that the autonomous research daemons and discrepancy hunters do **not** waste computational resources or cycle time re-evaluating known dead ends.

---

## 1. High-Profile Failed Claims & Debunked Strategies

### 1.1 Purely Perturbative Mass Gap Claims
- **Claimed Heuristic**: Deducing the mass gap $\Delta > 0$ directly from the 1-loop or 2-loop asymptotic freedom formula:
  $$\beta(g) = -\frac{11 N}{3} \frac{g^3}{16\pi^2} + O(g^5) < 0 \implies \Lambda_{\text{QCD}} = \mu \exp\left(-\frac{1}{2 b_0 g^2}\right)$$
- **The Fatal Mathematical Flaw**:
  - The function $f(g) = e^{-1/(2 b_0 g^2)}$ has an **essential singularity** at $g = 0$.
  - Its Taylor expansion around $g = 0$ is identically zero to all orders:
    $$\left. \frac{d^k}{dg^k} e^{-1/(2 b_0 g^2)} \right|_{g=0} = 0 \quad \forall k \ge 0$$
  - As a result, the non-perturbative mass gap is mathematically invisible to any finite-order perturbation series, Borel summation of perturbation theory, or Feynman diagrammatic expansion.
  - Any paper claiming to "derive" confinement or the mass gap without non-perturbative constructive methods (such as lattice continuum limits, cluster expansions, or topological instanton measures) is mathematically vacuous.
- **Automated Filter**:
  - Track 1 and Track 4 discard any candidate that relies on truncated perturbative expansions for $\Delta$. The gap must be extracted via transfer matrix spectral decay or non-perturbative lattice scaling.

### 1.2 Global Gauge Fixing & Singer's Theorem (Singer, 1978)
- **Claimed Strategy**: Fixing the gauge globally in the continuum path integral using standard Faddeev-Popov conditions (e.g. Landau gauge $\partial_\mu A_\mu = 0$ or Coulomb gauge $\nabla \cdot \mathbf{A} = 0$) and computing functional determinants without boundary corrections.
- **The Fatal Mathematical Flaw**:
  - I.M. Singer (1978, *Communications in Mathematical Physics* 60, 7–12) proved that on compactified spacetime $S^4$ (or torus $T^4$), there exists **no continuous, global cross-section** of the gauge orbit bundle $\mathcal{A} \to \mathcal{A}/\mathcal{G}$.
  - Any continuous gauge-fixing condition inevitably encounters **Gribov horizons** (V.N. Gribov, 1977), where the Faddeev-Popov operator $-\partial_\mu D_\mu(A)$ develops zero eigenvalues and changes sign.
  - Naive functional integration across Gribov copies produces sign cancellations ($+1 - 1 = 0$) and invalidates the naive path integral measure.
- **Automated Filter**:
  - The hunter rejects any continuum functional integral formulation that assumes a non-singular global gauge section.
  - Rigorous formulations must work in manifest gauge-invariant variables (Wilson loops, lattice holonomies $U_\mu(x) \in SU(N)$) or restrict rigorously to the Fundamental Modular Region.

### 1.3 Osterwalder–Schrader Reflection Positivity Breakdown
- **Claimed Strategy**: Introducing non-local or non-covariant gauge-fixing terms or truncating gluon propagators to model infrared mass generation (e.g. Gribov-Zwanziger or massive gluon models).
- **The Fatal Mathematical Flaw**:
  - To reconstruct a physical, unitary quantum field theory in 4D Minkowski spacetime satisfying the Wightman axioms, the Euclidean theory **must** satisfy Osterwalder–Schrader (OS) Reflection Positivity:
    $$\langle \Theta(F) F \rangle \ge 0$$
    for all functionals $F$ supported on the positive time half-space $x_0 > 0$.
  - Many heuristic models of gluon confinement introduce propagators with complex conjugate poles or negative spectral weights. While this "confines" the gluon by removing it from the physical spectrum, doing so carelessly violates reflection positivity on the gauge algebra, leading to indefinite metrics and negative-norm states in the reconstructed Hilbert space.
- **Automated Filter**:
  - Track 3 (`track3_reflection_positivity`) audits the transfer matrix Gram matrix $\langle \Theta(A_i) A_j \rangle$, requiring strict positive-semidefiniteness (minimum eigenvalue $> 0$). Any action or approximation with negative eigenvalues is instantly flagged and rejected.

### 1.4 Haag's Theorem & The Free Fock Space Fallacy (Haag, 1955)
- **Claimed Strategy**: Representing interacting 4D Yang–Mills theory in the standard Fock space $\mathcal{F}(\mathcal{H})$ of free asymptotic gluons and defining the Hamiltonian as $H = H_0 + V$.
- **The Fatal Mathematical Flaw**:
  - Haag's theorem proves that in 4D relativistic quantum field theory, the interaction picture does not exist: any Poincaré-invariant field theory related to a free field by a unitary operator at a fixed time is itself a free field.
  - The physical vacuum state $|\Omega\rangle$ of interacting Yang–Mills contains infinite condensates ($\langle F_{\mu\nu}^a F^{\mu\nu}_a \rangle \ne 0$) and lives in a Hilbert space that is **unitarily inequivalent** to the free Fock space.
- **Automated Filter**:
  - Reject any proof attempting to build the physical Yang–Mills Hilbert space as a direct perturbation on the free Fock space.

---

## 2. Computational Pitfalls & Traps in Multiscale Analysis

### 2.1 The Determinant Locality Trap (Repo-Certified Trap U045)
- **Trap**: In multiscale phase-cell cluster expansions, bounding the functional determinant variation $\log \det(I + K)$ of coarse-graining fluctuations using naive operator rank bounds times the smallest eigenvalue.
- **Mathematical Failure**:
  - Charging every boundary variable the worst-case inverse high-mode gap yields an unsuppressed cost per hypercube:
    $$O(\delta \ell^5) = O(\alpha^{4/13} \alpha^{-5/13}) = O(\alpha^{-1/13}) \to \infty \quad \text{as } \alpha \to 0$$
  - This negative exponent produces an unsummable volume divergence that destroys the continuum limit as the lattice spacing $a \to 0$.
- **The Resolution (U046)**:
  - Determinant estimates must use the exact spatial Green kernel density, which exhibits surface-order trace scaling:
    $$O(\delta \ell^3) = O(\alpha^{4/13} \alpha^{-3/13}) = O(\alpha^{1/13}) \to 0 \quad \text{as } \alpha \to 0$$
  - The positive exponent $+1/13$ ensures uniform convergence and summability across the multiscale lattice hierarchy.
- **Automated Filter**:
  - Track 2 (`track2_green_trace_scaling`) explicitly verifies that the naive rank exponent is rejected (divergent) and that only the $O(\ell^3)$ Green trace exponent is accepted.

### 2.2 Compact $U(1)$ Roughening & Deconfinement False Analogy
- **Trap**: Concluding that because strong-coupling lattice gauge theory produces an area law $\langle W(C) \rangle \sim e^{-\sigma \text{Area}(C)}$ and a positive mass gap for $\beta \ll 1$, the continuum limit must also have a mass gap.
- **Mathematical Fact**:
  - In 4D compact $U(1)$ lattice gauge theory, Wilson's strong coupling expansion proves confinement for small $\beta$. However, at $\beta_c \approx 1.01$, the theory undergoes a **roughening and deconfinement phase transition** (Guth 1980, Fröhlich & Spencer 1982) into a massless Coulomb phase with no mass gap.
  - Strong coupling confinement alone is insufficient; one must rigorously prove the absence of a deconfinement transition as $\beta \to \infty$, which relies crucially on non-abelian asymptotic freedom ($SU(N)$).
- **Automated Filter**:
  - Sieve Track 4 enforces volume and coupling scaling checks across $\beta = 2.30 \dots 2.50$, rejecting claims based solely on strong-coupling expansion without asymptotic scaling.

### 2.3 Dimensionally Reduced 2D/3D Yang-Mills Extrapolation
- **Trap**: Generalizing proofs from 2D Yang–Mills (Migdal 1975, Witten 1991) to 4D.
- **Mathematical Fact**:
  - In 2D spacetime, the gauge field has $D - 2 = 0$ physical transverse polarizations: there are no propagating physical gluons. 2D confinement is purely geometric and kinematic.
  - In 4D, there are 2 physical transverse gluon polarizations, and the non-linear self-interactions generate non-trivial infrared dynamics and renormalization scale anomalies.
- **Automated Filter**:
  - Sieve scripts reject any reduction that suppresses transverse spatial gauge degrees of freedom.

---

## 3. Register Summary Table

| Category | Reference / Target | Flaw / Barrier | Automated Action |
|---|---|---|---|
| **Perturbative Trap** | Perturbative $\beta$-function | Essential singularity $e^{-1/g^2}$; Taylor series vanishes at $g=0$ | Reject perturbative-only mass gap derivations |
| **Gauge-Fixing Trap** | Singer's Theorem (1978) | No global continuous gauge section on $S^4$; Gribov horizons | Require gauge-invariant holonomies or modular domain |
| **Axiom Trap** | Osterwalder–Schrader Axioms | Negative-norm ghost states break reflection positivity $\langle\Theta(F)F\rangle \ge 0$ | Reject non-reflection-positive actions/propagators |
| **Hilbert Space Trap** | Haag's Theorem (1955) | Physical vacuum unitarily inequivalent to free Fock space | Reject free Fock space interaction-picture constructions |
| **Multiscale Trap** | U045 Naive Rank Bound | Divergent scaling $O(\delta \ell^5) = O(\alpha^{-1/13}) \to \infty$ | Enforce U046 Green trace scaling $O(\delta \ell^3) = O(\alpha^{1/13}) \to 0$ |
| **Lattice Trap** | Compact $U(1)$ Analogy | Roughening/deconfinement transition to massless Coulomb phase | Verify non-abelian asymptotic freedom scaling |
| **Dimension Trap** | 2D/3D Dimensional Reduction | Zero transverse gluons in 2D; fails to model 4D dynamics | Reject topological models lacking propagating transverse modes |

# No-Go Register: Refuted Yang–Mills Proof Strategies & Mathematical Barriers

Authoritative register of disproved conjectures, refuted frameworks, and structural barriers in 4D quantum Yang–Mills theory and the Clay Millennium Mass Gap Problem.

---

## 1. Perturbative Confinement & Asymptotic Freedom Overreach

- **Barrier**:
  Perturbation theory in 4D $SU(N)$ Yang–Mills yields asymptotic freedom ($\beta(g) = -\frac{11 N}{3} \frac{g^3}{16\pi^2} + O(g^5) < 0$). However, the physical mass gap $\Delta > 0$ and color confinement are non-perturbative:
  $$\Delta \propto \Lambda_{\text{QCD}} = \mu \exp\left(-\frac{1}{2 b_0 g^2(\mu)}\right)$$
  which has an essential singularity at $g = 0$ ($e^{-1/g^2}$ is non-analytic and has vanishing Taylor expansion at $g = 0$).
- **No-Go**: Any proof attempting to derive a strictly positive mass gap from finite-order perturbation theory or Borel resummation alone without non-perturbative topological/instanton or lattice continuum limits is fundamentally unsound.

---

## 2. Gribov Horizon & Global Gauge-Fixing Obstruction (Singer 1978)

- **Barrier**:
  Singer proved that in 4D Euclidean spacetime with compact gauge group $G$, there exists no continuous, global gauge-fixing condition (no global cross-section of the gauge orbit bundle $\mathcal{A}/\mathcal{G}$).
  Coulomb and Landau gauges possess Gribov copies where the Faddeev-Popov determinant $\det(-\partial_\mu D_\mu)$ vanishes or changes sign.
- **No-Go**: Any continuum proof that assumes a global, non-singular Faddeev-Popov gauge fixing without addressing Gribov horizons or Gribov-Zwanziger horizon condition fails.

---

## 3. Haag's Theorem & The Interaction Picture Barrier

- **Barrier**:
  Haag's theorem proves that the interaction picture cannot exist for non-trivial relativistic quantum field theories in 4D Minkowski spacetime satisfying the Wightman axioms. The physical vacuum and Hilbert space are unitarily inequivalent to the free Fock vacuum.
- **No-Go**: Any construction representing interacting 4D Yang–Mills as a unitary transformation or perturbation acting on the free Fock space violates Poincaré invariance and the Wightman axioms.

---

## 4. Determinant Locality Obstruction (U045) & Green Trace Scaling (U046)

- **Barrier**:
  In multiscale phase-cell cluster expansions, bounding the functional determinant variation by rank times smallest eigenvalue fails:
  Charging every boundary variable the worst-case inverse high-mode gap yields an unsuppressed cost $O(\delta \ell^5) = O(\alpha^{-3/26})$.
- **Resolution**:
  Determinant estimates must use the exact spatial Green kernel density, which exhibits surface-order $O(\ell^3)$ trace scaling on 4D slabs ($O(\delta \ell^3) = O(\alpha^{1/26}) \to 0$).

---

## 5. Reflection Positivity & Osterwalder–Schrader Reconstructibility

- **Barrier**:
  Euclidean lattice gauge path integrals must satisfy Reflection Positivity with respect to time-slice hyperplanes:
  $$\langle \Theta(F) F \rangle \ge 0$$
  for any functional $F$ supported on the positive half-space.
- **No-Go**: Any discretization, gauge fixing, or regularized Hamiltonian that destroys reflection positivity fails to reconstruct a physical Hilbert space with positive-definite metric and self-adjoint Hamiltonian with positive energy spectrum.

---

## 6. Ultrasoft Mode Inheritance Obstruction (U022 / U023)

- **Barrier**:
  Decoupling coarse spatial blocks without exact Steklov boundary conditioning leaves zero-energy and ultrasoft gauge modes inherited across slab boundaries, destroying cluster decomposition and exponential decay.

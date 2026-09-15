# U024 — smallest plaquette compression cannot supply a weak-coupling lower mass bound

Date: 2026-09-14.

**We have not solved the Yang–Mills problem yet.**

This bounded attempt follows U023 back to the physical bottleneck: can the smallest gauge-invariant plaquette sector provide a rigorous positive finite-volume lower energy that survives weak coupling in physical units? The answer is negative for the obvious two-character compression. Its Ritz matrix develops a large negative eigenvalue before the omitted sectors are restored, so it can provide variational upper information but no lower bound on the full excitation gap. This is a structural variational-direction obstruction, not evidence against a Yang–Mills mass gap.

## 1. Reuse only the verified U003 matrix elements

In the U003 Hamiltonian convention,

    H=(g^2/a) Hhat,
    Hhat=Hhat_E+Vhat,
    lambda=4/g^4.

For the centered gauge-invariant pair

    f=chi_(1/2)(U_p),
    h=chi_1(U_p),

U003 exactly obtained

    E_pair=diag(3/2,4),
    W_pair=[[0,-lambda/2],[-lambda/2,0]],

where W is the magnetic interaction after its irrelevant constant shift. Therefore the compressed shifted Hamiltonian is

    M(lambda)= [[3/2,-lambda/2],[-lambda/2,4]].          (M)

No claim is made that this 2x2 matrix is an invariant subspace of the full Hamiltonian; it is a quadratic-form compression.

## 2. Exact compressed eigenvalues

The eigenvalues of (M) are

    e_-(lambda)=[11-sqrt(25+4lambda^2)]/4,
    e_+(lambda)=[11+sqrt(25+4lambda^2)]/4.

Wolfram 15.0.1 independently returned exactly these expressions.

The lower compressed eigenvalue becomes negative once

    sqrt(25+4lambda^2)>11,

that is

    lambda^2>24,
    lambda>2 sqrt(6).

Since lambda=4/g^4, this occurs deep in the weak-coupling regime and indeed for all sufficiently small g.

Restoring physical units gives

    E_-(g,a)
      = (g^2/(4a))[11-sqrt(25+64/g^8)].

As g->0,

    E_-(g,a) = -2/(a g^2) + 11 g^2/(4a) + lower terms.

Thus the shifted two-state compression is violently nonpositive at weak coupling.

## 3. Why this does not mean the full Hamiltonian is unstable

The original magnetic potential

    lambda sum_p [1-(1/2)chi_(1/2)(U_p)]

is nonnegative. The negative compressed eigenvalue appears only after subtracting the extensive constant lambda N_p and then restricting to a tiny non-invariant centered subspace. The true vacuum energy shifts by a large amount, and the true vacuum vector is not the Haar vacuum, as U003 already proved.

Therefore the negative Ritz value is not a physical negative excitation energy. It says the chosen reference/centering is inappropriate for extracting weak-coupling lower excitation bounds.

## 4. Variational direction obstruction

For a self-adjoint Hamiltonian H, restricting the Rayleigh quotient to a trial subspace gives **upper bounds** on ordered eigenvalues via the min-max principle when the indexing and orthogonality conditions are handled correctly. It does not give a lower bound on the full first excitation merely because the compressed matrix has a positive eigenvalue.

In particular, e_+(lambda) cannot certify that every physical state orthogonal to the true vacuum has energy at least e_+. Omitted states may lie below it, and the trial vectors are not even known to be orthogonal to the true weak-coupling vacuum.

Hence the smallest Wilson-loop/plaquette compression fails the stated U023 target as a source of a rigorous **lower** mass bound.

## 5. What kind of method could give a lower bound?

A lower excitation bound requires control on the entire centered physical space or a theorem reducing it to controlled sectors. Candidate mechanisms include:

1. a positive-commutator/coercivity inequality around the **true** vacuum;
2. a representation-theoretic decomposition into invariant sectors with a lower bound in every nonvacuum sector;
3. a ground-state transform producing a Dirichlet form with a Poincare inequality in the true vacuum measure;
4. a rigorous Feshbach/Schur reduction where the omitted complement has a proved lower coercivity and the mixing is controlled — structurally the U019 certificate.

The first two are direct mass-generation routes; the third resembles the strong-coupling stochastic/transfer approach but would need weak-coupling true-vacuum control; the fourth is the multiscale route developed U019–U023.

## 6. A useful positive conclusion from the failure

The computation shows why a finite set of Wilson-loop trial states is the wrong direction for proving the mass gap: variational truncations naturally estimate low energies from above, whereas the Clay problem needs a uniform positive lower spectral edge after removing the vacuum.

Therefore future finite-dimensional computations should be used to **falsify candidate coercivity constants or identify invariant-sector structure**, not to infer a lower mass gap from positive Ritz eigenvalues.

## 7. Literature status

A fresh Consensus search for rigorous weak-coupling Hamiltonian SU(2) lower-gap results was attempted as requested by the project workflow, but the connected account remains at its monthly 30-search limit and reports reset October 1. No new literature claim is inferred from that failed search.

## 8. Outcome classification

Outcome: **refuted for the smallest plaquette-compression lower-bound route**.

Proved from U003's exact matrix elements:

    e_±=[11±sqrt(25+4lambda^2)]/4,

and the lower shifted Ritz value is negative for lambda>2sqrt(6), diverging as -2/(a g^2) in physical units as g->0.

Not proved:

- any lower bound on the true weak-coupling Yang–Mills excitation energy;
- a true-vacuum coercivity inequality;
- invariant-sector reduction;
- continuum mass gap.

## 9. Next bounded attempt

Test the **representation-sector** alternative rather than another variational truncation. On a finite spatial lattice, use gauge invariance and center/charge-conjugation symmetries to identify exact invariant sectors of the Hamiltonian. Determine whether the vacuum sector and the lightest nontrivial gauge-invariant sector are separated by a symmetry label that survives the continuum limit. If all glueball excitations share the vacuum's exact global quantum numbers (as the scalar 0++ channel does), symmetry alone cannot furnish a lower gap and this route should be rejected quickly. The test is conceptual and source-checkable before attempting any heavy computation.
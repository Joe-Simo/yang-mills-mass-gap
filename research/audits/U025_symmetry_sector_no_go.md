# U025 — exact symmetry sectors cannot separate the vacuum from all glueball excitations

Date: 2026-09-14.

**We have not solved the Yang–Mills problem yet.**

This bounded attempt executes U024's representation-sector stress test. Outcome: exact global symmetry decomposition is useful for organizing the spectrum, but it cannot by itself prove the full mass gap because nonvacuum scalar glueball excitations occur in the same vacuum-quantum-number sector. A lower bound is still required **inside** that sector.

## 1. Exact-sector idea

On a finite periodic spatial lattice, the pure gauge Hamiltonian commutes with exact lattice symmetries including translations, the cubic rotation group, parity, and (where applicable) charge conjugation and center-related transformations. Therefore the physical Hilbert space decomposes into invariant sectors labeled by these quantum numbers.

If every nonvacuum state were forced into a sector different from the vacuum, one could hope to bound each nontrivial sector separately and use symmetry to exclude dangerous mixing with the vacuum.

The key stress test is whether a genuine excited state exists with the vacuum's own exact quantum numbers.

## 2. The scalar glueball is in the vacuum-quantum-number channel

Fresh web/source checks found explicit lattice literature describing the lightest scalar glueball as 0++ and, more decisively, Della Morte and Giusti's lattice Yang–Mills work describes a computation of "the lightest glueball with vacuum quantum numbers" using exact global-symmetry sectors. A recent lattice glueball form-factor source likewise states that the A1+ / positive-charge-conjugation interpolators excite the positive-parity 0++ glueball after vacuum subtraction.

Relevant source records inspected during this attempt:

- Michele Della Morte and Leonardo Giusti, *A novel approach for computing glueball masses and matrix elements in Yang-Mills theories on the lattice*, arXiv:1012.2562. Its abstract says the partition function is decomposed by parity, charge conjugation, translations, rotations and central conjugations, and that the method computes the lightest glueball **with vacuum quantum numbers**.
- A recent lattice source on gravitational form factors of glueballs states that vacuum-subtracted A1+/A1 positive-C interpolators have the positive-parity 0++ glueball as their lowest-energy state.

These are physics/lattice results, not a rigorous construction of continuum Yang–Mills. For the present logical test they establish the intended meaning of the symmetry labels used in the candidate route: the scalar glueball channel shares the vacuum's global quantum numbers.

## 3. Abstract mathematical obstruction

The obstruction does not depend on trusting a numerical glueball mass. Let H commute with a symmetry group G, and let H_triv be the invariant/trivial representation sector containing the vacuum Omega. Symmetry decomposition only gives

    H = H_triv direct-sum (other irreducible sectors).

Nothing prevents H_triv from having spectrum

    0 = E_0 < E_1 <= E_2 <= ...

or even E_n downarrow 0 in a limiting sequence of theories/volumes. The excited vectors in H_triv transform exactly like the vacuum under G while remaining orthogonal to it.

Thus lower bounds on all **nontrivial** symmetry sectors do not imply a mass gap. One must also prove

    H|_(H_triv intersect Omega-perp) >= m I

with m>0 in physical units.

That is essentially the original hard spectral problem restricted to the vacuum-quantum-number sector.

## 4. Vacuum subtraction does not create a new symmetry sector

A scalar gauge-invariant operator O with nonzero vacuum expectation can be centered:

    O_c = O - <Omega,O Omega> I.

Then O_c Omega is orthogonal to Omega, but O_c has the same transformation law as O. If O is symmetry invariant, O_c Omega remains in H_triv.

Therefore centering/vacuum subtraction removes the vacuum vector algebraically but does not provide a symmetry label separating scalar excitations from it. This is exactly why vacuum-subtracted scalar correlators can probe the 0++ channel.

## 5. Center symmetry also does not solve the full problem

Center/electric-flux sectors can separate certain winding or charged sectors from the vacuum and may be valuable for string-tension/confinement questions. But local glueballs are center-neutral. Hence even a rigorous positive lower bound in nontrivial center sectors would leave the neutral 0++ sector untreated.

Likewise parity or charge-conjugation bounds can control odd sectors without addressing the even-even scalar channel.

## 6. Consequence for research strategy

Reject the idea that **representation labels alone** can furnish the Clay mass gap. They remain useful as reductions: a complete proof may bound sectors separately, but it must include a coercivity argument inside the vacuum quantum-number sector after removing the one-dimensional vacuum.

This points back to the true-vacuum Dirichlet/Poincare or Schur-complement mechanisms rather than a pure symmetry superselection argument.

A potentially useful reformulation is now sharper:

> Prove a Poincare/spectral-gap inequality for centered gauge-invariant scalar observables in the true weak-coupling vacuum measure/transfer Dirichlet form, uniformly in volume and along the continuum trajectory.

If this scalar vacuum sector can be controlled, other exact symmetry sectors may then be easier auxiliary obligations.

## 7. Evidence qualification

The external source check was performed through current web search because the connected Consensus account remains rate-limited. No claim is made that the cited lattice papers rigorously prove the continuum mass gap. They are used only to verify that the standard 0++ glueball channel is the vacuum-quantum-number channel, which is the discriminating fact for this route.

The abstract symmetry argument itself is exact and independent of those numerical lattice conclusions: whenever the trivial representation contains any centered excitations, symmetry alone supplies no lower energy bound within it.

## 8. Outcome classification

Outcome: **refuted as a complete symmetry-only route**.

Established:

- exact symmetries decompose the finite-lattice Hilbert space into invariant sectors;
- the physically relevant scalar 0++ glueball is conventionally the vacuum-quantum-number channel;
- vacuum subtraction leaves centered scalar excitations in the same symmetry representation;
- therefore symmetry separation cannot by itself prove the full positive gap.

Not proved:

- a uniform lower bound inside the centered scalar/vacuum sector;
- true-vacuum weak-coupling Poincare inequality;
- continuum construction or mass gap.

## 9. Next bounded attempt

Attack the centered scalar sector directly through a **ground-state transformed Dirichlet form**. Start with a one-plaquette SU(2) model where the true positive ground state can be represented explicitly or reduced to a one-dimensional Sturm–Liouville problem. Determine how its Poincare/spectral gap scales at weak coupling after restoring physical units. This is not the full lattice, but unlike U024 it is a lower-gap calculation in the true vacuum rather than a Ritz upper-bound truncation. If even the one-plaquette true-vacuum gap collapses in the relevant scaling, it will identify another obstruction; if it stays positive/diverges, the next question is whether interactions and volume destroy it.
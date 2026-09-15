# U004 — weak-coupling localization frontier after U003

Date: 2026-09-14.

**We have not solved the Yang–Mills problem yet.**

This is a research checkpoint, not a complete candidate. It resumes from U003 and preserves the distinction between exact auxiliary results and the unproved Clay/Jaffe–Witten target.

## 1. Starting point

U003 proved a conditional full-space gap-transport theorem: if the true fixed-physical-time transfer deficit G_j=I-S_j has a coarse block with summably small relative loss, a uniformly coercive fine block, and square-summable relative mixing, then the full gap stays positive. The theorem is useful only if those hypotheses are established in the actual vacuum representation of Yang–Mills.

U003 also showed that two natural weak-coupling initializations do not supply those hypotheses. Relative boundedness of the magnetic term by the pure-electric operator diverges at least as 2/(sqrt(6) g^4), and the globally optimized one-plaquette positive exponential dressing has residual oscillation growing as 2 lambda-3 sqrt(lambda)+9/8 with lambda=4/g^4.

## 2. Consequence: a global electric perturbation route is quantitatively mis-scaled

The exact SU(2) two-character compression gives

    ||H_E^(-1/2) Q W Q H_E^(-1/2)|| >= 2/(sqrt(6) g^4).

Therefore any weak-coupling proof that treats the entire magnetic interaction as a small relative perturbation of the electric Hamiltonian, uniformly in the physical Hilbert space, cannot close as g->0. This is a no-go statement for that proof architecture, not for Yang–Mills itself.

The one-plaquette trial result points in the same direction: even after a positive exponential dressing optimized over one scalar parameter, the residual oscillation is asymptotically 2 lambda, not o(1). Thus the weak-coupling reference object must absorb substantially more of the magnetic sector before a small-error argument can begin.

## 3. Literature cross-check

A focused Consensus search on rigorous Hamiltonian/lattice weak-coupling mass-gap work returned no established theorem that supplies the missing U003 relative block estimates. One relevant 2025 paper is:

Paulo A. Faria da Veiga and M. O'Carroll, *On charge conjugation, correlations, Elitzur’s theorem and the mass gap problem in lattice SU(N) Yang–Mills models in d=4 dimensions*, Journal of Mathematical Physics (2025), Consensus citation count 1 at retrieval. The fetched abstract says that a mass gap is related to exponential decay of truncated gauge-invariant plaquette correlations and proves structural statements including charge-conjugation sectors and Elitzur-type vanishing results. Its mass-gap discussion is conditional/indicative: it says "if a mass gap occurs" and describes a Haar-measure local mass term as an indication that a gap may develop. It therefore does not close the continuum gap obligation.

Consensus record: https://consensus.app/papers/on-charge-conjugation-correlations-elitzur’s-theorem-and-veiga-ocarroll/71e6a1bb4b4b5cb097f1577a2ca5fa86/?utm_source=chatgpt

The 2026 Faizal–Shabir construction remains under the separate U002 audit and is not imported as a verified theorem.

## 4. Sharpened frontier

The next viable analytic route is **localized weak-coupling coercivity in the true vacuum**, not a global perturbation of Haar/electric theory.

A sufficient local-to-global program would have to establish, on the same asymptotically free trajectory:

1. A true or rigorously controlled approximate vacuum/reference measure concentrated near low-action configurations, with gauge redundancy handled without discarding physical states.
2. A fixed-physical-time transfer deficit whose fine-sector coercivity is uniform after localization.
3. A coarse/fine mixed form estimate with square-summable relative coefficient, as required by U003 or an improved replacement theorem.
4. A large-field complement estimate whose probability/form contribution is exponentially small enough to be summable **without assuming the desired mass gap or clustering**.
5. Reflection positivity and sufficient OS convergence for the same objects, followed by a nonzero positive-time witness to rule out a vacuum-only or infinite-mass limit.

The key unknown is item 4: a noncircular large-field suppression estimate strong enough in physical units. Standard weak-coupling intuition says the Wilson action concentrates around flat connections, but turning this into the required uniform transfer-form estimate while preserving gauge invariance, volume control, topology and OS positivity is precisely the difficult bridge.

## 5. What was established in this unit

- No new Yang–Mills mass-gap theorem was proved.
- The U003 exact lower bound rules out the simplest global electric-relative weak-coupling perturbation architecture.
- The optimized one-plaquette dressing also fails to produce a small global residual.
- A focused literature check did not reveal an existing theorem supplying the missing true-vacuum relative block estimates.
- The research frontier is now isolated to a noncircular **localized weak-coupling coercivity + large-field suppression** estimate compatible with reflection positivity and the continuum trajectory.

## 6. Next executable step

Construct and test a finite-volume gauge-invariant localization inequality around flat connections for the Wilson action. The first falsification target is whether a candidate large-field tail estimate can be uniform enough in volume and lattice spacing to enter the U003 block theorem after conversion to fixed physical time. Any estimate whose constants grow like the number of plaquettes, or whose exponent loses the required physical-scale factor, will be rejected before attempting a full multiscale construction.

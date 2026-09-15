# Yang–Mills Existence and Mass Gap Research

Private working repository. **No complete verified solution.**

The target is the full Jaffe–Witten/Clay assertion: a nontrivial four-dimensional quantum Yang–Mills theory for every compact simple gauge group in scope, with the required axioms, Yang–Mills identification, continuum/infinite-volume setting, and strictly positive finite physical mass gap.

## Latest checkpoint — U034, 2026-09-15

Read `research/audits/U034_history_variance_and_physical_cycles.md`.

The six-color retained-history decomposition now has an explicit sufficient collective-variance coefficient on the ENTIRE centered physical endpoint algebra. A lower bound on this coefficient gives a physical-time transfer bound without assuming independent history layers or replacing history operators by powers of a reduced transfer. A direct bounded-density comparison proves a positive finite-Wilson coefficient, but the bound deteriorates exponentially in space-time volume and coupling.

An exactly integrated two-dimensional Wilson cylinder has a centered, gauge-invariant boundary-loop observable with conditional-variance eigenvalue `1-[I_2(beta)/I_1(beta)]^L`, tending to zero at fixed circumference L as beta increases. The conditional algebras still intersect exactly at constants. This is a diagnostic Wilson model, NOT the four-dimensional vacuum or a counterexample to its mass gap.

Retaining a forest at ONE TIME leaves only constants among physical retained observables, for any gauge-invariant vacuum measure. Combining this with U032 proves a full finite-regulator gap lower bound `-log(tanh(sum_cotree beta_e))/tau`; for a periodic spatial N-cube the uniform-coupling cotree count is `2N^3+1`. The bound is too weak in growing volume. The forest argument does not remove the full retained TIME HISTORY.

Eleven new exact checks and all twelve U033 checks passed. Run `python checks/U034_history_variance_and_cycle_checks.py --output evidence/U034_checks.json`. The checker includes exact weighted path enumeration, noncommuting SU(2) cylinder geometry, twelve all-tail Bessel-ratio certificates, and a finite-group forest control. The note and manifest distinguish these populations from the universal arguments. Two structural polynomial-equality test defects were repaired and recorded. Compilation and indentation checks passed; static lint/typecheck and Lean were unavailable. Results are self-reviewed, not formal/expert verification or a novelty claim.

Next target: an actual-vacuum conditional-variance response for overlapping physical cycle algebras, with connected-correlation control independent of the external volume and appropriate physical scaling. Trivial intersection, gauge invariance alone, and the finite cotree gap do not discharge this estimate. No continuum construction or scale-uniform physical Yang–Mills mass bound is established.

## Preserved nearest dependencies

- U033: `research/audits/U033_history_conditioned_sparse_slabs.md` — extensive noncofacial columns, actual endpoint weights, full-history contraction and the retained-history obligation.
- U032: `research/audits/U032_true_vacuum_local_memory_bound.md` — fixed-set actual-vacuum contraction and all-time memory tail.
- U031: `research/audits/U031_boundary_time_and_weighted_memory.md` — finite Wilson slabs and finite-moment limitations.
- U029–U030: unchanged exact link/overlapping integration and temporal-memory records.
- U026–U028: unchanged small-graph results and their nonuniform-limit limitations.
- U003: conditional full-space gap transport, not an established Yang–Mills construction.

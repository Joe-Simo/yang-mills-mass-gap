# Yang–Mills Existence & Mass Gap Research — Working Instructions

**The Yang–Mills Existence and Mass Gap problem is not solved.** Treat every claim of an unconditional continuum construction or mass gap proof as unverified until audited against primary source dependencies and verified under machine-checked Lean 4 formalization.

## HARD RULE: Every research cycle STARTS with a Jev call

Not "consider using Jev" — **the first tool call of every research turn is a Jev batch.** If you are about to read, audit, compare, or choose between multiple candidate hypotheses or papers, run the screen first using `python3 code/jev_genius.py` or `python3 code/jev_yang.py`.

Jev decisions that are fast, cheap, and mandatory:
- **Triage & ranking**: screen every candidate hypothesis with `code/jev_genius.py triage`.
- **Failure mode check**: verify arguments against the 5 canonical Yang–Mills traps.
- **Statement fidelity**: for formal Lean 4 files, audit statement fidelity with `code/jev_genius.py lean-audit`.

## Canonical Yang–Mills Failure Modes to Reject Immediately

1. **Perturbative Confinement Conflation**:
   Attempting to deduce the physical mass gap from finite-order perturbation theory or 1-loop running couplings $\beta(g)$. The gap $\Delta \sim \Lambda_{\text{QCD}} \propto e^{-1/(2 b_0 g^2)}$ is non-perturbative with zero Taylor coefficients at $g=0$.
2. **Gribov Ambiguity / Horizon Ignoring**:
   Claiming a global non-singular gauge fixing in 4D Euclidean spacetime. Singer (1978) proved that global continuous gauge sections do not exist; Gribov copies necessarily appear.
3. **Haag's Theorem Violation**:
   Using the free Fock vacuum or standard interaction picture representation for interacting 4D Yang–Mills fields. Relativistic interacting fields require unitarily inequivalent Hilbert space representations.
4. **Reflection Positivity Breakdown**:
   Using regularizations, discretizations, or boundary smoothing functions that fail the Osterwalder–Schrader reflection positivity axiom $\langle \Theta(F) F \rangle \ge 0$, rendering the reconstructed Hamiltonian non-Hermitian or creating negative-norm ghost states.
5. **Determinant Locality Overreach (U045 Trap)**:
   Bounding multiscale determinant corrections by rank times the minimum eigenvalue, which incurs an unsuppressed $O(\delta \ell^5)$ error instead of the exact surface-order $O(\ell^3)$ Green trace scaling.

## Tools & Files

| Path | Role |
|---|---|
| `code/jev.py` | Stdlib-only Jev client. Reads key from `$TYPESAFE_API_KEY` or `.env.local`. Never log or commit the key. |
| `code/jev_yang.py` | Focused Yang–Mills candidate screener and failure-mode auditor. |
| `code/jev_genius.py` | Multi-tier Jev mathematical intelligence engine for Yang–Mills. |
| `code/yang_mills_lattice_fast.c` | OpenMP-accelerated 4D $SU(2)$ lattice gauge Wilson plaquette trace kernel. |
| `code/comprehensive_yang_discrepancy_suite.py` | Multi-track suite validating plaquette energy, Green trace scaling, and mass gap. |
| `code/autonomous_yang_engine.py` | Multi-core autonomous research daemon. |
| `formalization/YangMillsPlaquette.lean` | Lean 4 machine-checked proof of $SU(2)$ plaquette gauge invariance & cyclicity. |
| `sources/NO_GO_REGISTER.md` | Primary register of disproved frameworks and structural barriers. |
| `sources/FAILED_CALCULATIONS_REGISTER.md` | Authoritative register of refuted literature calculations, retracted papers, and excluded heuristics. |
| `CHECKPOINT.json` | Persistent machine-readable project state. |

## Standing Discipline

- Exact integer, rational fraction, and verified interval arithmetic for all theoretical claims.
- Never claim Yang–Mills existence or mass gap is proved without a complete, machine-checked Lean 4 formalization satisfying the Osterwalder–Schrader or Wightman axioms.

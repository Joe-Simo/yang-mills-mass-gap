"""Yang-Mills Failure-Mode & Candidate Screener (code/jev_yang.py).

Screens mathematical claims, proof strategies, and candidate bounds
against canonical Yang-Mills traps:
1. Perturbative Confinement & Asymptotic Freedom Conflation
2. Gribov Horizon & Singer Global Gauge-Fixing Obstruction
3. Haag's Theorem & Free Fock Representation Fallacy
4. Reflection Positivity Breakdown (Osterwalder-Schrader Axiom)
5. Determinant Locality Overreach (U045 trap vs U046 Green trace scaling)
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "code"))

import jev

CANONICAL_TRAPS = [
    "Perturbative confinement / non-perturbative essential singularity conflation",
    "Gribov ambiguity / Singer global gauge-fixing obstruction",
    "Haag theorem violation / free Fock vacuum interaction picture",
    "Osterwalder-Schrader reflection positivity breakdown",
    "Determinant locality overreach (U045) / rank-only determinant bound"
]

def build_screening_questions() -> dict[str, Any]:
    return {
        "avoids_perturbative_trap": jev.noul(
            "Does this proposal strictly avoid deriving the physical mass gap from finite-order perturbation theory or Borel resummation alone?",
            true="Unconditionally non-perturbative (lattice continuum, cluster expansion, or topological instanton vacuum)",
            false="Relies on perturbative beta function or finite-loop truncation for confinement"
        ),
        "respects_gribov_ambiguity": jev.noul(
            "Does the argument account for Singer's theorem on the non-existence of global continuous gauge fixings and Gribov horizons?",
            true="Accounts for Gribov horizons or works in gauge-invariant lattice/holonomy variables",
            false="Assumes global non-singular Faddeev-Popov gauge section without horizon bounds"
        ),
        "preserves_reflection_positivity": jev.noul(
            "Does the regularization satisfy Osterwalder-Schrader reflection positivity <Theta(F) F> >= 0 for physical Hilbert space reconstruction?",
            true="Reflection positive on time-slice hyperplanes, yielding positive-definite metric and physical Hamiltonian",
            false="Breaks reflection positivity, introducing negative-norm ghosts or non-Hermitian transfer operator"
        ),
        "respects_haag_and_u1_barriers": jev.noul(
            "Does the argument respect Haag's theorem and avoid false analogies with compact U(1) roughening?",
            true="Works outside free Fock space and relies on non-abelian asymptotic freedom",
            false="Assumes free Fock space interaction picture or treats compact U(1) confinement as proof of continuum gap"
        ),
        "methodology": jev.choice(
            "What is the mathematical foundation of this approach?",
            criteria={
                "lattice_constructive_qft": "Wilson lattice gauge theory with Osterwalder-Schrader continuum transfer recursion",
                "phase_cell_cluster_expansion": "Multiscale Balaban-style phase-cell renormalization with boundary Green trace scaling (U046)",
                "effective_or_holographic": "AdS/CFT, holographic QCD, or phenomenological potential model (conditional/heuristic)",
                "purely_perturbative_or_flawed": "Perturbative expansion, unverified operator ansatz, or flawed gauge fixing"
            }
        ),
        "viability_score": jev.score(
            "Assess the mathematical soundness of this candidate Yang-Mills proof strategy:",
            criteria=[
                "Mathematically rigorous, non-perturbative, preserves reflection positivity and Osterwalder-Schrader axioms",
                "Promising constructive framework, relies on established lattice cluster expansions with verified Green kernel bounds",
                "Heuristic, phenomenological, or contains unverified continuum limits or determinant bounds",
                "Fatal flaw: purely perturbative confinement, breaks reflection positivity, or ignores Gribov copies"
            ]
        )
    }

def screen_candidate(candidate_id: str, proposal_text: str) -> dict[str, Any]:
    state = {
        "project": "Yang-Mills Existence and Mass Gap",
        "target": "Jaffe-Witten Millennium Prize Problem",
        "candidate_id": candidate_id,
        "proposal_text": proposal_text
    }
    questions = build_screening_questions()
    resp = jev.ask(state, questions)
    try:
        jev.persist(candidate_id, state, questions, resp)
    except Exception:
        pass
    return resp

def main() -> None:
    parser = argparse.ArgumentParser(description="Jev Yang-Mills Candidate Screener")
    parser.add_argument("command", nargs="?", default="screen", choices=["screen", "triage", "cache-stats", "clear-cache"])
    parser.add_argument("--id", default="candidate", help="Candidate identifier")
    parser.add_argument("--text", help="Text description of proof strategy or theorem")
    args = parser.parse_args()

    if args.command == "cache-stats":
        print(json.dumps(jev.cache_stats(), indent=2))
    elif args.command == "clear-cache":
        count = jev.clear_cache()
        print(f"Cleared {count} cache entries")
    else:
        if not args.text:
            print("Error: --text required for screening", file=sys.stderr)
            sys.exit(1)
        res = screen_candidate(args.id, args.text)
        print(json.dumps(res, indent=2))

if __name__ == "__main__":
    main()

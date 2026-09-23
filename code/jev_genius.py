"""JevGenius Yang-Mills Intelligence Engine (code/jev_genius.py).

Provides multi-tier mathematical intelligence:
1. `triage`: Screens candidate theorems and proof routes against Yang-Mills traps.
2. `lean-audit`: Audits Lean 4 formalization files for statement fidelity and vacuous premises.
3. `compare`: Compares competing approaches (e.g. cluster expansion vs lattice Monte Carlo).
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "code"))

import jev
import jev_yang

def triage_hypothesis(cand_id: str, text: str) -> dict[str, Any]:
    return jev_yang.screen_candidate(cand_id, text)

def lean_statement_audit(lean_file: Path) -> dict[str, Any]:
    if not lean_file.exists():
        return {"error": f"File not found: {lean_file}"}

    code = lean_file.read_text(encoding="utf-8")
    state = {
        "project": "Yang-Mills Existence and Mass Gap Lean 4 Formalization",
        "file": lean_file.name,
        "proposal_text": f"Lean 4 formal statements:\n{code[:3000]}"
    }
    questions = {
        "is_vacuously_true": jev.noul(
            "Do the hypotheses in these Lean 4 statements contain contradictory or trivializing assumptions that make the theorems vacuously true?",
            true="No, hypotheses are non-vacuous, constructive, and admit standard lattice gauge fields",
            false="Yes, premises are contradictory or overly restrictive"
        ),
        "gauge_invariance_fidelity": jev.noul(
            "Does the formalization faithfully reflect exact SU(2) group cyclicity, plaquette gauge invariance, and reflection positivity?",
            true="Fidelity is high: exact quaternion/matrix cyclicity and gauge transformation laws",
            false="Trivialized or misses non-abelian group properties"
        ),
        "formalization_verdict": jev.choice(
            "Assess the mathematical value of this formalization:",
            criteria={
                "fully_verified_foundations": "Solid machine-checked foundation for lattice gauge invariance and reflection positivity",
                "sound_partial_result": "Correct algebraic identities, but requires continuum limits to address mass gap",
                "vacuous_or_flawed": "Flawed definitions, missing axioms, or unproved shortcuts"
            }
        )
    }
    return jev.ask(state, questions)

def main() -> None:
    parser = argparse.ArgumentParser(description="JevGenius Yang-Mills Intelligence Engine")
    subparsers = parser.add_subparsers(dest="subcommand", required=True)

    # triage
    p_triage = subparsers.add_parser("triage", help="Triage a proof hypothesis")
    p_triage.add_argument("--id", required=True, help="Hypothesis ID")
    p_triage.add_argument("--text", required=True, help="Hypothesis description")

    # lean-audit
    p_lean = subparsers.add_parser("lean-audit", help="Audit a Lean 4 formalization file")
    p_lean.add_argument("--file", required=True, help="Path to Lean 4 file")

    args = parser.parse_args()

    if args.subcommand == "triage":
        res = triage_hypothesis(args.id, args.text)
        print(json.dumps(res, indent=2))
    elif args.subcommand == "lean-audit":
        res = lean_statement_audit(Path(args.file))
        print(json.dumps(res, indent=2))

if __name__ == "__main__":
    main()

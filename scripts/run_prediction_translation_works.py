#!/usr/bin/env python3
"""Scientific work queue: prediction and possible translation first, cost zero.

Uses existing IberOS gates and reports missing external semantic evidence.
No external services, no mutation of corpus, no semantic metric updates.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from iberos.holdout_01 import run as holdout_audit
from iberos.prospective_gate_audit import audit_prospective_gates
from iberos.serreta_sensitivity import run as serreta_sensitivity
from iberos.prediction_translation_work import build_docket

ROOT = Path(__file__).resolve().parents[1]
DEFAULT = ROOT / "data/review/prediction_translation_pilot_v1.json"


def audit(document: dict) -> dict:
    docket = build_docket(document)
    holdout = holdout_audit()
    gates = audit_prospective_gates()
    serreta = serreta_sensitivity()
    return {
        "schema": "IberOS-Prediction-Translation-Work-Audit/1.0",
        "goal": "TESTABLE_PREDICTION_AND_POSSIBLE_TRANSLATION",
        "docket": docket,
        "existing_controls": {
            "hold01_semantic_gold_available": holdout["semantic_gold_available"],
            "hold01_independence_certified": holdout["independence_certified"],
            "prospective_gates": [{
                "protocol": g["protocol"], "state": g["gate_state"],
                "passing_candidates": len(g["passing_candidates"])
            } for g in gates["gates"]],
            "serreta_editorial_sensitivity_scenarios": serreta["scenario_count"],
            "serreta_semantic_validation": serreta["semantic_validation"],
            "corex_p01_character_baseline": "EXISTING_MODULE_NOT_RUN_WITHOUT_VERIFIED_INPUT",
        },
        "works": [
            {"id": "WORK-01", "name": "Verified readings and independent HOLD by physical object",
             "status": "BLOCKED_EXTERNAL_SIGN_AND_CONTEXT_EVIDENCE"},
            {"id": "WORK-02", "name": "Rival possible translations and falsifiable predictions",
             "status": "RETROSPECTIVE_HYPOTHESES_RECORDED"},
            {"id": "WORK-03", "name": "Blind prospective scoring, negatives and publication",
             "status": "BLOCKED_INDEPENDENT_SEMANTIC_GOLD"},
        ],
        "scientific_verdict": "NOT_EVALUATED",
        "translation_validated": False,
        "automatic_core_promotion": False,
        "external_review_completed": False,
    }


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--input", type=Path, default=DEFAULT)
    p.add_argument("--output", type=Path)
    p.add_argument("--require-scientific-confirmation", action="store_true")
    args = p.parse_args(argv)
    report = audit(json.loads(args.input.read_text(encoding="utf-8")))
    payload = json.dumps(report, indent=2, ensure_ascii=False) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(payload, encoding="utf-8")
    else:
        print(payload, end="")
    if args.require_scientific_confirmation and report["scientific_verdict"] != "CONFIRMED":
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

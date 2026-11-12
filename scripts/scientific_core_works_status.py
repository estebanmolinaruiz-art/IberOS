#!/usr/bin/env python3
"""SCI-CORE-WORKS: source-first scientific pipeline status, no fabricated evidence.

Read curated leads, the locked language rule and the existing blank evaluator.
Never read protected human role gold or alter official metrics/partitions.
"""
from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path

from iberos.prospective_role_lock import PROTOCOL_PATH
from iberos.prospective_role_evaluation import evaluate_cohort
from iberos.scientific_candidate_intake import audit

ROOT = Path(__file__).resolve().parents[1]
QUEUE = ROOT / "data/review/sci_pred04_candidate_queue_v1.json"


def compile_status(queue: dict, protocol: dict) -> dict:
    intake = audit(queue)
    zero = evaluate_cohort([], protocol)
    blocked_counts = dict(sorted(Counter(
        issue for row in intake["results"] for issue in row["issues"]
    ).items()))
    candidates = intake["ready_for_external_admission_audit"]
    return {
        "schema": "IberOS-SCI-CORE-WORKS-STATUS/1.0",
        "priority": "FALSIFIABLE_LANGUAGE_PREDICTION_AND_POSSIBLE_TRANSLATION",
        "intake": intake,
        "evidence_gap_counts": blocked_counts,
        "work_items": [
            {"id": "WORK-01", "goal": "Independent physical readings and character baselines",
             "status": "EXTERNAL_READINGS_REQUIRED"},
            {"id": "WORK-02", "goal": "Locked rival possible translations -te",
             "status": "RETROSPECTIVE_HYPOTHESES_FIXED"},
            {"id": "WORK-03", "goal": "Unblind external maker/commissioner roles and replicate",
             "status": zero["experimental_state"]},
            {"id": "WORK-04", "goal": "Admit new independent objects without known-case leakage",
             "status": "EXTERNAL_ADMISSION_AUDIT_REQUIRED" if candidates else "NO_NEW_ADMISSIBLE_CASES"},
            {"id": "WORK-05", "goal": "Obtain two blind human readings and external role gold",
             "status": "NOT_EVALUATED"},
        ],
        "scientific_results": {
            "unblinded_real_objects": zero["total_attempted_physical_objects"],
            "confirmed_semantic_predictions": 0,
            "confirmed_translations": 0,
            "role_accuracy": None,
            "scientific_pass": False,
        },
        "next_action": ("Externally audit the ready candidate(s) before sealing any prediction"
                        if candidates else
                        "Identify a NEW physical inscription with traceable image, two independent "
                        "blind sign readings and role gold kept outside the predictor"),
        "project_cost_eur": 0,
        "official_core_metrics_changed": False,
        "full3406_modified": False,
    }


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--queue", type=Path, default=QUEUE)
    p.add_argument("--protocol", type=Path, default=PROTOCOL_PATH)
    p.add_argument("--output", type=Path)
    p.add_argument("--require-scientific-pass", action="store_true")
    args = p.parse_args(argv)
    result = compile_status(json.loads(args.queue.read_text(encoding="utf-8")),
                            json.loads(args.protocol.read_text(encoding="utf-8")))
    payload = json.dumps(result, indent=2, ensure_ascii=False) + "\n"
    if args.output:
        if args.output.resolve() in {args.queue.resolve(), args.protocol.resolve()}:
            raise ValueError("Refusing to overwrite locked source files")
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(payload, encoding="utf-8")
    else:
        print(payload, end="")
    return 2 if args.require_scientific_pass and not result["scientific_results"]["scientific_pass"] else 0


if __name__ == "__main__":
    raise SystemExit(main())

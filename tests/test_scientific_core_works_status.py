"""SCI-CORE-WORKS integration: process readiness must not inflate metrics."""
import json
from pathlib import Path

from scripts.scientific_core_works_status import compile_status
from iberos.prospective_role_lock import PROTOCOL_PATH

ROOT = Path(__file__).resolve().parents[1]


def test_real_repository_queue_reports_no_prospective_gold():
    queue = json.loads((ROOT / "data/review/sci_pred04_candidate_queue_v1.json").read_text(encoding="utf-8"))
    protocol = json.loads(PROTOCOL_PATH.read_text(encoding="utf-8"))
    report = compile_status(queue, protocol)
    assert report["intake"]["total_leads"] == 5
    assert report["intake"]["ready_for_external_admission_audit"] == 0
    assert report["scientific_results"]["unblinded_real_objects"] == 0
    assert report["scientific_results"]["confirmed_translations"] == 0
    assert report["scientific_results"]["role_accuracy"] is None
    assert report["scientific_results"]["scientific_pass"] is False
    assert report["work_items"][3]["status"] == "NO_NEW_ADMISSIBLE_CASES"
    assert report["project_cost_eur"] == 0
    assert report["official_core_metrics_changed"] is False

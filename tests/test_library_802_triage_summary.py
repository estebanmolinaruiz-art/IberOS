import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def test_harvest_802_summary_keeps_evidence_gates_closed():
    d=json.loads((ROOT/"data/review/library_802_harvest_triage_summary_v1.json").read_text(encoding="utf-8"))
    assert d["source_metadata_records"]==d["unique_dois_within_run"]==802
    assert sum(d["triage"].values())==802
    assert d["scientific_articles_individually_read"]==0
    assert d["scientific_fiches_approved"]==0 and d["semantic_core_promotions"]==0
    assert d["review_stage"]=="PRELIMINARY_AUTOMATIC_TRIAGE_COMPLETED_EDITORIAL_PENDING"

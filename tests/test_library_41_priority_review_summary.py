"""Keep bibliographic title screening distinct from scientific approval."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def test_library_priority_review_reconciles_41():
    d=json.loads((ROOT/"data/review/library_41_priority_review_summary_v1.json").read_text(encoding="utf-8"))
    assert sum(d["levels"].values())==d["reviewed_candidate_metadata"]==41
    assert len(d["verified_dois"])==d["levels"]["verified_journal_metadata"]==2
    assert d["source_documents_read"]==d["scientifically_approved_epigraphic_fiches"]==0
    assert d["automatic_core_promotion"] is False

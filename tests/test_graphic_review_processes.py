"""Reproducible non-promoting review check suite."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
from audit_graphic_review_processes import audit

def test_ten_graphic_review_controls_pass():
    result=audit()
    assert result["total"]==10
    assert result["passed"]==10
    assert result["checked_records"]==9
    assert result["checked_objects"]==3
    assert result["scientific_translations_validated"]==0

def test_graphic_audit_corpus_alignment():
    import json
    review=ROOT/"data/review"
    sources=[review/"casinos_graphic_uncertainties_v1.json",review/"sagunto_caminreal_graphic_uncertainties_v1.json"]
    observations=[r for f in sources for r in json.loads(f.read_text(encoding="utf-8"))["records"]]
    editorial=[json.loads(x) for x in (review/"editorial_readings_pending_v1.jsonl").read_text(encoding="utf-8").splitlines() if x.strip()]
    assert {r["object_id"] for r in observations}=={r["object_id"] for r in editorial}
    assert len({(r["object_id"],r["region"]) for r in observations})==len(observations)
    assert audit()["checks"]["P10_corpus_coverage"]

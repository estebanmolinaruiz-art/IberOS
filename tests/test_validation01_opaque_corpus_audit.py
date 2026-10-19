import importlib.util,csv
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location("opaque",ROOT/"scripts/validation01_opaque_corpus_audit.py")
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
def test_staged_opaque_batch_no_fabricated_labels():
    with (ROOT/"data/review/validation01_external_opaque_readings_batch01.csv").open(encoding="utf8",newline="") as f:r=list(csv.DictReader(f))
    s=m.audit(r)
    assert s["status"]=="PASS"
    assert s["records_staged"]==12
    assert s["holdout_cases"]==s["decoded_atomic_inscriptions"]==0
def test_opaque_promote_blocked():
    a={"source_id":"I00001","editorial_id":"x","support":"plom","source_url":"https://cathalaunia.org/Iberika/I00001",
        "source_encoded_excerpt":"ABC","encoding":"CUSTOM_FONT_OPAQUE","reading_status":"REVIEWED","te_status":"PRESENT","prospective_eligible":"YES"}
    assert m.audit([a])["status"]=="BLOCKED"

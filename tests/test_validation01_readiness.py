import csv,json,importlib.util
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
s=importlib.util.spec_from_file_location("v01ready",ROOT/"scripts/validation01_readiness.py")
m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
def test_real_files_block():
 p=json.loads((ROOT/"data/review/validation01_preregistration_v1.json").read_text())
 r=m.evaluate(m.load(ROOT/"data/review/validation01_te_tokenized_review_v1.csv"),
              m.load(ROOT/"data/review/validation01_holdout_v1.csv"),p)
 assert r["gate"]=="BLOCKED"
 assert r["result"]=="NOT_EVALUATED"
 assert "NO_HOLD_RECORDS" in r["blockers"]
 assert "PREREGISTRATION_INCOMPLETE" in r["blockers"]
def test_fabricated_te_detection_not_validation():
 p={"target_definition":"PENDING"}
 r=m.evaluate([{"te_status":"1","reading_status":"RAW_UNREVIEWED"}],[],p)
 assert "UNREVIEWED_TE_CLASSIFICATION" in r["blockers"]

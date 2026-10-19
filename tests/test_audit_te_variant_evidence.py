import importlib.util,csv
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
s=importlib.util.spec_from_file_location("te15",ROOT/"scripts/audit_te_variant_evidence.py")
m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
def test_actual_te_variant_staging():
 with (ROOT/"data/review/te_variant_evidence_15_v1.csv").open() as f:rows=list(csv.DictReader(f))
 result=m.audit(rows)
 assert result["status"]=="PASS_STAGING"
 assert result["records"]==15 and result["verified_glyphs"]==0
def test_premature_activation_rejected():
 with (ROOT/"data/review/te_variant_evidence_15_v1.csv").open() as f:rows=list(csv.DictReader(f))
 rows[0]["activation_status"]="VERIFIED"
 assert m.audit(rows)["status"]=="BLOCKED"

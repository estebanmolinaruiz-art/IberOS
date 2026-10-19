import importlib.util,csv
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location("audit_signary",ROOT/"scripts"/"audit_cathalaunia_signary.py")
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
def test_source_label_concordance():
 s=m.read(ROOT/"data/review/cathalaunia_signary_source_codes_v5_2026-10-19.csv")
 c=m.read(ROOT/"data/review/cathalaunia_signary_review_queue_286_v2.csv")
 r=m.audit(s,c)
 assert r["status"]=="PASS_SOURCE_METADATA"
 assert r["source_records"]==r["candidate_records"]==286
 assert r["classes"]["SIMPLE_SOURCE_LABEL"]==133
 assert r["glyphs_visually_verified"]==0
def test_mismatch_is_blocked():
 s=[{"unicode_decimal":"101","source_variant_label":"te13"}]
 c=[{"unicode_decimal":"101","source_variant_label":"te1","review_queue":"SIMPLE_SOURCE_LABEL","source_value_candidate":"te","usable_for_auto_reading":"NO","independent_review":"PENDING"}]
 assert m.audit(s,c)["status"]=="BLOCKED"
def test_promotion_is_blocked():
 s=[{"unicode_decimal":"101","source_variant_label":"te13"}]
 c=[{"unicode_decimal":"101","source_variant_label":"te13","review_queue":"SIMPLE_SOURCE_LABEL","source_value_candidate":"te","usable_for_auto_reading":"YES","independent_review":"PENDING"}]
 assert m.audit(s,c)["status"]=="BLOCKED"

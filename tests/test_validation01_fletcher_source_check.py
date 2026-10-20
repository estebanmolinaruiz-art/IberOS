import importlib.util,csv
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
s=importlib.util.spec_from_file_location("src",ROOT/"scripts/validation01_fletcher_source_check.py")
m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
def test_source_editorial_diff_only():
 with (ROOT/"data/review/validation01_fletcher_critical_passages_source_checked.csv").open() as f:rows=list(csv.DictReader(f))
 r=m.check(rows)
 assert r["gate"]=="PASS_EDITORIAL_ONLY" and r["index_zero_based"]==5
 assert r["scientific_verdict"]=="NOT_EVALUATED"
def test_no_hold_or_false_visual_certification():
 with (ROOT/"data/review/validation01_fletcher_critical_passages_source_checked.csv").open() as f:rows=list(csv.DictReader(f))
 rows[0]["split"]="HOLD"
 assert m.check(rows)["gate"]=="BLOCKED"
 rows[0]["split"]="DEVELOPMENT";rows[0]["visual_glyphs_verified"]="9"
 assert m.check(rows)["gate"]=="BLOCKED"

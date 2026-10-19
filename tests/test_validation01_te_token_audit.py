import importlib.util
from pathlib import Path
p=Path(__file__).resolve().parents[1]/"scripts"/"validation01_te_token_audit.py"
s=importlib.util.spec_from_file_location("te_check",p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
def row(**kw):
 r=dict(object_id="T1",physical_group="P1",source_url="https://example.org/source",edition_locator="p.1 line 2",
 signary="NE",sign_tokens="a te r",reading_status="REVIEWED",full_line_reviewed="YES",
 independent_reviewer="external",cohort="DEVELOPMENT");r.update(kw);return r
def test_positive_atomic_te(): assert m.inspect([row()])["results"][0]["te_status"]=="PRESENT"
def test_te_not_substring(): assert m.inspect([row(sign_tokens="ta e")])["results"][0]["te_status"]=="ABSENT_IN_REVIEWED_LINE"
def test_lacuna_abstention(): assert m.inspect([row(sign_tokens="a te ?")])["results"][0]["te_status"]=="UNKNOWN"
def test_unreviewed_absence_abstention(): assert m.inspect([row(sign_tokens="a r",reading_status="UNREVIEWED")])["results"][0]["te_status"]=="UNKNOWN"
def test_hold_is_rejected(): assert m.inspect([row(cohort="HOLD")])["status"]=="ERROR"
def test_concat_is_not_tokenization(): assert m.inspect([row(sign_tokens="ater")])["status"]=="ERROR"

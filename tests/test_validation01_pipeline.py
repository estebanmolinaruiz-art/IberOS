import importlib.util
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
s=importlib.util.spec_from_file_location("v01_pipeline",ROOT/"scripts/validation01_pipeline.py")
m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
def test_current_corpus_requires_hold_and_review():
 r=m.run()
 assert r["pipeline_gate"]=="BLOCKED"
 assert r["readiness"]["hold_rows"]==0
 assert r["readiness"]["reviewed_atomic_lines"]==0
 assert r["scientific_verdict"]=="NOT_EVALUATED"
 assert r["hold_scoring_gate"]=="BLOCKED"

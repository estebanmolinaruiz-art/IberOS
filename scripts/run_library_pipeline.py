#!/usr/bin/env python3
"""Run the complete safe metadata-to-screening pipeline, with consistency checks."""
import json
import subprocess
import sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/"site"/"data"
def main():
    for script in ("build_bibliographic_fichas.py","audit_epigraphic_extractions.py","screen_epigraphic_candidates.py"):
        subprocess.run([sys.executable,str(ROOT/"scripts"/script)],cwd=ROOT,check=True)
    library=json.loads((DATA/"library_candidates_v1.json").read_text(encoding="utf-8"))["items"]
    fichas=json.loads((DATA/"bibliographic_fichas_v1.json").read_text(encoding="utf-8"))["items"]
    candidates=json.loads((DATA/"epigraphic_extraction_candidates_v1.json").read_text(encoding="utf-8"))["items"]
    audit=json.loads((DATA/"epigraphic_extraction_audit_v1.json").read_text(encoding="utf-8"))["items"]
    screening=json.loads((DATA/"epigraphic_screening_v1.json").read_text(encoding="utf-8"))["items"]
    assert len(fichas)<=len(library)
    assert len(candidates)==len(audit)==len(screening)
    assert {x["object_id"] for x in candidates}=={x["object_id"] for x in audit}
    assert all(not x["automatic_semantic_validation"] for x in audit)
    assert all(x["core_rules_executed"]==0 and x["automated_translation"] is None for x in screening)
    assert all(x["core_processing"]["status"]=="BLOCKED_UNVERIFIED_OBJECT" for x in fichas)
    print(f"Consistent pipeline: {len(fichas)} bibliographic fichas, {len(audit)} inscription audits; 0 semantic promotions")
if __name__=="__main__":
    main()

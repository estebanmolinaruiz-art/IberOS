#!/usr/bin/env python3
"""Gate newly identified epigraphic objects before scientific Core processing.

A bibliographic title is never an archaeological object or transcription.
"""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/"site"/"data"
REQUIRED=("object_id","source_doi","source_url","edition_figure","inventory_or_catalogue_id","transcription","reviewer","review_date")

def assess(item):
    missing=[field for field in REQUIRED if not isinstance(item.get(field),str) or not item[field].strip()]
    flags=("exact_object_match_verified","transcription_checked_against_edition","source_rights_checked","independent_review_completed")
    missing += [field for field in flags if item.get(field) is not True]
    return {"object_id":item.get("object_id"),"ready_for_core":not missing,
            "missing_requirements":missing,
            "core_status":"ELIGIBLE_FOR_CONTROLLED_REVIEW" if not missing else "BLOCKED_UNVERIFIED_EVIDENCE",
            "automatic_semantic_validation":False}

def build():
    source=DATA/"epigraphic_extraction_candidates_v1.json"
    records=json.loads(source.read_text(encoding="utf-8")).get("items",[])
    return {"schema":"IberOS-Epigraphic-Extraction-Audit/1.0",
            "items":[assess(item) for item in records],
            "note":"An eligible record requires controlled scientific review; it is not a validated translation."}

def main():
    target=DATA/"epigraphic_extraction_audit_v1.json"
    result=build()
    target.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(len(result["items"]),"candidate inscriptions audited; no automatic translation")
if __name__=="__main__":main()

#!/usr/bin/env python3
"""Create an auditable, non-interpretative screening report for extracted inscriptions."""
import json
from pathlib import Path
from audit_epigraphic_extractions import assess

DATA=Path(__file__).resolve().parents[1]/"site"/"data"
def build():
    queue=json.loads((DATA/"epigraphic_extraction_candidates_v1.json").read_text(encoding="utf-8"))
    rows=[]
    for item in queue.get("items",[]):
        gate=assess(item)
        variants=item.get("edition_readings",[])
        rows.append({"object_id":item.get("object_id"),"bibliographic_ficha_id":item.get("source_bibliographic_ficha_id"),
            "source_doi":item.get("source_doi"),"variant_count":len(variants),
            "attested_edition_variants":[{"reading":v.get("reading"),"role":v.get("role"),"citation_location":v.get("citation_location"),
                "review_status":v.get("review_status")} for v in variants],
            "missing_requirements":gate["missing_requirements"],"core_gate_status":gate["core_status"],
            "core_rules_executed":0,"automated_translation":None,
            "decision":"AWAIT_DOCUMENTARY_REVIEW" if not gate["ready_for_core"] else "AWAIT_CONTROLLED_CORE_RUN"})
    return {"schema":"IberOS-Extraction-Screening/1.0","items":rows,
      "notice":"A transcription variant is a documented hypothesis, not a validated translation. Core rules have not run in this screening."}
if __name__=="__main__":
    result=build()
    (DATA/"epigraphic_screening_v1.json").write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(len(result["items"]),"screened; no invented Core results")

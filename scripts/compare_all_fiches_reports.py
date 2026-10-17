#!/usr/bin/env python3
"""Run a non-promoting, reproducible cross-check for all editorial fiches."""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/"site"/"data"

def main():
    rows=[]
    for shard in range(1,6):
        rows.extend(json.loads((DATA/f"ficha-enrichment-{shard}.json").read_text(encoding="utf-8")))
    ids=[r["OBJECT_ID"] for r in rows]
    if len(ids)!=len(set(ids)):
        raise ValueError("Duplicate OBJECT_ID in enrichment shards")
    from iberos.core import load_registry
    registry={r["OBJECT_ID"]:r for r in load_registry()}
    if set(ids)!=set(registry):
        raise ValueError("Fiche enrichment and curated registry identifiers differ")
    featured=json.loads((DATA/"ficha-enrichment-featured.json").read_text(encoding="utf-8"))
    fmap={r["OBJECT_ID"]:r for r in featured}
    if len(fmap)!=len(featured) or not set(fmap).issubset(set(ids)):
        raise ValueError("Featured references invalid")
    result=[]
    for row in rows:
        oid=row["OBJECT_ID"]
        ref=row.get("citation","")
        fields={k:bool(isinstance(row.get(k),str) and row[k].strip()) for k in ("evidence","inference","hypothesis","limits","citation")}
        # Editorial prose is NOT an independently transcribed, signed-off epigraphic reading.
        result.append({
            "object_id":oid,
            "title":row.get("title",""),
            "citation_present":fields["citation"],
            "citation_is_external_primary_source_verified":False,
            "editorial_fields_complete":all(fields.values()),
            "editorial_fields":fields,
            "featured_in_public_selection":oid in fmap,
            "hypothesis_vs_report":"DOCUMENTARY_COMPARISON_ONLY",
            "reviewed_sign_transcription_available_in_this_input":False,
            "core_execution":"BLOCKED_MISSING_REVIEWED_TRANSCRIPTION",
            "agreement_with_report":"NOT_TESTABLE_FROM_EDITORIAL_PROSE",
            "conflict_with_report":"NOT_TESTABLE_FROM_EDITORIAL_PROSE",
            "new_semantic_inference":None,
            "translation_validated":False,
        })
    report={
        "schema":"IberOS-Whole-Corpus-Report-Comparison/1.0",
        "method":"Every curated fiche compared to available editorial fields; core semantic engine gated on independently reviewed transcriptions",
        "count":len(result),
        "cited_count":sum(x["citation_present"] for x in result),
        "editorial_complete_count":sum(x["editorial_fields_complete"] for x in result),
        "core_executed_count":0,
        "scientifically_validated_translations":0,
        "records":result,
    }
    out=DATA/"all_fiches_report_comparison_v1.json"
    out.write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(f"IBEROS ALL-FICHES: {report['count']} objects; {report['cited_count']} citations; {report['editorial_complete_count']} editorial-complete; 0 Core semantic executions (reviewed transcriptions absent)")
    assert report["count"]==38 and report["cited_count"]==38
    assert all(x["core_execution"]=="BLOCKED_MISSING_REVIEWED_TRANSCRIPTION" for x in result)

if __name__=="__main__":
    main()

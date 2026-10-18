#!/usr/bin/env python3
"""Run a non-promoting, reproducible cross-check for all editorial fiches."""
import json
import argparse
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/"site"/"data"

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--reviewed-readings', help='Optional JSONL of reviewed readings; no approval inferred from fiche prose')
    args=parser.parse_args()
    from iberos.library_readings_bridge import analyze_library_readings
    reading_reports={}
    if args.reviewed_readings:
        input_rows=[json.loads(line) for line in Path(args.reviewed_readings).read_text(encoding='utf-8-sig').splitlines() if line.strip()]
        review=analyze_library_readings(input_rows)
        for item in review['reports']:
            reading_reports.setdefault(item['object_id'],[]).append(item)
    graphic=json.loads((ROOT/"data/review/casinos_graphic_uncertainties_v1.json").read_text(encoding="utf-8"))
    graphic_by_id={}
    for evidence in graphic["records"]:
        if evidence["sign_by_sign_verified"] or evidence["core_execution_allowed"] or evidence["meaning_validated"]:
            raise ValueError("Unreviewed graphic evidence must not be promoted")
        graphic_by_id.setdefault(evidence["object_id"],[]).append(evidence)
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
        evaluated=reading_reports.get(oid,[])
        approved=[x for x in evaluated if x["review_gate_passed"]]
        pending=[x for x in evaluated if not x["review_gate_passed"]]
        result.append({
            "object_id":oid,
            "title":row.get("title",""),
            "citation_present":fields["citation"],
            "citation_is_external_primary_source_verified":False,
            "editorial_fields_complete":all(fields.values()),
            "editorial_fields":fields,
            "featured_in_public_selection":oid in fmap,
            "hypothesis_vs_report":"DOCUMENTARY_COMPARISON_ONLY",
            "graphic_uncertainty_count":len(graphic_by_id.get(oid,[])),
            "graphic_uncertainties":[{"evidence_id":e["evidence_id"],"region":e["region"],"location":e["location"],"alternatives":e["editorial_alternatives"],"review_status":e["review_status"],"sign_by_sign_verified":False} for e in graphic_by_id.get(oid,[])],
            "editorially_approved_reading_in_input":bool(approved),
            "independently_verified_sign_transcription":False,
            "core_execution":"NON_PROMOTING_DOMAIN_SUGGESTIONS" if approved else "BLOCKED_MISSING_APPROVED_READING",
            "editorially_approved_reading_count":len(approved),
            "pending_editorial_readings":[{
                "reading_id":p["reading_id"],
                "review_reference":next((source.get("review_reference") for source in input_rows if source.get("reading_id")==p["reading_id"]),None) if args.reviewed_readings else None,
                "editorial_transcription":next((source.get("editorial_transcription") for source in input_rows if source.get("reading_id")==p["reading_id"]),None) if args.reviewed_readings else None,
                "uncertainties":next((source.get("uncertainties",[]) for source in input_rows if source.get("reading_id")==p["reading_id"]),[]) if args.reviewed_readings else [],
                "scientific_reading_status":"PENDING_GRAPHIC_REVIEW"
            } for p in pending],
            "semantic_domain_suggestions":[z for reading in approved for z in reading["suggestions"]],
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
        "graphic_uncertainty_count":sum(x["graphic_uncertainty_count"] for x in result),
        "pending_readings_count":sum(len(x["pending_editorial_readings"]) for x in result),
        "core_executed_count":sum(x["core_execution"]=="NON_PROMOTING_DOMAIN_SUGGESTIONS" for x in result),
        "scientifically_validated_translations":0,
        "records":result,
    }
    out=DATA/"all_fiches_report_comparison_v1.json"
    out.write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(f"IBEROS ALL-FICHES: {report['count']} objects; {report['cited_count']} citations; {report['editorial_complete_count']} editorial-complete; {report['core_executed_count']} non-promoting semantic-domain evaluations")
    assert report["count"]==38 and report["cited_count"]==38
    assert all(not x["translation_validated"] and x["new_semantic_inference"] is None for x in result)
    assert all(not x["independently_verified_sign_transcription"] for x in result)

if __name__=="__main__":
    main()

#!/usr/bin/env python3
"""Export conservative per-object CORE audit for the static IberOS website."""
from __future__ import annotations
import json
from pathlib import Path
from iberos.core import load_registry, AUTHORITY
from iberos.object_rule_audit import audit_object_rules
from iberos.rule_catalog import rule_catalog
from iberos.reviewed_observations import evaluate_reviewed_observations
from iberos.evidence_triage import build_evidence_triage
from iberos.publication_gate import build_publication_manifest
from iberos.documentary_evidence import build_documentary_evidence
from iberos.publication_priority import build_publication_priority

def build(observations=None):
    evaluations = evaluate_reviewed_observations(observations if observations is not None else [])
    objects = {}
    for item in load_registry():
        oid = item["OBJECT_ID"]
        report = audit_object_rules(oid)
        objects[oid] = {
            "object_id": oid,
            "families_tagged": report["families_tagged"],
            "modules": report["modules"],
            "rules": report["rules"],
            "evaluated_rules": evaluations.get(oid, []),
            "scientific_state": "UNVERIFIED",
            "automatic_core_promotion": False,
        }
    return {"schema":"IberOS-Web-Core-Audit/1.0",
            "authority":dict(AUTHORITY),
            "source":"src/iberos/object_rule_audit.py",
            "evaluation_policy":"REVIEWED_SOURCED_OBSERVATIONS_ONLY",
            "object_count":len(objects),"objects":objects,
            "notice":"Reglas candidatas y controles; no hay traducciones verificadas automáticamente."}

def main():
    target=Path("site/data/core_object_audit_v1.json")
    target.parent.mkdir(parents=True,exist_ok=True)
    target.write_text(json.dumps(build(),ensure_ascii=False,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    # Reuse actual existing editorial hypotheses; do not claim semantic verification.
    featured_path=Path("site/data/ficha-enrichment-featured.json")
    featured=json.loads(featured_path.read_text(encoding="utf-8")) if featured_path.exists() else []
    # Merge existing curated fiche shards, keeping featured entries authoritative.
    (target.parent/"featured_documentary_review_v1.json").write_text(json.dumps(build_documentary_evidence(featured),ensure_ascii=False,indent=2,sort_keys=True)+chr(10),encoding="utf-8")
    featured_ids={item.get("OBJECT_ID") for item in featured}
    for shard in range(1,6):
        source=Path(f"site/data/ficha-enrichment-{shard}.json")
        if not source.exists():
            continue
        for item in json.loads(source.read_text(encoding="utf-8")):
            if item.get("OBJECT_ID") in featured_ids:
                continue
            if all(isinstance(item.get(k),str) and item[k].strip() for k in ("hypothesis","evidence","limits","citation")):
                featured.append(item)
                featured_ids.add(item["OBJECT_ID"])
    interpretations={x["OBJECT_ID"]:{"candidates":[],"translation_validated":False,
                                      "status":"AWAITING_DOCUMENTED_HYPOTHESES"} for x in load_registry()}
    (target.parent/"fiche_publication_priority_v1.json").write_text(json.dumps(build_publication_priority(featured),ensure_ascii=False,indent=2,sort_keys=True)+chr(10),encoding="utf-8")
    (target.parent/"fiche_publication_status_v1.json").write_text(json.dumps(build_publication_manifest(featured),ensure_ascii=False,indent=2,sort_keys=True)+chr(10),encoding="utf-8")
    for item in featured:
        oid=item.get("OBJECT_ID")
        if oid.startswith("IBR-CTL-") or oid=="IBR-COI-0002":
            continue
        if oid not in interpretations or not all(isinstance(item.get(k),str) and item[k].strip() for k in ("hypothesis","limits","evidence")):
            continue
        # Some original fichas have an empty suggested citation but contain
        # bibliographic references. Retain actual sources without fabricating a citation.
        citation = item.get("citation", "").strip()
        bibliography = [ref.strip() for ref in item.get("bibliography", []) if isinstance(ref, str) and ref.strip()]
        sources = [citation] if citation else bibliography
        if not sources:
            continue
        interpretations[oid]["candidates"].append({
            "id":"EDITORIAL-FEATURED-01",
            "possible_translation":item["hypothesis"],
            "sources":sources,
            "supporting_observations":[item["evidence"]],
            "objections":[item["limits"]],
            "epistemic_layer":"HYPOTHESIS",
            "meaning_validated":False,
            "reading_verified_independently":False,
            "provenance":"EXISTING_FEATURED_FICHA_EDITORIAL",
            "estimated_probability":None,
        })
        interpretations[oid]["status"]="EXISTING_EDITORIAL_HYPOTHESIS_UNVERIFIED"
    interpretation_feed={"schema":"IberOS-Interpretation-Web/1.0",
                         "authority":dict(AUTHORITY),"object_count":len(interpretations),
                         "objects":interpretations,
                         "notice":"Se muestran hipótesis editoriales existentes; ninguna traducción validada automáticamente."}
    (target.parent/"core_interpretations_v1.json").write_text(json.dumps(interpretation_feed,ensure_ascii=False,indent=2,sort_keys=True)+chr(10),encoding="utf-8")
    # Bibliographic page checked externally; inscription-level reading still blocked.
    source_check_path=Path("data/review/epigraphic_source_verification_2026-10-16.json")
    if source_check_path.exists():
        source_checks=json.loads(source_check_path.read_text(encoding="utf-8"))
        assert source_checks["schema"]=="IberOS-Source-Verification/1.0"
        assert all(row["semantic_analysis_eligible"] is False for row in source_checks["checks"])
        (target.parent/"epigraphic_source_verification_v1.json").write_text(
            json.dumps(source_checks,ensure_ascii=False,indent=2,sort_keys=True)+chr(10),encoding="utf-8")
    # Existing edition readings are review candidates, never approved CORE inputs.
    extraction_path=Path("site/data/epigraphic_extraction_candidates_v1.json")
    extraction=json.loads(extraction_path.read_text(encoding="utf-8")) if extraction_path.exists() else {"items":[]}
    reading_queue=[]
    for entry in extraction.get("items",[]):
        for idx,variant in enumerate(entry.get("edition_readings") or []):
            if not isinstance(variant,dict) or not isinstance(variant.get("reading"),str) or not variant["reading"].strip():
                continue
            reading_queue.append({
                "source_object_id":entry.get("object_id"),
                "candidate_reading_id":str(entry.get("object_id"))+"-ED-"+str(idx+1),
                "reading":variant["reading"],"attribution":variant.get("attribution"),
                "citation_location":variant.get("citation_location"),
                "curated_object_id":None,
                "exact_object_match_verified":False,
                "transcription_checked_against_edition":False,
                "eligible_for_core_execution":False,
                "review_status":"SECONDARY_READING_UNVERIFIED",
            })
    queue={"schema":"IberOS-Editorial-Readings-Queue/1.0",
           "count":len(reading_queue),"records":reading_queue,
           "automatic_core_promotion":False,
           "notice":"Lecturas editoriales preexistentes pendientes de cotejo; no entran en CORE."}
    (target.parent/"editorial_readings_review_v1.json").write_text(json.dumps(queue,ensure_ascii=False,indent=2,sort_keys=True)+chr(10),encoding="utf-8")
    (target.parent/"core_evidence_triage_v1.json").write_text(json.dumps(build_evidence_triage(),ensure_ascii=False,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    (target.parent/"core_rule_catalog_v1.json").write_text(json.dumps(rule_catalog(),ensure_ascii=False,indent=2,sort_keys=True)+"\n",encoding="utf-8")

if __name__=="__main__":
    main()

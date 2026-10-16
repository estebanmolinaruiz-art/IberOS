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
    interpretations={x["OBJECT_ID"]:{"candidates":[],"translation_validated":False,
                                      "status":"AWAITING_DOCUMENTED_HYPOTHESES"} for x in load_registry()}
    for item in featured:
        oid=item.get("OBJECT_ID")
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
    (target.parent/"core_evidence_triage_v1.json").write_text(json.dumps(build_evidence_triage(),ensure_ascii=False,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    (target.parent/"core_rule_catalog_v1.json").write_text(json.dumps(rule_catalog(),ensure_ascii=False,indent=2,sort_keys=True)+"\n",encoding="utf-8")

if __name__=="__main__":
    main()

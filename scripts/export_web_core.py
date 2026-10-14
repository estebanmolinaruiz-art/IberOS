#!/usr/bin/env python3
"""Export conservative per-object CORE audit for the static IberOS website."""
from __future__ import annotations
import json
from pathlib import Path
from iberos.core import load_registry, AUTHORITY
from iberos.object_rule_audit import audit_object_rules
from iberos.rule_catalog import rule_catalog
from iberos.reviewed_observations import evaluate_reviewed_observations

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
    (target.parent/"core_rule_catalog_v1.json").write_text(json.dumps(rule_catalog(),ensure_ascii=False,indent=2,sort_keys=True)+"\n",encoding="utf-8")

if __name__=="__main__":
    main()

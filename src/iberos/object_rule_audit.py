"""Evidence-aware rule applicability report for curated IberOS objects.

Applicability != rule success and family-tag matches are not transcriptions.
"""
from __future__ import annotations
from .core import get_object, AUTHORITY
from .rule_catalog import rule_catalog
from .multimodule import research_pipeline

def audit_object_rules(object_id: str) -> dict:
    obj = get_object(object_id)
    if obj is None:
        raise ValueError("Unknown OBJECT_ID")
    tags = {v.strip().upper() for v in (obj.get("Familias_Tags") or "").split(";") if v.strip()}
    catalogue = rule_catalog()
    matching = []
    for rule in catalogue["entries"]:
        family = rule.get("family")
        # Family metadata is a screening aid, never direct attestation.
        if family:
            tokens = set(family.split("_"))
            related = family in tags or bool(tokens.intersection(tags))
            state = "CANDIDATE_FROM_REGISTRY_TAGS" if related else "NOT_EVALUATED_FOR_OBJECT"
        else:
            state = "GENERAL_GUARD_AVAILABLE" if rule["kind"] == "ACTIVE_GUARD" else "NOT_EVALUATED_FOR_OBJECT"
        matching.append({"id":rule["id"],"family":family,"applicability":state,
                         "rule_passed":None,"evidence_verified":False,
                         "semantic_translation_verified":False})
    pipeline=research_pipeline(object_id)
    return {"object_id":object_id,"source":"data/curated/iberos_objects_registry_v2.0.csv",
            "families_tagged":sorted(tags),"rules":matching,
            "modules":{k:v["state"] for k,v in pipeline["modules"].items()},
            "authority":dict(AUTHORITY),"automatic_core_promotion":False,
            "notice":"Family tags identify review candidates; no epigraphic reading or prediction is confirmed."}

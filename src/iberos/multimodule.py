"""Conservative multi-module orchestration for an IberOS object.

A module being represented in the output is not a claim of autonomous
linguistic decoding. GEO is context-only, INFER never promotes claims.
"""
from __future__ import annotations
from typing import Any
from .core import get_object, rhotic_search_key, AUTHORITY
from .geo import geo_context
from .rule_catalog import rule_catalog

MODULES = ("GEO", "PALEO", "MORPH", "LEXSEM", "TRACE", "INFER")

def research_pipeline(object_id: str) -> dict[str, Any]:
    item = get_object(object_id)
    if item is None:
        raise ValueError("Unknown OBJECT_ID")
    tags = {x.strip() for x in (item.get("Modulos_Activos") or "").split(";") if x.strip()}
    evidence = {
        "object_id": object_id,
        "authority": dict(AUTHORITY),
        "source": "data/curated/iberos_objects_registry_v2.0.csv",
        "modules": {
            "GEO": {"state": "CONTEXT_ONLY", "result": geo_context(object_id)},
            "PALEO": {"state": "METADATA_ONLY", "active_in_registry": "PALEO" in tags,
                      "paleo_status": item.get("PALEO_Status", "")},
            "MORPH": {"state": "REGISTRY_TAG_ONLY", "active_in_registry": "MORPH" in tags,
                      "family_tags": item.get("Familias_Tags", "")},
            "LEXSEM": {"state": "HYPOTHESES_NOT_TRANSLATION", "active_in_registry": "LEXSEM" in tags,
                       "catalogued_rules": rule_catalog()["counts"]["documented_entries"]},
            "TRACE": {"state": "DOCUMENTARY_METADATA", "dependency_group": item.get("Dependency_Group", ""),
                      "inclusion": item.get("IberOS_Inclusion", "")},
            "INFER": {"state": "PENDING_INDEPENDENT_VALIDATION", "candidate_meaning": None,
                      "automatic_core_promotion": False},
        },
        "automatic_core_promotion": False,
        "geography_is_semantic_evidence": False,
    }
    return evidence

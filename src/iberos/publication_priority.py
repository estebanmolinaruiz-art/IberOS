"""Deterministic editorial completion queue; never ranks truth of hypotheses."""
from __future__ import annotations
from .publication_gate import build_publication_manifest
from .core import load_registry, AUTHORITY

def build_publication_priority(featured: list[dict]) -> dict:
    manifest=build_publication_manifest(featured)
    reg={row["OBJECT_ID"]:row for row in load_registry()}
    tasks=[]
    for oid,state in manifest["records"].items():
        if state["publication_status"]=="PUBLICABLE_EDITORIAL":
            continue
        pending=state["pending_documentation"]
        tasks.append({
            "object_id":oid,
            "object_name":reg[oid].get("Nombre_objeto") or oid,
            "pending_documentation":pending,
            "pending_count":len(pending),
            "editorial_fiche_registered":state["editorial_fiche_registered"],
            "priority_basis":"FEWEST_DECLARED_EDITORIAL_GAPS_ONLY",
            "scientific_state":"UNVERIFIED",
            "automatic_core_promotion":False,
        })
    tasks.sort(key=lambda row:(row["pending_count"],not row["editorial_fiche_registered"],row["object_id"]))
    return {"schema":"IberOS-Publication-Priority/1.0","authority":dict(AUTHORITY),
            "pending_count":len(tasks),"tasks":tasks,
            "automatic_core_promotion":False,
            "notice":"Ordering reflects declared metadata completeness only; no claim of scientific readiness."}

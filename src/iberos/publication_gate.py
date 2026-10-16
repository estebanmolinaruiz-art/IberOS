"""Public fiche publication status, distinct from scientific validation."""
from __future__ import annotations
from .core import load_registry, AUTHORITY

def build_publication_manifest(featured: list[dict]) -> dict:
    if not isinstance(featured,list):
        raise ValueError("Expected editorial fiche list")
    registry={x["OBJECT_ID"]:x for x in load_registry()}
    by_id={}
    for item in featured:
        oid=item.get("OBJECT_ID") if isinstance(item,dict) else None
        if oid not in registry or oid in by_id:
            raise ValueError("Unknown or duplicate featured object")
        by_id[oid]=item
    records={}
    for oid,obj in registry.items():
        f=by_id.get(oid)
        editorial_complete=bool(f and all(isinstance(f.get(k),str) and f[k].strip() for k in ("hypothesis","evidence","limits","citation")))
        fiche_registered=bool(obj.get("Ficha_existente","").strip().lower() in {"sí","si","yes"})
        records[oid]={
            "object_id":oid,
            "publication_status":"PUBLICABLE_EDITORIAL" if editorial_complete and fiche_registered else "EDITORIAL_REVIEW_REQUIRED",
            "featured_interpretation_available":editorial_complete,
            "editorial_fiche_registered":fiche_registered,
            "translation_validated":False,
            "scientific_validation_status":"UNVERIFIED",
            "automatic_core_promotion":False,
        }
    return {"schema":"IberOS-Fiche-Publication/1.0","authority":dict(AUTHORITY),
            "object_count":len(records),"records":records,
            "notice":"Editorial publishability does not certify reading, meaning or original image rights."}

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
        is_documentary_control=oid.startswith("IBR-CTL-") or oid=="IBR-COI-0002"
        fiche_registered=bool(obj.get("Ficha_existente","").strip().lower() in {"sí","si","yes"})
        pending=[]
        if not fiche_registered:
            pending.append("Registrar y revisar la ficha documental de la pieza")
        if not f:
            pending.append("Preparar interpretación con evidencia y fuentes")
        else:
            labels={"hypothesis":"Redactar hipótesis interpretativa","evidence":"Vincular evidencia textual específica","limits":"Documentar incertidumbres y objeciones","citation":"Aportar cita editorial verificable"}
            for field,label in labels.items():
                if not isinstance(f.get(field),str) or not f[field].strip():
                    pending.append(label)
        verification={
            "bibliographic_reference_present":bool(f and (str(f.get("citation") or "").strip() or f.get("bibliography"))),
            "editorial_hypothesis_documented":editorial_complete and not is_documentary_control,
            "reading_compared_with_original_edition":False,
            "independent_epigraphic_review_completed":False,
            "image_rights_verified":False,
            "original_3d_model_rights_verified":False,
        }
        verification_pending=[
            "Cotejar transcripción con edición o facsímil original",
            "Registrar revisión epigráfica independiente",
            "Verificar licencia y atribución de imágenes",
            "Comprobar licencia y procedencia del modelo 3D antes de integrarlo",
        ]
        records[oid]={
            "object_id":oid,
            "publication_status":("DOCUMENTARY_CONTROL_AVAILABLE" if is_documentary_control and editorial_complete and fiche_registered else "DOCUMENTARY_CONTROL_REVIEW" if is_documentary_control else "PUBLICABLE_EDITORIAL" if editorial_complete and fiche_registered else "EDITORIAL_REVIEW_REQUIRED"),
            "featured_interpretation_available":editorial_complete and not is_documentary_control,
            "documentary_control":is_documentary_control,
            "editorial_fiche_registered":fiche_registered,
            "pending_documentation":pending,
            "scientific_documentation_checklist":verification,
            "scientific_documentation_pending":verification_pending,
            "translation_validated":False,
            "scientific_validation_status":"UNVERIFIED",
            "automatic_core_promotion":False,
        }
    return {"schema":"IberOS-Fiche-Publication/1.0","authority":dict(AUTHORITY),
            "object_count":len(records),"records":records,
            "notice":"Editorial publishability does not certify reading, meaning or original image rights."}

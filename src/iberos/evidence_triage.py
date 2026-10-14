"""Prioritize curatorial review without manufacturing epigraphic observations."""
from __future__ import annotations
from .core import load_registry, AUTHORITY

TARGETS = {
    "ROK": ("ROK-DIRECTION-GUARD-01",),
    "SALIR": ("SALIR-PROSPECTIVE-01",),
    "BI": ("BI-DISAMBIG-01",),
    "BIN": ("BI-DISAMBIG-01",),
    "KA": ("KA-DIRECTION-PROSPECTIVE-01",),
    "KU": ("KA-DIRECTION-PROSPECTIVE-01",),
    "KA_KE_KU": ("KA-DIRECTION-PROSPECTIVE-01",),
}

def build_evidence_triage() -> dict:
    tasks = []
    for obj in load_registry():
        tags = {t.strip().upper() for t in (obj.get("Familias_Tags") or "").split(";") if t.strip()}
        rules = sorted({r for tag in tags for r in TARGETS.get(tag, ())})
        if not rules:
            continue
        tasks.append({
            "object_id": obj["OBJECT_ID"],
            "reference": obj.get("Referencia_epigráfica") or "",
            "editorial_source": obj.get("Fuente") or "",
            "source_verified_for_rule": False,
            "candidate_rule_ids": rules,
            "review_status": "NEEDS_EXACT_PASSAGE_AND_INDEPENDENT_CHECK",
            "required_evidence": [
                "Exact diplomatic transcription and reading variants",
                "Passage-to-rule match confirmed by reviewer",
                "Physical object and documentary independence",
                "Explicit external anchor for semantic or directional inference",
            ],
            "eligible_for_technical_execution": False,
            "automatic_core_promotion": False,
        })
    return {"schema":"IberOS-Evidence-Triage/1.0", "authority":dict(AUTHORITY),
            "object_count":len(tasks), "tasks":tasks,
            "notice":"Corpus family tags route verification work only; they are not observations."}

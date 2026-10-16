"""Suggest bounded semantic *domains* from reviewer-supplied epigraphic segments.

Never infer a full translation or identify sign readings from unrestricted text.
"""
from __future__ import annotations
from .core import AUTHORITY, get_object

DOMAIN_RULES = {
    "ROK": ("ROK-DIRECTION-GUARD-01", "transfer-related function; direction unknown"),
    "SALIR": ("SALIR-PROSPECTIVE-01", "economic/value domain under test"),
    "KUTUR": ("KUTUR-PROSPECTIVE-01", "writing/formulary domain under test"),
    "BI": ("BI-DISAMBIG-01", "numeral candidate only with independent quantitative context"),
    "BIN": ("BI-DISAMBIG-01", "numeral candidate only with independent quantitative context"),
}
def suggest_semantic_domains(object_id: str, segments: list[dict]) -> dict:
    if get_object(object_id) is None:
        raise ValueError("Unknown curated object")
    if not isinstance(segments, list) or len(segments) > 500:
        raise ValueError("Expected at most 500 documented segments")
    suggestions=[]
    for index,segment in enumerate(segments):
        if not isinstance(segment,dict):
            raise ValueError("Each segment must be an object")
        form=segment.get("form")
        ref=segment.get("reading_source")
        if not isinstance(form,str) or not form.strip() or not isinstance(ref,str) or not ref.strip():
            raise ValueError("Documented form and reading_source are mandatory")
        if segment.get("reading_reviewed") is not True:
            continue
        normalized=form.strip().upper()
        if normalized not in DOMAIN_RULES:
            continue
        rule,domain=DOMAIN_RULES[normalized]
        if normalized in ("BI","BIN") and segment.get("independently_quantitative") is not True:
            domain="meaning unresolved; no numeral without independent quantitative evidence"
        suggestions.append({
            "segment_index":index,"attested_form":form,"source":ref,
            "candidate_rule":rule,"possible_domain":domain,
            "epistemic_layer":"HYPOTHESIS","meaning_validated":False,
            "independent_semantic_anchor_verified":False,
            "translation_fragment":None,
        })
    return {"schema":"IberOS-Semantic-Domain-Suggestions/1.0",
            "object_id":object_id,"authority":dict(AUTHORITY),
            "suggestions":suggestions,
            "possible_full_translation":None,
            "translation_validated":False,
            "automatic_core_promotion":False}

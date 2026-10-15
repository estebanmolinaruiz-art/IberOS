"""Rank explicitly documented possible meanings without inventing translations.

Ranking measures documentary completeness, NOT probability that a meaning is true.
"""
from __future__ import annotations
from .core import get_object, AUTHORITY

def compare_interpretations(object_id: str, reading: dict, proposals: list[dict]) -> dict:
    if get_object(object_id) is None:
        raise ValueError("Unknown curated object")
    if not isinstance(reading, dict) or not isinstance(reading.get("transcription"), str) or not reading["transcription"].strip() or not isinstance(reading.get("source"), str) or not reading["source"].strip():
        raise ValueError("Explicit sourced transcription required")
    if not isinstance(proposals, list) or len(proposals)>30:
        raise ValueError("Expected up to 30 hypotheses")
    output=[]
    ids=set()
    for p in proposals:
        if not isinstance(p,dict) or not isinstance(p.get("id"),str) or not p["id"].strip() or p["id"] in ids:
            raise ValueError("Hypotheses require distinct identifiers")
        ids.add(p["id"])
        gloss=p.get("possible_translation")
        if not isinstance(gloss,str) or not gloss.strip():
            raise ValueError("Nonempty possible_translation required")
        sources=p.get("sources")
        if not isinstance(sources,list) or not sources or any(not isinstance(x,str) or not x.strip() for x in sources):
            raise ValueError("Hypothesis sources required")
        objections=p.get("objections")
        if not isinstance(objections,list) or any(not isinstance(x,str) for x in objections):
            raise ValueError("Explicit objections list required")
        supporting=p.get("supporting_observations")
        if not isinstance(supporting,list) or any(not isinstance(x,str) for x in supporting):
            raise ValueError("Explicit supporting observations required")
        output.append({
            "id":p["id"],
            "possible_translation":gloss.strip(),
            "sources":sources,
            "supporting_observations":supporting,
            "objections":objections,
            "epistemic_layer":"HYPOTHESIS",
            "meaning_validated":False,
            "documentary_completeness":sum((bool(sources),bool(supporting),bool(objections))),
            "estimated_probability":None,
        })
    output.sort(key=lambda x:(-x["documentary_completeness"],x["id"]))
    return {"schema":"IberOS-Interpretation-Candidates/1.0","object_id":object_id,
            "transcription":reading["transcription"],"transcription_source":reading["source"],
            "reading_verified_independently":False,
            "candidates":output,"authority":dict(AUTHORITY),
            "automatic_core_promotion":False,
            "translation_validated":False,
            "notice":"Documentary completeness is not semantic confidence; no translation is inferred."}

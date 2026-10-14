"""Execute frozen, non-promoting IberOS rules on explicitly supplied observations.

No automatic identification of BI or ROK from free-text inscriptions.
"""
from __future__ import annotations
from .core import evaluate_bi_context, rok_semantic_guard, validate_rhotic_usage, evaluate_ka_direction_candidate, KA_DIRECTION_CANDIDATES, AUTHORITY

def execute_rules(observation: dict) -> dict:
    if not isinstance(observation, dict):
        raise ValueError("Expected observation dictionary")
    if not isinstance(observation.get("source_reference"), str) or not observation["source_reference"].strip():
        raise ValueError("A source_reference is mandatory")
    requested = observation.get("rules", [])
    if not isinstance(requested, list) or any(r not in {"BI-DISAMBIG-01", "ROK-DIRECTION-GUARD-01", "PALEO-RHOTIC-LOCK-01", "KA-DIRECTION-PROSPECTIVE-01"} for r in requested):
        raise ValueError("Only registered executable rules are allowed")
    results = []
    for name in dict.fromkeys(requested):
        if name == "BI-DISAMBIG-01":
            quant = observation.get("independently_quantitative")
            verbal = observation.get("verbal_complex")
            if type(quant) is not bool or type(verbal) is not bool:
                results.append({"rule":name,"status":"BLOCKED","missing":["independently_quantitative","verbal_complex"],
                                "rule_result":None})
            elif quant and not observation.get("quantitative_source_reference"):
                results.append({"rule":name,"status":"BLOCKED","missing":["quantitative_source_reference"],
                                "rule_result":None})
            else:
                results.append({"rule":name,"status":"EVALUATED_NOT_SEMANTICALLY_VERIFIED","missing":[],
                                "rule_result":evaluate_bi_context(independently_quantitative=quant,verbal_complex=verbal)})
        elif name == "PALEO-RHOTIC-LOCK-01":
            purpose, neutralized = observation.get("rhotic_purpose"), observation.get("rhotic_neutralized")
            if not isinstance(purpose, str) or not purpose.strip() or type(neutralized) is not bool:
                results.append({"rule":name,"status":"BLOCKED","missing":["rhotic_purpose","rhotic_neutralized"],"rule_result":None})
            else:
                result = validate_rhotic_usage(purpose=purpose,neutralized=neutralized)
                results.append({"rule":name,"status":"EVALUATED_NOT_SEMANTICALLY_VERIFIED" if result["allowed"] else "REJECTED_BY_GUARD","missing":[],"rule_result":result})
        elif name == "KA-DIRECTION-PROSPECTIVE-01":
            ref = observation.get("ka_candidate_reference")
            if not isinstance(ref, str) or ref not in KA_DIRECTION_CANDIDATES:
                results.append({"rule":name,"status":"BLOCKED","missing":["known_ka_candidate_reference"],"rule_result":None})
            else:
                result = evaluate_ka_direction_candidate(ref)
                results.append({"rule":name,"status":"OPEN_PENDING_INDEPENDENT_DIRECTION" if result["state"] == "OPEN" else "AWAITING_INDEPENDENT_REVIEW","missing":result["missing_requirements"],"rule_result":result})
        else:
            candidate = observation.get("rok_literal")
            if candidate is not None and not isinstance(candidate, str):
                raise ValueError("rok_literal must be text or null")
            results.append({"rule":name,"status":"EVALUATED_NOT_SEMANTICALLY_VERIFIED","missing":[],
                            "rule_result":rok_semantic_guard(candidate)})
    return {"source_reference":observation["source_reference"],
            "object_id":observation.get("object_id"),
            "results":results,"authority":dict(AUTHORITY),
            "scientific_state":"UNVERIFIED",
            "automatic_core_promotion":False}

"""Conservative classification of possible historical route functions.

This module does not infer military use from straightness or commercial use
from proximity alone. It groups independent, dated observations for review.
"""
from dataclasses import dataclass
from typing import Iterable

KINDS = frozenset({"commercial", "military", "mixed", "ritual", "administrative", "unknown"})
FEATURES = {
    "commercial": frozenset({"market", "port", "production", "warehouse", "trade_goods"}),
    "military": frozenset({"fort", "watchtower", "garrison", "defensive_gate", "campaign_camp"}),
    "ritual": frozenset({"sanctuary", "processional_way", "votive_deposit"}),
    "administrative": frozenset({"milestone", "official_waystation", "boundary_record"}),
}

@dataclass(frozen=True)
class RouteObservation:
    feature: str
    source_id: str
    independent_group: str
    earliest: int
    latest: int
    directly_associated: bool = False

def assess_route_function(
    observations: Iterable[RouteObservation],
    year_start: int,
    year_end: int,
) -> dict:
    """Return hypotheses, not historical attestations.

    Dates must span the entire period; independent groups count only once;
    contextual associations cannot independently establish a route's function.
    """
    if year_start > year_end:
        raise ValueError("Invalid period")
    usable = [
        o for o in observations
        if o.source_id and o.independent_group
        and o.earliest <= year_start <= year_end <= o.latest
    ]
    report = {}
    for function, accepted in FEATURES.items():
        relevant = [o for o in usable if o.feature in accepted]
        directly = {o.independent_group for o in relevant if o.directly_associated}
        contextual = {o.independent_group for o in relevant if not o.directly_associated}
        report[function] = {
            "direct_independent_groups": len(directly),
            "contextual_independent_groups": len(contextual - directly),
            "supporting_sources": sorted({o.source_id for o in relevant}),
            "status": "candidate_for_external_review" if len(directly) >= 2 else "insufficient_direct_evidence"
        }
    commercial = report["commercial"]["status"] == "candidate_for_external_review"
    military = report["military"]["status"] == "candidate_for_external_review"
    tentative = "mixed" if commercial and military else "commercial" if commercial else "military" if military else "unknown"
    return {
        "period": [year_start, year_end],
        "candidate_type": tentative,
        "assessments": report,
        "function_proven": False,
        "route_existence_proven": False,
        "epistemic_status": "hypothesis_only",
    }

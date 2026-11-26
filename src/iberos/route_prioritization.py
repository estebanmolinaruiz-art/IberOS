"""G-114: reproducible evidence-led ranking of route verification tasks.

This ranks which hypothesis to TEST NEXT, not which ancient road existed.
Literary signals are provisional until edited, dated and linked to places.
"""
from dataclasses import dataclass
import re
import unicodedata

KEYWORDS = {
 "trade": ("mercancia","comercio","portus","puerto","salinas","almacen"),
 "military": ("militar","campamento","guarnicion","torre","muralla"),
 "movement": ("camino","via","itinerario","travesia","vado","paso"),
}
@dataclass(frozen=True)
class DocumentaryLead:
    lead_id: str
    corridor: str
    source_id: str
    independent_group: str
    evidence_type: str
    directly_observed: bool
    within_target_period: bool
    coordinate_verified: bool = False
    note: str = ""

def text_candidates(text: str) -> dict:
    """Keyword-based retrieval for HUMAN review; no automatic route claims."""
    normalized = unicodedata.normalize("NFKD",text.casefold())
    normalized = "".join(c for c in normalized if not unicodedata.combining(c))
    return {kind:sorted({key for key in words
            if re.search(r"(?<!\w)"+re.escape(key)+r"(?!\w)",normalized)})
            for kind,words in KEYWORDS.items()}

def prioritize(leads: list[DocumentaryLead], target_period: str) -> dict:
    """Scores are investigation priorities, explicitly not historical probabilities."""
    if not target_period: raise ValueError("Target period required")
    seen={}
    for lead in leads:
        if not lead.source_id or not lead.independent_group or not lead.corridor:
            raise ValueError("Missing provenance")
        key=(lead.corridor,lead.independent_group)
        # Use only the strongest representative from a dependent source group.
        value=(3 if lead.within_target_period and lead.directly_observed else 0)
        value+=2 if lead.coordinate_verified and lead.directly_observed else 0
        value+=1 if lead.directly_observed else 0
        if key not in seen or value>seen[key][0]: seen[key]=(value,lead)
    groups={}
    for (corridor,group),(value,lead) in seen.items():
        groups.setdefault(corridor,[]).append((value,lead))
    rankings=[]
    for corridor,items in groups.items():
        score=sum(value for value,_ in items)
        contemporaneous=sum(1 for _,l in items if l.within_target_period and l.directly_observed)
        mapped=sum(1 for _,l in items if l.coordinate_verified and l.directly_observed)
        rankings.append({
            "candidate":corridor,"investigation_priority_score":score,
            "independent_evidence_groups":len(items),
            "contemporaneous_direct_groups":contemporaneous,
            "georeferenced_direct_groups":mapped,
            "historical_road_proven":False,
            "complete_route_proven":False,
            "needs_field_or_archival_verification":True
        })
    rankings.sort(key=lambda x:(-x["investigation_priority_score"],x["candidate"]))
    return {"target_period":target_period,"rankings":rankings,
            "scores_are_probabilities":False,"route_geometry":None,
            "note":"Ranked for verification, not evaluated as historical likelihood."}

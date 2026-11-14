"""Historical textual signals for GeoRoutes (G-112).

Text testimony may motivate a route hypothesis; it cannot certify geometry.
Dates use astronomical years. Event dates and document composition dates
are separate, and duplicate witnesses share a dependency group.
"""
from dataclasses import dataclass
from collections import defaultdict

ALLOWED = frozenset({
    "explicit_itinerary", "movement", "trade", "campaign",
    "port_reference", "place_relation", "later_tradition"
})

@dataclass(frozen=True)
class TextWitness:
    witness_id: str
    source_id: str
    dependency_group: str
    type: str
    event_earliest: int | None
    event_latest: int | None
    written_earliest: int | None
    written_latest: int | None
    start_place: str = ""
    end_place: str = ""
    named_intermediates: tuple[str, ...] = ()
    original_excerpt: str = ""
    reference_locator: str = ""
    editorial_status: str = "unverified"
    route_directly_named: bool = False

    def __post_init__(self):
        if not self.witness_id or not self.source_id or not self.dependency_group:
            raise ValueError("Witness requires stable identity, source and dependency group")
        if self.type not in ALLOWED:
            raise ValueError("Unrecognized testimony type")
        if self.event_earliest is not None and self.event_latest is not None:
            if self.event_earliest > self.event_latest:
                raise ValueError("Invalid event chronology")
        if self.written_earliest is not None and self.written_latest is not None:
            if self.written_earliest > self.written_latest:
                raise ValueError("Invalid composition chronology")

def evaluate_texts(
    witnesses: list[TextWitness], start_place: str, end_place: str,
    year_start: int, year_end: int
) -> dict:
    """Assess contextual and direct testimony; never fabricate a route line.

    'dated_overlap' is only a possible event overlap, never proof of use for
    the full period. Place matches must be controlled by curated identifiers,
    not unreviewed similarity of historical names.
    """
    if year_start > year_end or not start_place or not end_place:
        raise ValueError("Invalid case")
    groups = defaultdict(list)
    exclusions=[]
    for w in witnesses:
        if w.editorial_status != "verified":
            exclusions.append({"witness":w.witness_id,"reason":"unverified_reading"})
            continue
        if w.event_earliest is None or w.event_latest is None:
            exclusions.append({"witness":w.witness_id,"reason":"event_date_unresolved"})
            continue
        if w.event_latest < year_start or w.event_earliest > year_end:
            exclusions.append({"witness":w.witness_id,"reason":"outside_period"})
            continue
        # Explicit same-pair testimony only; direction may be reversible.
        pair_matches = {w.start_place,w.end_place} == {start_place,end_place}
        if not pair_matches:
            exclusions.append({"witness":w.witness_id,"reason":"place_pair_not_verified"})
            continue
        groups[w.dependency_group].append(w)
    independent=[]
    for group, members in sorted(groups.items()):
        direct = [w for w in members if w.route_directly_named and w.type=="explicit_itinerary"]
        chosen = (direct or members)[0]
        independent.append({
            "dependency_group":group,
            "witness":chosen.witness_id,
            "source_id":chosen.source_id,
            "support":"explicit_route_reference" if direct else "contextual_relation",
            "event_interval":[chosen.event_earliest,chosen.event_latest],
            "written_interval":[chosen.written_earliest,chosen.written_latest],
            "intermediate_places":list(chosen.named_intermediates),
        })
    direct_count=sum(w["support"]=="explicit_route_reference" for w in independent)
    return {
        "target_period":[year_start,year_end],
        "independent_witnesses":independent,
        "excluded":exclusions,
        "explicit_witness_group_count":direct_count,
        "status":"textual_route_candidate" if direct_count else (
            "contextual_hypothesis_only" if independent else "no_qualified_textual_evidence"
        ),
        "geometry":None,
        "road_proven":False,
        "function_proven":False,
        "note":"Textual association, itinerary and archaeology must be validated independently.",
    }

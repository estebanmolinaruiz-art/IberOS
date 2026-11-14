"""G-113: historical route continuity audit for IberOS GeoRoutes.

Historical persistence is a hypothesis, not reverse dating. Independent
sources, period overlap and geography must be checked separately.
Astronomical years: -429 = 430 BCE; 1 = AD 1.
"""
from __future__ import annotations
from dataclasses import dataclass
from collections import defaultdict

KINDS = frozenset({"material_road", "textual_itinerary", "landscape_trace",
                   "toponym", "settlement_relation", "dated_surface"})
PERIOD_TYPES = frozenset({"verified", "unverified"})

@dataclass(frozen=True)
class ContinuityWitness:
    witness_id: str
    corridor_id: str
    source_id: str
    dependency_group: str
    kind: str
    earliest: int | None
    latest: int | None
    verification: str = "unverified"
    direct_route_evidence: bool = False
    geometry_verified: bool = False
    notes: str = ""

    def __post_init__(self):
        if not all((self.witness_id, self.corridor_id, self.source_id, self.dependency_group)):
            raise ValueError("Missing provenance or corridor identity")
        if self.kind not in KINDS or self.verification not in PERIOD_TYPES:
            raise ValueError("Invalid evidence kind or verification")
        if self.earliest is not None and self.latest is not None and self.earliest > self.latest:
            raise ValueError("Invalid chronological interval")

@dataclass(frozen=True)
class Period:
    name: str
    earliest: int
    latest: int

    def __post_init__(self):
        if not self.name or self.earliest > self.latest:
            raise ValueError("Invalid period")

def audit_continuity(witnesses: list[ContinuityWitness], corridor_id: str,
                     periods: list[Period]) -> dict:
    """Audit historical evidence within each period, without backward projection.

    No score or hypothesis may certify a roadway. Verified geometry and
    two independent directly associated witnesses allow a *review candidate*
    for a given period only. Separate period candidates do not imply continuity
    through undocumented intervals.
    """
    if not corridor_id or not periods:
        raise ValueError("Corridor and periods required")
    if len(set(p.name for p in periods)) != len(periods):
        raise ValueError("Period names must be unique")
    by_period = {}
    excluded = []
    for p in periods:
        groups = defaultdict(list)
        for w in witnesses:
            if w.corridor_id != corridor_id:
                continue
            if w.verification != "verified":
                excluded.append({"period":p.name,"witness":w.witness_id,"reason":"unverified"})
                continue
            if w.earliest is None or w.latest is None:
                excluded.append({"period":p.name,"witness":w.witness_id,"reason":"undated"})
                continue
            if w.latest < p.earliest or w.earliest > p.latest:
                continue
            groups[w.dependency_group].append(w)
        unique = []
        for group, members in sorted(groups.items()):
            best = sorted(members, key=lambda w: (
                not (w.direct_route_evidence and w.geometry_verified),
                not w.direct_route_evidence,
                w.witness_id
            ))[0]
            unique.append({
                "witness_id":best.witness_id,
                "dependency_group":group,
                "source_id":best.source_id,
                "kind":best.kind,
                "direct":best.direct_route_evidence,
                "geometry_verified":best.geometry_verified
            })
        direct = sum(1 for w in unique if w["direct"] and w["geometry_verified"])
        # Even independent point observations do not prove a connecting corridor.
        by_period[p.name] = {
            "years":[p.earliest,p.latest],
            "qualified_independent_witnesses":unique,
            "direct_geometric_witness_groups":direct,
            "status":"candidate_for_archaeological_review" if direct >= 2 else (
                "context_only" if unique else "no_qualified_evidence"),
            "road_proven":False
        }
    return {
        "corridor_id":corridor_id,
        "periods":by_period,
        "excluded":excluded,
        "continuity_between_periods_proven":False,
        "backdating_allowed":False,
        "geographic_route":None,
        "warning":"A later road or name never dates an earlier road without independent contemporary evidence."
    }

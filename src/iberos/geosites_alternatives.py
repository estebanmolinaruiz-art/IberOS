"""G-128: compare alternative GeoSites corridors with strict paleoenvironment gates.

No artificial raster or historical probabilities. Cost: 0 EUR.
"""
from dataclasses import dataclass
from math import isfinite

BARRIERS=frozenset({"lagoon","river","moat","floodplain","estuary"})
KINDS=BARRIERS | {"land","unknown"}
EVIDENCE={"observed","restored","inferred","unknown"}

@dataclass(frozen=True)
class CorridorSegment:
    key: str
    start: str
    end: str
    terrain: str
    classification: str
    source: str = ""
    earliest: int | None = None
    latest: int | None = None
    geometry_source: str = ""
    transit_source: str = ""
    crossing_source: str = ""
    measured_length_m: float | None = None
    length_source: str = ""

    def __post_init__(self):
        if not self.key or not self.start or not self.end or self.start==self.end:
            raise ValueError("Invalid segment endpoints")
        if self.terrain not in KINDS or self.classification not in EVIDENCE:
            raise ValueError("Invalid terrain/evidence")
        if self.earliest is not None and self.latest is not None and self.earliest>self.latest:
            raise ValueError("Inverted chronology")
        if self.measured_length_m is not None and (not isfinite(self.measured_length_m)
                or self.measured_length_m<=0 or not self.length_source):
            raise ValueError("Length requires positive finite value and source")

def evaluate_segment(s: CorridorSegment, period=(-429,-349)) -> dict:
    lo,hi=period
    if lo>hi: raise ValueError("Invalid period")
    missing=[]
    if s.terrain=="unknown": missing.append("paleoterrain_unknown")
    if s.classification!="observed": missing.append("structure_not_observed")
    if not s.source: missing.append("missing_provenance")
    if s.earliest is None or s.latest is None or s.earliest>lo or s.latest<hi:
        missing.append("period_not_covered")
    if not s.geometry_source: missing.append("geometry_unverified")
    if not s.transit_source: missing.append("transit_unverified")
    if s.terrain in BARRIERS and not s.crossing_source:
        missing.append("independent_crossing_unverified")
    if s.measured_length_m is None: missing.append("measured_length_unavailable")
    return {"segment":s.key,"eligible":not missing,"blockers":missing,
            "terrain":s.terrain,"evidence":s.classification}

def compare_corridors(segments: list[CorridorSegment],
                      candidates: dict[str,list[str]], period=(-429,-349)) -> dict:
    """Chains must be contiguous; rank only fully source-verified lengths."""
    if not candidates: raise ValueError("No candidates")
    bykey={s.key:s for s in segments}
    if len(bykey)!=len(segments): raise ValueError("Duplicate segments")
    assessments={key:evaluate_segment(s,period) for key,s in bykey.items()}
    results=[]
    for name,chain in candidates.items():
        if not name or not chain or len(chain)!=len(set(chain)):
            raise ValueError("Invalid corridor")
        if any(key not in bykey for key in chain): raise ValueError("Missing link")
        possible={bykey[chain[0]].start,bykey[chain[0]].end}
        for idx,key in enumerate(chain[1:],start=1):
            s=bykey[key]
            next_possible=set()
            if s.start in possible: next_possible.add(s.end)
            if s.end in possible: next_possible.add(s.start)
            if not next_possible: raise ValueError("Disconnected chain "+name)
            possible=next_possible
        blockers=sorted({b for key in chain for b in assessments[key]["blockers"]})
        fully_verified=not blockers
        known_lengths=[bykey[k].measured_length_m for k in chain
                       if bykey[k].measured_length_m is not None]
        results.append({"candidate":name,"segments":chain,"eligible":fully_verified,
                        "blockers":blockers,
                        "verified_length_m":round(sum(known_lengths),3) if fully_verified else None,
                        "partial_measured_sum_m":round(sum(known_lengths),3) if known_lengths else None,
                        "historical_road_proven":False})
    results.sort(key=lambda r:(not r["eligible"],
                 r["verified_length_m"] if r["verified_length_m"] is not None else float("inf"),
                 r["candidate"]))
    return {"model":"GEOSITES_G128_EVIDENCE_FIRST","period":list(period),
            "candidate_count":len(results),
            "certified_corridors":sum(r["eligible"] for r in results),
            "ranked_candidates":results,
            "rank_is_conditional_not_historical_probability":True,
            "archaeological_road_proven":False}

def picola_ilici_alternative_preflight() -> dict:
    segments=[
      CorridorSegment("picola_foso","picola_ne","beyond_foso","moat","unknown","Moret-Badie-1998"),
      CorridorSegment("coastal_paleoground","beyond_foso","middle_coast","unknown","unknown"),
      CorridorSegment("coastal_to_ilici","middle_coast","ilici_se","unknown","unknown"),
      CorridorSegment("interior_paleoground","beyond_foso","middle_inland","unknown","unknown"),
      CorridorSegment("inland_to_molar","middle_inland","molar","unknown","unknown"),
      CorridorSegment("molar_to_ilici","molar","ilici_se","land","inferred","Moratalla-2015")
    ]
    result=compare_corridors(segments,{
      "coastal_hypothesis":["picola_foso","coastal_paleoground","coastal_to_ilici"],
      "interior_via_molar_hypothesis":["picola_foso","interior_paleoground",
                                      "inland_to_molar","molar_to_ilici"]
    })
    result["real_period_raster_loaded"]=False
    result["new_geographic_route_drawn"]=False
    result["next_evidence"]="Excavated Picola crossing; dated paleoland; verified Ilici SE gate-to-Molar geometry"
    return result

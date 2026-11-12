"""GeoSites G-127: chronological, archaeological evidence-gated site corridor network.
Unknown, reconstructed and undated edges are not traversable. No paid dependencies.
Astronomical years: 430 BCE = -429, 350 BCE = -349.
"""
from dataclasses import dataclass
from math import hypot, isfinite

@dataclass(frozen=True)
class SiteNode:
    key: str
    label: str
    x: float | None = None
    y: float | None = None
    source: str = ""
    crs: str = "EPSG:25830"
    coordinate_role: str = "none"

    def __post_init__(self):
        if not self.key or not self.label: raise ValueError("Missing node identity")
        if (self.x is None)!=(self.y is None): raise ValueError("Both coordinates required")
        if self.x is not None and (not isfinite(self.x) or not isfinite(self.y) or not self.source):
            raise ValueError("Invalid coordinates or missing provenance")
        if self.coordinate_role not in {"none","surveyed_site","perimeter_reference","provisional"}:
            raise ValueError("Invalid location role")
        if (self.x is None)!=(self.coordinate_role=="none"):
            raise ValueError("Coordinate role must agree with presence of coordinates")

@dataclass(frozen=True)
class RouteLink:
    key: str
    a: str
    b: str
    evidence: str
    source: str = ""
    earliest: int | None = None
    latest: int | None = None
    transit_attested: bool = False
    geom_verified: bool = False
    obstruction: str = ""
    crossing_source: str = ""

    def __post_init__(self):
        if not self.key or not self.a or not self.b or self.a==self.b:
            raise ValueError("Invalid link identity or endpoints")
        if self.evidence not in {"observed","restored","inferred","unknown"}:
            raise ValueError("Invalid evidence type")
        if self.earliest is not None and self.latest is not None and self.earliest>self.latest:
            raise ValueError("Invalid chronological interval")

def audit_corridor(nodes: list[SiteNode], links: list[RouteLink], origin: str,
                   destination: str, period=(-429,-349)) -> dict:
    """Strictly audit observed, transit-attested, dated and geometrically surveyed links."""
    lo,hi=period
    if lo>hi: raise ValueError("Invalid period")
    byid={n.key:n for n in nodes}
    if len(byid)!=len(nodes) or origin not in byid or destination not in byid:
        raise ValueError("Missing/duplicate nodes")
    if len({e.key for e in links})!=len(links): raise ValueError("Duplicate link")
    accepted=[];excluded=[];adj={k:[] for k in byid}
    for e in links:
        if e.a not in byid or e.b not in byid: raise ValueError("Link points to missing node")
        blockers=[]
        if e.evidence!="observed":blockers.append("not_excavated_or_observed")
        if not e.source:blockers.append("missing_source")
        if e.earliest is None or e.latest is None or e.earliest>lo or e.latest<hi:
            blockers.append("not_dated_for_full_period")
        if not e.transit_attested:blockers.append("passage_not_attested")
        if not e.geom_verified:blockers.append("geometry_not_verified")
        if e.obstruction and not e.crossing_source:blockers.append("obstruction_crossing_unverified")
        record={"key":e.key,"a":e.a,"b":e.b,"classification":e.evidence,
                "source":e.source,"blockers":blockers}
        if blockers:excluded.append(record)
        else:
            accepted.append(record);adj[e.a].append((e.b,e.key));adj[e.b].append((e.a,e.key))
    reached={origin:None};queue=[origin]
    for u in queue:
        for v,key in adj[u]:
            if v not in reached:reached[v]=(u,key);queue.append(v)
    path=[]
    if destination in reached:
        u=destination
        while u!=origin:
            v,key=reached[u];path.append(key);u=v
        path.reverse()
    a,b=byid[origin],byid[destination]
    baseline=None
    if a.x is not None and b.x is not None and a.crs==b.crs=="EPSG:25830":
        baseline=round(hypot(a.x-b.x,a.y-b.y),3)
    return {"case_id":"GEOSITES-G127","period":[lo,hi],"origin":origin,
            "destination":destination,"documentary_links":len(links),
            "eligible_links":len(accepted),"excluded_links":excluded,
            "eligible_link_details":accepted,"certified_connected_chain":destination in reached,
            "certified_link_path":path,"map_polyline":None,
            "straight_baseline_reference_m":baseline,
            "historical_road_proven":False,
            "note":"Connected attestations alone do not prove a single engineered road."}

def picola_ilici_research_case() -> dict:
    nodes=[
      SiteNode("picola_bic","La Picola BIC perimeter A1",713265,4230490,"BIC-Picola-A1",coordinate_role="perimeter_reference"),
      SiteNode("picola_gate","La Picola NE gate"),
      SiteNode("picola_moat","La Picola ditch exterior"),
      SiteNode("intermediate","Undocumented 430-350 BCE terrain"),
      SiteNode("molar","Camino del Molar historical trace"),
      SiteNode("ilici_gate","Ilici SE gate"),
      SiteNode("ilici_ref","La Alcudia eastern thermal complex reference",701823.285,4234872.059,"ASTERO-2017",coordinate_role="provisional")
    ]
    links=[
      RouteLink("picola_internal_exit","picola_bic","picola_gate","inferred","Moret-Badie-1998"),
      RouteLink("picola_moat_crossing","picola_gate","picola_moat","unknown","Moret-Badie-1998",obstruction="ditch"),
      RouteLink("picola_marsh_and_countryside","picola_moat","intermediate","unknown",obstruction="paleolagoon"),
      RouteLink("ilici_approach","intermediate","molar","unknown"),
      RouteLink("molar_to_ilici_gate","molar","ilici_gate","inferred","Moratalla-2015"),
      RouteLink("ilici_gate_to_reference","ilici_gate","ilici_ref","inferred","UA-2025")
    ]
    out=audit_corridor(nodes,links,"picola_bic","ilici_ref")
    out["historical_anchors_are_not_gate_coordinates"]=True
    out["priority_gaps"]=[
      {"link":"picola_moat_crossing","requires":"Dated excavated ditch interruption or crossing"},
      {"link":"picola_marsh_and_countryside","requires":"Period-dated dry ground/water crossing mask"},
      {"link":"molar_to_ilici_gate","requires":"Independently surveyed SE gate and Molar axis coordinates"}
    ]
    return out

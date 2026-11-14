"""IberOS GeoRoutes G-117: evidence-gated predictive route ensemble.

Computational prediction means conditional route-search sensitivity, NOT a
trained archaeological model or Bayesian probability of historic existence.
Uses only cells with verified source and chronologically covering interval.
"""
from __future__ import annotations
from collections import Counter
import heapq
import math
import random
from .route_research import EvidenceCell, RouteCase, eligible
from .route_case_audit import GeoAnchor, inspect_case


def ensemble_routes(grid: list[list[EvidenceCell]], case: RouteCase,
                    trials: int = 100, seed: int = 117,
                    terrain_weight_range: tuple[float,float] = (0.5, 2.0)) -> dict:
    """Run Monte Carlo over *cost assumptions*, never over unknown terrain.

    Returned hit frequencies are conditional model stability, not a
    probability that a roadway was historically present.
    """
    if not 1 <= trials <= 2000: raise ValueError("trials must be 1..2000")
    lo, hi = terrain_weight_range
    if not (math.isfinite(lo) and math.isfinite(hi) and 0 < lo <= hi):
        raise ValueError("Invalid cost range")
    if not grid or not grid[0] or any(len(row)!=len(grid[0]) for row in grid):
        raise ValueError("Grid must be rectangular and non-empty")
    rows,cols=len(grid),len(grid[0])
    def inside(p): return 0 <= p[0]<rows and 0 <= p[1]<cols
    if not inside(case.start) or not inside(case.end):
        raise ValueError("Endpoint outside grid")
    mask=[[eligible(c,case) for c in row] for row in grid]
    base={"case_id":case.case_id,"trials":trials,"period":[case.year_start,case.year_end],
          "seed":seed,"cost_range":[lo,hi],
          "model":"evidence_gated_cost_ensemble",
          "conditional_frequencies_not_archaeological_probabilities":True,
          "historical_path_proven":False,"road_function_proven":False}
    if not mask[case.start[0]][case.start[1]] or not mask[case.end[0]][case.end[1]]:
        return {**base,"status":"not_evaluable","connected_runs":0,"cell_frequency":[]}
    rng=random.Random(seed)
    counts=Counter()
    connected=0
    distances=[]
    for _ in range(trials):
        weights=[[rng.uniform(lo,hi) if mask[i][j] else math.inf
                  for j in range(cols)] for i in range(rows)]
        dist={case.start:0.0}
        prev={}
        queue=[(0.0,case.start)]
        while queue:
            cost,u=heapq.heappop(queue)
            if cost>dist.get(u,math.inf)+1e-12: continue
            if u==case.end: break
            for dr in (-1,0,1):
                for dc in (-1,0,1):
                    if dr==0 and dc==0: continue
                    v=(u[0]+dr,u[1]+dc)
                    if not inside(v) or not mask[v[0]][v[1]]: continue
                    if dr and dc and not (mask[u[0]+dr][u[1]] and mask[u[0]][u[1]+dc]):
                        continue
                    step=math.hypot(dr,dc)*case.resolution_m*(
                        weights[u[0]][u[1]]+weights[v[0]][v[1]])/2
                    alt=cost+step
                    if alt+1e-12 < dist.get(v,math.inf):
                        dist[v]=alt; prev[v]=u
                        heapq.heappush(queue,(alt,v))
        if case.end not in dist: continue
        connected+=1
        route=[case.end]
        while route[-1]!=case.start:
            route.append(prev[route[-1]])
        route.reverse()
        distances.append(round(sum(math.hypot(b[0]-a[0],b[1]-a[1])
                                   for a,b in zip(route,route[1:]))*case.resolution_m,3))
        counts.update(route)
    if connected==0:
        return {**base,"status":"no_connected_certified_cells",
                "connected_runs":0,"cell_frequency":[]}
    return {**base,"status":"conditional_candidates_computed",
            "connected_runs":connected,
            "length_range_m":[min(distances),max(distances)],
            "cell_frequency":[{"cell":list(cell),"runs":n,"fraction_of_trials":round(n/trials,4)}
                              for cell,n in sorted(counts.items())]}


def audit_picola_ensemble() -> dict:
    """Run the actual case preflight. NEVER fabricate a historic raster."""
    origin=GeoAnchor("La Alcudia",701823.285,4234872.059,"EPSG:25830",
                     "ASTERO-2017","modern_excavation_reference")
    destination=GeoAnchor("La Picola",713265,4230490,"EPSG:25830",
                          "BIC-Picola-A1","site_perimeter_vertex")
    audit=inspect_case(origin,destination,-429,-349)
    return {
        "case":"PICOLA-ALCUDIA-G117",
        "audit":audit,
        "ensemble_run":None,
        "ensemble_status":"blocked_no_dated_continuous_paleogeographic_grid",
        "priority":"Verify Camino del Molar / southeast Ilici gate geometry; Picola northeast entrance and marsh barriers.",
        "historical_road_proven":False,
        "model_trained":False
    }

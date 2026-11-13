"""IberOS GeoRoutes: investigación de conexiones, no identificación automática de caminos.

Motor puro Python (sin dependencias de pago ni geoespaciales obligatorias).
Las celdas desconocidas nunca son transitables. Las fechas son intervalos
en años astronómicos: 430 a. C. = -429; 350 a. C. = -349.
"""
from __future__ import annotations
from dataclasses import dataclass
import heapq
import math
import random

@dataclass(frozen=True)
class EvidenceCell:
    kind: str  # land, lagoon, river, unknown
    earliest: int | None = None
    latest: int | None = None
    source_id: str = ""
    crossing_evidence_id: str = ""
    elevation_m: float | None = None

@dataclass(frozen=True)
class RouteCase:
    case_id: str
    start: tuple[int, int]
    end: tuple[int, int]
    year_start: int
    year_end: int
    resolution_m: float
    crs: str

    def __post_init__(self):
        if self.year_start > self.year_end or self.resolution_m <= 0 or not self.crs:
            raise ValueError("Invalid period, grid resolution or CRS")

def eligible(cell: EvidenceCell, case: RouteCase) -> bool:
    """Conservative: evidence interval must cover the whole requested period."""
    dated = (cell.earliest is not None and cell.latest is not None
             and cell.earliest <= case.year_start <= case.year_end <= cell.latest)
    if not dated or not cell.source_id:
        return False
    return cell.kind == "land" or (cell.kind == "river" and bool(cell.crossing_evidence_id))

def analyze(grid: list[list[EvidenceCell]], case: RouteCase, method="dijkstra",
            penalty_cells=None, seed=0) -> dict:
    """Shortest or grade-penalized path. No diagonal corner cutting."""
    if method not in ("dijkstra", "astar", "grade"):
        raise ValueError("Unknown method")
    if not grid or not grid[0] or any(len(row) != len(grid[0]) for row in grid):
        raise ValueError("Grid must be nonempty and rectangular")
    rows, cols = len(grid), len(grid[0])
    def inside(p): return 0 <= p[0] < rows and 0 <= p[1] < cols
    if not inside(case.start) or not inside(case.end):
        raise ValueError("End point outside grid")
    passed = [[eligible(c,case) for c in row] for row in grid]
    base = {"case_id": case.case_id, "crs":case.crs, "period":[case.year_start,case.year_end],
            "method":method, "historical_path_proven":False,
            "unknown_cells":sum(c.kind=="unknown" for row in grid for c in row)}
    if not passed[case.start[0]][case.start[1]] or not passed[case.end[0]][case.end[1]]:
        return {**base, "status":"not_evaluable", "path":[]}
    rng = random.Random(seed)
    # deterministic seeded tie-breaking; no relaxation of archaeological restrictions
    dist={case.start:0.}; prev={}; queue=[(0.,0.,case.start)]
    while queue:
        priority,cost,u=heapq.heappop(queue)
        if cost != dist.get(u): continue
        if u == case.end:
            path=[u]
            while u in prev:
                u=prev[u];path.append(u)
            path.reverse()
            return {**base,"status":"candidate_computed","path":[list(p) for p in path],
                    "cost":round(cost,3),"length_m":round(sum(math.hypot(b[0]-a[0],b[1]-a[1])
                    for a,b in zip(path,path[1:]))*case.resolution_m,3)}
        for dr in (-1,0,1):
            for dc in (-1,0,1):
                if not dr and not dc: continue
                v=(u[0]+dr,u[1]+dc)
                if not inside(v) or not passed[v[0]][v[1]]: continue
                if dr and dc and not (passed[u[0]+dr][u[1]] and passed[u[0]][u[1]+dc]):
                    continue
                step=math.hypot(dr,dc)*case.resolution_m
                if method=="grade":
                    a,b=grid[u[0]][u[1]].elevation_m,grid[v[0]][v[1]].elevation_m
                    if a is None or b is None: continue
                    step *= 1+10*((b-a)/(math.hypot(dr,dc)*case.resolution_m))**2
                if penalty_cells and v in penalty_cells: step *= 3
                # tiny jitter only for alternate cost ties
                if seed: step *= 1+1e-7*rng.random()
                new=cost+step
                if new < dist.get(v,math.inf):
                    dist[v]=new;prev[v]=u
                    h=(math.hypot(case.end[0]-v[0],case.end[1]-v[1])
                       *case.resolution_m if method=="astar" else 0)
                    heapq.heappush(queue,(new+h,new,v))
    return {**base,"status":"no_connected_certified_cells","path":[]}

def compare(grid: list[list[EvidenceCell]], case: RouteCase, trials=20) -> dict:
    """Multiple cost assumptions, without granting transit to unknown cells."""
    if trials < 0 or trials > 10000: raise ValueError("Invalid trials")
    primary=analyze(grid,case)
    variants={"shortest":primary,"astar":analyze(grid,case,"astar"),
              "grade":analyze(grid,case,"grade")}
    if primary["path"]:
        penalized=set(map(tuple,primary["path"][1:-1]))
        variants["alternative"]=analyze(grid,case,penalty_cells=penalized)
    frequency={}
    for i in range(trials):
        candidate=analyze(grid,case,seed=i+1)
        for p in candidate["path"]:
            k=tuple(p);frequency[k]=frequency.get(k,0)+1
    return {"case_id":case.case_id,"routes":variants,
            "frequencies":[{"cell":list(k),"count":v} for k,v in sorted(frequency.items())],
            "trials":trials,"historical_path_proven":False}

"""G-129 GeoSites: source-accurate 100 m borehole grid cells, no ancient land inference.

Coordinates in Blázquez Morilla (2003), p.107 are grid references with
no verified datum: they are NOT EPSG:25830 points. Free Python only.
"""
from dataclasses import dataclass
from math import hypot, isfinite
import re

SOURCE="Blazquez-Morilla-2003-Universitat-Valencia-p107-table"
SOURCE_URL="https://roderic.uv.es/bitstream/10550/15135/1/blazquez.pdf"

@dataclass(frozen=True)
class Borehole:
    name: str
    grid: str
    altitude_m: float
    depth_m: float
    source: str = SOURCE
    dated_430_350_bce_layer: bool = False
    period_environment: str | None = None
    def __post_init__(self):
        if not self.name or not self.source or not isfinite(self.altitude_m) or not isfinite(self.depth_m) or self.depth_m<=0:
            raise ValueError("Invalid borehole provenance or measurements")
        if self.period_environment is not None and not self.dated_430_350_bce_layer:
            raise ValueError("Period environment needs dated layer")

def decode_local_grid(value: str) -> dict:
    """Decode just 30S XH/YH six-digit grid cells for the Elx area."""
    norm=re.sub(r"\s+","",value).upper()
    m=re.fullmatch(r"30S([XY])H(\d{3})(\d{3})",norm)
    if not m: raise ValueError("Unsupported or incomplete MGRS reference")
    e={"X":600000,"Y":700000}[m.group(1)]+100*int(m.group(2))
    n=4200000+100*int(m.group(3))
    return {"easting_m":[e,e+100],"northing_m":[n,n+100],
            "center_m":[e+50,n+50],"cell_width_m":100,
            "datum_verified":False,"crs":"UTM-30; horizontal datum unknown"}

def distance_bounds(cell: dict,x: float,y: float) -> list[float]:
    """Exact planar min/max distances to a 100m square; NOT datum-corrected."""
    ex=cell["easting_m"]; ny=cell["northing_m"]
    dx=max(ex[0]-x,0,x-ex[1]);dy=max(ny[0]-y,0,y-ny[1])
    return [round(hypot(dx,dy),2),round(max(hypot(xx-x,yy-y)
            for xx in ex for yy in ny),2)]

def study_cores() -> list[Borehole]:
    return [
        Borehole("Pinet","30SYH081 278",1,36),
        Borehole("Picola","30SYH133 305",2,23),
        Borehole("Mórtoles","30SYH089 311",2,31),
        Borehole("Salinas","30S YH086 270",1,30),
        Borehole("Fondo","30SXH996 292",8,12),
        Borehole("Riegos","30SYH954 322",9,8)
    ]

def audit_picola_paleocores() -> dict:
    records=[]
    for c in study_cores():
        cell=decode_local_grid(c.grid)
        records.append({"name":c.name,"published_grid":c.grid,"cell":cell,
          "altitude_m_as_published":c.altitude_m,"total_depth_m":c.depth_m,
          "provisional_distance_to_picola_BIC_A1_m":distance_bounds(cell,713265,4230490),
          "original_source":c.source,"period_lithology":"undetermined",
          "date_and_layer_correlation_verified":False})
    r=next(c for c in records if c["name"]=="Riegos")
    hypothesis=decode_local_grid("30SXH954 322")
    return {"case_id":"GEOSITES-G129","source_url":SOURCE_URL,
            "period_astronomical_years":[-429,-349],"core_count":len(records),
            "cores":records,
            "riegos_anomaly":{"published":r["published_grid"],
                "hypothetical_not_verified":"30SXH954 322",
                "east_difference_m":r["cell"]["center_m"][0]-hypothesis["center_m"][0],
                "action":"quarantine_and_check_original_fig7.1"},
            "paleoland_cells_eligible":0,"period_raster":None,
            "route_evaluable":False,"horizontal_datum_transformation_verified":False,
            "result":"ABSTAIN_NO_DATED_LAYER_GEOMETRY",
            "warning":"Published core positions are 100m grid cells with unspecified datum, not ancient land or crossing evidence."}

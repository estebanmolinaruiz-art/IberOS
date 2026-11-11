"""G-122: La Picola gate-to-moat exit scenario calculation.

Pure geometric sensitivity, NOT an excavation or confirmation of a bridge.
Widths are source-derived ranges; the crossing angle is hypothetical.
"""
from dataclasses import dataclass
from math import cos, radians, isfinite

@dataclass(frozen=True)
class ObstacleBand:
    name: str
    width_min_m: float
    width_max_m: float
    source_id: str
    verified_for_period: bool

    def __post_init__(self):
        if not self.name or not self.source_id or not all(
            isfinite(x) for x in (self.width_min_m,self.width_max_m)
        ) or self.width_min_m <= 0 or self.width_max_m < self.width_min_m:
            raise ValueError("Invalid source or width interval")

def crossing_sensitivity(band: ObstacleBand, angles_deg=(0,15,30,45,60)) -> dict:
    """Distance within strip if crossing at angle from its normal.

    Only local width math; not projected geospatial coordinates. A schematic
    continuation of street R2 is not evidence of an actual crossing.
    """
    scenarios=[]
    for angle in angles_deg:
        if not isinstance(angle,(int,float)) or not isfinite(angle) or abs(angle)>=89:
            raise ValueError("Angle must be finite within (-89,89)")
        factor=1/cos(radians(angle))
        scenarios.append({
            "offset_angle_from_band_normal_deg":float(angle),
            "crossing_length_min_m":round(band.width_min_m*factor,3),
            "crossing_length_max_m":round(band.width_max_m*factor,3),
        })
    return {
        "obstacle":band.name,
        "source_id":band.source_id,
        "band_width_range_m":[band.width_min_m,band.width_max_m],
        "chronologically_verified":band.verified_for_period,
        "hypothetical_crossing_scenarios":scenarios,
        "crossing_identified":False,
        "causeway_or_bridge_proven":False,
        "road_alignment_proven":False,
        "map_geometry":None,
        "model_kind":"dimensioned_geometric_sensitivity_only",
    }

def assess_picola_gate_exit() -> dict:
    """Strict Picola evidence audit; no fabricated gate GPS or bridge."""
    moat=ObstacleBand("La Picola - possible NE moat strip",5.0,6.0,
                      "Moret-Badie-1998-plan-review-required",False)
    return {
        "case_id":"PICOLA-NE-GATE-G122",
        "gate":"northeast curtain, leads into internal street R2",
        "gate_center_epsg25830":None,
        "r2_axis_epsg25830":None,
        "moat_edges_epsg25830":None,
        "obstacle_sensitivity":crossing_sensitivity(moat),
        "terrain_beyond_moat_430_350_bce":"unknown",
        "exit_route_status":"not_georeferenced_and_not_dated",
        "next_needed":["surveyed gate center","two street R2 axis points",
                       "moat inner and outer crest lines","crossing stratigraphy",
                       "dated dry-ground mask outside the ditch"],
        "connection_to_ilici_proven":False,
        "note":"5–6 m is a published approximate upper moat width; diagram-only scenario, not a bridge measurement."
    }

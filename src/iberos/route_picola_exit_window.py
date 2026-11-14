"""G-125: strictly local dimensions of the northeast exit at La Picola.

All distances are schematic normal offsets from the OUTER curtain face.
No plan georeferencing, excavated causeway, bridge or road is assumed.
"""
from dataclasses import dataclass
from math import cos, radians, isfinite

@dataclass(frozen=True)
class PicolaDefenceGeometry:
    curtain_length_m: float = 56.0
    street_width_m: float = 3.55
    glacis_min_m: float = 5.0
    glacis_max_m: float = 5.5
    moat_top_min_m: float = 5.0
    moat_top_max_m: float = 6.0
    entire_defence_min_m: float = 12.0
    entire_defence_max_m: float = 13.0
    source_id: str = "Moret-Badie-1998-AEspA71-fig2-fig3"

def estimate_exit_window(data: PicolaDefenceGeometry | None = None,
                         angle_deg: float = 0) -> dict:
    """Bound normal transverse offsets. Angle is illustrative, not measured."""
    d=data or PicolaDefenceGeometry()
    sizes=(d.curtain_length_m,d.street_width_m,d.glacis_min_m,d.glacis_max_m,
           d.moat_top_min_m,d.moat_top_max_m,d.entire_defence_min_m,d.entire_defence_max_m)
    if any(not isfinite(v) or v <= 0 for v in sizes) or not d.source_id:
        raise ValueError("Invalid dimensions or provenance")
    if not (d.glacis_min_m<=d.glacis_max_m and d.moat_top_min_m<=d.moat_top_max_m
            and d.entire_defence_min_m<=d.entire_defence_max_m):
        raise ValueError("Inverted width interval")
    if not isfinite(angle_deg) or abs(angle_deg)>=80:
        raise ValueError("Angle outside comparison range")
    factor=1/cos(radians(angle_deg))
    return {
        "case":"PICOLA-NE-GATE-G125",
        "reference_frame":"local; zero at outer northeast curtain face; positive outward",
        "curtain_midpoint_nominal_m":d.curtain_length_m/2,
        "r2_road_width_m":d.street_width_m,
        "moat_near_edge_normal_offset_m":[d.glacis_min_m,d.glacis_max_m],
        "moat_far_edge_normal_offset_m":[d.glacis_min_m+d.moat_top_min_m,
                                          d.glacis_max_m+d.moat_top_max_m],
        "crossing_to_near_edge_along_hypothetical_axis_m":[
            round(d.glacis_min_m*factor,3),round(d.glacis_max_m*factor,3)],
        "crossing_to_far_edge_along_hypothetical_axis_m":[
            round((d.glacis_min_m+d.moat_top_min_m)*factor,3),
            round((d.glacis_max_m+d.moat_top_max_m)*factor,3)],
        "orientation_angle_deg":angle_deg,
        "published_defence_band_m":[d.entire_defence_min_m,d.entire_defence_max_m],
        "not_equivalent_to_full_defence_band":True,
        "site_epsg25830_geometry":None,
        "axis_R2_coordinates":None,
        "moat_crossing_observed":False,
        "bridge_or_causeway_proven":False,
        "historical_road_proven":False,
        "published_source":d.source_id,
        "note":"Calculated dimension envelopes; actual R2 crossing direction and moat geometry not georeferenced."
    }

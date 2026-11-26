"""G-116: measured association between a traced route axis and an excavated gate.

Only use coordinates measured in the same projected CRS. Returns geometry and
measurement uncertainty, never chronology or archaeological identification.
"""
from dataclasses import dataclass
from math import hypot, isfinite

@dataclass(frozen=True)
class SurveyPoint:
    east_m: float
    north_m: float
    uncertainty_m: float
    source_id: str
    crs: str = "EPSG:25830"

    def __post_init__(self):
        if not all(isfinite(x) for x in (self.east_m,self.north_m,self.uncertainty_m)):
            raise ValueError("Nonfinite measurement")
        if self.uncertainty_m < 0 or not self.source_id:
            raise ValueError("Missing source or invalid uncertainty")

def gate_axis_test(start: SurveyPoint, end: SurveyPoint, gate: SurveyPoint,
                   gate_width_m: float = 0) -> dict:
    """Measure shortest distance to *mapped segment* and line extrapolation.

    Extrapolated axis is disclosed separately from the observed segment.
    Conservative distance interval uses sum of source uncertainty radii.
    """
    if len({start.crs,end.crs,gate.crs}) != 1 or start.crs != "EPSG:25830":
        raise ValueError("All observations must be EPSG:25830")
    if not isfinite(gate_width_m) or gate_width_m < 0:
        raise ValueError("Gate width must be finite and nonnegative")
    dx,dy=end.east_m-start.east_m,end.north_m-start.north_m
    length=hypot(dx,dy)
    if length == 0: raise ValueError("Route segment requires two distinct points")
    gx,gy=gate.east_m-start.east_m,gate.north_m-start.north_m
    along=(gx*dx+gy*dy)/length
    t=along/length
    projection=(start.east_m+t*dx,start.north_m+t*dy)
    extrapolated=hypot(gate.east_m-projection[0],gate.north_m-projection[1])
    clipped=max(0.,min(1.,t))
    segment_distance=hypot(gate.east_m-(start.east_m+clipped*dx),
                           gate.north_m-(start.north_m+clipped*dy))
    tolerance=start.uncertainty_m+end.uncertainty_m+gate.uncertainty_m+gate_width_m/2
    return {
        "observed_axis_length_m":round(length,3),
        "gate_distance_to_observed_segment_m":round(segment_distance,3),
        "gate_distance_to_extrapolated_axis_m":round(extrapolated,3),
        "projection_on_observed_segment":0 <= t <= 1,
        "projection_fraction":round(t,6),
        "conservative_distance_interval_m":[round(max(0,extrapolated-tolerance),3),
                                             round(extrapolated+tolerance,3)],
        "geometric_overlap_possible":extrapolated <= tolerance,
        "sources":[start.source_id,end.source_id,gate.source_id],
        "archaeological_connection_proven":False,
        "contemporary_use_proven":False,
        "warning":"A projected line can intersect a gate without proving road use."
    }

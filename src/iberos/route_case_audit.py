"""IberOS GeoRoutes: auditable case-level readiness and geometric baseline.

A coordinate pair is never evidence for a road, a ford or a dry corridor.
Dates use astronomical integer years, e.g. 430 BCE = -429.
No network access or paid dependencies.
"""
from __future__ import annotations

from dataclasses import dataclass
from math import atan2, degrees, hypot, isfinite
from typing import Mapping


@dataclass(frozen=True)
class GeoAnchor:
    site_id: str
    east_m: float
    north_m: float
    crs: str
    source_id: str
    anchor_type: str = "site_reference"

    def __post_init__(self):
        if not self.site_id or not self.source_id or not self.crs:
            raise ValueError("Anchor must have site, source and CRS")
        if not all(isfinite(x) for x in (self.east_m, self.north_m)):
            raise ValueError("Coordinates must be finite")


def inspect_case(
    origin: GeoAnchor,
    destination: GeoAnchor,
    year_start: int,
    year_end: int,
    layer_inventory: Mapping[str, bool] | None = None,
) -> dict:
    """Preflight before any route computation.

    Inventory flags indicate *validated* layers spanning the entire period,
    not the mere presence of modern maps or unreferenced figures.
    """
    if origin.crs != destination.crs:
        raise ValueError("Mixed CRS: transform before comparing")
    if origin.site_id == destination.site_id:
        raise ValueError("Distinct sites required")
    if year_start > year_end:
        raise ValueError("Invalid time interval")
    if origin.crs != "EPSG:25830":
        raise ValueError("Metric ETRS89 UTM 30N required for this baseline")
    required = ("georeferenced_ancient_land", "dated_lagoon_mask",
                "dated_river_mask", "verified_crossings",
                "ancient_access_points", "continuous_evidence_grid")
    inventory = layer_inventory or {}
    missing = [name for name in required if inventory.get(name) is not True]
    dx = destination.east_m - origin.east_m
    dy = destination.north_m - origin.north_m
    # Clockwise from north. Distance is a Euclidean baseline, not a road length.
    bearing = (degrees(atan2(dx, dy)) + 360) % 360
    return {
        "origin": origin.site_id,
        "destination": destination.site_id,
        "crs": origin.crs,
        "astronomical_years": [year_start, year_end],
        "straight_line_m": round(hypot(dx, dy), 3),
        "bearing_deg": round(bearing, 3),
        "anchor_sources": [origin.source_id, destination.source_id],
        "anchor_types": [origin.anchor_type, destination.anchor_type],
        "ready_for_historical_routing": not missing,
        "missing_verifications": missing,
        "route_status": "not_evaluable_missing_evidence" if missing else "ready_for_routing_only",
        "route_geometry": None,
        "archaeological_road_proven": False,
        "road_function_proven": False,
        "note": "Site anchors do not locate gates; a straight line is not an archaeological route.",
    }

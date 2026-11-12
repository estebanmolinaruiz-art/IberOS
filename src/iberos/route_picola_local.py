"""G-124 local-coordinate geometric constraints from Moret & Badie (1998).

Not world-space georeferencing; no bridge or road claimed.
"""
from dataclasses import dataclass

@dataclass(frozen=True)
class PicolaLocalReference:
    curtain_ne_length_m: float = 56.0
    r2_street_width_m: float = 3.55
    r2_to_nw_scarp_base_m: float = 34.0
    r2_to_se_eroded_slope_m: float = 33.35
    defensive_band_min_m: float = 12.0
    defensive_band_max_m: float = 13.0
    moat_top_min_m: float = 5.0
    moat_top_max_m: float = 6.0

def assess_picola_local_axes(ref: PicolaLocalReference | None = None) -> dict:
    """Dimensionally bounded local plan, not excavated gate coordinates."""
    ref = ref or PicolaLocalReference()
    if min(ref.curtain_ne_length_m,ref.r2_street_width_m,
           ref.r2_to_nw_scarp_base_m,ref.r2_to_se_eroded_slope_m,
           ref.defensive_band_min_m,ref.moat_top_min_m) <= 0:
        raise ValueError("Invalid metric evidence")
    if ref.defensive_band_min_m>ref.defensive_band_max_m or ref.moat_top_min_m>ref.moat_top_max_m:
        raise ValueError("Invalid intervals")
    return {
        "local_curtain_midpoint_from_end_m":ref.curtain_ne_length_m/2,
        "curtain_midpoint_is_inference":True,
        "r2_street_width_m":ref.r2_street_width_m,
        "observed_scarp_side_difference_m":round(ref.r2_to_nw_scarp_base_m-ref.r2_to_se_eroded_slope_m,3),
        "side_difference_interpretation":"SE scarp eroded; no evidence of actual lateral street-axis displacement",
        "defensive_band_range_m":[ref.defensive_band_min_m,ref.defensive_band_max_m],
        "moat_top_width_range_m":[ref.moat_top_min_m,ref.moat_top_max_m],
        "world_coordinates":None,
        "moat_exit_point":None,
        "bridge_proven":False,
        "external_route_proven":False,
        "source":"Moret and Badie (1998), AEspA 71, 53-61, fig.3",
    }

"""Read-only GEO bridge from the published six-node IberOS Atlas.

Atlas nodes are territorial references, NOT object findspot coordinates.
No geographic observation is allowed to promote linguistic hypotheses.
"""
from __future__ import annotations
from typing import Any
from .core import get_object

ATLAS_NODES = (
    {"id":"KELIN","name":"Los Villares / Kelin","query":"Los Villares","lat":39.55354,"lon":-1.28322,"precision":"SITE_REFERENCE","zone":"LEV"},
    {"id":"SAGUNTO","name":"Arse / Saguntum","query":"Sagunto","lat":39.6799,"lon":-0.2786,"precision":"TERRITORIAL_REFERENCE","zone":"LEV"},
    {"id":"TIVISSA","name":"Castellet de Banyoles","query":"Tivissa","lat":41.0624,"lon":0.6655,"precision":"SITE_REFERENCE","zone":"NE"},
    {"id":"CAMINREAL","name":"La Caridad","query":"Caminreal","lat":40.8435,"lon":-1.3385,"precision":"SITE_REFERENCE","zone":"CONTACT"},
    {"id":"PICO_AJOS","name":"Pico de los Ajos","query":"Pico de los Ajos","lat":39.38,"lon":-0.81,"precision":"APPROXIMATE_LOCALITY","zone":"LEV"},
    {"id":"LLIRIA","name":"Tossal de Sant Miquel / Edeta","query":"Llíria","lat":39.62,"lon":-0.60,"precision":"APPROXIMATE_LOCALITY","zone":"LEV"},
)

def atlas_nodes() -> list[dict[str, Any]]:
    """Copy published atlas references; never present them as artifact locations."""
    return [dict(n) for n in ATLAS_NODES]

def geo_context(object_id: str) -> dict[str, Any]:
    """Find an explicit catalog place match, without fuzzy or inferred coordinates."""
    obj = get_object(object_id)
    if obj is None:
        raise ValueError("Unknown OBJECT_ID")
    # The matched catalogue text is descriptive, not proof of exact findspot.
    haystack = " | ".join((obj.get("Yacimiento") or "", obj.get("Localidad") or ""))
    words = haystack.casefold()
    matches = [dict(n) for n in ATLAS_NODES if n["query"].casefold() in words]
    return {
        "object_id": object_id,
        "catalogue_yacimiento": obj.get("Yacimiento", ""),
        "catalogue_localidad": obj.get("Localidad", ""),
        "atlas_matches": matches,
        "object_coordinates_verified": False,
        "regional_linguistic_inference": "NOT_PERMITTED",
        "scientific_state": "CONTEXT_ONLY",
        "automatic_core_promotion": False,
    }

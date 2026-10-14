"""Read-only GEO bridge from the published six-node IberOS Atlas.

Atlas nodes are territorial references, NOT object findspot coordinates.
No geographic observation is allowed to promote linguistic hypotheses.
"""
from __future__ import annotations
from typing import Any
import json
from pathlib import Path
from .core import get_object, REPO_ROOT

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
    source = REPO_ROOT / "site" / "data" / "geo_atlas_nodes.json"
    if source.is_file():
        nodes = json.loads(source.read_text(encoding="utf-8"))
        if not isinstance(nodes, list) or len(nodes) != 6:
            raise ValueError("Unexpected shared GEO catalogue")
        required = {"id", "name", "query", "lat", "lon", "precision", "zone"}
        if any(not isinstance(row, dict) or not required.issubset(row) for row in nodes):
            raise ValueError("Malformed shared GEO catalogue")
        return [dict(n) for n in nodes]
    # Compatibility fallback for standalone iberos==1.0.1 installs;
    # must remain identical to the shared source under CI.
    return [dict(n) for n in ATLAS_NODES]

def geo_context(object_id: str) -> dict[str, Any]:
    """Find an explicit catalog place match, without fuzzy or inferred coordinates."""
    obj = get_object(object_id)
    if obj is None:
        raise ValueError("Unknown OBJECT_ID")
    # The matched catalogue text is descriptive, not proof of exact findspot.
    haystack = " | ".join((obj.get("Yacimiento") or "", obj.get("Localidad") or ""))
    words = haystack.casefold()
    matches = [dict(n) for n in atlas_nodes() if n["query"].casefold() in words]
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

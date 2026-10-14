from iberos.geo import atlas_nodes, geo_context
import pytest

def test_atlas_published_nodes_have_no_object_location_claim():
    nodes = atlas_nodes()
    assert len(nodes) == 6
    assert all(n["precision"] for n in nodes)
    nodes[0]["lat"] = 0
    assert atlas_nodes()[0]["lat"] != 0

def test_tivissa_object_finds_atlas_reference_only():
    result = geo_context("IBR-PLM-0002")
    assert any(n["id"] == "TIVISSA" for n in result["atlas_matches"])
    assert result["object_coordinates_verified"] is False
    assert result["automatic_core_promotion"] is False

def test_unknown_object_fails_closed():
    with pytest.raises(ValueError):
        geo_context("IBR-NOT-A-REAL-OBJECT")


def test_shared_atlas_catalogue_matches_standalone_python_fallback():
    from iberos.geo import ATLAS_NODES
    from iberos.core import REPO_ROOT
    import json
    source = REPO_ROOT / "site" / "data" / "geo_atlas_nodes.json"
    if source.is_file():
        published = json.loads(source.read_text(encoding="utf-8"))
        assert len(published) == len(ATLAS_NODES)
        for new, old in zip(published, ATLAS_NODES):
            assert all(new[key] == old[key] for key in
                       ("id", "name", "query", "lat", "lon", "precision", "zone"))

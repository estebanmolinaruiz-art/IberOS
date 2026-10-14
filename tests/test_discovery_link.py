from iberos.discovery_link import proposed_object_links
import pytest

def test_explicit_known_id_is_only_proposed():
    result=proposed_object_links([{"id":"DISC-sample","title":"Review of IBR-PLM-0002"}])[0]
    assert result["candidate_object_ids"] == ["IBR-PLM-0002"]
    assert result["link_is_evidence"] is False
    assert result["automatic_core_promotion"] is False

def test_place_names_do_not_create_object_links():
    result=proposed_object_links([{"id":"DISC-sample","title":"Iberian inscriptions in Tivissa"}])[0]
    assert result["candidate_object_ids"] == []
    assert result["link_state"] == "NO_EXPLICIT_OBJECT_ID"

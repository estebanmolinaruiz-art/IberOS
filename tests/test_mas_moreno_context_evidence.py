"""Boundary tests: real published context must not be semantic gold."""
import copy
import json

import pytest

from iberos.mas_moreno_context_evidence import DATA, audit


@pytest.fixture
def document():
    return json.loads(DATA.read_text(encoding="utf-8"))


def test_published_context_passes_without_translation(document):
    out = audit(document)
    assert out["stamp_families_documented_editorially"] == 6
    assert out["families_by_script"] == {"IBERIAN": 5, "LATIN": 1}
    assert out["published_stamp_impressions_until_2015"] == 15
    assert out["verified_roles_of_named_people"] == 0
    assert out["translation_validated"] is False


def test_us13358_pair_are_distinct_stamps(document):
    out = audit(document)
    assert out["us_13358_pair"] == ["ILURATIN", "ACINI"]
    bad = copy.deepcopy(document)
    bad["associations"][0]["object_relation"] = "BILINGUAL_SAME_VESSEL"
    with pytest.raises(ValueError, match="conflate"):
        audit(bad)


def test_cannot_invent_role_gold(document):
    document["associations"][0]["roles_of_named_people_known"] = True
    with pytest.raises(ValueError, match="maker/owner"):
        audit(document)


def test_cannot_claim_unreviewed_image_is_adjudicated(document):
    document["stamp_families"][0]["photo_adjudicated"] = True
    with pytest.raises(ValueError, match="photo verification"):
        audit(document)


def test_cannot_fabricate_physical_ids(document):
    document["stamp_families"][0]["physical_object_id"] = "INVENTED"
    with pytest.raises(ValueError, match="inventory"):
        audit(document)


def test_unknown_source_is_rejected(document):
    document["stamp_families"][0]["source_ids"] = ["NOT-VERIFIED"]
    with pytest.raises(ValueError, match="source"):
        audit(document)


def test_duplicate_family_is_rejected(document):
    document["stamp_families"].append(copy.deepcopy(document["stamp_families"][0]))
    with pytest.raises(ValueError, match="duplicate"):
        audit(document)


def test_published_count_mismatch_is_rejected(document):
    document["published_counts"][0]["total_stamps"] = 25
    with pytest.raises(ValueError, match="count mismatch"):
        audit(document)


def test_negative_control_cannot_be_promoted(document):
    document["negative_controls"][0]["expected"] = True
    with pytest.raises(ValueError, match="causal conclusion"):
        audit(document)


def test_cost_must_be_zero(document):
    document["cost_eur"] = 1
    with pytest.raises(ValueError, match="zero-cost"):
        audit(document)

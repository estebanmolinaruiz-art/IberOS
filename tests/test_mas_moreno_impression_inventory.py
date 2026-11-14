"""Evidence tests for the 9+6 Mas de Moreno historical inventory reconstruction."""
import copy
import json
import pytest

from iberos.mas_moreno_impression_inventory import DATA, audit_impressions


@pytest.fixture
def registry():
    return json.loads(DATA.read_text(encoding="utf-8"))


def test_baseline_reconciles_without_semantic_claims(registry):
    out = audit_impressions(registry)
    assert out["reconciled_historical_impressions"] == 15
    assert out["individual_2009_descriptions"] == 9
    assert out["anonymous_reconciliation_slots"] == 6
    assert out["2009_figure_panels"] == 8
    assert out["object_support_totals"] == {
        "STORAGE_JAR_RIM": 8, "LOOM_WEIGHT": 5,
        "COMMON_WARE": 1, "AMPHORA": 1,
    }
    assert out["original_inventory_numbers_verified"] == 0
    assert out["translation_validated"] is False


def test_duplicate_local_id_rejected(registry):
    registry["records"][1]["local_record_id"] = registry["records"][0]["local_record_id"]
    with pytest.raises(ValueError, match="Duplicate"):
        audit_impressions(registry)


def test_unverified_official_number_cannot_be_invented(registry):
    registry["records"][0]["official_inventory_id"] = "fictional"
    with pytest.raises(ValueError, match="Official archaeological IDs"):
        audit_impressions(registry)


def test_unexamined_photo_cannot_be_adjudicated(registry):
    registry["records"][0]["photo_independently_read"] = True
    with pytest.raises(ValueError, match="photographic"):
        audit_impressions(registry)


def test_die_identity_cannot_be_assumed(registry):
    registry["records"][0]["stamp_matrix_id"] = "die-1"
    with pytest.raises(ValueError, match="Stamp dies"):
        audit_impressions(registry)


def test_anonymous_slot_cannot_be_promoted(registry):
    r = registry["records"][-1]
    r["family"] = "BALKEI"
    with pytest.raises(ValueError, match="Unidentified 2015"):
        audit_impressions(registry)


def test_2009_partial_o_not_ortinko(registry):
    r = next(x for x in registry["records"] if x["local_record_id"] == "MM09-O-01")
    r["family"] = "ORTINKO"
    with pytest.raises(ValueError, match="Ortinko"):
        audit_impressions(registry)


def test_published_support_distribution_must_reconcile(registry):
    registry["records"][-1]["object_support"] = "AMPHORA"
    with pytest.raises(ValueError, match="object support counts|material support classes"):
        audit_impressions(registry)


def test_kaku_script_uncertainty_preserved(registry):
    r = next(x for x in registry["records"] if x["local_record_id"] == "MM09-KAK-01")
    r["script"] = "IBERIAN"
    with pytest.raises(ValueError, match="kaku script"):
        audit_impressions(registry)


def test_no_semantic_gold_promotion(registry):
    registry["semantic_gold_count"] = 1
    with pytest.raises(ValueError, match="Scientific validation"):
        audit_impressions(registry)


def test_zero_cost_only(registry):
    registry["cost_eur"] = 1
    with pytest.raises(ValueError, match="Costs"):
        audit_impressions(registry)

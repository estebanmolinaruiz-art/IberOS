from iberos.metrology_assemblages_04 import audit
import pytest

def test_no_selection_of_favorable_weights():
    a=audit()
    assert a["published_mass_count"] == 37
    assert a["assemblage_count"] == 5
    assert a["directly_described_2018"] == 5
    assert a["secondary_citations_2018"] == 32
    assert a["count_within_tolerance"] == 22

def test_2018_primary_five_kept_even_if_discordant():
    g=audit()["groups"][0]
    assert [r["mass_g"] for r in g["items"]] == [21.,41.5,62.7,106.5,214.3]
    assert g["within_tolerance"] == 3
    assert not g["items"][2]["within_tolerance"]
    assert not g["items"][3]["within_tolerance"]

def test_preserve_support_and_context():
    g=next(x for x in audit()["groups"] if x["group"]=="ORLEYL_TOMB_11")
    assert [r["support"] for r in g["items"]] == ["LEAD"]*4+["BRONZE"]
    assert not g["independent_sign_readings_available"]

def test_provenance_is_not_ignored():
    g=audit()["groups"][0]
    assert "WITHOUT_CONTROLLED_EXCAVATION" in g["archaeological_context"]
    assert all(x["source_status"] == "SECONDARY_CITATION_2018" for x in audit()["groups"][1:])

def test_no_decipherment_claims():
    a=audit()
    assert a["nonblind_literature_data"]
    assert a["numeric_fit_not_semantic_gold"]
    assert not a["a_o_ki_testable_with_mass_only"]
    assert not a["full3406_accessed"]
    assert not a["official_metrics_changed"]

def test_invalid_thresholds():
    for args in ({"unit_g":0},{"tolerance_percent":-1},{"tolerance_percent":101}):
        with pytest.raises(ValueError):
            audit(**args)

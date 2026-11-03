"""Regression tests for the D1 Serreta formal-sensitivity experiment."""
from iberos.core import OFFICIAL_METRICS
from iberos.serreta_sensitivity import PHYS_ID, run, scenarios, tokens_for


def test_all_eight_scenarios_match_drive_numbering():
    rows = scenarios()
    assert len(rows) == 8
    assert len({(r["B2"], r["B3"], r["B4"]) for r in rows}) == 8
    assert rows[0] == {
        "scenario": "SER-SENS-01", "B2": "dai",
        "B3": "gadenin", "B4": "bidudenin",
    }
    assert rows[1]["B2"] == "darr"
    assert rows[2]["B3"] == "gadedin"
    assert rows[4]["B4"] == "bidudedin"
    assert rows[7]["scenario"] == "SER-SENS-08"


def test_formal_counts_and_fixed_tokens():
    result = run()
    assert result["scenario_count"] == 8
    assert result["stable_segment_count"] == 14
    assert all(r["line_count"] == 5 and r["segment_count"] == 17 for r in result["rows"])
    assert [r["dedin_count"] for r in result["rows"]] == [0, 0, 1, 1, 1, 1, 2, 2]
    assert [r["denin_count"] for r in result["rows"]] == [2, 2, 1, 1, 1, 1, 0, 0]
    assert all(r["iunstir_present"] and r["naltinge_present"] for r in result["rows"])


def test_evidence_is_not_promoted_and_same_object_not_independent():
    result = run()
    assert PHYS_ID
    assert result["independent_physical_objects"] == 1
    assert result["source_level"] == "D1"
    assert result["semantic_validation"] == "NOT_PERFORMED"
    assert result["original_core_semantic_engine_executed"] is False
    assert result["scientific_promotion"] is False
    assert result["official_metrics_changed"] is False
    assert result["official_metrics"] == OFFICIAL_METRICS
    assert all(row["scientific_promotion"] is False for row in result["rows"])


def test_rhotics_are_not_normalized():
    t = [token for line in tokens_for(scenarios()[0]) for token in line]
    assert "basiŕtiŕ" in t
    assert "seŕaikala" in t

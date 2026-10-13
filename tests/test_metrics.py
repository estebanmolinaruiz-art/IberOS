from iberos.core import OFFICIAL_METRICS
from iberos.metrics import metric_registry, compare_metric_values


def test_catalog_preserves_all_frozen_values():
    r = metric_registry()
    assert {key: item["value"] for key, item in r["metrics"].items()} == OFFICIAL_METRICS
    assert r["authority"]["semantic_release"] == "C594"
    assert r["single_global_completion_percentage"] is None
    assert r["historical_pre_github_baseline"] == "NOT_VERIFIED"
    assert r["automatic_core_promotion"] is False


def test_core_denominator_explicit_and_decipherment_never_claimed():
    r = metric_registry()["metrics"]
    assert r["CORE"]["denominator"] == 45
    assert r["CORE_plus_INFER"]["denominator"] == 45
    assert r["ICS_global"]["denominator"] is None
    assert r["INFER_progress"]["denominator"] is None
    assert all(not m["language_decipherment_percentage"] for m in r.values())


def test_rejects_mixed_indicators_as_comparable():
    for a, b in [("CORE", "CORE_plus_INFER"), ("CORE", "ICS_global"),
                 ("INFER_progress", "CORE"), ("ROK", "SALIR")]:
        assert compare_metric_values(a, b)["comparable_as_same_rubric"] is False


def test_same_frozen_core_rubric_can_be_identified():
    assert compare_metric_values("CORE", "CORE")["comparable_as_same_rubric"] is True

"""HOLD-01 leakage and epistemic-lock regression tests."""
from iberos.holdout_01 import CANDIDATES, run


def test_previous_objects_excluded_from_holdout():
    result = run()
    assert {r["id"] for r in result["preexisting_exclusions"]} == {
        "IBR-MUS-0001", "IBR-MUS-0002", "HOLD-01-A"
    }


def test_blind_packet_does_not_reveal_text_or_sources():
    result = run()
    payload = str(result["blinded_packet"])
    assert len(result["blinded_packet"]) == 1
    for c in CANDIDATES:
        assert c.name not in payload
        assert c.phys_id not in payload
        assert c.source not in payload
    assert all(r["grammatical_prediction"] is None for r in result["blinded_packet"])


def test_independence_and_no_grammar_scoring():
    r = run()
    assert len({c.phys_id for c in CANDIDATES}) == 1
    assert len({c.leak_group for c in CANDIDATES}) == 1
    assert r["semantic_gold_available"] == 0
    assert r["score_grammar_accuracy"] is None
    assert not r["independence_certified"]
    assert not r["holdout_locked_for_prospective_claim"]
    assert not r["model_predictions_executed"]
    assert not r["release_promotion"]
    assert not r["official_metrics_changed"]


def test_xabia_documentary_leak_excluded_from_holdout():
    r = run()
    xabia = next(x for x in r["preexisting_exclusions"] if x["id"] == "HOLD-01-A")
    assert xabia["row"] == 4354
    assert xabia["tabs"] == ["text", "cadenes"]
    assert r["external_candidates"] == 1
    assert r["candidate_concordance_status"] == "LA_MESA_PENDING_LEGACY_3406_AUDIT"

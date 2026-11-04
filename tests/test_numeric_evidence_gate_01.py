"""Blind eligibility regression tests: metadata only, synthetic fixtures."""
from iberos.numeric_evidence_gate_01 import gate


def sample(uid, title, split):
    return {"uid": uid, "catalog_id": title, "split_v3_4_9": split}


def test_casinos_hold_overlap_blocked():
    out = gate([sample("P14@R4128", "P14,9 Casinos (València) cara A", "HOLD")])
    item = out["sources"][0]
    assert item["status"] == "HISTORICAL_CORPUS_OVERLAP_BLOCKED"
    assert item["historical_catalog_hits"][0]["historical_split"] == "HOLD"
    assert not item["eligible_for_new_blind_evaluation"]


def test_absent_name_is_not_clean_hold():
    item = gate([sample("other", "Unrelated", "TRAIN")])["sources"][0]
    assert item["status"] == "ABSENCE_BY_NAME_ONLY_NOT_NEWNESS_PROOF"
    assert not item["eligible_for_new_blind_evaluation"]


def test_review_not_specimen():
    item = gate([])["sources"][1]
    assert item["status"] == "REVIEW_ARTICLE_NOT_A_NEW_SPECIMEN"
    assert not item["numeric_value_confirmed"]


def test_does_not_touch_hold_signature():
    class Record(dict):
        def get(self, key, default=None):
            assert key != "signature"
            return super().get(key, default)
    out = gate([Record({**sample("c", "Casinos A", "HOLD"), "signature": object()})])
    assert out["valid"] and not out["hold_signatures_read"]


def test_duplicate_uid_fails():
    assert not gate([sample("a", "Casinos A", "TRAIN"), sample("a", "Casinos B", "VAL")])["valid"]


def test_no_semantic_promotion():
    out = gate([])
    assert not out["numeric_semantics_validated"]
    assert not out["training_or_scoring_executed"]
    assert not out["official_metrics_changed"]

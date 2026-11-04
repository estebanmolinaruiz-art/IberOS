"""Cluster-aware falsification tests with synthetic records only."""
from iberos.morph_rivals_02 import analyze


def item(uid, sign, split="TRAIN", dep=None):
    return {"uid":uid,"signature":sign,"split_v3_4_9":split,
            "dependency_key_v3_4_9":dep or uid}


def test_terminal_vs_internal_and_boundaries():
    rows=[item("a","BI-N¦BA-N-X"),item("b","BA-N¦BI¦N")]
    result=analyze(rows)
    assert result["valid"]
    x=result["metrics"]["TRAIN"]
    assert x["BI_N"]["occurrences"] == 1
    assert x["BI_N"]["terminal_occurrences"] == 1
    assert x["BA_N"]["occurrences"] == 2
    assert x["BA_N"]["terminal_occurrences"] == 1


def test_cluster_duplicate_editions_are_not_independent():
    rows=[item("a","BI-N","TRAIN","same"),item("b","BI-N","TRAIN","same")]
    r=analyze(rows)["metrics"]["TRAIN"]["BI_N"]
    assert r["uid_records"]==2
    assert r["dependency_groups"]==1
    assert r["dependency_groups_with_terminal_occurrence"]==1


def test_hold_and_excluded_are_never_read_as_signatures():
    rows=[item("train","BA-N"),item("h","BI-N","HOLD"),
          item("x","BI-N","EXCLUDED")]
    r=analyze(rows)
    assert r["valid"]
    assert r["excluded_from_analysis"] == {"HOLD":1, "EXCLUDED":1}
    assert r["hold_records_inspected_for_signature"]==0
    assert r["metrics"]["TRAIN"]["BI_N"]["occurrences"]==0


def test_train_val_dependency_overlap_fails_closed():
    r=analyze([item("a","BI-N","TRAIN","same"),item("b","BA-N","VAL","same")])
    assert not r["valid"]
    assert "TRAIN_VAL_DEPENDENCY_OVERLAP" in r["issues"]


def test_duplicate_uid_fails_closed():
    r=analyze([item("a","BI-N"),item("a","BI-N")])
    assert not r["valid"]


def test_rivals_do_not_pretend_meaning_or_significance():
    r=analyze([item("a","BI-N"),item("b","BA-N")])
    assert r["semantic_gold"] == 0
    assert not r["linguistic_translation_validated"]
    assert r["observations"]["TRAIN"]["cluster_independence_p_value"] is None
    assert not r["official_metrics_changed"]

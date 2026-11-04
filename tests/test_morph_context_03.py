"""Adversarial and non-semantic controls of MORPH-CONTEXT-03."""
from iberos.morph_context_03 import analyze, read_segments


def r(uid, sig, split="TRAIN", group=None, support=None):
    return {"uid":uid, "signature":sig, "split_v3_4_9":split,
            "dependency_key_v3_4_9":group or uid, "support":support}


def test_neighbor_boundaries_no_cross_segment():
    assert read_segments("BI¦N") == [["BI"],["N"]]
    o=analyze([r("a","R1-BI-N-KE¦BI¦N")])
    z=o["results"]["TRAIN"]["BI_N"]
    assert z["occurrences"]==1
    assert z["preceding_signs"]==[{"token":"R1","count":1}]
    assert z["following_signs"]==[{"token":"KE","count":1}]


def test_support_kept_raw_and_missing_explicit():
    out=analyze([r("a","BI-N","TRAIN","grp","plom"),
                 r("b","BI-N","TRAIN","grp",None)])
    x=out["results"]["TRAIN"]["BI_N"]
    assert x["uid_records"]==2
    assert x["dependency_groups"]==1
    assert x["groups_with_missing_support"]==1
    assert {"token":"plom","count":1} in x["editorial_support_labels"]


def test_context_position_and_cluster_concentration():
    out=analyze([r("a","BI-N¦S-BI-N-KE","TRAIN","grp"),
                 r("b","BI-N","TRAIN","grp")])
    x=out["results"]["TRAIN"]["BI_N"]
    assert x["occurrences"]==3
    assert x["initial_occurrences"]==2
    assert x["terminal_occurrences"]==2
    assert x["max_occurrences_in_one_dependency_group"]==3


def test_hold_not_read_even_with_nonstring_signature():
    out=analyze([r("a","BI-N"),r("b",object(),"HOLD"),
                 r("c",object(),"EXCLUDED")])
    assert out["valid"] and out["hold_signatures_inspected"]==0
    assert out["excluded_from_motif_analysis"]=={"HOLD":1,"EXCLUDED":1}


def test_duplicate_uid_fails_closed():
    assert not analyze([r("a","BI-N"),r("a","BA-N")])["valid"]


def test_train_val_group_overlap_fails_closed():
    x=analyze([r("a","BI-N","TRAIN","grp"),r("b","BA-N","VAL","grp")])
    assert not x["valid"]


def test_no_gold_or_semantics():
    out=analyze([r("a","BI-N")])
    assert out["data_mode"]=="RETROSPECTIVE_DESCRIPTIVE_NOT_INDEPENDENT_VALIDATION"
    assert out["translation_validated"] is False
    assert out["numeric_gold_available"] is False
    assert out["official_metrics_changed"] is False

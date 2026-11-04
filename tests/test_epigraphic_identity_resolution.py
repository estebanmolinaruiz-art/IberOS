"""Adversarial controls for historical epigraphic identity reconciliation."""
from iberos.epigraphic_identity_resolution import (
    PECH_TEXT_UIDS, PECH_EDITORIAL_NOTE_UID, VISPESA_UIDS, reconcile
)


def fixture():
    group = "pech-one-object"
    return [
        {"uid": PECH_TEXT_UIDS[0], "signature": "S-R-I", "split_v3_4_9": "VAL",
         "dependency_key_v3_4_9": group},
        {"uid": PECH_TEXT_UIDS[1], "signature": "B-I", "split_v3_4_9": "VAL",
         "dependency_key_v3_4_9": group},
        {"uid": PECH_EDITORIAL_NOTE_UID, "signature": "", "split_v3_4_9": "VAL",
         "dependency_key_v3_4_9": group},
        {"uid": VISPESA_UIDS[0], "signature": "T-A", "split_v3_4_9": "HOLD",
         "dependency_key_v3_4_9": "vispesa-hands"},
        {"uid": VISPESA_UIDS[1], "signature": "B-I", "split_v3_4_9": "TRAIN",
         "dependency_key_v3_4_9": "vispesa-horses"},
    ]


def test_single_physical_pech_maho_not_three_independent_texts():
    data = fixture()
    result = reconcile(data)
    assert result["status"] == "PASS_WITH_EPISTEMIC_LOCKS"
    assert result["pech_maho"]["independent_texts"] == 1
    assert result["pech_maho"]["editorial_notes_excluded_from_text_analysis"] == 1
    assert not result["original_splits_modified"]
    assert data[0]["split_v3_4_9"] == "VAL"


def test_vispesa_monumental_dependency_remains_conservatively_blocked():
    result = reconcile(fixture())
    assert result["la_vispesa"]["same_monument"] == "DISPUTED_IN_LITERATURE"
    assert not result["la_vispesa"]["prospective_holdout_eligible"]
    assert not result["scientific_promotion"]


def test_duplicate_uid_fails_closed():
    data = fixture()
    data.append(dict(data[0]))
    assert reconcile(data)["status"] == "FAIL_CLOSED"


def test_note_with_signature_fails_closed():
    data = fixture()
    data[2]["signature"] = "TEST"
    assert "EDITORIAL_NOTE_IS_NOT_EMPTY" in reconcile(data)["issues"]


def test_pech_split_drift_fails_closed():
    data = fixture()
    data[1]["split_v3_4_9"] = "TRAIN"
    assert "PECH_SPLIT_CHANGED" in reconcile(data)["issues"]


def test_vispesa_group_collapse_does_not_silently_pass():
    data = fixture()
    data[-1]["dependency_key_v3_4_9"] = data[-2]["dependency_key_v3_4_9"]
    assert "VISPESA_DEPENDENCY_KEY_CHANGED" in reconcile(data)["issues"]

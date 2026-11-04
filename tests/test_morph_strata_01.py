"""Adversarial fixtures for graphemic counts, without private corpus in CI."""
from iberos.morph_strata_01 import token_segments, count_occurrences, audit_records, audit_file
import pytest


def record(uid, signature, split="TRAIN", dep=None):
    return {"uid":uid, "signature":signature, "split_v3_4_9":split,
            "dependency_key_v3_4_9":dep or uid}


def test_boundaries_and_rhotics():
    assert token_segments("KU-TU¦R1") == [["KU", "TU"], ["R1"]]
    r = audit_records([record("a","KU-TU¦R1"),record("b","KU-TU-R1"),record("c","KU-TU-R")])
    assert r["results"]["KUTUR_ORTHOGRAPHIC_VARIANTS"]["total_uid_records"] == 2
    assert r["results"]["KU_TU_R1"]["total_uid_records"] == 1


def test_bi_not_inside_person_name():
    r = audit_records([record("a","BI-U-R1"),record("b","BI"),record("c","BA-I-TE-S-BI")])
    assert r["results"]["BI_ISOLATED"]["total_uid_records"] == 1
    assert r["results"]["BI_N"]["total_uid_records"] == 0


def test_group_collapse_without_split_mutation():
    r = audit_records([record("a","BI-N","HOLD","shared"),
                       record("b","BI-N","HOLD","shared"),
                       record("c","BI-N","TRAIN","other")])
    assert r["results"]["BI_N"]["total_uid_records"] == 3
    assert r["results"]["BI_N"]["total_dependency_units"] == 2
    assert not r["frozen_splits_modified"]


def test_excluded_ignored():
    r = audit_records([record("a","BA-I-TE-S","EXCLUDED"),record("b","BA-I-TE-S","VAL")])
    assert r["results"]["BA_I_TE_S"]["total_uid_records"] == 1


def test_no_grammar_or_semantics_claim():
    r = audit_records([record("a","BA-I-TE-S-BI¦BA-TI-R1¦KU-TU-R")])
    assert r["valid"] and r["grammatical_accuracy"] is None
    assert not r["training_or_prediction_executed"] and r["semantic_gold_available"] == 0


def test_duplicate_uid_rejected():
    r = audit_records([record("a","BI-N"),record("a","BI-N")])
    assert not r["valid"] and "DUPLICATE_UID:a" in r["errors"]


def test_corrupted_snapshot_rejected(tmp_path):
    p=tmp_path/"snapshot.json";p.write_text('{"records":[]}',encoding="utf-8")
    with pytest.raises(ValueError,match="SHA256"):
        audit_file(p)

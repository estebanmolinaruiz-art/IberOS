"""Fail-closed external crosswalk tests: no I-code/MLH conflation."""
import pytest
from iberos.external_crosswalk import build_external_bridge


def record(uid, catalog, split="TRAIN"):
    return {"uid":uid, "catalog_id":catalog, "split_v3_4_9":split}


def link(obj, ids="I01126;I01127", labels="c.2.3 a;c.2.3 b", status="FULL_GROUP_VERIFIED"):
    return {"OBJECT_ID":obj, "UPSTREAM_IDS":ids, "Upstream_Labels":labels,
            "Verified_ID_Count":str(len(ids.split(";"))),
            "Link_Status":status,"Confidence":"HIGH",
            "Source_URL":"https://cathalaunia.org/Iberika/I01126"}


def registry(obj, ref="C.2.3"):
    return {"OBJECT_ID":obj, "Referencia epigráfica":ref}


def test_upstream_group_and_historical_editorial_not_equated():
    result = build_external_bridge([registry("U")],[link("U")],
        [record("c.2.3 a@R1431","c.2.3 a","VAL")])
    assert result["valid"]
    assert result["distinct_external_I_codes"] == 2
    assert result["distinct_historical_label_uids"] == 1
    assert not result["records"][0]["identity_crosswalk_certified"]
    assert not result["promotion_permitted"]


def test_hesperia_bdh_does_not_automatically_match_mlh():
    result = build_external_bridge([registry("T","BDH V.21.01-02")],
        [link("T","I03049;I03050","P11,9 Tos Pelat A2b1;A2b2","PARTIAL_GROUP")],
        [record("potential","v.21.01","TRAIN")])
    assert result["records"][0]["historical_mlh_candidate_count"] == 0
    assert result["records"][0]["historical_label_candidate_count"] == 0
    assert result["records"][0]["risk"] == "PARTIAL_SOURCE_GROUP"


def test_collision_exact_label_and_prefix():
    result = build_external_bridge([registry("U")], [link("U","I01126","c.2.3 a")],
        [record("ok","c.2.3 a"), record("wrong","c.2.3 ab")])
    assert result["records"][0]["historical_label_candidate_uids"] == ["ok"]


def test_invalid_upstream_duplicate_cross_object_is_blocked():
    result = build_external_bridge([registry("U"),registry("V")],
        [link("U","I01126","c.2.3 a"),link("V","I01126","f.17.1 a")], [])
    assert not result["valid"]
    assert "UPSTREAM_ID_SHARED_BY_DIFFERENT_OBJECTS" in [
        e["error"] for e in result["invalid"]]


def test_missing_object_and_bad_count_are_rejected():
    x=link("NONCURATED","I99999","f.1.1")
    x["Verified_ID_Count"]="2"
    result = build_external_bridge([registry("U")],[x],[])
    assert {"OBJECT_NOT_CURATED","DECLARED_EXTERNAL_ID_COUNT_MISMATCH"} <= {
        e["error"] for e in result["invalid"]}


def test_same_historical_uid_no_physical_inference():
    result = build_external_bridge([registry("U")], [link("U","I01126","c.2.3 a")],
                                   [record("one","c.2.3 a")])
    assert not result["records"][0]["physical_independence_certified"]
    assert not result["records"][0]["grammatical_gold_available"]

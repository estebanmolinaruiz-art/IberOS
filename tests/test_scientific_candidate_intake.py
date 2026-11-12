"""SCI-PRED-04 intake controls; all human readings in tests are SYNTHETIC."""
import copy
import json
from pathlib import Path

import pytest

from iberos.scientific_candidate_intake import audit
from iberos.prospective_role_lock import seal

ROOT = Path(__file__).resolve().parents[1]


def record(i=1):
    persons = [
        {"person_id": "A", "name_form": "foo-te",
         "name_status": "INDEPENDENTLY_IDENTIFIED"},
        {"person_id": "B", "name_form": "bar",
         "name_status": "INDEPENDENTLY_IDENTIFIED"},
    ]
    return {
        "candidate_id": f"SYNTHETIC-LEAD-{i}",
        "physical_id": f"SYNTHETIC-PHYS-{i}",
        "documentary_lineage_id": f"SYNTHETIC-LINEAGE-{i}",
        "aliases": [f"TEST-{i}"],
        "reading_source_url": "https://example.org/synthetic/read",
        "image_reference_url": "https://example.org/synthetic/image",
        "image_sha256": "a" * 64,
        "script": "IBERIAN", "context_type": "BUILDING",
        "prior_exposure": "NEW_DECLARED",
        "physical_audit_reference": "https://example.org/synthetic/identity",
        "physical_auditor": "synthetic-expert",
        "sign_reviews": [
            {"reviewer_id": "synthetic-r1", "independence_group": "group-a",
             "source_image_sha256": "a" * 64,
             "method": "DIRECT_IMAGE", "blind_to_editorial": True,
             "participants": persons},
            {"reviewer_id": "synthetic-r2", "independence_group": "group-b",
             "source_image_sha256": "a" * 64,
             "method": "DIRECT_IMAGE", "blind_to_editorial": True,
             "participants": copy.deepcopy(persons)},
        ],
    }


def wrap(*records):
    return {"schema": "SCI-PRED-04/1", "candidates": list(records)}


def test_empty_queue_reports_zero_not_fake_success():
    out = audit(wrap())
    assert out["total_leads"] == 0
    assert out["ready_for_external_admission_audit"] == 0
    assert out["translation_validated"] is False
    assert out["gold_labels_consumed"] is False


def test_existing_real_candidates_are_all_retrospective():
    data = json.loads((ROOT / "data/review/sci_pred04_candidate_queue_v1.json").read_text(encoding="utf-8"))
    out = audit(data)
    assert out["total_leads"] == 5
    assert out["ready_for_external_admission_audit"] == 0
    assert all(x["state"] == "EXCLUDED_FROM_PROSPECTIVE_HOLD" for x in out["results"])
    assert all(x["blind_packet_preview"] is None for x in out["results"])


def test_complete_synthetic_packet_still_requires_external_auditor():
    out = audit(wrap(record()))["results"][0]
    assert out["state"] == "READY_FOR_EXTERNAL_ADMISSION_AUDIT"
    assert out["automatic_sealing_permitted"] is False
    assert out["independent_admission_verified"] is False
    preview = out["blind_packet_preview"]
    assert preview["independence_status"] == "REQUIRES_EXTERNAL_AUDIT"
    proto = json.loads((ROOT / "research/protocols/SCI_PRED_02_FUTURE_ROLE_RULE_20261112.json").read_text(encoding="utf-8"))
    with pytest.raises(ValueError, match="independence"):
        seal(preview, proto)


@pytest.mark.parametrize("field,val", [
    ("prior_exposure", "KNOWN_TRAIN"),
    ("prior_exposure", "UNKNOWN"),
    ("prior_exposure", "KNOWN_HOLD"),
])
def test_exposure_excludes_even_when_reviewers_seem_ready(field, val):
    c = record()
    c[field] = val
    out = audit(wrap(c))["results"][0]
    assert out["state"] == "EXCLUDED_FROM_PROSPECTIVE_HOLD"
    assert out["blind_packet_preview"] is None


@pytest.mark.parametrize("key,value", [
    ("gold", "PRODUCER"), ("translation", "meaning"),
    ("roles", {"A": "PRODUCER"}), ("true_role", "COMMISSIONER"),
])
def test_gold_leakage_raises_before_any_prediction(key, value):
    c = record()
    c[key] = value
    with pytest.raises(ValueError):
        audit(wrap(c))
    c = record()
    c["sign_reviews"][0][key] = value
    with pytest.raises(ValueError):
        audit(wrap(c))


def test_forged_independent_review_group_is_rejected():
    c = record()
    c["sign_reviews"][1]["independence_group"] = "group-a"
    out = audit(wrap(c))["results"][0]
    assert "REVIEWERS_NOT_INDEPENDENT" in out["issues"]
    assert out["blind_packet_preview"] is None


def test_two_different_readings_need_human_adjudication():
    c = record()
    c["sign_reviews"][1]["participants"][0]["name_form"] = "foo-ke"
    out = audit(wrap(c))["results"][0]
    assert "SIGN_READINGS_OR_PERSON_SPANS_DISAGREE" in out["issues"]
    assert out["state"] == "BLOCKED_EVIDENCE"


def test_same_physical_object_and_same_punch_are_not_independent():
    a, b = record(1), record(2)
    b["physical_id"] = a["physical_id"]
    b["documentary_lineage_id"] = a["documentary_lineage_id"]
    out = audit(wrap(a, b))
    assert "REPEATED_PHYSICAL_OBJECT" in out["results"][1]["issues"]
    assert "REPEATED_PUNCH_OR_EDITORIAL_LINEAGE" in out["results"][1]["issues"]
    assert out["results"][1]["state"] == "DUPLICATE_DEPENDENCY_BLOCK"


def test_gaps_block_with_explicit_reason_codes():
    c = record()
    c["sign_reviews"] = []
    c["image_sha256"] = ""
    out = audit(wrap(c))["results"][0]
    assert "TWO_BLIND_SIGN_READINGS_REQUIRED" in out["issues"]
    assert "SOURCE_IMAGE_HASH_REQUIRED" in out["issues"]
    assert out["blind_packet_preview"] is None


def test_reject_duplicate_candidate_identifier():
    with pytest.raises(ValueError, match="candidate_id"):
        audit(wrap(record(), record()))


def test_reuse_of_known_editorial_alias_cannot_be_mislabeled_new():
    known = record(1)
    known["prior_exposure"] = "KNOWN_TRAIN"
    new = record(2)
    new["aliases"] = [known["aliases"][0].lower()]
    result = audit(wrap(known, new))["results"][1]
    assert "REUSED_EDITORIAL_ALIAS" in result["issues"]
    assert result["state"] == "DUPLICATE_DEPENDENCY_BLOCK"
    assert result["blind_packet_preview"] is None

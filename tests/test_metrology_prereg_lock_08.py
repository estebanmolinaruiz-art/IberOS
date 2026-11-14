from iberos.metrology_prereg_lock_08 import inspect_contract, canonical_digest
from iberos.metrology_admission_07 import REQUIRED_PROSPECTIVE
import pytest


def specimen():
    return dict(object_id="SYNTHETIC", institution="TEST",
        inventory_id="TEST-I", physical_object_identity="TEST-UNIQUE",
        context_reference="institutional archive", image_reference="photo ID",
        image_rights="allowed", reading_reference="blind transcriptions",
        mass_g=42.0, resolution_g=0.01, uncertainty_g=0.1,
        instrument_id="BAL-1", calibration_reference="CAL-1",
        measurement_date="2026-11-09", conservation_assessment="intact",
        independent_mark_readings=[
            dict(reading="o",reader_id="A",reading_date="2026-11-09",blind_to_weight_and_model=True),
            dict(reading="o",reader_id="B",reading_date="2026-11-09",blind_to_weight_and_model=True)],
        **{field:True for field in REQUIRED_PROSPECTIVE})


def contract():
    pred=[dict(object_id="SYNTHETIC",model_id=x,predicted_quantity=10,
        prediction_unit="units",abstention_rule="no eligible data => abstain",
        negative_control_plan="independent blanks") for x in
          ("A_O_KI_10_12","WEIGHT_FAMILY_2_1_G","NULL_BASELINE")]
    hashvalue=canonical_digest(pred)
    fields=("institutional_inventory_evidence", "physical_alias_audit_evidence",
            "instrument_calibration_evidence", "independent_mark_reading_evidence",
            "external_preregistration_record", "independent_quantity_label_evidence")
    refs={k:{"uri":f"https://example.org/{k}","sha256":("a"*64 if k!="external_preregistration_record" else hashvalue),
            "recorded_at":"2026-11-09T12:00:00Z" if k!="independent_quantity_label_evidence" else "2026-11-10T12:00:00Z",
            "custodian":"test external archive"} for k in fields}
    return dict(specimen=specimen(),predictions=pred,evidence=refs)


def test_missing_everything_abstains():
    out=inspect_contract({})
    assert not out["local_formally_complete"]
    assert not out["ready_for_independent_evaluation"]


def test_formal_completeness_is_not_external_verification():
    out=inspect_contract(contract())
    assert out["local_formally_complete"]
    assert out["status"]=="AWAITING_EXTERNAL_VERIFICATION"
    assert not out["external_issuer_and_hash_verified"]
    assert not out["ready_for_independent_evaluation"]


def test_hash_tampering_detected():
    c=contract()
    c["predictions"][0]["predicted_quantity"]=12
    assert "PREREGISTERED_HASH_MISMATCH" in inspect_contract(c)["issues"]


def test_postdated_registration_rejected():
    c=contract()
    c["evidence"]["external_preregistration_record"]["recorded_at"]="2026-11-11T12:00:00Z"
    assert "PREDICTION_NOT_BEFORE_INDEPENDENT_LABEL" in inspect_contract(c)["issues"]


def test_missing_rival_and_null_rejected():
    c=contract()
    c["predictions"]=c["predictions"][:2]
    assert "THREE_RIVAL_MODELS_REQUIRED" in inspect_contract(c)["issues"]


def test_boolean_quantity_rejected():
    c=contract()
    c["predictions"][0]["predicted_quantity"]=True
    assert "PREDICTION_0_QUANTITY_NOT_NUMERIC" in inspect_contract(c)["issues"]


def test_invalid_future_synthetic_evidence_is_not_real_museum_validation():
    c=contract()
    c["evidence"]["institutional_inventory_evidence"]["uri"]="file:///tmp/foo"
    assert "MISSING_VERIFIABLE_REFERENCE_INSTITUTIONAL_INVENTORY_EVIDENCE" in inspect_contract(c)["issues"]


def test_no_full3406_gold_or_madeup_accuracy():
    out=inspect_contract(contract())
    assert out["accuracy"] is None and out["interpretation"] is None
    assert not out["full3406_accessed"] and not out["official_metrics_modified"]


def test_canonical_hash_order_independent():
    a=contract()["predictions"]
    b=[dict(reversed(list(item.items()))) for item in a]
    assert canonical_digest(a)==canonical_digest(b)


def test_bad_contract_rejected():
    with pytest.raises(ValueError):
        inspect_contract(None)

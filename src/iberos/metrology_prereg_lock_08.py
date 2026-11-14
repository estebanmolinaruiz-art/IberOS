"""METROLOGY-PREREG-LOCK-08: evidence-bound prospective experiment contract.

This module does NOT prove any external timestamp or attest a real object.
A hash proves byte integrity only. Claims of novelty, independent review,
and preregistration need separate institutional/public verification.
"""
from __future__ import annotations
import argparse
from datetime import datetime, timezone
from hashlib import sha256
import json
from pathlib import Path
from urllib.parse import urlparse
from .metrology_admission_07 import assess

REQUIRED_ATTESTATIONS = (
    "institutional_inventory_evidence", "physical_alias_audit_evidence",
    "instrument_calibration_evidence", "independent_mark_reading_evidence",
    "external_preregistration_record",
    "independent_quantity_label_evidence",
)
REQUIRED_PREDICTIONS = ("object_id", "model_id", "predicted_quantity",
                        "prediction_unit", "abstention_rule", "negative_control_plan")
ALLOWED_MODELS = ("A_O_KI_10_12", "WEIGHT_FAMILY_2_1_G", "NULL_BASELINE")


def _time(value: str):
    if not isinstance(value, str):
        return None
    try:
        dt = datetime.fromisoformat(value.replace("Z", "+00:00"))
        return dt.astimezone(timezone.utc) if dt.tzinfo else None
    except ValueError:
        return None


def _external_reference(value):
    if not isinstance(value, dict):
        return False
    uri = value.get("uri")
    digest = value.get("sha256")
    if not isinstance(uri, str) or not isinstance(digest, str):
        return False
    parsed = urlparse(uri)
    return (parsed.scheme == "https" and bool(parsed.netloc)
            and len(digest) == 64 and all(c in "0123456789abcdef" for c in digest.lower())
            and _time(value.get("recorded_at")) is not None
            and isinstance(value.get("custodian"), str) and bool(value["custodian"].strip()))


def canonical_digest(predictions: list[dict]) -> str:
    raw = json.dumps(predictions, sort_keys=True, separators=(",", ":"),
                     ensure_ascii=False, allow_nan=False).encode("utf-8")
    return sha256(raw).hexdigest()


def inspect_contract(contract: dict) -> dict:
    if not isinstance(contract, dict):
        raise ValueError("CONTRACT_MUST_BE_OBJECT")
    issues = []
    specimen = contract.get("specimen")
    admission = assess(specimen if isinstance(specimen, dict) else {})
    if not admission["documentation_complete"]:
        issues.append("PRIMARY_DOCUMENTATION_INCOMPLETE")
    if admission["prospective_issues"]:
        issues.append("PROSPECTIVE_DECLARATIONS_INCOMPLETE")
    evidence = contract.get("evidence")
    if not isinstance(evidence, dict):
        evidence = {}
    for field in REQUIRED_ATTESTATIONS:
        if not _external_reference(evidence.get(field)):
            issues.append("MISSING_VERIFIABLE_REFERENCE_" + field.upper())
    predictions = contract.get("predictions")
    if not isinstance(predictions, list) or not predictions:
        issues.append("NO_PREDICTIONS")
        predictions = []
    for i, row in enumerate(predictions):
        if not isinstance(row, dict):
            issues.append(f"INVALID_PREDICTION_{i}")
            continue
        for field in REQUIRED_PREDICTIONS:
            if field not in row or isinstance(row[field], (dict, list)) or row[field] in ("", None):
                issues.append(f"PREDICTION_{i}_MISSING_{field.upper()}")
        if row.get("model_id") not in ALLOWED_MODELS:
            issues.append(f"PREDICTION_{i}_UNKNOWN_MODEL")
        if row.get("object_id") != admission["object_id"]:
            issues.append(f"PREDICTION_{i}_OBJECT_MISMATCH")
        if isinstance(row.get("predicted_quantity"), bool) or not isinstance(row.get("predicted_quantity"), (int, float)):
            issues.append(f"PREDICTION_{i}_QUANTITY_NOT_NUMERIC")
    specified = {r.get("model_id") for r in predictions if isinstance(r, dict)}
    if set(ALLOWED_MODELS) != specified:
        issues.append("THREE_RIVAL_MODELS_REQUIRED")
    label_ref = evidence.get("independent_quantity_label_evidence")
    pre_ref = evidence.get("external_preregistration_record")
    if _external_reference(pre_ref) and _external_reference(label_ref):
        if _time(pre_ref["recorded_at"]) >= _time(label_ref["recorded_at"]):
            issues.append("PREDICTION_NOT_BEFORE_INDEPENDENT_LABEL")
    dig = None
    if predictions:
        try:
            dig = canonical_digest(predictions)
        except (TypeError, ValueError):
            issues.append("PREDICTION_NOT_CANONICAL_JSON")
    if dig and _external_reference(pre_ref) and pre_ref.get("sha256", "").lower() != dig:
        issues.append("PREREGISTERED_HASH_MISMATCH")
    # Intentionally NEVER declare evidence independently verified from mere
    # user-supplied links, dates, digests, checkboxes or synthetic fixture.
    return {
        "experiment": "METROLOGY_PREREG_LOCK_08",
        "object_id": admission["object_id"],
        "prediction_digest_sha256": dig,
        "local_formally_complete": not issues,
        "external_issuer_and_hash_verified": False,
        "ready_for_independent_evaluation": False,
        "status": "AWAITING_EXTERNAL_VERIFICATION" if not issues else "ABSTAIN_EVIDENCE_GAPS",
        "issues": issues,
        "interpretation": None,
        "accuracy": None,
        "full3406_accessed": False,
        "official_metrics_modified": False,
    }


def main(argv=None):
    p = argparse.ArgumentParser()
    p.add_argument("contract", type=Path)
    p.add_argument("--json", type=Path)
    args = p.parse_args(argv)
    if args.json and args.json.resolve() == args.contract.resolve():
        raise ValueError("REFUSE_OVERWRITE_INPUT")
    payload = json.loads(args.contract.read_text(encoding="utf-8"))
    report = inspect_contract(payload)
    s = json.dumps(report, ensure_ascii=False, indent=2) + "\n"
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(s, encoding="utf-8")
    else:
        print(s, end="")
    return 0 if report["local_formally_complete"] else 2


if __name__ == "__main__":
    raise SystemExit(main())

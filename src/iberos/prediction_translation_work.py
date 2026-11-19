"""SCI-PRED-01: rival possible translations with falsifiable predictions.

This is a *hypothesis docket*, not a translation model or linguistic gold set.
It reuses curated object identities and never changes frozen CORE metrics or HOLD.
"""
from __future__ import annotations

import hashlib
import json
from urllib.parse import urlsplit

from .core import AUTHORITY, get_object

SCHEMA = "IberOS-Prediction-Translation-Docket/1.0"
LEVELS = frozenset({"D1", "D2", "D3"})


def _text(record: dict, key: str) -> str:
    value = record.get(key)
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"Missing nonempty {key}")
    return value.strip()


def _https(url: str) -> bool:
    parsed = urlsplit(url)
    return parsed.scheme == "https" and bool(parsed.netloc) and not (
        parsed.username or parsed.password
    )


def _hash_json(value: dict) -> str:
    canonical = json.dumps(value, ensure_ascii=False, sort_keys=True,
                           separators=(",", ":"))
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


def build_docket(document: dict) -> dict:
    """Validate case identities and emit only unverified, testable rivals.

    All admitted cases here are historical TRAIN references; HOLD data are
    forbidden even when a caller claims to have verified a reading or label.
    Timestamp priority, semantic scores and successful translation are NOT
    asserted by this function. A separate external adjudication is required.
    """
    if not isinstance(document, dict) or document.get("schema") != "SCI-PRED-01/1":
        raise ValueError("Unknown prediction docket input schema")
    cases = document.get("cases")
    if not isinstance(cases, list) or not 1 <= len(cases) <= 25:
        raise ValueError("Expected 1 to 25 historical cases")
    seen_cases = set()
    output = []
    physical_groups = set()
    for case in cases:
        if not isinstance(case, dict):
            raise ValueError("Case must be an object")
        cid = _text(case, "case_id")
        oid = _text(case, "object_id")
        phys = _text(case, "physical_id")
        source = _text(case, "reading_source_url")
        transcription = _text(case, "editorial_transcription")
        level = _text(case, "reading_level")
        role = _text(case, "evaluation_role")
        if cid in seen_cases:
            raise ValueError("Duplicate case_id")
        seen_cases.add(cid)
        if get_object(oid) is None:
            raise ValueError("Object not present in curated registry")
        if not _https(source):
            raise ValueError("A valid HTTPS reading source is required")
        if level not in LEVELS:
            raise ValueError("Unknown epigraphic evidence level")
        if role != "RETROSPECTIVE_ONLY":
            raise ValueError("HOLD/VAL or prospective content cannot enter this docket")
        if case.get("independent_semantic_gold") is not False:
            raise ValueError("No independent semantic gold is admitted here")
        if case.get("translation_validated") is not False:
            raise ValueError("No validated translation may be declared here")
        hypotheses = case.get("hypotheses")
        if not isinstance(hypotheses, list) or not 2 <= len(hypotheses) <= 8:
            raise ValueError("Each case requires 2-8 competing hypotheses")
        names, predictions = set(), set()
        rivals = []
        for hyp in hypotheses:
            if not isinstance(hyp, dict):
                raise ValueError("Hypothesis must be an object")
            hid = _text(hyp, "hypothesis_id")
            translation = _text(hyp, "possible_translation")
            prediction = _text(hyp, "falsifiable_prediction")
            disconfirmation = _text(hyp, "disconfirming_observation")
            basis = _text(hyp, "documentary_basis")
            if hid in names or prediction in predictions:
                raise ValueError("Duplicate hypothesis or indistinguishable prediction")
            names.add(hid)
            predictions.add(prediction)
            statement = {
                "object_id": oid,
                "physical_id": phys,
                "hypothesis_id": hid,
                "possible_translation": translation,
                "falsifiable_prediction": prediction,
                "disconfirming_observation": disconfirmation,
                "documentary_basis": basis,
                "editorial_transcription": transcription,
                "reading_source_url": source,
            }
            rivals.append({
                **statement,
                "statement_sha256": _hash_json(statement),
                "epistemic_layer": "HYPOTHESIS",
                "prediction_lock_state": "NOT_PROSPECTIVELY_LOCKED",
                "evaluation_state": "NOT_EVALUATED",
                "semantic_gold": None,
                "estimated_probability": None,
                "translation_validated": False,
            })
        physical_groups.add(phys)
        output.append({
            "case_id": cid,
            "object_id": oid,
            "physical_id": phys,
            "reading_level": level,
            "evaluation_role": role,
            "hypotheses": rivals,
            "reading_independently_adjudicated_here": False,
        })
    return {
        "schema": SCHEMA,
        "authority": dict(AUTHORITY),
        "experiment": "SCI-PRED-01",
        "cases": output,
        "historical_cases": len(output),
        "independent_physical_objects_represented": len(physical_groups),
        "rival_hypotheses": sum(len(x["hypotheses"]) for x in output),
        "semantically_evaluated_predictions": 0,
        "translation_accuracy": None,
        "preregistration_verified": False,
        "external_reviewer_completed": False,
        "translation_validated": False,
        "automatic_core_promotion": False,
        "next_gate": (
            "Lock a prediction before viewing new external evidence; establish "
            "independent physical identity, blind sign readings and context gold; "
            "evaluate rival predictions and abstentions on unseen objects."
        ),
        "notice": (
            "Hashes only identify exact statements; they do not prove dates, "
            "prediction accuracy, or priority. All possible translations are hypotheses."
        ),
    }

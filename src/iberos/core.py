from __future__ import annotations

import csv
import json
import re
from pathlib import Path
from typing import Any

try:
    from jsonschema import Draft202012Validator
except ImportError:
    Draft202012Validator = None

PACKAGE_ROOT = Path(__file__).resolve().parent
REPO_ROOT = PACKAGE_ROOT.parent.parent.parent

ENGINE_PROTOCOL_VERSION = "CORE-GUARDS-0.1"

AUTHORITY = {
    "semantic_release": "C594",
    "prospective_lock": "C474",
    "technical_floor": "C539",
    "rok_network": "C541",
}

OFFICIAL_METRICS = {
    "ICS_global": 70.8,
    "ROK": 75,
    "KA_KE": 75,
    "SALIR": 75,
    "KUTUR": 75,
    "BAIDES_BATIR": 75,
    "D_E_I": 50,
    "CORE": "27/45 = 60.0%",
    "CORE_plus_INFER": "28/45 = 62.2%",
    "INFER_progress": 98,
}

ACTIVE_PROTOCOLS = {
    "BI-DISAMBIG-01": (
        "BI/BIN=2 is allowed only when the context is independently quantitative; "
        "BI in BI+D(E/I)+V is non-numeral by default."
    ),
    "PALEO-RHOTIC-LOCK-01": (
        "R/R1 must be preserved for grouping, independence, splits and promotion; "
        "neutralization is permitted only as a search key."
    ),
    "ROK-DIRECTION-GUARD-01": (
        "ROK is a transfer-related functional domain; exact direction and "
        "giver/receiver mapping remain open."
    ),
    "EPISTEMIC-LAYER-01": (
        "Keep EVIDENCE, INFERENCE, HYPOTHESIS and ESTIMATED_TRANSLATION separate."
    ),
}

EPISTEMIC_LAYERS = (
    "EVIDENCE",
    "INFERENCE",
    "HYPOTHESIS",
    "ESTIMATED_TRANSLATION",
)


def _registry_path() -> Path:
    packaged = PACKAGE_ROOT / "data" / "iberos_objects_registry_v2.0.csv"
    if packaged.exists():
        return packaged
    candidate = REPO_ROOT / "data" / "curated" / "iberos_objects_registry_v2.0.csv"
    if candidate.exists():
        return candidate
    raise FileNotFoundError("IberOS registry not found.")


def load_registry() -> list[dict[str, str]]:
    path = _registry_path()
    with path.open(encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def get_object(object_id: str) -> dict[str, str] | None:
    for row in load_registry():
        if row.get("OBJECT_ID") == object_id:
            return row
    return None


def family_objects(family: str) -> list[dict[str, str]]:
    family = family.upper()
    results = []
    for row in load_registry():
        families = {x.upper() for x in row.get("Familias_Tags", "").split(";") if x}
        if family in families:
            results.append(row)
    return results


def schema_path() -> Path:
    return PACKAGE_ROOT / "schema" / "iberos-result-v1.schema.json"


def validate_result(path_or_record: str | Path | dict[str, Any]):
    if isinstance(path_or_record, dict):
        record = path_or_record
    else:
        with Path(path_or_record).open(encoding="utf-8") as f:
            record = json.load(f)
    with schema_path().open(encoding="utf-8") as f:
        schema = json.load(f)
    if Draft202012Validator is None:
        return False, ["jsonschema is not installed"]
    validator = Draft202012Validator(schema)
    errors = sorted(validator.iter_errors(record), key=lambda e: list(e.path))
    return len(errors) == 0, [e.message for e in errors]


def engine_status() -> dict[str, Any]:
    """Return the frozen authority chain, metrics and active scientific guards."""
    return {
        "engine_protocol_version": ENGINE_PROTOCOL_VERSION,
        "authority": dict(AUTHORITY),
        "official_metrics": dict(OFFICIAL_METRICS),
        "active_protocols": dict(ACTIVE_PROTOCOLS),
        "epistemic_layers": list(EPISTEMIC_LAYERS),
        "note": "Validation indicators are not a percentage of the Iberian language deciphered.",
    }


def evaluate_bi_context(
    *,
    independently_quantitative: bool = False,
    verbal_complex: bool = False,
) -> dict[str, Any]:
    """Apply BI-DISAMBIG-01 without assigning a universal lexical meaning to BI."""
    if verbal_complex:
        return {
            "protocol": "BI-DISAMBIG-01",
            "decision": "NON_NUMERAL_DEFAULT",
            "numeric_value": None,
            "reason": "BI occurs in a BI+D(E/I)+V-type verbal complex.",
        }
    if independently_quantitative:
        return {
            "protocol": "BI-DISAMBIG-01",
            "decision": "NUMERAL_CONTEXT_SUPPORTED",
            "numeric_value": 2,
            "reason": "The context is independently quantitative.",
        }
    return {
        "protocol": "BI-DISAMBIG-01",
        "decision": "UNRESOLVED",
        "numeric_value": None,
        "reason": "No independent quantitative anchor is present.",
    }


def rhotic_search_key(signature: str) -> str:
    """Return a neutralized R/R1 key for retrieval only.

    This function MUST NOT be used to generate OBJECT_ID, LEAK_GROUP,
    split identity, independence claims or morphological promotions.
    """
    return re.sub(r"(?<![A-Z0-9])R1(?![A-Z0-9])", "R", signature)


def validate_rhotic_usage(*, purpose: str, neutralized: bool) -> dict[str, Any]:
    """Enforce PALEO-RHOTIC-LOCK-01 for uses of a neutralized signature."""
    restricted = {
        "GROUPING",
        "OBJECT_ID",
        "LEAK_GROUP",
        "SPLIT",
        "INDEPENDENCE",
        "MORPH_PROMOTION",
    }
    purpose_u = purpose.upper()
    if neutralized and purpose_u in restricted:
        return {
            "protocol": "PALEO-RHOTIC-LOCK-01",
            "allowed": False,
            "purpose": purpose_u,
            "reason": "R/R1 neutralization is search-only and cannot define scientific identity.",
        }
    return {
        "protocol": "PALEO-RHOTIC-LOCK-01",
        "allowed": True,
        "purpose": purpose_u,
        "reason": "Usage is compatible with the rhotic lock.",
    }


def rok_semantic_guard(literal: str | None = None) -> dict[str, Any]:
    """Keep ROK at its validated transfer-domain level unless a literal is marked open."""
    open_literals = {"give", "deliver", "receive", "assign"}
    if literal is None:
        return {
            "protocol": "ROK-DIRECTION-GUARD-01",
            "status": "VALIDATED_FUNCTIONAL_DOMAIN",
            "function": "transfer-related operation",
            "literal": None,
        }
    literal_norm = literal.strip().lower()
    if literal_norm in open_literals:
        return {
            "protocol": "ROK-DIRECTION-GUARD-01",
            "status": "PROBABLE_OPEN",
            "function": "transfer-related operation",
            "literal": literal_norm,
        }
    return {
        "protocol": "ROK-DIRECTION-GUARD-01",
        "status": "UNSUPPORTED_LITERAL",
        "function": "transfer-related operation",
        "literal": literal_norm,
    }


def validate_epistemic_layer(layer: str) -> bool:
    return layer.upper() in EPISTEMIC_LAYERS


VALIDATION_EVENT_CLASSES = (
    "STRICT_PROSPECTIVE_PASS",
    "EXTERNAL_CONVERGENCE",
    "RETROSPECTIVE_REPLICATION",
    "FAIL",
    "INDETERMINATE",
)


def classify_validation_event(
    *,
    gate_passed: bool | None,
    prospective: bool = False,
    preregistered: bool = False,
    independent: bool = False,
    contamination_free: bool = False,
    external_source: bool = False,
) -> dict[str, Any]:
    """Classify a validation event without automatically promoting scientific CORE."""
    if gate_passed is False:
        label = "FAIL"
    elif gate_passed is None:
        label = "INDETERMINATE"
    elif prospective and preregistered and independent and contamination_free:
        label = "STRICT_PROSPECTIVE_PASS"
    elif external_source:
        label = "EXTERNAL_CONVERGENCE"
    elif independent and contamination_free:
        label = "RETROSPECTIVE_REPLICATION"
    else:
        label = "INDETERMINATE"

    return {
        "classification": label,
        "automatic_core_promotion": False,
        "requires_explicit_release_decision": True,
        "authority": dict(AUTHORITY),
    }

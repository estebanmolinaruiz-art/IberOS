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

ENGINE_PROTOCOL_VERSION = "CORE-GUARDS-0.3"

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


GENERIC_DEPENDENCY_LABELS = {
    "",
    "INDEPENDENT_OR_UNRESOLVED",
    "DEPENDENT_COPY",
    "NONE",
    "N/A",
    "NA",
    "UNKNOWN",
    "UNRESOLVED",
}

SPLIT_PRECEDENCE = {
    "TRAIN": 1,
    "VAL": 2,
    "HOLD": 3,
}


def _first_nonempty(record: dict[str, Any], *keys: str) -> str | None:
    for key in keys:
        value = record.get(key)
        if value is not None and str(value).strip():
            return str(value).strip()
    return None


def independence_key(record: dict[str, Any]) -> str:
    """Return the strongest available documentary-independence key.

    Priority:
    PHYS_ID > LEAK_GROUP > specific Dependency_Group > OBJECT_ID.

    Generic status labels such as INDEPENDENT_OR_UNRESOLVED or DEPENDENT_COPY
    are not treated as shared identities.
    """
    phys_id = _first_nonempty(record, "PHYS_ID", "phys_id")
    if phys_id:
        return f"PHYS:{phys_id}"

    leak_group = _first_nonempty(record, "LEAK_GROUP", "leak_group")
    if leak_group:
        return f"LEAK:{leak_group}"

    dep_group = _first_nonempty(record, "Dependency_Group", "dependency_group")
    if dep_group and dep_group.upper() not in GENERIC_DEPENDENCY_LABELS:
        return f"DEP:{dep_group}"

    object_id = _first_nonempty(record, "OBJECT_ID", "object_id")
    if object_id:
        return f"OBJ:{object_id}"

    raise ValueError(
        "Cannot determine documentary independence: record lacks PHYS_ID, "
        "LEAK_GROUP, a specific Dependency_Group and OBJECT_ID."
    )


def collapse_independent(records: list[dict[str, Any]]) -> dict[str, list[dict[str, Any]]]:
    """Group records into documentary independence units without discarding evidence."""
    groups: dict[str, list[dict[str, Any]]] = {}
    for record in records:
        key = independence_key(record)
        groups.setdefault(key, []).append(record)
    return groups


def independence_audit(records: list[dict[str, Any]]) -> dict[str, Any]:
    """Audit how many raw records collapse to independent documentary units."""
    groups = collapse_independent(records)
    collapsed = {
        key: [
            _first_nonempty(r, "ENTRY_ID", "entry_id", "OBJECT_ID", "object_id") or "<anonymous>"
            for r in members
        ]
        for key, members in groups.items()
        if len(members) > 1
    }
    return {
        "protocol": "PHYS-LEAK-SAFE-01",
        "input_records": len(records),
        "independent_units": len(groups),
        "collapsed_record_count": len(records) - len(groups),
        "multi_record_units": collapsed,
        "automatic_independence_inference": False,
        "note": (
            "A shared PHYS_ID/LEAK_GROUP/specific dependency group prevents "
            "counting records as independent confirmations."
        ),
    }


def resolve_split(labels: list[str]) -> dict[str, Any]:
    """Resolve mixed TRAIN/VAL/HOLD labels using HOLD > VAL > TRAIN."""
    normalized = [str(x).strip().upper() for x in labels if str(x).strip()]
    unknown = sorted({x for x in normalized if x not in SPLIT_PRECEDENCE})
    known = [x for x in normalized if x in SPLIT_PRECEDENCE]
    if not known:
        return {
            "resolved_split": None,
            "conflict": bool(unknown),
            "unknown_labels": unknown,
        }
    resolved = max(known, key=lambda x: SPLIT_PRECEDENCE[x])
    return {
        "resolved_split": resolved,
        "conflict": len(set(known)) > 1 or bool(unknown),
        "unknown_labels": unknown,
    }


def split_integrity_audit(
    records: list[dict[str, Any]],
    *,
    split_field: str = "split",
) -> dict[str, Any]:
    """Detect split leakage inside one documentary-independence unit."""
    groups = collapse_independent(records)
    conflicts = []
    for key, members in groups.items():
        labels = [
            str(r.get(split_field, "")).strip().upper()
            for r in members
            if str(r.get(split_field, "")).strip()
        ]
        resolution = resolve_split(labels)
        if resolution["conflict"]:
            conflicts.append({
                "independence_key": key,
                "labels": sorted(set(labels)),
                **resolution,
            })
    return {
        "protocol": "PHYS-LEAK-SAFE-01",
        "split_field": split_field,
        "conflict_count": len(conflicts),
        "conflicts": conflicts,
        "policy": "HOLD > VAL > TRAIN",
    }


def registry_independence_audit() -> dict[str, Any]:
    """Run the independence audit on the packaged curated object registry."""
    return independence_audit(load_registry())


EVIDENCE_LEVEL_RANK = {
    "E1": 1,
    "E2": 2,
    "E3": 3,
    "E4": 4,
    "E5": 5,
}


def independent_evidence_summary(
    records: list[dict[str, Any]],
    *,
    level_field: str = "level",
    evidence_class_field: str = "evidence_class",
) -> dict[str, Any]:
    """Summarize evidence after documentary de-duplication.

    Each PHYS/LEAK unit contributes at most one independent unit. If several
    records in one unit carry different evidence levels, only the strongest
    level is used for the unit-level summary.
    """
    groups = collapse_independent(records)
    units = []
    level_counts = {level: 0 for level in EVIDENCE_LEVEL_RANK}
    evidence_classes: set[str] = set()

    for key, members in groups.items():
        valid_levels = [
            str(r.get(level_field, "")).strip().upper()
            for r in members
            if str(r.get(level_field, "")).strip().upper() in EVIDENCE_LEVEL_RANK
        ]
        strongest = (
            max(valid_levels, key=lambda x: EVIDENCE_LEVEL_RANK[x])
            if valid_levels else None
        )
        if strongest:
            level_counts[strongest] += 1

        classes = sorted({
            str(r.get(evidence_class_field, "")).strip().upper()
            for r in members
            if str(r.get(evidence_class_field, "")).strip()
        })
        evidence_classes.update(classes)
        units.append({
            "independence_key": key,
            "raw_records": len(members),
            "strongest_level": strongest,
            "evidence_classes": classes,
        })

    strongest_overall = None
    levels_present = [u["strongest_level"] for u in units if u["strongest_level"]]
    if levels_present:
        strongest_overall = max(levels_present, key=lambda x: EVIDENCE_LEVEL_RANK[x])

    return {
        "protocol": "EVIDENCE-INDEPENDENCE-01",
        "raw_records": len(records),
        "independent_units": len(groups),
        "strongest_level": strongest_overall,
        "independent_level_counts": level_counts,
        "evidence_classes": sorted(evidence_classes),
        "units": units,
    }


def evidence_promotion_review(
    records: list[dict[str, Any]],
    *,
    target_level: str,
    minimum_independent_units: int = 2,
    required_evidence_classes: list[str] | None = None,
    level_field: str = "level",
    evidence_class_field: str = "evidence_class",
) -> dict[str, Any]:
    """Check structural eligibility for human/release review, never auto-promote CORE."""
    target = target_level.strip().upper()
    if target not in EVIDENCE_LEVEL_RANK:
        raise ValueError(f"Unknown evidence level: {target_level}")

    summary = independent_evidence_summary(
        records,
        level_field=level_field,
        evidence_class_field=evidence_class_field,
    )
    target_rank = EVIDENCE_LEVEL_RANK[target]
    qualifying_units = [
        u for u in summary["units"]
        if u["strongest_level"]
        and EVIDENCE_LEVEL_RANK[u["strongest_level"]] >= target_rank
    ]

    required = {x.strip().upper() for x in (required_evidence_classes or []) if x.strip()}
    observed = set(summary["evidence_classes"])
    missing = sorted(required - observed)

    eligible = len(qualifying_units) >= minimum_independent_units and not missing
    return {
        "protocol": "EVIDENCE-INDEPENDENCE-01",
        "target_level": target,
        "qualifying_independent_units": len(qualifying_units),
        "minimum_independent_units": minimum_independent_units,
        "required_evidence_classes": sorted(required),
        "missing_evidence_classes": missing,
        "review_eligible": eligible,
        "automatic_core_promotion": False,
        "requires_explicit_release_decision": True,
        "summary": summary,
    }

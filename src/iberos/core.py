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

ENGINE_PROTOCOL_VERSION = "CORE-GUARDS-0.8"

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


FAMILY_GATE_POLICIES = {
    "SALIR": {
        "official_scope": "quantifiable economic/value domain",
        "official_state": "STRONG_FUNCTIONAL_DOMAIN",
        "functional_gate": {
            "target_level": "E4",
            "minimum_independent_units": 2,
            "required_evidence_classes": ["QUANTITATIVE", "ECONOMIC"],
        },
        "exact_gate": {
            "target_level": "E5",
            "minimum_independent_units": 2,
            "required_evidence_classes": ["QUANTITATIVE", "ECONOMIC", "ORTHOGONAL"],
        },
        "blocked_literalizations": ["money", "silver", "payment", "price"],
        "prospective_gate": "SALIR-PROSPECTIVE-01",
    },
    "ROK": {
        "official_scope": "transfer-related structural/functional domain",
        "official_state": "STRONG_STRUCTURAL_DOMAIN",
        "functional_gate": {
            "target_level": "E4",
            "minimum_independent_units": 2,
            "required_evidence_classes": ["STRUCTURAL", "TRANSFER_CONTEXT"],
        },
        "exact_gate": {
            "target_level": "E5",
            "minimum_independent_units": 2,
            "required_evidence_classes": ["STRUCTURAL", "ROLE_FIXED", "ORTHOGONAL"],
        },
        "blocked_literalizations": ["give", "deliver", "receive", "assign", "recipient", "giver"],
        "prospective_gate": "ROK-RECIPIENT-02",
    },
    "KA_KE_KU": {
        "official_scope": "relational opposition; KA enriched in quantified contexts; KU provenance/origin/affiliation contextual",
        "official_state": "STRONG_RELATIONAL_SYSTEM",
        "functional_gate": {
            "target_level": "E4",
            "minimum_independent_units": 2,
            "required_evidence_classes": ["RELATIONAL", "QUANTITATIVE"],
        },
        "exact_gate": {
            "target_level": "E5",
            "minimum_independent_units": 2,
            "required_evidence_classes": ["RELATIONAL", "FLOW_FIXED", "ORTHOGONAL"],
        },
        "blocked_literalizations": ["receiver", "provider", "input", "output", "source", "target"],
        "prospective_gate": "KA-DIRECTION-PROSPECTIVE-01",
    },
    "KUTUR": {
        "official_scope": "writing/inscription/formulary-compatible domain",
        "official_state": "STRONG_FUNCTIONAL_DOMAIN",
        "functional_gate": {
            "target_level": "E4",
            "minimum_independent_units": 2,
            "required_evidence_classes": ["FORMULARY", "STRUCTURAL"],
        },
        "exact_gate": {
            "target_level": "E5",
            "minimum_independent_units": 2,
            "required_evidence_classes": ["FORMULARY", "ORTHOGONAL"],
        },
        "blocked_literalizations": ["ritual", "money", "commodity", "gift", "unit"],
        "prospective_gate": "KUTUR-PROSPECTIVE-01",
    },
    "BAIDES_BATIR": {
        "official_scope": "human role/appellative families; BAIDES/BAITES distinct from BATIR",
        "official_state": "STRONG_ROLE_FAMILY",
        "functional_gate": {
            "target_level": "E4",
            "minimum_independent_units": 2,
            "required_evidence_classes": ["HUMAN_ROLE", "MORPHOLOGY"],
        },
        "exact_gate": {
            "target_level": "E5",
            "minimum_independent_units": 2,
            "required_evidence_classes": ["HUMAN_ROLE", "EXTERNAL_ROLE_FIXED", "ORTHOGONAL"],
        },
        "blocked_literalizations": ["witness", "beneficiary", "magistrate", "validator", "attester"],
        "prospective_gate": None,
    },
    "NUM_METRO": {
        "official_scope": "numeral/metrological compositional system",
        "official_state": "STRONG_STRUCTURAL_SYSTEM",
        "functional_gate": {
            "target_level": "E4",
            "minimum_independent_units": 2,
            "required_evidence_classes": ["COMBINATORIAL", "METROLOGY"],
        },
        "exact_gate": {
            "target_level": "E5",
            "minimum_independent_units": 2,
            "required_evidence_classes": ["QUANTITATIVE", "ORTHOGONAL"],
        },
        "blocked_literalizations": [],
        "prospective_gate": "NUM-VALUE-PER-LEXEME",
    },
}


def _normalize_family_name(family: str) -> str:
    key = family.strip().upper().replace("/", "_")
    aliases = {
        "KA_KE_KU": "KA_KE_KU",
        "KA_KE": "KA_KE_KU",
        "KA": "KA_KE_KU",
        "KE": "KA_KE_KU",
        "KU": "KA_KE_KU",
        "BAIDES": "BAIDES_BATIR",
        "BAITES": "BAIDES_BATIR",
        "BATIR": "BAIDES_BATIR",
        "NUMERAL": "NUM_METRO",
        "METROLOGY": "NUM_METRO",
        "NUM-METRO": "NUM_METRO",
        "ROK": "ROK",
        "ŔOK": "ROK",
        "SALIR": "SALIR",
        "KUTUR": "KUTUR",
        "KUTU": "KUTUR",
    }
    return aliases.get(key, key)


def family_gate_policy(family: str) -> dict[str, Any]:
    """Return the frozen gate policy for a scientific family."""
    key = _normalize_family_name(family)
    if key not in FAMILY_GATE_POLICIES:
        raise KeyError(f"No family gate policy registered for: {family}")
    return {
        "family": key,
        **json.loads(json.dumps(FAMILY_GATE_POLICIES[key])),
        "authority": dict(AUTHORITY),
    }


def evaluate_family_gate(
    family: str,
    records: list[dict[str, Any]],
    *,
    scope: str = "functional",
    strict_prospective_pass: bool = False,
) -> dict[str, Any]:
    """Evaluate a family-specific evidence gate after PHYS/LEAK de-duplication.

    scope='functional' checks the broad functional domain.
    scope='exact' checks a narrower literal/directional claim.
    No result can automatically update scientific CORE.
    """
    policy = family_gate_policy(family)
    scope_norm = scope.strip().lower()
    if scope_norm not in {"functional", "exact"}:
        raise ValueError("scope must be 'functional' or 'exact'")

    gate_cfg = policy[f"{scope_norm}_gate"]
    review = evidence_promotion_review(
        records,
        target_level=gate_cfg["target_level"],
        minimum_independent_units=gate_cfg["minimum_independent_units"],
        required_evidence_classes=gate_cfg["required_evidence_classes"],
    )

    prospective_gate = policy.get("prospective_gate")
    prospective_required = scope_norm == "exact" and prospective_gate is not None
    prospective_block = prospective_required and not strict_prospective_pass

    if prospective_block:
        state = "BLOCKED"
        reason = f"Exact claim requires prospective gate {prospective_gate}."
    elif review["review_eligible"]:
        state = "REVIEW_ELIGIBLE"
        reason = "Family-specific independent-evidence requirements are satisfied."
    else:
        state = "OPEN"
        reason = "Family-specific evidence requirements are not yet satisfied."

    return {
        "protocol": "FAMILY-GATE-01",
        "family": policy["family"],
        "scope": scope_norm.upper(),
        "official_scope": policy["official_scope"],
        "official_state": policy["official_state"],
        "state": state,
        "reason": reason,
        "prospective_gate": prospective_gate,
        "strict_prospective_pass": strict_prospective_pass,
        "blocked_literalizations": list(policy["blocked_literalizations"]),
        "review": review,
        "automatic_core_promotion": False,
        "requires_explicit_release_decision": True,
        "authority": dict(AUTHORITY),
    }


def family_gate_matrix(
    evidence_by_family: dict[str, list[dict[str, Any]]],
    *,
    scope: str = "functional",
) -> dict[str, Any]:
    """Evaluate all registered family gates supplied in an evidence mapping."""
    results = {}
    for family, records in evidence_by_family.items():
        normalized = _normalize_family_name(family)
        results[normalized] = evaluate_family_gate(
            normalized,
            records,
            scope=scope,
        )
    return {
        "protocol": "FAMILY-GATE-01",
        "scope": scope.upper(),
        "families": results,
        "automatic_core_promotion": False,
        "authority": dict(AUTHORITY),
    }


FAMILY_SCIENTIFIC_SNAPSHOT = {
    "SALIR": {
        "official_score": 75,
        "release_status": "CORE_FUNCTIONAL_DOMAIN",
        "physical_counts": {
            "objects": 21,
            "compatible": 21,
            "incompatible": 0,
        },
        "validated_statement": "quantifiable economic/value domain",
        "blocked_statement": "money/silver/payment/price as universal literal meaning",
        "next_gate": "SALIR-PROSPECTIVE-01",
        "next_gate_requirement": "post-lock independent SALIR occurrence with externally fixed economic/value context",
    },
    "ROK": {
        "official_score": 75,
        "release_status": "CORE_STRUCTURAL_DOMAIN",
        "physical_counts": {
            "provisional_ROK_objects": 15,
            "SALIR_KUTUR_union": 29,
            "SALIR_KUTUR_with_ROK": 6,
        },
        "validated_statement": "transfer-related structural/functional domain",
        "blocked_statement": "exact give/receive direction and universal recipient/giver mapping",
        "next_gate": "ROK-RECIPIENT-02",
        "next_gate_requirement": "second independent NP-E/ER + ROK construction with recipient role fixed externally",
    },
    "KA_KE_KU": {
        "official_score": 75,
        "release_status": "CORE_RELATIONAL_SYSTEM",
        "physical_counts": {
            "KA_Q": "7/154",
            "KE_Q": "0/115",
            "KU_Q": "0/72",
            "OOS_KA_Q": "5/67",
            "OOS_KE_KU_Q": "0/69",
            "fisher_global": 0.0035498356773919974,
            "fisher_OOS": 0.02683178534571723,
        },
        "validated_statement": "KA is enriched in strict quantitative contexts; KA/KE/KU are functionally selective; KU has provenance/origin/affiliation support",
        "blocked_statement": "universal source/target/provider/receiver direction",
        "next_gate": "KA-DIRECTION-PROSPECTIVE-01",
        "next_gate_requirement": "independent transaction with flow fixed externally before linguistic interpretation",
    },
    "KUTUR": {
        "official_score": 75,
        "release_status": "CORE_FUNCTIONAL_DOMAIN",
        "physical_counts": {
            "objects": 9,
            "with_ROK": 2,
        },
        "validated_statement": "writing/inscription/formulary-compatible domain",
        "blocked_statement": "ritual-only or commodity/money/gift/unit universal literalization",
        "next_gate": "KUTUR-PROSPECTIVE-01",
        "next_gate_requirement": "new independent post-lock KUTU-/KUTUR occurrence in externally writing/formulary-compatible context",
    },
    "BAIDES_BATIR": {
        "official_score": 75,
        "release_status": "CORE_ROLE_OPPOSITION",
        "physical_counts": {
            "BAITES_objects": 9,
            "BATIR_objects": 5,
        },
        "validated_statement": "distinct human/documentary role labels with contextual functional hierarchy/opposition",
        "blocked_statement": "BAIDES=universal witness or BATIR=universal magistrate/beneficiary",
        "next_gate": "BAIT-BAT-ROLE-ORTHO-01",
        "next_gate_requirement": "independent procedural/bilingual evidence fixing an institutional role without circular lexical inference",
    },
    "NUM_METRO": {
        "official_score": None,
        "release_status": "CROSS_MODULE_WORKING_SYSTEM",
        "physical_counts": {
            "BAN": "1 strong",
            "BI_BIN": "2 contextual strong",
            "LAUR": "4 contextual",
            "BORSTE": "5 contextual",
            "SEI": "6 contextual strong",
            "SISBI": "7 strong contextual / not physically closed",
            "SORSE": "8 external-system candidate / C.1.8 physical gate failed",
            "TOR": "9 best current value / not closed",
            "ABAR": "10 strong",
            "ORGEI": "20 strong",
        },
        "validated_statement": "compositional numeral/metrological system with several physically or contextually anchored values",
        "blocked_statement": "automatic promotion of every reconstructed numeral or TOR=9 as closed",
        "next_gate": "NUM-789-NEXT",
        "next_gate_requirement": "independent quantitative PHYS_ID for SISBI/SORSE/TOR or exact compositional/physical discriminator",
    },
}


def family_scientific_snapshot(family: str) -> dict[str, Any]:
    key = _normalize_family_name(family)
    if key not in FAMILY_SCIENTIFIC_SNAPSHOT:
        raise KeyError(f"No scientific snapshot registered for: {family}")
    return {
        "family": key,
        **json.loads(json.dumps(FAMILY_SCIENTIFIC_SNAPSHOT[key])),
        "authority": dict(AUTHORITY),
    }


def _dashboard_state(snapshot: dict[str, Any]) -> str:
    status = snapshot["release_status"]
    if status.startswith("CORE_"):
        return "CORE"
    if status == "CROSS_MODULE_WORKING_SYSTEM":
        return "INFER"
    return "OPEN"


def family_dashboard(families: list[str] | None = None) -> dict[str, Any]:
    """Return the release-grounded scientific dashboard for active families."""
    requested = families or list(FAMILY_SCIENTIFIC_SNAPSHOT)
    rows = []
    for family in requested:
        snap = family_scientific_snapshot(family)
        rows.append({
            "family": snap["family"],
            "state": _dashboard_state(snap),
            "official_score": snap["official_score"],
            "release_status": snap["release_status"],
            "validated_statement": snap["validated_statement"],
            "blocked_statement": snap["blocked_statement"],
            "next_gate": snap["next_gate"],
            "next_gate_requirement": snap["next_gate_requirement"],
            "physical_counts": snap["physical_counts"],
        })
    return {
        "protocol": "FAMILY-DASHBOARD-01",
        "authority": dict(AUTHORITY),
        "official_metrics": dict(OFFICIAL_METRICS),
        "rows": rows,
        "automatic_core_promotion": False,
        "note": "Dashboard state reflects the frozen release plus explicitly marked working modules; it does not create new promotions.",
    }


def family_bottlenecks() -> list[dict[str, Any]]:
    """Rank current next gates by the frozen scientific priority."""
    priority = [
        "ROK",
        "KA_KE_KU",
        "SALIR",
        "KUTUR",
        "BAIDES_BATIR",
        "NUM_METRO",
    ]
    return [
        {
            "rank": i + 1,
            "family": family,
            "next_gate": FAMILY_SCIENTIFIC_SNAPSHOT[family]["next_gate"],
            "requirement": FAMILY_SCIENTIFIC_SNAPSHOT[family]["next_gate_requirement"],
            "current_state": _dashboard_state(FAMILY_SCIENTIFIC_SNAPSHOT[family]),
        }
        for i, family in enumerate(priority)
    ]


ROK_RECIPIENT_CANDIDATES = {
    "D.0.1": {
        "independent_from_primary": False,
        "np_e_er_secure": True,
        "recipient_role_fixed_externally": True,
        "same_rok_lexeme": True,
        "note": "Primary anchor: BASTUBAR-ER + TEŔOKAN + UTUR.",
    },
    "F.9.5": {
        "independent_from_primary": True,
        "np_e_er_secure": False,
        "recipient_role_fixed_externally": False,
        "same_rok_lexeme": True,
        "note": "Orleyl intra-object E/KUTUR/ROK network; E segmentation/role not externally fixed.",
    },
    "F.9.7": {
        "independent_from_primary": True,
        "np_e_er_secure": False,
        "recipient_role_fixed_externally": False,
        "same_rok_lexeme": True,
        "note": "Published aŕeŕ-e ... KUTU ... BAS-BITEŔOK; not adequate for automatic recipient count.",
    },
    "H.0.1": {
        "independent_from_primary": True,
        "np_e_er_secure": True,
        "recipient_role_fixed_externally": False,
        "same_rok_lexeme": True,
        "note": "HOLD physical replication of formal E/ER+ROK frame; recipient identity not externally fixed.",
    },
    "B.7.38": {
        "independent_from_primary": True,
        "np_e_er_secure": False,
        "recipient_role_fixed_externally": False,
        "same_rok_lexeme": True,
        "note": "VAL formal compatibility; nearby -e role is not independently fixed.",
    },
    "C.17.1": {
        "independent_from_primary": True,
        "np_e_er_secure": False,
        "recipient_role_fixed_externally": False,
        "same_rok_lexeme": True,
        "note": "Published eŕok-paradigm occurrence; no independently fixed recipient participant.",
    },
    "C.21.10": {
        "independent_from_primary": True,
        "np_e_er_secure": False,
        "recipient_role_fixed_externally": False,
        "same_rok_lexeme": True,
        "note": "ŚALAIÁRKIS is a secure personal name in śalaiárkisteŕokan, but -te segmentation and recipient role remain open.",
    },
}


def evaluate_rok_recipient_candidate(reference: str) -> dict[str, Any]:
    """Evaluate one object against the frozen ROK-RECIPIENT-02 discriminator."""
    if reference not in ROK_RECIPIENT_CANDIDATES:
        raise KeyError(f"Unknown ROK recipient candidate: {reference}")
    c = ROK_RECIPIENT_CANDIDATES[reference]
    criteria = {
        "independent_from_primary": bool(c["independent_from_primary"]),
        "np_e_er_secure": bool(c["np_e_er_secure"]),
        "recipient_role_fixed_externally": bool(c["recipient_role_fixed_externally"]),
        "same_rok_lexeme": bool(c["same_rok_lexeme"]),
    }
    missing = [k for k, v in criteria.items() if not v]
    passed = all(criteria.values())
    return {
        "protocol": "ROK-RECIPIENT-02",
        "reference": reference,
        "criteria": criteria,
        "missing_requirements": missing,
        "state": "STRICT_PROSPECTIVE_PASS" if passed else "OPEN",
        "note": c["note"],
        "automatic_core_promotion": False,
        "authority": dict(AUTHORITY),
    }


def rok_recipient_candidate_matrix() -> dict[str, Any]:
    rows = [evaluate_rok_recipient_candidate(ref) for ref in ROK_RECIPIENT_CANDIDATES]
    passing = [r["reference"] for r in rows if r["state"] == "STRICT_PROSPECTIVE_PASS"]
    return {
        "protocol": "ROK-RECIPIENT-02",
        "rows": rows,
        "passing_candidates": passing,
        "gate_state": "PASS" if passing else "OPEN",
        "next_required_evidence": (
            "A second independent physical object with secure NP-E/ER, "
            "same ROK lexeme, and recipient/beneficiary role fixed by "
            "bilingual, archaeological or procedural evidence."
        ),
        "automatic_core_promotion": False,
        "authority": dict(AUTHORITY),
    }


KA_DIRECTION_CANDIDATES = {
    "BASTIDA-I": {
        "new_independent_transaction": False,
        "flow_fixed_before_linguistic_analysis": False,
        "ka_ku_opportunity": True,
        "prediction_preregistered": False,
        "source_independent_of_hypothesis": False,
        "classification": "STRONG_RETROSPECTIVE_CONVERGENCE",
        "note": "Source-generating case for the outflow/inflow interpretation; cannot validate itself prospectively.",
    },
    "ORLEYL-CS.21.08": {
        "new_independent_transaction": True,
        "flow_fixed_before_linguistic_analysis": False,
        "ka_ku_opportunity": True,
        "prediction_preregistered": False,
        "source_independent_of_hypothesis": False,
        "classification": "STRONG_RETROSPECTIVE_CROSS_OBJECT_CONVERGENCE",
        "note": "Independent physical object replicating KA vs (I)KU structure, but direction is interpreted within the same research framework.",
    },
    "PECH-MAHO-2025": {
        "new_independent_transaction": True,
        "flow_fixed_before_linguistic_analysis": False,
        "ka_ku_opportunity": False,
        "prediction_preregistered": False,
        "source_independent_of_hypothesis": True,
        "classification": "EXTERNAL_CONVERGENCE",
        "note": "Commercial/accounting context compatible, but no independently fixed directional KA/KU contrast.",
    },
    "EL-VILAR-2024": {
        "new_independent_transaction": True,
        "flow_fixed_before_linguistic_analysis": False,
        "ka_ku_opportunity": False,
        "prediction_preregistered": False,
        "source_independent_of_hypothesis": True,
        "classification": "RETROSPECTIVE_REPLICATION",
        "note": "Commercial lead with relevant vocabulary; transaction direction is not externally fixed.",
    },
    "MURCIA-2026-FRAGMENT": {
        "new_independent_transaction": True,
        "flow_fixed_before_linguistic_analysis": True,
        "ka_ku_opportunity": False,
        "prediction_preregistered": True,
        "source_independent_of_hypothesis": True,
        "classification": "INDETERMINATE",
        "note": "Independent economic/administrative context, but only 11 signs and no secure KA/KU morphology.",
    },
}


def evaluate_ka_direction_candidate(reference: str) -> dict[str, Any]:
    if reference not in KA_DIRECTION_CANDIDATES:
        raise KeyError(f"Unknown KA/KU direction candidate: {reference}")
    c = KA_DIRECTION_CANDIDATES[reference]
    criteria = {
        "new_independent_transaction": bool(c["new_independent_transaction"]),
        "flow_fixed_before_linguistic_analysis": bool(c["flow_fixed_before_linguistic_analysis"]),
        "ka_ku_opportunity": bool(c["ka_ku_opportunity"]),
        "prediction_preregistered": bool(c["prediction_preregistered"]),
        "source_independent_of_hypothesis": bool(c["source_independent_of_hypothesis"]),
    }
    missing = [k for k, v in criteria.items() if not v]
    passed = all(criteria.values())
    return {
        "protocol": "KA-DIRECTION-PROSPECTIVE-01",
        "reference": reference,
        "criteria": criteria,
        "missing_requirements": missing,
        "state": "STRICT_PROSPECTIVE_PASS" if passed else "OPEN",
        "classification": c["classification"],
        "note": c["note"],
        "automatic_core_promotion": False,
        "authority": dict(AUTHORITY),
    }


def ka_direction_candidate_matrix() -> dict[str, Any]:
    rows = [evaluate_ka_direction_candidate(ref) for ref in KA_DIRECTION_CANDIDATES]
    passing = [r["reference"] for r in rows if r["state"] == "STRICT_PROSPECTIVE_PASS"]
    return {
        "protocol": "KA-DIRECTION-PROSPECTIVE-01",
        "rows": rows,
        "passing_candidates": passing,
        "gate_state": "PASS" if passing else "OPEN",
        "frozen_prediction": {
            "KA": "target/destination/allocation-like; compatible with document-perspective outflow",
            "KU": "source/origin/provenance-like; compatible with document-perspective inflow",
        },
        "next_required_evidence": (
            "A genuinely independent transaction/offering/ledger where direction is fixed "
            "before linguistic analysis and KA/KE versus KU can be tested against a "
            "preregistered target/source prediction."
        ),
        "automatic_core_promotion": False,
        "authority": dict(AUTHORITY),
    }


SALIR_PROSPECTIVE_CANDIDATES = {
    "PECH-MAHO-2025": {
        "post_lock_or_genuinely_unused": False,
        "salir_secure": True,
        "economic_context_fixed_independently": False,
        "source_independent_of_hypothesis": True,
        "classification": "STRONG_EXTERNAL_CONVERGENCE",
        "note": "Commercial/accounting interpretation is plausible, but publication predates C474 and depends partly on recognizing śalir.",
    },
    "EL-VILAR-2024": {
        "post_lock_or_genuinely_unused": False,
        "salir_secure": True,
        "economic_context_fixed_independently": False,
        "source_independent_of_hypothesis": True,
        "classification": "STRONG_RETROSPECTIVE_DOMAIN_REPLICATION",
        "note": "Long commercial lead with śalir; publication predates C474 and operation type is not independently fixed enough.",
    },
    "MURCIA-2026-FRAGMENT": {
        "post_lock_or_genuinely_unused": True,
        "salir_secure": False,
        "economic_context_fixed_independently": True,
        "source_independent_of_hypothesis": True,
        "classification": "INDEPENDENT_ECONOMIC_CONTEXT_LINGUISTICALLY_INDETERMINATE",
        "note": "Administrative/economic context from cancellation treatment, but only 11 signs and no secure SALIR.",
    },
}


def evaluate_salir_prospective_candidate(reference: str) -> dict[str, Any]:
    if reference not in SALIR_PROSPECTIVE_CANDIDATES:
        raise KeyError(f"Unknown SALIR prospective candidate: {reference}")
    c = SALIR_PROSPECTIVE_CANDIDATES[reference]
    criteria = {
        "post_lock_or_genuinely_unused": bool(c["post_lock_or_genuinely_unused"]),
        "salir_secure": bool(c["salir_secure"]),
        "economic_context_fixed_independently": bool(c["economic_context_fixed_independently"]),
        "source_independent_of_hypothesis": bool(c["source_independent_of_hypothesis"]),
    }
    missing = [k for k, v in criteria.items() if not v]
    passed = all(criteria.values())
    return {
        "protocol": "SALIR-PROSPECTIVE-01",
        "reference": reference,
        "criteria": criteria,
        "missing_requirements": missing,
        "state": "STRICT_PROSPECTIVE_PASS" if passed else "OPEN",
        "classification": c["classification"],
        "note": c["note"],
        "automatic_core_promotion": False,
        "authority": dict(AUTHORITY),
    }


def salir_prospective_candidate_matrix() -> dict[str, Any]:
    rows = [evaluate_salir_prospective_candidate(ref) for ref in SALIR_PROSPECTIVE_CANDIDATES]
    passing = [r["reference"] for r in rows if r["state"] == "STRICT_PROSPECTIVE_PASS"]
    return {
        "protocol": "SALIR-PROSPECTIVE-01",
        "rows": rows,
        "passing_candidates": passing,
        "gate_state": "PASS" if passing else "OPEN",
        "next_required_evidence": (
            "A post-C474 or genuinely unused object with secure SALIR and an "
            "economic/value context fixed independently of SALIR recognition."
        ),
        "fail_or_degrade_trigger": (
            "A secure replicated SALIR occurrence in a clearly non-economic/non-value referent."
        ),
        "automatic_core_promotion": False,
        "authority": dict(AUTHORITY),
    }

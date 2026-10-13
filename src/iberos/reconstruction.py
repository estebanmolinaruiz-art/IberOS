"""Conservative, auditable reconstruction records for IberOS CORE.

This module formats documented proposals; it does not infer meanings or
promote hypotheses to scientific facts.
"""
from __future__ import annotations

from typing import Any
import re

LAYERS = frozenset({"EVIDENCE", "INFERENCE", "HYPOTHESIS", "AMBIGUOUS", "UNRESOLVED"})
SEMANTIC_LAYERS = frozenset({"INFERENCE", "HYPOTHESIS", "AMBIGUOUS"})
MAX_SEGMENTS = 500


def validate_reconstruction(segments: Any) -> tuple[bool, list[str]]:
    """Reject untraceable and semantically overclaimed colored segments."""
    errors: list[str] = []
    if not isinstance(segments, list) or not segments or len(segments) > MAX_SEGMENTS:
        return False, ["segments must be a nonempty list of at most 500 items"]
    for i, segment in enumerate(segments):
        prefix = f"segments[{i}]"
        if not isinstance(segment, dict):
            errors.append(f"{prefix}: expected an object")
            continue
        layer = segment.get("layer")
        label = segment.get("text")
        if not isinstance(layer, str) or layer not in LAYERS:
            errors.append(f"{prefix}: invalid epistemic layer")
        if not isinstance(label, str) or not label.strip() or len(label) > 2000:
            errors.append(f"{prefix}: text must contain 1-2000 meaningful characters")
        if "meaning_claim" in segment and not isinstance(segment["meaning_claim"], bool):
            errors.append(f"{prefix}: meaning_claim must be boolean")
        if layer == "EVIDENCE" and segment.get("meaning_claim"):
            errors.append(f"{prefix}: EVIDENCE cannot certify a semantic translation")
        if isinstance(layer, str) and layer in (LAYERS - {"UNRESOLVED"}):
            source = segment.get("source")
            if not isinstance(source, str) or not source.strip():
                errors.append(f"{prefix}: documented source required")
        if isinstance(layer, str) and layer in SEMANTIC_LAYERS:
            rationale = segment.get("rationale")
            if not isinstance(rationale, str) or not rationale.strip():
                errors.append(f"{prefix}: rationale required for interpretation")
        if layer == "UNRESOLVED" and segment.get("meaning_claim"):
            errors.append(f"{prefix}: unresolved text cannot claim a meaning")
    return not errors, errors


def build_reconstruction(object_id: str, segments: list[dict[str, Any]]) -> dict[str, Any]:
    """Return a display-ready proposal only after validating its provenance."""
    if not isinstance(object_id, str) or not re.fullmatch(r"IBR-[A-Z]{3}-[0-9]{4}", object_id):
        raise ValueError("A valid IberOS object identifier is required")
    valid, errors = validate_reconstruction(segments)
    if not valid:
        raise ValueError("; ".join(errors))
    return {
        "schema": "IberOS-Reconstruction/1.0",
        "object_id": object_id,
        "reconstruction_segments": [
            {key: segment[key] for key in ("text", "layer", "source", "rationale", "meaning_claim")
             if key in segment}
            for segment in segments
        ],
        "scientific_state": "UNVERIFIED",
        "automatic_core_promotion": False,
        "notice": "Evidence of a reading is not evidence of a translation.",
    }


def audit_reconstruction_sources(
    segments: Any, source_catalog: Any
) -> dict[str, Any]:
    """Cross-check declared segment sources against a curated source inventory.

    Source presence verifies an identifier's registration, NOT its philological
    correctness, independence or semantic meaning.
    """
    valid, errors = validate_reconstruction(segments)
    if not isinstance(source_catalog, dict):
        errors.append("source_catalog must map source IDs to documented records")
        source_catalog = {}
    for i, segment in enumerate(segments if isinstance(segments, list) else []):
        if not isinstance(segment, dict) or segment.get("layer") == "UNRESOLVED":
            continue
        source_id = segment.get("source")
        if not isinstance(source_id, str) or not source_id.strip():
            continue
        record = source_catalog.get(source_id)
        if not isinstance(record, dict):
            errors.append(f"segments[{i}]: source not found in catalog")
            continue
        if not isinstance(record.get("reference"), str) or not record["reference"].strip():
            errors.append(f"segments[{i}]: source has no bibliographic reference")
        if not isinstance(record.get("locator"), str) or not record["locator"].strip():
            errors.append(f"segments[{i}]: source lacks exact passage/page locator")
        if record.get("excluded_control") is True:
            errors.append(f"segments[{i}]: excluded control cannot anchor reconstruction")
    return {
        "status": "BLOCKED" if errors else "REGISTERED_SOURCES_ONLY",
        "errors": errors,
        "scientific_state": "UNVERIFIED",
        "independence_audited": False,
        "semantic_validation": False,
        "automatic_core_promotion": False,
    }


def audit_reconstruction_independence(
    segments: Any, source_catalog: Any
) -> dict[str, Any]:
    """Conservatively join editions by *any* shared specific identity.

    This graph audit is not a claim of physical or linguistic independence.
    Transitive PHYS_ID, LEAK_GROUP and specific Dependency_Group bridges are
    collapsed rather than mistakenly counted as independent confirmations.
    """
    from .core import GENERIC_DEPENDENCY_LABELS

    source_audit = audit_reconstruction_sources(segments, source_catalog)
    errors = list(source_audit["errors"])
    if not isinstance(source_catalog, dict):
        source_catalog = {}
    source_ids = sorted({
        segment["source"] for segment in (segments if isinstance(segments, list) else [])
        if isinstance(segment, dict) and segment.get("layer") != "UNRESOLVED"
        and isinstance(segment.get("source"), str) and segment["source"].strip()
    })
    parent = {source_id: source_id for source_id in source_ids}

    def find(source_id: str) -> str:
        while parent[source_id] != source_id:
            parent[source_id] = parent[parent[source_id]]
            source_id = parent[source_id]
        return source_id

    def union(a: str, b: str) -> None:
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[max(ra, rb)] = min(ra, rb)

    seen: dict[str, str] = {}
    unresolved: list[str] = []
    for source_id in source_ids:
        record = source_catalog.get(source_id)
        if not isinstance(record, dict):
            unresolved.append(source_id)
            continue
        keys = []
        for label, names in (
            ("PHYS", ("PHYS_ID", "phys_id")),
            ("LEAK", ("LEAK_GROUP", "leak_group")),
            ("DEP", ("Dependency_Group", "dependency_group")),
        ):
            value = next((record[n].strip() for n in names
                          if isinstance(record.get(n), str) and record[n].strip()), "")
            if label == "DEP" and value.upper() in GENERIC_DEPENDENCY_LABELS:
                continue
            if value:
                keys.append(label + ":" + value)
        if not keys:
            unresolved.append(source_id)
        for key in keys:
            if key in seen:
                union(source_id, seen[key])
            else:
                seen[key] = source_id
    units: dict[str, list[str]] = {}
    for source_id in source_ids:
        if source_id not in unresolved:
            units.setdefault(find(source_id), []).append(source_id)
    if unresolved:
        errors.append("Unresolved physical/leak/dependency identity: " + ", ".join(unresolved))
    return {
        "protocol": "RECONSTRUCTION-PHYS-LEAK-02",
        "status": "BLOCKED" if errors else "IDENTITY_GROUPED_REVIEW_REQUIRED",
        "errors": errors,
        "source_count": len(source_ids),
        "identity_unit_count": len(units),
        "identity_units": {key: sorted(members) for key, members in sorted(units.items())},
        "unresolved_sources": sorted(unresolved),
        "independence_audited": False,
        "independence_confirmed": False,
        "scientific_state": "UNVERIFIED",
        "semantic_validation": False,
        "automatic_core_promotion": False,
    }

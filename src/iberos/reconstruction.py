"""Conservative, auditable reconstruction records for IberOS CORE.

This module formats documented proposals; it does not infer meanings or
promote hypotheses to scientific facts.
"""
from __future__ import annotations

from typing import Any

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
        if layer not in LAYERS:
            errors.append(f"{prefix}: invalid epistemic layer")
        if not isinstance(label, str) or not label.strip() or len(label) > 2000:
            errors.append(f"{prefix}: text must contain 1-2000 meaningful characters")
        if layer == "EVIDENCE" and segment.get("meaning_claim"):
            errors.append(f"{prefix}: EVIDENCE cannot certify a semantic translation")
        if layer in (LAYERS - {"UNRESOLVED"}):
            source = segment.get("source")
            if not isinstance(source, str) or not source.strip():
                errors.append(f"{prefix}: documented source required")
        if layer in SEMANTIC_LAYERS:
            rationale = segment.get("rationale")
            if not isinstance(rationale, str) or not rationale.strip():
                errors.append(f"{prefix}: rationale required for interpretation")
        if layer == "UNRESOLVED" and segment.get("meaning_claim"):
            errors.append(f"{prefix}: unresolved text cannot claim a meaning")
    return not errors, errors


def build_reconstruction(object_id: str, segments: list[dict[str, Any]]) -> dict[str, Any]:
    """Return a display-ready proposal only after validating its provenance."""
    if not isinstance(object_id, str) or not object_id.startswith("IBR-"):
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

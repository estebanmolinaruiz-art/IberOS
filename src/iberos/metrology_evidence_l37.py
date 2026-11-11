"""L37: editorial graphic candidates are not confirmed metrological families.

Independent documentation requires external audit. No caller-provided evidence
can automatically produce FAMILY_CONFIRMED. L36 inputs are development data.
"""
from __future__ import annotations

from typing import Mapping
from .metrology_family_router_l35 import route

GRAPHIC_CANDIDATE = "GRAPHIC_CANDIDATE"
INDETERMINATE = "INDETERMINATE"
FAMILY_CONFIRMED = "FAMILY_CONFIRMED"  # reserved for an independently audited future registry

ACCEPTED_EVIDENCE_TYPES = frozenset({
    "independent_original_sign_reading",
    "independent_archaeological_context",
    "independently_dated_metrological_control",
})


def _audit_candidate(record: Mapping | None, family: str) -> bool:
    """Test record completeness only; never attest the evidence is true."""
    return bool(
        isinstance(record, Mapping)
        and record.get("family") == family
        and record.get("evidence_type") in ACCEPTED_EVIDENCE_TYPES
        and isinstance(record.get("source_id"), str)
        and record["source_id"].strip()
        and record.get("verified_independently") is True
        and record.get("review_status") == "approved"
        and record.get("supports_family_attribution") is True
    )


def evaluate(text: str, *, independent_evidence: Mapping | None = None) -> dict:
    """Conservative overlay; no edits to L35, L32, numeric values or translations."""
    original = route(text)
    candidates = []
    for hit in original["legacy_l32_hits"]:
        category = hit["classification"]
        ambiguous = category in {
            "e_complex_unresolved", "embedded_unit_strokes_unresolved",
            "unit_mixed_strokes_unresolved",
        }
        candidates.append({
            "raw": hit["raw"], "start": hit["start"], "end": hit["end"],
            "proposed_family": None if ambiguous else "a_o_ki_editorial",
            "state": INDETERMINATE if ambiguous else GRAPHIC_CANDIDATE,
            "reason": category, "source_layer": "EDITORIAL_TRANSCRIPTION",
        })
    for hit in original["ko_ti_hits"]:
        candidates.append({
            "raw": hit["raw"], "start": hit["start"], "end": hit["end"],
            "proposed_family": "ko_ti_editorial",
            "state": GRAPHIC_CANDIDATE, "reason": "ko_ti_pattern",
            "source_layer": "EDITORIAL_TRANSCRIPTION",
        })
    for candidate in candidates:
        family = candidate["proposed_family"]
        candidate["promotion_record_eligible_for_audit"] = bool(
            candidate["state"] == GRAPHIC_CANDIDATE and family is not None
            and _audit_candidate(independent_evidence, family)
        )
    candidates.sort(key=lambda x: (x["start"], x["end"]))
    return {
        "module": "L37_PROVENANCE_STATES",
        "legacy_router_decision": original["decision"],
        "candidates": candidates,
        "states": sorted({c["state"] for c in candidates}),
        "family_confirmed_count": 0,
        "numeric_values_decoded": 0,
        "new_semantic_translations_validated": 0,
        "note": "Record-format gating is not independent factual verification.",
    }

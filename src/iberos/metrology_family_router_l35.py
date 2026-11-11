"""IberOS L35: experimental editorial metrology-family router.

Evidence patterns only. No value decoding, semantic hypotheses or validated
physical sign readings. Vieille-Toulouse HGA records are development data.
"""
from __future__ import annotations

import re
from .editorial_quantity_normalizer import extract as l32_extract

_KO_TI_GROUP = re.compile(
    r"(?<![\w])(?P<unit>ko|ti)(?P<sep>\s+)"
    r"(?P<marks>[sSLΠIΙ]+(?:\s+[sSLΠIΙ]+)*)(?!\w)", re.UNICODE
)

def parse_ko_ti(text: str) -> list[dict]:
    """Conservative candidates with exact positions and undecoded marks."""
    matches = []
    for match in _KO_TI_GROUP.finditer(text):
        marks = match.group("marks")
        if not any(char in "IΙΠL" for char in marks):
            continue
        matches.append({
            "start": match.start(), "end": match.end(), "raw": match.group(),
            "family": "ko_ti_editorial_candidate", "unit": match.group("unit"),
            "marks": marks, "numeric_value": None, "semantic_function": None,
            "independently_verified": False,
            "epistemic_status": "EDITORIAL_CANDIDATE_ONLY",
        })
    return matches

def route(text: str) -> dict:
    """Route editorial pattern candidates for review; never infer meaning."""
    legacy = l32_extract(text)
    ko_ti = parse_ko_ti(text)
    families = (["a_o_ki_editorial"] if legacy else []) + (
        ["ko_ti_editorial"] if ko_ti else []
    )
    decision = {
        0: "abstain", 1: (
            "ko_ti_review" if ko_ti else "a_o_ki_review"
        ), 2: "mixed_families_review",
    }[len(families)]
    return {
        "decision": decision, "candidate_families": families,
        "ko_ti_hits": ko_ti, "legacy_l32_hits": legacy,
        "numeric_values_decoded": 0, "semantic_labels_validated": 0,
    }

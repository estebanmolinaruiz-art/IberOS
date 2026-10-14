"""Auditable inventory of implemented IberOS guards and research gates.

Counts are catalog entries, not verified decipherment rules.
"""
from __future__ import annotations

from .core import ACTIVE_PROTOCOLS, FAMILY_GATE_POLICIES, AUTHORITY

SCIENTIFIC_GATES = {
    "SALIR": "SALIR-PROSPECTIVE-01",
    "ROK": "ROK-RECIPIENT-02",
    "KA_KE_KU": "KA-DIRECTION-PROSPECTIVE-01",
    "KUTUR": "KUTUR-PROSPECTIVE",
    "BAIDES_BATIR": "BAIDES-BATIR-ROLE",
    "NUM_METRO": "NUM-7-8-9-EXACT",
    "D_E_I": "DEDI-COMBINED-GATE-01",
}

def rule_catalog() -> dict:
    """Return code-linked rules without elevating open linguistic hypotheses."""
    entries = []
    for rule_id, description in ACTIVE_PROTOCOLS.items():
        entries.append({
            "id": rule_id, "kind": "ACTIVE_GUARD",
            "source": "src/iberos/core.py:ACTIVE_PROTOCOLS",
            "description": description, "validation": "IMPLEMENTED_GUARD",
            "semantic_translation_verified": False,
        })
    for family, policy in FAMILY_GATE_POLICIES.items():
        entries.append({
            "id": SCIENTIFIC_GATES[family], "kind": "FAMILY_GATE",
            "family": family, "source": "src/iberos/core.py:FAMILY_GATE_POLICIES",
            "description": policy["official_scope"],
            "validation": "OPEN_PROSPECTIVE_GATE",
            "semantic_translation_verified": False,
        })
    entries.append({
        "id": SCIENTIFIC_GATES["D_E_I"], "kind": "FAMILY_GATE",
        "family": "D_E_I", "source": "src/iberos/core.py:dedi_combined_gate",
        "description": "Formal D(E/I) contrast; exact grammatical variable unresolved",
        "validation": "OPEN_PROSPECTIVE_GATE",
        "semantic_translation_verified": False,
    })
    entries.append({
        "id": "ROK-SEGMENTATION-PROSPECTIVE-01", "kind": "RESEARCH_PROTOCOL",
        "family": "ROK", "source": "src/iberos/rok_prospective.py",
        "description": "Preregister H1/H2/H3 alternatives with documentary-independence checks",
        "validation": "AWAITING_INDEPENDENT_EVIDENCE",
        "semantic_translation_verified": False,
    })
    if len(entries) != len({entry["id"] for entry in entries}):
        raise ValueError("Duplicate rule id")
    return {
        "catalog_version": "IBEROS-RULE-CATALOG-1",
        "authority": dict(AUTHORITY),
        "counts": {
            "active_guards": len(ACTIVE_PROTOCOLS),
            "family_gates": len(SCIENTIFIC_GATES),
            "research_protocols": 1,
            "documented_entries": len(entries),
            "verified_translation_rules": 0,
        },
        "entries": entries,
        "note": ("Catalog coverage counts code-linked entries only; it is not an "
                 "exhaustive count of every if-statement or scientific inference. "
                 "Zero verified translation rules in this catalog does not imply "
                 "zero existing external linguistic knowledge."),
        "automatic_core_promotion": False,
    }

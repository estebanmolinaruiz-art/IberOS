"""Regression guard for the human-provenance warning in HOLD screening.

The message is part of the scientific safety contract: a passing known-ID
screen must never imply an object has independently verified provenance.
"""
import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("hold_guard_contract", ROOT / "scripts" / "validation01_hold_leakage_guard.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_unknown_object_retains_explicit_human_provenance_warning():
    result = module.evaluate(
        [{"split": "HOLD", "object_id": "UNSEEN-2026-01", "physical_group": "UNSEEN-2026-01"}],
        [],
        [],
    )
    assert result["gate"] == "PASS_KNOWN_OBJECT_SCREEN"
    assert "human provenance" in result["note"].lower()
    assert result["gate"] != "VALIDATED"

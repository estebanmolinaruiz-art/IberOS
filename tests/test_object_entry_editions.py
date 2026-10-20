from pathlib import Path
from scripts.audit_object_entry_editions import inspect

def test_object_entry_edition_consistency():
    report=inspect(Path(__file__).resolve().parents[1])
    assert report["object_count"]==38
    assert report["needs_subentry_split"]==6
    assert report["automatic_scientific_promotion"] is False
    assert report["verified_physical_entry_edition"]==0
    assert len(report["assessments"])==report["object_count"]
    assert all("EDITION_TO_ENTRY_NOT_INDEPENDENTLY_COLLATED" in row["open_checks"] for row in report["assessments"])

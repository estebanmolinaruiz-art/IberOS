from pathlib import Path
import importlib.util

SCRIPT=Path(__file__).resolve().parents[1] / 'scripts' / 'audit_object_entry_editions.py'
spec=importlib.util.spec_from_file_location('object_entry_editions', SCRIPT)
module=importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
inspect=module.inspect

def test_object_entry_edition_consistency():
    report=inspect(Path(__file__).resolve().parents[1])
    assert report["object_count"]==38
    assert report["needs_subentry_split"]==6
    assert report["automatic_scientific_promotion"] is False
    assert report["verified_physical_entry_edition"]==0
    assert len(report["assessments"])==report["object_count"]
    assert all("EDITION_TO_ENTRY_NOT_INDEPENDENTLY_COLLATED" in row["open_checks"] for row in report["assessments"])

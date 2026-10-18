"""Reproducible non-promoting review check suite."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
from audit_graphic_review_processes import audit

def test_ten_graphic_review_controls_pass():
    result=audit()
    assert result["total"]==10
    assert result["passed"]==10
    assert result["checked_records"]==9
    assert result["checked_objects"]==3
    assert result["scientific_translations_validated"]==0

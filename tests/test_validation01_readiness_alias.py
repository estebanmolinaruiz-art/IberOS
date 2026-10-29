"""Readiness must not double-count textual variants of one archaeological object."""
import importlib.util
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
s=importlib.util.spec_from_file_location("readiness_alias",ROOT/"scripts/validation01_readiness.py")
m=importlib.util.module_from_spec(s)
s.loader.exec_module(m)

def test_renamed_same_hold_group_counts_once():
    data=[
        {"split":"HOLD","physical_group":"ORLEYL VII"},
        {"split":"HOLD","physical_group":"F.9.7"},
        {"split":"HOLD","physical_group":"Orléyl-VII"},
    ]
    out=m.evaluate([],data,{})
    assert out["unique_hold_groups"]==1
    assert "UNDER_20_INDEPENDENT_HOLD_PHYSICAL_GROUPS" in out["blockers"]
    assert out["result"]=="NOT_EVALUATED"

def test_distinct_objects_are_not_merged():
    out=m.evaluate([],[{"split":"HOLD","physical_group":"Orleyl V"},{"split":"HOLD","physical_group":"Orleyl VII"}],{})
    assert out["unique_hold_groups"]==2

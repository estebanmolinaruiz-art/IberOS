import importlib.util
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
s=importlib.util.spec_from_file_location("holdguard",ROOT/"scripts/validation01_hold_leakage_guard.py")
m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
def test_reject_orleyl_aliases():
 r=m.evaluate([{"split":"HOLD","object_id":"F.9.7","physical_group":"ORLEYL-VII"}],[],[])
 assert r["gate"]=="BLOCKED"
def test_reject_screened_id():
 r=m.evaluate([{"split":"HOLD","object_id":"IBR-CER-0001","physical_group":"NewName"}],[{"object_id":"IBR-CER-0001"}],[])
 assert r["gate"]=="BLOCKED"
def test_unknown_is_not_certified_novel():
 r=m.evaluate([{"split":"HOLD","object_id":"NEW-1","physical_group":"NEW-1"}],[],[])
 assert r["gate"]=="PASS_KNOWN_OBJECT_SCREEN"
 assert "human provenance" in r["note"]

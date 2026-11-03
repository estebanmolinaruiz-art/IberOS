from pathlib import Path
import pytest
from iberos_ext.runner import Evidence, evaluate, save_report
from iberos_ext.functions import leave_one_group_out, terminal_counts, image_pair_manifest

def test_fail_closed():
    e=Evidence("CASE-NET-PROSPECTIVE-01","","","","","","","","",False,False,"STRICT_PROSPECTIVE_PASS","","")
    assert evaluate(e)["classification"]=="INDETERMINATE"

def test_fail_cannot_be_rewritten():
    e=Evidence("SALIR-PROSPECTIVE-01","src","2026-11-03","v1","p","g","literal","sha",True,True,"FAIL","checked","digest")
    r=evaluate(e)
    assert r["proposed"]=="FAIL" and r["classification"]=="INDETERMINATE"

def test_group_leak():
    assert leave_one_group_out([{"leak_group":"a","sequence":"X"},{"leak_group":"b","sequence":"X"}])["a"]["overlap_with_other_groups"]==1

def test_terminals_deduplicate():
    assert terminal_counts([{"leak_group":"a","signs":["K","A"]},{"leak_group":"a","signs":["K","A"]}])=={"A":1}

def test_image_requires_provenance():
    with pytest.raises(ValueError): image_pair_manifest([{"phys_id":"a"}])

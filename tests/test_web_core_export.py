from scripts.export_web_core import build

def test_web_core_export_has_every_curated_object():
    report=build()
    assert report["schema"]=="IberOS-Web-Core-Audit/1.0"
    assert report["object_count"]==38
    assert len(report["objects"])==38
    assert "IBR-PLM-0002" in report["objects"]

def test_web_core_export_never_marks_scientific_validation():
    report=build()
    assert all(o["automatic_core_promotion"] is False for o in report["objects"].values())
    assert all(o["scientific_state"]=="UNVERIFIED" for o in report["objects"].values())
    assert all(r["rule_passed"] is None for o in report["objects"].values() for r in o["rules"])

import pytest
from iberos.reviewed_observations import evaluate_reviewed_observations

def test_only_reviewed_sourced_object_observations_execute():
    pending={"evidence_id":"e-1","object_id":"IBR-PLM-0002",
             "review_status":"PENDING","source_reference":"Editorial source","rules":["BI-DISAMBIG-01"]}
    approved={**pending,"evidence_id":"e-2","review_status":"APPROVED_FOR_TECHNICAL_EVALUATION"}
    output=evaluate_reviewed_observations([pending,approved])
    assert len(output["IBR-PLM-0002"])==1
    assert output["IBR-PLM-0002"][0]["results"][0]["status"]=="BLOCKED"
    assert output["IBR-PLM-0002"][0]["automatic_core_promotion"] is False

def test_reject_unknown_or_duplicate_provenance():
    base={"evidence_id":"e-1","object_id":"IBR-PLM-0002",
          "review_status":"APPROVED_FOR_TECHNICAL_EVALUATION",
          "source_reference":"Editorial source","rules":["BI-DISAMBIG-01"]}
    with pytest.raises(ValueError):
        evaluate_reviewed_observations([base,base])
    with pytest.raises(ValueError):
        evaluate_reviewed_observations([{**base,"object_id":"NOT_A_CURATED_OBJECT"}])

def test_web_export_empty_by_default_and_real_executions_when_explicit():
    import importlib.util
    from pathlib import Path
    spec=importlib.util.spec_from_file_location("export_web_core",Path(__file__).resolve().parents[1]/"scripts"/"export_web_core.py")
    mod=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    assert not mod.build()["objects"]["IBR-PLM-0002"]["evaluated_rules"]
    approved={"evidence_id":"e-1","object_id":"IBR-PLM-0002",
              "review_status":"APPROVED_FOR_TECHNICAL_EVALUATION",
              "source_reference":"Editorial source","rules":["BI-DISAMBIG-01"]}
    report=mod.build([approved])["objects"]["IBR-PLM-0002"]["evaluated_rules"][0]
    assert report["results"][0]["status"]=="BLOCKED"

from iberos.publication_priority import build_publication_priority

def test_priority_queue_has_gaps_and_does_not_promote():
    report=build_publication_priority([])
    assert report["pending_count"]==38
    assert all(x["pending_documentation"] and x["scientific_state"]=="UNVERIFIED" for x in report["tasks"])
    assert [x["pending_count"] for x in report["tasks"]]==sorted(x["pending_count"] for x in report["tasks"])

def test_featured_complete_object_is_removed_from_pending():
    entry={"OBJECT_ID":"IBR-PLM-0002","hypothesis":"Propuesta","evidence":"Prueba","limits":"Objeciones","citation":"Edición"}
    report=build_publication_priority([entry])
    assert all(x["object_id"]!="IBR-PLM-0002" for x in report["tasks"])
    assert report["automatic_core_promotion"] is False

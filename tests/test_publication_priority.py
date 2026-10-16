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

def test_pseudoscript_and_known_forgeries_are_not_linguistic_translation_work():
    tasks={x["object_id"]:x for x in build_publication_priority([])["tasks"]}
    assert tasks["IBR-COI-0002"]["workstream"]=="SIGNARY_OR_PSEUDOSCRIPT"
    assert tasks["IBR-CER-0005"]["workstream"]=="SIGNARY_OR_PSEUDOSCRIPT"
    assert tasks["IBR-CTL-0001"]["workstream"]=="CONTROL_AUTHENTICITY"
    assert tasks["IBR-COI-0001"]["workstream"]=="TEXTUAL_INTERPRETATION"
    assert all(x["eligible_for_automatic_translation"] is False for x in tasks.values())

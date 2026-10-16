from iberos.publication_gate import build_publication_manifest

def test_complete_featured_fiche_is_editorially_publishable_not_scientifically_validated():
    entry={"OBJECT_ID":"IBR-PLM-0002","hypothesis":"Propuesta","evidence":"Fuente","limits":"Limitación","citation":"Publicación"}
    result=build_publication_manifest([entry])
    row=result["records"]["IBR-PLM-0002"]
    assert row["publication_status"]=="PUBLICABLE_EDITORIAL"
    assert row["translation_validated"] is False
    assert row["scientific_validation_status"]=="UNVERIFIED"
    assert result["object_count"]==38

def test_missing_citation_blocks_featured_publishability():
    row=build_publication_manifest([{"OBJECT_ID":"IBR-PLM-0002","hypothesis":"Propuesta","evidence":"Fuente","limits":"Límite","citation":""}])["records"]["IBR-PLM-0002"]
    assert row["publication_status"]=="EDITORIAL_REVIEW_REQUIRED"
    assert row["featured_interpretation_available"] is False

def test_missing_citation_is_listed_as_pending():
    row=build_publication_manifest([{"OBJECT_ID":"IBR-PLM-0002","hypothesis":"Propuesta","evidence":"Indicio","limits":"Objeción","citation":""}])["records"]["IBR-PLM-0002"]
    assert "Aportar cita editorial verificable" in row["pending_documentation"]

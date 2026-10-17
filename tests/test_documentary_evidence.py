from iberos.documentary_evidence import build_documentary_evidence

def test_internal_citation_is_not_external_reading_review():
    q=build_documentary_evidence([{"OBJECT_ID":"IBR-PLM-0002","citation":"Cita sugerida de esta ficha: IberOS","bibliography":["Edición impresa, p. 5"]}])
    row=q["records"][0]
    assert row["self_citation_only"] is True
    assert row["reading_approved"] is False
    assert row["original_edition_page_or_figure_checked"] is None
    assert q["automatically_validated"] is False

def test_scholarly_citation_also_requires_independent_verification():
    row=build_documentary_evidence([{"OBJECT_ID":"IBR-MUS-0001","citation":"Simón Cornago (2015)","bibliography":[]}])["records"][0]
    assert row["self_citation_only"] is False
    assert row["reading_approved"] is False

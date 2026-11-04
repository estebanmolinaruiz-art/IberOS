from iberos.catalog_crosswalk import reference_codes, concordance

def record(uid, code, split="TRAIN"):
    return {"uid": uid, "catalog_id": code, "split_v3_4_9": split,
            "dependency_key_v3_4_9": uid}

def test_no_f13_3_prefix_collision():
    registry = [{"OBJECT_ID":"A", "Referencia epigráfica":"MLH F.13.3 · Hesperia V.06.008"}]
    out = concordance(registry, [record("yes","f.13.3 1"),
                                 record("no1","f.13.30"), record("no2","f.13.31")])
    assert [e["uid"] for e in out["cases"][0]["entries"]] == ["yes"]

def test_embedded_b_7_38_is_not_physical_proof():
    reg = [{"OBJECT_ID":"B", "Referencia epigráfica":"B.7.38"}]
    out = concordance(reg, [record("b","RAN21,p61.Pech-Maho B.7.38 (plom6)")])
    assert out["cases"][0]["status"] == "EDITORIAL_REVIEW_REQUIRED"
    assert not out["cases"][0]["physical_identity_verified"]

def test_primary_mlh_not_bdh_and_explicit_double_id():
    assert reference_codes("BDH B.08.01") == []
    assert reference_codes("MLH E.7.1 = K.5.3") == ["e.7.1","k.5.3"]
    assert reference_codes("MLH G.1.1 · Hesperia A.04.01a-b") == ["g.1.1"]
    assert reference_codes("MLH D.12.1-2 · Hesperia HU.01.01-02") == ["d.12.1","d.12.2"]

def test_multisplit_editorial_family_requires_review():
    reg = [{"OBJECT_ID":"D", "Referencia epigráfica":"MLH D.12.1-2"}]
    old = [record("a","d.12.1 a","HOLD"),record("b","d.12.2","TRAIN")]
    out = concordance(reg, old)
    assert out["multisplit_reference_objects"] == ["D"]
    assert out["cases"][0]["status"] == "MULTISPLIT_EDITORIAL_REFERENCE_REVIEW"
    assert old[0]["split_v3_4_9"] == "HOLD"
    assert not out["scientific_promotion"]

def test_no_reference_never_fabricates_match():
    out = concordance([{"OBJECT_ID":"N","Referencia epigráfica":"Por fijar"}], [])
    assert out["cases"][0]["status"] == "NO_EXPLICIT_MLH_REFERENCE"

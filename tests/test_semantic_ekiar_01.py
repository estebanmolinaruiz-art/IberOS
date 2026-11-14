from iberos.semantic_ekiar_01 import DOCUMENTED_CASES, evaluate, interpret

def test_four_attestations_include_correct_archaeological_supports():
    r=evaluate()
    assert r["n_documented_cases"]==4
    assert r["formula_matches"]==4
    assert len(r["contexts"])==4
    assert "GREY_IBERIAN_CERAMIC" in r["contexts"]
    assert "SILVER_VESSEL" not in r["contexts"]

def test_c12_de_egiar_not_falsely_normalized_to_te_ekiar():
    row=next(x for x in evaluate()["outputs"] if x["id"]=="MLH_C_12_2")
    assert "degiar" in row["transcription"]
    assert row["reading_disputed"]
    assert row["morphotype"].startswith("NP-de egiar")
    assert row["person_candidate"]=="bilo[s]aŕker"

def test_coin_name_and_source_are_updated():
    row=next(x for x in evaluate()["outputs"] if x["id"]=="MLH_A_33_2")
    assert row["transcription"].startswith("aŕsbikisteekiar")
    assert row["person_candidate"]=="aŕsbikis"
    assert row["reading_disputed"]

def test_person_extraction_is_not_overtranslated():
    row=next(x for x in evaluate()["outputs"] if x["id"]=="MLH_E_7_1")
    assert row["person_candidate"]=="likine"
    assert "NO distinguibles" in row["semantic_rendering"]
    assert "usekeŕteku" in row["transcription"]

def test_negative_nonmatching_morphotype_abstains():
    row=interpret(dict(id="SYN",kind="CONTROL",transcription="likine salir",
                       name="likine",known_source="test",note="not epi",reading_disputed=False))
    assert not row["formula_attested"]
    assert row["semantic_rendering"] is None

def test_english_role_is_only_broad():
    r=evaluate()
    assert r["verb_versus_noun_unresolved"]
    assert r["producer_versus_sponsor_unresolved"]
    assert r["novel_lexical_decipherments"] == 0
    assert r["independently_held_out_evaluations"] == 0
    assert r["novel_blind_accuracy"] is None
    assert not r["full3406_accessed"]

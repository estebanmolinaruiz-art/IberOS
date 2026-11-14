from iberos.semantic_ekiar_01 import evaluate, interpret

def test_cross_support_formula_without_pretending_blind():
    r=evaluate()
    assert r["n_documented_cases"]==4
    assert r["formula_matches"]==4
    assert len(r["contexts"])==4
    assert r["independently_held_out_evaluations"]==0

def test_person_extraction_and_not_forced_translation():
    x=next(x for x in evaluate()["outputs"] if x["id"]=="MLH_E_7_1")
    assert x["person_candidate"]=="likine"
    assert "autor o comitente" in x["semantic_rendering"]
    assert x["role_predicted"]=="PERSON_ASSOCIATED_WITH_PRODUCTION_OR_COMMISSION"

def test_known_variants_and_unresolved_differences():
    r=evaluate()
    assert r["verb_versus_noun_unresolved"] is True
    assert r["producer_versus_sponsor_unresolved"] is True
    assert r["novel_lexical_decipherments"]==0

def test_no_translation_on_nonmatching_pattern():
    case=dict(id="SYN",kind="TEST",transcription="likine salir",name="likine",
              known_source="none",note="negative control")
    x=interpret(case)
    assert not x["formula_attested"]
    assert x["semantic_rendering"] is None

def test_no_frozen_corpus_or_fake_metrics():
    r=evaluate()
    assert not r["full3406_accessed"]
    assert not r["official_metrics_modified"]
    assert r["novel_blind_accuracy"] is None

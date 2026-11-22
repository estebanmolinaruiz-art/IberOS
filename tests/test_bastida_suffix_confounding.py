"""SCI-SEM-05: verify name confound and exact subset enumeration."""
import json
from pathlib import Path
import pytest
from iberos.bastida_suffix_confounding import analyse

DATA=Path(__file__).resolve().parents[1]/"data/review/sci_sem04_bastida_19_entries_ferrer2026.json"

def original():
    return json.loads(DATA.read_text(encoding="utf-8"))

def test_original_name_confound():
    x=analyse(original())
    assert x["distinct_names"]==12
    assert x["ku_names"]==["aiduaŕgi","saldulako"]
    assert x["names_with_both_suffixes"]==[]
    assert x["person_conditioned_label_swaps_possible"]==0
    assert not x["suffix_separable_from_person_within_artifact"]
    assert not x["semantic_direction_confirmed"]

def test_exact_sensitivity():
    x=analyse(original())["sensitivity"]
    for key,n,k in [
        ("all_19",750,4),
        ("without_beŕśir_high_549_5",600,1),
        ("without_all_beŕśir",270,1),
        ("without_editorially_corrected",240,4),
    ]:
        assert x[key]["assignments"]==n
        assert x[key]["as_or_more_extreme"]==k
        assert x[key]["p_one_sided_conditional"]==pytest.approx(k/n)

def test_invalid_change_not_silently_accepted():
    d=original()
    d["entries"][0]["suffix_editorial"]="ku"
    with pytest.raises(ValueError):
        analyse(d)

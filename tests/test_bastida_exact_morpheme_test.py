"""Protect the original 19-row published edition and its scientific limits."""
import json
from pathlib import Path
import pytest
from iberos.bastida_exact_morpheme_test import analyse

DATA=Path(__file__).resolve().parents[1]/"data/review/sci_sem04_bastida_19_entries_ferrer2026.json"


def original():
    return json.loads(DATA.read_text(encoding="utf-8"))


def test_all_original_rows_exact_stratified_association():
    x=analyse(original())
    assert x["rows"]==19 and x["physical_artifacts"]==1
    assert (x["ka_entries"],x["ku_entries"])==(14,5)
    assert x["median_ka_editorial_g"]==21
    assert x["median_ku_editorial_g"]==441
    assert x["exact_assignments"]==750
    assert x["one_sided_assignments_ge_observed"]==4
    assert x["conditional_one_sided_p"]==pytest.approx(4/750)
    assert x["exception"].startswith("beŕśir")
    assert not x["actual_translation_demonstrated"]
    assert x["semantic_success_count"]==0


def test_no_relabel_and_no_false_measurement_gold():
    data=original()
    data["entries"][4]["suffix_editorial"]="ka"
    with pytest.raises(ValueError):
        analyse(data)
    data=original()
    data["entries"][0]["image_read_independently"]=True
    with pytest.raises(ValueError):
        analyse(data)
    data=original()
    data["entries"][0]["measurement_status"]="INSTRUMENT_MEASURED"
    with pytest.raises(ValueError):
        analyse(data)


def test_missing_row_rejected():
    data=original()
    data["entries"].pop()
    with pytest.raises(ValueError):
        analyse(data)

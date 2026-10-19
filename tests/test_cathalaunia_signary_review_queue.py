import importlib.util
from pathlib import Path
p=Path(__file__).resolve().parents[1]/"scripts"/"cathalaunia_signary_review_queue.py"
spec=importlib.util.spec_from_file_location("queue",p);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
def test_simple_te():assert m.classify("te13")==("SIMPLE_SOURCE_LABEL","te")
def test_uncertain_ke():assert m.classify("ke14?")==("AMBIGUOUS","")
def test_dual_variant_not_dropped():assert m.classify("kiB14")[0]=="DUAL_OR_DISTINCT_SERIES"
def test_capital_series_not_equated():assert m.classify("S87")[0]=="DUAL_OR_DISTINCT_SERIES"
def test_multiple_variants_are_ambiguous():assert m.classify("o2,o3")[0]=="AMBIGUOUS"
def test_punctuation_not_transliterated():assert m.classify("pun1")[0]=="NONREADING_OR_SPECIAL"

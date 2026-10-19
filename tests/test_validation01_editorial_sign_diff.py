import importlib.util,csv
from pathlib import Path
root=Path(__file__).resolve().parents[1]
s=importlib.util.spec_from_file_location('align',root/'scripts/validation01_editorial_sign_diff.py')
m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
def test_real_editorial_pair():
 with (root/'data/review/validation01_orleyl_fletcher_editorial_alignment_v1.csv').open(encoding='utf8') as f:r=list(csv.DictReader(f))
 d=m.align(r[0]['atomic_core_tokens'],r[1]['atomic_core_tokens'])
 assert d['edit_distance']==1
 assert d['differences']==[{'operation':'ONLY_IN_FIRST','sign':'te','index':5}]
 assert d['linguistic_validation']=='NOT_EVALUATED'
def test_same_sign_is_not_phonetic_splitting():
 assert m.align('ta e','te')['edit_distance']!=0

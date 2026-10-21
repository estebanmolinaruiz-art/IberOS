"""IberOS M06 adversarial checks, entirely in temporary directories."""
import csv
import hashlib
import importlib.util
import json
import shutil
import tempfile
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('m06', ROOT/'scripts/validation01_m06_gate.py')
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)

def fixture(root):
    d=root/'data/review';d.mkdir(parents=True)
    shutil.copy(ROOT/'data/review/validation01_orleyl_17_visual_alignment_v1.csv',d)
    (d/'validation01_progress_scorecard_v1.json').write_text(json.dumps({'milestones':[{'id':'M06','status':'DONE'}]}))
    (root/'synthetic-evidence.txt').write_text('SYNTHETIC TEST ONLY')
    digest=hashlib.sha256((root/'synthetic-evidence.txt').read_bytes()).hexdigest()
    with (d/'validation01_orleyl_17_visual_alignment_v1.csv').open() as f:
        signs=[{**{k:r[k] for k in ('object_id','editorial_word','index')},
                'status':'REVIEWED','editorial_key_hidden':True,'bbox':[0,0,10,10],
                'reviewer':'synthetic reviewer','review_record':'synthetic record',
                'variant_id':'synthetic variant','signary_reference':'synthetic reference',
                'discrepancy_notes':'none in synthetic fixture',
                **{p+'_path':'synthetic-evidence.txt' for p in ('source','crop','review')},
                **{p+'_sha256':digest for p in ('source','crop','review')}} for r in csv.DictReader(f)]
    (d/'validation01_m06_evidence_v1.json').write_text(json.dumps({'signs':signs}))
    return signs

def test_current_m06_blocked():
    assert m.evaluate(ROOT)['gate']=='BLOCKED'

def test_done_without_evidence_rejected():
    with tempfile.TemporaryDirectory() as tmp:
        root=Path(tmp);fixture(root)
        (root/'data/review/validation01_m06_evidence_v1.json').unlink()
        assert m.evaluate(root)['gate']=='BLOCKED'

def test_integrity_control_and_adversarial_mutations():
    with tempfile.TemporaryDirectory() as tmp:
        root=Path(tmp);signs=fixture(root)
        assert m.evaluate(root)['gate']=='EVIDENCE_REFERENCES_CHECKED'
        for field,value in [('status','PENDING'),('editorial_key_hidden',False),('variant_id','UNRESOLVED'),('crop_sha256','wrong'),('review_path','../outside'),('bbox',[10,0,0,1])]:
            bad=json.loads(json.dumps(signs));bad[0][field]=value
            (root/'data/review/validation01_m06_evidence_v1.json').write_text(json.dumps({'signs':bad}))
            assert m.evaluate(root)['gate']=='BLOCKED',field
        (root/'data/review/validation01_m06_evidence_v1.json').write_text(json.dumps({'signs':signs[:-1]}))
        assert m.evaluate(root)['gate']=='BLOCKED'

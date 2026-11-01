import json
from pathlib import Path
from scripts.corex_p01 import load,run
def test_ineligible_reading_blocked(tmp_path):
    p=tmp_path/'x.jsonl'
    p.write_text(json.dumps(dict(object_id='1',physical_group='p',transcription='abcdefghi',source='test',reading_status='EDITORIAL'))+'\n')
    rows,errors=load(p)
    assert not rows and errors
def test_independent_split():
    rows=[dict(object_id=str(i),physical_group=f'p{i}',transcription='abce abce abcdef',source='synthetic',reading_status='EXPERT_REVIEWED') for i in range(8)]
    r=run(rows)
    assert r['status']=='EXPERIMENTAL_BASELINE_ONLY'
    assert r['training_groups']+r['holdout_groups']==8
    assert r['not_semantic_validation']
def test_insufficient():
    assert run([])['status']=='INSUFFICIENT_INDEPENDENT_GROUPS'

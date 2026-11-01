import json
from pathlib import Path
import importlib.util

module_path = Path(__file__).resolve().parents[1] / 'scripts' / 'corex_p01.py'
spec = importlib.util.spec_from_file_location('corex_p01', module_path)
corex = importlib.util.module_from_spec(spec)
spec.loader.exec_module(corex)
load, run = corex.load, corex.run
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

def test_stability_tracks_variation_without_semantic_claims():
    rows=[dict(object_id=str(i),physical_group=f'p{i}',transcription=('abce abce abcdef' if i%2 else 'kutu kutu kitura'),source='synthetic',reading_status='EXPERT_REVIEWED') for i in range(12)]
    result=corex.stability(rows)
    assert result['status']=='EXPERIMENTAL_STABILITY_ONLY'
    assert result['trials']==20
    assert result['independent_group_holdout'] is True
    assert 0<=result['bigram_wins']<=20
    assert result['not_semantic_validation'] is True
    for metric in ('frequency_accuracy','left_bigram_accuracy'):
        value=result[metric]
        assert 0<=value['min']<=value['median']<=value['max']<=1

def test_stability_requires_independent_groups():
    assert corex.stability([])['status']=='INSUFFICIENT_FOR_STABILITY'

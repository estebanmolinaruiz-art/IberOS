#!/usr/bin/env python3
"""Dama de Ilice CORE-X P01: leak-resistant character prediction baseline.
Input JSONL: {object_id, physical_group, transcription, source, reading_status}.
Not a semantic decipherment test.
"""
import argparse, collections, hashlib, json, random, re
from pathlib import Path
ALLOWED={'INDEPENDENT_VERIFIED','EXPERT_REVIEWED'}
def load(path):
    seen=set(); rows=[]; failures=[]
    for n,line in enumerate(Path(path).read_text(encoding='utf-8').splitlines(),1):
        if not line.strip(): continue
        try: o=json.loads(line)
        except Exception as e: failures.append(f'line {n}: invalid JSON: {e}');continue
        missing=[k for k in ('object_id','physical_group','transcription','source','reading_status') if not str(o.get(k,'')).strip()]
        if missing: failures.append(f'line {n}: missing {missing}');continue
        if o['reading_status'] not in ALLOWED:failures.append(f'line {n}: non-verified reading');continue
        seq=re.sub(r'\s+',' ',str(o['transcription']).lower()).strip()
        if not re.fullmatch(r'[a-záéíóúüñśŕḿ· :|/-]+',seq) or len(seq.replace(' ',''))<8:
            failures.append(f'line {n}: transcription too short/ambiguous');continue
        k=(o['physical_group'],seq)
        if k in seen:failures.append(f'line {n}: duplicate physical group and transcription');continue
        seen.add(k);rows.append({**o,'transcription':seq})
    return rows,failures
def run(rows,seed=29):
    groups=sorted({r['physical_group'] for r in rows})
    if len(groups)<6:return {'status':'INSUFFICIENT_INDEPENDENT_GROUPS','groups':len(groups),'needed':6}
    rng=random.Random(seed);rng.shuffle(groups);held=set(groups[:max(1,round(len(groups)*.25))])
    train=[r for r in rows if r['physical_group'] not in held];test=[r for r in rows if r['physical_group'] in held]
    if not train or not test:return {'status':'INSUFFICIENT_SPLIT'}
    prior=collections.Counter();left=collections.defaultdict(collections.Counter)
    def chars(r):return re.sub(r'[^a-záéíóúüñśŕḿ]','',r['transcription'])
    for r in train:
        for i,c in enumerate(chars(r)):prior[c]+=1;left[chars(r)[i-1] if i else '^'][c]+=1
    if not prior:return {'status':'NO_TRAINING_CHARS'}
    freq=prior.most_common(1)[0][0];total=correct=ngcorrect=0
    for row in test:
        sequence=chars(row)
        for i,c in enumerate(sequence):
            total+=1;correct+=(freq==c)
            context=sequence[i-1] if i else '^'
            guess=left[context].most_common(1)[0][0] if left[context] else freq
            ngcorrect+=(guess==c)
    return {'status':'EXPERIMENTAL_BASELINE_ONLY','seed':seed,'training_groups':len({x['physical_group'] for x in train}),'holdout_groups':len(held),'test_characters':total,'frequency_accuracy':round(correct/total,4),'left_bigram_accuracy':round(ngcorrect/total,4),'not_semantic_validation':True}
def main():
    p=argparse.ArgumentParser();p.add_argument('jsonl');p.add_argument('--seed',type=int,default=29);a=p.parse_args()
    rows,reasons=load(a.jsonl);result=run(rows,a.seed)
    result.update(accepted_rows=len(rows),rejected_rows=len(reasons),rejection_reasons=reasons[:30],input_sha256=hashlib.sha256(Path(a.jsonl).read_bytes()).hexdigest())
    print(json.dumps(result,ensure_ascii=False,indent=2))
if __name__=='__main__':main()

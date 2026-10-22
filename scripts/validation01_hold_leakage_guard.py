#!/usr/bin/env python3
"""Reject known development objects and conservatively normalized aliases from HOLD."""
import csv,json,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent))
from validation01_identity import identity, identities, declared_conflict
ROOT=Path(__file__).resolve().parents[1]
KNOWN=('ORLEYL V','ORLEYL VII','F.9.5','F.9.7','IBR-PLM-0006')
def known_ids(screening,critical):
    rows=list(screening)+list(critical)
    ids={identity(x) for x in KNOWN}
    for row in rows: ids.update(identities(row))
    return {x for x in ids if x}
def evaluate(hold,screening,critical):
    known=known_ids(screening,critical)
    issues=[];seen={}
    for i,row in enumerate(hold,2):
        if row.get('split','').upper()!='HOLD':continue
        keys=identities(row)
        if declared_conflict(row):issues.append({'row':i,'issue':'CONFLICTING_KNOWN_ALIASES'})
        if keys & known:issues.append({'row':i,'issue':'KNOWN_DEVELOPMENT_OBJECT_IN_HOLD','matches':sorted(keys & known)})
        for k in keys:
            if k in seen:issues.append({'row':i,'issue':'DUPLICATE_HOLD_IDENTITY','previous_row':seen[k],'identity':k})
            seen[k]=i
    return {'gate':'BLOCKED' if issues else 'PASS_KNOWN_OBJECT_SCREEN','known_development_ids':len(known),'issues':issues,
        'note':'Only documented aliases and normalized exact identifiers are matched. Other uncertain provenance remains subject to human review.'}
def load(path):
    with open(path,encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))
if __name__=='__main__':
    print(json.dumps(evaluate(load(ROOT/'data/review/validation01_holdout_v1.csv'),load(ROOT/'data/review/validation01_te_screening_2026-10-19.csv'),load(ROOT/'data/review/validation01_orleyl_critical_lines_v1.csv')),ensure_ascii=False,indent=2))

#!/usr/bin/env python3
"""Structural editorial alignment only: never infer grammatical TE or glyph truth."""
import csv,sys,json
from pathlib import Path
def align(a,b):
 x=a.split();y=b.split();n=len(x);m=len(y)
 d=[[0]*(m+1) for _ in range(n+1)]
 for i in range(n+1):d[i][0]=i
 for j in range(m+1):d[0][j]=j
 for i in range(1,n+1):
  for j in range(1,m+1):
   d[i][j]=min(d[i-1][j]+1,d[i][j-1]+1,d[i-1][j-1]+(x[i-1]!=y[j-1]))
 i=n;j=m;ops=[]
 while i or j:
  if i and j and x[i-1]==y[j-1] and d[i][j]==d[i-1][j-1]:i-=1;j-=1;continue
  if i and d[i][j]==d[i-1][j]+1:ops.append({'operation':'ONLY_IN_FIRST','sign':x[i-1],'index':i-1});i-=1;continue
  if j and d[i][j]==d[i][j-1]+1:ops.append({'operation':'ONLY_IN_SECOND','sign':y[j-1],'index':j-1});j-=1;continue
  ops.append({'operation':'SUBSTITUTION','from':x[i-1],'to':y[j-1]});i-=1;j-=1
 return {'edit_distance':d[n][m],'differences':ops[::-1],'evidence_level':'EDITORIAL_ATOMIC_TOKEN_COMPARISON','linguistic_validation':'NOT_EVALUATED'}
if __name__=='__main__':
 with open(sys.argv[1] if len(sys.argv)>1 else 'data/review/validation01_orleyl_fletcher_editorial_alignment_v1.csv',encoding='utf8',newline='') as f:r=list(csv.DictReader(f))
 if len(r)!=2:raise SystemExit('Expected exactly V and VII-B editorial pairs')
 print(json.dumps(align(r[0]['atomic_core_tokens'],r[1]['atomic_core_tokens']),ensure_ascii=False,indent=2))

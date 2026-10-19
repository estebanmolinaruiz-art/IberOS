#!/usr/bin/env python3
"""Stage XLSX editorial readings without discarding rich text uncertainty.
Requires Python standard library only; does not infer Iberian glyph values."""
import argparse,csv,json,zipfile,re
from xml.etree import ElementTree as E
M={'x':'http://schemas.openxmlformats.org/spreadsheetml/2006/main','r':'http://schemas.openxmlformats.org/officeDocument/2006/relationships'}
def runs(si):
    if si is None:return []
    rr=si.findall('x:r',M)
    if not rr:rr=[si]
    out=[]
    for r in rr:
        t=r.find('x:t',M)
        if t is None:continue
        p=r.find('x:rPr',M)
        out.append({'text':t.text or '','bold':p is not None and p.find('x:b',M) is not None,
          'underline':p is not None and p.find('x:u',M) is not None,
          'italic':p is not None and p.find('x:i',M) is not None})
    return out
def col(c):
    n=0
    for x in re.match(r'[A-Z]+',c).group(0):n=n*26+ord(x)-64
    return n
def convert(src,out,sheet=None,ref_col=1,text_col=2):
    records=[]
    with zipfile.ZipFile(src) as z:
        shared=[]
        if 'xl/sharedStrings.xml' in z.namelist():
            s=E.fromstring(z.read('xl/sharedStrings.xml'))
            shared=[runs(i) for i in s.findall('x:si',M)]
        wb=E.fromstring(z.read('xl/workbook.xml'))
        rel=E.fromstring(z.read('xl/_rels/workbook.xml.rels'))
        targets={r.attrib['Id']:r.attrib['Target'] for r in rel}
        for sh in wb.findall('x:sheets/x:sheet',M):
            name=sh.get('name')
            if sheet and name!=sheet:continue
            target=targets[sh.get('{'+M['r']+'}id')].lstrip('/')
            path=target if target.startswith('xl/') else 'xl/'+target
            xml=E.fromstring(z.read(path))
            for row in xml.findall('x:sheetData/x:row',M):
                if int(row.get('r'))==1:continue
                values={}
                for c in row.findall('x:c',M):
                    v=c.find('x:v',M)
                    i=c.find('x:is',M)
                    if c.get('t')=='s' and v is not None:parts=shared[int(v.text)]
                    elif i is not None:parts=runs(i)
                    elif v is not None:parts=[{'text':v.text or '','bold':False,'underline':False,'italic':False}]
                    else:parts=[]
                    values[col(c.get('r'))]=parts
                ref=''.join(p['text'] for p in values.get(ref_col,[]))
                parts=values.get(text_col,[])
                raw=''.join(p['text'] for p in parts)
                if not ref.strip() or not raw.strip():continue
                records.append({'reference':ref,'transcription_raw':raw,'source_sheet':name,'source_row':row.get('r'),
                  'editorial_markup':json.dumps(parts,ensure_ascii=False),
                  'uncertainty':'MARKED' if any(p['bold'] or p['underline'] or p['italic'] for p in parts) else 'UNASSESSED',
                  'reading_state':'RAW_UNREVIEWED','te_status':'UNKNOWN','hold_eligible':'NO'})
    if sheet and not records:raise ValueError('No matching nonempty records in chosen sheet')
    with open(out,'w',encoding='utf-8',newline='') as f:
        fields=['reference','transcription_raw','source_sheet','source_row','editorial_markup','uncertainty','reading_state','te_status','hold_eligible']
        w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(records)
    return len(records)
if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('input');p.add_argument('output');p.add_argument('--sheet')
    p.add_argument('--reference-col',type=int,default=1);p.add_argument('--transcription-col',type=int,default=2)
    a=p.parse_args()
    print(json.dumps({'records_staged':convert(a.input,a.output,a.sheet,a.reference_col,a.transcription_col),
                     'verified_readings':0,'holdout':0}))

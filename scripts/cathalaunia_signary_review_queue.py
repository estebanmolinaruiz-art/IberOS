#!/usr/bin/env python3
"""Review queue for Cathalaunia font labels, not validation of glyph readings."""
import argparse,csv,json,re
from collections import Counter
BASE=set("a e i o u l m n r ŕ s ś ḿ ba be bi bo bu ta te ti to tu ka ke ki ko ku".split())
def classify(label):
    parts=[x.strip() for x in re.split(r"[,/]",label)]
    if any("?" in x for x in parts) or len(parts)!=1:return ("AMBIGUOUS","")
    m=re.fullmatch(r"([A-Za-zŕśḿ]+?)(B?)([0-9]+)",parts[0])
    if not m:return ("NONSTANDARD_LABEL","")
    base,dual,_=m.groups()
    # Do not silently collapse capitals (S vs s / R vs r / M vs m) or B-series.
    if dual or base!=base.lower():return ("DUAL_OR_DISTINCT_SERIES","")
    if base in BASE:return ("SIMPLE_SOURCE_LABEL",base)
    return ("NONREADING_OR_SPECIAL","")
def transform(rows):
    out=[]
    for r in rows:
        kind,candidate=classify(r["source_variant_label"])
        out.append({"unicode_decimal":r["unicode_decimal"],"source_variant_label":r["source_variant_label"],
                    "source_value_candidate":candidate,"review_queue":kind,"independent_review":"PENDING",
                    "usable_for_auto_reading":"NO","source_url":r["source_url"]})
    return out
def main():
    p=argparse.ArgumentParser();p.add_argument("input");p.add_argument("output");a=p.parse_args()
    with open(a.input,encoding="utf-8",newline="") as f:out=transform(csv.DictReader(f))
    with open(a.output,"w",encoding="utf-8",newline="") as f:
        w=csv.DictWriter(f,fieldnames=list(out[0]));w.writeheader();w.writerows(out)
    print(json.dumps({"total":len(out),"classification":dict(Counter(x["review_queue"] for x in out)),"auto_reading_activated":0}))
if __name__=="__main__":main()

"""Evidence-based six-pillar CORE readiness audit. Never equate coverage with scientific validity."""
from __future__ import annotations
import csv
import json
from collections import Counter
from pathlib import Path

PILLARS = {
 "paleography": ["data/review/orleyl_te_glyph_review_v1.json", "data/review/palaeographic_alignment_priority_v1.json"],
 "hypotheses": ["src/iberos/semantic_hypothesis_engine.py", "src/iberos/rule_catalog.py"],
 "symbols": ["src/iberos/multimodule.py", "data/review/cathalaunia_signary_review_queue_286_v2.csv"],
 "independent_validation": ["data/review/validation01_preregistration_v1.json", "data/review/validation01_progress_scorecard_v1.json"],
 "corpus": ["data/curated/iberos_curated_objects_v1.jsonl", "data/curated/iberos_objects_registry_v2.0.csv"],
 "reproducible_lab": ["scripts/validation01_pipeline.py", "scripts/validation01_blind_score.py"]
}
def audit(root: Path) -> dict:
    root=Path(root)
    pillars={}
    for key,files in PILLARS.items():
        existing=[p for p in files if (root/p).is_file()]
        pillars[key]={"files_present":len(existing),"files_expected":len(files),
                      "missing":[p for p in files if p not in existing],
                      "evidence_status":"INFRASTRUCTURE_ONLY" if len(existing)==len(files) else "INCOMPLETE"}
    records=[]
    path=root/PILLARS["corpus"][0]
    if path.exists():
        for line in path.read_text(encoding="utf-8").splitlines():
            if line.strip():
                records.append(json.loads(line))
    ids=[x.get("object_id") for x in records]
    known=[i for i in ids if isinstance(i,str) and i.strip()]
    corpus={"records":len(records),"unique_nonempty_ids":len(set(known)),
            "duplicate_ids":sorted(k for k,v in Counter(known).items() if v>1),
            "missing_ids":len(records)-len(known),
            "records_with_source":sum(bool(x.get("source")) for x in records),
            "records_with_provenance":sum(bool(x.get("provenance")) for x in records)}
    validation_path=root/"data/review/validation01_progress_scorecard_v1.json"
    validation={"scientific_status":"NOT_EVALUATED","completed_milestones":0,"total_milestones":0}
    if validation_path.exists():
        score=json.loads(validation_path.read_text(encoding="utf-8"))
        steps=score.get("milestones",[])
        validation={"scientific_status":score.get("scientific_status","NOT_EVALUATED"),
                    "completed_milestones":sum(s.get("status")=="DONE" for s in steps),
                    "total_milestones":len(steps)}
    orleyl_path=root/"data/review/orleyl_te_glyph_review_v1.json"
    glyph_verified=False
    if orleyl_path.exists():
        glyph_verified=json.loads(orleyl_path.read_text(encoding="utf-8")).get("exact_glyph_coordinates_verified") is True
    blockers=[]
    if not glyph_verified: blockers.append("Orleyl glyph coordinates not independently verified")
    if validation["scientific_status"] not in ("VALIDATED","REPLICATED"):
        blockers.append("Independent scientific validation not demonstrated")
    if corpus["duplicate_ids"] or corpus["missing_ids"]:
        blockers.append("Corpus object identifier integrity problems")
    return {"schema":"IberOS-Core-Six-Pillar-Audit/1.0","pillars":pillars,
            "corpus":corpus,"validation":validation,
            "orleyl_glyphs_verified":glyph_verified,"scientific_blockers":blockers,
            "semantic_promotion_allowed":False,
            "interpretation":"File presence is technical coverage, not scientific verification."}

def main():
    import argparse
    parser=argparse.ArgumentParser()
    parser.add_argument("--root",type=Path,default=Path(__file__).resolve().parents[1])
    parser.add_argument("--out",type=Path)
    args=parser.parse_args()
    result=json.dumps(audit(args.root),indent=2,ensure_ascii=False)+"\n"
    if args.out:
        args.out.parent.mkdir(parents=True,exist_ok=True)
        args.out.write_text(result,encoding="utf-8")
    else: print(result,end="")

if __name__=="__main__":
    main()

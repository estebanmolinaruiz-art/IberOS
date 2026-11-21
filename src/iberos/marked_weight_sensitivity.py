"""SCI-MET-04: test *observational sensitivity* to 2 vs 3 marks, not meaning.

Three real published weights. Fits only Bas-129-A and Bas-273-C, evaluates
the already-known Bas-273-B retrospectively. No blind semantic gold.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

DATA = Path(__file__).resolve().parents[2] / "data/review/sci_met04_bastida_dot_mark_cases_v1.json"


def evaluate(document: dict) -> dict:
    if document.get("schema") != "IberOS-SCI-MET-04-Marked-Bastida-Objects/1.0":
        raise ValueError("Unexpected data schema")
    calibration = document.get("calibration_objects")
    target = document.get("preidentified_contradiction")
    if not isinstance(calibration,list) or len(calibration)!=2 or not isinstance(target,dict):
        raise ValueError("Two calibration weights and one targeted discrepancy required")
    if [c.get("id") for c in calibration] != ["Bas-129-A","Bas-273-C"] or target.get("id")!="Bas-273-B":
        raise ValueError("Unexpected archaeological object identities")
    if [x.get("reported_dot_count") for x in calibration] != [2,5]:
        raise ValueError("Calibration mark counts cannot be silently rewritten")
    if target.get("reported_dot_count")!=2 or target.get("alternative_unseen_dot_count")!=3:
        raise ValueError("Two-vs-three mark sensitivity requires original declared uncertainty")
    if {x.get("department") for x in calibration} != {"129","273"} or target.get("department")!="273":
        raise ValueError("Cannot swap archaeological dependencies")
    for row in [*calibration,target]:
        if (type(row.get("mass_g")) not in (float,int) or not math.isfinite(row["mass_g"])
                or row["mass_g"]<=0 or row.get("visual_image_adjudicated") is not False):
            raise ValueError("Missing valid published mass or unverified visual status")
    # Least-squares quantum from two externally published mass/count observations.
    marks=[c["reported_dot_count"] for c in calibration]
    weights=[c["mass_g"] for c in calibration]
    quantum=sum(n*m for n,m in zip(marks,weights))/sum(n*n for n in marks)
    outcomes=[]
    for n in (target["reported_dot_count"],target["alternative_unseen_dot_count"]):
        expected=quantum*n
        residual=target["mass_g"]-expected
        outcomes.append({
            "assumed_mark_count":n,
            "predicted_mass_g":round(expected,6),
            "signed_residual_g":round(residual,6),
            "absolute_relative_error_pct":round(100*abs(residual)/expected,6),
            "within_descriptive_10pct_band":abs(residual)/expected<=0.10,
            "assumption_photographically_verified":False,
        })
    return {
        "schema":"IberOS-SCI-MET-04-Point-Count-Sensitivity/1.0",
        "experiment":"SCI-MET-04",
        "calibration_object_ids":[c["id"] for c in calibration],
        "calibration_quantum_g":round(quantum,6),
        "calibration_values_g":weights,
        "target_object_id":target["id"],
        "target_mass_g":target["mass_g"],
        "archaeological_dependency_warning":"Bas-273-B and Bas-273-C both from department 273: not two independent prospective contexts.",
        "alternative_mark_count_scenarios":outcomes,
        "number_of_marks_verified_from_original_image":False,
        "interpretation":"Two photographed dots would contradict the common 20-21g/point reading for this group; if a THIRD dot exists the same mass is within 3% of a three-unit reading. Neither meaning is established.",
        "clinical_or_statistical_certification":False,
        "blind_test":False,
        "confirmed_iberian_sign_values":0,
        "confirmed_translations":0,
        "core_or_full3406_modified":False,
        "cost_eur":0,
    }


def main(argv=None):
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--input",type=Path,default=DATA)
    p.add_argument("--output",type=Path)
    args=p.parse_args(argv)
    report=evaluate(json.loads(args.input.read_text(encoding="utf-8")))
    text=json.dumps(report,ensure_ascii=False,indent=2)+"\n"
    if args.output:
        if args.input.resolve()==args.output.resolve():
            raise ValueError("Cannot overwrite original source")
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(text,encoding="utf-8")
    else: print(text,end="")
    return 0


if __name__=="__main__":
    raise SystemExit(main())

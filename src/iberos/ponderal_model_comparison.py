"""SCI-MET-03: quantify published mass series without inventing mark semantics.

Model comparison is retrospective and cannot decide whether 21 g is a full
unit or half of 42 g. A diagram/report from a publication is NOT an independent
blind reading of the artefact. Does not modify Core or HOLD.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data/review/sci_met03_published_weights_v1.json"


def _rms(observed: list[float], predicted: list[float]) -> float:
    if len(observed) != len(predicted) or not observed:
        raise ValueError("At least one matched mass/ratio pair required")
    return math.sqrt(sum((a-b)**2 for a,b in zip(observed,predicted)) / len(observed))


def analyse(payload: dict) -> dict:
    if payload.get("schema") != "IberOS-SCI-MET-03-Sourced-Masses/1.0":
        raise ValueError("Unknown source dataset")
    groups = {g["group_id"]:g for g in payload["groups"]}
    vj = groups["VILLANUEVA_JARA_DEPOSIT"]
    masses = vj["mass_g"]
    ratios = vj["published_ratios_21g"]
    if len(masses) != 5 or ratios != [1,2,3,5,10]:
        raise ValueError("Fixed archaeological reference series altered")
    if any(type(x) not in (int, float) or not math.isfinite(x) or x<=0
           for x in masses):
        raise ValueError("Invalid mass")
    fitted = sum(m*r for m,r in zip(masses,ratios))/sum(r*r for r in ratios)
    original = {u: _rms(masses, [u*r for r in ratios])
                for u in (20.525,21.0,fitted)}
    aras = groups["ARAS_ECOMUSEO_DONATED"]
    marked, other, small = aras["objects"]
    if (marked["reported_incisions"] != 2 or marked["reported_shape"] != "TRIANGULAR"
            or marked["same_symbol_as_iberian_o"] != "UNDEMONSTRATED"):
        raise ValueError("Mark category not independently verified")
    # Model A: one 41.05 g unit, two marks denote non-numeric workshop or class.
    # Model B: two equal 20.525 g subunits. They predict the SAME observed mass.
    one_unit = marked["mass_g"]
    two_subunits = marked["mass_g"]/2
    comparison = groups["COMPARATIVE_DOT_MARKS_2026"]["objects"]
    per_mark = []
    for obj in comparison:
        n=obj["reported_incisions"]
        per_mark.append({
            "id":obj["id"],"reported_shape":obj["reported_shape"],
            "mass_g":obj["mass_g"], "mark_count":n,
            "mass_per_mark_if_additive_g":round(obj["mass_g"]/n,5),
            "additive_semantics_verified":False,
        })
    if not math.isclose(_rms(masses,[fitted*r for r in ratios]),
                        _rms(masses,[2*fitted*(r/2) for r in ratios]),abs_tol=1e-10):
        raise AssertionError("Half-unit model must be observationally identical")
    return {
        "schema":"IberOS-SCI-MET-03-Retrospective-Comparison/1.0",
        "villanueva": {
            "ratios_published":ratios,
            "fitted_unit21_g":round(fitted,6),
            "rms_g_21_fixed":round(original[21.0],6),
            "rms_g_20_525_from_aras_fixed":round(original[20.525],6),
            "rms_g_21_fitted":round(original[fitted],6),
            "observed_masses_g":masses,
            "model_42_with_half_ratios_exactly_identical_to_21":True,
            "semi_unit_hypothesis_equivalent": "42.69928057553957 g with ratios 0.5,1,1.5,2.5,5 yields the same predicted masses as fitted 21.349640287769785 g"
        },
        "aras": {
            "marked_mass_g":one_unit,
            "marks_reported":2,
            "one_41_05_unit_if_marks_non_quantitative":one_unit,
            "two_20_525_units_if_each_mark_additive":two_subunits,
            "companion_unmarked_mass_g":other["mass_g"],
            "companion_small_mass_g":small["mass_g"],
            "mass_does_not_discriminate_mark_interpretations":True,
            "image_sign_collation_completed":False,
        },
        "published_comparative_mark_controls":per_mark,
        "exclusion_warning":"Do not pool marks of different graphic shapes or unverified provenance as if identical numerals.",
        "scientific_result":"UNDERDETERMINED_MARK_SEMANTICS",
        "independent_blind_semantic_success":False,
        "validated_translation_count":0,
        "full3406_modified":False,
        "cost_eur":0,
    }


def main(argv=None):
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--input",type=Path,default=DATA)
    ap.add_argument("--output",type=Path)
    a=ap.parse_args(argv)
    result=analyse(json.loads(a.input.read_text(encoding="utf-8")))
    encoded=json.dumps(result,ensure_ascii=False,indent=2)+"\n"
    if a.output:
        if a.input.resolve()==a.output.resolve():
            raise ValueError("Refuse source overwrite")
        a.output.parent.mkdir(parents=True,exist_ok=True)
        a.output.write_text(encoded,encoding="utf-8")
    else:
        print(encoded,end="")
    return 0

if __name__=="__main__":
    raise SystemExit(main())

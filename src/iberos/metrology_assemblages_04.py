"""METROLOGY-ASSEMBLAGES-04: whole published weight groups, not cherry-picked objects.

Source: Martinez Chico & Gonzalez Garcia (2018), Florentia Iliberritana 29,
pp. 383, 386-387. First assemblage described in paper; the other four are
secondary bibliographic citations from earlier studies. No access to FULL3406.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path

SOURCE = "https://revistaseug.ugr.es/index.php/florentia/article/download/8829/7412/25457"
RATIOS = (1, 2, 2.5, 3, 4, 5, 8, 10, 20, 40, 60, 100)
ASSEMBLAGES = {
 "VILLANUEVA_DE_LA_JARA": {
   "masses": (21.,41.5,62.7,106.5,214.3),
   "status": "DIRECT_DESCRIPTION_2018",
   "context": "SURFACE_FIND_WITHOUT_CONTROLLED_EXCAVATION"},
 "EL_CIGARRALEJO_TOMB_200": {
   "masses": (1.98,3.38,5.01,7.4,15.83,20.48,41.46,81.65,125.,208.45),
   "status": "SECONDARY_CITATION_2018", "context": "TOMB_200"},
 "CABECICO_DEL_TESORO_TOMB_117": {
   "masses": (2.04,4.,4.48,6.05,8.64,19.5,20.15,36.25,39.44,82.87,123.93,197.5,209.6),
   "status": "SECONDARY_CITATION_2018", "context": "TOMB_117"},
 "ORLEYL_TOMB_11": {
   "masses": (21.71,22.92,92.62,132.88,43.7),
   "status": "SECONDARY_CITATION_2018", "context": "TOMB_11",
   "supports": ("LEAD","LEAD","LEAD","LEAD","BRONZE")},
 "COVALTA_BUILDING_27": {
   "masses": (42.2,81.8,122.25,209.5),
   "status": "SECONDARY_CITATION_2018", "context": "BUILDING_27"},
}

def audit(unit_g: float = 2.1, tolerance_percent: float = 5.) -> dict:
    if unit_g <= 0 or not 0 <= tolerance_percent <= 100:
        raise ValueError("INVALID_UNIT_OR_TOLERANCE")
    groups = []
    for name, record in ASSEMBLAGES.items():
        rows = []
        for i, mass in enumerate(record["masses"]):
            error, ratio = min(
                ((100 * abs(mass - unit_g * ratio) / mass, ratio) for ratio in RATIOS),
                key=lambda pair: (pair[0], pair[1]))
            rows.append({
                "index": i + 1, "mass_g": mass,
                "closest_published_series_ratio": ratio,
                "expected_g": round(unit_g * ratio, 4),
                "absolute_deviation_percent": round(error, 4),
                "within_tolerance": error <= tolerance_percent,
                "support": record.get("supports", ("NOT_SPECIFIED",) * len(record["masses"]))[i],
            })
        groups.append({
            "group": name, "source_status": record["status"],
            "archaeological_context": record["context"],
            "n_objects": len(rows),
            "within_tolerance": sum(r["within_tolerance"] for r in rows),
            "items": rows, "independent_sign_readings_available": False,
        })
    return {
        "experiment": "METROLOGY_ASSEMBLAGES_04",
        "source": SOURCE, "published_mass_count": sum(g["n_objects"] for g in groups),
        "assemblage_count": len(groups),
        "directly_described_2018": sum(g["n_objects"] for g in groups if g["source_status"] == "DIRECT_DESCRIPTION_2018"),
        "secondary_citations_2018": sum(g["n_objects"] for g in groups if g["source_status"] == "SECONDARY_CITATION_2018"),
        "published_series_ratios": RATIOS, "assumed_unit_g": unit_g,
        "descriptive_tolerance_percent": tolerance_percent,
        "count_within_tolerance": sum(g["within_tolerance"] for g in groups),
        "groups": groups,
        "numeric_fit_not_semantic_gold": True,
        "nonblind_literature_data": True,
        "new_independent_measurements": 0,
        "a_o_ki_testable_with_mass_only": False,
        "full3406_accessed": False, "official_metrics_changed": False,
        "caveat": "Mass-only closeness to an already-published 2.1-g family is not an independent test of an a/o/ki epigraphic model; no marks or confirmed denominations for these 37 objects."
    }

def main(argv=None):
    p = argparse.ArgumentParser()
    p.add_argument("--unit-g", type=float, default=2.1)
    p.add_argument("--tolerance-percent", type=float, default=5.)
    p.add_argument("--json", type=Path)
    args = p.parse_args(argv)
    content = json.dumps(audit(args.unit_g, args.tolerance_percent), ensure_ascii=False, indent=2) + "\n"
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(content, encoding="utf-8")
    else:
        print(content, end="")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())

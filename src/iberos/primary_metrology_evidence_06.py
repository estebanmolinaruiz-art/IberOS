"""Primary-metrology evidence gate: never convert published decimals into certified uncertainty."""
from __future__ import annotations
from dataclasses import dataclass, asdict
import json
from pathlib import Path
import argparse


@dataclass(frozen=True)
class Specimen:
    id: str
    object: str
    published_mass_g: float
    museum_inventory: str | None
    publication: str
    figure: str | None
    author_examined_object: bool
    inscription_reading_in_publication: str | None
    independent_mark_verification: bool
    balance_model: str | None = None
    resolution_g: float | None = None
    measurement_uncertainty_g: float | None = None
    calibration_report: str | None = None
    conservation_note: str | None = None


SPECIMENS = (
    Specimen(
        id="PUIG_MISERICORDIA_2309",
        object="Stone weight Puig de la Misericordia (Vinaros)",
        published_mass_g=41.29,
        museum_inventory="2309 (2013 article museum file; current id pending)",
        publication="Ferrer i Jane 2013, Quad. Preh. Arq. Cast. 31, pp.137-148",
        figure="Fig. 1, published photograph with scale",
        author_examined_object=True,
        inscription_reading_in_publication="o (H-shaped sign; northeastern Iberian)",
        independent_mark_verification=False,
        conservation_note="Surface archaeological context UE 200, dated broadly second half 2nd c BCE; uncertainty not given.",
    ),
    Specimen(
        id="PUIG_CASTELLAR_423_78",
        object="Inscribed stone weight Puig Castellar (Santa Coloma de Gramenet)",
        published_mass_g=423.78,
        museum_inventory=None,
        publication="Ferrer i Jane 2013, Quad. Preh. Arq. Cast. 31, p.145 n.4",
        figure="Fig. 6 line drawing (not an independently checked mark photograph)",
        author_examined_object=True,
        inscription_reading_in_publication="Variant reading disputed; one small sign partly obscured",
        independent_mark_verification=False,
        conservation_note="Iron ring likely lost material; 423.78 g is a reported reweigh with precision scale.",
    ),
)


def audit(specimens=SPECIMENS) -> dict:
    items = []
    for s in specimens:
        if s.published_mass_g <= 0:
            raise ValueError("INVALID_MASS")
        if s.measurement_uncertainty_g is not None and s.measurement_uncertainty_g <= 0:
            raise ValueError("INVALID_UNCERTAINTY")
        data = asdict(s)
        data["verified_metrology"] = bool(
            s.balance_model and s.resolution_g and
            s.measurement_uncertainty_g and s.calibration_report
        )
        data["eligible_for_blind_semantic_test"] = False
        data["reading_credibility"] = (
            "INDEPENDENTLY_REVIEWED" if s.independent_mark_verification
            else "AUTHOR_PUBLICATION_ONLY"
        )
        items.append(data)
    return {
        "experiment":"PRIMARY_METROLOGY_EVIDENCE_06",
        "publication_date":"2026-11-11",
        "items":items,
        "published_mass_count":len(items),
        "instrumental_uncertainty_verified":sum(x["verified_metrology"] for x in items),
        "independent_mark_readings":sum(x["independent_mark_verification"] for x in items),
        "test_samples_qualified":sum(x["eligible_for_blind_semantic_test"] for x in items),
        "historical_full3406_accessed":False,
        "metrics_modified":False,
        "note":"A publication with two decimal places is NOT evidence of measurement uncertainty 0.01 g. Author autopsy and a figure are not independent re-reading.",
    }


def main(argv=None):
    p=argparse.ArgumentParser()
    p.add_argument("--json",type=Path)
    args=p.parse_args(argv)
    result=json.dumps(audit(),ensure_ascii=False,indent=2)+"\n"
    if args.json:
        args.json.parent.mkdir(parents=True,exist_ok=True)
        args.json.write_text(result,encoding="utf-8")
    else:
        print(result,end="")
    return 0

if __name__=="__main__":
    raise SystemExit(main())

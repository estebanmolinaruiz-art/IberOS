"""SEMANTIC-EKIAR-01 corrected: conservative Iberian formula recognition.

This is a retrospective bibliography check, NOT a novel translation
or a blind prediction. Distinguish archaeological support, literal
edition, normalisation and conjectural morpheme boundaries.
"""
from __future__ import annotations
import argparse
import json
import re
from pathlib import Path

DOCUMENTED_CASES = (
    {
        "id": "MLH_E_7_1", "kind": "MOSAIC",
        "transcription": "likinete ekiar usekeŕteku",
        "name": "likine",
        "known_source": "Lujan 2010, Palaeohispanica 10:289-301",
        "note": "usekeŕteku: geographical association, NOT a certain literal translation",
        "reading_disputed": False,
        "morphology": "NP-te ekiar",
    },
    {
        "id": "MLH_C_12_2", "kind": "GREY_IBERIAN_CERAMIC",
        "transcription": "bilo[s]aŕkerdegiar",
        "name": "bilo[s]aŕker",
        "known_source": "Moncunill 2007; Francès, Velaza & Moncunill 2008",
        "note": "Ca n'Oliver, Cerdanyola. Autopsy supports -de + egiar; [s] editorially restored",
        "reading_disputed": True,
        "morphology": "NP-de egiar, not asserted identical to NP-te ekiar",
    },
    {
        "id": "MLH_A_33_2", "kind": "COIN",
        "transcription": "aŕsbikisteekiar / arseetar",
        "name": "aŕsbikis",
        "known_source": "BDHesp Numismatica, Mon.33.2; earlier MLH arsakiskuekiar",
        "note": "The NP/title reading and segmentation conflict across editions",
        "reading_disputed": True,
        "morphology": "possible NP-te ekiar; coin legends may indicate magistrate",
    },
    {
        "id": "MLH_F_13_3_6", "kind": "PAINTED_CERAMIC",
        "transcription": "ebiŕteekiar",
        "name": "ebiŕ",
        "known_source": "Moncunill 2007, Lexic d'inscripcions iberiques",
        "note": "F.13.3 line 6, not equivalent to all lines of F.13.3",
        "reading_disputed": False,
        "morphology": "NP-te ekiar",
    },
)

def normalize(value: str) -> str:
    if not isinstance(value, str):
        return ""
    txt = value.casefold().replace("ŕ", "r").replace("ś", "s").replace("ḿ", "m")
    # Bracketed restitution retained as a separate uncertainty flag.
    return txt.replace("[", "").replace("]", "").replace(" ", "").replace("·", "").replace(".", "")

def interpret(case: dict) -> dict:
    txt = normalize(case["transcription"].split("/")[0])
    name = normalize(case["name"])
    # Only literal witnessed morphotypes; do not erase paleographic
    # distinction between the readings /teekiar/ and /degiar/.
    patterns = (name + "teekiar", name + "tekiar",
                name + "degiar", name + "deg(i)ar")
    matched = any(token in txt for token in patterns)
    return {
        "id": case["id"], "context": case["kind"],
        "transcription": case["transcription"],
        "formula_attested": matched,
        "morphotype": case.get("morphology"),
        "person_candidate": case["name"] if matched else None,
        "role_predicted": "PERSON_ASSOCIATED_WITH_PRODUCTION_OR_COMMISSION" if matched else None,
        "semantic_rendering": (
            f"Realización u obra relacionada con {case['name']} "
            "(ejecutor, promotor o titular: NO distinguibles)" if matched else None
        ),
        "reading_disputed": case.get("reading_disputed", True),
        "translation_status": "PREVIOUSLY_PUBLISHED_CONTEXTUAL_HYPOTHESIS",
        "source": case["known_source"], "limitations": case["note"],
    }

def evaluate(cases=DOCUMENTED_CASES) -> dict:
    rows = [interpret(c) for c in cases]
    return {
        "experiment": "SEMANTIC_EKIAR_FORMULA_01_CORRECTED",
        "scope": "NP-te ekiar and independently documented variants (-de egiar)",
        "n_documented_cases": len(rows),
        "contexts": sorted({x["context"] for x in rows}),
        "formula_matches": sum(x["formula_attested"] for x in rows),
        "disputed_readings": sum(x["reading_disputed"] for x in rows),
        "outputs": rows,
        "proposed_function": "PRODUCTION_OR_COMMISSION_ATTRIBUTION",
        "verb_versus_noun_unresolved": True,
        "producer_versus_sponsor_unresolved": True,
        "reading_variants_excluded_from_gold": True,
        "novel_lexical_decipherments": 0,
        "independently_held_out_evaluations": 0,
        "novel_blind_accuracy": None,
        "full3406_accessed": False,
        "official_metrics_modified": False,
    }

def main(argv=None):
    parser=argparse.ArgumentParser()
    parser.add_argument("--json",type=Path)
    args=parser.parse_args(argv)
    out=json.dumps(evaluate(),ensure_ascii=False,indent=2)+"\n"
    if args.json:
        args.json.parent.mkdir(parents=True,exist_ok=True)
        args.json.write_text(out,encoding="utf-8")
    else:
        print(out,end="")
    return 0

if __name__=="__main__":
    raise SystemExit(main())

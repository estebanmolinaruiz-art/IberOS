"""SEMANTIC-EKIAR-01: restricted, retrospective Iberian formula interpretation.

Not an original decipherment. Published reading NP-te ekiar suggests an
act of making/commissioning. Treat agent-vs-commissioner as unresolved.
All cases were known in advance; none is a blind or novel discovery.
"""
from __future__ import annotations
import json
import re
import argparse
from pathlib import Path

DOCUMENTED_CASES = (
    {"id": "MLH_E_7_1", "kind": "MOSAIC", "transcription": "likinete ekiar usekerdeku",
     "name": "likine", "known_source": "Lujan 2010; mosaic of Caminreal",
     "note": "usekerdeku has a proposed Osicerda association; not independently translated"},
    {"id": "MLH_C_12_2", "kind": "SILVER_VESSEL", "transcription": "bilosarkertekiar",
     "name": "bilosarker", "known_source": "Orduña 2010; Quintanilla 2005",
     "note": "orthography normalized from bilo[s]árkertekiar"},
    {"id": "MLH_A_33_2", "kind": "COIN", "transcription": "arsakisteekiar",
     "name": "arsakis", "known_source": "Quintanilla 2005; divergent monetary edition",
     "note": "coin legends have alternative editions; this reading is contested"},
    {"id": "MLH_F_13_3", "kind": "PAINTED_CERAMIC", "transcription": "ebirteekiar",
     "name": "ebir", "known_source": "Lowe 2014 citing Llíria vessel",
     "note": "published as a maker/commission formula, not new to IberOS"},
)

def normalize(s: str) -> str:
    replacements = {"á":"a","à":"a","é":"e","í":"i","ó":"o",
                    "ú":"u","ŕ":"r","ś":"s","ḿ":"m"}
    return "".join(replacements.get(c,c) for c in s.lower())

def interpret(case: dict) -> dict:
    txt = normalize(case["transcription"]).replace(" ", "").replace(".", "")
    name = normalize(case["name"])
    markers = (name + "teekiar", name + "tekiar")
    matched = any(x in txt for x in markers)
    return {
        "id": case["id"], "context": case["kind"],
        "transcription": case["transcription"], "formula_attested": matched,
        "person_candidate": case["name"] if matched else None,
        "role_predicted": "PERSON_ASSOCIATED_WITH_PRODUCTION_OR_COMMISSION" if matched else None,
        "semantic_rendering": (f"Obra/realización asociada a {case['name']} "
                               "(autor o comitente sin distinguir)" if matched else None),
        "translation_status": "PUBLISHED_CONTEXTUAL_HYPOTHESIS_NOT_NEW",
        "source": case["known_source"], "limitations": case["note"],
    }

def evaluate(cases=DOCUMENTED_CASES) -> dict:
    result=[interpret(c) for c in cases]
    return {
        "experiment":"SEMANTIC_EKIAR_FORMULA_01",
        "scope":"NP-te ekiar, cross-support descriptive transfer",
        "n_documented_cases":len(result),
        "contexts":sorted({x["context"] for x in result}),
        "formula_matches":sum(x["formula_attested"] for x in result),
        "outputs":result,
        "proposed_function":"PRODUCTION_OR_COMMISSION_ATTRIBUTION",
        "verb_versus_noun_unresolved":True,
        "producer_versus_sponsor_unresolved":True,
        "reading_variants_excluded_from_gold":True,
        "novel_lexical_decipherments":0,
        "independently_held_out_evaluations":0,
        "novel_blind_accuracy":None,
        "full3406_accessed":False,
        "official_metrics_modified":False,
    }

def main(argv=None):
    p=argparse.ArgumentParser()
    p.add_argument("--json", type=Path)
    a=p.parse_args(argv)
    out=json.dumps(evaluate(),ensure_ascii=False,indent=2)+"\n"
    if a.json:
        a.json.parent.mkdir(parents=True,exist_ok=True)
        a.json.write_text(out,encoding="utf-8")
    else:
        print(out,end="")
    return 0

if __name__=="__main__":
    raise SystemExit(main())

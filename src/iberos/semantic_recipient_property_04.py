"""SEMANTIC-RECIPIENT-PROPERTY-04: falsifiable role predictions on folded leads.

The three archaeological references were interpreted in prior literature,
so they are DEVELOPMENT/COUNTEREXAMPLE, NEVER external blind accuracy.
No translation promotion and no FULL3406 access.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path

EVIDENCE = (
    {
        "id":"GI.10.11", "site":"Emporion",
        "external_sequence":"katulatien",
        "folded_or_rolled":True,
        "short_external_label":True,
        "long_internal_message":True,
        "independent_text_reuse":False,
        "property_marker_nai":False,
        "external_editor_interpretation":"RECIPIENT_PROPOSED",
        "source":"Sanmartí-Grego 1988; etnografía Veleia 40 (2023)",
    },
    {
        "id":"A.04.01a", "site":"La Serreta",
        "external_sequence":"śakariskerarnai",
        "folded_or_rolled":True,
        "short_external_label":True,
        "long_internal_message":True,
        "independent_text_reuse":False,
        "property_marker_nai":True,
        "external_editor_interpretation":"RECIPIENT_PROPOSED",
        "source":"Veleia 40 (2023), recipient formula discussion",
    },
    {
        "id":"ILLET_BANYETS_2018_PUBL2024", "site":"Illeta dels Banyets",
        "external_sequence":"ka+belauŕ / nai",
        "folded_or_rolled":True,
        "short_external_label":False,
        "long_internal_message":False,
        "independent_text_reuse":True,
        "property_marker_nai":True,
        "external_editor_interpretation":"REUSED_PROPERTY_OR_GOODS_LABEL_PROPOSED",
        "source":"Ferrer et al., Palaeohispanica 24 (2024), DOI 10.36707/palaeohispanica.v24i1.629",
    },
)

def predict(record: dict) -> dict:
    """Out-of-sample rule can be frozen; no lexical translation is asserted."""
    if record.get("independent_text_reuse") is True:
        decision="ABSTAIN_RECIPIENT_VS_PROPERTY"
        comment="Multiple independent inscriptions/reuse, property or goods label possible"
    elif (record.get("folded_or_rolled") is True
          and record.get("short_external_label") is True
          and record.get("long_internal_message") is True):
        decision="RECIPIENT_HYPOTHESIS"
        comment="Physical epistolary format; ownership/genitive alternative remains"
    else:
        decision="ABSTAIN_INSUFFICIENT_PHYSICAL_CONTEXT"
        comment="External position or -nai alone is not sufficient for recipient role"
    return {
        "id":record.get("id"),
        "decision":decision,
        "alternative_role":"OWNER_OR_GOODS_LABEL",
        "reading":record.get("external_sequence"),
        "explanation":comment,
        "new_lexical_translation":False,
        "role_independently_certified":False,
    }

def audit():
    rows=[predict(r) for r in EVIDENCE]
    return {
        "experiment":"SEMANTIC_RECIPIENT_PROPERTY_04",
        "status":"RETROSPECTIVE_FALSIFICATION_AND_FUTURE_RULE",
        "calibration_cases":len(rows),
        "reported_cases":rows,
        "future_prediction":"On a previously unexposed folded commercial lead with a single external NP-like text and long interior message, predict addressee rather than workshop maker; if multiple reused texts, abstain and preserve property-label rival.",
        "positive_published_cases":sum(x["decision"]=="RECIPIENT_HYPOTHESIS" for x in rows),
        "abstention_published_cases":sum(x["decision"].startswith("ABSTAIN") for x in rows),
        "new_blind_cases":0,
        "external_two_role_gold":0,
        "property_vs_recipient_lexically_disambiguated":False,
        "official_metrics_modified":False,
        "full3406_accessed":False,
    }

def main(argv=None):
    p=argparse.ArgumentParser()
    p.add_argument("--json",type=Path)
    a=p.parse_args(argv)
    output=json.dumps(audit(),ensure_ascii=False,indent=2)+"\n"
    if a.json:
        a.json.parent.mkdir(parents=True,exist_ok=True)
        a.json.write_text(output,encoding="utf-8")
    else:
        print(output,end="")
    return 0

if __name__=="__main__":
    raise SystemExit(main())

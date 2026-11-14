"""SEMANTIC-EKIAR-CHALLENGE-02: independent of four seed texts, NOT blind.

Cases were visible in the published Moncunill index before the challenge.
The test checks generalisation *within known literature*, not new translation.
Some fragmentary names cannot be assigned a complete human identity.
"""
from __future__ import annotations
import argparse, json
from pathlib import Path
from .semantic_ekiar_01 import normalize

SOURCES = (
    "Moncunill 2007, Lexic d'inscripcions iberiques, p.156-157",
    "Frances/Velaza/Moncunill, Un nuevo calato inscrito de Ca n'Oliver",
)
CHALLENGES = (
    {
        "id": "MLH_F_11_28", "attestation": "iltubokontekiar",
        "support": "INSCRIBED_OBJECT_EDITION_PENDING",
        "agent_candidate": "iltubokon",
        "target_type": "NP_TE_EKIAR",
        "evidence_source": SOURCES[0],
        "status": "PUBLISHED_HISTORICAL_IN_INDEX",
    },
    {
        "id": "MLH_F_17_7", "attestation": "]balkarte ekiar",
        "support": "INSCRIBED_OBJECT_EDITION_PENDING",
        "agent_candidate": "]balkar",
        "target_type": "FRAGMENTARY_NP_TE_EKIAR",
        "evidence_source": SOURCES[0],
        "status": "PUBLISHED_HISTORICAL_FRAGMENT",
    },
    {
        "id": "CA_N_OLIVER_CALATHUS", "attestation": "adintaŕekiaḿi",
        "support": "IBERIAN_CALATHUS",
        "agent_candidate": "adintaŕ",
        "target_type": "RELATED_EKIA_VARIANT_WITH_MI",
        "evidence_source": SOURCES[1],
        "status": "PUBLISHED_BEFORE_TEST",
    },
    {
        "id": "NEGATIVE_CONTROL_ARTIFICIAL_1", "attestation": "likine salir",
        "support": "SYNTHETIC_NEGATIVE_NOT_AN_ARTIFACT",
        "agent_candidate": "likine",
        "target_type": "NEGATIVE_NO_EKIAR",
        "evidence_source": "synthetic negative created for software unit test",
        "status": "SYNTHETIC",
    },
)

def infer(case: dict) -> dict:
    txt=normalize(case["attestation"])
    name=normalize(case["agent_candidate"])
    # Recognise only fully attested NP + suffix + ekiar / egiar.
    # Broken left edge ]balkar still denotes a partial *sequence*, not a
    # fully known name and therefore no external person role.
    strict=any((name+ending) in txt for ending in ("teekiar", "tekiar", "degiar"))
    complete=strict and not case["attestation"].startswith("]")
    variant=("ekia" in txt and not strict and "mi" in txt)
    return {
        "id": case["id"],
        "source":case["evidence_source"],
        "attestation":case["attestation"],
        "object_support":case["support"],
        "source_previously_public":case["status"]!="SYNTHETIC",
        "formula_like":strict,
        "full_person_name_certified":complete,
        "uncertain_related_variant":variant,
        "decision": "CONTEXTUAL_ASSOCIATION_ONLY" if complete else "ABSTAIN",
        "gloss":f"realización vinculada a {case['agent_candidate']}" if complete else None,
        "agent_vs_sponsor_resolved":False,
        "external_two_role_gold":False,
        "novel_decipherment":False,
    }

def audit() -> dict:
    r=[infer(c) for c in CHALLENGES]
    return {
        "experiment":"SEMANTIC_EKIAR_CHALLENGE_02",
        "status":"RETROSPECTIVE_LITERATURE_STRESS_TEST",
        "training_cases":4,
        "additional_published_cases":3,
        "synthetic_negative_controls":1,
        "formula_like_count":sum(x["formula_like"] for x in r),
        "contextual_interpretations":sum(x["decision"]=="CONTEXTUAL_ASSOCIATION_ONLY" for x in r),
        "abstentions":sum(x["decision"]=="ABSTAIN" for x in r),
        "predictions":r,
        "independent_external_roles_confirmed":0,
        "new_blind_predictions_confirmed":0,
        "claim_of_new_decipherment":False,
        "full3406_accessed":False,
        "official_metrics_modified":False,
        "conclusion":"Published transfer: one complete author/commission association only; incomplete and morphological alternatives require abstention.",
    }

def main(argv=None):
    p=argparse.ArgumentParser();p.add_argument("--json",type=Path);a=p.parse_args(argv)
    s=json.dumps(audit(),ensure_ascii=False,indent=2)+"\n"
    if a.json:
        a.json.parent.mkdir(parents=True,exist_ok=True);a.json.write_text(s,encoding="utf-8")
    else:print(s,end="")
    return 0

if __name__=="__main__":
    raise SystemExit(main())

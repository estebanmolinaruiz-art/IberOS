"""SEMANTIC-DUALROLE-K54-03: compare Latin role evidence to Iberian hypotheses.

Two mortars have co-occurring Latin/Iberian stamps. That independently
certifies role distinctions in Latin, NOT their complete Iberian translation.
All inscriptions were previously published. No genuine blind gold.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path

LATIN = "FL ATILI / L S"
IBERIAN = "bilakeaiunatin / en abiner"

OBJECTS = (
    {"physical_context": "LA_CARIDAD_CAMINREAL", "paired_stamps": True,
     "latin": LATIN, "iberian": IBERIAN,
     "published": True, "new_to_corpus_independence_certified": False},
    {"physical_context": "LA_CORONA_FUENTES_DE_EBRO", "paired_stamps": True,
     "latin": LATIN, "iberian": IBERIAN,
     "published": True, "new_to_corpus_independence_certified": False},
)

EXTERNAL_ONOMASTIC_PARALLEL = {
    "reference": "IRC V 11, Isona; Latin graffito on terra sigillata",
    "latin_text": "Fulvius Abiner(icus)",
    "attests_abiner_as_personal_name_in_latin_context": True,
    "is_same_physical_object_as_k54": False,
    "same_language_as_k54": False,
    "proves_iberian_abiner_means_personal_name": False,
    "scholarly_discussion": "Moncunill & Velaza, Abiner, Abinericus (2011)",
}

LATIN_ROLE_GOLD = (
    {"latin_entity": "Flaccus (Fl.)", "externally_attested_role": "servus_of_Lucius_Atilius"},
    {"latin_entity": "Lucius Atilius (Atili L.)", "externally_attested_role": "master_in_genitive"},
)

RIVALS = (
    {
        "model": "H1_ABINER_SERVUS",
        "iberian_role_alignments": {
            "bilake": "Flaccus_worker_slave",
            "aiunatin": "Lucius_Atilius_master",
            "abiner": "servus_title",
        },
        "assumes_identical_role_labels": True,
        "status": "DISPUTED_SCHOLARLY_HYPOTHESIS",
    },
    {
        "model": "H2_ABINER_PERSONAL_NAME",
        "iberian_role_alignments": {
            "bilake": "Flaccus_worker_slave",
            "aiunatin": "Lucius_Atilius_master",
            "abiner": "personal_name_or_cognomen",
        },
        "assumes_identical_role_labels": False,
        "status": "DISPUTED_SCHOLARLY_HYPOTHESIS",
    },
    {
        "model": "H3_PRAGMATIC_NOT_LITERAL_EQUIVALENCE",
        "iberian_role_alignments": {},
        "assumes_identical_role_labels": False,
        "status": "CAUTIOUS_NULL_INTERPRETATION",
    },
)

def audit() -> dict:
    for obj in OBJECTS:
        if obj["latin"] != LATIN or obj["iberian"] != IBERIAN:
            raise AssertionError("MISMATCH_PUBLISHED_STAMP_TYPE")
    return {
        "experiment": "SEMANTIC_DUALROLE_K54_03",
        "date": "2026-11-14",
        "archaeological_support": "MORTAR_CO_STAMPED_LATIN_IBERIAN",
        "published_physical_objects": len(OBJECTS),
        "independent_formula_types": 1,
        "objects": list(OBJECTS),
        "latin_text_normalized": LATIN,
        "latin_externally_supported_roles": list(LATIN_ROLE_GOLD),
        "latin_role_count": len(LATIN_ROLE_GOLD),
        "iberian_text_normalized": IBERIAN,
        "rival_mapping_hypotheses": list(RIVALS),
        "independent_onomastic_parallel": dict(EXTERNAL_ONOMASTIC_PARALLEL),
        "external_context_suggests_abiner_personal_name": True,
        "lexical_disambiguation_complete": False,
        "hard_gold_iberian_roles": 0,
        "iberian_roles_external_confirmed": False,
        "abiner_means_servus_confirmed": False,
        "bilake_flaccus_identification_confirmed": False,
        "aiunatin_lucius_atilius_identification_confirmed": False,
        "roles_from_latin_predictable": True,
        "roles_from_iberian_independently_scored": False,
        "historical_bilingual_training_reuse": True,
        "genuine_new_blind_result": False,
        "new_decipherment_confirmed": False,
        "full3406_accessed": False,
        "official_metrics_modified": False,
        "next_discriminating_test": (
            "Find a new, genuinely independent object with an Iberian "
            "role formula and separately documented Latin/slavery/workshop "
            "roles; register the Iberian role mapping before revealing Latin."
        ),
    }

def main(argv=None):
    p=argparse.ArgumentParser()
    p.add_argument("--json",type=Path)
    a=p.parse_args(argv)
    out=json.dumps(audit(),ensure_ascii=False,indent=2)+"\n"
    if a.json:
        a.json.parent.mkdir(parents=True,exist_ok=True)
        a.json.write_text(out,encoding="utf-8")
    else:print(out,end="")
    return 0

if __name__=="__main__":
    raise SystemExit(main())

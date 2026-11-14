"""Read-only evidence audit for Mas de Moreno pottery workshop.

This module tracks archaeological-context corroboration, NOT Iberian decipherment.
No automatic promotion to scientific core, no new HOLD and no role inference.
"""
from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data/review/mas_moreno_context_evidence_v1.json"
SCHEMA = "IberOS-MASMORENO-CTX/1.0"


def audit(document: dict) -> dict:
    if not isinstance(document, dict) or document.get("schema") != SCHEMA:
        raise ValueError("Unknown or missing schema")
    if document.get("cost_eur") != 0:
        raise ValueError("Only zero-cost research is authorized")
    sources = document["sources"]
    source_ids = [x["id"] for x in sources]
    if len(set(source_ids)) != len(source_ids) or not source_ids:
        raise ValueError("Invalid/duplicate sources")
    for s in sources:
        parsed = urlsplit(s["url"])
        if parsed.scheme != "https" or not parsed.netloc:
            raise ValueError("Source must use HTTPS")
    families = document["stamp_families"]
    family_ids = [x["id"] for x in families]
    if len(set(family_ids)) != len(family_ids) or not family_ids:
        raise ValueError("Invalid/duplicate stamp families")
    for family in families:
        if family["script"] not in ("IBERIAN", "LATIN"):
            raise ValueError("Unknown script")
        if not family["editorial_forms"] or family["photo_adjudicated"] is not False:
            raise ValueError("Editorial transcriptions cannot masquerade as photo verification")
        if family["physical_object_id"] is not None:
            raise ValueError("No verified individual object inventory in these family records")
        if not set(family["source_ids"]).issubset(source_ids):
            raise ValueError("Unresolved family source")
    associations = document["associations"]
    for a in associations:
        if not set(a["family_ids"]).issubset(family_ids):
            raise ValueError("Unknown family in association")
        if not set(a["source_ids"]).issubset(source_ids):
            raise ValueError("Unknown association source")
        if a["independent_archaeological_context"] is not True:
            raise ValueError("Context not independently published")
        if a["roles_of_named_people_known"] is not False:
            raise ValueError("Context does not establish individual maker/owner roles")
    unit = [a for a in associations if a["id"] == "US13358-COOCCURRENCE"]
    if len(unit) != 1 or set(unit[0]["family_ids"]) != {"ILURATIN", "ACINI"}:
        raise ValueError("Published US13358 pairing is required")
    if unit[0]["object_relation"] != "TWO_DISTINCT_STAMPS_NOT_SAME_VESSEL":
        raise ValueError("Cannot conflate different stamps with a bilingual single object")
    for count in document["published_counts"]:
        if count["iberean_stamps"] + count["latin_stamps"] != count["total_stamps"]:
            raise ValueError("Published count mismatch")
        if not set(count["source_ids"]).issubset(source_ids):
            raise ValueError("Unknown count source")
    if any(x["expected"] is not False for x in document["negative_controls"]):
        raise ValueError("A forbidden causal conclusion was promoted")
    by_script = Counter(x["script"] for x in families)
    return {
        "schema": "IberOS-MASMORENO-CTX-AUDIT/1.0",
        "evidence_class": "ARCHAEOLOGICALLY_DOCUMENTED_CONTEXT",
        "historical_retrospective_only": True,
        "stamp_families_documented_editorially": len(families),
        "families_by_script": dict(by_script),
        "published_stratigraphic_associations": len(associations),
        "us_13358_pair": ["ILURATIN", "ACINI"],
        "published_stamp_impressions_until_2015": document["published_counts"][0]["total_stamps"],
        "physical_objects_individually_audited": 0,
        "independent_photo_readings": 0,
        "verified_roles_of_named_people": 0,
        "bilingual_translation_equivalences": 0,
        "prospective_semantic_trials": 0,
        "translation_validated": False,
        "automatic_core_promotion": False,
        "next_test": "Obtain per-object inventory and two independent image readings; then test stamp-place association against matched non-workshop controls.",
    }


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--input", type=Path, default=DATA)
    p.add_argument("--output", type=Path)
    opts = p.parse_args(argv)
    result = audit(json.loads(opts.input.read_text(encoding="utf-8")))
    encoded = json.dumps(result, indent=2, ensure_ascii=False) + "\n"
    if opts.output:
        if opts.input.resolve() == opts.output.resolve():
            raise ValueError("Cannot overwrite source")
        opts.output.write_text(encoded, encoding="utf-8")
    else:
        print(encoded, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

"""SCI-PRED-02: seal role predictions without seeing independent role labels.

A locked H-MAKER rule, not a decipherment or trained semantic model.
The evaluator must separately attest physical independence and unblind gold
*after* the sha256-committed prediction is fixed in an immutable Git commit.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[2]
PROTOCOL_PATH = ROOT / "research/protocols/SCI_PRED_02_FUTURE_ROLE_RULE_20261112.json"
VALID_CONTEXTS = {"BUILDING", "MANUFACTURE"}
VALID_READINGS = {"D2", "D3"}
CASE_FIELDS = {
    "blind_id", "physical_id", "reading_source_url", "context_type",
    "reading_level", "participants", "script", "independence_status",
}
PERSON_FIELDS = {"person_id", "name_form", "name_status"}
GOLD_FIELDS = {
    "gold", "label", "role", "true_role", "maker", "producer",
    "commissioner", "owner", "slave", "latin", "translation", "outcome",
    "known_result",
}


def _clean_fields(data: dict, fields: set[str], where: str):
    if not isinstance(data, dict):
        raise ValueError(f"{where}: expected object")
    unknown = set(data) - fields
    if unknown:
        raise ValueError(f"{where}: extra or gold-bearing fields forbidden: {sorted(unknown)}")


def _nonempty(value) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _sha(obj: dict) -> str:
    return hashlib.sha256(json.dumps(obj, sort_keys=True, ensure_ascii=False,
                        separators=(",", ":")).encode("utf-8")).hexdigest()


def seal(case: dict, protocol: dict) -> dict:
    if protocol.get("protocol") != "SCI-PRED-02/1.0":
        raise ValueError("Unknown protocol")
    _clean_fields(case, CASE_FIELDS, "case")
    for key in CASE_FIELDS - {"participants"}:
        if not _nonempty(case.get(key)):
            raise ValueError(f"Missing {key}")
    parsed = urlsplit(case["reading_source_url"])
    if parsed.scheme != "https" or not parsed.netloc or parsed.username or parsed.password:
        raise ValueError("Source must use HTTPS")
    if case["script"] != "IBERIAN":
        raise ValueError("Out-of-scope script")
    if case["independence_status"] != "EXTERNALLY_ATTESTED":
        raise ValueError("Physical and documentary independence not established")
    if case["context_type"] not in VALID_CONTEXTS:
        raise ValueError("Unsupported context")
    if case["reading_level"] not in VALID_READINGS:
        raise ValueError("D1 editorial sources cannot establish a blinded case")
    people = case.get("participants")
    if not isinstance(people, list) or len(people) != 2:
        raise ValueError("Exactly two independent persons required")
    ids, marked = set(), []
    for person in people:
        _clean_fields(person, PERSON_FIELDS, "person")
        if not all(_nonempty(person.get(k)) for k in PERSON_FIELDS):
            raise ValueError("Incomplete person span")
        if person["person_id"] in ids:
            raise ValueError("Duplicate person id")
        ids.add(person["person_id"])
        if person["name_status"] != "INDEPENDENTLY_IDENTIFIED":
            raise ValueError("Person identities not independently identified")
        if person["name_form"].strip().lower().endswith("-te"):
            marked.append(person["person_id"])
    # If the morphology does not pick a unique person, do not guess.
    target = marked[0] if len(marked) == 1 else None
    signal = "ONE_DOCUMENTED_TE" if target else "ABSTAIN_AMBIGUOUS_OR_ABSENT_TE"
    statement = {
        "protocol_sha256": _sha(protocol), "blind_id": case["blind_id"],
        "physical_id": case["physical_id"],
        "participant_ids": sorted(ids),
        "input_sha256": _sha(case),
        "marked_person_id": target, "signal": signal,
        "h_maker_prediction": {"person_id": target, "role": "PRODUCER"} if target else None,
        "h_commissioner_prediction": {"person_id": target, "role": "COMMISSIONER"} if target else None,
        "h_null_prediction": "ABSTAIN",
    }
    return {
        "schema": "IberOS-SCI-PRED-02-Sealed-Prediction/1.0",
        "statement": statement,
        "statement_sha256": _sha(statement),
        "semantic_gold_provided_to_predictor": False,
        "gold_independently_verified": False,
        "date_priority_independently_verified": False,
        "evaluation": "AWAITING_EXTERNAL_ROLE_UNBLINDING",
        "translation_validated": False,
        "automatic_core_promotion": False,
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--case", type=Path, required=True)
    parser.add_argument("--protocol", type=Path, default=PROTOCOL_PATH)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args(argv)
    case = json.loads(args.case.read_text(encoding="utf-8"))
    protocol = json.loads(args.protocol.read_text(encoding="utf-8"))
    result = seal(case, protocol)
    encoded = json.dumps(result, indent=2, ensure_ascii=False) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(encoded, encoding="utf-8")
    else:
        print(encoded, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

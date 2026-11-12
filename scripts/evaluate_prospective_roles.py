#!/usr/bin/env python3
"""Run SCI-PRED-03 comparison after revealing independent role evidence.

No supplied pairs => report zero evidence, not a simulated scientific result.
Pairs JSON format: {"pairs":[{"sealed":{...},"gold":{...}}]}.
The evidence file must be passed explicitly; never read HOLD silently.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

from iberos.prospective_role_evaluation import evaluate_cohort
from iberos.prospective_role_lock import PROTOCOL_PATH


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--evidence", type=Path, help="Explicitly supplied unblinded evidence pairs JSON")
    parser.add_argument("--protocol", type=Path, default=PROTOCOL_PATH)
    parser.add_argument("--output", type=Path, help="Write audit output to a non-source output path")
    parser.add_argument("--train-baseline", type=float, help="Previously frozen TRAIN-only accuracy")
    args = parser.parse_args(argv)
    proto_bytes = args.protocol.read_bytes()
    protocol = json.loads(proto_bytes)
    if args.evidence:
        evidence_bytes = args.evidence.read_bytes()
        src = json.loads(evidence_bytes)
        if not isinstance(src, dict) or set(src) != {"pairs"}:
            raise ValueError("Expected JSON object with only pairs")
        pairs = src["pairs"]
        evidence_sha = hashlib.sha256(evidence_bytes).hexdigest()
    else:
        pairs, evidence_sha = [], None
    result = evaluate_cohort(pairs, protocol, locked_train_baseline_accuracy=args.train_baseline)
    result["experiment"] = "SCI-PRED-03"
    result["protocol_sha256_file"] = hashlib.sha256(proto_bytes).hexdigest()
    result["supplied_evidence_file_sha256"] = evidence_sha
    result["sources_automatically_retrieved"] = False
    result["environment_uses_synthetic_or_unverified_fixtures_for_gold"] = evidence_sha is None
    encoded = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        if args.evidence is not None and args.evidence.resolve() == args.output.resolve():
            raise ValueError("Cannot overwrite original gold evidence")
        if args.protocol.resolve() == args.output.resolve():
            raise ValueError("Cannot overwrite locked protocol")
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(encoded, encoding="utf-8")
    else:
        print(encoded, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

"""Fail-closed evaluation of external evidence against frozen C474 predictions."""
from dataclasses import dataclass, asdict
from pathlib import Path
import hashlib, json

PROTOCOLS = ("CASE-NET-PROSPECTIVE-01","ROK-RECIPIENT-02","KA-DIRECTION-PROSPECTIVE-01","SALIR-PROSPECTIVE-01","KUTUR-PROSPECTIVE-01","DEDI-ORTHO-01","VERBAL-PROSPECTIVE-01")
LABELS = ("STRICT_PROSPECTIVE_PASS","EXTERNAL_CONVERGENCE","RETROSPECTIVE_REPLICATION","FAIL","INDETERMINATE")

@dataclass(frozen=True)
class Evidence:
    protocol: str
    source: str
    published_at: str
    version: str
    phys_id: str
    leak_group: str
    prediction_literal: str
    prediction_lock_sha256: str
    independent: bool
    contamination_checked: bool
    outcome: str
    controls: str
    evidence_digest: str


def evaluate(item: Evidence):
    if item.protocol not in PROTOCOLS:
        raise ValueError("Unknown protocol")
    if item.outcome not in LABELS:
        raise ValueError("Unknown outcome")
    required = (item.source,item.published_at,item.version,item.phys_id,item.leak_group,item.prediction_literal,item.prediction_lock_sha256,item.controls,item.evidence_digest)
    complete = all(required)
    # No PASS/FAIL may be certified without independently audited provenance and lock.
    if item.outcome in ("STRICT_PROSPECTIVE_PASS","FAIL"):
        if not (complete and item.independent and item.contamination_checked):
            return {"classification":"INDETERMINATE","reason":"Missing independence, contamination audit or provenance; proposed outcome retained separately","proposed":item.outcome}
        # A complete record is necessary, not sufficient: external human audit required.
        return {"classification":"INDETERMINATE","reason":"Prospective PASS/FAIL requires manual comparison to independently dated original lock","proposed":item.outcome}
    return {"classification":item.outcome if complete else "INDETERMINATE","reason":"Auxiliary classification only; no Core promotion"}


def save_report(item: Evidence, output: Path):
    if output.exists():
        raise FileExistsError("Reports are append-only; choose a new filename")
    result = {"input":asdict(item),"assessment":evaluate(item)}
    output.parent.mkdir(parents=True,exist_ok=True)
    output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\\n",encoding="utf-8")
    return result

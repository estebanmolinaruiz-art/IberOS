"""Read-only inspection of IberOS historical ZIP backups; never restores FULL3406.

A candidate with 3406 rows is *not* proof that it is the frozen legacy corpus.
Check provenance, original hash, entry identity, and original splits separately.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import zipfile
from pathlib import Path

MAX_MEMBER_BYTES = 30_000_000
MAX_MEMBERS = 4000
EXTENSIONS = {".csv", ".tsv", ".json", ".jsonl", ".ndjson"}
IDENTITY_COLUMNS = {"entry_id", "phys_id", "object_id", "leak_group"}


def _read_member(zf: zipfile.ZipFile, info: zipfile.ZipInfo) -> bytes | None:
    if info.file_size > MAX_MEMBER_BYTES or info.flag_bits & 0x1:
        return None
    with zf.open(info) as stream:
        data = stream.read(MAX_MEMBER_BYTES + 1)
        if len(data) > MAX_MEMBER_BYTES:
            return None
    return data


def _inspect_rows(filename: str, data: bytes) -> dict:
    suffix = Path(filename).suffix.lower()
    try:
        content = data.decode("utf-8-sig")
    except UnicodeDecodeError:
        return {"status": "NON_UTF8_ENCODING_REVIEW", "entries": None}
    if suffix in {".csv", ".tsv"}:
        delimiter = "\t" if suffix == ".tsv" else ","
        try:
            reader = csv.DictReader(io.StringIO(content), delimiter=delimiter)
            columns = list(reader.fieldnames or [])
            count = sum(1 for row in reader if any((v or "").strip() for v in row.values() if isinstance(v, str)))
        except csv.Error:
            return {"status": "CSV_PARSE_ERROR", "entries": None}
        return {
            "status": "COUNTED_TABLE_ROWS",
            "entries": count,
            "identity_columns": sorted(IDENTITY_COLUMNS & {c.lower().lstrip("\ufeff") for c in columns}),
            "headers": columns[:30],
        }
    if suffix in {".jsonl", ".ndjson"}:
        try:
            rows = [json.loads(line) for line in content.splitlines() if line.strip()]
        except (ValueError, TypeError):
            return {"status": "JSONL_PARSE_ERROR", "entries": None}
        return {"status": "COUNTED_JSONL_RECORDS", "entries": len(rows)}
    if suffix == ".json":
        try:
            document = json.loads(content)
        except ValueError:
            return {"status": "JSON_PARSE_ERROR", "entries": None}
        if isinstance(document, list):
            return {"status": "COUNTED_JSON_ARRAY", "entries": len(document)}
        return {"status": "JSON_OBJECT_UNSCORABLE", "entries": None}
    return {"status": "UNSUPPORTED", "entries": None}


def inspect_backup(path: Path) -> dict:
    """Never extract paths or modify the ZIP, even on untrusted input."""
    if not zipfile.is_zipfile(path):
        raise ValueError("Not a ZIP archive")
    archive_hash = hashlib.sha256(path.read_bytes()).hexdigest()
    with zipfile.ZipFile(path) as zf:
        members = zf.infolist()
        if len(members) > MAX_MEMBERS:
            raise ValueError("Excessive ZIP member count")
        report = []
        for info in members:
            if info.is_dir():
                continue
            suffix = Path(info.filename).suffix.lower()
            if suffix not in EXTENSIONS:
                continue
            try:
                data = _read_member(zf, info)
                row = (_inspect_rows(info.filename, data) if data is not None
                       else {"status": "SKIPPED_TOO_LARGE_OR_ENCRYPTED", "entries": None})
            except (RuntimeError, OSError, EOFError, zipfile.BadZipFile, ValueError):
                row = {"status": "MEMBER_READ_FAILED", "entries": None}
            report.append({
                "path": info.filename,
                "uncompressed_bytes": info.file_size,
                **row,
                "matches_expected_row_count": row.get("entries") == 3406,
                "verified_as_full3406": False,
            })
    return {
        "experiment": "FULL3406_BACKUP_INSPECTION",
        "archive_filename": path.name,
        "archive_sha256": archive_hash,
        "candidate_tables": report,
        "candidates_with_3406_rows": sum(int(x["matches_expected_row_count"]) for x in report),
        "full3406_recovered": False,
        "scientific_promotion": False,
        "required_next_step": "Review provenance, schema, entry IDs, physical identities, leak groups, original TRAIN/VAL/HOLD splits and hashes",
    }


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Inspect IberOS ZIP backup without extraction or corpus modification")
    p.add_argument("archive", type=Path)
    p.add_argument("--json", type=Path, help="Save report outside source ZIP")
    args = p.parse_args(argv)
    result = inspect_backup(args.archive)
    output = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(output, encoding="utf-8")
    else:
        print(output, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

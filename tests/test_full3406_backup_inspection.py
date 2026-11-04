"""Regression tests for fail-closed historical ZIP backup inspection."""
import csv
import io
import json
import zipfile

import pytest

from iberos.full3406_backup import inspect_backup


def make_zip(path, members):
    with zipfile.ZipFile(path, "w") as z:
        for filename, content in members.items():
            z.writestr(filename, content)
    return path


def test_3406_count_not_automatically_certified(tmp_path):
    buf = io.StringIO()
    writer = csv.writer(buf)
    writer.writerow(["ENTRY_ID", "PHYS_ID", "LEAK_GROUP", "split"])
    writer.writerows((str(n), "p"+str(n), "g"+str(n), "TRAIN") for n in range(3406))
    path = make_zip(tmp_path / "example.zip", {"archive/FULL3406.csv": buf.getvalue()})
    r = inspect_backup(path)
    assert r["candidate_tables"][0]["entries"] == 3406
    assert r["candidate_tables"][0]["matches_expected_row_count"]
    assert r["candidate_tables"][0]["verified_as_full3406"] is False
    assert r["full3406_recovered"] is False
    assert r["scientific_promotion"] is False
    assert len(r["archive_sha256"]) == 64


def test_small_csv_no_false_positive(tmp_path):
    path = make_zip(tmp_path / "b.zip", {"legacy.csv": "ENTRY_ID,value\n1,a\n2,b\n"})
    r = inspect_backup(path)
    assert r["candidate_tables"][0]["entries"] == 2
    assert r["candidates_with_3406_rows"] == 0


def test_jsonl_and_nested_path_never_extracted(tmp_path):
    path = make_zip(tmp_path / "b.zip", {
        "../outside.jsonl": '{"a":1}\n{"a":2}\n',
        "images/a.png": b"abc",
    })
    r = inspect_backup(path)
    assert r["candidate_tables"][0]["entries"] == 2
    assert not (tmp_path.parent / "outside.jsonl").exists()


def test_json_object_cannot_be_mistaken_for_3406(tmp_path):
    path = make_zip(tmp_path / "b.zip", {"meta.json": json.dumps({"entry_count":3406})})
    r = inspect_backup(path)
    assert r["candidate_tables"][0]["status"] == "JSON_OBJECT_UNSCORABLE"
    assert r["candidates_with_3406_rows"] == 0


def test_reject_non_zip(tmp_path):
    f = tmp_path / "not.zip"
    f.write_text("not an archive")
    with pytest.raises(ValueError, match="Not a ZIP"):
        inspect_backup(f)

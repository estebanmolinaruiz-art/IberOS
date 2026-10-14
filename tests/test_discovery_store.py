import json
import pytest
from iberos.discovery_store import append_discoveries, classify_discovery

def test_persistent_inbox_deduplicates_across_runs(tmp_path):
    path = tmp_path / "inbox.jsonl"
    finding = {"title": "Epigrafia iberica", "url": "https://example.org/study",
               "modules": ["PALEO", "TRACE"]}
    first = append_discoveries(path, [finding, finding])
    second = append_discoveries(path, [finding])
    entries = [json.loads(line) for line in path.read_text().splitlines()]
    assert first["new"] == 1 and second["new"] == 0
    assert len(entries) == 1
    assert entries[0]["modules_to_review"] == ["PALEO", "TRACE"]
    assert entries[0]["eligible_for_core"] is False

def test_invalid_tag_rejected_without_file_write(tmp_path):
    path = tmp_path / "inbox.jsonl"
    with pytest.raises(ValueError):
        append_discoveries(path, [{"title":"Claim","url":"https://example.org/x","modules":["MAGIC"]}])
    assert not path.exists()

def test_bad_prior_ledger_fails_closed(tmp_path):
    path = tmp_path / "inbox.jsonl"
    path.write_text("{bad json\n")
    with pytest.raises(ValueError):
        append_discoveries(path, [{"title":"New","url":"https://example.org/new"}])
    assert path.read_text() == "{bad json\n"

def test_default_route_is_trace():
    assert classify_discovery({})["modules_to_review"] == ["TRACE"]

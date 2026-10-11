import json
import subprocess
import sys


def run_benchmark(tmp_path, evidence):
    path = tmp_path / 'evidence.json'
    path.write_text(json.dumps(evidence), encoding='utf-8')
    return subprocess.run(
        [sys.executable, '-m', 'iberos.cli', 'dedi-benchmark', str(path)],
        text=True, capture_output=True,
    )


def test_empty_evidence_remains_blocked(tmp_path):
    result = run_benchmark(tmp_path, {'observations': []})
    assert result.returncode == 0
    report = json.loads(result.stdout)
    assert 'formal_matrix' in report
    assert report['semantic_gate']['state'] == 'BLOCKED'
    assert report['semantic_gate']['scientific_state'] == 'UNVERIFIED'
    assert report['official_metrics_changed'] is False
    assert report['semantic_gate']['automatic_core_promotion'] is False
    assert report['semantic_gate']['authority']['semantic_release'] == 'C594'


def test_invalid_records_are_rejected(tmp_path):
    result = run_benchmark(tmp_path, {'observations': ['not-an-object']})
    assert result.returncode == 2
    assert 'Each observation must be an object' in result.stderr


def test_invalid_rule_is_rejected(tmp_path):
    result = run_benchmark(tmp_path, {'observations': [], 'preregistered_rule': []})
    assert result.returncode == 2
    assert 'preregistered_rule must be an object' in result.stderr

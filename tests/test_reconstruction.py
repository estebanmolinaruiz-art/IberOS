import pytest

from iberos.reconstruction import build_reconstruction, validate_reconstruction


def test_requires_documented_source():
    ok, errors = validate_reconstruction([{"text": "texto", "layer": "EVIDENCE"}])
    assert not ok and any("source" in e for e in errors)


def test_rejects_semantic_promotion_from_evidence():
    ok, errors = validate_reconstruction([
        {"text": "pago", "layer": "EVIDENCE", "source": "edition 1", "meaning_claim": True}
    ])
    assert not ok and any("semantic" in e for e in errors)


def test_requires_rationale_for_hypotheses():
    ok, errors = validate_reconstruction([
        {"text": "destinatario?", "layer": "HYPOTHESIS", "source": "edition 1"}
    ])
    assert not ok and any("rationale" in e for e in errors)


def test_valid_mixed_reconstruction_never_promotes_core():
    result = build_reconstruction("IBR-PLM-0002", [
        {"text": "SALIR", "layer": "EVIDENCE", "source": "transcription source"},
        {"text": "[función por determinar]", "layer": "AMBIGUOUS",
         "source": "documented analysis", "rationale": "prospective semantic gate open"},
        {"text": "[…]", "layer": "UNRESOLVED"},
    ])
    assert result["automatic_core_promotion"] is False
    assert result["scientific_state"] == "UNVERIFIED"
    assert [s["layer"] for s in result["reconstruction_segments"]] == [
        "EVIDENCE", "AMBIGUOUS", "UNRESOLVED"
    ]


@pytest.mark.parametrize("bad", [None, [], [{}], ["text"], [{"text": " ", "layer": "UNRESOLVED"}]])
def test_rejects_malformed_or_empty(bad):
    ok, _ = validate_reconstruction(bad)
    assert not ok


@pytest.mark.parametrize("claim", ["yes", 1, [], {"supported": True}])
def test_rejects_nonboolean_semantic_claims(claim):
    ok, errors = validate_reconstruction([
        {"text": "SALIR", "layer": "EVIDENCE", "source": "edition 1", "meaning_claim": claim}
    ])
    assert not ok and any("meaning_claim must be boolean" in e for e in errors)


def test_rejects_invalid_object_identifier():
    with pytest.raises(ValueError):
        build_reconstruction("not-a-valid-object", [{"text": "[…]", "layer": "UNRESOLVED"}])

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


def test_registered_sources_are_not_semantic_validation():
    from iberos.reconstruction import audit_reconstruction_sources
    result = audit_reconstruction_sources(
        [{"text": "SALIR", "layer": "EVIDENCE", "source": "edition-A"}],
        {"edition-A": {"reference": "Bibliographic edition", "locator": "p. 12, line 3"}},
    )
    assert result["status"] == "REGISTERED_SOURCES_ONLY"
    assert result["scientific_state"] == "UNVERIFIED"
    assert result["independence_audited"] is False
    assert result["semantic_validation"] is False
    assert result["automatic_core_promotion"] is False


def test_source_audit_blocks_unknown_and_excluded_sources():
    from iberos.reconstruction import audit_reconstruction_sources
    segment = [{"text": "SALIR", "layer": "EVIDENCE", "source": "edition-A"}]
    missing = audit_reconstruction_sources(segment, {})
    assert missing["status"] == "BLOCKED"
    excluded = audit_reconstruction_sources(segment, {
        "edition-A": {"reference": "Edition", "locator": "p. 2", "excluded_control": True}
    })
    assert excluded["status"] == "BLOCKED"


def test_source_audit_requires_precise_locator():
    from iberos.reconstruction import audit_reconstruction_sources
    result = audit_reconstruction_sources(
        [{"text": "SALIR", "layer": "EVIDENCE", "source": "edition-A"}],
        {"edition-A": {"reference": "Edition"}},
    )
    assert result["status"] == "BLOCKED"
    assert any("locator" in error for error in result["errors"])


def test_same_physical_object_editions_are_not_double_counted():
    from iberos.reconstruction import audit_reconstruction_independence
    seg = [{"text": "SALIR", "layer": "EVIDENCE", "source": "a"},
           {"text": "ROK", "layer": "EVIDENCE", "source": "b"}]
    catalog = {
        "a": {"reference": "Edition A", "locator": "p. 1", "PHYS_ID": "object-one"},
        "b": {"reference": "Edition B", "locator": "p. 2", "PHYS_ID": "object-one"},
    }
    audit = audit_reconstruction_independence(seg, catalog)
    assert audit["source_count"] == 2
    assert audit["identity_unit_count"] == 1
    assert audit["independence_confirmed"] is False
    assert audit["automatic_core_promotion"] is False


def test_sources_without_physical_identifiers_are_blocked():
    from iberos.reconstruction import audit_reconstruction_independence
    audit = audit_reconstruction_independence(
        [{"text": "SALIR", "layer": "EVIDENCE", "source": "a"}],
        {"a": {"reference": "Edition", "locator": "p. 1"}},
    )
    assert audit["status"] == "BLOCKED"
    assert audit["unresolved_sources"] == ["a"]


def test_shared_leak_group_collapses_entries():
    from iberos.reconstruction import audit_reconstruction_independence
    seg = [{"text": "SALIR", "layer": "EVIDENCE", "source": "a"},
           {"text": "ROK", "layer": "EVIDENCE", "source": "b"}]
    catalog = {
        "a": {"reference": "Edition A", "locator": "p. 1", "LEAK_GROUP": "duplicate"},
        "b": {"reference": "Edition B", "locator": "p. 2", "LEAK_GROUP": "duplicate"},
    }
    audit = audit_reconstruction_independence(seg, catalog)
    assert audit["identity_unit_count"] == 1
    assert audit["status"] == "IDENTITY_GROUPED_REVIEW_REQUIRED"


def test_cross_identifier_bridge_is_one_documentary_unit():
    from iberos.reconstruction import audit_reconstruction_independence
    segments = [
        {"text": "A", "layer": "EVIDENCE", "source": "a"},
        {"text": "B", "layer": "EVIDENCE", "source": "b"},
        {"text": "C", "layer": "EVIDENCE", "source": "c"},
    ]
    catalog = {
        "a": {"reference": "Ed A", "locator": "p1", "PHYS_ID": "P1"},
        "b": {"reference": "Ed B", "locator": "p2", "PHYS_ID": "P1", "LEAK_GROUP": "L1"},
        "c": {"reference": "Ed C", "locator": "p3", "LEAK_GROUP": "L1"},
    }
    result = audit_reconstruction_independence(segments, catalog)
    assert result["identity_unit_count"] == 1
    assert sorted(next(iter(result["identity_units"].values()))) == ["a", "b", "c"]
    assert result["automatic_core_promotion"] is False


def test_specific_dependency_bridge_collapses_but_generic_does_not():
    from iberos.reconstruction import audit_reconstruction_independence
    segs = [
        {"text": x, "layer": "EVIDENCE", "source": x}
        for x in ("a", "b", "c")
    ]
    catalog = {
        "a": {"reference": "A", "locator": "p1", "PHYS_ID": "P1",
              "Dependency_Group": "KNOWN_COPY"},
        "b": {"reference": "B", "locator": "p2", "Dependency_Group": "KNOWN_COPY"},
        "c": {"reference": "C", "locator": "p3", "PHYS_ID": "P2",
              "Dependency_Group": "INDEPENDENT_OR_UNRESOLVED"},
    }
    result = audit_reconstruction_independence(segs, catalog)
    assert result["identity_unit_count"] == 2
    assert result["independence_confirmed"] is False

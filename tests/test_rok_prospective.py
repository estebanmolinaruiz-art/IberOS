from iberos.rok_prospective import assess_rok_prospective

def sample(witness_id, physical_id, control_type):
    return {
        "witness_id": witness_id, "physical_id": physical_id,
        "source": "edition", "passage": "line 1",
        "lock_id": "prereg-1", "lock_hash": "sha256:synthetic",
        "prediction_id": "prediction-1", "prediction": "H1",
        "segmentation": "NP_TE_ROK", "external_role": "RECIPIENT",
        "external_role_source": "synthetic external check",
        "independent_context": True, "held_out": True,
        "reading_secure": True, "genre": "lead letter",
        "control_type": control_type,
    }

def test_synthetic_complete_is_review_only():
    result = assess_rok_prospective([
        sample("w1", "physical-1", "TARGET"),
        sample("w2", "physical-2", "NON_ROK"),
    ])
    assert result["status"] == "READY_FOR_INDEPENDENT_REVIEW"
    assert result["scientific_state"] == "UNVERIFIED"
    assert result["official_rok_recipient_gate"] == "OPEN"
    assert result["automatic_core_promotion"] is False

def test_same_physical_document_cannot_be_two_witnesses():
    result = assess_rok_prospective([
        sample("edition-A", "same-physical", "TARGET"),
        sample("edition-B", "same-physical", "NEGATIVE"),
    ])
    assert result["status"] == "BLOCKED"
    assert any("duplicate physical" in error for error in result["errors"])

def test_absent_independent_role_blocks():
    candidate = sample("a", "one", "TARGET")
    candidate["external_role"] = "UNRESOLVED"
    result = assess_rok_prospective([candidate, sample("b", "two", "NON_ROK")])
    assert result["status"] == "BLOCKED"

def test_invalid_prediction_and_missing_preregistration_block():
    candidate = sample("a", "one", "TARGET")
    candidate["prediction"] = "H99"
    candidate["lock_hash"] = ""
    result = assess_rok_prospective([candidate, sample("b", "two", "NEGATIVE")])
    assert result["status"] == "BLOCKED"

def test_no_controls_blocks():
    assert assess_rok_prospective([sample("a", "one", "TARGET")])["status"] == "BLOCKED"

def test_nonboolean_independence_is_invalid():
    candidate = sample("a", "one", "TARGET")
    candidate["held_out"] = "yes"
    assert assess_rok_prospective([candidate, sample("b", "two", "NEGATIVE")])["status"] == "BLOCKED"


def test_shared_leak_group_blocks_independence():
    a = sample("edition-A", "physical-1", "TARGET")
    b = sample("edition-B", "physical-2", "NON_ROK")
    a["LEAK_GROUP"] = b["LEAK_GROUP"] = "same-copy-lineage"
    result = assess_rok_prospective([a, b])
    assert result["status"] == "BLOCKED"
    assert any("cross-edition dependency" in error for error in result["errors"])


def test_specific_dependency_group_blocks_independence():
    a = sample("edition-A", "physical-1", "TARGET")
    b = sample("edition-B", "physical-2", "NEGATIVE")
    a["Dependency_Group"] = b["Dependency_Group"] = "SPECIFIC_DEPENDENCY"
    result = assess_rok_prospective([a, b])
    assert result["status"] == "BLOCKED"


def test_generic_dependency_labels_do_not_claim_shared_identity():
    a = sample("edition-A", "physical-1", "TARGET")
    b = sample("edition-B", "physical-2", "NON_ROK")
    a["Dependency_Group"] = b["Dependency_Group"] = "INDEPENDENT_OR_UNRESOLVED"
    result = assess_rok_prospective([a, b])
    assert result["status"] == "READY_FOR_INDEPENDENT_REVIEW"
    assert result["automatic_core_promotion"] is False


def test_transitive_identity_bridge_blocks_all_three_witnesses():
    a = sample("a", "P1", "TARGET")
    b = sample("b", "P2", "NON_ROK")
    c = sample("c", "P3", "NEGATIVE")
    a["LEAK_GROUP"] = b["LEAK_GROUP"] = "L1"
    b["Dependency_Group"] = c["Dependency_Group"] = "SPECIFIC-COPY"
    result = assess_rok_prospective([a, b, c])
    assert result["status"] == "BLOCKED"
    assert result["documentary_unit_count"] == 1
    assert result["documentary_components"] == [[0, 1, 2]]
    assert any("transitive documentary dependency" in e for e in result["errors"])


def test_separate_documentary_witnesses_remain_separate():
    a = sample("a", "P1", "TARGET")
    b = sample("b", "P2", "NON_ROK")
    c = sample("c", "P3", "NEGATIVE")
    result = assess_rok_prospective([a, b, c])
    assert result["status"] == "READY_FOR_INDEPENDENT_REVIEW"
    assert result["documentary_unit_count"] == 3
    assert result["official_rok_recipient_gate"] == "OPEN"

from pathlib import Path
from iberos import load_registry, get_object, family_objects, validate_result

def test_registry_has_curated_objects():
    rows = load_registry()
    assert len(rows) == 38

def test_tivissa_present():
    row = get_object("IBR-PLM-0002")
    assert row is not None
    assert "Tivissa" in row["Nombre_objeto"]

def test_family_lookup():
    rows = family_objects("EGIAR_EKIAR")
    assert any(r["OBJECT_ID"] == "IBR-CER-0001" for r in rows)

def test_example_validates():
    ok, errors = validate_result(Path("data/examples/tivissa.json"))
    assert ok, errors

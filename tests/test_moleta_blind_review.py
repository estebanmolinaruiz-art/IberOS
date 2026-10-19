"""Broad panels are only visual-workflow aids, never independently verified sign maps."""
import sys
from pathlib import Path
from PIL import Image
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
from build_moleta_blind_review import build

def test_blind_moleta_panels(tmp_path):
    p=tmp_path/"p.png";d=tmp_path/"d.png"
    Image.new("RGB",(320,120),"white").save(p)
    Image.new("RGB",(200,110),"white").save(d)
    out=tmp_path/"out"
    result=build(p,d,out)
    assert len(result["panels"])==6
    assert result["glyphs_independently_verified"]==0
    for row in result["panels"]:
        assert row["sign_roi"] is None
        assert row["glyph_labels_hidden"] is True
        assert row["independently_assessed"] is False
        assert (out/row["image"]).exists()
    assert (out/"manifest.json").exists()

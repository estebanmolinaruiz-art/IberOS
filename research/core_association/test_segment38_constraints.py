#!/usr/bin/env python3
import json
from pathlib import Path
P=Path(__file__).resolve().parent/"segment38_moleta_constraints.json"
d=json.loads(P.read_text(encoding="utf8"))
s=d["source_claims"];a=d["algorithmic_observations"];g=d["gates"]
assert s["text_lines"]==3
assert s["zone_1_lines"]+s["zone_2_lines"]==s["text_lines"]
assert s["visible_sign_remains"]==21
assert a["segment35_unverified_ink_bands"]==7
assert a["segment37_accepted_registrations"]==0
assert g["verified_line_to_crop_mapping"]==0
assert g["verified_glyph_to_crop_mapping"]==0
assert g["automatic_mapping_of_7_bands_to_3_lines_forbidden"]
print("PASS: documentary line count locked; 7 image bands not identified as 3 lines; photo-drawing matching unverified.")

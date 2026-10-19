import importlib.util
from pathlib import Path
s=importlib.util.spec_from_file_location("mapper",Path(__file__).resolve().parents[1]/"scripts"/"iberian_font_mapping_gate.py")
m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
def test_unknown_never_becomes_te():
 r=m.convert([{"record_id":"1","transcription_raw":"Ȁ9","uncertainty":""}],[{"source_codepoint":"Ȁ","sign_value":"te","review_status":"REVIEWED_MAPPING"}])
 assert r[0]["decode_status"]=="BLOCKED" and r[0]["te_status"]=="UNKNOWN"
def test_reviewed_mapping_is_still_not_verified_reading():
 r=m.convert([{"record_id":"1","transcription_raw":"Ȁ","uncertainty":""}],[{"source_codepoint":"Ȁ","sign_value":"te","review_status":"REVIEWED_MAPPING"}])
 assert r[0]["atomic_sign_tokens"]=="te" and r[0]["independent_sign_review"]=="NO" and r[0]["te_status"]=="UNKNOWN"
def test_bold_flags_block_mapping():
 r=m.convert([{"record_id":"1","transcription_raw":"Ȁ","uncertainty":"MARKED"}],[{"source_codepoint":"Ȁ","sign_value":"te","review_status":"REVIEWED_MAPPING"}])
 assert r[0]["decode_status"]=="BLOCKED"

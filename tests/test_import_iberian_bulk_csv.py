import importlib.util,csv
from pathlib import Path
p=Path(__file__).resolve().parents[1]/"scripts"/"import_iberian_bulk_csv.py"
s=importlib.util.spec_from_file_location("bulk",p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
def test_bulk_thousands_and_no_unverified_te(tmp_path):
    x=tmp_path/"input.csv";y=tmp_path/"out.csv"
    with x.open("w") as f:
        w=csv.writer(f);w.writerow(["reference","transcription_raw"])
        for i in range(2500):w.writerow([f"ref-{i}","opaque TE characters"])
    v=m.build(x,y,"TEST_DATA","METADATA_ONLY")
    assert v["imported_records"]==2500
    with y.open() as f:r=list(csv.DictReader(f))
    assert len(r)==2500
    assert all(x["te_status"]=="UNKNOWN" and x["hold_eligible"]=="NO" for x in r)
def test_dedup(tmp_path):
    x=tmp_path/"in.csv";y=tmp_path/"out.csv"
    x.write_text("reference,transcription_raw\na,x\na,x\n")
    assert m.build(x,y,"test","METADATA_ONLY")["duplicates_omitted"]==1

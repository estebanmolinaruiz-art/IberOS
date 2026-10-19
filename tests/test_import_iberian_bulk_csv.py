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

def test_preserve_editorial_markup_and_physical_group(tmp_path):
    x=tmp_path/"in.csv";y=tmp_path/"out.csv"
    with x.open("w",encoding="utf8",newline="") as f:
        w=csv.writer(f);w.writerow(["reference","transcription_raw","physical_group","uncertainty","editorial_markup"])
        w.writerow(["edit1","Ƅ?","OBJECT-7","unreadable last sign","underline 1-2"])
        w.writerow(["edit2","Ƅx","OBJECT-7","","bold alternative"])
        w.writerow(["edit3","b","", "", ""])
    result=m.build(x,y,"CATALOG","METADATA_ONLY")
    assert result["imported_records"]==3
    assert result["explicit_physical_groups"]==1
    assert result["physical_groups_with_multiple_readings"]==1
    assert result["records_without_physical_identity"]==1
    with y.open(encoding="utf8",newline="") as f:rows=list(csv.DictReader(f))
    assert rows[0]["transcription_raw"]=="Ƅ?"
    assert rows[0]["editorial_markup"]=="underline 1-2"
    assert rows[1]["physical_group"]=="OBJECT-7"
    assert rows[0]["te_status"]=="UNKNOWN"
def test_refuse_overwrite_and_unknown_license(tmp_path):
    x=tmp_path/"one.csv";x.write_text("reference,transcription_raw\\na,x\\n",encoding="utf8")
    import pytest
    with pytest.raises(ValueError):m.build(x,x,"catalog","METADATA_ONLY")
    with pytest.raises(ValueError):m.build(x,tmp_path/"out.csv","catalog","NO-LICENSE")

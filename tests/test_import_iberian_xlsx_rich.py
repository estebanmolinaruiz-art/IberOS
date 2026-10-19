import importlib.util,zipfile,csv,json
from pathlib import Path
p=Path(__file__).resolve().parents[1]/"scripts"/"import_iberian_xlsx_rich.py"
s=importlib.util.spec_from_file_location("xlsx_rich",p)
mod=importlib.util.module_from_spec(s);s.loader.exec_module(mod)
def test_xlsx_rich_runs_are_retained_without_te_promotion(tmp_path):
    x=tmp_path/"fixture.xlsx";out=tmp_path/"staging.csv"
    files={
      "xl/workbook.xml":'<workbook xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"><sheets><sheet name="Corpus" sheetId="1" r:id="rId1"/></sheets></workbook>',
      "xl/_rels/workbook.xml.rels":'<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rId1" Target="worksheets/sheet1.xml"/></Relationships>',
      "xl/sharedStrings.xml":'<sst xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main"><si><t>Reference</t></si><si><t>Reading</t></si><si><t>CASE-1</t></si><si><r><rPr><u/></rPr><t>te</t></r><r><rPr><b/></rPr><t>?</t></r></si></sst>',
      "xl/worksheets/sheet1.xml":'<worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main"><sheetData><row r="1"><c r="A1" t="s"><v>0</v></c><c r="B1" t="s"><v>1</v></c></row><row r="2"><c r="A2" t="s"><v>2</v></c><c r="B2" t="s"><v>3</v></c></row></sheetData></worksheet>'}
    with zipfile.ZipFile(x,"w") as z:
        for path,body in files.items():z.writestr(path,body)
    assert mod.convert(x,out)==1
    with out.open(encoding="utf8",newline="") as f:r=list(csv.DictReader(f))
    assert r[0]["transcription_raw"]=="te?"
    markup=json.loads(r[0]["editorial_markup"])
    assert markup[0]["underline"] and markup[1]["bold"]
    assert r[0]["te_status"]=="UNKNOWN"
    assert r[0]["hold_eligible"]=="NO"

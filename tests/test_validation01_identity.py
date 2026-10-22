import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from validation01_identity import identity
import validation01_hold_leakage_guard as g

def test_typographical_alias():
 assert identity(' Orléyl - VII ')==identity('F.9.7')
def test_distinct_tablets_not_collapsed():
 assert identity('Orleyl V')!=identity('Orleyl VII')
def test_undocumented_similarity_not_merged():
 assert identity('Other-VII')!=identity('Orleyl VII')
def test_known_from_screening_physical_group():
 result=g.evaluate([{'split':'HOLD','object_id':'new','physical_group':'A B - 7'}],[{'object_id':'old','physical_group':'AB7'}],[])
 assert result['gate']=='BLOCKED'
def test_alias_between_hold_records():
 result=g.evaluate([{'split':'HOLD','object_id':'x','physical_group':'C - 001'}, {'split':'HOLD','object_id':'y','physical_group':'C001'}],[],[])
 assert any(i['issue']=='DUPLICATE_HOLD_IDENTITY' for i in result['issues'])
def test_alias_for_orleyl():
 assert g.evaluate([{'split':'HOLD','object_id':'F 9 7','physical_group':'object'}],[],[])['gate']=='BLOCKED'
def test_unknown_not_certified():
 assert g.evaluate([{'split':'HOLD','object_id':'other','physical_group':'unrelated'}],[],[])['gate']=='PASS_KNOWN_OBJECT_SCREEN'

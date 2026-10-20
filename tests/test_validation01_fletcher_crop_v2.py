import importlib.util
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
s=importlib.util.spec_from_file_location("crops",ROOT/"scripts/validation01_fletcher_crop_v2.py")
m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
def test_coordinated_reference():
 assert m.SIZE==(2287,1727)
 assert m.SOURCES["V"]["page"]==65 and m.SOURCES["V"]["physical_line"]==3
 assert m.SOURCES["VIIB"]["page"]==111 and m.SOURCES["VIIB"]["physical_line"]==2
 for v in m.SOURCES.values():
  l,t,r,b=v["bbox"]; assert 0<=l<r<=m.SIZE[0] and 0<=t<b<=m.SIZE[1]

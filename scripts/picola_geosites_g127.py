"""Run documentary GeoSites G-127 case for La Picola to Ilici."""
import json
from iberos.geosites_corridors import picola_ilici_research_case
if __name__ == "__main__":
    print(json.dumps(picola_ilici_research_case(),indent=2,sort_keys=True,ensure_ascii=False))

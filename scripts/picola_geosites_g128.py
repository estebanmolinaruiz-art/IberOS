"""Run G-128 strict corridor preflight without making up ancient geography."""
import json
from iberos.geosites_alternatives import picola_ilici_alternative_preflight
if __name__=="__main__":
    print(json.dumps(picola_ilici_alternative_preflight(),indent=2,ensure_ascii=False))

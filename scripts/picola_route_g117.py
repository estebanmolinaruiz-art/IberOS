"""G-117: Strict evidence-only predictive preflight for La Picola–La Alcudia."""
import json
from iberos.route_prediction import audit_picola_ensemble

if __name__ == "__main__":
    print(json.dumps(audit_picola_ensemble(),ensure_ascii=False,indent=2,sort_keys=True))

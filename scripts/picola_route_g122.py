"""Run IberOS La Picola northeast gate / R2 / moat strict G-122."""
import json
from iberos.route_picola_exit import assess_picola_gate_exit

if __name__ == "__main__":
    print(json.dumps(assess_picola_gate_exit(),ensure_ascii=False,indent=2,sort_keys=True))

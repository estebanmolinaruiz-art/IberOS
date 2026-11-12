"""Auditable G-125 quantitative local La Picola access envelope."""
import json
from iberos.route_picola_exit_window import estimate_exit_window
if __name__=="__main__":
    print(json.dumps(estimate_exit_window(),ensure_ascii=False,sort_keys=True,indent=2))

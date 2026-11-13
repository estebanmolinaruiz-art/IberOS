"""Run strict historical-continuity audit for Picola–Alcudia (G-113)."""
from iberos.route_continuity import Period, audit_continuity
import json

def main():
    periods=[Period("iberian_picola_occupation",-429,-349),
             Period("roman_comparison",1,200),
             Period("early_modern_comparison",1501,1700)]
    report=audit_continuity([], "picola_alcudia", periods)
    print(json.dumps(report,indent=2,ensure_ascii=False,sort_keys=True))

if __name__=="__main__":
    main()

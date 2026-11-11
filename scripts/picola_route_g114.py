"""G-115: Run comparably scoped historic-road leads separately from Iberian gates."""
import json
from iberos.route_prioritization import DocumentaryLead, prioritize

roads=[
    DocumentaryLead("MOLAR_2015","camino_del_molar","Moratalla_2015",
        "Moratalla_2015","historical_aerial_trace",True,False,False,
        "Historic trace towards SE La Alcudia; no overlap measured with Iberian gate."),
    DocumentaryLead("CARMAHADET_2015","cami_de_carmahadet","Moratalla_2015",
        "Moratalla_2015","historical_aerial_trace",True,False,False,
        "Historical salines–Elche connection; no attested 430–350 BCE use.")
]
gates=[
    DocumentaryLead("ILICI_GATE_2025","ilici_southeast_access","UA_2025",
        "UA_2025","archaeological_gate",True,True,False,
        "Iberian gate; date broadly compatible, not evidence for external road."),
    DocumentaryLead("PICOLA_GATE_1997","picola_northeast_access","Badie_Moret_1997",
        "Badie_Moret_1997","archaeological_gate",True,True,False,
        "Iberian gate and R2; ditch crossing not identified.")
]
result={
    "case":"PICOLA-ALCUDIA-G115",
    "road_leads":prioritize(roads,"430-350 BCE"),
    "gateway_anchors":prioritize(gates,"430-350 BCE"),
    "road_ranking_tie":True,
    "expert_review_priority":"camino_del_molar",
    "expert_reason":"Trace approaches the same general southeast sector of La Alcudia as the newly excavated Iberian gate; metric connection and chronology unverified.",
    "next_measurement":"Georeference Moratalla figs 9-10 against the 2025 gate plan, measuring axis-to-entrance separation and uncertainty.",
    "route_geometry":None,
    "road_proven":False,
    "complete_picola_alcudia_route_proven":False,
    "note":"Independent historical clues; scores are not probabilities or proof."
}
if __name__=="__main__":
    print(json.dumps(result,indent=2,ensure_ascii=False,sort_keys=True))

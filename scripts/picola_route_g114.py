"""G-114 Picola example: source-grounded leads, not prehistoric paths."""
import json
from iberos.route_prioritization import DocumentaryLead, prioritize
leads=[
    DocumentaryLead("MOLAR_2015","camino_del_molar","Moratalla_2015",
        "Moratalla_2015","historical_aerial_trace",True,False,False,
        "Visible historic route southeast of La Alcudia; dating at 430-350 BCE not shown."),
    DocumentaryLead("CARMAHADET_2015","cami_de_carmahadet","Moratalla_2015",
        "Moratalla_2015","historical_aerial_trace",True,False,False,
        "Historical road from salines toward Elche, not dated to Picola period."),
    DocumentaryLead("ILICI_GATE_2025","ilici_southeast_access","UA_2025",
        "UA_2025","archaeological_gate",True,True,False,
        "Gate from V-IV BCE; not a directly observed external road."),
    DocumentaryLead("PICOLA_GATE_1997","picola_northeast_access","Badie_Moret_1997",
        "Badie_Moret_1997","archaeological_gate",True,True,False,
        "Gate and street R2; ditch crossing and exterior path unverified.")
]
result=prioritize(leads,"430-350 BCE")
result["research_decision"]="Camino del Molar for La Alcudia gate contact; northeast gate/ditch for Picola coastal exit; no validated full route."
result["interpretation_warning"]="Gate observations are not road traces; rankings across different candidate scopes are not archaeological likelihoods."
print(json.dumps(result,indent=2,ensure_ascii=False))

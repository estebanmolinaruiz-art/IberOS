"""GeoSites G-143: falsación de continuidad; no inventa trayectos ni coordenadas."""
from math import atan2,degrees,hypot
PERIODO=(-429,-349)
REF_PICOLA=(713265.0,4230490.0)
REF_ILICI=(701823.285,4234872.059)
RUTAS={
 "litoral":["R2","cruce_foso","paleoterreno","corredor_litoral","puerta_ilici"],
 "interior_molar":["R2","cruce_foso","paleoterreno","corredor_interior","molar","puerta_ilici"]
}
# Estos atributos solo significan que un objeto está atestiguado, NO que un camino sea transitable.
FUENTES={
 "R2":"Moret-Badie 1998",
 "cruce_foso":"Moret-Badie 1998 (foso, sin cruce fechado)",
 "paleoterreno":"Fumanal-Ferrer 1998; Ferrer 2005 (sin poligonos)",
 "corredor_litoral":"Blazquez-Morilla 2003; Tent-Manclus 2013",
 "corredor_interior":"Blazquez-Ferrer 2012",
 "molar":"Moratalla 2015 (fecha iberica hipotetica)",
 "puerta_ilici":"UA 2025 (puerta SE IV sobre acceso V a.C.)"
}
ATESTIGUADOS=frozenset(("R2","molar","puerta_ilici"))

def geometria():
    dx=REF_ILICI[0]-REF_PICOLA[0]
    dy=REF_ILICI[1]-REF_PICOLA[1]
    return {"delta_este_m":round(dx,3),"delta_norte_m":round(dy,3),
            "distancia_recta_referencias_m":round(hypot(dx,dy),3),
            "azimut_referencias_grados":round((degrees(atan2(dx,dy))+360)%360,3),
            "puerta_a_puerta":False,"distancia_camino":False}

def evaluar():
    # No hay una sola cadena con uso contemporaneo, geometria, cruce y transitabilidad verificados.
    resultado={}
    for nombre,cadena in RUTAS.items():
        faltas={n:("cronologia_geometria_transito_no_verificados" if n in ATESTIGUADOS
                   else "segmento_y_cruces_no_verificados") for n in cadena}
        resultado[nombre]={"certificada":False,"segmentos":cadena,"faltas":faltas,
                          "longitud_camino_m":None}
    return {"caso":"G143","periodo":PERIODO,"geometria":geometria(),
            "rutas":resultado,"confirmada":False,"descartada":False,
            "dictamen":"NO_DEMOSTRADA_CON_EVIDENCIA_ACTUAL",
            "nota":"Criterio conservador. Desconocido no equivale a inexistente."}

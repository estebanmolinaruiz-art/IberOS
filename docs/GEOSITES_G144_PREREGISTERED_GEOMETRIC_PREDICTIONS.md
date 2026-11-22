# IberOS G-144 — Predicciones geométricas originales, fijadas 2026-11-22

Coste adicional 0 EUR. 12/12 pruebas unitarias locales. No se reutilizaron estadísticas arqueológicas. **Todas las predicciones siguientes son matemáticas y condicionales; no afirman que existiera un camino.**

## Entradas
BIC Picola A1 = (713265,4230490); termas orientales La Alcudia = (701823.285,4234872.059); EPSG:25830. No son puntos de puerta. D=12252.1542278m, azimut A→B 290.956325°.

## P-144-01, elipses matemáticas
Dado un trayecto entre A y B de longitud <= (1+e)D, cada punto P de la trayectoria necesariamente cumple |P-A|+|P-B| <= (1+e)D. Se construyen tres envolventes con parámetros de escenario (NO estadísticos históricos):
- e=5%: máximo 12864.761939m, semiancho 1961.301642m, área 39.633828km².
- e=10%: máximo 13477.369651m, semiancho 2807.321209m, área 59.431559km².
- e=20%: máximo 14702.585073m, semiancho 4063.579845m, área 93.847428km².

## P-144-02, salida hipotética a 45° (NE)
Este azimut es un supuesto que NO se ha medido de la puerta. Q=A+s(sin45°,cos45°). Penalización mínima E=s+|B-Q|-D:
- s=100m → E=141.082504m
- s=250m → E=353.967677m
- s=500m → E=712.083168m.
Si el recorrido total tuviera una sobrelongitud <=5%, tramo recto inicial a 45° <=430.842m; para 10% <=853.422m y 20% <=1676.881m. Sensibilidad: un tramo de 100m a azimut 25° añade 107.46m frente a 169.73m a 65°. La predicción debe recalcularse con azimut de puerta y extremos excavados georreferenciados.

## P-144-03, banda defensiva hipotética
Moret–Badie 1998: glacis 5–5.5m y foso ancho superior 5–6m. Si fuesen bandas paralelas rectas de ancho normal y existiese un cruce rectilíneo oblicuo, longitud geométrica (ancho glacis + ancho foso)/cosθ.
0°: 10–11.5m; 30°: 11.547–13.279m; 45°: 14.142–16.263m; 60°: 20–23m.
Esto NO determina un puente, su anchura, ni prueba la presencia de una estructura de paso.

## Prueba independiente prerregistrada
Obtener punto real de puerta NE, puerta SE, azimut real de R2 y cuatro o más controles no colineales, más perfiles excavados del foso. Sustituir los puntos de referencia por las puertas verificadas y recalcular; comprobar tramos fechados en GIS. Quedar dentro de una elipse no confirma una vía. Estar fuera refuta solamente el escenario de longitud, no la existencia del camino.

## Material reproducible
Generados localmente: prediccion_geometrica.py, test_prediccion.py, predicciones_g144.json, predicciones_g144.csv, envolventes_condicionales_epsg25830.geojson (no lat/lon), escenarios_geometricos_g144.png, paquete ZIP. 12/12 pruebas pasadas. Sin publicar camino en web, sin alterar Core.

Fuente geometría defensiva: https://doi.org/10.3989/aespa.1998.v71.274 ; referencias de puntos previamente auditadas G143.

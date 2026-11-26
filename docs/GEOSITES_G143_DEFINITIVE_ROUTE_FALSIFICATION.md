# GeoSites G-143 — Prueba definitiva de continuidad (430–350 a. C.)

**Fecha:** 2026-11-22. **Coste 0 €.** Veredicto final del contraste disponible: **CAMINO NO DEMOSTRADO**, no descartado como inexistente.

## Tres fuentes contrastadas
1. Moret y Badie (1998), DOI https://doi.org/10.3989/aespa.1998.v71.274: calle R2 excavada 1995 se dirige a puerta NE; un foso de 5–6 m en coronación rodea el recinto. No se identificó cruce fechado que conectara la puerta con terreno exterior.
2. UA (12-12-2025), https://web.ua.es/es/actualidad-universitaria/2025/diciembre2025/8-14/la-identificacion-de-la-puerta-sureste-de-ilici-por-investigadores-de-la-ua-transforma-el-conocimiento-sobre-la-ciudad-iberica-de-la-alcudia.html: puerta SE monumental siglo IV a.C. de 2,60m sobre acceso anterior siglo V a.C. No demuestra llegada de camino desde La Picola.
3. Moratalla (2015), DOI https://doi.org/10.7203/SAGVNTVM.47.5225: traza Camino del Molar documentada; origen protohistórico hipotético y autor reconoce que sin intervención arqueológica su fecha no puede confirmarse indudablemente.

## Prueba matemática
Dos referencias no-puerta en EPSG:25830:
- Picola BIC A1 (713265,4230490)
- La Alcudia Termas Orientales (701823.285,4234872.059)
Delta E=-11441.715m; delta N=+4382.059m. Distancia euclidiana 12252.154m, azimut 290.956°; NO longitud del camino ni posición de puertas.

## Dos cadenas, ninguna acreditada
- **Litoral:** R2 → cruce del foso → paleoterreno → corredor litoral → Ilici SE. Cruce y geometría del terreno no demostrados.
- **Interior vía Molar:** R2 → cruce del foso → paleoterreno → corredor interior → Molar → Ilici SE. Además del cruce y paleoterreno, datación 430–350 a.C. de Molar no acreditada.

Todos los requisitos para aceptar deben ser simultáneos: geometría georreferenciada, cronología de uso compatible con un mismo periodo, transitabilidad, estructura de cruce con evidencia independiente y continuidad de segmentos. El motor G143 marca **desconocido/no demostrado** si falta prueba. El umbral local de cobertura de los 80 años es deliberadamente conservador y NO permite rechazar la posibilidad histórica de una vía utilizada solo durante una fracción de ellos.

## Evidencias faltantes de más valor
1. Planta georreferenciada identificando puerta NE, huella/obra de salida y tramo transitable del foso.
2. Paleotopografía fechada con control estratigráfico y coordenadas reales.
3. Segmentos materiales excavados y datados del corredor y llegada a la puerta SE, con enlace independiente.
4. Orientaciones desde puntos arqueológicos, no desde perímetros BIC o termas romanas.

## Reproducibilidad
Dos scripts en esta rama: src/iberos/route_definitive_g143.py y tests/test_route_definitive_g143.py. Paquete local con un modelo más estricto de pruebas unitarias 12/12, JSON, CSV y este dictamen. Capturas gráficas PDF de Moret-Badie y Moratalla fallaron por cache miss; no se dice haber digitalizado sus figuras. Las fotos modernas del usuario fueron analizadas en G139–G141 y no contienen puntos de control cartográficos.

**Resultado científico:** no se puede afirmar un camino La Picola–Ilici de 430–350 a.C. y tampoco afirmar que no existiera. La hipótesis se mantiene contrastable; las coincidencias de extremos no equivalen a confirmar un itinerario. No fusionar main ni modificar el Core epigráfico.
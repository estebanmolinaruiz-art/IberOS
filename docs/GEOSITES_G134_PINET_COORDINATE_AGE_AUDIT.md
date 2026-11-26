# GeoSites G-134 — cotejo de Pinet y edades sin interpolación arbitraria

**Fecha:** 2026-11-14. **Coste adicional 0 €**. Pruebas locales: **7/7**.

## Discrepancia geográfica confirmada en las fuentes
Tesis Blázquez Morilla 2003, p. 107: **Pinet 30SYH081 278**.
Artículo Blázquez y Usera 2010, tabla 1 p. 70: **Pinet 30SYH079 269**.

Decodificación de cuadrículas 100x100 m, sin conversión de datum:
- Centro 2003: (708150, 4227850).
- Centro 2010: (707950, 4226950).
- Desplazamiento 2010 menos 2003: **(-200, -900) m**.
- Distancia centros: sqrt(200² + 900²) = **921.954 m**.
- Distancia mínima entre celdas completas: sqrt(100²+800²)=**806.226 m**.
- Máxima: sqrt(300²+1000²)=**1044.031 m**.

**Ni una ubicación ni su datum están corregidos o confirmados topográficamente**. Ambas se mantienen separadas. La comparación es una métrica de cuadrículas publicadas, NO precisión SIG definitiva.

## Edades AMS cotejadas (Blázquez y Usera 2010, tablas 2,5,8)
- Salinas 3m: 7550–7620 cal BP, BETA-140894.
- Salinas 7m: 21490–22395 cal BP, BETA-140895.
- Pinet 2m: 13360–13640 cal BP, BETA-140892.
- Mórtoles 2.7m: 10180–10240 cal BP, BETA-140890.

Periodo buscado: 430–350 a.C. ~2379–2299 cal BP. **Cero solapamientos** con los cuatro registros AMS. La ausencia de solapamiento NO prueba que el sondeo no tenga sedimentos contemporáneos: los puntos de muestreo disponibles son escasos y discontinuos.

El artículo presenta facies superiores holocenas, pero **una facies sin edad calibrada y controles de persistencia no permite clasificar un polígono de 430–350 a.C.**. Cita depósitos de playa asociados indirectamente a un registro de 3290 BP en trabajos previos, que tampoco equivale a datar una ruta o toda una paleolaguna.

## Control documental adicional
Se intentó capturar la página del PDF de la tesis mediante visor, que devolvió fallo de caché. El cotejo se realizó desde texto indexado original y copia legible de lectura del artículo; el contraste visual facsimilar y datum quedan pendientes.

Resultado de G-134: 0 nuevos polígonos de tierra emergida o agua acreditados, sin rutas históricas inferidas. El módulo local reproducible se empaqueta junto a siete pruebas y datos JSON/CSV, **no se ha fusionado aún** al Core epigráfico.

Fuentes:
- https://roderic.uv.es/bitstream/10550/15135/1/blazquez.pdf
- https://www.academia.edu/30244162/Palaeoenvironments_and_Quaternary_foraminifera_in_the_Elx_coastal_lagoon_Alicante_Spain_
- https://doi.org/10.1016/j.quaint.2009.06.033

Siguiente dato crítico: mapa de localización original con control geodésico para Pinet, más series de edades calibradas y perfiles en los primeros metros de los tres sondeos.

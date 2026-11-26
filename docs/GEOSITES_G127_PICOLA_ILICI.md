# GeoSites G-127: auditoría de corredores La Picola → Ilici

## Objetivo
Evolucionar GeoRoutes con un grafo documental GeoSites de los tramos de
investigación entre la puerta noreste de La Picola y la puerta sureste
de Ilici. NO reutilizar mapas modernos como paleocaminos ibéricos.

## Desglose del caso y falsaciones
1. Referencia BIC Picola → puerta NE: no equivale a dos coordenadas de acceso.
2. Puerta NE → exterior del foso: falta paso excavado y datación específica.
3. Foso → corredor intermedio: falta paleoterreno emergido y pasos fechados.
4. Corredor intermedio → Camino del Molar: trazado antiguo no documentado.
5. Camino del Molar → puerta SE Ilici: falta medir la coincidencia geométrica
   con el centro del vano; antigüedad V–IV a. C. no demostrada.
6. Puerta SE → referencia arqueológica Alcudia: referencia moderna no es
   coordenada de puerta.

## Resultado reproducible G-127
- 6 conexiones documentales/hipotéticas evaluadas.
- 0 conexiones con **simultáneamente** fuente, geometría comprobada,
  evidencia de tránsito y periodo completo 430–350 a. C.
- Por tanto, 0 cadenas certificadas entre ambas referencias; se produce
  abstención en vez de fabricar un itinerario.
- Distancia recta de dos referencias **que no son ambas las puertas**:
  12.252,154 m. NO es recorrido terrestre.
- Cualquier tramo de agua/foso exige una fuente arqueológica específica
  de cruce; un tramo restituido nunca puede elevarse automáticamente.

El motor trabaja con años astronómicos -429 a -349 (430–350 a. C.)
y con clases observada/restaurada/inferida/desconocida. Acepta solo
observación con evidencia de tránsito, cronología que abarque el
intervalo, geometría verificada y cruce acreditado cuando exista barrera.
Incluso una cadena admisible no demuestra por sí sola una carretera
histórica ni función militar/comercial.

## Ejecución gratuita
```bash
python -m unittest discover -s tests -p 'test_geosites_corridors.py'
python scripts/picola_geosites_g127.py
```

La prueba de desarrollo del módulo independiente pasó 8 pruebas locales.
Las comprobaciones de integración en GitHub Actions se consultan por
separado tras el commit.

Fuentes: Moret y Badie 1998 (doi:10.3989/aespa.1998.v71.274),
Moratalla Jávega 2015 (doi:10.7203/SAGVNTVM.47.5225),
noticia UA de excavación de puerta SE (2025), y referencias
cartográficas BIC Picola / Termas Orientales Alcudia.

## Próxima evidencia que modifica la conclusión
Captura métrica de la figura 3 y de la planta del Plan Director para
identificar un corte del foso ante la puerta NE, con unidades
estratigráficas. En paralelo, georreferenciar puerta SE Ilici y traza
del Molar. Obtener paleocostas y lagunas 430–350 a. C.

**Coste adicional obligatorio: 0 €.** No hay cambios en las métricas
del Core epigráfico ni subida a web pública.

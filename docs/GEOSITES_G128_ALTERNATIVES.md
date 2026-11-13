# GeoSites G-128 — corredores alternativos La Picola–Ilici

**Premisa permanente:** 0 € de gasto adicional, solo fuentes abiertas y herramientas gratuitas.

Se comparan dos **hipótesis de investigación**, no dos caminos encontrados:
- franja litoral, desde la puerta NE de La Picola hacia Ilici;
- franja interior, desde La Picola hacia el entorno del Camino del Molar y la puerta SE de Ilici.

El motor `src/iberos/geosites_alternatives.py` exige para cada segmento
observación directa, fuente, cronología compatible con todo el intervalo
430–350 a. C. (años astronómicos -429 a -349), geometría verificada,
evidencia de tránsito y longitud medida con procedencia. Para laguna,
estuario, río, foso y terreno inundable se exige además un paso acreditado.
Elementos restituidos, inferidos o terreno desconocido NO son transitables.

El caso real registrado se abstiene: **0 de 2 corredores evaluables**.
No se han inventado celdas paleoambientales, líneas sobre el mapa ni
probabilidades de existencia. Ningún éxito de algoritmo por sí solo
demuestra una carretera antigua.

La siguiente evidencia discriminante sigue siendo material: paso del foso
de La Picola fechado para el periodo; paleosuelo y cruces hidráulicos
fechados entre los dos yacimientos; posición del vano SE de Ilici con
desviación medida respecto al eje del Molar.

Código de reproducción:
```bash
python -m unittest discover -s tests -p 'test_geosites_alternatives.py'
python scripts/picola_geosites_g128.py
```
Fuentes base:
- Moret y Badie 1998: https://doi.org/10.3989/aespa.1998.v71.274
- Moratalla 2015: https://doi.org/10.7203/SAGVNTVM.47.5225
- Expedientes internos GeoSites G-122 a G-127.

No modifica las métricas epigráficas oficiales del Core.

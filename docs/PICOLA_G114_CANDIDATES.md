# G-114 · Recuperación de candidatos y mejora textual GeoRoutes

## Ruta con mejor justificación en el hilo
**Camino del Molar** fue la última pista viaria priorizada (G-99 a G-106)
para la **aproximación sureste a La Alcudia**. Moratalla (2015) documentó
su traza en fotografías de 1929–1930; el hallazgo independiente de la
puerta sureste de Ilici (2025) convierte en testable la coincidencia de sector.

**No es una ruta completa La Picola–La Alcudia** ni está fechada en 430–350
a. C. Su eje se interrumpe aproximadamente 350 m antes del yacimiento;
no existe intersección métrica certificada con el vano de la puerta.

**Camí de Carmahadet** permanece como control de comunicación desde las
salinas hacia Elche, con peor adecuación como acceso ibérico directo a
La Alcudia por su trazado y cronología no acreditada. Una asociación
toponímica con el litoral no constituye prueba contemporánea.

**La Picola**: su puerta nordeste y la calle R2 están documentadas; el
paso exterior del foso y la continuidad con un corredor interior no lo están.

## Función de G-114

- `text_candidates(text)`: recupera términos indicativos para revisión
  humana; no extrae coordenadas, topónimos ni itinerarios fiables por sí solo.
- `prioritize(leads, target_period)`: ordena **prioridades de comprobación**,
  colapsa fuentes dependientes, conserva el control cronológico y rechaza
  tratar puntuaciones como probabilidades históricas.

La comparación de prioridades requiere observaciones con el mismo alcance:
la puntuación de una puerta no puede compararse sin más con un recorrido
completo de 12 km. No introducir al motor conexiones geométricas inferidas
como si hubieran sido observadas.

## Prueba propuesta
1. Georreferenciar el eje publicado del Molar (Moratalla, figs. 9–10).
2. Obtener el centro métrico de la puerta sureste de 2025 y sus unidades
   estratigráficas.
3. Medir separación perpendicular y error de ambos georreferenciados.
4. Para La Picola: comprobar foso y acceso exterior con las plantas revisadas.
5. Entre ambos puntos: reconstruir terreno firme y cruces con fechas.
6. Contrastar las trazas de época romana/medieval como controles
   y **no** retrodatarlas.

Lecturas:
- https://doi.org/10.7203/SAGVNTVM.47.5225
- https://web.ua.es/es/actualidad-universitaria/2025/diciembre2025/8-14/la-identificacion-de-la-puerta-sureste-de-ilici-por-investigadores-de-la-ua-transforma-el-conocimiento-sobre-la-ciudad-iberica-de-la-alcudia.html
- https://www.persee.fr/doc/palla_0031-0387_1997_num_46_1_1428

Comandos:
```bash
python -m unittest discover -s tests -p 'test_route_prioritization.py'
python scripts/picola_route_g114.py
```

Sin modificaciones al Core epigráfico ni publicación web; cero costes.

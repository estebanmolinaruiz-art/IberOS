# SEGMENT-36 — Auditoría de estabilidad de subdivisiones en Moleta

Fecha: 2026-11-22. Ejecución comprobada: [GitHub Actions #45069966219](https://github.com/estebanmolinaruiz-art/IberOS/actions/runs/45069966219), **SUCCESS**.

## Procedimiento
Se regeneraron desde la publicación original las figuras 4 y 5 de Moleta del Remei (SEGMENT-34) y las siete bandas de tinta candidatas (SEGMENT-35). Para cada banda se probaron tres binarizaciones independientes (`Otsu`, `adaptativa gaussian 31`, `adaptativa gaussian 51`); se localizaron corredores de baja densidad en proyección horizontal y se retuvieron solo separadores presentes, dentro de tolerancia, en **las tres** representaciones. No se usaron etiquetas fonéticas, posiciones editoriales de Orleyl ni límites de signo inventados.

| Banda | Propuestas Otsu / A31 / A51 | Consenso |
|---|---|---:|
| Fotografía 4 B01 | 0 / 0 / 0 | 0 |
| Fotografía 4 B02 | 4 / 0 / 0 | 0 |
| Dibujo 5 B01 | 0 / 0 / 0 | 0 |
| Dibujo 5 B02 | 0 / 0 / 0 | 0 |
| Dibujo 5 B03 | 0 / 0 / 0 | 0 |
| Dibujo 5 B04 | 0 / 0 / 0 | 0 |
| Dibujo 5 B05 | 1 / 0 / 0 | 0 |

**Resultado:** 7 bandas examinadas, **0 separadores interiores estables**. El fracaso del consenso no demuestra ausencia de renglones: indica insuficiencia de este método sobre estos recortes y umbrales.

**Puertas científicas:** cero renglones comprobados visualmente por un revisor independiente, cero grafemas acreditados, cero tasa de segmentación externa, cero traducciones. La mejora retrospectiva 35/43 de SEGMENT-32 **no está validada fuera de Orleyl**. La dependencia de contraste y tinta probablemente obliga a pasar a geometría de trazos/inspección de la imagen original y correspondencia foto-dibujo; esa explicación es una hipótesis de ingeniería, no prueba.

## Artefactos y seguridad
Código: `research/core_association/segment36_moleta_stability.py`; resultados completos `report.json`, `candidate_subdivisions.csv` y vistas temporales de las figuras anotadas en artefacto [14772782746](https://github.com/estebanmolinaruiz-art/IberOS/actions/runs/45069966219/artifacts/14772782746) (retención de un día). No redistribuir figuras bajo licencia CC BY-NC-ND fuera de investigación interna.

**Siguiente cambio metodológico necesario:** visualizar y registrar manualmente las regiones que contienen escritura, anclarlas en foto y dibujo y congelar límites antes de utilizar el segmentador. No seguir afinando umbrales contra las mismas siete bandas sin referencia independiente.

Core, FULL3406, C594/C474/C539/C541 sin cambios. Coste adicional 0 €.

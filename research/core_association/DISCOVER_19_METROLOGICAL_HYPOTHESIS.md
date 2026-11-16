# DISCOVER-19 · Auditoría estadística y prioridad metrológica (2026-11-16)

**Resultado: análisis exploratorio, NO traducción ni prueba de logografía.** Core/FULL3406/C594/C474/C539/C541 intactos. Coste adicional 0 €.

Se reanalizó `IBEROS_FULL_LINE_ALIGN_17/aligned_slots.csv` (Orleyl V y Orleyl VII-B, dos líneas; las 69 lecturas son **editoriales condicionadas**, no signos identificados de fotografía).

Se repitió el análisis de n-gramas de 2, 3 y 4 tokens, con **20.000 permutaciones por cada modelo nulo** (global dentro de cada objeto, y restringido dentro de cada grupo puntuado). Se hizo corrección Bonferroni por las tres longitudes. No se ha corregido la selección retrospectiva de material/hipótesis; los p no implican resultados prospectivos.

| Longitud | N. de secuencias compartidas | p global | p restringida | p restringida × 3 |
|---|---:|---:|---:|---:|
| 2 | 7 | 0,016299 | 0,037648 | 0,112944 |
| 3 | 2 | 0,013649 | 0,031948 | 0,095845 |
| 4 | 0 | 1 | 1 | 1 |

Al excluir grupos enteros que contienen el valor editorial `W` (aún sin correspondencia paleográfica confirmada), solo persiste el triple `A-R-I`. Dejar fuera cualquier grupo completo produce entre uno y dos triples, indicando sensibilidad a la muestra. No hay validación de significado.

## Cambio de objetivo experimental

Una fuente académica independiente ya documenta usos de signos/elementos gráficos en **sistemas metrológicos y monetales ibéricos**, que no deben confundirse con logografía general:

Ferrer i Jané, J., y Moncunill, N. (2019), *Palaeohispanic Writing Systems: Classification, Origin, and Development*, §2.6 (https://diposit.ub.edu/dspace/bitstream/2445/145739/1/Chapter_4._Palaeohispanic_writing_syste.pdf).

Los grupos de barras indican cantidad; ciertos signos `a/o/ki/e/be/l/ti/ḿ/ka` **podrían** funcionar como abreviaturas de unidades; el signo en L y las marcas fraccionarias exigen una ontología gráfica distinta del silabario. **Estas propuestas pertenecen a la bibliografía y no son hallazgos de IberOS.**

**Candidatos documentales para verificar en nuevos objetos:** F.17.1 (Villares), V.13.02 (Iàtova), monedas de undikesken y śaitabi, inscripciones de ánforas de Vieille-Toulouse. No se han recuperado nuevas fotografías ni fijado predicciones de esos objetos en este turno.

Cuatro modelos a comparar con blind HOLD por PHYS_ID: fonético convencional; abreviatura de unidad/medida; logograma de palabra; marca no lingüística. Para elegir entre abreviatura y logograma se exigen usos contextuales **fuera de notación de cantidades** y contexto externo acreditado; ningún éxito derivado de transcripción editorial se convierte automáticamente en oro semántico.

**Artefacto reproducible generado localmente:** `IBEROS_DISCOVER_19.zip`, con `audit.py`, `results.json`, `leave_one_group_out.csv`, `PROTOCOLO.md` y `README.md`; integridad ZIP verificada. Ningún archivo del Core modificado.

# IberOS CORE — Programa integrado de seis pilares (2026-10-20)

**Regla central:** no promover traducciones, morfemas ni continuidad simbólica sin prueba independiente. La presencia de archivos es cobertura de infraestructura, no resultado científico.

## Mapa de reutilización (sin duplicar hilos)
1. **Paleografía:** reutilizar `data/review/orleyl_te_glyph_review_v1.json`, controles Moleta y cola de signarios. Prioridad: imágenes con hash, cajas por signo, variantes, revisión doble.
2. **Hipótesis lingüísticas:** reutilizar `src/iberos/semantic_hypothesis_engine.py`, `rule_catalog.py`, `prediction_compare.py`. Prioridad: hipótesis versionadas, predicciones pre-registradas y condiciones de refutación.
3. **Tradición simbólica:** reutilizar `src/iberos/multimodule.py` y signarios; crear vínculos con soporte, cronología y región sin inferir automáticamente continuidad cultural.
4. **Validación independiente:** conservar `VALIDATION-01`, los controles HOLD y baselines. Evitar filtración de las respuestas al entrenamiento.
5. **Corpus:** mantener `data/curated/iberos_curated_objects_v1.jsonl` como registro auditado de partida; controles de ID, fuente y procedencia; no equiparar bibliografía con inscripciones independientes.
6. **Laboratorio:** reutilizar CLI, `validation01_pipeline.py`, exportaciones y fichas. Resultado deseado: informe con fuentes, versiones, incertidumbre, falsadores y controles.

## Entregable técnico de esta tanda
`python scripts/audit_core_six_pillars.py --out data/review/core_six_pillar_audit_latest.json`
Pruebas: `python -m unittest discover -s tests -p 'test_audit_core_six_pillars.py'`.

El script produce un diagnóstico reproducible sobre la copia local del repositorio. No escribe resultados de investigación válidos por sí solo ni cambia la autoridad del motor. Evitar subir informes derivados de copias desactualizadas.

## Gates, por orden
A. Trazabilidad y normalización del corpus
B. Identificación de signos revisada a doble ciego cuando proceda
C. Hipótesis con evidencia independiente y variantes alternativas
D. Predicciones preinscritas y HOLD inmune a filtraciones
E. Resultado comparado frente a baseline y controles negativos
F. Ficha del laboratorio con replicación y revisión externa

## Caso piloto
`ORL-GLYPH-MAP-01` y `VALIDATION-01`: localización de `BASBITEROKETINE`, comparación con `BITEROKETETINE`, y TE-MASK. Los hilos no deben reabrir recortes o transcripciones históricas sin evidencia nueva.

## Estado honesto
Instrumentación transversal creada; no se afirma ejecución validada de tests, integración a la web, verificación gráfica independiente o regla lingüística descubierta. `ROK-RECIPIENT-02` sigue OPEN.

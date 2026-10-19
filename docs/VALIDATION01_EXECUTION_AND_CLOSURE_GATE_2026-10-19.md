# VALIDATION-01 — Plan de ejecución hasta dictamen científico (2026-10-19)

## Dictamen actual
**NOT_EVALUATED**. El conjunto `data/review/validation01_holdout_v1.csv` contiene 0 observaciones. La tabla `data/review/validation01_te_tokenized_review_v1.csv` tiene 0 lecturas independientes auditadas. Los 20 objetos de screening son retrospectivos, no se pueden convertir en HOLD intacto por renombrarlos.

## Objetivo científico: evitar la tautología
No basta predecir que una transcripción contiene el signo `te` si la etiqueta gold es «la transcripción contiene te». Eso sería reconocimiento/lectura, no una predicción de una regularidad lingüística. La tarea específica debe especificar antes de ver HOLD una **variable contextual independiente y observable** de los tokens de entrada (p. ej., un criterio editorial independiente de posición/función estructural, definido inequívocamente), sin ambigüedad interpretativa.

## Secuencia de cierre estricta
**FASE A — definición falsable**. Definir unidad de predicción, criterios de verdad, ventanas, abstenciones, población elegible, baseline y diferencia mínima relevante. Registrarlo en `data/review/validation01_preregistration_v1.json`. Estado actual: DRAFT_NOT_FROZEN.

**FASE B — lecturas**. Usar `validation01_te_tokenized_review_v1.csv`: identidad de objeto, grupo físico, edición, línea completa y signos atómicos, revisor sin acceso a predicciones. `te` no equivale a caracteres `t` + `e`. Dos lecturas del mismo objeto no cuentan como unidades independientes.

**FASE C — split y blindaje**. Excluir del HOLD objetos utilizados en desarrollo y cribado; mínimo de 20 grupos físicos nuevos según protocolo actual. No incluir copias ni reediciones duplicadas; custodiar versiones originales y fuentes. Cerrar por hash y tiempo las predicciones del Core y baseline **antes** de adjudicar etiquetas gold.

**FASE D — evaluación**. Auditar primero `scripts/validation01_readiness.py` y luego `scripts/validation01_blind_score.py`. Publicar la tabla de contingencia, tasa de abstención, métricas por clase y diferencias con incertidumbre. La herramienta de scoring actual ofrece métricas descriptivas; para una reivindicación de superioridad se requerirán método inferencial y replicación fijados antes del HOLD.

**FASE E — veredicto**. Resultado solo como: `BLOCKED/NOT_EVALUATED` (sin evidencia suficiente), `EVALUATED_NOT_SUPERIOR`, o `EVALUATED_SUPPORTIVE_PENDING_REPLICATION`; **VALIDATED** solo con replicación y revisión independientes según preregistro.

## Tareas inmediatas, orden de prioridad
1. Definir predicción estructural concreta con criterio de verdad no tautológico. Requiere criterio científico explícito.
2. Adquirir 20+ inscripciones nuevas elegibles con datos gráficos y transcripción editorial controlada, sin uso previo.
3. Cotejar líneas con edición física y designar revisor gold independiente.
4. Congelar reglas y compromiso criptográfico y evaluar después.

El inventario de 286 códigos y 15 variantes te es recurso paleográfico, **no** observación HOLD ni prueba de semántica.

Comprobación:
```bash
python scripts/validation01_readiness.py
pytest -q tests/test_validation01_readiness.py
```

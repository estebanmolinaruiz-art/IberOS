# VALIDATION-01 — Endurecimiento de identidad física / anti-duplicados (22 octubre 2026)

## Riesgo
Las grafías alternativas, la puntuación y los identificadores editoriales distintos pueden referirse a un mismo objeto físico. Si llegan a TRAIN/VAL y HOLD se produciría fuga de información.

## Implementación
1. `scripts/validation01_identity.py` aplica NFKD, elimina diacríticos, mayúsculas y signos de puntuación y usa un diccionario **conservador** de alias documentados: `F.9.5`↔Orleyl V, `F.9.7`↔Orleyl VII. No usa similitud difusa ni presupone equivalencia entre piezas.
2. `scripts/validation01_hold_leakage_guard.py` coteja tanto `object_id` como `physical_group` del candidato con ambos campos en el cribado y líneas críticas; detecta duplicidades dentro de HOLD y conflicto entre alias declarados.
3. `scripts/validation01_blind_score.py` usa las mismas identidades normalizadas para rechazar fugas entre TRAIN/VAL/HOLD y grupos repetidos dentro de split; el mínimo HOLD usa identidad normalizada del grupo físico.
4. Pruebas: `tests/test_validation01_identity.py` siete casos del detector; `tests/test_validation01_blind_score_alias.py` tres escenarios de integración.

## Ejecución y límites
La **versión local del nuevo detector superó 7/7 pruebas**. Los tres escenarios añadidos de integración se han registrado en GitHub, pero su ejecución de CI no ha sido verificada todavía.

La normalización no constituye una autoridad arqueológica: una coincidencia homógrafa puede producir falso positivo y un alias desconocido puede escapar. El estado `PASS_KNOWN_OBJECT_SCREEN` significa únicamente que el cotejo de identidades **conocidas** no encontró conflicto, NO confirma novedad física. Antes de admitir HOLD hacen falta fotografía, procedencia, signatura y revisión humana con identidad física inequívoca.

## Estado científico
M06 PENDING, M07 PENDING, 0 HOLD independientes, VALIDATION-01 NOT_EVALUATED, 30% preparación administrativa. Ninguna puntuación de validación alterada por una mejora técnica.

# VALIDATION-01 — Resultado intermedio auditable (2026-10-19)

## Pregunta
¿Puede IberOS predecir una regularidad estructural ibérica no usada durante el diseño mejor que un baseline?

**Respuesta actual: NO DEMOSTRADO; prueba prospectiva sin datos evaluables.**
Esto NO significa que la hipótesis sea falsa: aún no se ha realizado una comparación prospectiva.

## Evidencia auditada
- `data/curated/iberos_curated_objects_v1.jsonl`: 38 objetos, 20 `INCLUDE`; el auditor inicial no encuentra en ese archivo 20 conjuntos completos de transcripción verificada + identidad física + compromiso prospectivo + etiqueta independiente.
- `data/review/iberos_visual_matcher_manifest_v08.csv`: contiene solamente cabecera; 0 ejemplos visuales etiquetados para evaluación.
- `data/review/validation01_holdout_v1.csv`: contiene solamente cabecera; 0 predicciones ciegas para puntuar.
- La documentación de benchmark declara 37 unidades documentales independientes, pero ninguna equivale automáticamente a un HOLD prospectivo.

## Software
- `scripts/validation01_eligibility.py`: audita requisitos de entrada.
- `scripts/validation01_blind_score.py`: bloquea muestras vacías, fugas de grupos, lecturas no revisadas, etiquetas ausentes, predicciones sin compromiso y posterioridad temporal; solo computa estadísticas descriptivas sobre muestras admitidas.
- `tests/test_validation01_blind_score.py`: tres pruebas de seguridad declarativa.

## Condiciones de un resultado publicable
1. Formular una predicción específica, sin redefinirla después.
2. Congelar reglas de IberOS y baseline A/B, selección de grupos y tamaño de muestra antes de inspeccionar etiquetas HOLD.
3. Recoger inscripciones y transcripciones con procedencia primaria, segmentación y revisión independiente; evitar copias del mismo objeto.
4. Congelar predicciones mediante artefactos verificables y firma temporal antes de la revisión gold.
5. Comparar acierto y abstenciones con sensibilidad/especificidad, intervalos por grupo, control de clases y contrastes preregistrados.
6. Validación replicada en otro conjunto independiente, cuando exista tamaño suficiente.

Ningún test de software debe convertirse automáticamente en una afirmación de traducción ni en una validación semántica.

## Limitaciones actuales
El evaluador binario es un primer andamio para pruebas estructurales; no es un motor de entrenamiento, no ha aplicado validación de significación estadística, y no mide traducción. El campo `predictions_frozen_sha256` requiere comprobación externa de un artefacto depositado y timestamp confiable para una auditoría científica completa; su mera presencia no acredita por sí sola un compromiso temporal. La marca de revisor independiente también necesita corroboración fuera del CSV.

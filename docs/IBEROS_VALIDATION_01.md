# IberOS-VALIDATION-01 — preregistro y auditoría inicial

Fecha: 2026-10-19
Estado: FASE 1 EJECUTADA (elegibilidad); FASE 2 BLOQUEADA (predicción prospectiva).

## Pregunta
¿Puede IberOS anticipar en documentos físicos independientes una regularidad de distribución de secuencias epigráficas que no haya sido utilizada para ajustar sus reglas, mejor que una línea base simple?

## Alcance falsable
Primera tarea propuesta: predicción binaria predefinida de presencia/ausencia de una secuencia o posición contextual (por ejemplo TE), con segmentación editorial e incertidumbre congeladas ANTES de mirar las muestras de prueba. La mera coincidencia de signos es una predicción estructural, NO una demostración del significado de TE, ni de una función morfológica.

## Conjuntos y fuga
- TRAIN: documentos usados para definición/ajuste de la hipótesis.
- VAL: ajuste de umbral; no reutilizar para confirmar.
- HOLD: nuevos objetos físicos independientes, seleccionados por protocolo publicado antes de conocer sus etiquetas.
- Identidad: PHYS_ID > LEAK_GROUP > Dependency_Group específico > OBJECT_ID.
- Abstenerse si no hay transcripción auditada o lectura editorial suficientemente trazable.
- No convertir automáticamente ninguno de los 38 objetos retrospectivos en prospectivos.

## Comparadores
- Baseline A: tasa mayoritaria de TRAIN para la etiqueta binaria.
- Baseline B: modelo de frecuencia/posición de signos condicionado a longitud y soporte, entrenado SOLO en TRAIN.
- IberOS: regla y versión de algoritmo fijadas antes del HOLD.
- Se informarán cobertura (abstenciones), balanced accuracy, precision/recall para etiqueta positiva, Brier score si hay probabilidades, matriz de confusión e intervalos de confianza por unidad documental independiente.
- Establecer tamaño muestral, umbral y contraste estadístico antes de liberar HOLD. Sin tamaño suficiente, informar descriptivamente y no anunciar éxito.

## Hipótesis
H0: el desempeño de IberOS no mejora al mejor baseline relevante en unidades independientes no vistas.
H1: mejora prospectiva replicable, con intervalo de incertidumbre y criterio preregistrado.
Ningún resultado aislado prueba una traducción o gramática ibérica.

## Auditoría inicial sobre data/curated/iberos_curated_objects_v1.jsonl
Fecha: 2026-10-19; revisión del contenido del archivo a través de GitHub.
- Registros: 38
- Marcados INCLUDE: 20
- INCLUDE con campos suficientes para entrar directamente en scoring prospectivo: 0
- 20 INCLUDE sin transcripción verificada en los campos auditados (verified_transcription/validated_transcription/sign_sequence)
- 20 sin identidad física/leak_group explícita en esos campos
- 20 sin precompromiso (prospective_locked, lock_date, prediction_created_at)
- 20 sin gold_task_label independiente
Estos conteos son SOBRE EL ARCHIVO JSONL CURADO Y LOS CAMPOS SOLICITADOS POR EL AUDITOR, no sobre todas las fuentes de IberOS ni sobre transcripciones existentes en otros archivos. La auditoría de independencia documental del benchmark v1.0.1 (37 unidades) es distinta: no implica 37 unidades HOLD aptas para puntuación prospectiva.

## Estado de respuesta
PREGUNTA: AÚN NO DEMOSTRADO. No es un resultado de inferioridad ni superioridad: no existe todavía prueba ciega evaluable en estos datos.
FASE 1: El auditor de elegibilidad se ha añadido en scripts/validation01_eligibility.py.
FASE 2: Requiere recopilar transcripciones independientes, fijar conjunto HOLD y predicciones, controles, umbrales y fecha de congelación ANTES de la evaluación.
Regla de publicación: prohibido calificar como descubrimiento lingüístico una prueba que solo valida infraestructura o una comparación circular.

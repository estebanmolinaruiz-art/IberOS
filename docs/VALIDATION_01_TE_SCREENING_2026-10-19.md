# IberOS-VALIDATION-01 — TE: screening y preregistro preliminar
Fecha: 2026-10-19. Estado: **RETROSPECTIVE_SCREENING_COMPLETE; PROSPECTIVE_HOLD_NOT_ASSEMBLED**.

## Pregunta de predicción
¿Puede una regla IberOS fijada antes de revisar nuevos testimonios predecir una propiedad observacional de la distribución del valor silábico **te** mejor que predictores basados en frecuencia y longitud?

**No se propone ni se afirma que TE posea función morfológica demostrada.** La definición exacta de la etiqueta binaria, posición, ventanas de contexto, unidad de análisis y reglas de normalización sigue **SIN CONGELAR**. Por tanto no puede emitirse una predicción ciega válida.

## Selección inicial
Fuente: `data/curated/iberos_curated_objects_v1.jsonl` a fecha de este informe.
- 38 objetos de colección, 20 `INCLUDE` examinados como pantalla de selección; 20/20 **NO** son actualmente HOLD prospectivo.
- Los documentos ya presentes en el corpus y las discusiones de Orleyl, Pech-Maho y Tivissa no pueden etiquetarse retrospectivamente como pruebas ciegas.
- `research/protocols/ORLEYL-CROSSCHECK-MATRIX-2026-10-18.csv` contiene una entrada `TE-MORPH-01` **sin objeto asignado, signo localizado ni lectura verificada**.
- Las familias temáticas de las fichas no demuestran que TE figure o no figure en ellas.

El archivo `data/review/validation01_te_screening_2026-10-19.csv` enumera cada objeto y su condición; `NOT_ASSESSED` no equivale a ausencia de te. Ningún caso es positivo, negativo, o candidato HOLD puntuable sin revisión adicional.

## Pasos necesarios antes del lock
1. Elegir UNA etiqueta observable exacta y reproducible (no un significado). Definir cómo tratar alternancias duales, lagunas, segmentaciones y lecturas múltiples.
2. Registrar la versión y hash del motor, baseline A mayoritario y baseline B dependiente de longitud/posición. Evitar entrenar sobre objetos relacionados físicamente o por calco.
3. Seleccionar fuentes con transcripciones completas y cotejo de un revisor independiente; separar TRAIN, VAL y HOLD según objeto físico y tradiciones editoriales.
4. Seleccionar de antemano tamaño y clase mínima para cada grupo, regla de abstención, métricas, contraste e intervalo. El umbral provisional del evaluador (20 objetos HOLD) es un guardarraíl técnico, **no** una justificación de potencia estadística.
5. Congelar predicciones de IberOS y baselines en fichero sellado temporalmente ANTES de adquirir o abrir las etiquetas gold HOLD.
6. Registrar fuentes y licencias para cada imagen; separar una prueba visual de una prueba lingüística.

## Condiciones de fracaso, abstención y éxito
- Si no hay cobertura suficiente o datos independientes: **NO EVALUABLE**, nunca superioridad.
- Si se incumple el preregistro o se abren etiquetas antes del lock: análisis **exploratorio**, no confirmatorio.
- Solo una mejora preregistrada e independiente frente a ambos baselines, acompañada de intervalos y replicación, permitiría una afirmación acotada a **predicción estructural**, no traducción.

## Resultado a 2026-10-19
`HOLD_OBJECTS=0`; `BLIND_PREDICTIONS=0`; `TE_SIGN_ATTESTATIONS_INDEPENDENTLY_REVIEWED_IN_THIS_SCREENING=0`.
`VERDICT=NOT_EVALUATED`.

# IberOS — Auditoría de cierre de VALIDATION-01 y tabla Cathalaunia v5
Fecha 2026-10-19. Decisión: **VALIDATION-01 NO CERRADO COMO VALIDADO**; preparativos y catálogo fuente ampliados.

## Evidencias nuevas
La tabla `data/review/cathalaunia_signary_source_codes_v5_2026-10-19.csv` registra 286 filas de correspondencia entre **código de fuente**, **carácter usado por iber.ttf** y **etiqueta de variante del signario Cathalaunia**. Fuente https://cathalaunia.org/Iberika/Signari.
- 286 códigos fuente recuperados; no equivale a 286 signos distintos fonológicamente ni a 286 transcripciones independientes.
- Los campos `sign_value` y `reviewer` permanecen vacíos para evitar promoción sin acuerdo editorial y control de variantes. `review_status=SOURCE_ATTESTED_NOT_INDEPENDENTLY_REVIEWED`.
- La correspondencia es específica a iber.ttf v5.0 de Cathalaunia; no utilizar como tabla de conversión para el signario de Carme J. Huertas.
- Códigos con denominaciones `?`, alternativas con `/`, múltiple variante y signos de puntuación/metrología exigen resolución manual. No asumir 'te' por semejanza.
- La tabla es utilizable para trazabilidad y posterior revisión editorial, **no** habilita conversión automática de inscripciones a lectura auditada.

## Auditoría de VALIDATION-01
Evaluación confirmatoria de regularidad contextual TE:
- Pregunta falsable general: formulada.
- Regla predictiva específica y ventana de etiqueta previamente congeladas: **NO**.
- Baseline B entrenado exclusivamente en TRAIN: **NO**.
- Corpus HOLD prospectivo, con separación física y editorial, predicciones selladas antes del gold: **0**.
- Lecturas de TE y ausencias revisadas signo a signo por editor independiente y ligadas a un objeto físico para este experimento: **0**.
- Estadística de resultado ciego, intervalo y replicación: **NO DISPONIBLES**.

**Veredicto: NOT_EVALUATED.** No existe fundamento científico para declarar VALIDATION-01 completado, positivo o negativo. Puede darse por cerrada la subtarea de **inventario del signario fuente**, no su revisión ni el experimento lingüístico.

## Próximas acciones científicamente necesarias
1. Registrar atribución por cada variante (a/e/i/o/u, sonantes y silabogramas), excluir signos dudosos y funciones no silábicas del mapeo automático.
2. Verificar equivalencias visuales con el signario de origen por un segundo revisor; fuente diferente = tabla independiente.
3. Conseguir corpus de transcripciones con grafía/variantes preservadas, procedencia, identidad física y cotejo editorial.
4. Congelar una predicción de TE explícita y un baseline entrenado sin exposición a HOLD.
5. Capturar etiquetas gold de otro equipo tras el sellado temporal; evaluar cobertura, aciertos e incertidumbre antes de informar resultado.

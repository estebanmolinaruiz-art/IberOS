# IberOS — Primer lote externo de lecturas codificadas (2026-10-19)

## Resultado material
Se han incorporado **12 registros epigráficos de procedencia identificada** del corpus público Cathalaunia/Ibèrika a:
`data/review/validation01_external_opaque_readings_batch01.csv`.
Cada fila guarda referencia editorial, tipo de soporte, identificador de fuente, enlace permanente y **extracto breve de la transcripción codificada que presenta el sitio**.

**No son 12 lecturas ibéricas transliteradas y verificadas.** El sitio trabaja con fuente epigráfica propia (`Iberika/Signari`, 286 signos). Sus caracteres de pantalla (p. ej. `Ȁ`, `Ƅ`, `9`) no pueden interpretarse directamente como letras latinas. La columna `te_status` permanece `UNKNOWN`.

## Procedencia y licencia
- Índice: https://cathalaunia.org/Iberika/Iberika
- Tabla de glifos y códigos de fuente: https://cathalaunia.org/Iberika/Signari
- Corpus de Folch Flórez: https://www.ibers.cat/corpuseng.html
- Folch Flórez publica su corpus bajo CC BY-NC-SA 3.0; verificar condiciones de cualquier descarga y atribuir autores. No se ha incorporado el archivo Excel completo ni se ha redistribuido la fuente `iber.ttf`.
- Los extractos de Cathalaunia se han conservado para identificación documental y control técnico, no como versión reproducible del corpus completo.

## Estado científico de los 12 casos
- Proveniencia enlazada: 12
- Transliteración a valores atómicos verificadamente descodificada: **0**
- Lecturas de TE afirmadas: **0**
- Ausencias de TE afirmadas: **0**
- Unidades HOLD: **0**
- Transcripciones revisadas gráficamente por revisor independiente: **0**

## Para aumentar el corpus de manera responsable
1. Obtener fichero fuente directamente de su autor o repositorio bajo términos de licencia adecuados. No adivinar el valor de signos personalizados a partir de caracteres ASCII o Unicode.
2. Construir una tabla de conversión de los 286 glifos desde el propio signario y someterla a revisión independiente sobre un lote de control.
3. Registrar lineas, alternativas tipográficas de duda, identidad física, caras y estado de lagunas. Las entradas numismáticas, ediciones y duplicados deben agruparse.
4. Normalizar SOLO después de revisar código-fuente y edición. Enviar las líneas a `validation01_te_tokenized_review_v1.csv` en secuencias atómicas, con procedencia.
5. Mantener el corpus público conocido en DEVELOPMENT o RETROSPECTIVE_SCREENING. HOLD prospectivo debe ser independiente y registrado antes de revelar resultados.
6. Aumentar mediante lotes auditables con conteos por objetos, no con 'número de letras' ni copias de una misma matriz física.

## Automatización
`python scripts/validation01_opaque_corpus_audit.py data/review/validation01_external_opaque_readings_batch01.csv`

El auditor bloquea la clasificación TE de textos de fuente no descodificada y las declaraciones de elegibilidad prospectiva. La validación informativa del corpus no equivale a desciframiento lingüístico.

## Próximo punto de decisión
La **descodificación documental legítima del corpus fuente** es el factor limitante principal. Hasta entonces es preferible conservar 12 registros sin etiquetas a crear miles de lecturas falsas.

Resultado VALIDATION-01: **NOT_EVALUATED**.

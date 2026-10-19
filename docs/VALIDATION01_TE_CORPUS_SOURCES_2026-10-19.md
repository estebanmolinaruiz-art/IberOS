# VALIDATION-01 — localización de fuentes e importación TE (2026-10-19)

## Corpus externos localizados
- Hesperia: http://hesperia.ucm.es/ — ediciones, transcripciones y bibliografía paleohispánica. Consulta y contraste por ficha antes de copiar lecturas.
- Ibers.cat: https://www.ibers.cat/corpuscast.html — David Folch Flórez, corpus informatizado; Excel, corpus nororiental. Licencia anunciada CC BY-NC-SA 3.0. El sitio advierte que hay lecturas dudosas y decisiones editoriales señaladas tipográficamente; al convertir formatos se pueden perder estas marcas. No redistribuir íntegramente ni asumir aptitud para explotación comercial sin revisar las condiciones.
- Cathalaunia / Ibèrika: https://cathalaunia.org/Iberika/Iberika — corpus con miles de entradas y agrupaciones por objetos, muchas numismáticas. La entrada NO es una unidad física independiente y la exposición pública descarta considerarla ciega retrospectivamente.

## Avance técnico
- `scripts/validation01_te_token_audit.py` recibe `data/review/validation01_te_tokenized_review_v1.csv` con **signos atómicos separados por espacios**, e.g. `a te r`. Solo la unidad silábica `te` cuenta. `ta e` NO cuenta como `te`.
- Estado `UNKNOWN` si lectura ambigua, símbolo perdido `?`, laguna `[lacuna]`, o línea no revisada de principio a fin. La ausencia TE solo se permite en una línea revisada completa.
- Requiere objeto físico, fuente, localizador de edición, signario, revisión y cohorte; no admite `HOLD` en el importador retrospectivo.
- La hoja de entrada está deliberadamente vacía. Por ahora: **0 attestaciones individualizadas verificadas**; no inferir frecuencia ni ausencia de TE.
- Pruebas añadidas para falso positivo por subcadena y bloqueo de fuga HOLD.

## Pasos materiales para liberar el primer lote
1. Descargar y leer la edición correspondiente (según licencia), cotejar cada línea con su fotografía/calco y registrar cara/fila/página.
2. Transcribir **signo a signo**, preservando variantes e incertidumbre sin reemplazar automáticamente `te` por letras `t+e`.
3. Solicitar a revisor independiente la lectura y registrar desacuerdo. Introducir únicamente líneas con trazabilidad en plantilla.
4. Ejecutar auditor, publicar resultados como **retrospectivos**. No mezclar revisión retrospectiva con predicción prospectiva.
5. Para el experimento confirmatorio: fuente futura o conjunto ciego no expuesto, hipótesis y código congelados, etiquetas protegidas, baselines entrenados, tamaño y estadística preregistrados.

## Resultado
**No hay todavía evidencia suficiente para puntuar VALIDATION-01**. Se ha identificado material documental recuperable y se ha implementado una vía estricta para su incorporación. Reconocimiento paleográfico y significado de `te` siguen no demostrados.

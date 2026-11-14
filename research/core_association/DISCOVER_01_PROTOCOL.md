# IBEROS-DISCOVER-01 — hipótesis alternativas y regla de falsación
Fecha: 2026-11-14. Estado: **EXPERIMENTAL**. Core / FULL3406 / C594 / C474 / C539 / C541 intactos. Sin gasto adicional.

## Qué hemos comprobado
- Se reutilizan registros del catálogo de objetos, enlaces epigráficos, fuentes visuales y 17 posiciones editoriales Orleyl.
- El manifiesto de muestras del lector visual es solo cabecera, sin ejemplos etiquetados.
- Las posiciones Orleyl están marcadas `UNVERIFIED_DO_NOT_USE_AS_SIGN_PROOF`. Su existencia **no certifica** la correspondencia fotografía→grafema.
- Las 286 variantes de signario y 133 etiquetas simples no equivalen a imágenes arqueológicas reconocidas independientemente.
- El sistema debe devolver `ABSTAIN_NO_INDEPENDENT_SEMANTIC_GOLD` cuando falten pruebas externas, sin inventar tasas de acierto.

## Cuatro modelos que deben contrastarse, sin imponer el desenlace
1. **P**: grafema→valor fonético o silábico (control estable para escritura nororiental).
2. **L**: ciertos signos autónomos actúan como unidades léxicas; restringir las propuestas a casos donde se documente la autonomía.
3. **M**: combinación de valores fonéticos, marcadores semánticos y funciones especiales; penalizar parámetros adicionales para evitar sobreajuste.
4. **N**: marca no lingüística, estampilla, símbolo de taller u otra señal gráfica, como control negativo.

No basta con que un modelo explique retrospectivamente una coincidencia. Un modelo alternativo solo progresa si mejora en conjunto independiente previamente reservado, con unidad física `PHYS_ID` y grupo de filtración `LEAK_GROUP`, respecto a P y N. Los contextos se etiquetan con fuentes externas anteriores a la predicción; no pueden derivarse del supuesto significado del propio signo.

## Pruebas necesarias para activar la comparación
- Capturas/fotografías o figuras de objetos **físicamente identificados**; licencia y fuente individual registradas.
- Recortes de signos comprobados por un segundo lector, sin forzar valores modernos sobre grafías antiguas.
- Transliteración editorial conservada y distinguida de lectura independiente.
- Segmentación y límites de palabra comprobados, o alternativas explícitas.
- Hipótesis semánticas fijadas antes de conocer los datos de evaluación.
- Comparar precisión, cobertura, abstención, calibración, permutación de etiquetas y tasa de falsos positivos en controles anepigráficos.
- Si no hay traducciones externas demostradas, medir tareas intermedias (clasificación de función documental, identificación de marcas no lingüísticas, predicción de rasgos contextuales), sin llamarlas desciframiento.

## Reproducibilidad
```sh
python research/core_association/discover.py --output /tmp/iberos-discover-01.json
python -m unittest discover -s research/core_association -p 'test_*.py' -v
```

La tabla de salida `object_evidence_queue` distingue disponibilidad de enlace, fuente visual e imágenes con signos verificadas. Las filas **no son casos de entrenamiento** hasta que se acredite su lectura y procedencia. Los archivos fuente quedan ligados a sus hashes SHA-256.

## Decisión
No se promociona ningún significado ni puntuación al Core. Primer umbral: obtener dos objetos físicamente distintos con controles visuales y contexto externo; segundo umbral: realizar un HOLD ciego con suficiente tamaño y potencia estadística. El primer umbral no demuestra por sí solo rendimiento.

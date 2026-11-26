# GOLDSET-39 | Primer conjunto de referencia documental epigráfico preparado para validación gráfica

Fecha: 2026-11-26. Se cotejó directamente Ferrer i Jané, Garcia i Rubert, Moreno Martínez y Velaza Frías (2008), *Palaeohispanica* 8, pp. 203–216, especialmente pp. 207–208, [PDF original](https://ifc.dpz.es/recursos/publicaciones/28/40/_ebook.pdf). SHA-256 del documento previamente recuperado: `2965fd62b2a040aa99bb5428bbe8018fba56ebfb201b35034e93a2c38b292e22`.

Se han creado **21 fichas documentales** en `goldset39_moleta_records.json`, organizadas **3+9+9** en tres renglones y dos zonas físicas. Cada ficha incluye hipótesis paleográficas de la edición, alternativas y abstenciones. El artículo señala restos de **21 signos** y advierte que en zona 2 se perciben **al menos nueve** restos; las posiciones del registro son una indexación operativa, **no 21 caracteres enteros comprobados**. La variante `tu1/ku2` y los candidatos `ta1/ko1`, `be3/bo2/bo4`, `m4/a3` se conservan como alternativas editoriales, no como etiquetas ya verificadas.

**La fuente ha sido verificada, pero no existe aún patrón oro visual independiente:** 0 recortes asociados de forma acreditada a signos individuales, 0 cajas signo/píxel aprobadas, 0 clasificaciones ciegas validadas, 0 traducciones. Los recortes de las figs. 4 y 5 están identificados en SEGMENT-34, pero su atribución a signos necesita revisión independiente.

Se incluye `test_goldset39.py` para rechazar la promoción de etiquetas sin prueba, impedir filtración de una misma pieza entre entrenamiento/evaluación y registrar 21 IDs exclusivos. La carpeta local reproducible `IBEROS_GOLDSET_39.zip` incluye el constructor Python, CSV con descripciones más extensas, ficha de revisión ciega sin etiquetas y manifiesto de procedencia. No se suben ni redistribuyen fotografías originales o derivadas por la licencia de la edición CC BY-NC-ND.

**Siguiente control que convertiría esto en conjunto gráfico verificable:** un observador ciego delimita dos regiones físicas y tres líneas en los gráficos originales, identifica los restos de trazos **sin leer las variantes editoriales** y graba las coordenadas sobre las imágenes de SEGMENT-34. Un segundo cotejo foto/dibujo verifica por separado cada caja o consigna discrepancia. Solo entonces se abre el registro editorial para acuerdo y discrepancia. Los no reconocibles se registran como ABSTAIN. Ninguna mejora cuantitativa en SEGMENT-32 queda confirmada por este dataset hasta completar la anotación.

Protección: Core, FULL3406, C594/C474/C539/C541 inalterados. Coste adicional 0 €.

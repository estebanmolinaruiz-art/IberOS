# IberOS CORE-X — Inferencia semántica mediante contexto histórico-arqueológico
Fecha: 2026-11-01. Estado: protocolo propuesto; no prueba de traducción.

## Hipótesis rectora
Las inscripciones se producen en prácticas humanas concretas; el soporte, la procedencia, el contexto estratigráfico, el paisaje social, la fecha y los paralelos documentales restringen el conjunto de interpretaciones admisibles. **Contexto limita posibilidades; no convierte automáticamente una palabra en su traducción.** La función de un documento y el significado de un token no son equivalentes.

## Variables, fuentes y separación de evidencias
- Objeto físico único / agrupación de fragmentos; soporte; orientación y ubicación de la escritura; integridad y alteraciones.
- Yacimiento, unidad estratigráfica y situación primaria/secundaria/descontextualizada; cronología y rango.
- Contexto independiente: actividad productiva, circulación, vivienda, necrópolis, santuario, depósito, hallazgo monetario; materiales asociados *de forma arqueológicamente acreditada*.
- Señales epigráficas observables: longitud, repetición, secuencias, posiciones, numerales, signos ambiguos, segmentación alternativa, antropónimos propuestos y calidad de lectura.
- Paralelos independientes, cecas / leyendas bilingües cuando procede, fórmulas comparadas y fuentes etnohistóricas con fecha y sesgos.
- Cada dato: identificador de evidencia, fuente primaria, cita o página, estado (OBSERVED/REPORTED/INFERRED/UNKNOWN), responsable, permiso y posible contaminación.

## Escenarios contextuales iniciales (hipótesis, no asignaciones a piezas)
| Soporte o entorno | Hipótesis funcionales candidatas | Alternativas y precauciones |
|---|---|---|
| Láminas de plomo | correspondencia, contabilidad, transacción, lista, etiqueta | también usos rituales y otros; el soporte no implica comercio |
| Cerámica con inscripción breve | identificación de propietario, destinatario, fabricante, contenido | numeral, marca, fórmula votiva, signos sin contenido lingüístico |
| Monedas | ceca/topónimo, autoridad, marca de valor, nombre | diferenciar leyenda, icono, marcas monetarias |
| Estelas funerarias | nombre personal, relaciones de filiación, fórmula conmemorativa | ubicación secundaria o reutilización; función a confirmar |
| Santuarios/cuevas | ofrenda, dedicación, ritual, identificación | uso habitacional o no ritual, depósitos desplazados |
| Pesos y equipamiento productivo | unidad, cantidad, productor, propiedad | marca instrumental no lingüística |

## Algoritmo propuesto
1. Construir conjunto de hipótesis semánticas **predefinidas** por género y compararlas con una hipótesis nula/indeterminada.
2. Extraer **rasgos independientes de la secuencia** (soporte, hallazgo, fecha, contexto) y **rasgos lingüísticos** (posición, repetición, asociación con signos numéricos), manteniéndolos separados.
3. Calcular puntuaciones calibrables con un modelo probabilístico transparente: log P(H|evidencia) = log P(H) + suma de contribuciones condicionadas; no sumar evidencias correlacionadas como si fuesen independientes.
4. Aplicar restricciones: si la lectura paleográfica es incierta, propagar alternativas; si falta contexto, ensanchar intervalo y permitir abstención.
5. Generar predicciones refutables sobre **nuevos objetos físicos**: posición de posibles unidades, coocurrencia con numerales, distribución por tipo de soporte y patrones morfológicos.
6. Evaluar por grupos de objeto/yacimiento, prueba ciega y comparación con base rate por contexto, frecuencia léxica, modelos n-gram y permutaciones; hacer ablación del contexto para medir valor añadido.
7. Registrar resultados negativos, contradicciones y discrepancias con bibliografía especializada. Nunca permitir que una predicción de IA se convierta a sí misma en gold.

## Primer piloto falsable
**Tarea 1: función documental**, clasificación probabilística entre administrativo/comercial, identificación/propiedad, funerario, ritual, indeterminado, usando etiquetas externas independientes.
**Tarea 2: regularidades de tokens**, evaluar si ciertas secuencias se asocian con números/contextos sin inferir un diccionario automático.
**Tarea 3: hipótesis semánticas**, formular alternativas para formas documentadas como śalir; contrastarlas con contextos externos y retener la incertidumbre.

## Prevención de circularidad
Prohibido etiquetar como 'comercial' solo porque aparezca una palabra interpretada como dinero, y después concluir que esa misma palabra significa dinero. Usar etiquetas de excavación independientes del texto; registrar cuándo una función deriva ya de la interpretación epigráfica. Conservar muestra nula, incertidumbre cronológica, editor y tipo de hallazgo.

## Fuentes
- Helena Bonet Rosado, «Contextos arqueológicos de los textos ibéricos valencianos», Palaeohispanica 13 (2013): https://ifc-ojs.es/index.php/palaeohispanica/en/article/view/172
- Noemí Moncunill y Javier Velaza, «Iberian», Palaeohispanica 20 (2020): https://ifc.dpz.es/recursos/publicaciones/38/77/17moncunillvelaza.pdf
- Ferrer, Moncunill y Velaza, propuestas para escritura nororiental y repertorio de géneros epigráficos: https://ifc.dpz.es/recursos/publicaciones/35/02/_ebook.pdf
- Estudio del plomo de Fundació CIRNE/Xàbia, discusión de usos administrativos, cartas, etiquetas y posibles usos rituales, y de śalir: https://aespa.revistas.csic.es/index.php/aespa/article/download/619/689

Mantener VALIDATION-01=NOT_EVALUATED, M06/M07 pendientes. Documento metodológico, no prueba empírica ejecutada.

# METROLOGY-DISCRIMINATION-03 · control rival antes de evaluar el significado

Actualizado el **11 de noviembre de 2026**. Frente a los módulos
METROLOGY-MODELS-01 y METROLOGY-HYBRID-02, que comparan solo
relaciones 10:1 y 12:1 con una selección bibliográfica, se añade una
objeción histórica documentada: en los ponderales ibéricos se han
publicado series interpretadas con unidad fundamental **2,1 g**.

**Coincidencia no discriminante**:
- 42 g = 20 × 2,1 g.
- 420 g = 200 × 2,1 g.
- Tos Pelat 418 g = 199 × 2,1 g + 0,1 g; es una coincidencia de masa
  numérica, no una atribución independiente de unidad metrológica.
- El objeto de Puig de la Misericòrdia 41,29 g tampoco permite asignar
  por masa sola valor léxico al signo o.

Referencia de la alternativa: Martínez y González, «Un conjunto de
ponderales ibéricos procedente de Villanueva de la Jara (Cuenca)»,
*Florentia Iliberritana* 29 (2018), 381–390, menciona la serie
teórica de 2,1 g propuesta por Fletcher y Silgo (1995).
https://www.researchgate.net/publication/331529729_Un_conjunto_de_ponderales_ibericos_procedente_de_Villanueva_de_la_Jara_Cuenca

El modelo híbrido a/o/ki queda como hipótesis metrológica
publicada; no es traducción demostrada. Las coincidencias de
múltiplos pueden sostener varias propuestas sin identificación de
los signos. El módulo crea un reporte de **no-identificabilidad**,
no puntúa modelos ni selecciona ganadores.

## Seguimiento documental

El Museo Arqueológico Municipal de Moncada respondió el **5-11-2026**
a la petición de IberOS enviada el 4-11-2026. Josep Maria Burriel
Alberich indica que facilitará la información cuando pueda. El
mensaje no incluía número de inventario, masas originales, fotografías
ni permisos. El proyecto conserva el contacto sin insistir todavía.

## Puerta de avance

1. Inventario y muestreo completo de ponderales elegibles, incluyendo
   anómalos y negativos, sin elegir solo masas de 42/420 g.
2. Tabla independiente de masa, instrumento/tolerancia, conservación,
   material, contexto, cronología y autenticidad de las marcas.
3. Lectura epigráfica y cuantificación anotadas por evaluadores
   diferentes antes de contrastar modelos.
4. Comparar propuestas rivales (híbrido 10/12, 2,1 g y modelos
   alternativos) en una muestra no utilizada para formularlas.
5. Registrar abstenciones y contrastes falsables; no abrir FULL3406
   ni reinterpretar el antiguo HOLD como novedad.
6. Solo publicar resultados lingüísticos cuando existan
   evidencias contextuales y predicciones independientes.

Código: `python -m iberos.metrology_discrimination_03 --json informe.json`.
Pruebas: `pytest -q tests/test_metrology_discrimination_03.py`.
No requiere servicios de pago. No altera FULL3406, splits ni métricas.

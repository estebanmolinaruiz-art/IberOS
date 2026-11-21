# SCI-MET-03 — Contraste de conjuntos arqueológicos y análisis de identificabilidad

**Fecha:** 21 noviembre 2026. **Coste:** 0 €. **Core, FULL3406 y particiones TRAIN/VAL/HOLD:** intactos.

## Fuentes materiales revisadas

**Villanueva de la Jara (Cuenca):** D. Martínez Chico y A. González García (2018), «Un conjunto de ponderales ibéricos procedente de Villanueva de la Jara», *Florentia Iliberritana* 29, pp. 381–390, [texto y figura 2](https://revistaseug.ugr.es/index.php/florentia/article/download/8829/7412/25457). Cinco ponderales discoidales perforados de 21,0; 41,5; 62,7; 106,5 y 214,3 g (p. 383); los autores asignan proporción **1:2:3:5:10**. Son cinco objetos físicos **de un solo conjunto**, NO cinco muestras estadísticamente independientes. Se recuperaron en un hallazgo superficial y sin excavación estratigráfica regular. La fuente incluye figura 2, pero **el visor web no permitió examinar la fotografía de forma fiable**: no declaramos lectura paleográfica directa de signos ni marcas.

**Aras de los Olmos:** J. V. Montes Novella (2026), «El sistema ponderal ibérico: arqueología frente a epigrafía», *ELEA* 23, pp. 149–229, [texto académico libre](https://www.academia.edu/172876427/EL_SISTEMA_PONDERAL_IB%C3%89RICO_ARQUEOLOG%C3%8DA_FRENTE_A_EPIGRAF%C3%8DA), figura indicada hacia pp. 198–200. Pesa de **41,05 g con dos incisiones triangulares**; otras piezas atribuidas por el autor al conjunto donado al Ecomuseo: **42,52 g y 6,68 g**. No se ha obtenido una imagen en resolución suficiente para comprobar si las incisiones son gráficamente equivalentes a un signo ibérico. Procedencia de donación y agrupación estratigráfica no demostrada; el texto académico es una fuente de informe, **no una autopsia**.

**Controles de formas heterogéneas del mismo trabajo:** piezas publicadas de 40,34 g con dos puntos; 103,5 g con cinco puntos; 41,73 g con una marca triangular/lúnula; 8,5 g con cinco marcas triangulares/lúnulas. Procedencia y cronología de estos cuatro testimonios deben conciliarse antes de tratarlos como una única población de una misma clase de signos. No han sido cotejados directamente en fotos.

**Otras series con agrupación arqueológica:** El Cigarralejo, sepultura 200: masas 1,98; 3,38; 5,01; 7,4; 15,83; 20,48; 41,46; 81,65; 125; 208,45 g. Covalta, construcción 27: 42,2; 81,8; 122,25; 209,5 g. Son masas publicadas en Martínez Chico y González García (2018), pp. 386–387, citando a Fletcher y Mata. Demuestran que existe una familia de escalas cercana a 21/42 g, pero no adjudican individualmente el significado de cada incisión.

## Cálculo independiente ejecutado

Método: con la **serie de 5 objetos de Villanueva de la Jara** y el vector de proporciones publicado `r = [1,2,3,5,10]`, ajustar una escala `u` por mínimos cuadrados sin intercepto:

`u = Σ(r_i * masa_i) / Σ(r_i²) = 21,3496402878 g`

`RMSE(u) = sqrt(Σ(masa_i - r_i*u)^2/5)`.

| Modelo | Parámetro impuesto o ajustado | Error medio cuadrático RMSE |
| --- | ---: | ---: |
| A. Unidad 21 g (publicada) | 21,000 g × [1,2,3,5,10] | **2,0533 g** |
| B. Dos incisiones de Aras = dos unidades | 20,525 g × [1,2,3,5,10] | **4,4410 g** |
| C. Mejor ajuste a la propia serie | 21,34964 g × [1,2,3,5,10] | **0,9042 g** |
| D. Unidad entera doble, semimúltiplos permitidos | 42,69928 g × [0,5;1;1,5;2,5;5] | **0,9042 g (idéntico a C)** |

**El punto crítico es matemático:** el modelo D predice exactamente las mismas cinco masas que C, porque `42,69928 * (r/2) = 21,34964 * r`. Por tanto, una selección de masas y sus proporciones **no puede discriminar por sí sola** si la unidad léxica/gráfica es ~21 g o ~42 g y se emplean medias unidades. Elegir escala desde la propia serie en ambos modelos crearía la ilusión de haber confirmado una traducción.

**Aras individual:** 41,05 g con dos incisiones se puede expresar como **1 × 41,05 g** si las incisiones son marcas no aditivas, o como **2 × 20,525 g** si son dos signos de valor 1. La misma masa es compatible con ambas hipótesis; la pieza de 42,52 g podría corresponder a 1 × 42,52 o 2 × 21,26. El tercer objeto de 6,68 g podría ser una fracción distinta, no evidencia directa de 21/42 g.

## Prueba de forma: por qué «contar incisiones» no basta

| Masa publicada | Incisiones reportadas | Clase gráfica | Masa/marca **si aditivo** |
| ---: | ---: | --- | ---: |
| 40,34 g | 2 | Puntos | 20,17 g |
| 103,50 g | 5 | Puntos | 20,70 g |
| 41,73 g | 1 | Triángulo o lúnula | 41,73 g |
| 8,50 g | 5 | Triángulos o lúnulas | 1,70 g |
| **41,05 g (Aras)** | **2** | **Triángulos** | **20,525 g** |

Una misma clase gráfica aparente (**triángulo/lúnula**) puede producir valores condicionales muy diferentes, lo que impide asumir que todas las incisiones significan siempre la misma unidad. Sin lectura de imagen y procedencia de estos objetos, la división masa/nº de marcas es **un contrafactual matemático, no desciframiento**.

## Experimento informático reproducible

Dataset con procedencia y estado de lectura: `data/review/sci_met03_published_weights_v1.json`.

Motor: `src/iberos/ponderal_model_comparison.py` (biblioteca estándar, sin costes).

Tests: `tests/test_ponderal_model_comparison.py`.

Ejecución desde repositorio:
```bash
python -m iberos.ponderal_model_comparison
python -m pytest -q tests/test_ponderal_model_comparison.py
```

GitHub Actions científico ejecuta el mismo contraste y publica el JSON de auditoría; ninguna función puede poner `translation_validated=True`.

## Veredicto

**Resultado positivo real:** la serie de Villanueva de la Jara confirma a nivel de masas una relación de **escala ~21 g con múltiplos 1:2:3:5:10**, reproducida numéricamente. **Resultado negativo/indeterminado igualmente real:** esa proporción no demuestra por sí misma que las incisiones de Aras signifiquen «dos», que exista un signo ibérico para media unidad, o que `o` y `a` tengan una equivalencia léxica determinada. La relación doble/mitad de escala es **no identificable a partir de estas masas**.

**Siguiente evidencia decisiva:** cotejo original de la figura de Aras con fotografía bajo luz rasante para distinguir marcas intencionadas de grafemas ibéricos, y reconstrucción de un conjunto estratificado que incluya **dos o más pesos con marcas gráficas idénticas** y una serie de masas no elegida a posteriori. Si la misma marca gráfica aparece de modo estable sobre **~20,5 g** y **~41 g**, o sobre dos pesos de razón 2:1 con diferentes cantidades de marca, se puede distinguir entre unidad y múltiplo. Sin esos datos no se debe introducir valor de signo en el modelo de traducción de IberOS.

**No hay aciertos semánticos ciegos nuevos.** Este es un contraste cuantitativo RETROSPECTIVO sobre medidas publicadas. 0 traducciones independientes confirmadas.

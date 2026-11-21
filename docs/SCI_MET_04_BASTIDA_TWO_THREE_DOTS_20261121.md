# SCI-MET-04 — Controles independientes de marcas y masa: la tercera marca hipotética

**Fecha:** 21-XI-2026 · **Coste monetario:** 0 € · **Estado:** CONTRADICCIÓN RETROSPECTIVA CUANTIFICADA / RESOLUCIÓN VISUAL PENDIENTE.

## Búsqueda dirigida a la figura de Aras

El estudio de **José Vicente Montes Novella (2026), ELEA 23, pp. 149–229**, está disponible en texto íntegro mediante [Academia.edu](https://www.academia.edu/172876427/EL_SISTEMA_PONDERAL_IB%C3%89RICO_ARQUEOLOG%C3%8DA_FRENTE_A_EPIGRAF%C3%8DA), con referencia a **figura 11, p. ~198**. Se vuelve a identificar la pesa de **Aras de los Olmos, 41,05 g, dos incisiones triangulares**, conservada en el Ecomuseo a raíz de una donación. **No se consiguió acceso directo y fiable a una reproducción de la figura 11 apta para inspección de trazos**. Las búsquedas específicas de imágenes devolvieron objetos ajenos; no se atribuye a Aras una imagen genérica ni se declara reconocimiento visual. La masa de 42,52 g y la de 6,68 g corresponden a otros dos ponderales del conjunto donado, no a piezas con dos signos `o` demostrados.

## Evidencia arqueológica con identificador de objeto, sin extrapolaciones

La nueva línea prioritaria es La Bastida de les Alcusses (Moixent). El estudio original de [Thibaud Poigt, capítulos metrológicos de la península Ibérica, UNA Éditions](https://una-editions.fr/la-peninsule-iberique-creuset-dune-pratique-ponderale/), secciones dedicadas a las marcas de la Bastida y figuras **3-118** y **3-154**, permite documentar piezas físicamente diferenciadas:

| Objeto | Departamento | Peso real publicado | Marcas puntiformes descritas | Masa si marca aditiva |
| --- | --- | ---: | ---: | ---: |
| **Bas-129-A** | 129 | **40,34 g** | 2 puntos | 20,17 g/punto |
| **Bas-273-C** | 273 | **103,50 g** | 5 puntos | 20,70 g/punto |
| **Bas-273-B** | 273 | **63,41 g** | 2 puntos, **posible tercera invisible** | 31,705 g/punto si 2; 21,1367 g si 3 |

La lectura alternativa de una tercera marca **no es descubrimiento visual de IberOS**: la menciona Montes Novella (2026, pp. 171–172). Ferrer i Jané (2026) registra la controversia de los tres pesos bitroncocónicos de la Bastida, ya conocida en los trabajos de Poigt. **Son varias publicaciones acerca de las MISMAS piezas**, no lecturas ciegas independientes.

### Prueba matemática concreta sin entrenar con el objeto problemático

Fijamos **Bas-129-A y Bas-273-C** como calibración retrospectiva del valor de masa por punto. Ajuste por mínimos cuadrados sin intercepto:

`u = [2 * 40,34 + 5 * 103,5] / [2² + 5²] = 20,6268965517 g`.

Para el **Bas-273-B de 63,41 g**, sin usar su masa en la calibración:

| Número supuesto de puntos | Masa predicha | Diferencia observada – predicha | Error porcentual relativo |
| ---: | ---: | ---: | ---: |
| **2**, lectura editorial | **41,2538 g** | **+22,1562 g** | **53,71 %** |
| **3**, lectura alternativa *hipotética* | **61,8807 g** | **+1,5293 g** | **2,47 %** |

**Observación que discrimina:** si la figura fotográfica muestra efectivamente **tres** puntos intencionados de la misma clase, el modelo homogéneo de aproximadamente 20,63 g/punto sería coherente con los tres objetos con una tolerancia descriptiva del 10 %. Si conserva **solo dos**, el modelo de masa uniforme por punto falla gravemente para esta pieza y habría que estudiar sistemas mixtos de ~31,7 g, errores antiguos de marcado o valores no aditivos. **Ningún resultado determina automáticamente el significado lingüístico del signo ibérico `o`**, y los puntos no son grafemas `o` verificados.

### Restricciones y controles metodológicos

- Departamento 273 contiene los dos objetos Bas-273-B y C: no tratarlos como contextos arqueológicos independientes para validación prospectiva; aquí solo se contrasta una regla física histórica.
- Masas de una misma serie y descripciones de punto / triángulo / lúnula no se agregan sin homologación de forma gráfica; la unidad de 21 g y la de 42 g con semimúltiplos siguen siendo matemáticamente equivalentes en SCI-MET-03.
- La figura original de Aras **no ha sido examinada** y la fotografía de la figura 3 de Montes (2026), atribuida a Jaime Vives-Ferrándiz, tampoco se ha cotejado trazo a trazo; **COTEJO_D2/D3 = PENDIENTE**.
- Fotografías publicadas requieren conservación de derechos, atribución y huella de archivo; no dibujar tres signos inexistentes ni tratar una imagen de pesos ajenos como evidencia.
- El modelo del 10 % es una banda descriptiva, no un intervalo de confianza o una precisión declarada por un laboratorio.
- Resultado es **retrospectivo** y deriva de hechos ya documentados en publicaciones de 2022–2026. No es un acierto nuevo de desciframiento ni una predicción semántica ciega.

## Próxima verificación decisiva de coste cero

1. Abrir la **figura 3** de Montes 2026 (fotografías originales de La Bastida, Jaime Vives-Ferrándiz) y la **figura 3-118** de Poigt en UNA Éditions; identificar exactamente **Bas-273-B**, fotografiar ambas caras si están disponibles en publicación libre y registrar si hay dos puntos, tres u otras marcas. No utilizar fotografías de otras piezas.
2. Si los repositorios web bloquean la figura, mantener `IMAGE_NOT_ACCESSIBLE` y contrastar descripciones originales, sin declarar análisis visual.
3. Repetir el cálculo con **conteos adjudicados visualmente**, y luego estudiar si los modelos de unidades 20–21 y 31–34 g se distinguen por morfología, lugar y peso.
4. Conservar la resolución o persistencia del contraejemplo aunque contradiga el modelo preferido. Continuar la búsqueda de piezas con un signo `o` y masa conocida fuera de entrenamiento SCI-MET-02; ninguna pieza sin `o` puede contarse como el éxito que ese protocolo precomprometió.

## Código, datos y estado

- Datos: `data/review/sci_met04_bastida_dot_mark_cases_v1.json` (identidad, departamento, masa, forma y grado de revisión).
- Modelo: `src/iberos/marked_weight_sensitivity.py` (solo biblioteca estándar).
- Tests: `tests/test_marked_weight_sensitivity.py` (incluye contraprueba del número de marcas y prohibición de falsa validación).
- Pipeline: `.github/workflows/science-prediction-translation.yml` genera `sci_met04.json` y bloquea cualquier afirmación de traducción validada.
- CORE congelado / FULL3406 / HOLD: **sin modificaciones**.
- Verdadero GOLD semántico nuevo / aciertos ciegos / traducciones confirmadas: **0 / 0 / 0**.

**Resultado científico real de esta búsqueda:** se ha precisado el contraste numérico que hace decisiva la fotografía de una pieza arqueológica identificada: **Bas-273-B**. No se ha resuelto la lectura gráfica, y ésa es la frontera restante.

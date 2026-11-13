# G-126 · La Picola: excavado vs. restituido y cronología del supuesto paso

**Fuente primaria:** Moret, P. y Badie, A. (1998), *Archivo Español de
Arqueología* 71, 53–61, figura 3 y pp. 54–56.
https://doi.org/10.3989/aespa.1998.v71.274

## Dato editorial crítico
La leyenda de la figura 3 define **gris oscuro = estructuras conservadas** y
**gris claro = estructuras restituidas**. La figura 2 es un **perfil
reconstruido** de las defensas; no equivale a un corte excavado de un puente.

## Evidencia observada por los excavadores
- Cortinas conservadas en lados NE y NO.
- Puerta localizada en el centro de la cortina NE; R2 desembocaba en ella.
- R2 identificada mediante una excavación en septiembre de 1995.
- Tramos del foso y paramentos conservados en sectores excavados.

## Restituciones o inferencias
- Sector del recinto muy destruido por modificaciones posteriores;
  los autores especifican que no cabe una restitución completa y distinguen
  gráficamente los segmentos restituidos.
- Continuación hipotética del eje de R2 *sobre* el foso.
- Hipótesis de un puente, terraplén, interrupción en la zanja o paso.

## Cronología
Los niveles cerámicos permiten situar la fundación del asentamiento
hacia 450/430 a. C., con abandono hacia 330 a. C. Esto caracteriza
**la ocupación del recinto**, pero NO fecha automáticamente un hipotético
puente o una obra de paso. Para demostrarlo se necesitan unidades
estratigráficas directamente asociadas al cruce y dataciones independientes.

## Dictamen reproducible del nuevo motor G-126
`picola_1998_case()` devuelve
`NO_DIRECT_DATED_CROSSING_EVIDENCE` y mantiene
`bridge_or_causeway_confirmed: false`. Esta formulación significa
**sin evidencia directa identificada en esta publicación**, y no equivale
a concluir que nunca existió un puente.

La leyenda es inequívoca, pero la imagen original de la figura no pudo
descargarse como archivo local calibrable en este turno. Por eso esta
auditoría clasifica a nivel de los elementos descritos en el texto
y la leyenda, NO asigna polígonos píxel a píxel ni mide la intersección
del eje R2 con un hueco preciso del foso.

## Próxima prueba discriminante, gratuita
Examinar la planta de excavación (figura 3 original y Plan Director 2023,
planchas de arqueología), localizando expresamente **cualquier corte del
foso frente al vano** y cotejando sus números de unidad estratigráfica.
Documentar si corresponde a excavación o restitución, y fase cronológica.
No usar el gris claro como restos observados.

Reproducir: `python -m unittest discover -s tests -p 'test_route_picola_stratigraphy.py'`.
Regla permanente: **0 € adicionales**; sin alteración de métricas de Core.

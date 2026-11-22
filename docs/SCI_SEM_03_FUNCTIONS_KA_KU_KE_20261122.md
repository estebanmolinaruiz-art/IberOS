# SCI-SEM-03 — Funciones candidatas de -ka, -ku y -ke con comprobación adversarial

**Fecha de auditoría:** 2026-11-22. **Prioridad:** semántica ibérica del Core, sin modificar FULL3406, TRAIN/VAL/HOLD ni reglas SCI-PRED-02. **Coste:** 0 €.

## Resultado: funciones propuestas en bibliografía, NO descifradas por IberOS

| Segmento | Función explícita de la hipótesis | Grado de comprobación | Contra-hipótesis |
|---|---|---|---|
| `-ka` | destinatario/receptor, cuenta de una **salida** del sistema | **PROPUESTA DOCUMENTADA / CONVERGENCIA CONTEXTUAL**; sin gold independiente | sujeto de obligación, proveedor, agente, cuenta individual, variante morfológica |
| `-ku` | origen/proveedor, cuenta de una **entrada** al sistema | **PROPUESTA DOCUMENTADA / DISTINCIÓN DE DISTRIBUCIONES**; sin gold independiente | deudor de cuantías mayores, categoría de producto, variante gráfica/alomorfo |
| `-ke` | participante asociado a cantidad, quizá titular de una **salida** en listas grecoibéricas | **POSICIÓN SINTÁCTICA DOCUMENTADA**; dirección de transacción NO establecida por gold | alomorfo de -ka, función de caso no orientada, receptor, agente o clase de documento |

**Importante**: estas propuestas no son lingüísticamente nuevas en 2026 ni constituyen una traducción validada por IberOS.

## Documentación precisa

**La Bastida I, cara B (V.17.02, MPV 13417)**. Ferrer i Jané (2026), «Algunes reflexions a propòsit del plom ibèric Bastida I: paleografia, metrologia i negoci», *Archivo de Prehistoria Levantina* XXXVI, pp.133–166. [Texto abierto del museo](https://mupreva.org/web_mupreva_dedalo/publicaciones/1642/va). Según el autor:
- Los 19 registros forman **cuatro grupos**; en **tres grupos hay cuatro entradas -ka y una final -ku**, y en el **tercero hay dos -ka y dos -ku**. Esto suma **14 usos -ka y 6 -ku si se contabilizan las cifras tal como se describen**, aparentemente **20 entradas**, frente a las **19 expresiones** de la síntesis. **ALERTA: INCONSISTENCIA DE CONTEO**; investigar tabla de segmentación antes de utilizar 19 o 20 como denominador. Es probable que parte del pasaje aluda a agrupaciones, duplicaciones o una entrada excluida. **No inferir frecuencias brutas hasta revisar la tabla completa de edición**.
- Los nombres con -ka reciben casi siempre cantidades pequeñas del orden ki, mientras que los que llevan -ku tienen cantidades mayores del orden a; **beŕśir** es una excepción con grandes cuantías en -ka y anotaciones pendientes de cancelar.
- El autor interpreta `-ka` como **destinativo (salida)** y `-ku` como **ablativo de origen (entrada)**. La relación direccional es una **hipótesis inferida del orden y las magnitudes**, no traducción externa acreditada.
- Una fuente anterior propone una **relación de préstamos/deudores** para la misma pieza, distinta del modelo salida/entrada (Rodríguez Ramos 2016, citado en Ferrer 2026). El desacuerdo obliga a mantener control rival.

**Coimbra del Barranco Ancho, plomo grecoibérico**. Ferrer i Jané (2026), «El plom greco-ibèric de Coimbra del Barranco Ancho», *ELEA* 23, pp.117–147, [edición y tabla 7](https://www.academia.edu/124304178/El_plom_greco_ib%C3%A8ric_de_Coimbra_del_Barranco_Ancho_Jumilla_Murcia_Revisi%C3%B3_de_la_seva_lectura_i_an%C3%A0lisi_del_seu_sistema_metrol%C3%B2gic); López Fernández (2016), [edición original abierta](https://ifc.dpz.es/recursos/publicaciones/35/76/09lopezfernandez.pdf). El texto recoge doce expresiones `NP+ke+Q`; Ferrer señala que Coimbra **solo presenta salidas (-ke)** frente a Bastida con las dos direcciones. Esa atribución de «salidas» **depende de interpretar Coimbra con el mismo modelo de Bastida**. No usarla como gold independiente que demuestre `-ke = -ka`.

**Discusión histórica**: Jesús Rodríguez Ramos (2002), «Acerca de los afijos adnominales de la lengua íbera», *Faventia* 24/1, 115–134, [repositorio UAB](https://ddd.uab.cat/record/640/?ln=es). Argumenta posibles valores de destinatario/receptor para `-ka`; las alternativas de agentes, préstamos, caso y `-ke` muestran que la función específica **no es consensuada en su detalle**.

## Control de falsación, sin ajustes post hoc

- **H-DIR**: `-ka` se asocia a **salidas** y `-ku` a **entradas**. Falsación: un documento con operaciones identificables **independientemente** cuya dirección muestre de modo sistemático `-ka` entradas y `-ku` salidas, o alternancias compatibles solo con el mismo participante/caso tras controlar estructura; conservar errores y excepciones.
- **H-CASE**: `-ka` = beneficiario/destinatario sin dirección inherente; `-ku` = procedencia/origen. La distinción caso vs dirección se decide con datos de origen y destinatario, no solo con cantidades. Una persona puede ser receptor de dinero y salida de mercancía simultáneamente.
- **H-LOAN**: `-ka` = deudor, `-ku` = acreedor o cuenta central; predicciones sobre repeticiones de nombres, cantidades canceladas y balances documentales.
- **H-ALLO**: diferencias gráficas/dialectales con idéntico papel semántico; examinar distribución por escriba, signo S43, lengua y posición, no magnitudes únicamente.
- **H-KE**: `-ke` en Coimbra es un **marcador de participante con cantidad**, quizá función de `-ka`. Para probar identidad de función exigir una alternancia controlada en un mismo sistema o evidencia bilingüe exterior, no similitud de lista ni reconstrucción editorial.

### Alerta cuantitativa que debe resolverse primero

La afirmación editorial «tres grupos con 4 -ka y 1 -ku, un grupo con 2 -ka y 2 -ku» implica **14 -ka + 5 -ku = 19** (no 6 -ku). Así queda reconciliada aritméticamente con 19 expresiones, *si cada grupo está completo y sin incidencias*. Este reparto **14/5 es una inferencia aritmética del pasaje**, no una auditoría independiente de los 19 renglones. No tratarlo como frecuencia confirmada signo a signo hasta revisar la tabla.

## Siguiente prueba ejecutable y útil

Obtener una tabla original de Bastida de **19 partidas con nombre, lectura de sufijo, unidad metrológica, cantidad, orden del grupo, cancelación, estado gráfico** y predefinir dos modelos predictivos: uno que permita `-ka` y `-ku` como alomorfos independientes de tamaño; otro que modele dos poblaciones de tamaños (con cautela: los grupos no son independientes, y la magnitud monetaria depende de la lectura del sistema a-o-ki). Comparación por **permutación estratificada por grupo** sin asumir normalidad y excluyendo posibles restauraciones inciertas. Reportar la excepción `beŕśir`.

Solo después buscar una pieza externa distinta cuyo papel operacional pueda verificarse sin consultar los morfemas. Con las tres fuentes retrospectivas actuales se puede probar clase funcional general pero **NO** salida/entrada como lectura lingüística definitiva.

**Resultados:** clases contextuales plausibles con controles rivales, **0 nuevas traducciones confirmadas**, 0 aciertos ciegos semánticos, sin costes ni cambios al Core congelado.

# IberOS — sincronización ERDER y protocolo ciego v0.1
Fecha: 2026-10-19. EXPERIMENTAL / NO PROMOTION / C474 INDETERMINATE.

## Alcance y autoridad
Referencia común para recuperar desde otros hilos; no acredita entrega o lectura en esos chats.
Auditoría basada en el snapshot 8cef229 y sus antecedentes 0246241, 838c2b6, 5c731f7, 6e2528b y 92d5042.
C594 + C474 + C539 + C541, FULL3406 y métricas oficiales permanecen intactos.

## Estado sincronizable por módulo
| Módulo/hilo | Estado verificado y acción pendiente |
|---|---|
| Principal / ERDER | Matriz bibliográfica retrospectiva; erder≈mitad contextual, sin HOLD superado. |
| Metrología / KITAR-ETAR | Aplicar la retractación 5c731f7: reutilizar cuño entre nominales no refuta por sí solo una marca de valor. No equiparar kitar a masa universal. |
| PALEO / catálogo | Diez referencias localizadas no equivalen a diez inspecciones de signos; en el snapshot, cero ediciones paleográficas completamente comprobadas. |
| La Vispesa | Mantener alerta WRONG_LINK y corrección pendiente del enlace catalogado; referencia Garcés 2007 identificada, sin comprobación gráfica. |
| Serreta | Catálogo museístico de identificación; edición paleográfica primaria pendiente. |
| Write | Requisito: no promover ERDER/KITAR/ETAR como significados seguros. Bloqueo efectivo del código NO VERIFICADO en esta auditoría. |
| Talk / Mobile | Ningún léxico nuevo autorizado por esta tanda; implementación y ejecutables no auditados aquí. |
| Tesis / web | Incorporar solo como auditoría metodológica experimental si procede; sin elevar conclusiones ni afirmar prueba ciega superada. Integración efectiva pendiente. |

## Controles comprobados
La matriz ERDER y los documentos de KITAR/ETAR son documentación, no ejecutores de prueba ciega.
Las cuatro funciones de tests/test_graphic_intake_batch_01.py se ejecutaron directamente con Python sobre los dos archivos recuperados de 8cef229: PASS. pytest no estaba instalado localmente; no se ejecutó localmente la suite completa.
GitHub Actions registró tests success para 8cef229 (run 39086163283).
Estos tests comprueban estados y coherencia de registros: no prueban imágenes, independencia editorial ni validez semántica.

## Familias de dependencia
- ildiŕda, undikesken y Arse comparten la argumentación de Ferrer y Giral 2007. No equivalen a tres validaciones editoriales independientes.
- Hesperia Mon.18.10 depende parcialmente de esa publicación; conservar erder/erkur.
- Arse: agrupar las ocurrencias derivadas de reutilización de cuño.
- Can Rodon y Val de Alegre: objetos distintos, fuente común Veleia 31 (2014).
Un catálogo nuevo, una fotografía nueva o una fecha posterior no garantizan independencia: comprobar genealogía de piezas, lectura y clasificación del nominal.

## ERDER-BLIND-01 — propuesta de protocolo, aún no congelada
Pregunta: ¿la presencia de una lectura ERDER predefinida mejora la predicción de fracción 1/2 fuera de familias usadas para desarrollar la hipótesis?

### Admisión
Registrar specimen_id, mint, issue_id, die_id, dependence_family, metal, date_range, mass_g, conservation, catalogue_id, source_reference, image_reference, source_genealogy, prior_exposure y nominal_basis.
Una dependencia desconocida no se presume independiente: excluir del análisis confirmatorio y conservar para exploración.
Excluir del HOLD piezas y familias usadas en desarrollo. Lecturas expuestas en esta auditoría son antecedentes.
Para el nominal, exigir adjudicación independiente de ERDER y de su supuesto significado. Si la clasificación catalográfica se apoya en la leyenda, el caso no sirve como patrón externo confirmatorio.

### Separación de información
A: lectura desde recortes de leyenda, sin iconografía, masa, ceca ni nominal, con alternativas y abstención.
B: nominal por tipología/iconografía y catálogo, sin acceso a la lectura objetivo. Registrar dudas sin forzar etiqueta.
C: comprobar dependencias y reunir A/B solo después de congelar predicciones.
Si el evaluador ya conoce la pieza o puede reconocer su nominal, marcar exposición y no contabilizarla como ciega.

### Comparación y criterio
Seleccionar controles contemporáneos sin ERDER sin consultar sus resultados.
Separar metales; agrupar por emisión y cuño; mantener familias enteras fuera del desarrollo.
Comparar modelo contextual (ceca/época/metal) frente al mismo modelo con lectura ERDER; ninguna selección de variantes tras ver los resultados.
Métrica primaria propuesta: diferencia de Brier por familia, con ponderación igual por familia; valores menores favorecen el modelo con ERDER.
Antes de cualquier revelado deben fijarse: codificación exacta de variantes, modelos/probabilidades, tamaño y potencia, exclusiones, abstenciones y procedimiento de incertidumbre por familias.
Criterio propuesto para aprobar el ensayo: mejora cuyo intervalo preespecificado del 95% excluya cero a favor de ERDER, y supervivencia del efecto al análisis de lecturas alternativas y retirada por ceca cuando sea estimable.
Un resultado inconcluso o una muestra insuficiente permanece INDETERMINATE; no es refutación.
Un resultado contrario robusto debilita la generalización predictiva planteada; no demuestra por sí solo otro significado.
Incluso superar el ensayo no autoriza promoción automática de la autoridad congelada.

### Gates de ejecución
1. Inventario y genealogía completos: PENDIENTE.
2. HOLD realmente no expuesto y nominal independiente: PENDIENTE.
3. Plan cuantitativo y potencia fijados: PENDIENTE.
4. Manifest de protocolo/datos/predicciones con SHA-256 y registro fechado anterior al revelado: PENDIENTE.
5. Ejecución reproducible y comparación con negativos: PENDIENTE.
No se ha extraído un HOLD nuevo ni ejecutado este experimento. Este documento inicia el diseño; no constituye una preinscripción cerrada.

## Fuentes internas
- [Matriz ERDER](ERDER_CROSS_MINT_EVIDENCE_MATRIX_2026-10-18.md)
- [Corrección de cuños](KITAR_ETAR_DIE_REUSE_CORRECTION_2026-10-18.md)
- [Controles de emisión](KITAR_COIN_ISSUE_CONTROLS_2026-10-18.md)
- [Datos de las diez entradas](../data/review/graphic_intake_batch_01_v1.json)
- [Tests de las diez entradas](../tests/test_graphic_intake_batch_01.py)

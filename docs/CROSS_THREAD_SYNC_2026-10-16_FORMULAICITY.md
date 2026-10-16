# IberOS — Cross-thread sync: FORMULAICITY-STRATA-01

**Fecha:** 2026-10-16  
**Estado:** EXTERNAL METHOD CANDIDATE / NON-PROMOTIONAL  
**Autoridad preservada:** C594 + C474 + C539 + C541  
**Release pública preservada:** IberOS Open Research Kit v1.0.1

## 1. Fuente y alcance

Fuente primaria:

Eren Nacak (2026), “The Evolution and Current State of Digital Tools in Epigraphy: Documentation, Analysis, and Infrastructure”, *Phaselis* XII, 135–161. Publicación en línea: 2026-10-14. DOI: https://doi.org/10.5281/zenodo.21504428

El trabajo revisa RTI, fotogrametría SfM, imagen multiespectral/hiperespectral, EpiDoc, FAIR/IIIF y sistemas de IA epigráfica. Su conclusión metodológica relevante para IberOS es que las replicaciones independientes siguen siendo escasas y que el rendimiento automático puede variar sustancialmente entre textos formularios y testimonios poco atestiguados.

La publicación no aporta nuevas lecturas ibéricas ni evidencia lingüística directa. Entra exclusivamente por la ruta:

`EXTERNAL METHOD → CANDIDATE → IBEROS EQUIVALENT TEST → ADVERSARIAL CONTROL → REGRESSION → ADOPT/REJECT`

## 2. Protocolo candidato

### FORMULAICITY-STRATA-01

Toda evaluación que pueda beneficiarse de fórmulas repetidas, objetos duplicados o variantes editoriales próximas debe informar resultados separados para:

1. `FORMULAIC`: secuencias altamente repetitivas o con plantilla conocida.
2. `SEMI_FORMULAIC`: estructura parcialmente repetida con contenido variable.
3. `LOW_ATTESTATION`: formas, construcciones o lecturas raras.
4. `UNSCORABLE`: evidencia insuficiente, segmentación no estabilizada o lectura paleográfica no resoluble.

Controles obligatorios:

- agrupar por `OBJECT_ID/PHYS_ID` antes de TRAIN/VAL/HOLD;
- mantener juntas las variantes editoriales de un mismo objeto;
- prohibir que una forma simplificada neutralice diferencias PALEO para crear independencia artificial;
- informar métrica global y métrica por estrato;
- registrar abstención, desacuerdo experto y motivo;
- exigir réplica independiente o segunda implementación antes de promoción;
- conservar separadas imagen, lectura diplomática, PALEO, SIMPLIFIED y MORPH.

## 3. Sincronización por hilo

### Motor principal / Validation Suite

- Añadir `FORMULAICITY_STRATUM` como campo derivado de evaluación, nunca como nueva lectura.
- Recalcular métricas por estrato además del agregado.
- Ejecutar un control adversarial `GROUPED-FAMILY-HOLDOUT`.
- No modificar FULL3406, LEAK_GROUP ni los splits congelados: el primer ensayo se ejecuta sobre copia.

### D(E/I)

- Tratar D(E/I) como `LOW_ATTESTATION` hasta disponer de evidencia paleográfica independiente.
- Excluir del entrenamiento todas las variantes del mismo objeto y las familias que revelen indirectamente la respuesta.
- Comparar el rendimiento del split ordinario con un HOLD agrupado por objeto y familia.
- Criterio adversarial: si el resultado cae al nivel de azar o exige la forma simplificada para sostenerse, mantener bloqueo fail-closed.

### KUTUR

- Separar ocurrencias formularias de apariciones raras y variantes R/R1.
- Mantener PALEO-RHOTIC-LOCK-01.
- Prohibir que KUTUR, KUTUŔ o variantes editoriales del mismo objeto caigan en splits distintos.
- Criterio adversarial: una asociación que desaparezca en LOW_ATTESTATION no puede promover función ni semántica.

### IberOS-Write

- Verificar que el generador no aprende respuestas desde frases o plantillas presentes en VALIDACIÓN/HOLDOUT.
- Los significados bloqueados permanecen inaccesibles.
- Reportar por separado reconstrucciones basadas en fórmulas conocidas y reconstrucciones de baja atestiguación.
- No convertir el RETRO-RECONSTRUCTION BENCHMARK en blind test estricto.

### IberOS-Talk

- Sin cambio fonético ni de assets.
- Conservar la procedencia exacta de cada forma y marcar `STALE` si cambia READING/PALEO.
- No usar frecuencia formularia como evidencia de pronunciación.

### Tesis / documentación pública

- Incorporar el protocolo únicamente en metodología, limitaciones y trabajo futuro.
- No elevar métricas oficiales ni reescribir resultados congelados.
- Explicitar que IA y herramientas de imagen son apoyo a decisión, no validación autónoma.

### La Picola / GEO / ICONO

- RTI, SfM y multiespectral pueden registrarse como técnicas candidatas para recuperar trazos o documentar superficies.
- Una reconstrucción 3D no adquiere estatus de evidencia epigráfica por realismo visual.
- Mantener separadas capas DOCUMENTED / INFERRED / HYPOTHETICAL y cautela topográfica.

## 4. Hipótesis lingüísticas: impacto

Sin cambio directo en:

- BI/BIN = 2;
- BAIDES/BAITES y su paradigma;
- BAIDES-BI/IR y BATI-BI/R;
- KI/KIKE;
- KA/KE/KU frente a IKA/IKE/IKU;
- LAKO/LAKOŚ/LAKU;
- IR frente a IRUR;
- ŔOK, SALIR, STIR/IUNSTIR.

El protocolo puede reducir confianza futura si una hipótesis solo mantiene rendimiento dentro de material formulario o mediante duplicados/variantes editoriales.

## 5. Gate de adopción

`KEEP_CANDIDATE` hasta completar:

1. etiquetado reproducible de estratos;
2. auditoría de acuerdo entre dos clasificadores o revisores;
3. prueba `GROUPED-FAMILY-HOLDOUT`;
4. comparación con el split ordinario;
5. regresión completa sin contaminación por `OBJECT_ID/PHYS_ID`;
6. documentación de fallos y abstenciones.

Solo entonces podrá pasar a `ADOPTED_METHOD`. Incluso adoptado, no promoverá por sí mismo ninguna interpretación lingüística.

## 6. Resultado de sincronización

- CORE promotions: 0
- Demotions/reversions: 0
- FULL3406 changes: 0
- Split changes: 0
- Official metric changes: 0
- Public version bump: no

# VALIDATION-01 — Auditoría de calidad del registro maestro (22 octubre 2026)

## Base y reconciliación
La lectura directa de `data/review/validation01_master_physical_objects_v1.csv` arroja **22 filas**, no 21: **20 inscripciones del cribado retrospectivo + 2 piezas referenciadas por Fletcher para Orleyl**. Este documento corrige el conteo comunicado antes. No se equipara el número de filas a piezas físicamente distintas.

## Hallazgos y acciones
- **20/22** filas tienen el campo `physical_group=UNRESOLVED`. Las otras dos corresponden a ORLEYL V y ORLEYL VII y siguen sin verificación fotográfica independiente.
- **0/22** candidatos admisibles a HOLD nuevo; sus columnas `HOLD_eligible` están en `NO`.
- **Una URL vacía**: `IBR-PLM-0002` (Tivissa).
- **Dos URL truncadas** todavía pendientes: `IBR-PLM-0003` (Pech-Maho V) y `IBR-PLM-0005` (Villares V). No sustituir un enlace bibliográfico general por una ficha específica sin cotejo.
- **Un vínculo institucional recuperado**: `IBR-PLM-0010`, el Museo de Arte Ibérico El Cigarralejo, sala VIII, confirma la exposición de un plomo con inscripción greco-ibérica. La página **no aporta una signatura física individual** para atribuir sin otras fuentes. Fuente: https://museosregiondemurcia.carm.es/web/museo-de-arte-iberico-el-cigarralejo/sala-viii.
- La publicación Ferrer 2013 `Els sistemes duals de les escriptures ibèriques` existe en https://doi.org/10.36707/palaeohispanica.v0i13.175, pero no debe reemplazar automáticamente una ficha museística de Pech-Maho V.
- **20** identidades por verificar y **0** auditorías de procedencia concluidas.

## Control reproducible
El nuevo `scripts/validation01_master_audit.py` recorre todas las filas sin mutar datos, detecta IDs repetidos o vacíos, URL ausentes o truncadas, identidades físicas sin resolver y promociones a HOLD sin fotografías, lectura, procedencia y revisor. Se añadieron **cuatro pruebas** en `tests/test_validation01_master_audit.py` para proteger el inventario. Las pruebas están **registradas pero no confirmadas en CI de este commit**.

La regla de validación exige separar los criterios **fuente bibliográfica / objeto físico / lectura paleográfica / condición prospectiva / gold independiente**. Ningún valor se infiere automáticamente por coincidencia de nombre.

## Estado de hitos
M01–M05 acreditados (30 % preparación), M06/M07 pendientes, M10=0 objetos HOLD; VALIDATION-01=`NOT_EVALUATED`. No se aumenta el índice administrativo por tareas adicionales ajenas al cuadro de hitos.

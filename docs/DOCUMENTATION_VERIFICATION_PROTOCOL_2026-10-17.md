# IberOS — protocolo de verificación documental de cada ficha

La finalización editorial de las 38 fichas no implica por sí sola verificación epigráfica ni permiso para reutilizar imágenes o modelos.

## Cuatro puertas independientes

1. **Lectura cotejada con edición original**: registrar editor, edición, página/figura o facsímil, la transcripción reproducida y discrepancias.
2. **Revisión epigráfica independiente**: identificar responsable, fecha, material realmente examinado y decisión motivada. Sin revisión no cambiar el indicador.
3. **Fotografías**: conservar autor, titular, licencia exacta, enlace a la fuente y restricciones. Si falta algún dato, usar enlace al sitio titular en lugar de incorporar el fichero.
4. **Modelos 3D reales**: registrar objeto exacto, institución o autor, URL canónica, licencia/permiso y condiciones de atribución o incrustación. Ante dudas, vincular a la web original en lugar de redistribuir.

El fichero `site/data/fiche_publication_status_v1.json` expone `scientific_documentation_checklist` y `scientific_documentation_pending` por OBJECT_ID. Los campos de verificación empiezan en `false` deliberadamente: no hay una tabla de revisiones específicas y permisos comprobados que autorice a marcarlos `true`.

Las hipótesis y glosas editoriales siguen en `core_interpretations_v1.json` con `meaning_validated=false` y `reading_verified_independently=false`. Ni la visualización de una ficha ni la existencia de un DOI son pruebas de desciframiento. La edición de cualquier objeto conserva la vinculación con sus fuentes; las falsificaciones y pseudoescritura permanecen en controles, no se cuentan como inscripciones independientes.

## Siguiente iteración

Crear y revisar registros objeto por objeto con identificadores de evidencia estables; validar que la prueba adjunta respalda cada cambio de estado antes de publicarlo. No aprobar en bloque las 38 fichas.

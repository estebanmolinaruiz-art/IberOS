# IberOS CORE — Tanda 02, auditoría del corpus (23 octubre 2026)

Se añadió `scripts/iberos_core_corpus_audit.py` y `tests/test_iberos_core_corpus_audit.py` con tres regresiones: ausencia de lectura verificada, fuente negativa vacía y bloqueo de HOLD carente de procedencia.

## Resultado sobre la tabla real del repositorio
- Registros: **22**
- Lecturas completas verificadas: **0/22**
- Grupo físico no resuelto: **20/22**
- URL vacía: **1**, `IBR-PLM-0002`.
- Enlace truncado: **2**, `IBR-PLM-0003` y `IBR-PLM-0005`.
- HOLD acreditados: **0**.
Estos recuentos se han derivado del CSV existente; no se han aportado fuentes externas nuevas en esta tanda.

## Limitaciones
Se trata de un auditor de metadatos, **no de un sistema de OCR de signos, un clasificador fotográfico ni una prueba de traducción**. La fila puede tener imágenes o ediciones publicadas sin que sus campos `full_sign_reading_verified` estén certificados. Las pruebas se han **añadido a GitHub**, sin confirmación de CI en esta tanda.

## Próximos pasos
1. Resolver referencias truncadas de Pech-Maho V y Villares V contra la edición original.
2. Convertir cada ficha en una entidad física auditable: signatura, contexto, fotografía, edición, variantes y notas de incertidumbre.
3. Mantener fuera de HOLD los objetos de desarrollo conocidos.
4. Ejecutar pruebas de regresión de forma aislada y luego en el pipeline continuo.

VALIDATION-01 sigue con M06 y M07 pendientes, avance administrativo 30 %, dictamen científico NOT_EVALUATED.

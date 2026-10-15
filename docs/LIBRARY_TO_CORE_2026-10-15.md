# IberOS: biblioteca ampliada → bandeja científica CORE

La biblioteca pública puede crecer sin afectar al corpus curado de 38 objetos ni al benchmark congelado. Desde 2026-10-15 están implementados `src/iberos/library_ingest.py` y `scripts/import_library_to_core.py`.

## Contrato de entrada

Exportar registros como JSONL, uno por línea, con al menos `title` y `source_url` HTTPS. `physical_object_id` es opcional y **solo** se vincula automáticamente si coincide exactamente con un `OBJECT_ID` ya curado. `independence_evidence` es una alegación documental pendiente de contrastar, nunca validación automática.

Ejemplo de formato (ficticio; no constituye evidencia):
```json
{"title":"Edición de ejemplo","source_url":"https://example.org/edicion","physical_object_id":"IBR-PLM-0002"}
```

Ejecutar desde la raíz del repositorio:
```bash
python scripts/import_library_to_core.py --input biblioteca_export.jsonl --output site/data/library_core_inbox_v1.json
```

El informe deduplica documentos repetidos según título+URL. Separa `DOCUMENTARY_EDITION_OF_CURATED_OBJECT` de `UNMATCHED_OBJECT_REVIEW`. **Dos ediciones de un objeto son dos documentos, pero no dos testimonios independientes.** Cualquier objeto nuevo, lectura, identificación física o alegación de independencia requiere revisión explícita y un identificador canónico asignado conforme al protocolo.

Todos los registros se mantienen con `reading_verified=false`, `physical_independence_verified=false`, `ready_for_core_execution=false`, `counts_as_new_independent_object=false`. El motor no ejecuta reglas científicas ni publica transcripciones a partir de la ingesta.

## Estado de integración

El puente Python y su exportador existen en GitHub. **Aún no se ha localizado y conectado un archivo real de exportación de la biblioteca ampliada**; no se deben anunciar cientos o miles de testimonios científicos añadidos por este desarrollo. La web puede alojar el resultado JSON una vez validado su origen y creado el export, pero no debe mostrarlo como CORE validado. Siguen intactas las autoridades C594/C474/C539/C541.

## Próximo paso

Incorporar desde el proceso de construcción de la biblioteca su catálogo real (con licencia/procedencia, ids documentales y registro de variantes), ejecutar importador y auditar duplicados y enlaces antes de incorporarlo a `site/data`. Después estudiar las observaciones de piezas individuales por lotes de revisión.

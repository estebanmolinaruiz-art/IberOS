# IberOS — lecturas revisadas de Biblioteca al CORE (16-10-2026)

El puente `analyze_library_readings(records)` consume **registros documentales suministrados externamente**, vinculados a un `OBJECT_ID` del corpus curado, y produce candidaturas de dominios semánticos no validadas.

Cada línea JSONL requiere `reading_id` único, `object_id`, y lista `segments` con `form`, `reading_source`, `reading_reviewed`. Solo una lectura con `review_status="APPROVED_READING"` y `review_reference` no vacío permite que el motor considere los segmentos marcados explícitamente como revisados. Cualquier otro estado causa abstención. Una aprobación declarada en JSONL es **un metadato editorial sin verificación criptográfica ni cotejo físico**.

Uso:
```bash
python scripts/analyze_library_readings.py --input lecturas_revisadas.jsonl --output site/data/library_reading_analysis_v1.json
```

No se crea ningún archivo con evidencias nuevas al instalar el módulo. No se han identificado datos auténticos de la biblioteca ampliada listos para la ejecución de este contrato. Salidas: `suggestions` hipotéticas, `translation_validated=false`, `automatic_core_promotion=false`. El sistema no genera traducciones completas ni presupone independencia de lecturas, objetos o fuentes. Las autoridades C594/C474/C539/C541 siguen congeladas.

**Siguiente tarea**: localizar la exportación real de lecturas y decisiones editoriales, verificar sus fuentes y vincularla a este comando; revisar el lote antes de publicar resultados individuales en las fichas.

# IberOS — lecturas revisadas de Biblioteca al CORE (16-10-2026)

El puente `analyze_library_readings(records)` consume **registros documentales suministrados externamente**, vinculados a un `OBJECT_ID` del corpus curado, y produce candidaturas de dominios semánticos no validadas.

Cada línea JSONL requiere `reading_id` único, `object_id`, y lista `segments` con `form`, `reading_source`, `reading_reviewed`. Solo una lectura con `review_status="APPROVED_READING"` y `review_reference` no vacío permite que el motor considere los segmentos marcados explícitamente como revisados. Cualquier otro estado causa abstención. Una aprobación declarada en JSONL es **un metadato editorial sin verificación criptográfica ni cotejo físico**.

Uso:
```bash
python scripts/analyze_library_readings.py --input lecturas_revisadas.jsonl --output site/data/library_reading_analysis_v1.json
```

No se crea ningún archivo con evidencias nuevas al instalar el módulo. No se han identificado datos auténticos de la biblioteca ampliada listos para la ejecución de este contrato. Salidas: `suggestions` hipotéticas, `translation_validated=false`, `automatic_core_promotion=false`. El sistema no genera traducciones completas ni presupone independencia de lecturas, objetos o fuentes. Las autoridades C594/C474/C539/C541 siguen congeladas.

**Siguiente tarea**: localizar la exportación real de lecturas y decisiones editoriales, verificar sus fuentes y vincularla a este comando; revisar el lote antes de publicar resultados individuales en las fichas.

## Integración editorial real — 16-10-2026

El exportador `scripts/export_web_core.py` consume ahora las seis entradas candidatas de `site/data/ficha-enrichment-featured.json` y crea `site/data/core_interpretations_v1.json` durante el despliegue. Solo las cuatro entradas que tienen cita editorial no vacía se publican como hipótesis. Cada hipótesis conserva el texto interpretativo **ya existente** en la ficha destacada, la cita, su evidencia y sus objeciones. El panel «Posible traducción» de la ficha pública puede consultarlas sin inventar nuevas frases.

**Limitación esencial:** estas son hipótesis editoriales previas, no registros JSONL de lecturas revisadas por el puente `analyze_library_readings`. No se han introducido en el motor semántico como nuevas observaciones ni se ha comprobado independientemente la transcripción original. El export marca `reading_verified_independently=false`, `meaning_validated=false` y `translation_validated=false`; las restantes 34 piezas muestran abstención.

La integración real con la biblioteca ampliada a escala completa requerirá extraer transcripciones exactas de sus ediciones, asignar un vínculo verificable a la pieza física y documentar cada revisión individual.

Verificación: IBR-MUS-0001 e IBR-LAP-0005 tienen el campo `citation` vacío, por lo que quedan excluidas de esta exportación. Se conservan como fichas editoriales, pero no se inventan fuentes ni se cuentan como propuestas con procedencia suficiente.

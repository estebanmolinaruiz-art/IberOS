# IberOS — expansión masiva, estado de adquisición (2026-10-19)

## Fuente candidata
- David Folch Flórez, *Iberian Corpus*, en https://www.ibers.cat/corpuscast.html
- Licencia declarada: CC BY-NC-SA 3.0, atribución a David Folch Flórez y Carme J. Huertas.
- Página verificable describe archivo Excel y tipografía Huertas: marcas subrayadas (lecturas dudosas), negrita (alternativas); se debe conservar esa distinción al exportar.
- En la inspección accesible no hay enlace directo a Excel en la página consultada, por lo que **no hemos obtenido ni importado el fichero**. No afirmar miles de registros descargados.

## Capacidad realizada
- `scripts/import_iberian_bulk_csv.py` importa CSV de procedencia identificada, con columnas `reference, transcription_raw` y metadatos opcionales.
- Conserva texto raw, fuente, licencia, notas, y control de duplicados exactos por fuente-referencia-texto.
- Estado de cada fila: `RAW_UNREVIEWED`, `te_status=UNKNOWN`, `hold_eligible=NO`.
- Prueba automatizada genera 2500 **filas SINTÉTICAS**, únicamente para carga técnica. **No son 2500 lecturas arqueológicas nuevas.**
- Origen externo previamente registrado: 12 registros codificados en `data/review/validation01_external_opaque_readings_batch01.csv`, no revisados ni descodificados.

## Uso una vez obtenido un CSV legítimo
```bash
python scripts/import_iberian_bulk_csv.py fuente.csv salida_staging.csv --source ibers-cat-folch-2024 --license CC-BY-NC-SA-3.0
```
No usar archivos Excel exportados a CSV si se pierden los marcadores de subrayado/negrita; convertir estos estados en columnas explícitas y preservar el original para auditoría. No instalar ni redistribuir archivos de fuentes sin revisar condiciones.

## Bloqueos
- Archivo masivo fuente realmente accesible: NO
- Millar de inscripciones fuente documentadas importadas: NO
- Descifrado de glifos de tipografía especializada: NO
- VALIDATION-01 blind: sigue bloqueado

Siguiente acción: descargar la hoja de cálculo directamente del titular, o solicitarla a `correu@ibers.cat`, conservar su licencia y marcas de edición; después procesar y verificar recuentos antes de informar de miles.

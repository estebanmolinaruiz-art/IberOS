# IberOS — comparación de posibles traducciones (15-10-2026)

El CORE incorpora `compare_interpretations(object_id, reading, proposals)` para **presentar alternativas semánticas documentadas** sin confundir hipótesis con traducción científica validada. Complementa el módulo ya existente `reconstruction.py`; no sustituye la autopsia, las reglas prospectivas ni las lecturas paleográficas.

Se requiere `OBJECT_ID` curado; `reading = {transcription, source}` y una lista de hipótesis con `id`, `possible_translation`, `sources`, `supporting_observations` y `objections`. Se impiden ids de hipótesis duplicados, lectura sin fuente y glosas sin referencia. Las entradas deben proceder de la revisión editorial; **el motor no inventa significados**.

El resultado presenta para cada opción la traducción posible, argumentos a favor, objeciones, fuentes y capa `HYPOTHESIS`. El orden favorece solo **completitud documental**, nunca una probabilidad semántica; `estimated_probability=null`, `meaning_validated=false`, `translation_validated=false` y `automatic_core_promotion=false`. El indicador `reading_verified_independently=false` advierte que una referencia declarada no es revisión real.

Ejemplo sintético, NO ibérico histórico:
```python
from iberos import compare_interpretations
result = compare_interpretations(
 "IBR-PLM-0002",
 {"transcription":"[lectura editorial]", "source":"[edición identificada]"},
 [{"id":"H1","possible_translation":"[significado estimado]",
   "sources":["[edición y discusión bibliográfica]"],
   "supporting_observations":["[paralelo]"],
   "objections":["[anclaje semántico independiente pendiente]"]}])
```

Siguiente hito: cotejar hipótesis reales sobre segmentos de inscripciones revisadas y mostrar estas alternativas en la ficha visual destacada, junto con los controles y el derecho a abstenerse. No se han alterado las métricas científicas ni las reglas C594/C474/C539/C541.

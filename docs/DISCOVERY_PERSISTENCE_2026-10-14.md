# IberOS — bandeja persistente de descubrimientos científicos

Fecha 2026-10-14. Implementación: `src/iberos/discovery_store.py`, interfaz Python pública `append_discoveries`, `classify_discovery`.

## Alcance efectivamente implementado
- Persistencia local JSONL, deduplicación por identificador estable `DISC-...` heredado de `review_discoveries`, relectura de entradas existentes, escritura de sustitución atómica con fichero temporal.
- Ruta de revisión explícita entre GEO, PALEO, MORPH, LEXSEM, TRACE e INFER. Si el registro de entrada no especifica módulos, se enruta a TRACE; no se infieren disciplinas ni significados a partir del título.
- Entradas siempre `UNVERIFIED_INBOX`, `eligible_for_core=false`, `automatic_core_promotion=false`; estado de revisión `AWAITING_HUMAN_REVIEW`, hipótesis `NOT_TESTED`.
- Rechazo de fuente sin URL HTTPS, nombres de módulo ajenos al catálogo o libro JSONL preexistente corrupto. Pruebas en `tests/test_discovery_store.py`.

## Uso local
```python
from iberos import append_discoveries
r = append_discoveries("data/inbox/discoveries.jsonl", [
    {"title": "Artículo a contrastar", "url": "https://example.org/paper",
     "modules": ["PALEO", "TRACE"]}
])
print(r)
```

El ejemplo es sintético; **no se han ingerido publicaciones reales por este cambio**. El fichero de ejemplo no constituye un corpus validado.

## Distinciones indispensables
1. El seguimiento diario de literatura científica envía avisos; **no está conectado directamente a la persistencia GitHub**.
2. El registro JSONL se actualiza solo cuando se ejecuta la función en un entorno con almacenamiento escribible; instalar esta versión del código no lanza un crawler.
3. La bandeja sirve para **autoinformación asistida**, no autoaprendizaje epigráfico no supervisado ni entrenamiento del modelo. El CORE no incorpora automáticamente hipótesis, traducciones o cambios de métricas.
4. Antes de aprobar un descubrimiento se requieren fuente real, lectura crítica, identificación de la inscripción, independencia documental y contraste experto. Una búsqueda diaria no sustituye esto.
5. Siguiente fase: adaptadores de fuentes científicas abiertas con actualización programada verificable y propuesta de revisión con historial; control de licencias y DOI.

Autoridad científica congelada: C594/C474/C539/C541. `ROK-RECIPIENT-02=OPEN`. Benchmark y métricas sin modificación intencional.

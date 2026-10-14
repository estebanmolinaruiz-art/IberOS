# IberOS — vigilancia bibliográfica OpenAlex

Implementado 2026-10-14: `src/iberos/openalex_adapter.py`, `scripts/sync_discoveries.py`, `.github/workflows/discovery-watch.yml` y `tests/test_openalex_adapter.py`.

**Qué hace:** consulta la API pública OpenAlex (metadatos, búsqueda orientativa `Iberian inscriptions epigraphy`), mapea título, URL HTTPS (DOI o landing page), fecha y fuente; inserta los candidatos en el registro JSONL mediante `append_discoveries` y conserva el estado `UNVERIFIED_INBOX`. No obtiene lecturas epigráficas comprobadas ni asegura que todos los resultados sean ibéricos relevantes. El etiquetado inicial PALEO/TRACE es una ruta de revisión, no una evaluación científica de las fuentes.

**Automatización GitHub:** la tarea `scientific-discovery-watch` declara una ejecución diaria a las 07:30 UTC y admite `workflow_dispatch`. Crea un artefacto `openalex-unverified-candidates` conservado 30 días. Usa permisos `contents:read`, no commits, no PR y ninguna modificación de CORE, corpus curado o métricas. Su ejecución en red y la disponibilidad de OpenAlex deben verificarse en GitHub Actions; que el workflow esté creado no garantiza que haya generado resultados.

**Ejecutar manualmente:** `python scripts/sync_discoveries.py --out /tmp/iberos-openalex.jsonl --limit 20`. La deduplicación es local al archivo de salida: el artefacto efímero de CI no representa una historia acumulada entre días; para eso se necesitará un repositorio persistente revisado. La automatización conversacional de alertas es distinta y no alimenta este artefacto.

**Control científico:** resultados siempre candidatos bibliográficos sin promoción automática; corroboración de DOI, autores, título, objeto, independencia documental, licencias y revisión experta exigida antes de integrarse. Las búsquedas genéricas pueden recuperar ruido o duplicados con diferentes URLs. `ROK-RECIPIENT-02=OPEN`; métricas congeladas C594/C474/C539/C541 sin cambios.

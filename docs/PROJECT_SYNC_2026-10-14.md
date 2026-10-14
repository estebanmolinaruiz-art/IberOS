# IberOS — sincronización transversal de procesos y versiones (2026-10-14)

## Regla central
GitHub `estebanmolinaruiz-art/IberOS`, rama `main`, es la **fuente técnica compartida** para todos los hilos. Este documento fija el mapa de módulos, dependencias y estado de integración. Los hilos de ChatGPT mantienen su propio contexto y **no se reescriben ni se sincronizan automáticamente entre sí**: cada responsable debe consultar este documento y el último commit antes de desarrollar.

## Versión vs. desarrollo
- **Paquete publicado:** `pyproject.toml` sigue identificando `iberos==1.0.1`. No se ha comprobado una nueva publicación PyPI o Zenodo por esta sincronización.
- **Rama principal:** contiene cambios posteriores a la versión publicada; NO equivale a una nueva release. Distinguir `main/dev` de versión `1.0.1`.
- **Ciencia congelada:** C594 / C474 / C539 / C541; CORE 27/45, CORE+INFER 28/45, ROK-RECIPIENT-02 abierto. No subir indicadores por mejoras técnicas.

## Matriz operativa por hilo
| Hilo de trabajo | Autoridad y archivos canónicos | Funciones disponibles en main | Pendiente de integración comprobada |
|---|---|---|---|
| CORE — investigación | `src/iberos/core.py`, `rule_catalog.py`, `rule_execution.py`, `object_rule_audit.py`, `prediction_compare.py` | Gates científicos, catálogo 12 entradas, cuatro ejecutores BI/ROK/KA/PALEO, auditoría por objeto, cotejo científico; no promoción automática | Entradas epigráficas verificadas para ejecutar reglas por objeto; ejecutar contrastes prospectivos reales |
| GEO y multimódulo | `src/iberos/geo.py`, `multimodule.py`, `site/data/geo_atlas_nodes.json` | Seis referencias de Atlas, consulta contextual Python, estado de seis módulos | Enlaces GEO con identidad de piezas verificada; unión funcional PALEO/MORPH/LEXSEM/INFER más allá de metadatos |
| WEB pública | `site/`, `site/atlas/index.html`, `site/fichas/`, `site/laboratorio/`, `site/modelos3d/` | Secciones e interfaz de investigación; Atlas consume el JSON GEO | Verificar que fichas acordadas incluyan pieza, signos, análisis y posible traducción en formato arqueológico; conectar salidas CORE sin atribuir traducción automática |
| APP-Móvil / Write / Talk | Artefactos de este módulo pueden residir en otros hilos/ZIP no incluidos en esta auditoría; inspeccionar antes de declarar versión | No se certifica paquete instalable ni build sincronizado por este documento | Recuperar ZIP/artefactos maestros y verificar compatibilidad de esquema, versiones y compilación |
| Descubrimientos / Red Hermana | `discovery.py`, `discovery_store.py`, `openalex_adapter.py`, `discovery_link.py`, `prediction_compare.py`; `.github/workflows/discovery-watch.yml` | Ingesta bibliográfica, cola de revisión, deduplicación y cotejo con predicciones | Confirmar ejecución real del workflow y archivado persistente; no entrenar ni promover evidencia sin revisión |
| Publicación / EpiHub | `pyproject.toml`, `docs/ARCHITECTURE.md`, `docs/BENCHMARK.md`, workflows de release | Paquete 1.0.1 y benchmark público de 38 objetos | Revisión de checklist académico, release y web estable antes de anunciar actualización |

## Protocolo de sincronización para cualquier hilo
1. Leer esta matriz, `docs/PROJECT_SYNC_2026-10-14.md`, `docs/BENCHMARK.md` y la última rama `main`.
2. Identificar archivos afectados y responsable del módulo. **No modificar el mismo archivo desde dos hilos sin comparar SHA** y volver a leer antes del commit.
3. Implementar cambios en su fuente correspondiente; añadir pruebas; comprobar GitHub Actions; registrar commit y efectos colaterales.
4. Actualizar esta matriz cuando cambie una interfaz común o el estado de validación, y avisar en el hilo respectivo qué commit debe incorporar.
5. No presentar una mejora en `main` como desplegada en WEB, APP o PyPI hasta verificarlo en cada destino.
6. Cada hilo conserva su autoridad científica / funcional; la matriz no sustituye una aprobación de ficha o una prueba externa.

## Contrato de intercambio acordado
- Identificador canónico `OBJECT_ID`.
- Metadatos de objeto + GEO contextual + módulos y reglas candidatas/evaluadas.
- Separar `EVIDENCE`, `INFERENCE`, `HYPOTHESIS` y `UNRESOLVED` en ficha y en respuestas JSON.
- Todos los resultados experimentales: `automatic_core_promotion=false`, con fuente, estado y controles de independencia.
- Evoluciones de esquema: versionar explícitamente y añadir test de compatibilidad WEB/APP antes de migrar.

## Actualizaciones recientes de main
- Motor multimódulo, GEO compartido y bandeja de descubrimientos.
- Comparación externa de predicciones con hash y guardas de prioridad.
- Catálogo de doce entradas y auditoría por objeto.
- Ejecutores científicos BI, ROK, PALEO-RHOTIC y KA-DIRECTION, validados técnicamente en GitHub Actions en una ejecución previa; no existe todavía integración automática de ese ejecutor en todas las fichas web.
- Estado del paquete en `pyproject.toml` revisado: `1.0.1`, sin incremento de release.

**Esta sincronización es documental y técnica dentro de GitHub; no es una modificación automática de los mensajes pasados de otros hilos.**

## Integración transversal CORE → ficha WEB (tanda 2026-10-14)

- `scripts/export_web_core.py`: exporta de forma determinista auditorías científicas para los **38 objetos curados** utilizando `audit_object_rules` y `research_pipeline`. El producto es `site/data/core_object_audit_v1.json` **generado durante el despliegue**; no se ha editado a mano en el repositorio.
- `.github/workflows/pages.yml`: instala el paquete desde main, genera el JSON y exige 38 objetos antes de publicar GitHub Pages. Así cada despliegue utiliza el CORE del mismo commit, evitando duplicar las reglas como lógica web independiente.
- `site/ficha/index.html`: incorpora el panel «Análisis CORE · Reglas y módulos». Muestra estados de seis módulos, guardas generales y reglas candidatas derivadas de etiquetas, **no traducciones automáticamente probadas**. Si el JSON no carga, la ficha permanece accesible y muestra una advertencia.
- Se corrigió asimismo una concatenación defectuosa en el template de HTML que podía impedir la creación de los paneles científicos.
- `tests/test_web_core_export.py`: vigila el conteo, inclusión de Tivissa y la prohibición de promoción científica.

**Alcance del cierre:** WEB + CORE sincronizados a nivel de **auditoría de metadatos y reglas**, NO ejecución epigráfica automática por pieza. La APP móvil todavía no consume el exportador y requiere una tarea propia. Paquete distribuido `iberos 1.0.1` permanece sin nueva release. El estado del deploy debe verificarse en GitHub Actions antes de calificarlo como publicado.

**Próximo contrato necesario:** intercambio versionado de lectura documental verificada, referencias físicas y resultados de `execute_rules` para mostrar en la ficha estados `BLOCKED`/`OPEN`/`REVIEW`, sin confundir indicadores científicos con decisiones editoriales.

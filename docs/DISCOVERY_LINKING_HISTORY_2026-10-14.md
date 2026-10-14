# IberOS — historial y vínculos bibliográficos conservadores
Fecha: 2026-10-14.

## Nuevas capacidades
1. `src/iberos/discovery_link.py`: `proposed_object_links(records)` propone referencias a objetos **solo** cuando el título, resumen declarado o identificadores contienen un ID curado literal `IBR-XXX-0000`. No hay coincidencia difusa por localidad, yacimiento o familias. La marca es `PROPOSED_UNVERIFIED`, nunca prueba lingüística.
2. `.github/workflows/discovery-watch.yml`: antes de ejecutar la búsqueda OpenAlex diaria restaura el JSONL acumulado de GitHub Actions cache y tras completarla guarda una nueva clave por `run_id`. El registro sigue publicado como artefacto de 30 días. El repositorio se mantiene sin permisos de escritura (`contents:read`).
3. `tests/test_discovery_link.py`: comprueba ID explícito y rechazo de inferencias por nombre geográfico.

## Límites prácticos
- El cache es **best-effort**, está sujeto a expiración, evicción, concurrencia y alcance de rama; **no constituye un archivo histórico permanente**. La deduplicación compara título+URL, no identidad científica de DOI normalizada.
- La vigilancia de GitHub genera candidatos; **no extrae ni lee críticamente los artículos completos**, no incorpora lecturas verificadas ni reentrena modelos.
- Los identificadores IberOS casi nunca figuran en la literatura externa; con ello la vinculación será necesariamente escasa hasta añadir concordancias epigráficas documentadas (MLH/Hesperia/Corpus), con revisión experta.
- La automatización de alertas de ChatGPT y la de GitHub son procesos distintos.
- Siguiente etapa: persistencia duradera versionada en rama separada o base de datos, normalización DOI, informe de diferencias entre ejecuciones y tablas de concordancia verificadas.

## Dictamen
`ROK-RECIPIENT-02=OPEN`, `automatic_core_promotion=false`, autoridad C594/C474/C539/C541 sin cambios. Un resultado bibliográfico es una propuesta de investigación, no una traducción ni una nueva regla científica confirmada.

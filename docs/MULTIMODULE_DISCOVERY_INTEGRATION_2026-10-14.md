# IberOS — coordinación de módulos y novedades científicas

Fecha: 2026-10-14. **Alcance: primera integración técnica**, no recuperación íntegra de motores históricos aún no localizados.

## Coordinador por objeto
`src/iberos/multimodule.py`: `research_pipeline(OBJECT_ID)` produce una estructura común para `GEO`, `PALEO`, `MORPH`, `LEXSEM`, `TRACE` e `INFER`, usando el registro curado, las funciones GEO y el catálogo de reglas. Los estados son deliberadamente desiguales:
- GEO: referencia de Atlas, exclusivamente contexto.
- PALEO: etiqueta documental `PALEO_Status`; no OCR ni autopsia.
- MORPH: familias y activación declarada; no extracción morfológica automática.
- LEXSEM: catálogo e hipótesis, sin asignación automática de traducciones.
- TRACE: grupo de dependencia e inclusión; no sustituye auditoría de independencia completa.
- INFER: pendiente de validación independiente y sin candidato semántico.

## Ingesta de novedades
`src/iberos/discovery.py`: `review_discoveries(records)` comprueba título y URL HTTPS, elimina duplicados determinísticamente por título+URL y devuelve registros `UNVERIFIED_INBOX`; todos con `eligible_for_core=false`. No descarga contenidos, no verifica automáticamente artículos ni escribe el catálogo curado o el benchmark.

## Seguimiento externo
Automatización diaria de novedades científicas, activada por solicitud del investigador: revisa literatura, detecta cambios significativos y comunica fuentes y DOI cuando los encuentra. Es **notificación externa**, no ingestión autónoma en GitHub ni una máquina que aprenda nuevas semánticas. La incorporación efectiva al CORE exigirá proceso reproducible con autenticidad documental, revisión epigráfica, testigos independientes, gate prospectivo y aprobación científica explícita.

## Protección y pruebas
`tests/test_multimodule_discovery.py` verifica presencia de seis salidas, candados semánticos, error por objeto inexistente y cuarentena de noticias sin fuente o duplicadas. Estado del CI: verificar por ejecución posterior al último commit.

## Fases pendientes para integración completa
1. Recuperación de código histórico adicional y estructura de motores independientes.
2. Protocolos de salida para PALEO/MORPH/LEXSEM e interfaz conjunta con la web.
3. Conector trazable de descubrimientos a fuentes académicas, almacenaje inmutable, revisión humana y comparación de versiones.
4. Revisión externa antes de toda promoción científica; pruebas prospectivas independientes.

**Autoridad congelada C594/C474/C539/C541. CORE=27/45, CORE+INFER=28/45. Estas no son tasas de desciframiento.**

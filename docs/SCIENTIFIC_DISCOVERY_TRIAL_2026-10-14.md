# IberOS — prueba de autoinformación científica y comparación crítica

Fecha: 2026-10-14. Evidencia externa consultada en tiempo real y sometida a revisión conservadora.

## Prueba 1: proveedor bibliográfico
Petición pública a `https://api.openalex.org/works?search=Iberian%20inscriptions%20epigraphy&per-page=2`: **respuesta real** con metadatos `results`, `display_name`, `doi`, `publication_date`, `primary_location`. El proveedor es accesible desde la consulta realizada, pero la respuesta incluye materiales de años anteriores: los resultados del buscador **no acreditan nuevos descubrimientos por sí solos**. El módulo instalado `src/iberos/openalex_adapter.py` utiliza la misma API; aún no consta primera ejecución del workflow programado en GitHub Actions.

## Prueba 2: ejecución programada
Consulta pública a `api.github.com/repos/estebanmolinaruiz-art/IberOS/actions/workflows/discovery-watch.yml/runs`: **total_count=0**, sin ejecuciones. Por tanto no afirmar que se haya efectuado una sincronización automatizada real ni que exista historial temporal persistido por la tarea.

## Primeros trabajos identificados mediante verificación web, no como promociones
1. **Luján Martínez, Eugenio R. / Ngomo Fernández, Esteban (2026)**: *Un vaso de plata del Museo Británico con signos ibéricos*, *Veleia* 43, 155–170. DOI `10.1387/veleia.27983`. La descripción bibliográfica afirma que se detectaron signos ibéricos antes no reconocidos en un cuenco de Córdoba conservado en el British Museum. Ruta de revisión `PALEO, TRACE, GEO`. No se ha realizado autopsia fotográfica, ni se ha añadido el objeto al registro canónico.
2. **Lambert, Jack Thomas (2025)**: *Aspectos paleográficos de la epigrafía ibérica rupestre de Cerdaña y su contexto histórico-arqueológico*, *Palaeohispanica* 25, 203–226, DOI `10.36707/palaeohispanica.v25i1.709`. Resumen de autor sobre rasgos duales y variación regional paleográfica. Ruta `PALEO, GEO, TRACE`. No constituye una regla GEO→lengua validada.

Registro reproducible inicial de fuentes: `data/inbox/research_candidates_2026-10-14.jsonl`, **2 entradas explícitas** con `UNVERIFIED_INBOX`, `eligible_for_core=false`, `automatic_core_promotion=false`.

## Contraste científico y próxima decisión
Una publicación de 2026 en *Archivo de Prehistoria Levantina* relativa a La Bastida de les Alcusses plantea una dirección `-ka` / `-ku` y el valor de `bi`, según el texto indexado por la editorial. **Es una interpretación publicada que podría generar hipótesis rivales**, pero no supera por sí misma los gates independientes `KA-DIRECTION` y `BI-DISAMBIG`. Antes de añadirla como evidencia de gate, fijar referencia bibliográfica inequívoca, transcripción diplomática y criterios predictivos previos al contraste. No se ha incorporado a la bandeja DOI hasta verificarlos.

Siguiente tarea experimental: probar manualmente el workflow de GitHub Actions, consultar su archivo de salida y comprobar pertinencia, falsos positivos y duplicados en términos DOI; después reproducir para ROK/SALIR solo sobre testimonios independientemente catalogados.

**Estado de autoridad invariable:** C594/C474/C539/C541. `ROK-RECIPIENT-02=OPEN`. El proyecto no ha aumentado con estos registros el número de evidencias epigráficas validadas.

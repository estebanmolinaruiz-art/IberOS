# IberOS — VALIDATION-01: auditoría de fuentes alternativas y ruta de resolución
Fecha: 2026-10-19
Estado científico: **NOT_EVALUATED**.

## Hallazgo crítico
La edición de Fletcher 1981 registra dos series distintas: `BITEROKETETINE` (Orleyl V, F.9.5) y `BASBITEROKETINE` (Orleyl VII-B, F.9.7). Deben seguir separados objeto, línea física, variante editorial y segmentación. El prefijo `BAS` presenta duda de frontera léxica según Fletcher.

La tesis de **Eduardo Orduña (2006)**, *Segmentación de textos ibéricos y distribución de los segmentos*, aparece en catálogo de UNED y web del autor; un texto accesible de la tesis advierte un **error de inclusión de `biteŕoketine` en Orleyl 5.3, duplicado con Orleyl 7**, y distingue la secuencia `biteŕokete-tin-e` en Orleyl 5 de `bas-biteŕoke-tin-e` en Orleyl 7. **Debe comprobarse ese pasaje en la edición original de la tesis antes de usarlo como fe de erratas definitiva.**

Hay una segunda distinción clave: el artículo de Orduña (2009), **«De nuevo sobre el sufijo ibérico -te»**, trata `-te` en entornos nominales y formulares (frente a `-en`). Esto NO implica que el `TE` interno de `-TETINE` sea el mismo morfema. Serían hipótesis distintas y requieren controles diferentes.

## Fuentes con acceso localizado
1. Fletcher 1981: PDF aportado por el usuario, figuras 22 y 25 y lectura editorial.
2. Orduña 2006: tesis UNED registrada y web de publicaciones del autor; comprobar documento original.
3. Orduña 2009: PDF abierto https://ifc.dpz.es/recursos/publicaciones/29/54/34orduna.pdf (PalHisp 9, 501–514).
4. Banco de datos Hesperia: fichas de epigrafía con texto, aparato crítico, imágenes y metadatos; buscar identificadores físicos Orleyl bajo CS.21 y cotejar F.9.5/F.9.7.
5. Untermann, MLH III (1990): estándar de lectura y signos para comprobar F.9.5 y F.9.7, pendiente localizar material ilustrado.
6. Amics dels Ibers, «Ploms d'Orlell» (2024): transcripción alternativa `basbiteŕoketine` y `biteŕoketetine`; útil como control de variantes, no como demostración de traducciones propuestas.

## Ruta que realmente desbloquea VALIDATION-01
A. Construir matriz de **dos objetos físicos** y dos ediciones con fotografías/calcos, fila física, signos y dudas. No transcribir automáticamente por OCR ni por fuente tipográfica.
B. Revisar documentalmente la segmentación `biteŕokete-tin-e` y `bas-biteŕoke-tin-e`. Registrar hipótesis rivales (inserción de `te` vs fronteras de morfema), sin decidir por mera semejanza.
C. Separar **VALIDATION-01-TE-MASK** (predicción estructural de signo) y **VALIDATION-01-TE-MORPH** (predicción de función del sufijo `-te` con gold independiente), evitando sustituir una por otra.
D. Usar Orleyl exclusivamente DEVELOPMENT. No confundir otras ediciones del mismo objeto con HOLD.
E. Antes de pasar a HOLD, fijar baseline y métrica y obtener como mínimo 20 objetos físicos nunca usados, con revisión independiente.
F. La combinación de un diccionario y otro libro **no es independencia experimental** si describen los mismos dos plomos.

## Limitaciones honestas
No hay nueva línea de signos completa cotejada por dos revisores, no existe aún predictor congelado, no hay HOLD ciego, no se ha puntuado superioridad. Los enlaces de acceso son bibliografía priorizada, no transcripciones añadidas al CORE.

Ver `data/review/validation01_external_evidence_sources_2026-10-19.csv` para tabla operativa.

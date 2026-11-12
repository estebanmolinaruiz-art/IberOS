# IberOS · PICOLA–GEO — Auditoría cruzada de inventarios, archivos y fuentes web (11-11-2026)

**Firma visible:** IberOS · PICOLA–GEO. **Objeto:** inventarios v0.1/v0.2/v0.3 (Biblioteca), fichas públicas y tablas GitHub v0.3–v1.2, 66 registros de `main`, matriz de 15 fichas y referencias espaciales, frente a fuentes primarias y secundarias accesibles en Internet. **Alcance limitado:** búsqueda extensa y priorizada, no un rastreo literal de toda la web ni de todos los materiales realmente excavados; no se demuestra que 66 sea el total del yacimiento.

## 1. Control cuantitativo reproducible
- Conservados **66 registros**, con **14 PRIORITARIO_IBERICO, 1 REVISION_PENDIENTE y 51 ARCHIVO_NO_PRIORITARIO**.
- Tabla maestra conciliada `site/data/picola-catalogo-maestro-visual-v1.3.tsv`: **29 columnas, 66 datos**. Se conservan intactos identificadores, conjunto y fases de la tabla v1.2.
- **12 registros** confrontados directamente con publicaciones y documentados en nuevas columnas de auditoría (otros **54 siguen pendientes de cotejo individual primario** en esta ronda; no se afirma que estén mal).
- **15 fichas prioritarias/revisión**, de ellas **6 con dimensiones documentadas**: MARQ-001…006. **1 UE de la selección**: MARQ-002→2072.
- **15 de los 66** tienen medidas publicadas incorporadas en v1.3 (no significa que las otras piezas no tengan dimensiones en la bibliografía).
- **32 entradas** portan una UE numérica textual en el maestro: 1 ficha ibérica activa (UE2072), 3 auxiliares romanas del MARQ (UE2053, 2055, 2107) y 28 registros del archivo UE488. **Esos números NO equivalen a geometría de UE o pin GIS**.
- **0 geometrías de hallazgo aprobadas; 0 pins**. Sin nuevas fotos republicadas ni permisos inferidos.
- Para 16 referencias (UE/ambiente) documentales, crear `site/data/picola-control-contextos-ue-v1.tsv`. Una UE contextual conocida en un artículo no debe añadirse arbitrariamente a la ficha de un objeto.

## 2. Datos previamente presentes en fuentes pero omitidos de tabla visual
Datos recuperados del catálogo MARQ *Santa Pola. Arqueología y Museo* (2012–2013):
- **MARQ-005**, ánfora ibérica, n.º 105, Ribera 13, altura **410 mm** y anchura **250 mm**, p. impresa **260**.
- **MARQ-006**, fíbula bronce, S 94.E40.860.20, longitud **45 mm**, anchura **20 mm**, p. 260. El catálogo imprime **IV d. C.** junto a Puerto Ibérico (Picola). **Mantener la fecha literal** y revisión abierta; no convertir por intuición a siglo IV a. C.
- **MARQ-007**, plato africana D Hayes 50B, **360 mm de diámetro y 60 de altura**, inventario con sufijo 2001-5292, p. 261.
- **MARQ-008**, olpe tradición ibérica **250 × 170 mm**, inv. PI/82-271, p. 261, fechado I–II d. C. No pertenece automáticamente a la fase ibérica porque la tradición formal sea ibérica.
- **MARQ-009**, vaso Mayet XXIV **90 × 85 mm**, inv. SP-PAL85/2561, p. 262, ya archivado por fecha I d. C.
- **MARQ-010**, lucerna cristiana Hayes II B **110 × 85 mm**, IV d. C. en MARQ p. 262; v1.2 la tenía «Fecha pendiente».
- **MARQ-011**, herma báquica de terracota **90 × 40 mm**, UE2107 literal, p. 263; contexto romano.
- **MARQ-016**, cuenco sudgálico marmorata Dragendorff 35, **diámetro 95 / altura 35 mm**, I d. C., MARQ p. 265; v1.2 «Fecha pendiente».
- **MARQ-020**, cuenco hispánico Dragendorff 37a **diámetro 190 / altura 85 mm**, p. 267.
- **MARQ-026**, cuenco marmorata Dragendorff 37 **diámetro 220 / altura 110 mm**, UE2053, p. 271.
- **MARQ-027**, cuenco «lucente» Lamboglia 45 **140 × 100 mm**, p. 271. Debe verificarse terminología: el rótulo lo presenta como «terra sigillata africana Clara Lucente» pero el cuerpo textual lo atribuye a **Galia Narbonense**.
- **PIC-EX-001**, moneda griega de Melos: publicación numismática digital *La moneda griega a Ibèria* p. 154 señala **bronce, c. 400–350 a. C.**; mantiene «sin número individual confirmado» y residencia secundaria en contexto romano publicada por Álvarez Tortosa et al. (2022).

**Fuentes verificadas:** https://marqalicante.com/contenido/publicaciones/pub2_87.pdf ; https://web.iberiagraeca.net/descargas/La_moneda_grega_a_Iberia.pdf ; https://museodelmarsantapola.com/wp-content/uploads/2023/02/Arti%CC%81culo-LA-RELLA.pdf .

## 3. Conflictos primarios: dos números repetidos en MARQ
**Caso D1.** `PI/82-271` aparece con el **OLPE** de tradición ibérica (p. 261; 250 × 170 mm) y con el **CUENCO** de sigillata hispánica Drag.37a (p. 267; 190 × 85 mm). Se publican como objetos distintos, pero **comparten identificador**. Estado `HOLD_ID`; no fusionar ni crear ID corregido sin parte museístico original.

**Caso D2.** `Pol. Urb. Salinas/2001-5292` se publica para **plato africana D Hayes 50B** (p. 261; 360 × 60 mm) y para **cuenco lucente Lamboglia 45 con cabeza de león** (p. 271; 140 × 100 mm). Equivalencia de la cadena normalizada 2001-5292; tipología y medidas diferentes. Estado `HOLD_ID`, doble incidencia por clasificación discutible de MARQ-027. Sin supuesto de error editorial concreto hasta cotejo archivístico.

**Ambos conflictos están en las propias fichas publicadas**, no los ha originado necesariamente la digitalización de IberOS. La cadena de inventario, como string, **no sirve por sí sola como clave primaria universal**.

## 4. Contextos romanos y materiales ibéricos residuales
- *Carta Arqueológica Subacuática de Alicante II* (2022), pp. 96–107, figura 4: aporta un **plano de ambientes numerados**; texto atribuye cimentación romana de **ambientes 7 y 8** a presencia agregada de cerámicas ibéricas, fragmentos áticos, fragmentos escultóricos de caliza y moneda de Melos. La fuente **no identifica UE concreta de cada material residual**.
- El mismo texto identifica **UE 408** como estrato superficial de amortización del ambiente romano 7, con sigillata gálica y ARS A; **NO** demuestra que contenga la moneda de Melos.
- Otros contextos recuperados (aquí como registro espacial textual, no hallazgos ibéricos individualizados): **UE139** bajo mosaico de ambiente 19, sobre **UE134/121**; **UE396/397** en fosa/relleno de fase IV del ambiente 8, con **otra moneda de Constancio II (353–355 d. C.)**; **UE280** para ánfora Keay25 `PSAL-480-7203` en ambiente 36; **UE80/81**, contextos romanos tardíos; **UE488**, conjunto residual del archivo. Nunca mezclar la moneda romana de Constancio II con la griega de Melos.
- En la publicación, etiquetas de ambientes (7/8) se reutilizan entre representaciones de fases; se requiere identificador de plano, fase y fecha para cada vínculo, no basta el número de ambiente aislado.
- El BOE BIC 2022 confirma abundantes materiales de procedencia ibérica en niveles de época romana, pero sin inventarios ni posiciones individuales.
- **La única asociación activa individual objeto–UE del grupo ibérico es MARQ-002 → UE2072**, registrada literalmente como `PI.89/Urbano Salinas UE 2072 SGI 11295`. No se ha recuperado su polígono/cota/transformación.

Fuentes: https://s.ua.es/es/QD~d ; https://www.boe.es/diario_boe/txt.php?id=BOE-A-2022-4134 .

## 5. Matriz bibliográfica con grado de acceso
| Documento | Estado de acceso | Valor y limitaciones |
| --- | --- | --- |
| Catálogo MARQ *Santa Pola* 2012 | **Texto íntegro indexado, campos verificables**; captura web de PDF completo >10MB devuelve error | Confirmaciones MARQ-001..027 y dos conflictos de inventario |
| Artículo *La Rella* 35 (2022) | **Texto y página 55 examinados visualmente** | Conjunto de materiales residuales, sin UE individual |
| *Carta Arqueológica Subacuática II* (2022) | **Texto y figs. 4/13 examinados visualmente** | Ambientes y UEs romanas, sin posición original ibérica |
| Numismática *La moneda grega a Ibèria* | **Texto indexado p.154**, PDF completo >10MB no descargado en esta revisión | Metal y fecha de moneda de Melos; sin sigla de colección |
| Plan Director 2023, capítulo 12 | Referencia institucional y resumen YARQ previos, sin matriz primaria de UE2072 | Reconstrucción arquitectónica, no atribución de piezas |
| Soto Arias, memoria mecanografiada de 1989/1995 | **Solo referencia bibliográfica; no copia digital localizada** | Posible ficha original UE2072, no suponer contenido |
| Badie et al. 2000, fig. 57, 68, 72 y anexo desplegable | Publicaciones derivadas y cita editorial; **original de las láminas sin inspección suficiente** | Fichas griegas PIC-EX-003…007 sin identificador individual confirmado |

## 6. Derechos y estado histórico
- Publicación en PDFs oficiales o galerías NO autoriza reproducción de fotografías de terceros por IberOS.
- Nuevas actuaciones sobre el BIC y apertura al público anunciada para 2027 por el Ayuntamiento (2 octubre 2026), **sin nuevo inventario individual de hallazgos publicado** en las fuentes consultadas: https://santapola.es/el-museo-del-mar-de-santa-pola-ha-recibido-mas-de-133-000-visitantes-entre-enero-y-septiembre/ .
- Se revisaron la **biblioteca anterior** del proyecto, la matriz maestra de GitHub y varias familias de publicaciones externas; algunas búsquedas web con cadena exacta UE2072 y SGI11295 no devolvieron ficha original. **No cabe afirmar que no exista en archivos no indexados o en publicaciones de pago**.

## 7. Pruebas de cierre necesarias
1. Solicitar o localizar digitalmente **memoria de Soto Arias y ficha/figura de UE2072** para verificar sector, cotas, fase, relación de materiales y la signatura SGI11295.
2. Confirmar con el catálogo físico del Museo del Mar/MARQ las dos colisiones D1 y D2. Hasta entonces, **cuatro registros diferenciados, dos pares HOLD-ID**.
3. Recuperar identificadores de inventario/UE para **PIC-EX-001 Melos, PIC-EX-002 escultura**, y dibujos originales con inventarios de **PIC-EX-003..007**.
4. Recalcular homologías independientes Moret–Badie ↔ YARQ_2, con incertidumbre; **0 aprobadas REC-105**.
5. Mantener cronologías T1/T2/T3/T4/T5 separadas, y fotografías externas como enlaces hasta permiso individual.

**No modificar Core, corpus, benchmark, C594, C474, C539, C541, ni atribuir nuevos puntos a la maqueta 3D.**

## 8. Incidencia de integración CI del PR #140 (12-11-2026)
- Las ejecuciones originales `tests` (43098305574), `Web E2E` (43098305616) y `Comprobaciones web gratuitas` (43098305630) permanecieron en estado `queued` sin jobs asignados; no existían registros de fallo del código ni de las pruebas.
- GitHub Status confirma una incidencia de Actions, Pages y Webhooks el 11-11-2026, con recuperación anunciada a las 21:21 UTC. Correlación temporal, **no diagnóstico causal confirmado para este PR**.
- El PR #140 se cerró y reabrió sin modificar sus archivos, para intentar restaurar eventos. Las ejecuciones antiguas continuaron en cola tras esta operación.
- Este cambio documental sirve para provocar nuevos eventos de `push` y `pull_request`; **no altera datos arqueológicos, tests, workflows, modelo 3D ni autoridad científica**. Cualquier validación nueva deberá leerse por su commit específico, sin declarar válidas las ejecuciones antiguas.

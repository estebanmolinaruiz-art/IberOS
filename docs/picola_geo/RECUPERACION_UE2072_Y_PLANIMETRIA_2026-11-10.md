# IberOS · PICOLA–GEO — recuperación documental de UE 2072 y control de ubicación
Fecha de auditoría: 2026-11-10 · Estado: **IDENTIFICACIÓN DOCUMENTAL CONFIRMADA / GEOMETRÍA NO RECUPERADA**.

## 1. Evidencia individual: MARQ-002
**Fuente primaria para los datos de ficha:** MARQ, *Santa Pola. Arqueología y Museo* (2012), ficha «VASIJA IBÉRICA», p. impresa 258, https://marqalicante.com/contenido/publicaciones/pub2_87.pdf (texto indexado, consulta 2026-11-10).

Transcripción mínima de inventario: **`PI.89/Urbano Salinas UE 2072 SGI 11295`**.

La fuente identifica un cuenco globular de cerámica ibérica hecho a torno, engobe blanco y bandas rojo vinoso, **300 mm de anchura y 200 mm de altura**, cronología tipológica **siglo IV a. C.**, tipo Mata-Bonet 2620. Se registra como «Puerto Ibérico (Picola)»; **UE 2072** figura literalmente en la cadena de inventario, no en un plano reproducido en el catálogo.

### Desagregación de identificadores
| Elemento literal | Dato registrado | Límite |
| --- | --- | --- |
| `PI.89` | Prefijo de inventario (incluye 89) | No homologar por sí solo como campaña de 1989 sin parte de excavación |
| `Urbano Salinas` | Sector textual en la cadena de inventario | No supone coordenada métrica ni un área de planta digitalizada |
| `UE 2072` | Número de unidad estratigráfica referenciado para esta pieza | No equivale a polígono, habitación, cotas, fase de deposición ni posición puntual |
| `SGI 11295` | Identificador asociado literal | Significado institucional y concordancia pendiente |

## 2. Fuentes de planos disponibles
- El Museo del Mar publicó el **Plan Director del BIC La Picola (2023–2048)** por capítulos, con **capítulo 12 «Planimetría»**: https://museodelmarsantapola.com/plan-director-del-bic-la-picola/ .
- Acceso directo a cap.12: https://museodelmarsantapola.com/wp-content/uploads/2023/11/PDLAPICOLA-CAP12.pdf . Documento de ~46,7 MB: **la recuperación por lector web devolvió un error de exceso de tamaño** y no pudo guardarse en el contenedor por restricción de conexión de red. **No afirmar inspección completa ni ausencia de UE 2072 dentro del PDF.**
- Planos YARQ_1/2/3 ya referenciados en el control PICOLA–GEO. En los materiales de este control **no se ha comprobado una etiqueta UE 2072 asociada a geometría y escala homologable**.
- Moret y Badie (1998), *Metrología y arquitectura modular en el puerto de La Picola*, **Archivo Español de Arqueología 71, pp. 53–61**: https://doi.org/10.3989/aespa.1998.v71.274. Demuestra organización metrológica (pie ~29,7–30 cm); **no demuestra la ubicación de UE 2072 ni su concordancia métrica con YARQ_2**.
- El perímetro legal BIC (21 vértices ETRS89/UTM 30N), archivado en `site/data/picola-perimetro-bic-oficial-v1.tsv`, es **distinto de la planta de excavación y de la posición de una UE**.

## 3. Resultado de la recuperación
| Control | Resultado |
| --- | --- |
| Vínculo MARQ-002 → UE 2072 | **VERIFICADO**: cadena original del catálogo MARQ |
| Procedencia «Urbano Salinas» | **VERIFICADA COMO TEXTO** de inventario, no como geometría |
| Asignación campaña 1989 | **NO VALIDADA**; prefijo `89` no basta |
| Planta original de UE 2072 | **NO RECUPERADA** |
| Polígono/cota/sector excavado homologado | **NO RECUPERADO** |
| Transformación Moret–Badie ↔ YARQ_2 | **0 homologías métricas aprobadas** REC-105 |
| Coordenada ETRS89 de MARQ-002 | **NO DETERMINADA** |
| Marcador 3D/GIS autorizado | **NO** |

## 4. Evidencia que falta y vía de recuperación
1. **Diario/matriz estratigráfica o ficha original UE 2072**, intervención «Urbano Salinas», incluyendo sector, campaña, perfil, descripción sedimentaria, relación con otras UE y fase.
2. **Plano de excavación con etiqueta UE 2072 y escala fiable**, o coordenadas del sistema de cuadrículas del equipo original.
3. **Correspondencias independientes** hacia una base topográfica contemporánea y coordenadas de control; informar residuos y error de transformaciones.
4. **Control de derechos** para reproducir un recorte de plano y relacionarlo con un objeto.
5. La visualización futura será **sector/polígono** si solo se avala un área, no pin exacto inventado.

## 5. Acción web segura
Se permite mostrar en la ficha individual de MARQ-002 el identificador exacto `PI.89/Urbano Salinas UE 2072 SGI 11295`, la procedencia textual y un enlace al catálogo MARQ y al Plan Director. **No se dibuja un punto ni se coloca la vasija dentro de una habitación reconstruida.**

**Firma: IberOS · PICOLA–GEO.** Documento científico auxiliar; sin cambiar C594/C474/C539/C541, Core, corpus, benchmark ni el bloqueo REC-105.

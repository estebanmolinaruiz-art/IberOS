# IberOS · PICOLA–GEO — auditoría de imágenes y georreferenciación (10-11-2026)
**Estado:** actualización documental; no se alteran los registros de autoridad congelados. **Firma visible: IberOS · PICOLA–GEO.**

## Hallazgos identificados en publicaciones visuales
| ID | Objeto | Evidencia gráfica verificada en la fuente | Estado del permiso |
| --- | --- | --- | --- |
| MARQ-001 | Urna ibérica | Fotografía en catálogo MARQ (p. 257–258) y galería del Museo del Mar «Época antigua» | Sin autorización individual de republicación |
| MARQ-002 | Vasija ibérica | Fotografía en MARQ (p. 258) y galería de «Época antigua» | Sin autorización individual de republicación |
| MARQ-003 | Molino de barquilla y mano | Fotografía en MARQ (p. 258–259) y galería de «Época antigua» | Sin autorización individual de republicación |
| MARQ-004 | Kylix ático de figuras rojas | Fotografía en MARQ (p. 259), ficha museo «Época antigua»; inventario S-91-22-579-1, 45×225 mm | Sin autorización individual de republicación |
| MARQ-005 | Ánfora ibérica Ribera 13 | Fotografía en MARQ (p. 260), n.º 105 | Sin autorización individual de republicación |

**Fuentes visuales (solo enlaces):**
- Museo del Mar de Santa Pola: https://museodelmarsantapola.com/piezas/epoca-antigua/
- Catálogo MARQ de 2012: https://marqalicante.com/contenido/publicaciones/pub2_87.pdf

**Regla:** publicación institucional con imagen NO es licencia para copiar, incrustar o reusar; la web de IberOS no incluye ni hotlinkea estos archivos. Los enlaces dejan al usuario consultar la fuente en su lugar original. Las fotografías aún no se han integrado en el catálogo como assets propios.

## Corrección cronológica demostrada
- **MARQ-009**: el catálogo MARQ 2012, p. 262 identifica «Vaso de paredes finas», inv. **SP-PAL85/2561**, tipo **Mayet XXIV**, **siglo I d. C.** y procedencia **Portus Ilicitanus**. No corresponde a material ibérico de IV a. C. Queda **ARCHIVO_NO_PRIORITARIO**, no «REVISIÓN PENDIENTE».
- La **fíbula MARQ-006** permanece como única ficha en revisión: el catálogo imprimió IV d. C. con adscripción «Puerto Ibérico (Picola)»; no corregir automáticamente.
- Conservación: 14 prioritarios, 1 en revisión, 51 archivo, 66 total. El inventario v0.4 y v0.3 quedan como historia reproducible; versiones nuevas v0.5 y maestro v1.1.

## Perímetro BIC georreferenciado ≠ hallazgos georreferenciados
- La declaración oficial BIC de La Picola, **BOE-A-2022-4134**, sección 3.2, publica **21 vértices en ETRS89 / UTM huso 30**, conservados literalmente en `site/data/picola-perimetro-bic-oficial-v1.tsv` con su orden y fuente.
- Estos vértices definen **el límite legal del yacimiento protegido**, **no el fortín ibérico ni las zonas individuales excavadas**.
- No son homologías Moret–Badie ↔ YARQ_2, coordenadas de objetos ni ubicaciones de habitaciones.
- **REC-105: 0 homologías métricas independientes aceptadas**. Todos los objetos mantienen `geo_posicion_aprobada=NO`.
- Conocer el identificador de una UE (p.ej. 2072 o 488) no autoriza crear un punto espacial: faltan geometría, cota, plano escalado homologado y relación pieza-UE concreta.
- Los vestigios arquitectónicos visibles en un render 3D tampoco autorizan colocar en ellos los objetos.

### Puerta de aceptación para cada hallazgo
1. Documento primario con ID de excavación, UE, sector/ambiente, fase y procedencia inequívoca.
2. Registro gráfico propio o plano con definición métrica del contexto (no solo nombre de UE).
3. Correspondencias independientes aprobadas para llevar ese plano al marco ETRS89; informe de incertidumbre.
4. Revisión arqueológica de la relación entre el material y el estrato; residuales ibéricos en contextos romanos **no** regresan automáticamente al fortín.
5. Fuente, derechos del plano y trazabilidad temporal T1–T5.
6. Publicación de ubicación como **polígono/área** cuando la precisión solo avale un sector; pin puntual solo si consta una localización puntual validada. En ausencia de controles, **no mapa de hallazgos**.

## Verificación técnica de la publicación
- Actualizar el catálogo web para enlazar la fuente de la foto, **sin reproducirla**.
- Actualizar el inventario selectivo v0.5, el catálogo v1.1 y la noticia.
- Revisar `tests`, `Web E2E`, `Comprobaciones web gratuitas` y, separadamente, la difusión efectiva por Pages.
- Fotografías institucionales del museo: no iniciar nuevos contactos; respetar tramitaciones previas y verificaciones de autorización.

**IberOS · PICOLA–GEO — documentación científica auxiliar, Core congelado C594/C474/C539/C541.**

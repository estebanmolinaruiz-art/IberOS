# IberOS · PICOLA–GEO — concordancias controladas de figuras y objetos
Fecha: 2026-11-09 · Estado: **auditoría bibliográfica** · Sin altas de objetos físicos.

## Revisión del inventario v0.4
- `site/data/picola-inventario-iberico-v0.4.tsv`: **16 registros seleccionados** (14 prioritarios + 2 en revisión).
- `site/data/picola-cribado-iberico-v0.4.tsv`: decisiones razonadas de los **66 registros históricos**.
- `site/data/picola-inventario-v0.3.tsv`: archivo histórico completo con 66 filas; nunca borrar los contextos romanos.

## Concordancia de figuras de cerámica griega (García Martín 2004, cap. 3.4.1, pp. 82–85)
**Distinción crucial:** `figura 28a/b` es referencia a la figura **de García Martín**, mientras que `figuras 57, 65, 68` son referencias **a Badie et al. (2000)** citadas por García Martín. **No** tratarlas como parte de la misma numeración.

| Referencia | Descripción literal o parafraseada publicada | Cronología referida | Concordancia con inventario | Estado de objeto |
| --- | --- | --- | --- | --- |
| García Martín 2004, fig. 28a | Crátera de campana de figuras rojas próxima al Pintor de Cadmos | 420–400 a. C., segunda fase | Ningún `PHYS_ID` en v0.4 acreditado | **Candidato documental**, no alta |
| García Martín 2004, fig. 28b | Ánfora de cuello con asa trenzada, de figuras rojas | 430–420 a. C., segunda fase | Ningún `PHYS_ID` en v0.4 acreditado | **Candidato documental**, no alta |
| Badie et al. 2000, fig. 65.6 | Referencia editorial ligada a la secuencia de cerámica ática | Grupos de segunda mitad V–IV a. C.; no fecha propia sin original | No individualizar a partir de la mera cita | **Figura original no inspeccionada** |
| Badie et al. 2000, fig. 57.1 | Mortero corintio de pasta beige | Contexto datado en primera mitad IV a. C. | `PIC-EX-003` | **Ya registrado**; no duplicar |
| Badie et al. 2000, fig. 68.12 | Borde ánfora massaliota tipo Py 3 | Tipo de finales VI–V a. C. | `PIC-EX-004` | **Ya registrado** |
| Badie et al. 2000, fig. 68.13–14 | Dos bases en botón, ánforas de Grecia oriental, origen indeterminado | Una primera mitad IV a. C., otra segundo tercio IV a. C. | `PIC-EX-006` (conjunto) | **Ya registrado**; separar fichas solo con identificadores |
| Badie et al. 2000, fig. 68.15 | Fondo de botón completo de ánfora, **posiblemente** samia | Segundo tercio IV a. C. | `PIC-EX-007` | **Ya registrado**; origen hipotético |
| Badie et al. 2000, sin figura individual confirmada aquí | Dos fragmentos de panza de ánfora corintia A reciente | Siglos V–IV a. C. | `PIC-EX-005` | **Ya registrado**; no suponer dos vasijas |

### Regla de alta
Un fragmento, un dibujo y su ficha museística pueden representar el **mismo objeto**. Solo generar `PIC-IB-...` nuevo si consta un identificador único o concordancia independiente de `PHYS_ID` y, al menos, la figura/soporte original verificables. Si falta contexto de excavación o depósito museístico, señalarlo expresamente. Nunca asignar por la fecha de un estrato romano una fabricación tardía a un objeto ibérico.

### Observaciones nuevas sin interpretación forzada
- García Martín divide la cerámica de La Picola en **133 vasos áticos** (29 figuras rojas, 103 barniz negro, uno sobrepintado/reservado) y seis ánforas griegas más un mortero corintio, **140 materiales griegos** en total. Estos **no** son 140 fichas materiales verificadas.
- La primera fase (450–400 a. C.) suma 18 vasos; la segunda, último cuarto del V, 31; la tercera, siglo IV, 83; hay además una copa aislada C de Bloesch del primer tercio V. Los grupos son analíticos, no etiquetas automáticas de fabricación o deposición.
- **Interés prioritario:** recuperar en alta resolución las figuras originales 28a/28b de García Martín y las láminas 57, 65, 68 de Badie, además de la tabla de excavación. Una figura no aporta por sí misma UE, dimensiones, autoría exacta ni ubicación actual.

## Fuentes
1. Josep Miquel García Martín, 2004, *El comercio de cerámicas griegas en el sur del País Valenciano (siglos VIII al IV a. C.)*, cap. 3.4.1, pp.82–85, Universidad Autónoma de Madrid: https://repositorio.uam.es/bitstream/10486/12542/1/60734_garcia_martin_josep_miquel.pdf
2. Badie et al. 2000, *Le site antique de La Picola à Santa Pola (Alicante, Espagne)*, Casa de Velázquez (referencias de figuras citadas **indirectamente** hasta verificación del original): https://www.casadevelazquez.org/publications/librairie-en-ligne/publication/le-site-antique-de-la-picola-a-santa-pola-alicante-espagne
3. Inventario IberOS, selección ibérica v0.4, registro y matriz conservadora.

**Estado de acceso:** se ha consultado el texto digital extraído de la tesis; el servicio de captura de páginas del PDF devolvió 403, por lo que **la imagen de la figura 28 no ha sido inspeccionada visualmente aquí**. La monografía Badie 2000 tampoco se ha inspeccionado íntegramente. Sin fotografía original autorizada ni verificación de depósito físico.

**Firma: IberOS · PICOLA–GEO**. Documento auxiliar independiente; sin modificar C594/C474/C539/C541, Core, benchmark, corpus ni arqueometría de REC-105.

# IberOS — corrección del contraste kitar/etar y reutilización de cuño

**Fecha:** 2026-10-18. **Estado:** CORRECCIÓN METODOLÓGICA / NO PROMOTION. Autoridad C594/C474/C539/C541 y métricas intactas.

## Corrección obligatoria del informe anterior

El documento `docs/KITAR_ETAR_CROSS_DENOMINATION_TEST_2026-10-18.md` afirmó que la aparición de `arseetarkiterder` en varios nominales contradice una correspondencia biunívoca entre leyenda y denominación. **Esta inferencia es demasiado fuerte y debe considerarse RETRACTADA**: el artículo primario describe la reutilización de **un mismo cuño** originalmente diseñado para la hemidracma, después aplicado a óbolos y hemióbolos. La marca puede ser una marca de valor original aun cuando aparezca en piezas de otros nominales por reutilización técnica.

**Fuente primaria:** Ferrer i Jané y Giral Royo (2007), *A propósito de un semis de ildiŕda con leyenda erder. Marcas de valor léxicas sobre monedas ibéricas*, Palaeohispanica 7, 83–99: https://ifc.dpz.es/recursos/publicaciones/27/28/5.ferrer-giral.pdf ; ficha DOI https://doi.org/10.36707/palaeohispanica.v0i7.277 .

## Evidencia positiva y límites

- Semis de ildiŕda con `erder`, masa 8,2 g y creciente iconográfico que identifica el nominal: evidencia contextual favorable a `erder` como fracción 1/2, no traducción inequívoca independiente.
- `arseetarkiterder` documentado en hemidracma, óbolo y hemióbolo; **un único cuño** implica dependencia de las ocurrencias y permite explicación técnica de reutilización.
- Ferrer (2010) discute masas orientativas de hemidracma ~1,6 g, óbolo ~0,4 g y hemióbolo ~0,2 g: https://www.researchgate.net/publication/245585234_Analisis_interno_de_textos_ibericos_Tras_las_huellas_de_los_numerales .
- Vidal (2017) describe didracmas de śaitabi con `kitar` ~6,8 g y dracmas con `etar` ~3,4 g; su comparación sugiere relación 2:1 en **esas emisiones**, sin demostrar universalidad: https://www.researchgate.net/publication/329012821_La_palabra_iberica_abar_%27diez_decena%27_y_el_sistema_decimal_a_-_o_-_ki .

## Experimento controlado pendiente

Crear matriz por moneda con `specimen_id`, `die_id`, `mint`, `issue`, `date`, `nominal`, `metal`, `mass_g`, `legend_exact`, `legend_segmented`, `source`, `image`, `conservation`, `dependence_family`. La unidad de análisis para independencia no es cada moneda con leyenda repetida sino emisión/familia de cuño. Comparar marcas `erder`, `etar`, `kitar` y controles contemporáneos sin ellas; estratificar por metal, ceca, emisión y nominal. Congelar predicciones antes de incorporar un HOLD externo no usado en la literatura de desarrollo.

**Veredicto:** `erder ≈ mitad` recibe apoyo contextual; `kitar = masa fija` no queda validado; la inferencia previa de refutación por varios nominales queda corregida. C474 INDETERMINATE; no actualizar significados seguros ni tesis congelada.

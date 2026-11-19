# SCI-TOP-01 · Primer contraste de una predicción numismática

**Fecha de ejecución:** 2026-11-12. **Predicción fijada antes de buscar en un nuevo catálogo**, commit GitHub `90ee86a98268f882f302b18a05b4f26106731872`, archivo `research/protocols/SCI_TOP_01_COIN_PREDICTION_LOCK_20261112.json`.

**Regla bloqueada:** primera moneda física nueva de Arse-Saguntum en otro inventario museístico, 130–72 a. C., bronce de unidad y media/as, cabeza femenina galeada, reverso con proa + Victoria + caduceo. Predice **latín SAGVNT en anverso e ibérico ARSE en reverso**.

## Secuencia de búsqueda (se conserva primer candidato, no se escoge un acierto)

1. Tras guardar el compromiso, búsquedas abiertas localizaron un catálogo de la **Fundación Banco Santander (2026)** con as de la misma iconografía, nº 182–187. Presenta diferencias de denominación («as» frente a «unidad y media/as») y piezas de la misma categoría; estas fichas no se usan para inflar n.
2. A continuación, el catálogo científico institucional gratuito del **Museu de Prehistòria de València** describe explícitamente el tipo «Unidad y media/As. Ca. 130–72 a. C.», anverso cabeza femenina galeada a derecha, reverso proa a derecha, Victoria, caduceo y leyenda arse. Su **primer ejemplar de este tipo fuera de la muestra MARQ** es **catálogo nº 321, inventario 31.362**, AE 28,16 g, eje 12 h.
3. **Leyenda del anverso descrita para nº 321:** `ikoŕbeleś` (fuente usa tipografía romanizada con grafemas especiales) y `balkakaltuŕ`, ambas en **ibérico**. Reverso **`arse` en ibérico**.
4. Por tanto, **H1 falla**: su requisito de leyenda **latina SAGVNT en anverso** no se cumple. La subpredicción `arse` en reverso sí coincide. La alternativa H3 («solo ibérico ARSE, sin latin SAGVNT») es compatible con la descripción editorial del objeto.
5. **No saltar** al nº 324, inventario 31.927, donde sí aparece el rótulo latino SAGVNTINV con ARSE ibérico: es una **emisión distinta de la misma familia iconográfica**, permite entender por qué falla la regla general, pero no debe sustituir al primer ejemplar fallido en la evaluación.
6. Catálogo de la Fundación Banco Santander 2026 números 182/183 (ibérico en ambas caras), 184–187 (latín e ibérico) ofrece una segunda comparación retrospectiva; no es HOLD nuevo ni una validación estadística independiente.

## Fuentes físicas

- [Museu de Prehistòria de València (2013), *L’oppidum de la Carència de Torís i el seu territori*, Serie Trabajos Varios 116, inventarios nº 321 y 324 en catálogo numismático, pág. impresa 181](https://mupreva.org/dedalo/media/pdf/publicaciones/standar/mupreva194_mupreva153_147.pdf).
- [Fundación Banco Santander, colección numismática, listado 2026, inventarios 182–191](https://www.fundacionbancosantander.com/content/dam/fundacion-banco-santander/es/documentos-/cultura/arte/investiga_cbs/2026/Listado%20numismatica%20CBS.pdf).
- Caso de entrenamiento MARQ [NIM 727](https://www.marqalicante.com/es/producto/unidad-y-media-as-anos-130-72-a-c-2/).
- Estado original de hipótesis registrado en GitHub: [commit del protocolo](https://github.com/estebanmolinaruiz-art/IberOS/commit/90ee86a98268f882f302b18a05b4f26106731872).

## Resultado y validez

| Campo | Resultado |
| --- | --- |
| Hipótesis H1 (SAGVNT latino + ARSE ibérico) | **FAIL**, catalogación textual del primer objeto |
| Subpredicción ARSE reverso | **MATCH**, catalogación textual |
| Resultado completo | **0/1**, fallo de predicción conjunta |
| Contradicción encontrada | anverso `ikoŕbeleś` / `balkakaltuŕ` ibérico, no `SAGVNT` latino |
| Cotejo D2/D3 directo de la imagen por dos lectores | **NO** |
| Nuevos roles semánticos externamente comprobados | **0** |
| Traducciones nuevas confirmadas | **0** |
| Evaluación lingüística prospectiva genuinamente ciega | **NO**: fuentes de catalogación históricas y públicas |
| Reglas originales cambiadas tras resultado | **NO**, preservar original bloqueado |

**Conclusión útil:** una misma iconografía y período incluye emisiones exclusivamente ibéricas y emisiones bilingües, por lo que la regla que generaliza MARQ NIM 727 a toda unidad y media con proa es excesiva. Antes de probar una nueva hipótesis, habrá que fijar una **regla nueva** que incorpore una característica legible *sin revelar el propio contenido de la leyenda* o trabajar con una hipótesis sobre variación/serie catalográfica y comprobarla fuera de muestra. No entrenar y volver a examinar nº 321 como si fuera HOLD nuevo.

**Limitación de acceso visual:** se intentó renderizar la captura del PDF mediante visor web pero devolvió error de caché; los resultados se basan en la tabla textual del catálogo institucional, no en examen visual certificado. No reutilizar el acierto parcial como signo cotejado directamente.

**Estado del proyecto:** la falsación técnica/retrospectiva se incorpora a resultados negativos; SCI-PRED-02 sobre productor/comitente permanece intacto. Ninguna métrica oficial, FULL3406 ni web ha cambiado. Coste monetario 0 €.

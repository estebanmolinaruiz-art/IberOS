# IberOS — matriz de cotejo de Casinos, seis líneas (18-10-2026)

**Objeto** `IBR-PLM-0007` · **Fuente primaria:** Ferrer i Jané, J. y Escrivà Torres, V. (2014), *Palaeohispanica* 14, 205–227, DOI https://doi.org/10.36707/palaeohispanica.v0i14.54. PDF aportado para análisis. **Imágenes visibles:** figura 1, p. 207 (PDF p. 3), fotografías A/B; figura 2, p. 208 (PDF p. 4), dibujos A/B. **Aparato editorial:** pp. 211–212.

Esta matriz compara **lecturas editoriales** con elementos descritos por el estudio y con las reproducciones, pero **no certifica signo por signo** la totalidad del texto por autopsia o revisión externa. Los puntos de separación aquí normalizados se distinguen de los trazos físicos.

| Cara / línea | Lectura editorial dual (p. 212) | Alternativa no dual (p. 212) | Control paleográfico y grado |
|---|---|---|---|
| A1 | `aitusinka. a IIIIIII. (])` | Igual | 4º signo de `aitusinka` poco claro (posible `s`); `ka` desgastado, variante compleja con dudas; agrupaciones de barras y separador a cotejar. **Editorial con dudas; no verificada independientemente** |
| A2 | `abaŕgeŕes. eŕeil (])` | `abaŕkeŕes. eŕeil (])` | Signo de `r` y zona de `e` afectados por concreciones y erosión. Dualidad ge/ke depende del sistema asumido. **Alternativas editoriales** |
| A3 | `śeiar. bi` | Igual | Primer signo dañado: `s` probable según editores, con alternativas `i` o `n`; `bi` aislado por separador. **Lectura inicial dudosa** |
| B1 | `ideŕ. dagan. (])` | `iteŕ. takan. (])` | Inicio `i` afectado; posibilidad de signo precedente oculto; separación de tres y cuatro puntos según descripción. **Alternativas d/t, g/k; inicio dudoso** |
| B2 | `sisbibeiabin` | Igual | Posible signo previo bajo concreciones, con trazos compatibles con `s`; otras roturas superficiales. **Posible inicio incompleto** |
| B3 | `a I. o I. gi I /` | `a I. o I. ki I /` | Segmentos con abreviaturas metrológicas y barras, dos puntos como separadores según edición. **gi/ki alternativo** |

### Discrepancias contra la normalización previa

El archivo `data/review/editorial_readings_pending_v1.jsonl` conserva cadenas **normalizadas** (interpunctores como `·`, y el rótulo `[lacuna uncertain]`). Ahora también incorpora por separado la **lectura impresa** de p. 212; la notación `(])` es de la edición y no debe confundirse con un signo ibérico efectivamente visto. El marcador `/` después de B3 figura en la presentación impresa. **No rectificar silenciosamente** ambos tipos de datos.

### Advertencias de método

1. **No reconocer automáticamente las perforaciones como signos o interpunciones:** pp. 206–207 explican que podrían ser marcas mecánicas.
2. **No asumir unidad original de las dos caras:** los editores condicionan a ello la inferencia de dualidad gráfica (p. 212).
3. **No tratar `sisbibeiabin = 2/7` como traducción:** es una de varias hipótesis (pp. 219–222); el artículo no confirma valores numéricos.
4. **No dar permisos de reproducción por supuestos:** se usaron imágenes del PDF suministrado para examen; su publicación en IberOS requiere revisar derechos.
5. **Estado del Core:** `PENDING_GRAPHIC_REVIEW`, `reading_reviewed=false`, `translation_validated=false`; una matriz editorial no constituye certificación paleográfica.

### Próxima decisión por signo

Registrar de forma individual los signos más inseguros de **A1 (s/variante ka)**, **A3 (s/i/n)**, **B1 (inicio y dualidad dental/velar)** y **B2 (signo inicial bajo concreciones)** con recorte gráfico, posición y resolución, y someterlos a revisión independiente antes de aprobar una lectura para experimentos del Core.

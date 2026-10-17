# IberOS — auditoría inicial de calidad de las citas: Sagunto y Caminreal (17-10-2026)

**Alcance:** verificación de metadatos editoriales, identificación de fuente y coherencia entre cita e hipótesis; **no** autopsia de soporte ni cotejo visual de los signos.

## Sagunto — IBR-LAP-0005

- Registro actual: Orduña Aznar, Eduardo (2008), «Ergatividad en ibérico», *Emerita* 76(2), 275–302, sección «El arquitrabe bilingüe de Sagunto (F.11.8)», pp. 281–283. DOI: https://doi.org/10.3989/emerita.2008.v76.i2.299.
- Fuente primaria epigráfica a cotejar: Untermann, *MLH III*, **F.11.8**. El artículo de Orduña constituye discusión secundaria de las lecturas, **no** sustituye a la edición paleográfica original.
- Control de interpretación: la aproximación de `tebanen` a `coeravit/coerauit` se cita como **hipótesis académica**, no como equivalencia léxica demostrada. La inscripción es parcialmente fragmentaria y las líneas latina e ibérica no garantizan identidad literal.
- **Estado:** cita explícita ya registrada; comprobación independiente de fotografía, signos, daño y página de *MLH* pendiente. La verificación web del DOI de *Emerita* no ha producido nueva inspección del texto completo en esta auditoría; conservar cautela.

## Caminreal — IBR-MUS-0001

- Comprobación cruzada con el sumario de la editorial *Palaeohispanica* (volumen 15, **2015**), artículo de Ignacio Simón Cornago, pp. **87–127**. DOI: https://doi.org/10.36707/palaeohispanica.v0i15.39. Fuente: https://www.ifc-ojs.es/index.php/palaeohispanica/es/issue/view/15 .
- El resumen editorial en https://ifc-ojs.es/index.php/palaeohispanica/pt/article/view/39 explicita cuatro líneas de discusión: antropónimo **`likine`**, término **`ekiar`**, topónimo y posición/identidad de `likine`. Por tanto la cita **sustenta la existencia de debate**, no una lectura semántica final.
- La edición PDF primaria para una fase posterior se encuentra en https://ifc.dpz.es/recursos/publicaciones/35/02/03simon.pdf. **No se ha efectuado cotejo visual** de sus figuras ni facsímiles en esta auditoría.
- **Control de edición:** 2015 es el año del volumen; la plataforma online puede indicar una fecha posterior de digitalización/publicación.
- **Estado:** autor, título, revista, volumen, páginas y DOI corroborados con sumario/referencia editorial. Lectura `ekiar` = «hizo» y función social del personaje quedan como propuestas, no validaciones.

## Conclusión y pendientes

La última captura de las fichas `site/data/ficha-enrichment-2.json` y `-3.json` contiene las dos referencias completas. Cumplimentar el campo `citation` es un **control de completitud**, distinto de cotejo real de fuentes y de validación de interpretaciones. El inventario de 38/38 citas se mantiene como métrica de presencia del campo, **no de calidad revisada del corpus completo**.

Pendiente: (1) acceso a facsímiles con atribución y licencias; (2) cotejo independiente de signos y lagunas; (3) control cruzado con *MLH* para las dos piezas; (4) auditoría individual de las restantes 36 citas; (5) mantener `translation_validated=false`.

**CI de la versión anterior:** `bf28c9f726b7c4d61f52690d1bb1ece02fc38f49`: `tests`, `pages` y `Comprobaciones web gratuitas` = **success**, confirmado por GitHub Actions.

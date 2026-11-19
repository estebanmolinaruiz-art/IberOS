# SCI-MET-02 · Ejecución del compromiso cuantitativo y búsqueda de corroboración independiente

**Fecha:** 2026-11-14. **Gasto:** 0 €. **Protocolo anterior a la búsqueda:** commit [fb22d71](https://github.com/estebanmolinaruiz-art/IberOS/commit/fb22d71fae80d6780f8c290a418977685346c881), `research/protocols/SCI_MET_02_ONE_O_OUT_OF_SAMPLE_LOCK_20261114.json`.

## Regla intocable

Para el **primer ponderal físico ibérico distinto de las cuatro piezas de calibración**, con **un solo signo o adjudicado** y **masa medida**, se fijó predicción **41,29 g ±10 %**, intervalo cerrado **[37,161;45,419] g**. Se conservarían también objetos con imagen/signos ilegibles y sin medición como **ABSTAIN/INCOMPLETE**. No se permite seleccionar resultados positivos a posteriori.

## Búsqueda efectuada DESPUÉS del commit

Consultas: `ponderal ibérico signo o peso gramo marcado o`; `ponderales ibéricos signo o peso 2024 2025 marcas`; `Iberian inscribed weights sign o grams other than Puig Misericordia`; `ponderal ibérico signos inscritos 2025 2026 Aras de los Olmos peso`. Acceso libre desde navegador. Se examinaron el trabajo paleográfico de Ferrer i Jané 2013, el artículo de 2026 sobre Bastida y la nueva revisión de Montes Novella 2026, junto con síntesis de Poigt.

**Hallazgo decisivo para el diseño:** los repertorios antiguos presentan el ponderal **Puig de la Misericòrdia** de 41,29 g con signo `o` y **Puig Castellar** de 423,78 g con inscripción lexical `ustainabaŕ...` como los enlaces directos clásicos entre grafías y balanzas. **No se localizó un SEGUNDO ponderal distinto con signo `o` único y masa físicamente medida** para esta predicción. No marcar una pieza no observada como éxito.

**Resultado real del intento:** `NO_ELIGIBLE_NEW_OBJECT`; **0 intentos puntuables, 0 aciertos, 0 errores**. La búsqueda puede continuarse, pero sin evidencia nueva no puede cerrarse con evaluación positiva.

## Hallazgo externo nuevo: 2026 y alternativas al modelo simplista

**José Vicente Montes Novella (2026), «El sistema ponderal ibérico: arqueología frente a epigrafía», *ELEA* 23, pp. 149–229**, abierto como página textual https://www.academia.edu/172876427/EL_SISTEMA_PONDERAL_IB%C3%89RICO_ARQUEOLOG%C3%8DA_FRENTE_A_EPIGRAF%C3%8DA . La publicación refiere un **ponderal de Aras de los Olmos de 41,05 g con DOS marcas incisas**: 
- Dos marcas físicas no prueban dos signos `o` ni dos unidades de 42 g. La pieza es **INELIGIBLE** para SCI-MET-02 hasta cotejo de su figura e identidad gráfica.
- Si ambas marcas denotan unidades iguales, el cociente **41,05 / 2 = 20,525 g** sugiere una posible unidad material de **~20,5 g**, alternativa a una o de ~41–42 g. **Inferencia condicional**, no conclusión establecida.
- La masa 41,05 g dista 0,24 g (0,58%) de la masa conocida 41,29 g, pero la coincidencia **no demuestra que ambos signos tengan el mismo valor**.
- El autor señala también ponderal de Utiel con dos marcas que **podría** indicar media unidad: marca/valor **no equivalen universalmente**.
- Fuente adicional de debate arqueológico: https://una-editions.fr/la-peninsule-iberique-creuset-dune-pratique-ponderale/ discute cronología, diversidad de ponderales y unidad de ~42 g.
- **Nota de materialidad**: la publicación de Montes reproduce una revisión histórica del peso del cuenco de plata de La Granjuela: antiguamente 568,2 g y pesada posterior atribuida a Alicia Torrija/Torija en 2003 de **606,01 g** (cifra de las publicaciones científicas de 2011 y 2014; no 606,1 g, un redondeo o errata). El cambio es **37,81 g / 568,2 g = 6,65 %**: cualquier sistema algebraico que ajuste ese cuenco a un único peso fijo sin controlar procedencia de la medición puede inducir a error. **Pendiente cotejar ficha de museo original y circunstancias de la pesada**. NO tratar la cifra nueva como oro científico autocertificado por un sitio de alojamiento.
- Referencias antiguas: Ferrer i Jané, 2013, https://dialnet.unirioja.es/descarga/articulo/4561912.pdf, figura 1 para lectura física de `o`; Ferrer i Jané, 2026, https://mupreva.org/web_mupreva_dedalo/publicaciones/1642/va, para la propuesta híbrida 10a/12o.

## Lógica científica que extraemos de este intento

El resultado no apoya el cálculo directo de una unidad por contar incisiones **sin clasificarlas**: puntitos de valor, grafemas `o`, pares de marcas y numerales léxicos son sistemas semiológicos diferentes hasta prueba documental. La alternativa `2 × 20,5 g` y la alternativa `1 × 41 g` pueden explicar objetos de 41 g; para distinguirlas se requiere forma de marca, grupos ponderales de misma serie y un segundo objeto con relación física documentada.

## Regla siguiente, sin abrir otro test oportunista

Conservar precompromiso original abierto pero **sin casos válidos**. Siguiente búsqueda concreta: obtener la **figura original del ponderal Aras de los Olmos (41,05 g, 2 marcas)** y cualquier dato metrológico de su grupo; determinar si las marcas son incisiones equivalentes, marcas de capacidad, de taller o alfabetiformes. Comparar con la serie de 20–21 g de conjuntos de pesas. Se requiere prueba por **serie arqueológica**, no un hallazgo aislado favorable. Validar discrepancia Granjuela 568,2/606,1 desde inventario y pesada primaria. 

## Control de honestidad

Sin dos grupos de lecturas directas o una pieza nueva con mass withheld, esto **no es blind test**. No se han modificado FULL3406, TRAIN/VAL/HOLD, Core oficial, métricas o protocolos anteriores. **Cero traducciones nuevas confirmadas**.

## Verificación bibliográfica independiente de la masa del cuenco

La discrepancia de La Granjuela NO fue descubierta por IberOS en 2026. El artículo de Ferrer i Jané (2011), https://www.academia.edu/425643/Sistemas_metrol%C3%B3gicos_en_textos_ib%C3%A9ricos_1_del_cuenco_de_La_Granjuela_al_plomo_de_La_Bastida , ya señala **606,01 g**, citando la pesada de Torija (2003), y contrasta la ficha antigua de **568,2 g**. Ferrer i Jané y Escrivà (2014), *Palaeohispanica* 14, https://ifc-ojs.es/index.php/palaeohispanica/es/article/download/54/57/294 , vuelve a indicar **606,01 g**. La ficha histórica de 1954 del Museo Arqueológico Nacional, https://www.man.es/dam/jcr:ebe1ba8e-593b-4a1e-b3f9-49d0f7309745/1954-brah.pdf , identifica inventario **32708** y masa **568,2 g**. Ambas masas proceden de fuentes publicadas; **no se ha podido auditar la báscula ni la pieza original en IberOS**.

Para futuros cálculos, registrar ambas masas como **mediciones bibliográficas históricas discrepantes**, preferir 606,01 g en reconstrucciones que utilicen la bibliografía más reciente y realizar análisis de sensibilidad contra 568,2 g. Nunca presentar las dos pesadas como dos objetos arqueológicos.

## Objeto nuevo de Aras de los Olmos: expediente con precisión documental

Montes Novella (2026), https://www.academia.edu/172876427/EL_SISTEMA_PONDERAL_IB%C3%89RICO_ARQUEOLOG%C3%8DA_FRENTE_A_EPIGRAF%C3%8DA, pp. ~198–199, registra un conjunto donado al **Ecomuseo de Aras de los Olmos**, sin contexto arqueológico exacto; el peso de **41,05 g** tiene **dos marcas triangulares**. El autor estudia otras dos piezas del mismo conjunto, **42,52 g** (plomo deformado y perforado) y **6,68 g** (bronce), pero **no señala que estas tengan el signo ibérico único o**. La procedencia e identidad cultural/cronológica requieren cautela. Dos triángulos **no se pueden codificar como dos signos `o` ni como dos puntos convencionales sin autopsia**. La ratio 41,05/2 = **20,525 g** es una interpretación condicional de un posible valor doble, propuesta también por el autor; no refuta la coexistencia de patrones próximos a 42 g.

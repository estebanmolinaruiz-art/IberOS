# SCI-PRED-02 — Iteración documentada 2026-11-12

**Programa:** Dama de IberOS / predicción y posible traducción. **Resultado científico actual:** NO_PASS; 0 casos prospectivos contrastados y 0 traducciones validadas. **Coste 0 €**.

## Hallazgo metodológico

La revisión de bibliografía sobre bilingüismo ibérico confirma que reunir **dos antropónimos** o incluso una **inscripción bilingüe** no basta para asignar dos roles ibéricos distintos. Una transcripción posterior que ya publica los roles no puede presentarse como gold secreto ni como un hallazgo futuro. El test prospectivo necesita un protocolo firmado **antes de revelar gold externo** y exclusiones de toda evidencia conocida.

## Rastreo y descartes (sin reciclarlos como nuevos HOLD)

| ID | Fuente académica | Observación | Veredicto | Por qué |
| --- | --- | --- | --- | --- |
| REF-K54 | Estarán Tolosa 2012, DOI 10.36707/palaeohispanica.v0i12.66, pp. 78–80; Silgo 2008, DOI 10.36707/palaeohispanica.v0i8.259 | Dos morteros de Caminreal y Fuentes de Ebro exhiben sellos con Fl · Atili / L · s. y bilakeaiunatin / en · abiner. Texto latino diferencia persona esclavizada y dueño; en la lectura de Estarán el texto ibérico puede reiterar solo el nombre de Flaccus (p. 80). | TRAIN / RETROSPECTIVE ONLY | La correspondencia término a término no está demostrada; dos objetos con fórmula estampillada parecida no aportan dos validaciones independientes. No confundir propiedad/esclavitud con autor/encargo. |
| REF-SAG-F11.8 | Orduña 2008 y bibliografía de Sagunto; Estarán Tolosa 2023 en https://una-editions.fr/los-pueblos-paleohispanicos-ante-roma/ | Bilingüe edilicio latino-ibérico con tebanen y coeravit discutidos. | TRAIN / NO ROLE GOLD | Roles personales y valores exactos del verbo ibérico no cerrados; ya conocido por los experimentos de IberOS. |
| REF-CAM-E7.1 | Simón Cornago 2015, DOI 10.36707/palaeohispanica.v0i15.39 | likinete ekiar usekeŕteku; autor o comitente discutido. | TRAIN / PILOTO RIVAL | Los papeles maker/commissioner no se acreditan externamente en la misma pieza. |
| REF-AND-K28.1 | Orduña Aznar 2023, DOI 10.36707/palaeohispanica.v23i0.520 | Mosaico de Andelo, fórmula comparada con Caminreal y con pavimento latino de La Cabañeta. | TRAIN / SIN GOLD EXTERNO | Las comparaciones estructurales no fijan un rol individual. Adscripción lingüística debatida. |
| REF-CAB-2003 | Ferreruela et al. 2003, DOI 10.3989/aespa.2003.v76.115 | Pavimento latino con **dos magistri** vinculados a obra y edificio mercantil. | CONTROL CONTEXTUAL, EXCLUDED AS IBERIAN HOLD | La inscripción estudiada no está redactada en ibérico; ambos son magistri, no actor vs receptor demostrado. |
| REF-TAR-BILING | Estarán Tolosa, https://una-editions.fr/los-pueblos-paleohispanicos-ante-roma/ | Bilingües no monetales de Tarraco: dos funerarias perdidas y una monumental muy fragmentaria. | BLOCKED | Carecen de un conjunto íntegro verificable con dos roles distintos acreditados de manera externa. |
| REF-AZAILA | Estarán Tolosa 2012 pp. 78–79 y Silgo 2008 | Protemus fecit y baborotenbotenin comparados en morteros del área de Azaila. | NEGATIVE/CONTEXT CONTROL | Comparación discutida y no constituye un testimonio bilingüe con dos actores y roles verificados. |
| REF-LATIN-IBERIAN-NAMES | Moncunill et al. investigación reciente: https://diposit.ub.edu/server/api/core/bitstreams/7724cbfc-e73f-420e-b7b0-2fdeace6369b/content | Relaciones familiares en epigrafía latina con nombres ibéricos ayudan a detectar nombres, pero no demuestran equivalencia de funciones en textos ibéricos. | BACKGROUND TRAIN | Los roles en latín no se transfieren automáticamente a otro soporte o nombre semejante. |

## Predicción formulada antes de revelar un nuevo test

Archivo canónico: `research/protocols/SCI_PRED_02_FUTURE_ROLE_RULE_20261112.json`. Los commits posteriores deben **registrarse como nueva versión**, no sobrescribir reglas después de ver resultados.

- **H-MAKER**: en una nueva fórmula ibérica de construcción con dos personas identificadas independientemente y un solo antropónimo segmentado en `-te`, esa persona es **productor**.
- **H-COMMISSIONER**: misma condición, esa persona es **comitente**.
- **H-NULL**: no se asigna papel sin evidencia.
- **Bloqueo:** esta regla procede de material ya conocido y *no es una predicción de un caso nuevo*. Será contrastable solo en casos **nuevos** con etiquetas externas ocultas, alta D2/D3, identidad física comprobada, y sin reaprovechar familias de punzón ni ediciones.
- **Protocolo de éxito predeclarado:** 20 objetos independientes con roles externos revelados tras fijar cada predicción; ≥16 aciertos H-MAKER y ventaja ≥0,15 sobre baseline mayoritario calculado solo desde TRAIN; registrar incertidumbre, cobertura, fallos y abstenciones. Si no se reúnen 20 objetos, INSUFFICIENT_N y ningún «éxito».
- El test del código en `src/iberos/prospective_role_lock.py` sólo genera predicción y hash, **jamás ingiere gold**. Comprobar SHA del archivo y del commit externo antes del unblinding para acreditar anterioridad.

## Ruta de búsqueda repetible

1. Consultar nuevas ediciones en *Palaeohispanica*, Hesperia y repositorios abiertos; buscar **objetos nuevos** con dos antropónimos y contexto edificatorio o administrativo con roles probados fuera del texto.
2. Comparar antes de añadir con `#149`, `#150`, `#151`, `#155`, Drive SYNC-01 y catálogo de 38 objetos. Conservar descarte, fecha, motivo, URL/DOI, PHYS_ID si existe y posible familia de ejemplares.
3. Permitir selección del candidato sin revelar al Core el papel de cada persona; si no hay dos lectores ciegos independientes, registrar BLOCKED_D3.
4. Ejecutar `role_prediction_seal.seal` en un caso cuya ficha omita gold; publicar hash, commit y registro temporal **antes** de recibir etiquetas de un adjudicador externo.
5. Revelar gold solo si procede de fuentes independientemente verificadas; computar matriz de aciertos y errores, **incluyendo nulos y abstenciones**.
6. Si no pasa, registrar el fallo; no ajustar regla sobre el mismo HOLD. Versión nueva solo contra un **HOLD posterior independiente**. Continuar hasta evidencia suficiente o documentar límite insuperable sin crear resultados ficticios.

## Nuevos hechos científicos confirmados

**Ninguna traducción**. Lo confirmado por fuentes consultadas es **la escasez y disputa de paralelos**, y por el test software **la posibilidad de registrar una predicción sin consumir gold**. Están pendientes la ejecución de un caso real sobre soporte físico nuevo, la adjudicación externa y su comparación posterior.

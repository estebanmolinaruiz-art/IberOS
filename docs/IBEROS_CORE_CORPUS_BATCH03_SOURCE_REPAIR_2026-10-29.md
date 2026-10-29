# IberOS CORE — Tanda 03, reparación bibliográfica (29 octubre 2026)

## Cambios confirmados al registro maestro

- `IBR-PLM-0002` **Plomo de Tivissa**: la URL antes vacía se sustituye por DOI `https://doi.org/10.36707/palaeohispanica.v0i3.339`, artículo **«Inscripción ibérica sobre plomo procedente de Castellet de Banyoles (Tivissa)»**, Asensio, Miró, Sanmartí y Velaza, *Palaeohispanica* 3 (2003), 195–204. El artículo es pertinente al objeto descrito; **todavía no certifica inventario, identidad física individual ni lectura completa**.
- `IBR-PLM-0005` **Villares V**: se sustituye URL ResearchGate truncada por la URL completa de **«Una nova mirada al plom ibèric Villares V (Kelin, Caudete de las Fuentes). Un text comptable amb deu transaccions»**, Joan Ferrer i Jané, *Elea* 21 (2024), 309–360. El artículo identifica el objeto conservado en el Museu de Prehistòria de València como inventario **13411**. La fuente permite una asociación bibliográfica de inventario, pero no la comprobación física propia de una auditoría museística.
- `IBR-PLM-0003` **Pech-Maho V**: **sin cambios**. El enlace anterior está truncado y el trabajo localizado `Els sistemes duals de les escriptures ibèriques` aborda sistemas duales en general: no constituye prueba suficiente de la identidad exacta de la inscripción V. No forzar emparejamientos.

## Métricas antes/después
Sobre 22 filas: URL vacía **1 -> 0**; enlaces truncados **2 -> 1**; sin lectura paleográfica completa acreditada **22** (sin cambios); pertenencia a HOLD **0** (sin cambios). La mejora es documental, no una nueva traducción validada.

## Observaciones de control de calidad
El auditor `scripts/iberos_core_corpus_audit.py` registra la ausencia de fuentes y los enlaces truncados. Sus tests fueron añadidos en una tanda anterior; verificar resultados CI antes de dar por pasadas esas pruebas.

## Próxima tanda
Localizar la edición específica de **Pech-Maho V**, identificar claves modernas y museísticas y comprobar si la fuente es efectivamente el mismo plomo, antes de corregir el registro.

# PRIMARY-METROLOGY-EVIDENCE-06 — expedientes con marca y masa, sin falsa precisión

Fecha de corte: 11 de noviembre de 2026. Se han identificado dos
ponderales con datos bibliográficos suficientemente específicos para
solicitar expedientes **primarios**.

## 1. Puig de la Misericòrdia (Vinaròs)

- **41,29 g según ficha n.º 2309 del Museu de Belles Arts de Castelló**,
  citada en Ferrer i Jané (2013), Quaderns de Prehistòria i Arqueologia
  de Castelló 31, 137–148.
- Excavación de 1983; procedencia de un nivel superficial UE 200 de
  la zona NO del asentamiento; atribución cronológica general al
  siglo II a. C. No confundir asociación estratigráfica y fecha
  exacta de fabricación.
- **Figura 1**: fotografía del ponderal con escala y signo de forma H,
  interpretado por el autor como **o** ibérico nordoriental.
- El autor documenta **autopsia el 7 de marzo de 2011**, pero NO consta
  un segundo lector independiente de la marca para IberOS.
- Instrumento de la pesada, su calibración, resolución, repetibilidad
  e incertidumbre: **NO DOCUMENTADOS** en los datos verificados.
- Fuente: https://dialnet.unirioja.es/descarga/articulo/4561912.pdf

## 2. Puig Castellar

- Ferrer i Jané (2013), **p. 145, nota 4**: una nueva pesada
  confirmada por Carme Rovira Hortalà en el MAC con una balanza de
  precisión dio **423,78 g**; la cifra no equivale a incertidumbre
  instrumental de ±0,01 g.
- Se señala una probable pérdida de consistencia/material del
  **anillo de hierro**. Esto introduce un sesgo por conservación
  distinto de un error de balanza.
- **Figura 6**: dibujo del ponderal. La lectura de un signo pequeño
  permanece controvertida; la autopsia y los intentos de limpieza no
  la resolvieron por completo. NO hay lectura lingüística gold.
- Inventario y ficha instrumental: por localizar en MAC.
- Fuente: https://dialnet.unirioja.es/descarga/articulo/4561912.pdf

## Solicitudes enviadas, sin coste

11-11-2026 desde la cuenta contacto.iberos@gmail.com:
- Museu de Belles Arts de Castelló:
  museubellesartscastello@ivc.gva.es, solicitud ficha 2309,
  incertidumbre instrumental, fotos y contexto, Gmail ID
  `1a1cc66e92e95a57`.
- Museu d'Arqueologia de Catalunya (Barcelona):
  infomac@gencat.cat, pesada de 423,78 g, examen del aro y dibujos,
  Gmail ID `1a1cc66efde40886`.

El Museo de Moncada, consultado previamente sobre Tos Pelat 418 g
y diez puntos, respondió el 5-11-2026 que aportaría documentación
cuando pudiera; **todavía no han llegado esas mediciones**.

## Puerta de calidad

Nunca inferir incertidumbre de la última cifra decimal. Registrar
el instrumento, su calibración, resolución, fecha, número de repeticiones,
dispersión, conservación/material y lecturas de la marca realizadas
**independientemente**, sin usar hipótesis lingüísticas para orientar
la lectura. Si faltan esos datos, el objeto permanece en
`PUBLISHED_MASS_ONLY` y NO se califica como muestra ciega.

Verificación automática:
```bash
python -m iberos.primary_metrology_evidence_06
pytest -q tests/test_primary_metrology_evidence_06.py
```

No se modifica FULL3406, los splits ni las métricas históricas.

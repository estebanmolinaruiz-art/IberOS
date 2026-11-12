# GeoSites G-129 — Sondeos paleoambientales, incertidumbre y anomalía Riegos

## Fuente primaria verificada
Ana María Blázquez Morilla, *L'Albufera d'Elx: evolución cuaternaria y reconstrucción paleoambiental a partir del estudio de los foraminíferos fósiles*, Universitat de València, tesis 2001, edición 2003, apartado 7.3, p. 107.
https://roderic.uv.es/bitstream/10550/15135/1/blazquez.pdf

El trabajo describe seis sondeos mecánicos realizados en febrero de 1996:
Pinet (30SYH081 278, alt. 1m, prof. 36m);
Picola (30SYH133 305, 2m, 23m);
Mórtoles (30SYH089 311, 2m, 31m);
Salinas (30S YH086 270, 1m, 30m);
Fondo (30SXH996 292, 8m, 12m);
Riegos (30SYH954 322, 9m, 8m).
Conservamos exactamente la cadena textual publicada, incluidos posibles errores.

## Geometría matemática
Las referencias tienen tres dígitos por eje dentro de una cuadrícula UTM
de 100km: representan CELDAS de **100m×100m** (no puntos exactos).
Se reconstruyen los límites de cada celda, se obtiene la distancia
mínima/máxima euclídea hasta el vértice A1 del BIC La Picola
(713265,4230490) y se conserva la geometría completa.
**El datum horizontal de los sondeos no se ha identificado en el texto
consultado.** A1 está expresado en ETRS89. Por ello la comparación
con A1 es solo PROVISIONAL, NO constituye distancia geodésica medida.

La referencia publicada para Riegos, 30SYH954 322, cae a unos 82km
al este de A1 según esa convención. Sustituir YH por XH produce un
desplazamiento exacto de cuadrícula de 100000m hacia el oeste,
plausible con la descripción de un cono de Crevillent, pero ESTO
ES UNA HIPÓTESIS, no una corrección verificada. El sondeo se
cuarentena para todas las operaciones espaciales hasta contrastar
el mapa original, figura 7.1, y obtener el datum.

## Regla cronológica
La tesis contiene descripción estratigráfica y métodos de datación
radiocarbónica. Durante G-129 se verificaron la tabla de coordenadas
y el método, **no** las edades calibradas de las capas concretas del
periodo 430–350 a. C. Una muestra de sedimento marino a cierta
profundidad no autoriza a etiquetar su ubicación como lago en el
siglo V a. C.; tampoco una cota moderna prueba suelo transitable.
La salida correcta del módulo es **ABSTAIN_NO_DATED_LAYER_GEOMETRY**,
0 celdas paleoambientales aceptadas, sin ruta generada.

La comparación documental señala dónde concentrar la validación
posterior: las columnas Picola, Mórtoles y Pinet, incluidas sus
estratigrafías y dataciones en la tesis. También hay que localizar
la figura 7.1 para verificar Riegos. No debemos interpolar seis
sondeos como si fueran un raster completo.

## Reproducción gratuita
```bash
python -m unittest discover -s tests -p 'test_geosites_paleocores.py'
python -c "from iberos.geosites_paleocores import audit_picola_paleocores; print(audit_picola_paleocores())"
```

Referencias complementarias:
- BIC La Picola, coordenadas A1 en ETRS89:
  https://www.boe.es/diario_boe/txt.php?id=BOE-A-2020-16669
- Blázquez y Usera 2004, síntesis (resúmenes de facies, no mapa de 430–350 a. C.).
- Módulos GeoSites G-127/G-128.

**Coste 0 euros. No altera Core científico ni despliega web.**

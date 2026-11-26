# GeoSites G-145 — Predicción nueva de dirección inicial y sensibilidad

Fecha: 2026-11-22; coste adicional 0 EUR. Esta es una predicción **matemática condicional**, no una orientación arqueológica medida.

Referencias ETRS89 EPSG:25830: A=(713265,4230490) vértice BIC La Picola, B=(701823.285,4234872.059) termas orientales La Alcudia; no son centros de puertas. Distancia 12252.154228m, azimut A→B 290.956325°.

**P-145-01 preregistrada:** la proyección instantánea de un avance unitario con azimut α hacia el destino vale cos(α−290.956325°). La distancia al objetivo aumenta si esta cantidad es negativa. Para los escenarios de salida α=25°–65° (NO se afirma que sea la dirección real de R2), la distancia aumenta inicialmente, pues el umbral en el primer cuadrante es α=20.956325°. Si se avanzan 100m: α=25° aumenta 7.458m la distancia y exige como mínimo 107.458m de sobrelongitud respecto a la recta; 45°: 41.083m y 141.083m; 65°: 69.730m y 169.730m.

**P-145-02 preregistrada:** con perturbaciones hipotéticas de radio r en cada extremo, la diferencia angular está acotada por arcsin(2r/D). Con r=250m el límite es 2.339°, inferior al margen 4.044° del caso α=25°: el signo negativo de la proyección es robusto bajo ESTE SUPUESTO. Con r=450m ya no hay esa garantía para el extremo α=25°. Los radios NO proceden de mediciones arqueológicas.

**Falsación independiente:** georreferenciar puerta NE Picola, puerta SE Ilici y medir eje R2 a partir de planta norteada, escala y al menos 4 puntos de control, con incertidumbre. Sustituir las referencias y recalcular, confrontar un segmento exterior real excavado y fechado. Ningún giro, paso de foso, tramo vial ni terreno paleogeográfico se ha confirmado.

**Fuentes:** Moret y Badie 1998 DOI 10.3989/aespa.1998.v71.274, documenta R2→puerta NE y plano fig.3; otro plano de A. Badie está indexado en https://cultura.castillalamancha.es/sites/default/files/2022-03/150_A__os_con_los___beros_MEDIA_low.pdf con norte y escala, pero la captura visual no fue procesable y no se ha medido orientación verdadera.

**Paquete local:** script Python independiente, 14 pruebas unitarias superadas, CSV, JSON y curva de sensibilidad. Sin cambios al Core, sin inferencia de carretera histórica.
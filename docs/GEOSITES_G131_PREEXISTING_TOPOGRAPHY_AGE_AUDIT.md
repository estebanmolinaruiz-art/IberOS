# GeoSites G-131 — Auditoría de datos topográficos y edades
Fecha: 2026-11-12. Coste adicional 0 EUR. Periodo 430–350 a. C. = años astronómicos -429 a -349.

## Archivos existentes verificados
Se inspeccionó /mnt/data. Hay ZIP de GeoSites G-127/G-128/G-129, CSV, JSON y mapa de auditoría G-130, pero **no hay ningún MDT, GeoTIFF, ASC, GeoPackage, SHP ni LAS/LAZ auténtico** en ese almacenamiento. Los archivos PDF locales blazquez.pdf, tent2013.pdf y geotemas7.pdf del directorio iberos_g92 tienen 0 bytes y no deben utilizarse como PDFs ya descargados. Esto no descarta datos en otras máquinas o sesiones.

## Revisión matemática
La Picola BIC A1: (713265, 4230490); La Alcudia Termas Orientales: (701823.285, 4234872.059), referencias EPSG:25830. Distancia recta 12252.1542 m, NO entre las dos puertas ni ruta histórica.
Se conservaron las seis cuadrículas MGRS 100 × 100 m publicadas para Picola, Mórtoles, Pinet, Salinas, Fondo y Riegos. Datum de sondeos sin confirmar; no se trata de GPS precisos. Riegos mantiene la referencia impresa 30SYH954 322 y se cuarentena: cambiar la letra de cuadrícula YH por XH desplazaría 100000 m, hipótesis no comprobada.

## Hallazgos bibliográficos
Blázquez y Usera (2004), Geo-Temas 7, páginas 129–132, https://sge.usal.es/archivos/GEO_TEMAS/Geo_temas_7.pdf : demuestra ambientes geológicos diversos en el Cuaternario, pero la facies lagunar datada en 198800 BP corresponde a una fase muy anterior. La existencia de gran laguna al menos hasta la Edad del Bronce no demuestra continuidad hasta 430–350 a. C.
Tent-Manclús (2013), https://doi.org/10.3989/estgeogr.201324 : las reconstrucciones regionales y el nivel marino son interpretativos; no aportan automáticamente polígonos SIG acreditados para cada año del periodo.
Blázquez y colaboradores (2010), https://doi.org/10.1016/j.quaint.2009.06.033 : su resumen abierto estudia en concreto Salinas, Pinet y Mórtoles. No se ha cotejado una columna de muestras calibradas y edades correspondiente a todo 430–350 a. C.

## Dictamen
0 capas cronoestratigráficas verificadas que documenten directamente el intervalo completo. 0 polígonos terrestres o palustres acreditados y georreferenciados para ese intervalo. Esto significa **falta de evidencia utilizable**, no ausencia de tierra, humedal o camino antiguo.

## Nueva regla G-131
Se exigen procedencia y datum, profundidad de muestra, facies, cronología calendario calibrada con curva y reserva, persistencia independiente del ambiente durante el intervalo y geometría SIG validada. **Una incertidumbre de datación que abarque 80 años no demuestra persistencia de la facies durante 80 años.**

Se creó paquete reproducible local G-131 con CSV, JSON, código y 10 pruebas unitarias locales superadas, sin modificarse el Core epigráfico. El código está empaquetado localmente, NO fusionado a GitHub. Próxima tarea material: conseguir tablas y perfiles originales de Salinas, Pinet y Mórtoles, cotejar la figura 7.1 y confirmar datum, sin pagar.

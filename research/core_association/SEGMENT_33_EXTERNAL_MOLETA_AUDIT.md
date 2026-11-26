# SEGMENT-33 — auditoría externa de SEGMENT-32 (Moleta del Remei)

Fecha: 2026-11-21. **Ejecución completada** [GitHub Actions #44959600936](https://github.com/estebanmolinaruiz-art/IberOS/actions/runs/44959600936), 3/3 pruebas de guardarraíl.

## Evidencia comprobada
Se descargó realmente el PDF original del volumen *Palaeohispanica* 8 (2008), `https://ifc.dpz.es/recursos/publicaciones/28/40/_ebook.pdf`. SHA-256: `2965fd62b2a040aa99bb5428bbe8018fba56ebfb201b35034e93a2c38b292e22`, 7.873.731 bytes, 315 páginas. Se detectaron y renderizaron la fotografía (fig. 4, p. 215; página PDF base 0 = 209) y el dibujo arqueológico (fig. 5, p. 216; página PDF base 0 = 210). La Moleta del Remei (Alcanar, Tarragona) es físicamente independiente de los dos plomos de Orleyl previamente estudiados.

## Confirmación solicitada
**NO CONFIRMADO que SEGMENT-32 generalice.** En Moleta no hay en el conjunto de datos actual un registro equivalente de fronteras de signos decididas por revisión independiente, ni un recorte de franja predefinido y homogéneo con los renglones de Orleyl. La fuente se obtuvo y examinó a nivel de página, pero no se ejecutó una evaluación de precisión externa legítima. Declarar 81,4 % para Moleta sería inventar la referencia.

El resultado `35/43` continúa siendo una métrica retrospectiva sobre Orleyl y no es exactitud epigráfica, OCR ciego ni validación interyacimientos.

## Archivos
`research/core_association/segment33_external_gate.py`, `research/core_association/test_segment33.py`, `.github/workflows/iberos-segment33.yml`. Artefacto de ejecución `iberos-segment33-external-audit` (incluye informe JSON y páginas de las figuras para análisis interno, no publicaciones de las figuras en repositorio público).

## Siguiente puerta concreta
Se necesita (i) recorte del texto en la fotografía y dibujo, (ii) anotación independiente signo por signo con zonas ambiguas y justificantes de revisión, (iii) presupuestos de cortes y tolerancia relativa congelados, (iv) aplicar las dos versiones del algoritmo sin retocar parámetros para evaluar precisión, cobertura y abstenciones.

No se alteró el Core ni C594/C474/C539/C541/FULL3406. Coste adicional 0 €.

# IBEROS-FULL-LINE-ALIGN-17 · Corrección basada en tinta, 16 noviembre 2026

**Resultado experimental (no es identificación paleográfica ni desciframiento).** Reprocesados los renglones iniciales de Orleyl V (figura 22, página PDF 65) y Orleyl VII-B (figura 25, PDF 111) a partir de los PNG extraídos de la edición de Fletcher de 1981.

Partiendo de ALIGN-16, se ha reducido la influencia de las líneas horizontales largas de la lámina mediante morfología, buscado mínimos de tinta cerca de los límites anteriores y aplicado la regla **no aceptar un cambio que aumente la tinta cruzada**. Se conservan los recuentos de posiciones editoriales, separadores y restituciones sin dibujo.

### Mediciones de la ejecución
- Orleyl V: 44 posiciones, 37 fronteras entre posiciones, 2 mejoradas, 35 sin cambios, 0 empeoradas, **5 fronteras con más de dos píxeles de tinta cruzada**.
- Orleyl VII-B: 26 posiciones, 22 fronteras, 1 mejorada, 21 sin cambios, 0 empeoradas, **1 frontera con más de dos píxeles de tinta cruzada**.
- Total: **70 posiciones, 59 fronteras interiores, 3 mejoradas, 6 todavía dudosas**.
- Siguen existiendo **9 anclas de puntuación** y **3 restituciones editoriales sin grafema observado**; la matriz conserva exactamente las 82 filas anteriores.
- **0 lecturas originales automáticas verificadas**; la precisión de OCR sigue sin calcularse.

El paquete local `IBEROS_FULL_LINE_ALIGN_17.zip` contiene `run.py`, `aligned_slots.csv`, `boundary_audit.csv`, dos overlays, dos zooms, `report.json` y README. Todos los archivos están incluidos en el ZIP y pasó comprobación CRC.

### Cautelas
El número de casillas de cada grupo sigue **condicionado por Fletcher**, no procede de una segmentación sin supervisión. Algunas fronteras verdes pueden estar en blanco y aun así dividir incorrectamente un signo compuesto, mientras que la eliminación de reglas horizontales puede quitar partes de trazos reales. La revisión paleográfica integral sigue pendiente. Los gráficos editoriales no deben publicarse en abierto sin autorización de reutilización.

**Core sin cambios. C594/C474/C539/C541 y FULL3406 intactos. Coste adicional 0 €.**
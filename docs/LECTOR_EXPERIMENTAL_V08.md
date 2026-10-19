# IberOS lector experimental — integración web y comparador

Fecha: 2026-10-19. Estado: PROTOTIPO FUNCIONAL; sin OCR paleográfico validado.

## Herramientas
- Web: `site/lector-experimental.html` — entrada de transliteración, glosas contextuales demostrativas y anotación gráfica manual; exporta JSON. No sube imágenes al servidor.
- Comparador: `scripts/iberos_visual_matcher_v08.py` — vecinos más próximos en imágenes recortadas, con control de hash SHA-256 y grupos físicos TRAIN/HOLD.
- Datos: `data/review/iberos_visual_matcher_manifest_v08.csv` — cabecera vacía. Sin muestras reales publicadas o autorizadas: el programa debe abstenerse.

## Instalación local
```bash
python -m pip install pillow numpy
python scripts/iberos_visual_matcher_v08.py data/review/iberos_visual_matcher_manifest_v08.csv --root .
```
Para evaluar, completar manifiesto con rutas relativas a `--root`, estados REVIEWED_SIGN, hash y piezas físicas disjuntas, y ejecutar `--evaluate`. Esto produce solo una evaluación descriptiva del reconocimiento de recortes, no prueba de traducción ni de VALIDATION-01.

## Límites
El vocabulario incluido en la interfaz es ilustrativo, no constituye una base léxica exhaustiva ni aporta prueba de que las glosas sean correctas. La herramienta gráfica solo produce rectángulos y valores propuestos por el usuario; ni reconoce glifos automáticamente ni verifica la atribución gráfica. La similitud visual no equivale a probabilidad calibrada. Mantener separados TRAIN/VAL/HOLD y no usar dibujos de un mismo objeto en grupos independientes.

## Criterios restantes para producción
1. Curación autorizada de imágenes auténticas con variantes y revisión independiente.
2. Pruebas automatizadas e integración CI de la versión experimental.
3. Benchmark ciego de reconocimiento visual, con tasa de abstención y errores por signario.
4. Modelo lingüístico contrastado contra baselines; VALIDATION-01 sigue abierto.
5. Verificación externa de despliegue de GitHub Pages y navegación desde el menú principal.

No declarar 'traducción automática', 'reconocimiento validado' ni 'despliegue confirmado' antes de evidencias.

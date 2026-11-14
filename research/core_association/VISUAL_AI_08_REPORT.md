# IBEROS-VISUAL-AI-08 · Sensibilidad del cotejo a bordes y recortes

Fecha: 2026-11-14. Estado: **EXPERIMENTAL**, **sin lectura independiente**, coste adicional 0 €. Core, C594/C474/C539/C541 y FULL3406 sin cambios.

## Prueba ejecutada con Orleyl V

A partir de 15 ventanas fotográficas de la lámina XVIII de *Materiales de la necrópolis ibérica de Orleyl* (1981) se compararon todas las 105 parejas con HOG en cuatro variantes:

1. Región completa;
2. Banda superior de 16/64 píxeles neutralizada;
3. Únicamente región central (recorte 10:54 en una normalización 64×64);
4. Descriptores de gradiente Sobel.

**Resultados:** 12/105 parejas cambian la similitud absoluta más de 0,10 respecto a la imagen completa después de retirar la banda superior o la periferia; el solapamiento entre los 5 mejores candidatos completos y los 5 mejores del centro es **2/5**. La primera pareja B06–B08 pasa de 0,87049 a 0,79525 al quedarse con el centro. Son puntuaciones del descriptor HOG, no probabilidades ni tasas de reconocimiento.

**Interpretación cauta:** los rankings pueden estar condicionados por bordes, fondo y contornos vecinos. El recorte también elimina rasgos genuinos: una caída de semejanza es evidencia de sensibilidad al procedimiento, no falsación definitiva de identidad paleográfica.

No existe reconocimiento fonético validado en esta prueba. Todas las ventanas proceden de un único objeto físico; no hay ninguna pieza HOLD independiente. Los 133 candidatos de Cathalaunia son metadatos rotulados y aún no fueron contrastados contra plantillas visuales obtenidas. Wikimedia Commons identifica ilustraciones SVG, pero no se pudo descargar una copia para una prueba de imagen reproducible en este entorno. No inventar asociación foto→valor.

Artefacto local reproducible generado en el hilo: `IBEROS_VISUAL_AI_08.zip`, con script, CSV de 105 parejas, informe JSON y galería. Requiere las imágenes de VISUAL-AI-06. No se suben imágenes de la publicación a GitHub por derechos no verificados.

**Siguiente umbral:** obtener un recorte paleográficamente completo y una plantilla SVG con licencia y forma verificadas, fijar la predicción antes de revelar la transcripción editorial y repetir en un segundo objeto físico.

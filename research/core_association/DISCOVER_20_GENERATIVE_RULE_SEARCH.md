# IBEROS-DISCOVER-20 — Generación de reglas mediante aprendizaje de motivos

Fecha: 2026-11-16. **Exploratorio; no traducción ni logro epigráfico validado.** Core, C594/C474/C539/C541 y FULL3406 sin cambios. Coste 0 €.

## Algoritmos probados
**Transferencia de motivos**: entrenar en los tokens editoriales de la primera línea de Orleyl V, generar automáticamente todas las cadenas contiguas de longitud 2–4 que aparezcan ≥2 veces; congelar la lista; buscarla en Orleyl VII-B; comparar el mayor motivo recuperado con 20.000 permutaciones de signos dentro de cada grupo puntuado. Invertir los objetos y excluir los grupos con valor dudoso W.

**Búsqueda de posiciones variables**: inducir prefijos de longitud 2–3 que aparecen al menos dos veces con el mismo seguidor en V; congelar prefijo→seguidor; medir si VII-B conserva prefijo pero cambia el seguidor. Evaluar máximo prefijo observado con 20.000 permutaciones.

## Resultados
- Entrenamiento V: 8 motivos repetidos de longitudes 2–4; el mayor transferido a VII-B es `N-W-L` (3 signos); p exploratoria para la longitud máxima 0,01705 (el estadístico alternativo longitud+hits tiene p 0,00865, NO es una significación corregida de todas las exploraciones).
- Entrenamiento VII-B: sin motivos repetidos bajo esos criterios, no hay predicción inversa.
- Posición variable: `N-W-L-I` (dos casos en V) frente a `N-W-L-BE` (uno en VII-B), p exploratoria de ancla máxima 0,01400.
- Excluir todos los grupos que contienen W: la señal desaparece por completo.
- Ahorro MDL ingenuo descontando el coste de almacenar cada motivo: no positivo; todavía NO hay estructura compresiva robusta.

**Cautelas fundamentales:** todas las etiquetas de signos provienen de una edición de 1981 y la alineación visual previa estuvo condicionada por esas etiquetas. No existe lectura visual autónoma, semántica contrastada ni predicción verdaderamente prospectiva: estos objetos y el motivo NWL se exploraron con anterioridad. Las dos piezas comparten ámbito arqueológico; no constituyen muestras contextuales independientes. Un prefijo con sufijo variable es compatible con un sistema puramente fonético y no prueba logografía.

## Próxima falsación
Verificar el contorno y lectura real del signo W sobre la fuente; después registrar una predicción sobre un **tercer objeto físico no usado previamente** y contrastar fonética/morfología frente a hipotético logograma y marca no lingüística. Si falla el cotejo de W, se descarta el candidato. La calidad del Core permanece protegida.

Paquete local reproducible: `IBEROS_DISCOVER_20.zip` (Python estándar, datos derivados de ALIGN-17, informes JSON y tabla CSV).

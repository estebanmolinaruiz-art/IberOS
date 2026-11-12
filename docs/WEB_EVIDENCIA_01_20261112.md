# WEB-EVIDENCIA-01 — Transparencia científica sin alterar el Core

**Fecha:** 2026-11-12. **Coste adicional:** 0 €.

## Problema abordado
La web ya distinguía fuentes e hipótesis en fichas individuales, pero el visitante carecía de un punto único y rastreable que mostrase claramente el alcance de la evidencia del proyecto. Sin tal síntesis, los recuentos internos de fichas, variantes editoriales y pruebas de software podían interpretarse equivocadamente como lecturas o traducciones confirmadas.

## Entrega
- Página pública `site/evidencia/index.html`: tres magnitudes con denominador semántico explícito, tabla de evidencia/preguntas abiertas, método de falsación, fuentes bibliográficas y vínculos a expedientes activos.
- Enlaces desde Fichas, Método, Publicaciones y Menú completo; entrada en sitemap.
- Prueba automatizada `tests/test-scientific-evidence-web.mjs` que comprueba descripciones sin sobreafirmaciones, fuentes auditables y visibilidad.
- La validación se añade a GitHub Actions en QA web gratuita.

## Base documental y advertencias
- **38** elementos de catálogo (piezas y controles), no 38 lecturas D3.
- **26** unidades de cotejo proceden de **cinco** piezas físicas; documentación CORE-VIS-01. No multiplicar evidencia por número de variantes.
- **0** traducciones semánticas validadas prospectivamente hasta este corte. Esta cifra se muestra como dato fechado, no como contador vivo.
- Candidatos de roles `-te` y morteros K.5.4: fuente retrospectiva, no gold oculto. Referencias [PR #152](https://github.com/estebanmolinaruiz-art/IberOS/pull/152), issues #149-#151 y #155.
- La página remite a ediciones y registros originales sin reproducir fotografías ajenas.
- Los tests CI protegen afirmaciones públicas pero no prueban validez lingüística ni sustituyen revisores ciegos.

## Exclusiones deliberadas
No modificar `src/iberos/`, `data/`, scripts del motor, particiones HOLD, FULL3406, C594/C474/C539/C541, métricas oficiales ni la portada con su diseño aprobado. No declarar nuevas inscripciones, descubrimientos o traducciones.

## Condición de publicación
Solo publicar después de pruebas web/CI con resultado positivo. Verificar la página `https://iberos-ia.com/evidencia/`, el enlace desde el menú y el sitemap en HTTPS, y que la copia `IberOS-respaldo` sigue disponible. La publicación no modifica el DNS ni Google Search Console.

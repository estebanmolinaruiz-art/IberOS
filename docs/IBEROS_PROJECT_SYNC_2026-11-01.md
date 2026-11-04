# IberOS — sincronización de estado del proyecto (2026-11-01)

## Alcance
Consolidación del trabajo del hilo web/Write/CORE con el proyecto general IberOS. Este registro distingue aplicación web, investigación científica y validación; **no** altera el diseño aprobado de la portada.

## Web pública
- URL: https://estebanmolinaruiz-art.github.io/IberOS/
- Portada aprobada: mantener composición actual. El aviso News / Proyecto La Picola es una mini piedra gráfica a la derecha con fotografía y enlace al proyecto; no es modal. Su asset es `site/assets/news-picola-stone.svg`, la foto `site/assets/la-picola-rec101.jpg`.
- La piedra News es una **recreación visual**, no una pieza arqueológica original ni restitución verificada.
- GitHub Pages: despliegue `80baeca6` finalizado con resultado success en la consulta del 01/11/2026. No se afirma que todas las pantallas estén validadas por usuario.

## IberOS Write
- Regla funcional acordada: palabras ibéricas con equivalencia documentada cuando exista evidencia suficiente; resto como adaptación fonográfica moderna etiquetada. El motor lingüístico puede abstenerse de traducir, pero eso no debe impedir la escritura gráfica.
- Objetivo visual: piedra mineral irregular, inscripción con efecto de cincel, signos ibéricos cotejados y exportación fiel.
- Se corrigió en `site/write/index.html` la exportación SVG para incorporar los glifos gráficos recuperables y señalar con huecos los no recuperables. Añadida prueba en `tests/test_write.mjs`.
- Limitación abierta: carga de glifos externos, contraste paleográfico, exportación PNG, y comprobación visual de profundidad de incisión. **No dar Write por terminado**.
- Especificación: `docs/IBEROS_WRITE_HYBRID_INSCRIPTION_SPEC_2026-10-23.md`.

## CORE — Dama de IberOS
- Objetivo: avanzar hacia la comprensión de la lengua ibérica con corpus de objetos reales, edición fiable y comparaciones reproducibles.
- `scripts/corex_p01.py` ahora incorpora `stability(rows)`: 20 divisiones de grupos físicos independientes, resumen de min/mediana/max de exactitud, y frecuencia de victorias del bigrama frente a baseline simple. Test en `tests/test_corex_p01.py`.
- El error de sintaxis detectado en la primera versión se corrigió en commit `35be965f`.
- Verificación en GitHub Actions de ese commit: `tests`, `Comprobaciones web gratuitas` y `Dama de IberOS CORE-X P01 admission` = success.
- Es prueba estadística de predicción de caracteres, **no** validación semántica, traducción histórica ni porcentaje de desciframiento.

## Investigación y documentación
- Prioridad sostenida: objetos físicos auténticos, inscripciones individualizadas, fotos/capturas o enlaces al visor 3D original, lecturas editoriales, procedencia y licencias.
- Revisiones abiertas: asignación de variantes gráficas, certificación de signos dudosos, validación independiente y ampliación de corpus/bibliografía hasta 500–1.000 referencias **pertinentes** (sin tratar el volumen bruto como calidad científica).

## Próxima secuencia
1. Completar Write: mapa fuente-signo-glifo trazable, correspondencias que falten, exportación fiel y prueba visual en iPhone/PC.
2. Ejecutar CORE-X estabilidad sobre registros que pasen el filtro de independencia; conservar métricas y la abstención científica donde corresponda.
3. Revisar fichas e inventario para unir pieza física, edición, foto, licencia y CORE.
4. Mejorar UX interior sin modificar portada aprobada ni introducir overlays intrusivos.

## Criterios de evidencia
Los pases de CI garantizan solo las aserciones automatizadas disponibles. Separar siempre **implementado**, **desplegado**, **probado por navegador**, **comprobado por usuario** y **científicamente validado**.


## Sincronización nominal 2026-11-04
- **Nombre oficial vigente del programa experimental: Dama de IberOS.**
- La denominación anterior «Dama de Ilice» queda únicamente como referencia histórica o nombre técnico heredado de archivos/rutas, cuando renombrarlos pudiera romper compatibilidad.
- Ningún cambio de nombre modifica métricas, evidencia, estados de validación ni resultados científicos.

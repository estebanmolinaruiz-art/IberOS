# WEB-EVIDENCIA-02 — Pasaporte de evidencia por objeto

**Fecha:** 12-11-2026. **Coste adicional:** 0 €. **Resultado:** mejora de presentación; ninguna nueva lectura o traducción validada.

## Implementación

- `site/assets/scientific-evidence-passport.mjs`: panel HTML seguro generado desde los campos ya existentes de `scientific-review-queue-v1.json` (38 registros) y `epigraphic-visual-registry-v1.json` (7 expedientes gráficos).
- `site/ficha/index.html`: nuevo pasaporte con ficha individual `OBJECT_ID`, procedencia bibliográfica, estatus real de identificadores físicos, revisión paleográfica, figura, derechos y bloqueos. Si algún registro falta o no se carga, la interfaz no promociona evidencia y muestra una advertencia.
- `tests/test-scientific-evidence-passport.mjs`: 38 casos de catálogo, fallos de fuente gráfica, protección de contenido HTML malicioso y continuidad de la página. La prueba se integra en QA web.
- Las URL externas solamente se incluyen si tienen esquema HTTPS válido; imágenes con derechos no comprobados **no se incrustan**. Solo enlaces a fuentes originales permitidas.

## Interpretación científica

`physical_independence_audited=true` comunica que existe una auditoría, **no** que haya gold semántico independiente; `source_identifiers_verified=true` tampoco es cotejo paleográfico. El mapeo visual únicamente se marcaría revisado si el registro explícitamente lo acredita. El parámetro `publication_approved` es autorización interna de segmentos, nunca equivalencia con traducción validada. La capa semántica permanece no validada prospectivamente.

No modifica registros de evidencia, C594/C474/C539/C541, métricas, hipótesis, CORE, FULL3406, catálogo ni particiones HOLD. No añade nuevas publicaciones ni reproduce imágenes sin licencia.

## Pruebas y publicación

Unificar como un solo paquete de PR, pasar tests, benchmark, QA gratuita y navegador Chromium. Solo fusionar si todas las pruebas pasan. Publicar con disparador explícito de GitHub Pages. Verificar `https://iberos-ia.com/ficha/?id=IBR-PLM-0002`, una pieza sin registro gráfico y el respaldo público independiente.

**Limitación:** la interfaz no constituye una adjudicación epigráfica nueva. El resultado sigue a la espera de cotejos humanos independientes.

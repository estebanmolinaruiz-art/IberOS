# Sincronización transversal — IberOS+ Web / fichas / laboratorio (2026-10-16)

**Fuente de verdad técnica:** [rama main](https://github.com/estebanmolinaruiz-art/IberOS) del repositorio `estebanmolinaruiz-art/IberOS`.  
**Punto de corte comprobado:** `d0c08ce02f739f9fe96ccd2ef2a542d89f8b2ea1`.  
**Alcance:** coordinación entre WEB pública, Corpus/fichas, Laboratorio, publicación científica y Core. **No implica sincronización automática de historiales de ChatGPT**, ni actualización de releases distribuidas.

## Verificación en el punto de corte
- **tests:** éxito, ejecución [38924299114](https://github.com/estebanmolinaruiz-art/IberOS/actions/runs/38924299114).
- **Comprobaciones web gratuitas:** éxito, ejecución [38924298776](https://github.com/estebanmolinaruiz-art/IberOS/actions/runs/38924298776).
- **GitHub Pages:** aún en curso en la consulta, ejecución [38924298663](https://github.com/estebanmolinaruiz-art/IberOS/actions/runs/38924298663). No declarar completado hasta comprobar su resultado y marcador de despliegue.
- El último despliegue **confirmado exitoso antes de ese corte** corresponde al commit `428fab0a499a39bcce5912a99745fb43a1c0f8ac`.

## Avances ya incorporados a main
1. **Demostraciones públicas** — `site/demostracion/index.html`: Tivissa `IBR-PLM-0002`, Pech-Maho `IBR-PLM-0003` y Coimbra `IBR-PLM-0004`. Se nutren de `site/data/ficha-enrichment-featured.json`; son hipótesis editoriales, no traducciones literales verificadas. Enlazadas desde `site/presentacion/`, `site/mapa-web/` y el Laboratorio.
2. **Fichas visuales** — `site/ficha/index.html`: panel de interpretación más legible en móvil y PC, leyenda de estratos documentales y advertencia de incertidumbre. Regresión Chromium de tipografía ajustada en `scripts/test-laboratorio-browser.mjs`, commit `4a1a523a`, con pruebas posteriormente superadas.
3. **Archivo científico** — `site/fichas/index.html`: filtro por publicación, resumen de cobertura a partir de `fiche_publication_status_v1.json`, prioridades desde `fiche_publication_priority_v1.json`, protocolo de revisión y enlaces por objeto al cuaderno del Laboratorio. La publicación de estos JSON se genera en workflow; pueden no estar versionados como archivos individuales en `main`.
4. **Regresiones** — `scripts/test-integration.mjs`: verifica la visualización de estados, la trazabilidad de la documentación pendiente y la prohibición de tratar una hipótesis editorial como validación semántica.
5. **Documentación pública** — `docs/PRESENTACION_PUBLICA_IBEROS_2026.md`: guion de presentación y delimitación de capacidades.

## Compatibilidad con los hilos científicos
- Mantener intactos los gates de **C594 / C474 / C539 / C541** y las métricas congeladas documentadas en `docs/PROJECT_SYNC_2026-10-14.md`.
- Distinguir `PUBLICABLE_EDITORIAL` de `translation_validated`: **nueve hipótesis editoriales con fuentes recuperadas** según `docs/PUBLICATION_BATCH_2026-10-16.md`; ninguna debe anunciarse como traducción contrastada.
- **Corpus de 38 objetos** no equivale a 38 estudios cerrados. Las lecturas sin cotejo primario y las imágenes sin permiso acreditado permanecen pendientes.
- Bibliografía, descubrimiento, 3D y dispositivos móviles son flujos relacionados, pero la presente sincronización **no acredita** 500 referencias curadas, derechos de todos los modelos 3D ni compilaciones instalables de la app.
- No adelantar conclusiones del Core con resultados puramente web; conservar evidencia → inferencia → hipótesis → evaluación independiente.

## Próximos bloqueos verificables y responsables funcionales
| Flujo | Próxima acción y criterio de cierre |
|---|---|
| WEB / DevOps | Confirmar ejecución Pages `38924298663` y marcador SHA público; si falla, revisar logs antes de anunciar éxito |
| Fichas / Epigrafía | Cotejar edición primaria, transcripción y cita específica de Llíria, Castellet de Bernabé y La Joncosa antes de promoción editorial |
| Core / Investigación | Mantener salida sin promoción semántica hasta validación adversarial e independencia de testimonios |
| Biblioteca | Ampliar referencias verificadas, con deduplicación DOI y trazabilidad pieza ↔ fuente |
| Patrimonio 3D | Mostrar solo modelos con derechos de reutilización verificados; enlazar externamente cuando no exista permiso |
| Presentación | Capturas reales del portal, demostración de casos y dossier basado exclusivamente en evidencia visible |

## Uso por los demás hilos
Consultar primero `main`, los workflows y este documento; después revisar `docs/PROJECT_SYNC_2026-10-14.md`, `docs/PUBLICATION_BATCH_2026-10-16.md` y el expediente del módulo correspondiente. Evitar sustituir archivos del Core o reconstruir ZIP desde una copia anterior sin comparar SHA, procedencia y esquema.

## Adenda de integración posterior — lote Coimbra y 13 expedientes

Después del punto de corte anterior, la rama compartida incorporó:
- `e467f66f`: cita de edición de Coimbra para el caso `kaŕb` (páginas 155–157), conservando la hipótesis nominal como **no validada**.
- `4f6200d7`: comprobación de procedencia de Coimbra y **13 fichas con interpretación editorial pública** según el título del commit; este recuento corresponde a cobertura editorial, **no** a 13 traducciones demostradas. Consultar la generación de `fiche_publication_status_v1.json` para el recuento de cada despliegue.

**Comprobación CI del corte `4f6200d7`:** tests y comprobaciones web completadas con éxito; GitHub Pages seguía en progreso durante esta consulta. La presencia de un commit posterior de sincronización documental no valida por sí sola el despliegue de ninguna versión.

**Instrucción común:** antes de cotejar o ampliar Coimbra, consultar la edición citada y su trazabilidad; preservar la separación entre observación paleográfica, propuesta onomástica y equivalencia semántica. Los módulos de WEB no deben promover hipótesis de las 13 fichas al Core.

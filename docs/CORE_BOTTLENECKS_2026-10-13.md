# IberOS CORE — bloqueos, oportunidades y plan de desbloqueo
Fecha: 2026-10-13
Tipo: diagnóstico técnico-científico, sin revisión de autoridad ni promoción semántica.

## 1. Hallazgo principal
Distinguir bloqueo de ingeniería (reproducibilidad/contratos) de bloqueo epigráfico (falta de nuevos testimonios independientes). Ninguna corrección de software hace verdadera una interpretación no demostrada.

## 2. Prioridades ejecutables (sin nueva evidencia)
P0 — Ejecutar batería total Python y Node tras los últimos commits y comprobar resultado de Actions en main. **Aún sin certificar en este diagnóstico.**
P0 — Reproducir `scripts/benchmark_snapshot.py` y comparar byte a byte con `data/benchmark/benchmark_results_v1.0.1.json`; impedir alteración accidental de 38 objetos, 37 unidades y gates abiertos.
P0 — Auditar que `validate_reconstruction` requiere fuentes *declaradas* pero no comprueba todavía acceso o correspondencia a pasajes verificables: hace falta añadir IDs de testigo/edición, localizador y evidencia documental controlada, sin asignar significado automáticamente.
P1 — Diseñar fixtures adversariales para traducciones incompatibles, fuentes duplicadas, copias, pseudoescritura y pérdida de información durante exportación.
P1 — Mapear la autoridad de cada segmento a PHYS_ID y LEAK_GROUP y separar lectura paleográfica de traducción; no basta compartir OBJECT_ID.
P1 — Disponer de informes legibles y machine-readable por familia que incluyan `BLOCKED`, `OPEN`, evidencia faltante y criterio exacto de cierre.
P2 — Verificar consistencia del contrato Python/API con la futura interfaz web; trabajo visual en su hilo correspondiente.

## 3. Bloqueos científicos por familia (autoridad congelada)
| Familia | Bloqueo concreto | Evidencia necesaria | Accion investigadora |
|---|---|---|---|
| ROK | Destinatario/beneficiario y dirección no fijados | Segunda construcción físicamente independiente que identifique rol | Buscar paralelos en ediciones revisadas; auditar la independencia antes del contraste |
| KA/KE/KU | Dirección transaccional abierta | Marcador o contexto externo inequívoco independiente | Compilar contrastes con roles anclados extralingüísticamente |
| SALIR | Falta pase prospectivo | Ocurrencia de contexto económico/valor preespecificado | Prerregistrar criterio y probar en testimonio no usado para diseñarlo |
| KUTUR | Hipótesis estrecha abierta | Nueva ocurrencia independiente con restricciones morfológicas y contextuales | Búsqueda documental dirigida y test adversarial |
| BAIDES/BATIR | Rótulos institucionales exactos abiertos | Prueba ortogonal procedimental o bilingüe | Matriz de alternativas con predicciones contrarias |
| NUM 7/8/9 | Valor exacto sin cierre | Relaciones cuantitativas externas verificables | Excluir C.1.8/SORSE como ancla física y testar cómputos falsables |
| D(E/I) | Función gramatical no discriminada | Prueba preinscrita, cobertura de ambas ramas, procedencia limpia | Ejecutar `DEDI-COMBINED-GATE-01` con datos nuevos y revisión externa |

## 4. Rutas con mayor rendimiento
**Ruta técnica inmediata:** reproducibilidad + trazabilidad por segmento + controles adversariales; la podemos ejecutar sin alterar hipótesis y proporciona una base verificable.
**Ruta científica prioritaria:** preparar protocolos prospectivos ROK, KA/KE/KU y SALIR, localizando nuevas piezas independientes, no recontando las mismas ediciones.
**Regla de no-cierre:** si no existe evidencia externa que discrimine, el gate sigue OPEN/BLOCKED. Tests sintéticos no aportan evidencia lingüística.

## 5. Estado congelado y alcance
CORE 27/45 (60.0%), CORE + INFER 28/45 (62.2%): indicadores internos de release, NO tasa de desciframiento. Autoridad C594/C474/C539/C541. Referencia: `docs/BENCHMARK.md`, `docs/FAMILY_DASHBOARD_01_2026-10-08.md`, `docs/FAMILY_GATE_01_2026-10-08.md`, `docs/PROJECT_SYNC_2026-10-13.md`.

## 6. Condición de avance real
Una familia progresa científicamente cuando una prueba registrada previamente y físicamente independiente discrimina hipótesis rivales, se auditan fuentes y dependencias y hay revisión explícita. La implementación de tests por sí sola no satisface esa condición.

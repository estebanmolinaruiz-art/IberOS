# IberOS — auditoría KUTUR y D(E/I) (2026-10-15)

Implementación de consulta conservadora en `src/iberos/kutur_dedi_audit.py`. Reutiliza matrices congeladas y la puerta de entrada `dedi_combined_gate`, sin añadir lecturas o observaciones artificiales.

**KUTUR**: el protocolo `KUTUR-PROSPECTIVE-01` sigue abierto. La familia KUTU-/KUTUR requiere ocurrencia segura no utilizada y contexto de escritura, inscripción o formulario determinado independientemente. Queda consignado su falsador: ocurrencias repetidas seguras que pertenezcan inequívocamente a ámbitos semánticos ajenos al de escritura/formulario. Se informan candidatos y bloqueos de la matriz existente.

**D(E/I)**: se prueba explícitamente el comportamiento con cero observaciones; los filtros documental y predictivo permanecen bloqueados. Se requiere una comparación prospectiva con observaciones físicas y lecturas paleográficamente válidas, reglas fijadas previamente, controles de dependencia y preregistro verificable. Ninguna ausencia de evidencia puede clasificarse como confirmación.

**Alcance**: auditoría interna reproducible, sin nuevo testimonio externo. `new_external_evidence_checked=false`, `automatic_core_promotion=false`. Las métricas C594/C474/C539/C541 no varían. Pruebas en `tests/test_kutur_dedi_audit.py`.

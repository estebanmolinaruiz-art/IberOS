# METROLOGY-PREREG-LOCK-08 — verificación previa de predicciones

Criterio: la propuesta de diciembre de 2026 de una predicción ibérica
no puede basarse en que alguien marque casillas de «nueva»,
«independiente» y «prerregistrada». Esas declaraciones necesitan
soporte **externo** de archivo institucional o repositorio fechado.

Se necesitan seis referencias con URL, sello horario y SHA256:
inventario institucional, cotejo físico contra alias y FULL3406,
datos de calibración, lecturas paleográficas independientes
(sin conocer masa ni modelo), registro externo del pronóstico y
cantidad física de evaluación.

El pronóstico queda expresado en un JSON canónico cuyo SHA256 debe
coincidir con el depósito externo. El registro debe preceder al
etiquetado independiente. Se exigen modelos rivales:
A_O_KI_10_12, WEIGHT_FAMILY_2_1_G, NULL_BASELINE.
Se registran reglas de abstención y controles negativos.

**Limitación fundamental:** una URL y fecha escritas en un JSON
NO demuestran que existan, que el firmante tenga autoridad, que
el contenido vinculado tenga ese SHA ni que el dato sea nuevo.
Este validador local **nunca activa** 
\`ready_for_independent_evaluation\` sin comprobación externa real.
Un hash local verifica integridad pero NO certifica antigüedad
ni autoría. El siguiente paso exige auditar los documentos
institucionales y el depósito con fecha comprobable.

La evaluación sigue sin gold independiente. No se lee FULL3406
ni se modifica Core oficial.

\`\`\`bash
python -m iberos.metrology_prereg_lock_08 contract.json --json decision.json
pytest -q tests/test_metrology_prereg_lock_08.py
\`\`\`

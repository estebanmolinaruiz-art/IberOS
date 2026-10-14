# Auditoría conjunta de gates prospectivos: ROK y KA/KU

La función `audit_prospective_gates()` compara **sin modificar** las matrices ya implementadas de `ROK-RECIPIENT-02` y `KA-DIRECTION-PROSPECTIVE-01`. Devuelve por testimonio los criterios observados y los requisitos que faltan, así como el experimento independiente preciso que se debe buscar para desbloquear cada gate.

La función es de **reproducción interna**; no consulta publicaciones externas nuevas ni recalifica testigos. En particular, F.9.5 y F.9.7 siguen independientes como referencias editoriales y ambos requieren el rol de destinatario fijado externamente. En KA, los datos retrospectivos de Bastida no pueden fijar prospectivamente por sí mismos la dirección KA/KU.

`new_external_evidence_checked=false`; `automatic_core_promotion=false`. Los estados derivados se contrastan mediante `tests/test_prospective_gate_audit.py`. El estado científico congelado se conserva.

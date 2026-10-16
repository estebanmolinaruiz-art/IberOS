# Lecturas editoriales existentes: cola de revisión

Se ha identificado en `site/data/epigraphic_extraction_candidates_v1.json` una colección de tres posibles objetos epigráficos adicionales: anillo de Soses, plomo de Gádor y vaso de Torres. Sus identificadores `SOURCES-*` **no pertenecen al corpus curado**. Soses contiene variantes editoriales atribuidas, pero carece de transcripción aprobada; las otras dos entradas también están pendientes de requisitos documentales.

`scripts/export_web_core.py` extrae exclusivamente variantes existentes `edition_readings[].reading` a `site/data/editorial_readings_review_v1.json`. Guarda la atribución y ubicación bibliográfica declarada, sin transformar una variante histórica en lectura independiente. Todos los registros exportados fijan `exact_object_match_verified=false`, `transcription_checked_against_edition=false`, `eligible_for_core_execution=false`. No se crean fichas del corpus curado ni se generan traducciones.

Las fichas editoriales IBR-MUS-0001 (Caminreal) e IBR-LAP-0005 (Sagunto) tienen bibliografía general en `bibliography`, pero `citation` vacío. Esta bibliografía indica dónde revisar, sin certificar todavía el argumento interpretativo concreto. Se mantienen fuera del feed de hipótesis publicables hasta documentar esa relación.

Próximo paso: cotejar cada variante contra la publicación señalada, registrar el pasaje/figura y firmar una revisión humana verificable; solo después podrían prepararse lecturas elegibles para el CORE.

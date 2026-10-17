"""Audit-ready review queue for named featured inscriptions.

A citation is a lead to an edition, not confirmation that a reading was
checked against a facsimile. The registry never self-approves.
"""
from __future__ import annotations

def build_documentary_evidence(featured: list[dict]) -> dict:
    records=[]
    for item in featured:
        oid=item["OBJECT_ID"]
        citations=[x for x in item.get("bibliography",[]) if isinstance(x,str) and x.strip()]
        own_citation=str(item.get("citation") or "").strip()
        is_internal=own_citation.lower().startswith(("cita sugerida","molina ruiz"))
        primary=citations[0] if citations else ""
        records.append({
            "object_id":oid,
            "editorial_fiche_path":item.get("pdf_path"),
            "citation_in_fiche":own_citation,
            "self_citation_only":bool(is_internal),
            "first_bibliographic_reference":primary,
            "original_edition_page_or_figure_checked":None,
            "edition_comparison_notes":None,
            "reviewer":None,
            "review_date":None,
            "reading_approved":False,
            "image_license_evidence":None,
            "three_d_license_evidence":None,
            "next_action":"Cotejar lectura con la edición y registrar página o figura, revisión y discrepancias",
        })
    return {"schema":"IberOS-Documentary-Evidence-Review/1.0",
            "record_count":len(records),"records":records,
            "automatically_validated":False,
            "notice":"Citas internas y bibliografía no equivalen a cotejo original o revisión independiente."}

// Read-only scientific evidence passport for the published IberOS fichas.
// Never upgrades an editorial reading to independently validated palaeography.
const esc=value=>String(value??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const goodUrl=u=>typeof u==='string'&&/^https:\/\//i.test(u)&&!/[<>"'\s]/.test(u);
const state=(ok,yes,no)=>ok?yes:no;
const asArray=v=>Array.isArray(v)?v:[];
export function renderEvidencePassport(record,visual,id){
  const refs=asArray(record?.references_checked);
  const checks=asArray(record?.required_checks);
  const blockers=asArray(record?.technical_audit?.blockers);
  const figures=visual?.figure_locator||record?.original_edition?.figure_locator||'Localizador gráfico sin confirmar';
  const edition=record?.original_edition||null;
  const graphicMapped=visual?.sign_mapping_status==='SIGN_MAPPING_REVIEWED'&&asArray(visual?.glyphs).some(g=>g.reviewed===true&&g.source_position_verified===true);
  const publication=record?.publication_approved===true;
  const physicalAudit=record?.technical_audit?.physical_independence_audited===true;
  const sourceIds=record?.technical_audit?.source_identifiers_verified===true;
  const hasVisual=!!visual;
  const rights=visual?.rights_verified===true&&visual?.image_reuse_permission_verified===true;
  const refsHtml=refs.length?refs.map(item=>{
    const caption=esc(item.citation||item.title||'Referencia editorial');
    const link=goodUrl(item.url)?'<a href="'+esc(item.url)+'" target="_blank" rel="noopener noreferrer">'+caption+' ↗</a>':caption;
    return '<li>'+link+' · <code>'+esc(item.status||'Estado no declarado')+'</code>'+(item.locator?'<span> · '+esc(item.locator)+'</span>':'')+'</li>';
  }).join(''):'<li>No hay referencias individuales acreditadas en esta cola de revisión.</li>';
  const checkHtml=[...new Set([...blockers,...checks].filter(x=>typeof x==='string'&&x.trim()))].slice(0,8).map(x=>'<li>'+esc(x)+'</li>').join('')||'<li>Sin comprobaciones individualizadas cargadas: consultar expediente original.</li>';
  return '<section class="wrap" id="evidence-passport" aria-label="Pasaporte de evidencia científica" style="margin:24px auto">'
    +'<div class="research-card" style="padding:22px;border:1px solid #bfa477;border-radius:12px;background:#fffaf0;color:#173747">'
    +'<div class="section-kicker">Trazabilidad por pieza · sin inferencias automáticas</div>'
    +'<h2 class="section-title">Pasaporte de evidencia</h2>'
    +'<p><strong>Objeto:</strong> <code>'+esc(id)+'</code> · <strong>Referencia:</strong> '+esc(record?.epigraphic_reference||visual?.epigraphic_reference||'No especificada')+'</p>'
    +'<p><strong>Estado editorial consignado:</strong> '+esc(record?.scientific_state||'Sin expediente individual registrado')+'. Este estado no certifica cotejo fotográfico ni significado.</p>'
    +'<ul>'
    +'<li><strong>Identificadores de fuente:</strong> '+state(sourceIds,'auditoría de identificadores registrada','verificación aún no acreditada')+'.</li>'
    +'<li><strong>Independencia material:</strong> '+state(physicalAudit,'auditoría registrada (no equivale a gold externo)','auditoría aún pendiente')+'.</li>'
    +'<li><strong>Cotejo de signos por imagen:</strong> '+state(graphicMapped,'mapeos gráficos revisados registrados','sin verificación gráfica independiente consignada')+'.</li>'
    +'<li><strong>Publicación de segmentos:</strong> '+state(publication,'aprobación interna registrada; revisar alcance','sin aprobación de segmentos')+'.</li>'
    +'<li><strong>Traducción semántica:</strong> no validada prospectivamente en IberOS; no inferirla del estado editorial.</li>'
    +'<li><strong>Reproducción de imágenes:</strong> '+state(rights,'permiso declarado en el registro (revisar condiciones)','sin permiso de reproducción acreditado aquí')+'.</li>'
    +'</ul>'
    +'<p><strong>Figura o fotografía:</strong> '+esc(figures)+'. '+(hasVisual?'Expediente gráfico: '+esc(visual.status||'sin clasificación')+'.':'No consta expediente gráfico individual en el registro público.')+'</p>'
    +(goodUrl(visual?.source_url)?'<p><a href="'+esc(visual.source_url)+'" rel="noopener noreferrer" target="_blank">Consultar fuente gráfica original ↗</a></p>':goodUrl(edition?.url)?'<p><a href="'+esc(edition.url)+'" rel="noopener noreferrer" target="_blank">Consultar edición original ↗</a></p>':'')
    +'<details><summary><strong>Fuentes, localizadores y estado editorial ('+refs.length+')</strong></summary><ul>'+refsHtml+'</ul></details>'
    +'<details><summary><strong>Qué falta para la validación</strong></summary><ol>'+checkHtml+'</ol></details>'
    +'<p style="font-size:.88rem"><a href="../evidencia/">Criterios de falsación y niveles de evidencia →</a> · Los registros mostrados pueden contener revisiones editoriales dependientes; una referencia no equivale a una observación ciega.</p>'
    +'</div></section>';
}

import {readFileSync,existsSync} from 'node:fs';
import {createIberOS} from '../site/webengine/iberos-web.mjs';
import {readFile} from 'node:fs/promises';
import {fileURLToPath} from 'node:url';
globalThis.fetch=async url=>{try{const body=await readFile(fileURLToPath(url));return {ok:true,text:async()=>body.toString('utf8')}}catch{return {ok:false,status:404,text:async()=>''}}};
const assert=(ok,message)=>{if(!ok)throw Error('INTEGRACIÓN: '+message);console.log('✓ '+message)};
const base='site/';
const json=p=>JSON.parse(readFileSync(base+p,'utf8'));
assert(existsSync(base+'data/core_object_audit_v1.json'),'Export científico Python generado');
const audit=json('data/core_object_audit_v1.json');
const engine=await createIberOS();
const registry=engine.loadRegistry();
const ids=new Set(registry.map(x=>x.OBJECT_ID));
const auditIds=new Set(Object.keys(audit.objects||{}));
assert(ids.size===38&&audit.object_count===38&&auditIds.size===38,'Ambos cores contienen 38 objetos únicos');
assert([...ids].every(id=>auditIds.has(id))&&[...auditIds].every(id=>ids.has(id)),'Identificadores Python y JS coinciden exactamente');
assert([...ids].every(id=>audit.objects[id].object_id===id&&audit.objects[id].automatic_core_promotion===false),'Auditoría por pieza sin promoción científica ficticia');
const ficha=readFileSync(base+'ficha/index.html','utf8');
const lab=readFileSync(base+'laboratorio/index.html','utf8');
const atlas=readFileSync(base+'atlas/index.html','utf8');
const statusPage=readFileSync(base+'estado/index.html','utf8');
const library=json('data/iberian_resources.json');
const libraryPolicy=json('data/library-growth-policy-v1.json');
const libraryQueue=json('data/library_candidates_v1.json');
const bibliographyFichas=json('data/bibliographic_fichas_v1.json');
const bibliographyPage=readFileSync(base+'bibliografia/index.html','utf8');
assert(bibliographyPage.includes('bibliographic_fichas_v1.json')&&bibliographyPage.includes('epigraphic_extraction_audit_v1.json'),'Public bibliography presents fichas and Core eligibility audit separately');
assert(bibliographyPage.includes('extractionCards')&&bibliographyPage.includes('missing_requirements'),'Bibliographic viewer exposes individual Core gate requirements');
assert(readFileSync(base+'recursos/index.html','utf8').includes('../bibliografia/'),'Library links to public bibliographic fiche viewer');
const extractionQueue=json('data/epigraphic_extraction_candidates_v1.json');
const extractionAudit=json('data/epigraphic_extraction_audit_v1.json');
const extractionScreening=json('data/epigraphic_screening_v1.json');
assert(libraryQueue.items.length>=10&&bibliographyFichas.items.length===libraryQueue.items.length,'Expanded bibliography creates one reviewable fiche per unique reference');
assert(extractionQueue.items.length>=3&&extractionQueue.items.some(x=>x.authenticity_status==='AUTHENTICITY_DISPUTED'),'Corpus intake preserves disputed object authenticity and source attribution');
assert(extractionScreening.items.length===extractionQueue.items.length&&extractionScreening.items.every(x=>x.core_rules_executed===0&&x.automated_translation===null),'Pre-Core epigraphic screening does not invent rule results or translations');
assert(extractionScreening.items.some(x=>x.object_id==='SOURCES-SOSES-RING-1890'&&x.variant_count===3),'Soses screening preserves three contrasting attested edition variants');
assert(extractionScreening.items.some(x=>x.object_id==='SOURCES-SOSES-RING-1890'&&x.variant_comparisons?.length===3&&x.variant_comparisons.every(y=>y.meaning_inferred===false&&y.grapheme_differences.length>0)),'Soses variants have three mechanical grapheme contrasts, never semantic claims');
assert(extractionQueue.items.length===extractionAudit.items.length&&extractionQueue.items.every(x=>!x.transcription&&x.core_analysis_allowed===false)&&extractionAudit.items.every(x=>x.ready_for_core===false&&x.core_status==='BLOCKED_UNVERIFIED_EVIDENCE'),'Sourced inscription leads remain blocked until transcription and independent review');
assert(extractionQueue.items.some(x=>x.object_id==='SOURCES-SOSES-RING-1890'&&x.edition_readings?.length===3&&x.edition_readings.some(v=>v.reading==='belśtaŕtike')&&!x.transcription),'Soses preserves variant edition readings without claiming independently verified transcription');
assert(readFileSync('scripts/audit_epigraphic_extractions.py','utf8').includes('independent_review_completed'),'New epigraphic object processing requires independent review');
assert(bibliographyFichas.items.length===libraryQueue.items.length&&bibliographyFichas.items.every(x=>x.type==='BIBLIOGRAPHIC_SOURCE_NOT_OBJECT'&&x.core_processing.status==='BLOCKED_UNVERIFIED_OBJECT'&&x.core_processing.rule_results.length===0),'Bibliographic fichas cannot be mistaken for validated inscriptions or automatic Core results');
assert(libraryQueue.items.length>=5&&libraryQueue.items.every(x=>x.status==='PENDING_EDITORIAL_REVIEW'&&x.core_evidence_approved===false&&x.doi.startsWith('10.')),'Candidate bibliography has DOI references and cannot be promoted without review');
assert(new Set(libraryQueue.items.map(x=>x.doi.toLowerCase())).size===libraryQueue.items.length,'Candidate bibliography has no duplicate DOI identifiers');
assert(readFileSync(base+'recursos/index.html','utf8').includes('candidateList'),'Library separates public candidate review list from curated references');
assert(libraryPolicy.targets.phase_1===500&&libraryPolicy.targets.long_term===10000,'Library growth targets are explicit');
assert(libraryPolicy.review_policy.auto_approve_for_scientific_core===false&&libraryPolicy.review_policy.required_status==='PENDING_EDITORIAL_REVIEW','Automatic library discovery cannot promote unreviewed evidence to Core');
assert(library.length>=23&&new Set(library.map(x=>x.url)).size===library.length,'Library contains 23+ unique external research references');
assert(library.filter(x=>x.category==='Patrimonio 3D').length>=4&&library.some(x=>x.url.includes('1988_num_21_1_1324')),'Library links museum 3D collections and original Pech-Maho edition');
assert(readFileSync(base+'recursos/index.html','utf8').includes('resourceCount'),'Library shows searchable reference totals');
const registry3d=json('data/epigraphic-3d-registry-v1.json');
const external3d=json('data/real_3d_resources.json');
assert(external3d.length>=6&&external3d.every(x=>x.display_policy==='LINK_TO_ORIGINAL'&&x.local_file_hosted===false&&x.reuse_permission_verified_for_iberos===false),'External 3D resources link to legitimate origin without unverified local redistribution');
assert(external3d.length>=9&&external3d.filter(x=>x.inscription_category==='IBERIAN_INSCRIPTION_REPORTED').length>=2,'3D catalog includes at least two reported Iberian inscriptions');
assert(external3d.length>=11&&external3d.filter(x=>x.inventory_number?.startsWith('MAC ')).length>=2,'Museum photogrammetry links preserve exact published inventory numbers');
assert(external3d.filter(x=>x.atlas_provenance).length>=3&&external3d.filter(x=>x.atlas_provenance).every(x=>x.atlas_provenance.atlas_node_verified===false&&x.atlas_provenance.atlas_query),'3D provenance links cannot imply unverified geographic nodes');
assert(readFileSync(base+'modelos3d/index.html','utf8').includes('atlas/?q='),'3D catalog exposes Atlas lookup for documented provenance');
assert(external3d.filter(x=>x.inscription_category==='IBERIAN_INSCRIPTION_REPORTED').every(x=>x.catalog_crosswalk_status==='NOT_MATCHED_TO_IBEROS_38'&&x.authentic_inscription_visible_verified===false),'Reported inscriptions are not falsely linked to existing Core corpus records');
assert(external3d.some(x=>x.inscription_category==='SOUTHWEST_SCRIPT_NOT_IBERIAN_LANGUAGE'),'Southwest-script comparisons remain distinct from Iberian-language inscriptions');
assert(registry3d.objects.length>=2&&registry3d.objects.every(x=>x.model_status==='SOURCE_REQUIRED'&&x.inscription_from_object_verified===false&&!x.model_url),'3D originals remain explicitly unverified until real inscription models exist');
assert(registry3d.objects.every(x=>Array.isArray(x.research_leads)&&x.research_leads.length>=1&&x.research_leads.every(y=>y.verified_3d_model===false)),'Documentary leads are not misrepresented as verified 3D files');
assert(registry3d.objects.every(x=>x.institutional_contact&&x.institutional_contact.custody_status==='NOT_CONFIRMED_FOR_THIS_EXACT_OBJECT'&&x.acquisition_status==='CONTACT_PREPARED_NOT_SENT'&&x.files_received===false),'Contacts documented without inventing custody, requests or actual 3D files');
assert(registry3d.policy.public_authentic_3d_requires.includes('inscription_from_object_verified')&&readFileSync(base+'modelos3d/index.html','utf8').includes('epigraphic-3d-registry-v1.json'),'3D site requires exact real inscription and reads provenance gate');
const projects=json('data/projects-news-v1.json');
const projectsPage=readFileSync(base+'proyectos/index.html','utf8');
const navigation=readFileSync(base+'assets/portal-data.js','utf8');
assert(projects.projects.some(p=>p.id==='la-picola-reconstruction'&&p.status==='IN_PROGRESS'),'La Picola remains an in-progress reconstruction despite a published progress update');
assert(projects.news.every(n=>n.public_news_approved!==true||(n.editorial_approval===true&&n.source_verification===true&&n.media_rights_verification===true))&&projectsPage.includes('editorial_approval')&&projectsPage.includes('media_rights_verification'),'Published News requires editorial, source and reuse rights approval');
assert(navigation.includes('proyectos/')&&readFileSync(base+'mapa-web/index.html','utf8').includes('../proyectos/'),'Projects and News linked from navigation and full menu');

assert(statusPage.includes('deployment-version.json')&&statusPage.includes('release-version'),'Status dashboard exposes verifiable public deployment version');
const web=readFileSync(base+'webengine/index.html','utf8');
const rules=json('data/core_rule_catalog_v1.json');
assert(rules.counts.documented_entries===rules.entries.length,'Inventario de reglas generado desde Core Python');
assert(rules.counts.verified_translation_rules===0&&rules.entries.every(x=>x.semantic_translation_verified===false),'Las reglas exploratorias no se publican como traducción validada');
assert(web.includes('core_rule_catalog_v1.json')&&web.includes('core-rule-audit'),'Motor web consume catálogo de reglas científico');
assert(ficha.includes('core_object_audit_v1.json')&&ficha.includes('payload.objects'),'La ficha incorpora auditoría del Core Python');
assert(ficha.includes('../webengine/?q=')&&ficha.includes('../laboratorio/?id='),'Ficha enlaza al Core web y Laboratorio');
assert(web.includes('../laboratorio/?id=')&&lab.includes('URLSearchParams'),'Core web pasa el identificador al Laboratorio');
const nodes=json('data/geo_atlas_nodes.json');
assert(Array.isArray(nodes)&&nodes.length>0&&nodes.every(n=>Number.isFinite(n.lat)&&Number.isFinite(n.lon)&&n.precision),'GEO mantiene nodos reales con precisión declarada');
assert(atlas.includes('geo_atlas_nodes.json')&&ficha.includes('../atlas/'),'Fichas y Atlas utilizan rutas de geografía enlazadas');
const tivissa=engine.getObject('IBR-PLM-0002');
assert(tivissa&&nodes.some(n=>n.query==='Tivissa'),'Tivissa presente en Core y nodo GEO de referencia');
const graphics=json('data/epigraphic-visual-registry-v1.json');
assert(graphics.records.some(x=>x.object_id==='IBR-PLM-0002'),'Registro visual de Tivissa presente');
assert(graphics.records.every(x=>ids.has(x.object_id)&&(!x.rights_verified||x.exact_object_match_verified)),'Evidencia gráfica refiere a piezas del Core');
assert(ficha.includes('epigraphic-visual-registry-v1.json'),'Fichas consumen registro de evidencias gráficas');
assert(graphics.policy.watermark_and_attribution?.publish_requires.length===3,'Política de autoría y marcas de agua registrada');
assert(graphics.records.every(x=>x.image_reuse_permission_verified===false&&x.image_author_credit_verified===false&&x.watermark_preserved_verified===false),'Material sin permisos no se habilita para reproducción');
assert(ficha.includes('item.watermark_preserved_verified===true')&&ficha.includes('item.image_reuse_permission_verified===true'),'Visor impide reproducir imágenes sin permiso y conservación de marca de agua');
console.log('Integración IberOS: Core científico → motor web → fichas → GEO → laboratorio comprobada a nivel de datos y rutas.');

const candidateFeed=json('data/core_interpretations_v1.json');
assert(candidateFeed.schema==='IberOS-Interpretation-Web/1.0'&&candidateFeed.object_count===38,'Las 38 fichas tienen estado de hipótesis visible');
assert(Object.values(candidateFeed.objects).every(x=>x.translation_validated===false&&x.candidates.every(c=>c.epistemic_layer==='HYPOTHESIS'&&c.meaning_validated===false&&c.reading_verified_independently===false&&c.sources.length>0)),'Hipótesis editoriales con fuente, sin promoción automática');
const featuredEditorial=json('data/ficha-enrichment-featured.json');
const documentedEditorial=featuredEditorial.filter(x=>ids.has(x.OBJECT_ID)&&['hypothesis','limits','evidence'].every(k=>typeof x[k]==='string'&&x[k].trim())&&(typeof x.citation==='string'&&x.citation.trim()||Array.isArray(x.bibliography)&&x.bibliography.some(v=>typeof v==='string'&&v.trim())));
const actualEditorial=Object.entries(candidateFeed.objects).filter(([,record])=>record.candidates.length>0);
assert(documentedEditorial.length>=4&&actualEditorial.length>=documentedEditorial.length&&documentedEditorial.every(x=>candidateFeed.objects[x.OBJECT_ID].candidates.some(c=>c.sources.length>0)),'Todas las fichas editoriales documentadas generan hipótesis trazables sin promoción científica');
assert(ficha.includes('translation-candidates-slot')&&ficha.includes('core_interpretations_v1.json'),'Las fichas muestran panel de posibles interpretaciones');

const editorialQueue=json('data/editorial_readings_review_v1.json');
assert(editorialQueue.schema==='IberOS-Editorial-Readings-Queue/1.0','Cola de lecturas documentales generada');
assert(editorialQueue.records.every(x=>x.eligible_for_core_execution===false&&x.exact_object_match_verified===false),'Las variantes editoriales nunca se hacen pasar por lecturas revisadas');

const sourceChecks=json('data/epigraphic_source_verification_v1.json');
assert(sourceChecks.checks.length===3,'Tres publicaciones tienen metadatos bibliográficos cotejados');
assert(sourceChecks.checks.every(x=>x.bibliographic_metadata_checked===true&&x.transcription_checked_against_edition===false&&x.semantic_analysis_eligible===false),'Metadatos cotejados no promueven lecturas ni semántica');

const publication=json('data/fiche_publication_status_v1.json');
assert(publication.object_count===38&&Object.keys(publication.records).length===38,'Manifest de publicación por pieza completo');
assert(Object.values(publication.records).every(x=>x.translation_validated===false&&x.automatic_core_promotion===false),'Publicación editorial no valida traducciones');
assert(Object.values(publication.records).filter(x=>x.featured_interpretation_available).length>=19,'Al menos diecinueve interpretaciones editoriales documentadas disponibles');
const publishedEditorialIds=Object.entries(publication.records).filter(([,state])=>state.featured_interpretation_available).map(([id])=>id);
assert(publishedEditorialIds.every(id=>candidateFeed.objects[id]&&candidateFeed.objects[id].candidates.length>0),'Cada expediente publicable contiene su candidato editorial en el feed');
assert(publishedEditorialIds.every(id=>candidateFeed.objects[id].candidates.every(c=>Array.isArray(c.sources)&&c.sources.some(source=>typeof source==='string'&&source.trim())&&Array.isArray(c.supporting_observations)&&c.supporting_observations.some(o=>typeof o==='string'&&o.trim())&&Array.isArray(c.objections)&&c.objections.some(o=>typeof o==='string'&&o.trim())&&c.meaning_validated===false&&c.reading_verified_independently===false)),'Cada interpretación pública preserva fuente, observación, objeción y condición no validada');
assert(publishedEditorialIds.every(id=>publication.records[id].translation_validated===false&&publication.records[id].automatic_core_promotion===false),'Ninguna interpretación editorial se promociona automáticamente a significado probado');


const archive=readFileSync(base+'fichas/index.html','utf8');
assert(archive.includes('fiche_publication_status_v1.json')&&archive.includes('pubstate'),'Archivo consulta y filtra por estado de publicación editorial');
assert(archive.includes('Interpretación editorial disponible')&&archive.includes('Interpretación en revisión'),'Archivo distingue interpretaciones publicables y revisión pendiente');
assert(archive.includes('id="editorial-summary"')&&archive.includes('id="editorial-summary-text"'),'Archivo muestra el resumen de cobertura científica');
assert(archive.includes('records.filter(x=>x.publication_status==="PUBLICABLE_EDITORIAL").length')&&archive.includes('records.filter(x=>x.publication_status==="EDITORIAL_REVIEW_REQUIRED").length'),'Resumen calcula estados a partir del manifest sin cifras editoriales inventadas');
assert(archive.includes('0 traducciones semánticas validadas declaradas')&&Object.values(publication.records).every(x=>x.translation_validated===false),'Resumen público no anuncia traducciones semánticas validadas');


assert(Object.values(publication.records).every(x=>Array.isArray(x.pending_documentation)),'Cada ficha enumera documentación editorial pendiente');
assert(archive.includes('pendingEditorial(')&&archive.includes('Documentación pendiente'),'Archivo público presenta requisitos pendientes por pieza');
assert(archive.includes('Abrir cuaderno de investigación para esta pieza')&&archive.includes('encodeURIComponent(id)')&&archive.includes('Requisitos editoriales, no pruebas'),'Cada expediente pendiente conecta a su cuaderno sin elevar requisitos a hechos lingüísticos');
assert(archive.includes('id="documentation-protocol"')&&archive.includes('cotejo de signos con una edición epigráfica')&&archive.includes('No se atribuye un significado sin pruebas'),'Archivo explica protocolo de completar expedientes sin inventar lecturas');

const priority=json('data/fiche_publication_priority_v1.json');
assert(priority.schema==='IberOS-Publication-Priority/1.0','Cola de trabajo editorial exportada');
assert(priority.pending_count===Object.values(publication.records).filter(r=>r.publication_status!=='PUBLICABLE_EDITORIAL').length,'Cola solo incluye fichas con documentación pendiente');
assert(priority.tasks.every(r=>r.automatic_core_promotion===false),'Priorización no implica validación científica');

assert(archive.includes('editorial-priority')&&archive.includes('fiche_publication_priority_v1.json')&&archive.includes('showEditorialPriority()'),'Archivo presenta cola editorial priorizada enlazada a las fichas');

assert(['IBR-CER-0001','IBR-PLM-0005','IBR-PLM-0006'].every(id=>publication.records[id].featured_interpretation_available&&candidateFeed.objects[id].candidates.length>0),'Tres expedientes documentados de fragmentos existentes se añaden sin inventar traducciones');

assert(['IBR-CER-0002','IBR-CER-0003','IBR-CER-0004'].every(id=>publication.records[id].featured_interpretation_available&&candidateFeed.objects[id].candidates.every(c=>c.meaning_validated===false)),'Llíria, Castellet y Joncosa publicados solo como hipótesis editoriales');

assert(publication.records['IBR-COI-0001'].featured_interpretation_available&&candidateFeed.objects['IBR-COI-0001'].candidates.some(x=>x.meaning_validated===false&&x.sources.some(s=>s.includes('palaeohispanica.v0i16.29'))),'Coimbra kaŕb incorpora cita editorial sin validación automática');

assert(publication.records['IBR-LAP-0001'].featured_interpretation_available&&candidateFeed.objects['IBR-LAP-0001'].candidates.some(c=>c.sources.some(x=>x.includes('palaeohispanica.v0i9.243'))&&!c.meaning_validated),'El árula C.18.7 incluye fuente precisa sin validación semántica');

assert(['IBR-LAP-0002','IBR-LAP-0003','IBR-LAP-0004'].every(id=>publication.records[id].featured_interpretation_available&&candidateFeed.objects[id].candidates.some(c=>c.sources.length>0&&c.meaning_validated===false)),'La Vispesa Sinarcas y Santa Perpetua tienen atribución y siguen como hipótesis');

assert(['IBR-MON-0001','IBR-OBJ-0001'].every(id=>publication.records[id].featured_interpretation_available&&candidateFeed.objects[id].candidates.some(c=>c.sources.length>0&&c.meaning_validated===false)),'Moneda erder y tortera Can Rodon conservan fuentes e incertidumbre');

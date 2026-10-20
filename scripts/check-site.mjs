import {readFileSync,existsSync} from 'node:fs';
import {execFileSync} from 'node:child_process';
const base='site/';
const paths=['index.html','corpus/index.html','fichas/index.html','ficha/index.html','atlas/index.html','laboratorio/index.html','webengine/index.html','write/index.html','talk/index.html','modelos3d/index.html','estado/index.html','mapa-web/index.html','data/objects.csv','data/families.csv','data/iberos-result-v1.schema.json','models/inscribed-placa.gltf','models/inscribed-estela.gltf'];
let errors=0, checks=0;
const assert=(ok,msg)=>{checks++;console.log((ok?'✓ ':'✕ ')+msg);if(!ok)errors++};
for(const p of paths)assert(existsSync(base+p),'Recurso '+p);
const html=paths.filter(p=>p.endsWith('.html'));
for(const p of html){if(!existsSync(base+p))continue;const t=readFileSync(base+p,'utf8');assert(/<html\b/i.test(t)&&/<\/html>/i.test(t),'HTML válido básico '+p);const scripts=[...t.matchAll(/<script\b([^>]*)>([\s\S]*?)<\/script>/gi)];
for(const [i,m] of scripts.entries()){if(!m[2].trim())continue;if(/\bapplication\/ld\+json\b/i.test(m[1])){try{JSON.parse(m[2]);assert(true,'JSON-LD '+p+' #'+(i+1))}catch(e){assert(false,'JSON-LD inválido '+p+' #'+(i+1))}continue}try{const code=m[2];const tmp='/tmp/iberos-check-'+process.pid+'-'+i+(m[1].includes('module')?'.mjs':'.js');const {writeFileSync,unlinkSync}=await import('node:fs');writeFileSync(tmp,code);execFileSync(process.execPath,['--check',tmp],{stdio:'pipe'});unlinkSync(tmp);assert(true,'JavaScript '+p+' #'+(i+1))}catch(e){assert(false,'JavaScript '+p+' #'+(i+1)+' '+String(e.stderr||e.message).slice(0,180))}}}
for(const p of ['data/objects.csv','data/families.csv'])if(existsSync(base+p)){const text=readFileSync(base+p,'utf8');assert(text.includes('OBJECT_ID')&&text.trim().split(/\r?\n/).length>35,'CSV no vacío '+p)}
for(const p of ['data/iberos-result-v1.schema.json','data/real_3d_resources.json','models/inscribed-placa.gltf','models/inscribed-estela.gltf'])if(existsSync(base+p)){try{JSON.parse(readFileSync(base+p,'utf8'));assert(true,'JSON legible '+p)}catch(e){assert(false,'JSON inválido '+p)}}


/* Search discovery: make every submitted sitemap URL correspond to a real static page. */
if(existsSync(base+'sitemap.xml')){
 const xml=readFileSync(base+'sitemap.xml','utf8');
 const baseUrl='https://estebanmolinaruiz-art.github.io/IberOS/';
 const locations=[...xml.matchAll(/<loc>([^<]+)<\/loc>/g)].map(m=>m[1].trim());
 assert(xml.includes('xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"'),'Sitemap usa namespace estándar');
 assert(locations.length>=14 && new Set(locations).size===locations.length,'Sitemap contiene 14+ URL únicas');
 for(const url of locations){
  let ok=false;
  try{
   const u=new URL(url);
   const rel=u.href.startsWith(baseUrl) ? decodeURIComponent(u.pathname.slice('/IberOS/'.length)) : null;
   ok=rel!==null && !u.search && !u.hash && existsSync(base+rel+(rel.endsWith('/')||rel===''?'':'/')+'index.html');
  }catch{}
  assert(ok,'Sitemap enlaza a página estática publicada: '+url);
 }
 const robots=existsSync(base+'robots.txt')?readFileSync(base+'robots.txt','utf8'):'';
 assert(robots.includes('Sitemap: '+baseUrl+'sitemap.xml'),'robots.txt referencia el sitemap publicado');
}


import {readdirSync,statSync} from 'node:fs';
import {join,relative,dirname,resolve} from 'node:path';
function walk(dir){return readdirSync(dir).flatMap(name=>{const p=join(dir,name);return statSync(p).isDirectory()?walk(p):[p]})}
const all=walk(base);
for(const file of all.filter(p=>/\.(mjs|js)$/.test(p))){try{execFileSync(process.execPath,['--check',file],{stdio:'pipe'});assert(true,'Módulo JS '+relative(base,file))}catch(e){assert(false,'Módulo JS '+relative(base,file)+' '+String(e.stderr||e.message).slice(0,150))}}
for(const file of all.filter(p=>/\.html$/.test(p))){
 const source=readFileSync(file,'utf8');
 for(const m of source.matchAll(/(?:src|href)\s*=\s*["'](\.\.?\/[^"'?#]+)[^"']*["']/g)){
  const asset=resolve(dirname(file),decodeURIComponent(m[1]));
  assert(existsSync(asset),'Ruta local '+relative(base,file)+' → '+m[1]);
 }
}


const scientificPaths=['data/scientific-review-queue-v1.json','data/ficha-enrichment-3.json','diagnostico/index.html'];
for(const p of scientificPaths)assert(existsSync(base+p),'Recurso científico/diagnóstico '+p);
if(scientificPaths.slice(0,2).every(p=>existsSync(base+p))){
 try{
  const queue=JSON.parse(readFileSync(base+scientificPaths[0],'utf8'));
  const enrich=JSON.parse(readFileSync(base+scientificPaths[1],'utf8'));
  for(const id of ['IBR-PLM-0002','IBR-PLM-0003']){
   const record=queue.records?.find(r=>r.object_id===id);
   const fiche=enrich.find(r=>r.OBJECT_ID===id);
   assert(!!record&&!!fiche&&!!fiche.hypothesis&&!!fiche.limits,'Expediente y análisis existentes '+id);
   assert(record?.publication_approved===false&&Array.isArray(record?.reconstruction_segments)&&record.reconstruction_segments.length===0,'Sin promoción científica automática '+id);
   assert(record?.variant_review?.variants?.length>0,'Variantes documentadas '+id);
  }
 }catch(error){assert(false,'Lectura científica '+error.message)}
}
if(existsSync(base+'ficha/index.html')){
 const source=readFileSync(base+'ficha/index.html','utf8');
 assert(source.includes('loadVariantReview()')&&source.includes('scientific-review-queue-v1.json'),'Ficha conectada a variantes');
 assert(source.includes('publication_approved===true'),'Ficha exige autorización científica');
}

console.log('\n'+(checks-errors)+'/'+checks+' controles correctos');if(errors)process.exitCode=1;

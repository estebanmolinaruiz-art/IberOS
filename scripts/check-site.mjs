import {readFileSync,existsSync} from 'node:fs';
import {execFileSync} from 'node:child_process';
const base='site/';
const paths=['index.html','corpus/index.html','fichas/index.html','ficha/index.html','atlas/index.html','laboratorio/index.html','webengine/index.html','write/index.html','talk/index.html','modelos3d/index.html','estado/index.html','data/objects.csv','data/families.csv','data/iberos-result-v1.schema.json','models/inscribed-placa.gltf','models/inscribed-estela.gltf'];
let errors=0, checks=0;
const assert=(ok,msg)=>{checks++;console.log((ok?'✓ ':'✕ ')+msg);if(!ok)errors++};
for(const p of paths)assert(existsSync(base+p),'Recurso '+p);
const html=paths.filter(p=>p.endsWith('.html'));
for(const p of html){if(!existsSync(base+p))continue;const t=readFileSync(base+p,'utf8');assert(/<html\b/i.test(t)&&/<\/html>/i.test(t),'HTML válido básico '+p);const scripts=[...t.matchAll(/<script\b([^>]*)>([\s\S]*?)<\/script>/gi)];
for(const [i,m] of scripts.entries()){if(!m[2].trim())continue;try{const code=m[2];const tmp='/tmp/iberos-check-'+process.pid+'-'+i+(m[1].includes('module')?'.mjs':'.js');const {writeFileSync,unlinkSync}=await import('node:fs');writeFileSync(tmp,code);execFileSync(process.execPath,['--check',tmp],{stdio:'pipe'});unlinkSync(tmp);assert(true,'JavaScript '+p+' #'+(i+1))}catch(e){assert(false,'JavaScript '+p+' #'+(i+1)+' '+String(e.stderr||e.message).slice(0,180))}}}
for(const p of ['data/objects.csv','data/families.csv'])if(existsSync(base+p)){const text=readFileSync(base+p,'utf8');assert(text.includes('OBJECT_ID')&&text.trim().split(/\r?\n/).length>35,'CSV no vacío '+p)}
for(const p of ['data/iberos-result-v1.schema.json','data/real_3d_resources.json','models/inscribed-placa.gltf','models/inscribed-estela.gltf'])if(existsSync(base+p)){try{JSON.parse(readFileSync(base+p,'utf8'));assert(true,'JSON legible '+p)}catch(e){assert(false,'JSON inválido '+p)}}
console.log('\n'+(checks-errors)+'/'+checks+' controles correctos');if(errors)process.exitCode=1;

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

import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {renderEvidencePassport} from '../site/assets/scientific-evidence-passport.mjs';
const load=path=>JSON.parse(readFileSync(path,'utf8'));

test('All 38 catalogue review records have no fictional scientific approval',()=>{
 const q=load('site/data/scientific-review-queue-v1.json');
 const v=load('site/data/epigraphic-visual-registry-v1.json');
 assert.equal(q.records.length,38);
 assert.equal(new Set(q.records.map(x=>x.object_id)).size,38);
 for(const r of q.records){
  const visual=v.records.find(x=>x.object_id===r.object_id);
  const html=renderEvidencePassport(r,visual,r.object_id);
  assert.match(html,/Pasaporte de evidencia/);
  assert.match(html,/Traducción semántica/);
  assert.match(html,/no validada prospectivamente/);
  assert.match(html,/Qué falta para la validación/);
  assert.match(html,/evidencia\/"/);
  assert(!html.includes('undefined')&&!html.includes('null</'));
 }
});

test('A missing visual record never implies independently verified signs',()=>{
 const q=load('site/data/scientific-review-queue-v1.json').records[0];
 const s=renderEvidencePassport(q,null,q.object_id);
 assert.match(s,/sin verificación gráfica independiente consignada/);
 assert.match(s,/No consta expediente gráfico individual/);
});
test('Untrusted citations are escaped and unsafe URLs suppressed',()=>{
 const s=renderEvidencePassport({references_checked:[{citation:'<img src=x onerror=alert(1)>',url:'javascript:alert(1)',status:'<bad>'}],technical_audit:{blockers:['<script>']},scientific_state:'<unsafe>'},null,'<X>');
 assert(!s.includes('<img')&&!s.includes('<script>')&&!s.includes('href="javascript'));
 assert(s.includes('&lt;img')&&s.includes('&lt;script&gt;')&&s.includes('&lt;unsafe&gt;'));
});
test('Live ficha includes the evidence passport and safe fallback',()=>{
 const s=readFileSync('site/ficha/index.html','utf8');
 assert(s.includes('evidence-passport-slot'));
 assert(s.includes('renderEvidencePassport('));
 assert(s.includes('No se ha podido cargar el pasaporte'));
});

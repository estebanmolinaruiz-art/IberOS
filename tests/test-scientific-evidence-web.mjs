import {readFileSync,existsSync} from 'node:fs';
import {strict as assert} from 'node:assert';
import test from 'node:test';

const read=p=>readFileSync(p,'utf8');
const p='site/evidencia/index.html';

test('Public page has scientific scope, canonical and dated snapshot',()=>{
 assert(existsSync(p));
 const s=read(p);
 for(const token of ['12 de noviembre de 2026','38','26','cinco objetos físicos','0','Traducciones validadas','no validado','SCI-PRED-01/02'])
  assert(s.includes(token),'Missing scientific qualification: '+token);
 assert(s.includes('href="../reproducibilidad/"'));
 assert(s.includes('href="../corpus/"'));
 assert(s.includes('rel="canonical"'));
 assert(s.includes('coste')||s.includes('Coste'));
});

test('Scientific page documents contamination prevention and blind controls',()=>{
 const s=read(p);
 for(const token of ['TRAIN y HOLD','hipótesis','a ciegas','abstenciones','independientes','hash por sí solo','no es'])
  assert(s.toLowerCase().includes(token.toLowerCase()),'Missing falsification control: '+token);
 for(const token of ['/IberOS/issues/149','/IberOS/issues/150','/IberOS/issues/151','/IberOS/issues/155','/IberOS/pull/152'])
  assert(s.includes(token),'Missing auditable issue: '+token);
});

test('Scientific status page is discoverable from index, navigation and sitemap',()=>{
 const sitemap=read('site/sitemap.xml');
 assert(sitemap.includes('https://estebanmolinaruiz-art.github.io/IberOS/evidencia/'));
 for(const entry of ['site/reproducibilidad/index.html','site/publicaciones/index.html','site/mapa-web/index.html','site/fichas/index.html'])
  assert(read(entry).includes('../evidencia/'),entry+' lacks evidence link');
});

test('No authority layer, Core metrics or corpus files are modified by this test',()=>{
 // This test reads the published view only; it deliberately cannot mutate the scientific Core.
 const page=read(p);
 assert(page.includes('0</strong><h3>Traducciones validadas'));
 assert(page.includes('38</strong><h3>Registros y controles'));
 assert(page.includes('26</strong><h3>Unidades de cotejo'));
});

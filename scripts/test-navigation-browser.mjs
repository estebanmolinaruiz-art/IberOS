import { chromium } from 'playwright';

const base='http://127.0.0.1:8765';
const browser=await chromium.launch({headless:true});
const page=await browser.newPage();
const errors=[];
const checks=[
  ['/corpus/?q=Tivissa','Corpus',/\/ficha\/\?id=IBR-PLM-0002/],
  ['/ficha/?id=IBR-PLM-0002','Ficha',/\.\.\/webengine\/\?q=/],
  ['/webengine/?q=IBR-PLM-0002','CORE',/\.\.\/laboratorio\/\?id=/],
  ['/laboratorio/?id=IBR-PLM-0002','Laboratorio',/IBR-PLM-0002/]
];
try{
 for(const [path,label,expected] of checks){
  const response=await page.goto(base+path,{waitUntil:'domcontentloaded',timeout:20000});
  if(!response || response.status()!==200)throw Error(label+' HTTP '+(response?.status()??'sin respuesta'));
  await page.waitForTimeout(1000);
  const html=await page.content();
  if(!expected.test(html))throw Error(label+' carece de enlace o identificador esperado');
  console.log('✓ '+label+' disponible con contexto de Tivissa');
 }
 const publicModules=['/','/que-es-iberos/','/corpus/','/atlas/','/fichas/','/ficha/?id=IBR-PLM-0002','/laboratorio/','/webengine/','/write/','/talk/','/modelos3d/','/recursos/','/bibliografia/','/proyectos/','/casos/','/yacimientos/','/reproducibilidad/','/herramientas/','/comunidad/','/acerca/','/contactar/','/demostracion/','/diagnostico/','/estado/','/ecosistema/','/mapa-web/','/presentacion/'];
 for(const path of publicModules){
  const response=await page.goto(base+path,{waitUntil:'domcontentloaded',timeout:20000});
  if(!response||response.status()!==200)throw Error('Módulo '+path+' HTTP '+(response?.status()??'sin respuesta'));
  const title=await page.title();
  if(!title.trim())throw Error('Módulo '+path+' no tiene título');
  const visibleTechnical=await page.locator('pre').evaluateAll(nodes=>nodes.filter(el=>{const rect=el.getBoundingClientRect();const style=getComputedStyle(el);return rect.width>0&&rect.height>0&&style.display!=='none'&&style.visibility!=='hidden'&&el.closest('details:not([open])')===null&&/^\\s*[\\[{]\\s*["{]/.test(el.textContent||'')}).length);
  if(visibleTechnical)throw Error('Módulo '+path+' muestra JSON técnico visible en lugar de resultado legible');
  console.log('✓ Módulo '+path+' abre correctamente y no muestra JSON crudo como resultado principal');
 }
 await page.goto(base+'/modelos3d/',{waitUntil:'domcontentloaded'});
 await page.locator('#external3d a[href^="https://"]').first().waitFor({state:'visible',timeout:15000});
 const sourceLinks=await page.locator('#external3d a[href^="https://"]').count();
 if(sourceLinks<6)throw Error('Arqueología 3D: menos de seis enlaces a recursos originales');
 const demo=page.locator('details:has(.viewer-shell)');
 if(await demo.count()!==1||await demo.getAttribute('open')!==null)throw Error('Modelos 3D de muestra no están separados y plegados');
 console.log('✓ 3D: '+sourceLinks+' enlaces a modelos originales, demos ocultas');
 await page.goto(base+'/write/',{waitUntil:'domcontentloaded'});
 await page.locator('#write-readable strong').waitFor({state:'visible',timeout:15000});
 if(!((await page.locator('#write-readable').innerText()).includes('Reconstrucción')))throw Error('Write no explica el resultado');
 if(await page.locator('#out').isVisible())throw Error('Write muestra JSON crudo');
 console.log('✓ Write: explicación visible, JSON técnico plegado');
 // Validate every visible local navigation target resolves to a real page or asset.
 const seen=new Set();
 for(const path of publicModules){
  await page.goto(base+path,{waitUntil:'domcontentloaded'});
  const links=await page.locator('a[href]').evaluateAll(nodes=>nodes.map(a=>({href:a.getAttribute('href'),label:(a.getAttribute('aria-label')||a.textContent||'').trim()})));
  for(const link of links){
   if(!link.href||link.href.startsWith('#')||/^(mailto:|tel:|javascript:)/i.test(link.href))continue;
   const url=new URL(link.href,base+path);
   if(url.origin!==new URL(base).origin)continue;
   const key=url.pathname;
   if(seen.has(key))continue;seen.add(key);
   const response=await page.request.get(url.toString(),{timeout:15000,maxRedirects:5});
   if(response.status()>=400)throw Error('Enlace interno roto: '+path+' → '+link.href+' ('+response.status()+')');
  }
 }
 console.log('✓ '+seen.size+' destinos internos de navegación accesibles');
 // Check critical data-driven sections are populated, not merely that HTML exists.
 const populated=[
  ['/corpus/','.result-card',1,'Corpus'],
  ['/fichas/','a[href*="../ficha/"]',1,'Fichas'],
  ['/modelos3d/','#external3d a[href^="https://"]',6,'Modelos 3D originales'],
  ['/recursos/','#externalResources .resource-card',1,'Biblioteca'],
  ['/proyectos/','#project-list article, #news-list article',1,'Proyectos']
 ];
 for(const [path,selector,min,label] of populated){
  await page.goto(base+path,{waitUntil:'domcontentloaded'});
  try{await page.locator(selector).first().waitFor({state:'attached',timeout:12000})}catch{throw Error(label+' no presenta el contenido esperado ('+selector+')')}
  const n=await page.locator(selector).count();if(n<min)throw Error(label+' contenido insuficiente: '+n);
  console.log('✓ '+label+': '+n+' elementos cargados');
 }
 const ficheResponse=await page.goto(base+'/ficha/?id=IBR-PLM-0002',{waitUntil:'domcontentloaded'});
 if(!ficheResponse || ficheResponse.status()!==200)throw Error('Ficha Tivissa no disponible');
 await page.locator('#interpretationMain').waitFor({state:'visible',timeout:15000});
 const mainText=await page.locator('#interpretationMain').innerText();
 if(!mainText.trim())throw Error('Ficha sin contenido visible en el panel principal de interpretación');
 const caveat=await page.locator('.ib-reconstruction').innerText();
 if(!caveat.includes('no una traducción confirmada'))
  throw Error('Ficha no informa de los límites científicos de la interpretación');
 const note=await page.locator('#interpretationNote').innerText();
 if(!note.trim())throw Error('Ficha no presenta información sobre el estado de la lectura');
 const trace=await page.locator('#interpretationTrace').innerText();
 if(!trace.trim())throw Error('Ficha no informa de la procedencia documental o de su ausencia');
 console.log('✓ Ficha presenta interpretación visible con cautelas de validación científica');
 const corpus=await page.goto(base+'/corpus/?q=Tivissa',{waitUntil:'domcontentloaded'});
 await page.waitForTimeout(1000);
 if(await page.locator('a[href*="../ficha/?id=IBR-PLM-0002"]').count()===0)throw Error('Corpus no muestra acceso a ficha de Tivissa');
 console.log('✓ Corpus enlaza a la ficha desde resultados reales');
}catch(error){errors.push(error.message);await page.screenshot({path:'/tmp/iberos-navigation-fallo.png',fullPage:true}).catch(()=>{});}
finally{await browser.close();}
if(errors.length){console.error(errors.join('\n'));process.exit(1);}
console.log('Recorrido Corpus → Ficha → CORE → Laboratorio: PASS');

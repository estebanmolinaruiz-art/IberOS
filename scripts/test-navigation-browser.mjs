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
 // Home page regression: keep the project news card, never restore the external stone plaque.
 await page.goto(base+'/',{waitUntil:'domcontentloaded'});
 if(await page.locator('.ib-news-rock').count()!==0)throw Error('Portada escritorio: placa News duplicada');
 const inPageNews=page.locator('.flyer-frame .ib-project-feature');
 if(await inPageNews.count()!==1)throw Error('Portada escritorio: panel Nuevos Proyectos ausente o duplicado');
 const newsTarget=await inPageNews.locator('a[aria-label="Abrir News"]').getAttribute('href');
 if(newsTarget!=='proyectos/')throw Error('Portada: el enlace NEWS no lleva a Proyectos');
 console.log('✓ Portada escritorio: un solo panel News interior, sin piedra exterior y con enlace correcto');
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
 // Regression audit for duplicated editorial cards and leaked technical content.
 const pageStructures=[
  ['/herramientas/','.portal-grid > .portal-card',4,'Herramientas'],
  ['/contactar/','.contact-grid > .contact-card',4,'Contacto'],
  ['/publicaciones/','.resource-shelf > .resource-card',2,'Publicaciones'],
  ['/','.flyer-frame > .ib-project-feature',1,'News interior']
 ];
 for(const [path,selector,expected,label] of pageStructures){
  await page.goto(base+path,{waitUntil:'domcontentloaded'});
  const cards=page.locator(selector);
  const count=await cards.count();
  if(count!==expected)throw Error(label+': '+count+' tarjetas en lugar de '+expected+' (posible duplicación o desaparición)');
  const signatures=await cards.evaluateAll(nodes=>nodes.map(n=>(n.querySelector('h2,h3')?.textContent||n.getAttribute('aria-label')||n.textContent||'').trim().replace(/\s+/g,' ').slice(0,160)));
  if(new Set(signatures).size!==signatures.length)throw Error(label+': tarjetas con títulos repetidos');
  console.log('✓ '+label+': '+count+' tarjetas únicas');
 }
 for(const path of publicModules){
  await page.goto(base+path,{waitUntil:'domcontentloaded'});
  const leaked=await page.locator('body').evaluate(body=>{
   const walker=document.createTreeWalker(body,NodeFilter.SHOW_TEXT);
   let node;
   while((node=walker.nextNode())){
    const parent=node.parentElement;
    if(!parent||parent.closest('script,style,template,noscript,pre,code,details:not([open]),[hidden],[aria-hidden="true"]'))continue;
    const st=getComputedStyle(parent);
    if(st.display==='none'||st.visibility==='hidden')continue;
    const t=node.textContent.trim();
    if(t==='[object Object]'||/^Traceback \(most recent call last\):/.test(t)||/^SyntaxError: Unexpected token/.test(t))return t.slice(0,120);
   }
   return '';
  });
  if(leaked)throw Error('Código/error visible en '+path+': '+leaked);
 }
 console.log('✓ 27 módulos sin errores de código bruto evidentes en texto visible');
 await page.goto(base+'/modelos3d/',{waitUntil:'domcontentloaded'});
 await page.locator('#external3d a[href^="https://"]').first().waitFor({state:'visible',timeout:15000});
 const sourceLinks=await page.locator('#external3d a[href^="https://"]').count();
 if(sourceLinks<6)throw Error('Arqueología 3D: menos de seis enlaces a recursos originales');
 if(await page.locator('.viewer-shell').count()!==0)throw Error('3D: todavía presenta visor simbólico no acreditado');
 await page.locator('#epigraphic3d article').first().waitFor({state:'attached',timeout:15000});
 console.log('✓ 3D: '+sourceLinks+' enlaces originales, sin modelos de muestra; registro epigráfico presente');
 await page.goto(base+'/write/',{waitUntil:'domcontentloaded'});
 await page.locator('#q').fill('A Bastubar se transfiere un documento.');
 await page.locator('#go').click();
 await page.locator('#write-readable strong').waitFor({state:'visible',timeout:15000});
 if(!((await page.locator('#write-feedback').innerText()).includes('Patrón compatible')))throw Error('Write no confirma la entrada procesada');
 await page.locator('#q').fill('Esteban vende hierro');
 await page.locator('#go').click();
 if(!((await page.locator('#write-feedback').innerText()).includes('FALLBACK FONOGRÁFICO MODERNO')))throw Error('Write no distingue abstención semántica de salida gráfica');
 if((await page.locator('#write-stone-text').innerText()).includes('Sin signos'))throw Error('Write no muestra inscripción para entrada no reconocida');
 if(!(/reconstrucción/i.test(await page.locator('#write-readable').innerText())))throw Error('Write no explica el resultado');
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
 const guide=await page.locator('.ib-ficha-guide').innerText();
 if(!guide.includes('Cómo leer este expediente científico')||!guide.includes('Fuentes y reproducibilidad')||!guide.includes('Regla de fiabilidad'))
  throw Error('Ficha sin guía clara para diferenciar lectura, hipótesis, fuentes y validación');
 console.log('✓ Ficha presenta guía de interpretación rigurosa');
 const identification=await page.locator('.artifact-summary').innerText();
 if(!identification.includes('Alcance de la ficha')||!identification.includes('Control de entradas'))throw Error('Ficha no explica el alcance de validación paleográfica y de entradas');
 if(!identification.includes('Estado editorial del registro')||!identification.includes('Estado paleográfico')||!identification.includes('Fuente registrada'))throw Error('Ficha sin estado editorial/paleográfico o enlace documental en la identificación');
 await page.locator('#independent-review-slot h2').waitFor({state:'visible',timeout:15000});const scientificReview=await page.locator('#independent-review-slot').innerText();if(!scientificReview.includes('Ediciones y referencias')||!scientificReview.includes('Verificaciones necesarias'))throw Error('Tivissa: expediente de fuentes y pendientes no visible');
 const note=await page.locator('#interpretationNote').innerText();
 if(!note.trim())throw Error('Ficha no presenta información sobre el estado de la lectura');
 const trace=await page.locator('#interpretationTrace').innerText();
 if(!trace.trim())throw Error('Ficha no informa de la procedencia documental o de su ausencia');
 console.log('✓ Ficha presenta interpretación visible con cautelas de validación científica');
 const corpus=await page.goto(base+'/corpus/?q=Tivissa',{waitUntil:'domcontentloaded'});
 await page.waitForTimeout(1000);
 if(await page.locator('a[href*="../ficha/?id=IBR-PLM-0002"]').count()===0)throw Error('Corpus no muestra acceso a ficha de Tivissa');
 console.log('✓ Corpus enlaza a la ficha desde resultados reales');
 // Regression: original flyer titles must be tappable on an iPhone-sized viewport.
 const mobile=await browser.newPage({viewport:{width:390,height:844},deviceScaleFactor:3,isMobile:true,hasTouch:true});
 try{
  for(const [selector,expected] of [
   ['.tile-hotspot[aria-label="Abrir Corpus"]','/corpus/'],
   ['.tile-hotspot[aria-label="Abrir Atlas"]','/atlas/'],
   ['.tile-hotspot[aria-label="Abrir Fichas"]','/fichas/'],
   ['.tile-hotspot[aria-label="Abrir Laboratorio"]','/laboratorio/'],
   ['.tile-hotspot[aria-label="Abrir Arqueología 3D"]','/modelos3d/'],
   ['.tile-hotspot[aria-label="Abrir Recursos"]','/recursos/'],
   ['.tile-hotspot[aria-label="Abrir Casos de estudio"]','/casos/'],
   ['.tile-hotspot[aria-label="Abrir Comunidad"]','/comunidad/'],
   ['.nav-hotspot[aria-label="Inicio"]','/'],
   ['.nav-hotspot[aria-label="Corpus"]','/corpus/'],
   ['.nav-hotspot[aria-label="Herramientas"]','/herramientas/'],
   ['.nav-hotspot[aria-label="Comunidad"]','/comunidad/'],
   ['.nav-hotspot[aria-label="Recursos"]','/recursos/'],
   ['.nav-hotspot[aria-label="Acerca de"]','/acerca/']
  ]){
   await mobile.goto(base+'/',{waitUntil:'domcontentloaded'});
   const duplicate=mobile.locator('.ib-news-rock');
   if(await duplicate.count()!==0)throw Error('News: persiste una placa duplicada fuera de la portada');
   const news=mobile.locator('.flyer-frame .ib-project-feature');
   if(await news.count()!==1)throw Error('News: debe existir un único panel Nuevos Proyectos dentro de la portada');
   const el=mobile.locator(selector);
   await el.scrollIntoViewIfNeeded();
   const box=await el.boundingBox();
   if(!box||box.width<2||box.height<2)throw Error('iPhone: área táctil inexistente '+selector);
   const x=box.x+box.width/2,y=box.y+box.height/2;
   const hit=await mobile.evaluate(({x,y,selector})=>{const link=document.querySelector(selector);const target=document.elementFromPoint(x,y);return !!(link&&target&&(target===link||link.contains(target)))},{x,y,selector});
   if(!hit)throw Error('iPhone: otro elemento intercepta pulsación '+selector);
   await mobile.touchscreen.tap(x,y);
   await mobile.waitForURL('**'+expected,{timeout:10000});
   console.log('✓ iPhone: título original '+selector+' abre '+expected);
  }
 }finally{await mobile.close();}
}catch(error){errors.push(error.message);await page.screenshot({path:'/tmp/iberos-navigation-fallo.png',fullPage:true}).catch(()=>{});}
finally{await browser.close();}
if(errors.length){console.error(errors.join('\n'));process.exit(1);}
console.log('Recorrido Corpus → Ficha → CORE → Laboratorio: PASS');

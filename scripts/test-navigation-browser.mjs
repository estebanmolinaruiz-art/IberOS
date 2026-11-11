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
 const homeTarget=await page.locator('.nav-hotspot[aria-label="Inicio"]').getAttribute('href');
 if(homeTarget!=='./')throw Error('Portada: enlace Inicio incorrecto');
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
 const publicModules=['/cotejo-villares-v/','/formas/','/','/que-es-iberos/','/corpus/','/atlas/','/fichas/','/ficha/?id=IBR-PLM-0002','/laboratorio/','/webengine/','/write/','/talk/','/modelos3d/','/recursos/','/bibliografia/','/proyectos/','/casos/','/yacimientos/','/reproducibilidad/','/herramientas/','/comunidad/','/acerca/','/contactar/','/demostracion/','/diagnostico/','/estado/','/ecosistema/','/mapa-web/','/presentacion/'];
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
 const quick=page.locator('.ib-quick-read');
 await quick.waitFor({state:'visible',timeout:15000});
 const quickText=await quick.innerText();
 if(!quickText.includes('Plomo de Tivissa')||!quickText.includes('Imagen original:')||!quickText.includes('Significado:')||!quickText.includes('no existe traducción literal validada'))throw Error('Ficha sin resumen inicial de pieza, imagen y alcance semántico');
 if(await quick.locator('a[href="#sign-reading-slot"],a[href="#interpretationMain"],a[href="#documentary-slot"]').count()!==3)throw Error('Ficha: faltan accesos rápidos a lectura, hipótesis y fuentes');
 console.log('✓ WEB-05: ficha con lectura rápida, imagen acreditada/pendiente y cautela semántica');
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
 const directCore=page.locator('a[href="../webengine/?q=IBR-PLM-0002"]');
 if(await directCore.count()<1)throw Error('WEB-05: Corpus no ofrece acceso directo al Core para Tivissa');
 const cardStatus=await page.locator('.result-card').first().innerText();
 if(/\b(INCLUDE|CONDITIONAL|CONTROL_ONLY|EXCLUDED_CONTROL)\b/.test(cardStatus))throw Error('WEB-05: código de inclusión visible en tarjeta de Corpus');
 console.log('✓ WEB-05: Corpus enlaza a Core y usa estados legibles');
 console.log('✓ Corpus enlaza a la ficha desde resultados reales');
 // WEB-06: index only editorial variants of a single physical witness.
 await page.goto(base+'/formas/?q=SALIRIG',{waitUntil:'domcontentloaded'});
 await page.locator('.ib-forms-result').first().waitFor({state:'visible',timeout:15000});
 const editorialText=await page.locator('#formResults').innerText();
 const editorialStatus=await page.locator('#formSummary').innerText();
 if(!editorialText.includes('śalirg')||!editorialText.includes('SALIRIG')||!editorialText.includes('Pendiente'))throw Error('WEB-06: falla la consulta de variante histórica documentada');
 if(!editorialStatus.includes('1 cotejo')||!editorialStatus.includes('1 objeto físico'))throw Error('WEB-06: el conteo no distingue cotejos y objetos');
 await page.locator('#formQuery').fill('una-forma-no-documentada');
 if(await page.locator('#formResults .ib-forms-result').count()!==0)throw Error('WEB-06: búsqueda sin coincidencias genera falsas variantes');
 if(!((await page.locator('#formResults').innerText()).includes('No consta esta forma')))throw Error('WEB-06: falta abstención ante forma no documentada');
 console.log('✓ WEB-06: variantes editoriales, fuente, límites y abstención en navegador');

 // WEB-07: no extra objects, explicit distinction between form and formal comparison.
 await page.goto(base+'/formas/?forma=ekiar',{waitUntil:'domcontentloaded'});
 await page.locator('#crossResults .ib-forms-result').first().waitFor({state:'visible',timeout:15000});
 const ekiarSummary=await page.locator('#crossSummary').innerText();
 if(!ekiarSummary.includes('2 objetos')||!ekiarSummary.includes('1 solo en comparación formal'))throw Error('WEB-07: confunde ekiar de Caminreal con comparación formal de Andelo');
 const crossText=await page.locator('#crossResults').innerText();
 if(!crossText.includes('Mosaico de Caminreal')||!crossText.includes('Mosaico de Andelo')||!crossText.includes('no es lectura literal'))throw Error('WEB-07: contexto o cautelas de ekiar insuficientes');
 await page.locator('#crossQuery').fill('śalir');
 if(!((await page.locator('#crossSummary').innerText()).includes('3 objetos')))throw Error('WEB-07: no coteja Tivissa, Villares V y La Serreta');
 if(await page.locator('#crossResults .ib-forms-result').count()!==3)throw Error('WEB-07: recuento físico incorrecto');
 await page.locator('#crossQuery').fill('forma-inexistente-web07');
 if(await page.locator('#crossResults .ib-forms-result').count()!==0)throw Error('WEB-07: resultados falsos para forma no registrada');
 if(!((await page.locator('#crossResults').innerText()).includes('No consta la forma')))throw Error('WEB-07: falta abstención explícita');
 console.log('✓ WEB-07: cinco testimonios documentales, comparaciones formales separadas y abstención');
 // WEB-08: class filter must exclude formal comparisons from editorial attestations.
 await page.locator('#crossQuery').fill('ekiar');
 await page.locator('#crossEvidence').selectOption('EDITORIAL_FORM_UNCOLLATED');
 if(await page.locator('#crossResults .ib-forms-result').count()!==1)throw Error('WEB-08: ekiar lectura editorial debe apuntar solo a Caminreal');
 if(!((await page.locator('#crossResults').innerText()).includes('Mosaico de Caminreal')))throw Error('WEB-08: falta testimonio editorial de Caminreal');
 await page.locator('#crossEvidence').selectOption('FORMAL_COMPARISON_NOT_ATTESTED');
 if(await page.locator('#crossResults .ib-forms-result').count()!==1)throw Error('WEB-08: comparación formal ekiar debe apuntar solo a Andelo');
 if(!((await page.locator('#crossResults').innerText()).includes('Mosaico de Andelo')))throw Error('WEB-08: no señala comparación no literal de Andelo');
 await page.locator('#crossQuery').fill('śalirg');
 await page.locator('#crossEvidence').selectOption('EDITORIAL_VARIANT_UNCOLLATED');
 if(await page.locator('#crossResults .ib-forms-result').count()!==1)throw Error('WEB-08: śalirg debe permanecer variante editorial de La Serreta');
 if(!((await page.locator('#crossGate').innerText()).includes('cero cotejos independientes')))throw Error('WEB-08: no declara que faltan verificaciones de grafemas');
 console.log('✓ WEB-08: tres clases excluyentes y ningún cotejo paleográfico inventado');
 // WEB-09: page/passages are traceable, but cannot masquerade as photo verification.
 await page.locator('#crossQuery').fill('ekiar');
 await page.locator('#crossEvidence').selectOption('EDITORIAL_FORM_UNCOLLATED');
 const caminreal=await page.locator('#crossResults .ib-forms-result').first().innerText();
 if(!caminreal.includes('p. 96')||!caminreal.includes('segundo elemento')||!caminreal.includes('no se han examinado directamente grafemas'))throw Error('WEB-09: faltan página, posición y límites verificables en Caminreal');
 await page.locator('#crossQuery').fill('śalir');
 const summaries=await page.locator('#crossResults .ib-forms-result').allInnerTexts();
 if(!summaries.some(t=>t.includes('p. 200')&&t.includes('Línea 2')))throw Error('WEB-09: Tivissa sin página y línea editorial');
 if(!summaries.some(t=>t.includes('Villares V')&&t.includes('13411')&&t.includes('No cotejo visual independiente')))throw Error('WEB-10: Villares V requiere inventario y límite de cotejo fotográfico');
 await page.locator('#crossEvidence').selectOption('EDITORIAL_VARIANT_UNCOLLATED');
 await page.locator('#crossQuery').fill('śalirg');
 const serreta=await page.locator('#crossResults .ib-forms-result').first().innerText();
 if(!serreta.includes('Cara B, línea 1')||!serreta.includes('1.016')||!serreta.includes('sin verificación visual independiente'))throw Error('WEB-10: La Serreta necesita inventario museístico y límite visual');
 console.log('✓ WEB-09: localizadores editoriales y puertas científicas separados de lectura fotográfica');
 const catalogueLinks=await page.locator('#crossResults a').evaluateAll(xs=>xs.map(a=>a.href));
 if(!catalogueLinks.some(u=>u.includes('catalogo_cas_04_CATALOGO_MATERIALES.pdf')))throw Error('WEB-10: falta fuente museística de La Serreta');
 await page.locator('#crossQuery').fill('śalir');
 await page.locator('#crossEvidence').selectOption('EDITORIAL_FORM_UNCOLLATED');
 const villaresCard=page.locator('#crossResults .ib-forms-result').filter({hasText:'Villares V'});
 if(await villaresCard.count()!==1||!((await villaresCard.innerText()).includes('A1, A3, A5, A8, B1, B5')))throw Error('WEB-10: falta localización de śalir según museo de Villares V');
 if(!((await villaresCard.locator('a').evaluateAll(xs=>xs.map(a=>a.href))).some(u=>u.includes('13411'))))throw Error('WEB-10: vínculo a inventario 13411 ausente');
 console.log('✓ WEB-10: fuentes de museo localizadas, objeto correcto, sin promover lectura fotográfica');





 // WEB-11: one object, 14 museum-versus-2024 textual rows; no invented paleographic checks.
 await page.goto(base+'/cotejo-villares-v/',{waitUntil:'domcontentloaded'});
 await page.locator('#vv-rows tr').first().waitFor({state:'visible',timeout:15000});
 if(await page.locator('#vv-rows tr').count()!==14)throw Error('WEB-11: matrix does not contain 14 rows');
 const matrixText=await page.locator('#vv-rows').innerText();
 const matrixStatus=await page.locator('#vv-status').innerText();
 for(const code of ['A1','A3','A7','A8','A9','B1','B2','B4','B5'])if(!matrixText.includes(code))throw Error('WEB-11: missing line '+code);
 if(!matrixText.includes('bobai-da')||!matrixText.includes('śalir')||!matrixStatus.includes('0 cotejos independientes'))throw Error('WEB-11: matrix hides corrections or incorrectly claims verification');
 if(!((await page.locator('main').innerText()).includes('no son correcciones paleográficas acreditadas')))throw Error('WEB-11: scientific caveat absent');
 console.log('✓ WEB-11: 14 editorial rows, zero independent sign checks and source links');
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

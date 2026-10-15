import {chromium} from 'playwright';
const browser=await chromium.launch({headless:true,args:['--no-sandbox']});
const page=await browser.newPage({acceptDownloads:true});
const base='http://127.0.0.1:8765';
function check(v,msg){if(!v)throw Error('FALLA: '+msg);console.log('✓ '+msg)}
try{
 await page.goto(base+'/laboratorio/?id=IBR-CER-0002');
 check((await page.locator('#save').innerText()).includes('Ver mi cuaderno'),'Botón de visualización comprensible');
 check((await page.locator('#json').innerText()).includes('Guardar una copia'),'Botón para guardar copia comprensible');
 await page.locator('#name').fill('Prueba de recuperación IberOS');
 await page.locator('#question').fill('¿Se conserva la pregunta de investigación?');
 await page.reload();
 check(await page.locator('#name').inputValue()==='Prueba de recuperación IberOS','Nombre persiste tras recarga');
 check(await page.locator('#question').inputValue()==='¿Se conserva la pregunta de investigación?','Pregunta persiste tras recarga');
 check(await page.locator('#object').inputValue()==='IBR-CER-0002','Selección de pieza persiste');
 check(await page.locator('#actions a[href="../ficha/?id=IBR-CER-0002#core-audit-slot"]').count()===1,'Laboratorio enlaza auditoría científica específica de la pieza');
 await page.waitForFunction(()=>document.querySelector('#preview')?.textContent.includes('Reglas candidatas:'),null,{timeout:15000});
 const [dl]=await Promise.all([page.waitForEvent('download'),page.locator('#json').click()]);
 const json=JSON.parse((await (await import('node:fs/promises')).readFile(await dl.path())).toString('utf8'));
 check(json.name==='Prueba de recuperación IberOS'&&json.object==='IBR-CER-0002','Exportación JSON íntegra');
 check(json.core_audit_reference?.object_id==='IBR-CER-0002'&&json.core_audit_reference?.interpretation_status==='NOT_VALIDATED','Exportación incluye auditoría Core trazable sin validación inventada');
 check(Array.isArray(json.core_audit_reference?.rule_sources)&&json.core_audit_reference.rule_sources.every(x=>x.id&&x.applicability&&x.semantic_translation_verified===false),'Exportación identifica reglas, aplicabilidad y ausencia de validación semántica');
 check(json.core_audit_reference?.source_record?.catalog==='core_rule_catalog_v1.json','Exportación conserva referencia al catálogo de reglas');
 await page.locator('#name').fill('Cambios temporales');
 page.once('dialog',dialog=>{void dialog.accept().catch(()=>{});});
 await page.locator('#importProject').setInputFiles({name:'proyecto.json',mimeType:'application/json',buffer:Buffer.from(JSON.stringify(json))});
 await page.waitForFunction(expected=>document.querySelector('#name')?.value===expected,json.name);
 check(await page.locator('#name').inputValue()===json.name,'Importación restaura el nombre');
 check(await page.locator('#question').inputValue()===json.question,'Importación restaura la pregunta');
 await page.goto(base+'/laboratorio/?id=IBR-MUS-0001');
 check(await page.locator('#object').inputValue()==='IBR-MUS-0001','Al cambiar de pieza se abre la nueva');
 check(await page.locator('#question').inputValue()==='','No se mezclan preguntas de dos proyectos');
 page.once('dialog',dialog=>{void dialog.accept().catch(()=>{});});
 await page.locator('#restorePrevious').click();
 // La restauración requiere confirmación: probar con un clic adicional si se rechaza.
 check(await page.locator('#object').inputValue()==='IBR-CER-0002','Recuperación de cuaderno anterior');

 await page.goto(base+'/webengine/?q=IBR-MUS-0001');
 await page.locator('#core-cards .core-result-card').first().waitFor();
 check((await page.locator('#core-cards .core-result-card').count())>=1,'Core muestra tarjetas visuales');
 await page.locator('#core-rule-audit details').waitFor({timeout:15000});
 const scientificRules=await page.locator('#core-rule-audit').innerText();
 check(scientificRules.includes('reglas de traducción verificadas'),'Core muestra conteo auditado de reglas');
 check(scientificRules.includes('0 reglas de traducción verificadas'),'Core no confunde protocolos con traducciones verificadas');
 await page.locator('#core-rule-audit summary').click();
 check(await page.locator('#core-rule-audit li').count()>0,'Catálogo científico Python visible e interactivo');

 check((await page.locator('#core-cards .interpretation-main').first().innerText()).length>10,'Core muestra interpretación o límite explícito');
 await page.locator('#q').fill('IBEROS_SIN_COINCIDENCIAS_PRUEBA_2026');
 await page.locator('#go').click();
 check((await page.locator('#core-cards').innerText()).includes('No se encontraron coincidencias'),'Core informa de consultas sin resultados');
 await page.locator('#q').fill('IBR-MUS-0001');
 await page.locator('#go').click();
 const fiche=page.locator('#core-cards a[href*="../ficha/"]').first();
 check((await fiche.getAttribute('href')).includes('IBR-MUS-0001'),'Core enlaza a ficha correcta');
 for(const id of ['IBR-PLM-0002','IBR-PLM-0003']){
   const errors=[];
   const handler=e=>errors.push(e.message);
   page.on('pageerror',handler);
   await page.goto(base+'/ficha/?id='+id);
   await page.locator('#variant-review-slot .section-title').waitFor({timeout:15000});
   check((await page.locator('#variant-review-slot').innerText()).includes('Lecturas, variantes y verificaciones'),'Ficha '+id+' muestra cotejo de variantes');
   check((await page.locator('#variant-review-slot article.card').count())>=1,'Ficha '+id+' presenta variante documentada');
   check((await page.locator('#interpretationMain').innerText()).length>10,'Ficha '+id+' presenta interpretación o límite');
   await page.locator('#core-audit-slot .ib-core-state').first().waitFor({timeout:15000});
   check((await page.locator('#core-audit-slot .ib-core-state').first().innerText()).includes('Contexto geográfico'),'Estados científicos legibles en español '+id);
   const identityColors=await page.locator('.artifact-summary').evaluate(root=>{
     const values=selector=>{const node=root.querySelector(selector);return node?getComputedStyle(node).color:"missing"};
     return {title:values('h1'),description:values('p.meta'),button:values('.artifact-actions a:nth-child(2)')};
   });
   check(Object.values(identityColors).every(c=>c.startsWith('rgb(')&&Number((c.match(/[0-9]+/)||[])[0])<90),'Identificación oscura y botones legibles '+id+' '+JSON.stringify(identityColors));

   const readingContrast=await page.locator('.ib-sign-reading').evaluate(el=>{
     const rgb=x=>{const m=getComputedStyle(x).color.match(/\d+/g);return m?m.slice(0,3).map(Number):[]};
     const [r,g,b]=rgb(el);return r<90&&g<100&&b<120;
   });
   check(readingContrast,'Lectura ibérica con tinta oscura '+id);
   const normalizedInk=await page.locator('.ib-normalized-reading .ib-sign-script').first().evaluate(el=>{
     const nums=getComputedStyle(el).color.match(/\d+/g)?.map(Number)||[];
     return nums.length>=3&&nums[0]<80&&nums[1]<95&&nums[2]<110;
   });
   check(normalizedInk,'Transliteración normalizada con tinta de alto contraste '+id);
   const ratios=await page.evaluate(()=>{
     const rgb=value=>(value.match(/[0-9.]+/g)||[]).slice(0,3).map(Number);
     const lum=parts=>parts.slice(0,3).map(v=>{v=v/255;return v<=.04045?v/12.92:((v+.055)/1.055)**2.4}).reduce((acc,v,i)=>acc+v*[.2126,.7152,.0722][i],0);
     const contrast=(fg,bg)=>{const a=lum(rgb(fg)),b=lum(rgb(bg));return (Math.max(a,b)+.05)/(Math.min(a,b)+.05)};
     return [
       ['lectura', '.ib-normalized-reading .ib-sign-script','.ib-normalized-reading'],
       ['navegación', '.ib-expert-nav a','.ib-expert-nav a'],
       ['cabecera matriz', '.ib-hypothesis-matrix th','.ib-hypothesis-matrix th'],
       ['celda matriz', '.ib-hypothesis-matrix td','.ib-hypothesis-matrix td']
     ].map(([label,textSel,bgSel])=>{
       const el=document.querySelector(textSel),bg=document.querySelector(bgSel);
       if(!el||!bg)return {label,ratio:0};
       return {label,ratio:contrast(getComputedStyle(el).color,getComputedStyle(bg).backgroundColor)};
     });
   });
   check(ratios.every(x=>x.ratio>=4.5),'Contraste mínimo WCAG AA en lectura, navegación y matriz '+id+': '+JSON.stringify(ratios));


   check(await page.locator('.ib-expert-nav a').first().isVisible(),'Navegación experta visible '+id);

   await page.locator('#core-rule-evidence').waitFor({timeout:15000});
   await page.waitForFunction(()=>{const x=document.querySelector('#core-rule-evidence');return x&&!x.textContent.includes('Consultando catálogo')},{timeout:15000});
   check((await page.locator('#core-rule-evidence').innerText()).length>35,'Ficha enlaza reglas y estado científico '+id);
   check((await page.locator('#core-rule-evidence').innerText()).includes('Cadena de evidencia y límites'),'Cadena documental cargada '+id);
   await page.locator('#core-rule-evidence details summary').click();
   check(await page.locator('#core-rule-evidence details p').count()>=2,'Fuentes y obstáculos visibles '+id);
   check(await page.locator('#core-rule-evidence .ib-hypothesis-matrix th').count()===4,'Matriz científica con cuatro columnas '+id);
   const matrixContrast=await page.locator('.ib-hypothesis-matrix').evaluate(root=>{
      const light=(node)=>{const c=getComputedStyle(node).color.match(/\d+/g)?.map(Number)||[];return c.length===3&&c[0]<75&&c[1]<95&&c[2]<110};
      const body=root.querySelector('td'),heading=root.querySelector('th');
      const ink=light(body);
      const headerColor=getComputedStyle(heading).color;
      return ink&&headerColor==='rgb(255, 255, 255)';
   });
   check(matrixContrast,'Contraste legible de texto y cabeceras en matriz '+id);

   check(await page.locator('#core-rule-evidence .ib-hypothesis-matrix tbody tr').count()>=1,'Hipótesis y pruebas pendientes visibles '+id);
   const nav=page.locator('.ib-expert-nav');
   check(await nav.isVisible(),'Acceso experto visible '+id);
   check((await nav.locator('a').count())===6,'Seis accesos expertos '+id);
   check((await nav.locator('a[href="#geography-slot"]').count())===1,'Enlace geográfico '+id);
   check((await nav.locator('a[href="#sign-reading-slot"]').count())===1,'Acceso a signos y transliteración '+id);
   check((await nav.locator('a[href="#documentary-slot"]').count())===1,'Enlace de evidencia '+id);
   check((await nav.locator('a[href="#variant-review-slot"]').count())===1,'Enlace de variantes '+id);
   check((await nav.locator('a[href*="../webengine/?q="]').first().getAttribute('href')).includes(id),'Core apunta a la pieza '+id);
   const [exported]=await Promise.all([page.waitForEvent('download'),nav.locator('#expertExport').click()]);
   const exportedJson=JSON.parse((await (await import('node:fs/promises')).readFile(await exported.path())).toString('utf8'));
   check(exportedJson.object_id===id&&exportedJson.documentary_enrichment?.OBJECT_ID===id,'JSON documentado de '+id);
   check(exportedJson.scientific_review?.object_id===id&&exportedJson.scientific_review?.publication_approved===false,'Exportación conserva revisión no aprobada '+id);
   const size=await page.locator('#interpretationMain').evaluate(el=>parseFloat(getComputedStyle(el).fontSize));
   check(size<=23,'Tamaño de interpretación compacto '+id+' ('+size+' px)');

   check(errors.length===0,'Ficha '+id+' sin errores JavaScript: '+errors.join('; '));
   page.off('pageerror',handler);
 }
 // Recorrido completo reproducible: descubrimiento, evidencia, motor y cuaderno.
 await page.goto(base+'/corpus/?q=IBR-PLM-0002');
 const corpusLink=page.locator('#grid a[href*="../ficha/?id=IBR-PLM-0002"]').first();
 await corpusLink.waitFor({timeout:15000});
 check(await corpusLink.isVisible(),'Corpus encuentra Tivissa y ofrece ficha');
 await corpusLink.click();
 await page.locator('#interpretationMain').waitFor({timeout:15000});
 check(new URL(page.url()).searchParams.get('id')==='IBR-PLM-0002','Corpus abre la pieza correcta');
 const coreLink=page.locator('.ib-expert-nav a[href*="../webengine/?q="]');
 await coreLink.click();
 check(new URL(page.url()).searchParams.get('q')==='IBR-PLM-0002','Acceso experto envía la misma pieza al Core');
 await page.locator('#core-cards .core-result-card').first().waitFor({timeout:15000});
 const labLink=page.locator('#core-cards a[href="../laboratorio/?id=IBR-PLM-0002"]').first();
 await labLink.waitFor({timeout:15000});
 await labLink.click();
 check(new URL(page.url()).pathname.endsWith('/laboratorio/')&&new URL(page.url()).searchParams.get('id')==='IBR-PLM-0002','Core abre Laboratorio conservando la pieza');
 await page.waitForFunction(()=>document.querySelector('#object')?.value==='IBR-PLM-0002',null,{timeout:15000});
 check(await page.locator('#object').inputValue()==='IBR-PLM-0002','Laboratorio conserva la pieza de origen');
 await page.locator('#name').fill('Recorrido completo IberOS');
 await page.locator('#question').fill('¿Qué evidencia sostiene esta interpretación?');
 const [journeyFile]=await Promise.all([page.waitForEvent('download'),page.locator('#json').click()]);
 const journey=JSON.parse((await (await import('node:fs/promises')).readFile(await journeyFile.path())).toString('utf8'));
 check(journey.object==='IBR-PLM-0002'&&journey.name==='Recorrido completo IberOS','Proyecto exportado conserva la pieza y el nombre');
 await page.locator('#name').fill('Proyecto temporal sin guardar');
 page.once('dialog',dialog=>{void dialog.accept().catch(()=>{});});
 await page.locator('#importProject').setInputFiles({name:'recorrido-iberos.json',mimeType:'application/json',buffer:Buffer.from(JSON.stringify(journey))});
 await page.waitForFunction(()=>document.querySelector('#name')?.value==='Recorrido completo IberOS');
 check(await page.locator('#name').inputValue()===journey.name,'La importación recupera el nombre exportado');
 check(await page.locator('#object').inputValue()===journey.object,'La importación conserva la pieza');
 check(await page.locator('#question').inputValue()===journey.question,'La importación recupera la pregunta científica');

 await page.goto(base+'/atlas/?q=Pech-Maho');
 await page.locator('#mapStatus').waitFor({timeout:15000});
 check(await page.locator('#mapStatus').isVisible(),'Atlas informa de procedencia sin nodo cartográfico');
 check((await page.locator('#mapStatus').innerText()).includes('Pech-Maho'),'Atlas conserva el nombre de la procedencia solicitada');
 await page.goto(base+'/atlas/?q=Castellet%20de%20Banyoles');
 check((await page.locator('#siteQ').inputValue()).includes('Castellet de Banyoles'),'Atlas recibe búsqueda geográfica desde Tivissa');
 // Todas las fichas deben utilizar la plantilla científica canónica.
 const csvResponse=await page.request.get(base+'/data/objects.csv');
 check(csvResponse.ok(),'Catálogo accesible para verificar todas las fichas');
 const allIds=(await csvResponse.text()).replace(/^\uFEFF/,'').split(/\r?\n/).slice(1).map(line=>line.split(',')[0].trim()).filter(Boolean);
 check(allIds.length===38,'Cobertura esperada de 38 objetos y controles');
 for(const objectId of allIds){
   await page.goto(base+'/ficha/?id='+encodeURIComponent(objectId));
   await page.locator('.ib-canonical-banner').waitFor({timeout:15000});
   check(await page.locator('.ib-primary-grid').count()===1&&await page.locator('.ib-reconstruction').count()===1,'Plantilla canónica cargada '+objectId);
   await page.locator('#sign-reading-slot.ib-sign-reading').waitFor({timeout:15000});
   check((await page.locator('#sign-reading-slot').innerText()).length>45,'Lectura o ausencia documental explícita '+objectId);
   check(await page.locator('#sign-reading-slot .ib-normalized-reading').count()>=1,'Panel de normalización en ficha '+objectId);
   check(await page.locator('#sign-correspondence').count()===1,'Panel de signos en ficha '+objectId);
   const legibility=await page.locator('#sign-reading-slot').evaluate(root=>{
     const text=root.querySelector('.ib-normalized-reading .ib-sign-script')||root.querySelector('.ib-normalized-reading p');
     const nav=document.querySelector('.ib-expert-nav a');
     const rgb=value=>(value.match(/[0-9.]+/g)||[]).slice(0,3).map(Number);
     const lum=value=>rgb(value).map(v=>{const n=v/255;return n<=.04045?n/12.92:((n+.055)/1.055)**2.4}).reduce((sum,v,i)=>sum+v*[.2126,.7152,.0722][i],0);
     const ratio=(a,b)=>{const x=lum(a),y=lum(b);return (Math.max(x,y)+.05)/(Math.min(x,y)+.05)};
     if(!text||!nav)return {reading:0,navigation:0};
     const textStyle=getComputedStyle(text),bgStyle=getComputedStyle(text.closest('.ib-normalized-reading'));
     const navStyle=getComputedStyle(nav);
     return {reading:ratio(textStyle.color,bgStyle.backgroundColor),navigation:ratio(navStyle.color,navStyle.backgroundColor)};
   });
   check(legibility.reading>=4.5&&legibility.navigation>=4.5,'Contraste AA de lectura y navegación '+objectId+' '+JSON.stringify(legibility));

   await page.locator('#graphic-viewer-slot .ib-graphic-viewer').waitFor({timeout:15000});
   check(await page.locator('#graphic-viewer-slot .ib-graphic-viewer').count()===1,'Visor gráfico documental '+objectId);
   if(objectId==='IBR-PLM-0002'||objectId==='IBR-PLM-0003')check(await page.locator('#graphic-viewer-slot .ib-graphic-source').count()===0,'Sin reproducción gráfica no autorizada '+objectId);
   if(objectId==='IBR-PLM-0002'||objectId==='IBR-PLM-0003')check(await page.locator('#graphic-viewer-slot .ib-documentary-checklist a[href^="https://"]').count()>=1,'Enlace a imagen externa candidata, sin presentar reproducción no cotejada '+objectId);
   if(objectId==='IBR-PLM-0002'||objectId==='IBR-PLM-0003')check(await page.locator('#graphic-viewer-slot .ib-candidate-checks li').count()>=3,'Tres requisitos explícitos de cotejo de imagen '+objectId);
   if(objectId==='IBR-PLM-0002'||objectId==='IBR-PLM-0003'){
     const checklist=page.locator('#graphic-viewer-slot .ib-documentary-checklist').filter({has:page.locator('summary').getByText('Verificación documental de imagen y signos')});
     check(await checklist.count()===1,'Requisitos gráficos auditables '+objectId);
     await checklist.locator('summary').click();
     check((await checklist.innerText()).includes('Signos gráficos individualizados aptos para publicación: 0'),'Sin glifos falsamente acreditados '+objectId);
   }

   if(objectId==='IBR-PLM-0002'||objectId==='IBR-PLM-0003')check(await page.locator('#graphic-viewer-slot .ib-glyph-hotspot').count()===0,'Sin signos gráficos no verificados '+objectId);
   check(await page.locator('.ib-piece-original .doc-cover').count()===0,'Sin portada decorativa en panel de pieza original '+objectId);
   check(await page.locator('.ib-piece-original .ib-authentic-object, .ib-piece-original .ib-object-awaiting').count()===1,'Imagen acreditada o ausencia explícita '+objectId);
   if(objectId==='IBR-PLM-0002'){
     const first=page.locator('#sign-correspondence .ib-sign-choice').first();
     check(await first.count()>0,'Inventario editorial interactivo de Tivissa');
     await first.click();
     check(await first.getAttribute('aria-pressed')==='true','Selección accesible de signo');
     check((await page.locator('#ib-sign-detail').innerText()).includes('Pendiente de verificación individual'),'Límites del signo visibles');
   }
   check((await page.locator('#sign-reading-slot').innerText()).includes('01 · LECTURA EDITORIAL'),'Lectura editorial visible '+objectId);
   if(['IBR-CER-0001','IBR-PLM-0002','IBR-PLM-0003'].includes(objectId)){
     await page.setViewportSize({width:390,height:844});
     const mobile=await page.locator('.ib-primary-grid').evaluate(el=>{
       const rect=el.getBoundingClientRect();
       return rect.width>0&&rect.width<=document.documentElement.clientWidth+2;
     });
     check(mobile,'Ficha legible dentro de viewport móvil '+objectId);
     await page.setViewportSize({width:1280,height:800});
   }

 }
 // Navigation integrity: all visible directory links resolve to a real public document.
 await page.goto(base+'/mapa-web/');
 const directoryLinks=await page.locator('main a[href]').evaluateAll(nodes=>nodes.map(a=>({href:a.getAttribute('href'),label:a.textContent.trim()})).filter(a=>a.href&&!a.href.startsWith('#')));
 const broken=[];
 for(const item of directoryLinks){
   const url=new URL(item.href,page.url());
   if(url.origin!==new URL(base).origin)continue;
   const response=await page.request.get(url.toString());
   if(!response.ok())broken.push(item.label+' '+url.pathname+' HTTP '+response.status());
 }
 check(broken.length===0,'Menú completo: todos los enlaces internos responden correctamente '+broken.join('; '));
 await page.setViewportSize({width:390,height:844});
 await page.goto(base+'/proyectos/');
 const mobileNav=page.locator('.menu-toggle');
 check(await mobileNav.isVisible(),'Navegación móvil accesible desde Proyectos');
 await mobileNav.click();
 check(await mobileNav.getAttribute('aria-expanded')==='true','Menú móvil anuncia estado abierto');
 await page.keyboard.press('Escape');
 check(await mobileNav.getAttribute('aria-expanded')==='false','Menú móvil se cierra con Escape');
 await page.setViewportSize({width:1280,height:800});
 await page.goto(base+'/proyectos/');
 await page.locator('#project-list .project-card').first().waitFor({timeout:15000});
 check((await page.locator('#project-list').innerText()).includes('Reconstrucción arqueológica de La Picola'),'Proyectos presenta La Picola en curso');
 check((await page.locator('#news-list').innerText()).includes('No hay noticias aprobadas'),'La Picola no se publica como noticia terminada');
 check(await page.locator('.main-nav a[href$="proyectos/"]').count()===1,'Menú principal incluye Proyectos / News');
 await page.goto(base+'/mapa-web/');
 check(await page.locator('a[href="../proyectos/"]').count()>=1,'Menú completo enlaza Proyectos / News');
 await page.goto(base+'/diagnostico/');
 await page.locator('#results h2').waitFor({timeout:15000});
 check((await page.locator('#results h2').innerText()).includes('7 de 7'),'Diagnóstico gratuito supera sus siete verificaciones');
 console.log('Laboratorio y Core: pruebas de navegador satisfactorias');
}catch(error){
 console.error('FALLO DE PRUEBA EN '+page.url()+':',error);
 try{await page.screenshot({path:'/tmp/iberos-browser-fallo.png',fullPage:true});console.error('Captura guardada en /tmp/iberos-browser-fallo.png')}catch(captureError){console.error('No se pudo guardar captura:',captureError.message)}
 throw error;
}finally{await browser.close()}

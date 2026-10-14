import {chromium} from 'playwright';
const browser=await chromium.launch({headless:true,args:['--no-sandbox']});
const page=await browser.newPage({acceptDownloads:true});
const base='http://127.0.0.1:8765';
function check(v,msg){if(!v)throw Error('FALLA: '+msg);console.log('✓ '+msg)}
try{
 await page.goto(base+'/laboratorio/?id=IBR-CER-0002');
 await page.locator('#name').fill('Prueba de recuperación IberOS');
 await page.locator('#question').fill('¿Se conserva la pregunta de investigación?');
 await page.reload();
 check(await page.locator('#name').inputValue()==='Prueba de recuperación IberOS','Nombre persiste tras recarga');
 check(await page.locator('#question').inputValue()==='¿Se conserva la pregunta de investigación?','Pregunta persiste tras recarga');
 check(await page.locator('#object').inputValue()==='IBR-CER-0002','Selección de pieza persiste');
 const [dl]=await Promise.all([page.waitForEvent('download'),page.locator('#json').click()]);
 const json=JSON.parse((await (await import('node:fs/promises')).readFile(await dl.path())).toString('utf8'));
 check(json.name==='Prueba de recuperación IberOS'&&json.object==='IBR-CER-0002','Exportación JSON íntegra');
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
   const nav=page.locator('.ib-expert-nav');
   check(await nav.isVisible(),'Acceso experto visible '+id);
   check((await nav.locator('a').count())===5,'Cinco accesos expertos '+id);
   check((await nav.locator('a[href="#geography-slot"]').count())===1,'Enlace geográfico '+id);
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
 check(await page.locator('#object').inputValue()==='IBR-PLM-0002','Laboratorio conserva la pieza de origen');
 await page.locator('#name').fill('Recorrido completo IberOS');
 await page.locator('#question').fill('¿Qué evidencia sostiene esta interpretación?');
 const [journeyFile]=await Promise.all([page.waitForEvent('download'),page.locator('#json').click()]);
 const journey=JSON.parse((await (await import('node:fs/promises')).readFile(await journeyFile.path())).toString('utf8'));
 check(journey.object==='IBR-PLM-0002'&&journey.name==='Recorrido completo IberOS','Proyecto exportado conserva la pieza y el nombre');
 await page.goto(base+'/atlas/?q=Pech-Maho');
 await page.locator('#mapStatus').waitFor({timeout:15000});
 check(await page.locator('#mapStatus').isVisible(),'Atlas informa de procedencia sin nodo cartográfico');
 check((await page.locator('#mapStatus').innerText()).includes('Pech-Maho'),'Atlas conserva el nombre de la procedencia solicitada');
 await page.goto(base+'/atlas/?q=Castellet%20de%20Banyoles');
 check((await page.locator('#siteQ').inputValue()).includes('Castellet de Banyoles'),'Atlas recibe búsqueda geográfica desde Tivissa');
 await page.goto(base+'/diagnostico/');
 await page.locator('#results h2').waitFor({timeout:15000});
 check((await page.locator('#results h2').innerText()).includes('7 de 7'),'Diagnóstico gratuito supera sus siete verificaciones');
 console.log('Laboratorio y Core: pruebas de navegador satisfactorias');
}catch(error){
 console.error('FALLO DE PRUEBA EN '+page.url()+':',error);
 try{await page.screenshot({path:'/tmp/iberos-browser-fallo.png',fullPage:true});console.error('Captura guardada en /tmp/iberos-browser-fallo.png')}catch(captureError){console.error('No se pudo guardar captura:',captureError.message)}
 throw error;
}finally{await browser.close()}

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
 console.log('Laboratorio y Core: pruebas de navegador satisfactorias');
}finally{await browser.close()}

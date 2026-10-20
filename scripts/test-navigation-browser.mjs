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
 const corpus=await page.goto(base+'/corpus/?q=Tivissa',{waitUntil:'domcontentloaded'});
 await page.waitForTimeout(1000);
 if(await page.locator('a[href*="../ficha/?id=IBR-PLM-0002"]').count()===0)throw Error('Corpus no muestra acceso a ficha de Tivissa');
 console.log('✓ Corpus enlaza a la ficha desde resultados reales');
}catch(error){errors.push(error.message);await page.screenshot({path:'/tmp/iberos-navigation-fallo.png',fullPage:true}).catch(()=>{});}
finally{await browser.close();}
if(errors.length){console.error(errors.join('\n'));process.exit(1);}
console.log('Recorrido Corpus → Ficha → CORE → Laboratorio: PASS');

import test from 'node:test';
import assert from 'node:assert/strict';
import {spawn} from 'node:child_process';
import {setTimeout as delay} from 'node:timers/promises';
import {chromium} from 'playwright';

const server = spawn('python3', ['-m', 'http.server', '8765', '--directory', 'site'], {stdio: 'ignore'});
let browser;
async function visit(path) {
  const page = await browser.newPage();
  const response = await page.goto('http://127.0.0.1:8765/' + path, {waitUntil:'domcontentloaded'});
  assert.equal(response.status(), 200, 'HTTP 200: '+path);
  assert.ok((await page.title()).trim(), 'nonempty title: '+path);
  return page;
}
try {
  await delay(1100);
  browser = await chromium.launch({headless:true, args:['--no-sandbox']});
  test('Public navigation: homepage and modules render on mobile', async () => {
    const page = await browser.newPage({viewport:{width:390,height:844},isMobile:true,hasTouch:true});
    try {
      await page.goto('http://127.0.0.1:8765/', {waitUntil:'domcontentloaded'});
      assert.match(await page.title(), /IberOS/i);
      for (const path of ['corpus/','fichas/','laboratorio/','herramientas/','atlas/','modelos3d/','write/','webengine/']) {
        const response=await page.goto('http://127.0.0.1:8765/'+path,{waitUntil:'domcontentloaded'});
        assert.equal(response.status(),200,path);
        assert.ok(await page.locator('body').innerText(),path);
      }
    } finally {await page.close();}
  });
  test('Tool navigation via real mobile clicks', async () => {
    const page=await browser.newPage({viewport:{width:390,height:844},isMobile:true,hasTouch:true});
    try {
      await page.goto('http://127.0.0.1:8765/herramientas/',{waitUntil:'domcontentloaded'});
      for (const [label,path] of [
        ['Probar Core','/webengine/'],
        ['Probar Write','/write/'],
        ['Probar Talk','/talk/'],
        ['Abrir Atlas','/atlas/']
      ]) {
        await page.goto('http://127.0.0.1:8765/herramientas/',{waitUntil:'domcontentloaded'});
        await page.getByRole('link',{name:new RegExp(label,'i')}).click();
        await page.waitForURL(url=>url.pathname.endsWith(path));
        assert.ok((await page.locator('body').innerText()).length>50,label);
      }
    } finally {await page.close();}
  });
  test('Talk analysis displays an actual textual result', async () => {
    const page=await visit('talk/');
    try {
      await page.locator('#txt').fill('EKIAR KUTUR SALIR');
      await page.locator('#run').click();
      await page.waitForFunction(()=>document.querySelector('#out')?.textContent.trim().length>0,null,{timeout:12000});
      const result=await page.locator('#out').textContent();
      assert.ok(result.length>0);
      assert.doesNotMatch(result,/Error de preparaci[oó]n|Error t[eé]cnico/i);
    } finally {await page.close();}
  });
  test('Write renders a real graphic result for entered text', async () => {
    const page=await visit('write/');
    try {
      await page.locator('#q').fill('hola mundo');
      await page.locator('#go').click();
      await page.waitForTimeout(800);
      const out=(await page.locator('#out').innerText()).trim();
      const feedback=(await page.locator('#write-feedback').innerText()).trim();
      const graphic=await page.locator('#write-stone-preview').count();
      assert.match(feedback, /hola mundo/i, 'Write feedback must reflect submitted phrase');
      assert.ok(!out.startsWith('Error al analizar:'), 'Write must not return technical error');
      assert.ok(await page.locator('#write-stone-text').locator('img, span, strong').count() > 0, 'Write must render actual sign/token elements, not just an empty stone container');
      assert.match(await page.locator('#write-stone-note').innerText(), /fonogr[aá]fic|traducci[oó]n/i, 'Graphic output must be explicitly qualified');
    } catch(e) {
      await page.screenshot({path:'/tmp/iberos-e2e-write.png',fullPage:true});
      throw e;
    } finally {await page.close();}
  });
  test('3D external resources and filters respond', async () => {
    const page=await visit('modelos3d/');
    try {
      await page.waitForFunction(()=>document.querySelector('#resource3d-count')?.textContent.trim().length>0,null,{timeout:12000});
      const total=(await page.locator('#resource3d-count').textContent()).trim();
      await page.locator('#inscribed3d').click();
      assert.equal(await page.locator('#inscribed3d').getAttribute('aria-pressed'),'true');
      await page.locator('#heritage3d').click();
      assert.equal(await page.locator('#heritage3d').getAttribute('aria-pressed'),'true');
      await page.locator('#all3d').click();
      assert.equal(await page.locator('#all3d').getAttribute('aria-pressed'),'true');
      assert.ok(total.length>0);
      assert.ok(await page.locator('#external3d a[href^="https://"]').count()>0,'3D resource links must point to original source');
    } finally {await page.close();}
  });
  test('3D page excludes symbolic demo viewers', async () => {
    const page=await visit('modelos3d/');
    try {
      assert.equal(await page.locator('model-viewer.inscribed-real-model').count(),0);
      assert.equal(await page.locator('a[href*="inscribed-placa.gltf"],a[href*="inscribed-estela.gltf"]').count(),0);
      assert.match(await page.locator('body').innerText(),/modelos 3D originales|piezas arqueol[oó]gicas reales/i);
    } finally {await page.close();}
  });
  test('Write stone preview is visible, labeled and exportable', async () => {
    const page=await visit('write/');
    try {
      await page.locator('#q').fill('hola mundo');
      await page.locator('#go').click();
      await page.waitForFunction(()=>document.querySelector('#write-feedback')?.textContent.includes('hola mundo'),null,{timeout:12000});
      const stone=page.locator('#write-stone-preview');
      assert.ok(await stone.isVisible(), 'stone must be visible');
      assert.match(await stone.getAttribute('aria-label'),/recreaci[oó]n|piedra/i);
      assert.ok(await page.locator('#write-stone-text').locator('span,img,strong').count()>0,'visual signs must be present');
      assert.match(await page.locator('#write-stone-note').innerText(),/no es traducci[oó]n|fonogr[aá]fic/i);
      const downloadPromise=page.waitForEvent('download');
      await page.locator('#write-stone-export').click();
      const file=await downloadPromise;
      assert.match(file.suggestedFilename(),/\.svg$/i);
    } finally {await page.close();}
  });
  test('Core query controls are usable', async () => {
    const page=await visit('webengine/');
    try {
      await page.waitForFunction(() => { const out=document.querySelector('#out'); return out && out.textContent.trim().length>0; }, null, {timeout:12000});
      const initial=await page.locator('#out').textContent();
      assert.ok(!initial.startsWith('Error:'), 'Core initialization must succeed');
      await page.locator('#q').fill('SALIR');
      await page.locator('#go').click();
      await page.waitForFunction(() => { try { const data=JSON.parse(document.querySelector('#out').textContent); return data && typeof data.count==='number'; } catch { return false; } }, null, {timeout:12000});
      const result=JSON.parse(await page.locator('#out').textContent());
      assert.equal(typeof result.count,'number');
      assert.ok(result.count>0, 'Known CORE query SALIR must return matches');
    } finally {await page.close();}
  });
} finally {
  // node:test executes tests later, so close in after() instead.
}
import {after} from 'node:test';
after(async()=>{if(browser)await browser.close();server.kill();});

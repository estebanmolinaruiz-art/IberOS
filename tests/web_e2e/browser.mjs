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
  test('Core query controls are usable', async () => {
    const page=await visit('webengine/');
    try {
      await page.waitForFunction(() => { const out=document.querySelector('#out'); return out && out.textContent.trim().length>0; }, null, {timeout:12000});
      const initial=await page.locator('#out').innerText();
      assert.ok(!initial.startsWith('Error:'), 'Core initialization must succeed');
      await page.locator('#q').fill('SALIR');
      await page.locator('#go').click();
      await page.waitForFunction(() => { try { const data=JSON.parse(document.querySelector('#out').textContent); return data && typeof data.count==='number'; } catch { return false; } }, null, {timeout:12000});
      const result=JSON.parse(await page.locator('#out').innerText());
      assert.equal(typeof result.count,'number');
      assert.ok(result.count>0, 'Known CORE query SALIR must return matches');
    } finally {await page.close();}
  });
} finally {
  // node:test executes tests later, so close in after() instead.
}
import {after} from 'node:test';
after(async()=>{if(browser)await browser.close();server.kill();});

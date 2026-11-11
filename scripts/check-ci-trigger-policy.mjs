import { readFileSync } from 'node:fs';
import assert from 'node:assert/strict';

// WEB-14: asegure un solo disparador automático por paquete.
// Verifica los bloques de activación antes de los jobs; no interpreta scripts de trabajo.
for (const name of ['tests.yml', 'web-e2e-free.yml', 'qa-web.yml']) {
  const source = readFileSync(new URL('../.github/workflows/' + name, import.meta.url), 'utf8');
  const onBlock = source.split(/^jobs:\s*$/m, 1)[0];
  assert.match(onBlock, /^on:\s*$/m, name + ': falta bloque de triggers');
  assert.match(onBlock, /^\s{2}pull_request:\s*$/m, name + ': falta validación por PR');
  assert.doesNotMatch(onBlock, /^\s{2}push:\s*$/m, name + ': ejecución por push duplicaría la PR');
  assert.doesNotMatch(onBlock, /^on:\s*\[.*\bpush\b/m, name + ': lista de triggers incluye push');
  assert.match(onBlock, /^\s{2}workflow_dispatch:\s*$/m, name + ': falta modo manual');
  console.log('✓ ' + name + ': PR y manual, sin push redundante');
}
// Conservar la cobertura E2E de navegación y la comprobación web del Core.
const e2e = readFileSync(new URL('../.github/workflows/web-e2e-free.yml', import.meta.url), 'utf8');
assert.match(e2e, /tests\/web_e2e\/browser\.mjs/, 'E2E: desapareció la prueba real de navegador');
assert.match(e2e, /'site\/\*\*'/, 'E2E: desapareció el filtro de archivos web');
const qa = readFileSync(new URL('../.github/workflows/qa-web.yml', import.meta.url), 'utf8');
assert.match(qa, /scripts\/test-core\.mjs/, 'QA: desapareció el test del Core');
assert.match(qa, /scripts\/test-navigation-browser\.mjs/, 'QA: desapareció la navegación del explorador');
assert.match(qa, /scripts\/check-ci-trigger-policy\.mjs/, 'QA: no ejecuta este control de regresión');
const tests = readFileSync(new URL('../.github/workflows/tests.yml', import.meta.url), 'utf8');
assert.match(tests, /pytest -q/, 'Tests: desapareció pytest');
console.log('✓ Mantienen cobertura: Python, Core, navegación y E2E');

const pages = readFileSync(new URL('../.github/workflows/pages.yml', import.meta.url), 'utf8');
assert.match(pages, /\.github\/release-trigger\/\*\*/, 'Pages sin disparador explícito por paquete');
console.log('✓ Pages permanece limitado al lanzamiento explícito');

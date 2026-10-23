import test from 'node:test';
import assert from 'node:assert/strict';
import {readFile} from 'node:fs/promises';
import {IberOSWrite} from '../site/write/iberos-write.mjs';

globalThis.document={baseURI:'https://example.invalid/write/'};
const rules=JSON.parse(await readFile(new URL('../site/write/data/write-rules.json',import.meta.url)));
const write=new IberOSWrite();
write.rules=rules; write.ready=true;

for(const input of [
  'A Bastubar se transfiere un documento.',
  'A Bastubar se entrega un texto.',
  'A Esteban se entrega un documento.',
]) test(`Preserve unresolved meanings: ${input}`,()=>{
  const r=write.reconstruct(input);
  const verbal=r.segments.find(s=>s.form.includes('D(E/I)'));
  assert.equal(verbal.status,'structural');
  assert.match(verbal.notes,/No se resuelve DE\/DI ni dirección/);
  assert.equal(r.metrics.semantic_coverage,0);
  assert.equal(r.metrics.infer_rate,25);
  assert.equal(r.metrics.structural_rate,25);
  assert.equal(r.metrics.official_metrics_changed,false);
  assert.ok(!r.reconstruction.includes('EKIAR'));
});

test('Fallback names are excluded from semantic coverage',()=>{
  const r=write.reconstruct('A Esteban se transfiere un documento.');
  assert.equal(r.metrics.fallback_rate,25);
  assert.equal(r.metrics.probable_rate,25);
  assert.equal(r.metrics.semantic_coverage,0);
});

for(const input of ['Esteban hizo esto.','Esteban dedicó un monumento.','Bastubar recibió un documento.'])
 test(`Unsupported meanings abstain: ${input}`,()=>{
  const r=write.reconstruct(input);
  assert.equal(r.status,'CONTROLLED_ABSTENTION');
  assert.equal(r.metrics.semantic_coverage,0);
  assert.equal(r.metrics.gap_rate,100);
  assert.ok(!/EKIAR|EGIAR|BI-D/.test(r.reconstruction));
 });

test('Empty input abstains without fabricated coverage',()=>{
  const r=write.reconstruct('');
  assert.equal(r.metrics.total_segments,0);
  assert.equal(r.metrics.semantic_coverage,0);
});

for(const input of [
  'No se entrega un documento a Bastubar.',
  'Nunca se transfiere un documento a Bastubar.',
  'Bastubar entrega un documento a Esteban.',
  'Bastubar entrega un documento.',
  '¿Se entrega un documento a Bastubar?',
  'Se entrega un documento a Bastubar?',
  'Si se entrega un documento a Bastubar.',
  'A Bastubar se entrega un documento ayer.',
  'A Bastubar se entrega un documento y se paga.',
  'A Bastubar; se entrega un documento.',
  'A nadie se entrega un documento.',
  'A quién se entrega un documento.',
  'Se entrega un documento a ella.',
]) test(`Unsupported roles or scope abstain: ${input}`,()=>{
  const r=write.reconstruct(input);
  assert.equal(r.status,'CONTROLLED_ABSTENTION');
  assert.equal(r.metrics.semantic_coverage,0);
  assert.equal(r.reconstruction,'◇SEMANTIC_FRAME');
});

test('Recipient must occur in explicit passive recipient position',()=>{
  const r=write.reconstruct('Se entrega un texto a Bastubar.');
  assert.equal(r.status,'PARTIAL_RECONSTRUCTION');
  assert.equal(r.segments[0].form,'BASTUBAR-ER');
});

test('Missing recipient remains a gap',()=>{
  const r=write.reconstruct('Se entrega un documento.');
  assert.equal(r.segments[0].form,'◇RECIPIENT');
  assert.equal(r.metrics.gap_rate,25);
});

test('Accented recipient remains a marked modern fallback',()=>{
  const r=write.reconstruct('A María se transfiere una inscripción.');
  assert.equal(r.segments[0].form,'MARIA-ER');
  assert.equal(r.segments[0].status,'fallback');
});


test('Unsupported Spanish receives traceable Iberian-sign phonographic fallback',()=>{
  const r=write.reconstruct('Esteban vende hierro.');
  assert.equal(r.status,'CONTROLLED_ABSTENTION');
  assert.equal(r.fallback.mode,'WRITE_FALLBACK_PHONOGRAPHIC');
  assert.equal(r.fallback.semantic_translation,false);
  assert.deepEqual(
    r.fallback.words.map(w=>w.tokens.map(t=>t.value)),
    [['e','s','te','ba','n'],['be','n','te'],['i','e','ŕ','o']]
  );
  assert.match(r.fallback.label,/no traducción ibérica/i);
});

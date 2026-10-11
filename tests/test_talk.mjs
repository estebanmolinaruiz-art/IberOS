import test from 'node:test';
import assert from 'node:assert/strict';
import {readFile} from 'node:fs/promises';
import {analyzeTalk,prepareSyntheticPlayback} from '../site/talk/iberos-talk.mjs';
import {IberOSWrite} from '../site/write/iberos-write.mjs';

test('Documented forms allow an explicitly provisional demo, never production',()=>{
  const p=prepareSyntheticPlayback('EKIAR KUTUR SALIR');
  assert.equal(p.allowed,true);
  assert.equal(p.text,'ekiar kutur salir');
  assert.equal(p.production_whole_word_ready,false);
  assert.equal(p.historical_pronunciation_validated,false);
  assert.ok(p.analysis.tokens.every(t=>t.category==='UNKNOWN'));
});

for(const input of ['BI-D(E/I)-ŔOK-(AN)','(TE?)','◇SEMANTIC_FRAME','[EKIAR]','SETEBANE','EKIAR DESCONOCIDO'])
 test(`No synthetic playback of unresolved input: ${input}`,()=>{
  const p=prepareSyntheticPlayback(input);
  assert.equal(p.allowed,false);
  assert.equal(p.text,null);
  assert.equal(p.production_whole_word_ready,false);
 });

test('Notation is not split into guessed historical words',()=>{
  const a=analyzeTalk('BI-D(E/I)-ŔOK-(AN)');
  assert.equal(a.tokens.length,1);
  assert.equal(a.tokens[0].form,'BI-D(E/I)-ŔOK-(AN)');
  assert.equal(a.tokens[0].state,'BLOCKED_NOTATION');
});

test('Rhotic and sibilant variants are not neutralized',()=>{
  const a=analyzeTalk('ROK ŔOK SALIR ŚALIR');
  assert.deepEqual(a.tokens.map(t=>t.form),['ROK','ŔOK','SALIR','ŚALIR']);
  assert.equal(a.tokens[1].state,'UNRECOGNIZED_FORM');
  assert.equal(a.tokens[3].state,'UNRECOGNIZED_FORM');
  assert.equal(prepareSyntheticPlayback('ROK ŔOK').allowed,false);
});

test('Write reconstruction and abstention cannot bypass Talk guard',async()=>{
  globalThis.document={baseURI:'https://example.invalid/write/'};
  const w=new IberOSWrite();
  w.rules=JSON.parse(await readFile(new URL('../site/write/data/write-rules.json',import.meta.url)));
  w.ready=true;
  for(const text of ['A Bastubar se transfiere un documento.','No se entrega un texto a Bastubar.'])
    assert.equal(prepareSyntheticPlayback(w.reconstruct(text).reconstruction).allowed,false);
});

test('Empty input remains silent and authority unchanged',()=>{
  const p=prepareSyntheticPlayback('');
  assert.equal(p.allowed,false);
  assert.equal(p.reason,'EMPTY_INPUT');
  assert.equal(p.analysis.authority.semantic_release,'C594');
  assert.equal(p.analysis.approved_whole_words,0);
  assert.equal(p.analysis.official_metrics_changed,false);
});

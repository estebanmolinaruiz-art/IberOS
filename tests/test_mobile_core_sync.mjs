import test from 'node:test';
import assert from 'node:assert/strict';
import {loadMobileCoreStatus,showMobileCoreStatus} from '../site/assets/mobile-core-sync.mjs';
const good={schema:'IberOS-Mobile-Bundle/1.0',object_count:38,authority:{semantic_release:'C594'},objects:Object.fromEntries(Array.from({length:38},(_,i)=>['IBR-X-'+String(i).padStart(4,'0'),{automatic_core_promotion:false,translation_validated:false}]))};
test('loads scientifically safe shared bundle',async()=>{
 const result=await loadMobileCoreStatus('x',async()=>({ok:true,json:async()=>good}));
 assert.equal(result.object_count,38);
});
test('rejects promoted or incomplete scientific data',async()=>{
 const broken=structuredClone(good);broken.objects['IBR-X-0000'].translation_validated=true;
 await assert.rejects(loadMobileCoreStatus('x',async()=>({ok:true,json:async()=>broken})));
});
test('fails safely in offline mode',async()=>{
 const el={textContent:''};
 const report=await showMobileCoreStatus(el,'x',async()=>{throw Error('offline')});
 assert.equal(report,null);
 assert.match(el.textContent,/no disponible/);
});

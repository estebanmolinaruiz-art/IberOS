import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';

test('Dataset JSON-LD never uses a WebSite as isPartOf',()=>{
  const html=readFileSync('site/index.html','utf8');
  const blocks=[...html.matchAll(/<script\s+type="application\/ld\+json">([\s\S]*?)<\/script>/gi)];
  assert.ok(blocks.length,'Home JSON-LD exists');
  const nodes=blocks.flatMap(x=>{
    const document=JSON.parse(x[1]);
    return Array.isArray(document['@graph'])?document['@graph']:[document];
  });
  const dataset=nodes.filter(x=>x['@type']==='Dataset');
  assert.ok(dataset.length,'Home must retain real Dataset metadata');
  for(const node of dataset){
    assert.ok(typeof node.name==='string'&&node.name.length>0);
    assert.ok(typeof node.description==='string'&&node.description.length>=50);
    assert.ok(node.creator&&node.license,'Retain creator and license');
    if(node.isPartOf!==undefined){
      const parents=Array.isArray(node.isPartOf)?node.isPartOf:[node.isPartOf];
      for(const parent of parents){
        assert.ok(typeof parent==='string'&&/^https:\/\//.test(parent)||
          parent&&parent['@type']==='Dataset'&&typeof parent.name==='string'&&typeof parent.description==='string',
          'For Google Dataset isPartOf must be URL or a full Dataset, never WebSite');
      }
    }
  }
});

test('Dataset still points to the public corpus page',()=>{
  const html=readFileSync('site/index.html','utf8');
  assert.match(html,/"@type":"Dataset"/);
  assert.match(html,/"url":"https:\/\/estebanmolinaruiz-art.github.io\/IberOS\/corpus\/"/);
  assert.match(html,/"license":"https:\/\/github.com\/estebanmolinaruiz-art\/IberOS\/blob\/main\/LICENSE_POLICY.md"/);
});

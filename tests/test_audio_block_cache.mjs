import assert from 'node:assert/strict';
import { test } from 'node:test';
import { AudioBlockCache } from '../ailectures/static/audio-cache.mjs';

test('prefetch fills consecutive blocks before a transition and reuses their bytes',async()=>{
  const requests=[],revoked=[];
  const cache=new AudioBlockCache({fetch:async(url)=>{requests.push(url);return {ok:true,headers:new Map(),blob:async()=>({size:512,id:url})}},urls:{createObjectURL:blob=>'blob:'+blob.id,revokeObjectURL:url=>revoked.push(url)}});
  const rec={id:'one',segments:[0,1,2,3].map(index=>({index,url:'/audio/'+index}))};
  cache.prefetch(rec,0);
  await cache.pending('/audio/2');
  assert.deepEqual(requests,['/audio/1','/audio/2']);
  assert.equal(cache.cached('/audio/1'),'blob:/audio/1');
  cache.prefetch(rec,1); await cache.pending('/audio/3');
  assert.deepEqual(requests,['/audio/1','/audio/2','/audio/3']);
  cache.prefetch(rec,2);
  assert(revoked.includes('blob:/audio/1'));
  cache.reset('two');assert.equal(cache.entries.size,0);
});
test('failed, cancelled and oversized downloads fall back without skipping blocks',async()=>{
  let release;
  const gate=new Promise(resolve=>release=resolve);
  const revoked=[];
  const cache=new AudioBlockCache({fetch:async()=>{await gate;return {ok:true,headers:new Map(),blob:async()=>({size:999})}},maxBytes:512,urls:{createObjectURL:()=>{throw Error('too large')},revokeObjectURL:url=>revoked.push(url)}});
  const rec={id:'one',segments:[{index:1,url:'/one'}]};
  cache.prefetch(rec,0);const pending=cache.pending('/one');cache.close();release();
  assert.equal(await pending,null);assert.equal(cache.entries.size,0);
});

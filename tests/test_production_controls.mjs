import assert from 'node:assert/strict';
import { ProductionPanel } from '../ailectures/static/production.mjs';

const control = {dataset:{cancelJob:'job'},disabled:false,textContent:'Cancel'};
const messages = [];
const panel = new ProductionPanel({message:(message)=>messages.push(message)});
panel.root = {querySelectorAll:()=>[control]};
let refreshes = 0;
panel.showJobs = async ()=>{refreshes++;};
let finish;
let requests = 0;
globalThis.fetch = (url,options)=>{
  requests++;
  assert.ok(url.endsWith('/jobs/job'));
  assert.equal(options.method,'DELETE');
  return new Promise(resolve=>{finish=resolve;});
};
const pending = panel.cancelJob('job');
assert.equal(control.disabled,true);
assert.notEqual(control.textContent,'Cancel');
assert.ok(panel.cancelling.has('job'));
await panel.cancelJob('job');
assert.equal(requests,1);
finish({ok:true,json:async()=>({id:'job',state:'cancelled'})});
await pending;
assert.equal(panel.cancelling.has('job'),false);
assert.equal(refreshes,1);
assert.equal(messages.length,0);

globalThis.fetch = async ()=>({ok:false,status:503,json:async()=>({error:'Service unavailable'})});
await panel.cancelJob('job');
assert.equal(panel.cancelling.has('job'),false);
assert.ok(panel.cancelErrors.has('job'));
assert.deepEqual(messages,['Service unavailable']);
console.log('Cancellation feedback, duplicate-click handling, and visible request errors passed');

import assert from 'node:assert/strict';
import {narratorInventory, resumeTarget, voiceGroups, lectureGenerations, LectureAudio, blockWindow, coversBlocks, preferredNarrator} from '../ailectures/static/lecture-audio.mjs';
import {Player} from '../ailectures/static/player.mjs';

const installed = {id:'other-recording',variant:'other',complete:true,pages:['One.','Two.'],segments:[{index:0,duration:2},{index:1,duration:3}]};
const row = {id:'stories:001000',revision:'current',spoken_sha256:'spoken',recordings:[installed],title:'Story',origin:{release:'source'}};
const choice = {profile:'kokoro',voice:'af_alloy',speed:1,variant:'selected'};
assert.equal(resumeTarget(row,{spoken_sha256:'older',anchor_word:3},['One.','Two.']),null);
assert.equal(resumeTarget(row,{spoken_sha256:'spoken',anchor_word:3},['One two.','Three four.']).index,1);
const pending = {id:'job',lecture_id:row.id,revision:row.revision,variant:'selected',speed:1,inventory:{states:['ready','rendering']}};
assert.deepEqual(narratorInventory(choice,row,[],['One.','Two.']).states,['missing','missing']);
assert.deepEqual(narratorInventory(choice,row,[{...pending,revision:'old'}],['One.','Two.']).states,['missing','missing']);
assert.deepEqual(narratorInventory(choice,row,[pending],['One.','Two.']).states,['ready','rendering']);
assert.equal(narratorInventory({...choice,recording_id:installed.id},row,[pending],[]).recording,installed);

const elements = new Map();
const element = (id) => {
  if (!elements.has(id)) elements.set(id,{value:'1',textContent:'',hidden:false});
  return elements.get(id);
};
const audio = {
  currentTime:0,paused:true,src:null,
  pause(){this.paused=true;},load(){},
  removeAttribute(name){this[name]=null;},getAttribute(name){return this[name];},
  play(){this.paused=false;return Promise.resolve();},
};
elements.set('audio',audio);
globalThis.document = {getElementById:element,querySelector:()=>null};
globalThis.window = {addEventListener(){}};
globalThis.localStorage = {getItem:()=>null,setItem(){}};
const player = new Player({checkpoint(){},message(){},next(){}});
player.open(row,null,installed.id);
assert.equal(player.recording,installed);
// An explicit ungenerated selection must clear another available narrator.
player.open(row,null,false);
assert.equal(player.recording,null);
assert.equal(audio.src,null);
let requested = null;
player.requestMissing = (index,seconds) => {requested={index,seconds};};
player.play(0,0);
assert.deepEqual(requested,{index:0,seconds:0});
assert.equal(audio.paused,true);
const partial = {...installed,id:'selected-recording',complete:false,segments:[{index:0,duration:2,url:'/selected/0'}]};
requested = null;
player.open({...row,recordings:[partial]},{spoken_sha256:'spoken',recording_id:partial.id,segment:1,seconds:0.5},partial.id);
assert.equal(requested,null); // Opening a page is never an implicit generation request.
player.play(1,0.5);
assert.deepEqual(requested,{index:1,seconds:0.5});
assert.equal(audio.paused,true);
console.log('Voice-specific readiness, explicit selection, and missing-block requests passed');


// A discovered catalog should not flood the primary selector.
const catalogChoices = [
  {...choice,key:'kokoro-default',profile_default:true},
  {key:'prepared',label:'Prepared voice',recording_id:installed.id},
  ...Array.from({length:50},(_,index)=>({key:'extra-'+index,profile:'kokoro',variant:'extra-'+index})),
];
const shortlist = voiceGroups(catalogChoices,row,[],['One.','Two.'],'kokoro-default');
assert.deepEqual(shortlist.flatMap(group=>group.choices.map(choice=>choice.key)),['prepared','kokoro-default']);
assert.ok(voiceGroups(catalogChoices,row,[],['One.','Two.'],'extra-20').some(group=>group.choices.some(choice=>choice.key==='extra-20')));
const unrelated = {...pending,id:'unrelated',lecture_id:'another:001000',state:'running'};
const anotherVoice = {...pending,id:'another-voice',variant:'different',revision:'previous',state:'running'};
const stopped = {...pending,id:'stopped',state:'cancelled'};
assert.deepEqual(lectureGenerations([unrelated,anotherVoice,stopped],row.id).map(job=>job.id),['another-voice']);
assert.deepEqual(lectureGenerations([stopped],row.id,new Set(['stopped'])).map(job=>job.id),['stopped']);

// Stopping another voice must target its job without changing playback or pending play.
const controller = Object.create(LectureAudio.prototype);
Object.assign(controller,{row,choices:[{...choice,key:'selected'}],select:{value:'selected'},
  jobs:[anotherVoice],stopping:new Set(),recentlyStopped:new Set(),epoch:7,pending:{index:1},
  player:{audio:{pause(){throw new Error('Cancelling another voice paused playback');}}},
  render(){},generationList(){},async poll(){},message(){}});
let cancelledURL;
globalThis.fetch = async (url,options)=>{
  cancelledURL=url;
  assert.equal(options.method,'DELETE');
  return {ok:true,json:async()=>({id:anotherVoice.id,state:'cancelled'})};
};
await controller.cancel(anotherVoice);
assert.ok(cancelledURL.endsWith('/another-voice'));
assert.equal(controller.jobs[0].state,'cancelled');
assert.deepEqual(controller.pending,{index:1});
assert.equal(controller.epoch,7);
assert.ok(controller.recentlyStopped.has(anotherVoice.id));
console.log('Voice shortlist and cancellation independent of the selected voice passed');

assert.deepEqual(blockWindow(3,10),[3]);
assert.deepEqual(blockWindow(3,10,2),[3,4,5]);
assert.deepEqual(blockWindow(8,10,2),[8,9]);
assert.deepEqual(blockWindow(0,20,-1),[0]);
assert.ok(coversBlocks({state:'running',requested_blocks:[1,2]},[2]));
assert.ok(coversBlocks({state:'running',requested_blocks:null},[5]));
assert.equal(coversBlocks({state:'cancelled',requested_blocks:null},[5]),false);
assert.equal(coversBlocks({state:'ready',requested_blocks:[1]},[2]),false);
// The same end-of-block event composes with the continuation checkbox.
let playedNext=null;
player.save=()=>{};
player.play=(index)=>{playedNext=index;};
player.index=0;
player.continueBlocks=()=>false;
audio.onended();
assert.equal(playedNext,null);
player.continueBlocks=()=>true;
audio.onended();
assert.equal(playedNext,1);
console.log('One-block default, bounded lookahead, and opt-in continuation passed');

const sparse={...installed,id:'sparse',complete:false,segments:[installed.segments[0]]};
assert.deepEqual(narratorInventory({...choice,recording_id:sparse.id},{...row,recordings:[sparse]},[{...pending,inventory:{states:['missing','ready']}}],['One.','Two.']).states,['ready','ready']);

// A new voice can submit while the previous voice's request is still returning.
const comparison = Object.create(LectureAudio.prototype);
const voices = [{...choice,key:'first'}, {...choice,key:'second',profile:'alternate',voice:'am_echo',variant:'alternate'}];
Object.assign(comparison,{row,choices:voices,select:{value:'first'},jobs:[],views:new Map(),epoch:0,
  data:{tools_available:true},pages:['One.','Two.'],cache:{},continueBlocks:{checked:false},
  player:{row:null,index:0,recording:null,open(next){this.row=next;},position(){return null;}},
  render(){},message(){}});
comparison.choose(false);
const replies=[];
globalThis.fetch = async (url,options)=>new Promise(resolve=>replies.push({resolve,payload:JSON.parse(options.body)}));
const firstRequest=comparison.prepare(false,[1]);
comparison.select.value='second';
comparison.choose();
const secondRequest=comparison.prepare(false,[1]);
assert.equal(replies.length,2);
const receipt=(id,selected)=>({id,lecture_id:row.id,revision:row.revision,variant:selected.variant,speed:1,state:'queued',requested_blocks:[1],inventory:{states:['missing','queued']}});
replies[0].resolve({ok:true,json:async()=>receipt('first',voices[0])});
await firstRequest;
assert.equal(comparison.submitting,true);
replies[1].resolve({ok:true,json:async()=>receipt('second',voices[1])});
await secondRequest;
assert.equal(comparison.submitting,false);
assert.equal(replies[1].payload.profile,'alternate');
console.log('Rapid voice switching keeps both scoped generation requests responsive');

const primary = {key:'preferred',profile:'preferred',profile_default:true,recording_id:'partial',aliases:['recording:old-import']};
const readyOther = {key:'other',profile:'other',profile_default:true,recording_id:'full',recording_complete:true};
assert.equal(preferredNarrator([readyOther,primary],{preferred_profile:'preferred',default_profile:'preferred'}).key,'preferred');
assert.equal(preferredNarrator([readyOther,primary],{preferred_profile:'preferred'},{remembered:'other'}).key,'other');
assert.equal(preferredNarrator([readyOther,primary],{preferred_profile:'preferred'},{remembered:'recording:old-import'}).key,'preferred');
assert.equal(preferredNarrator([primary,readyOther],{}).key,'other');
console.log('Configured audio defaults and remembered legacy voices retain generation controls');

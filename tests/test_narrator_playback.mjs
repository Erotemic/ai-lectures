import assert from 'node:assert/strict';
import {narratorInventory, resumeTarget, voiceGroups, lectureGenerations, LectureAudio} from '../ailectures/static/lecture-audio.mjs';
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

import assert from 'node:assert/strict';
import {narratorInventory, resumeTarget} from '../ailectures/static/lecture-audio.mjs';
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

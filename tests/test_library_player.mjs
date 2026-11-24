import assert from 'node:assert/strict';
import {Player,pageDurations,locateTime} from '../ailectures/static/player.mjs';
const complete={pages:['first passage','middle passage','last passage'],segments:[{index:0,duration:10},{index:1,duration:20},{index:2,duration:30}]};
assert.deepEqual(pageDurations(complete),[10,20,30]);
assert.deepEqual(locateTime([10,20,30],15),{index:1,seconds:5});
assert.deepEqual(locateTime([10,20,30],10),{index:1,seconds:0});
assert.deepEqual(locateTime([10,20,30],60),{index:2,seconds:30});
assert.deepEqual(locateTime([10,20,30],100),{index:2,seconds:30});
assert.deepEqual(locateTime([10,20,30],-10),{index:0,seconds:0});
const partial={pages:['first passage','one two three'],segments:[{index:0,duration:7}]};
const durations=pageDurations(partial);
assert.equal(durations[0],7);
assert.ok(durations[1]>0);
assert.deepEqual(locateTime(durations,8).index,1);
console.log('Portable player measured/estimated timeline and cross-segment seeking passed');

const elements = new Map();
const element = (id) => {
  if (!elements.has(id)) elements.set(id, {value:'1', textContent:'', checked:true});
  return elements.get(id);
};
const audio = { currentTime:0, paused:true, duration:10,
  pause(){this.paused=true;}, load(){this.duration=this.src==='/second.wav'?20:10;},
  removeAttribute(name){delete this[name];}, getAttribute(name){return this[name];},
  play(){this.paused=false;return Promise.resolve();} };
elements.set('audio',audio);
globalThis.document = {getElementById:element,querySelector:()=>null};
globalThis.window = {addEventListener(){}};
globalThis.localStorage = {getItem:()=>null,setItem(){}};
const checkpoints=[],next=[];
const player=new Player({checkpoint:point=>checkpoints.push(point),message(){},next:options=>next.push(options)});
const recording={id:'recording',variant:'prepared',complete:true,pages:['First.','Second.'],segments:[{index:0,duration:10,url:'/first.wav'},{index:1,duration:20,url:'/second.wav'}]};
const row={id:'track:001000',revision:'current',spoken_sha256:'spoken',title:'First lecture',recordings:[recording],origin:{release:'source'}};
player.open(row,null,recording.id,'track:branch');
assert.equal(player.revealed,false);
audio.onloadedmetadata();player.started=true;audio.currentTime=4;
player.open(row,null,recording.id,'track:survey');
assert.equal(checkpoints.at(-1).course_id,'track:branch');
assert.equal(player.position().course_id,'track:survey');
assert.equal(audio.currentTime,4);
assert.equal(audio.src,'/first.wav');
player.continueBlocks=()=>false;
audio.onended();assert.equal(next.length,0);assert.equal(player.index,0);
player.index=1;
audio.onended();assert.deepEqual(next,[{automatic:true}]);
element('continue-course').checked=false;
audio.onended();assert.equal(next.length,1);
player.index=0;audio.currentTime=8;audio.paused=true;
player.seekBy(15);assert.equal(player.index,1);audio.onloadedmetadata();
assert.equal(audio.currentTime,13);assert.equal(audio.paused,true);
player.seekBy(-15);assert.equal(player.index,0);audio.onloadedmetadata();
assert.equal(audio.currentTime,8);
const timeline=element('timeline');
timeline.value='2000';
timeline.oninput();
assert.equal(element('elapsed').textContent,'0:06');
player.update();
assert.equal(timeline.value,'2000');
timeline.onchange();
assert.equal(audio.currentTime,6);
assert.equal(audio.paused,true);
// Selecting an unavailable passage while paused must clear the previous audio.
player.recording={...recording,complete:false,segments:[recording.segments[0]]};
player.seekBy(15);assert.equal(player.index,1);assert.equal(audio.src,undefined);
assert.equal(player.ready,false);
console.log('Final-block continuation, playback context and paused cross-block seeking passed');

// Both controls read the actual media state; a paused resume keeps its time.
player.lectureController = {syncPlayback(){this.label=element('toggle-play').textContent;}};
audio.paused=false; audio.onplay();
assert.equal(player.revealed,true);
assert.equal(element('toggle-play').textContent,'Pause');
assert.equal(player.lectureController.label,'Pause');
audio.pause();audio.onpause();
assert.equal(element('toggle-play').textContent,'Resume');
assert.equal(player.lectureController.label,'Resume');
let cancelled=0;
player.lectureController.pending={index:1};
player.lectureController.cancelPlayback=()=>{cancelled++;player.lectureController.pending=null;};
player.syncControls();assert.equal(element('toggle-play').textContent,'Cancel playback');
player.toggle();assert.equal(cancelled,1);
console.log('Shared playback controls follow media events and can cancel pending playback');

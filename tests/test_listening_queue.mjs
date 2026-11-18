import assert from "node:assert/strict";
import { ListeningQueue, editDeviceQueue } from "../ailectures/static/queue.mjs";

const one = { id: "one", lecture_id: "music:001000" },
  two = { id: "two", lecture_id: "history:001000" },
  three = { id: "three", lecture_id: "music:002000" };
let queue = editDeviceQueue([], { action: "add", entry: one });
queue = editDeviceQueue(queue, { action: "add", entry: two });
queue = editDeviceQueue(queue, { action: "add", entry: three });
assert.deepEqual(editDeviceQueue(queue, { action: "add", entry: one }), queue);
assert.deepEqual(
  editDeviceQueue(queue, { action: "move", id: "three", before: "one" }),
  [three, one, two],
);
assert.deepEqual(
  editDeviceQueue(queue, { action: "move", id: "one", before: null }),
  [two, three, one],
);
assert.deepEqual(editDeviceQueue(queue, { action: "remove", id: "two" }), [
  one,
  three,
]);
assert.throws(() =>
  editDeviceQueue(queue, { action: "move", id: "one", before: "removed" }),
);
console.log(
  "Device queue retains identities during additions, moves and removals",
);

let selected='listener',played=[],messages=[],edits=0;
const controller=new ListeningQueue({profile:()=>selected,lectures:()=>[one,two,three].map(entry=>({id:entry.lecture_id})),
  play:(entry,automatic)=>played.push({entry,automatic}),message:text=>messages.push(text)});
controller.read=async()=>[one,two,three];
controller.edit=async(operation,profile)=>{assert.equal(profile,'listener');edits++;return [two,three];};
await controller.advance(one.id,true);
assert.deepEqual(played,[{entry:two,automatic:true}]);
// A listener switch while consumption is in flight must not play their old queue.
played=[];
controller.edit=async()=>{selected='other';return [two,three];};
await controller.advance(one.id,true);assert.equal(played.length,0);
selected='listener';
controller.edit=async()=>[three];
await controller.advance(one.id,true);assert.equal(played.length,0);assert.equal(controller.advancing,false);
// Rapid Next taps and an ended event share one outstanding advance.
let finish;
controller.edit=async()=>{edits++;return new Promise(resolve=>{finish=resolve;});};
const pending=controller.advance(one.id,true);
await Promise.resolve();const before=edits;
await controller.advance(one.id,true);assert.equal(edits,before);
finish([two,three]);await pending;assert.equal(played.length,1);
// A presentation is an explicit navigation step, not implicit audio playback.
controller.lectures=()=>[{id:two.lecture_id,kind:'presentation'}];
controller.edit=async()=>{throw Error('Automatic presentation transition consumed the queue');};
await controller.advance(one.id,true);
assert.equal(played.length,1);
console.log('Queue continuation retains listener identity and handles concurrent edits and presentations');

// Previous restores a consumed occurrence, keeping Next's queue order intact.
let entries=[one,three,two];
const navigation=new ListeningQueue({profile:()=>null,lectures:()=>[one,two,three].map(entry=>({id:entry.lecture_id})),play:entry=>{played.push(entry);},message:text=>messages.push(text)});
navigation.read=async()=>entries;
navigation.edit=async operation=>(entries=editDeviceQueue(entries,operation));
assert.equal(navigation.previousEntry(entries,one.id),null);
await navigation.advance(one.id);
assert.deepEqual(entries,[three,two]);
assert.equal(navigation.previousEntry(entries,three.id).id,one.id);
await navigation.previous(three.id);
assert.deepEqual(entries,[one,three,two]);
assert.equal(played.at(-1).id,one.id);
await navigation.advance(one.id);
assert.equal(played.at(-1).id,three.id);
assert.equal(navigation.previousEntry(entries,three.id,'another-listener'),null);
console.log('Previous restores consumed queue items and keeps history scoped to the listener');

import assert from "node:assert/strict";
import { editDeviceQueue } from "../ailectures/static/queue.mjs";

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

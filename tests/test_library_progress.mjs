import assert from "node:assert/strict";
import { test } from "node:test";
import { getStored, store } from "../ailectures/static/api.mjs";
import {
  ProgressSync,
  mergeSharedProgress,
} from "../ailectures/static/progress.mjs";

const lecture = "music:001000";
const point = (sequence, expected_version, extra = {}) => ({
  lecture_id: lecture,
  update_id: "update-" + sequence,
  device_id: "browser",
  sequence,
  expected_version,
  seconds: sequence * 10,
  ...extra,
});
const accepted = (payload) => ({
  ...payload,
  version: payload.expected_version + 1,
});
const response = (data, status = 200) => ({
  ok: status < 400,
  status,
  json: async () => data,
});
const deferred = () => {
  let resolve;
  const promise = new Promise((done) => { resolve = done; });
  return { promise, resolve };
};

function setup(send) {
  const data = new Map();
  globalThis.localStorage = {
    getItem: (key) => data.get(key) ?? null,
    setItem: (key, value) => data.set(key, value),
  };
  const calls = [], conflicts = [], errors = [], saved = [];
  globalThis.fetch = async (url, options) => {
    const payload = JSON.parse(options.body);
    calls.push({ url, payload });
    return send(payload, calls.length);
  };
  const sync = new ProgressSync({
    onSaved: (profile, state) => saved.push({ profile, state }),
    onConflict: (conflict) => conflicts.push(conflict),
    onError: (error) => errors.push(error),
  });
  return { sync, calls, conflicts, errors, saved };
}

function enqueue(profile, payload) {
  const state = getStored("progress:" + profile, {});
  state[payload.lecture_id] = accepted(payload);
  store("progress:" + profile, state);
  store("pending:" + profile, [
    ...getStored("pending:" + profile, []),
    payload,
  ]);
}

test("a stale GET cannot roll back a checkpoint saved while it was in flight", () => {
  const stale = accepted(point(1, 8));
  const newer = accepted(point(2, 9));
  assert.deepEqual(
    mergeSharedProgress({ [lecture]: stale }, { [lecture]: newer }, []),
    { [lecture]: newer },
  );
  // The following checkpoint must expect version 10, not the GET's version 9.
  assert.equal(mergeSharedProgress(
    { [lecture]: stale }, { [lecture]: newer }, [],
  )[lecture].version, 10);
});

test("a GET preserves queued rewinds even when shared progress is newer", () => {
  const queued = point(2, 1, { seconds: 3 });
  const local = accepted(queued);
  const shared = accepted(point(5, 20));
  assert.equal(mergeSharedProgress(
    { [lecture]: shared }, { [lecture]: local }, [queued],
  )[lecture], local);
  assert.equal(mergeSharedProgress(
    { [lecture]: shared }, { [lecture]: local }, [],
  )[lecture], shared);
  assert.equal(mergeSharedProgress({}, {}, [point(1, 0), queued])[lecture], queued);
});

test("conflicts pause polling and checkpoint retries without losing queued positions", async () => {
  const current = accepted(point(1, 8));
  const { sync, calls, conflicts } = setup((payload) => response({
    conflict: true, current, alternate: payload,
  }, 409));
  const first = point(2, 8);
  enqueue("listener", first);
  await sync.flush("listener");
  enqueue("listener", point(3, 9));
  for (let poll = 0; poll < 5; poll++) await sync.flush("listener");
  assert.equal(calls.length, 1);
  assert.equal(conflicts.at(-1).payload.update_id, first.update_id);
  assert.equal(getStored("pending:listener").length, 2);
  assert.equal(getStored("progress:listener")[lecture].sequence, 3);

  // Another listener is independent of the paused queue.
  enqueue("other", point(1, 0));
  await sync.flush("other");
  assert.equal(calls.length, 2);
  assert.equal(conflicts.at(-1).profile, "other");
});

test("choosing local resets optimistic versions before new checkpoints arrive", async () => {
  const gate = deferred();
  const current = accepted(point(1, 8));
  const { sync, calls, conflicts } = setup((payload, call) => {
    if (call === 1) return response({ conflict: true, current }, 409);
    if (call === 2) return gate.promise;
    return response(accepted(payload));
  });
  enqueue("listener", point(2, 8));
  await sync.flush("listener");
  // Several checkpoints accumulate while the conflict is displayed.
  enqueue("listener", point(3, 9));
  enqueue("listener", point(4, 10));
  const unrelated = point(5, 0, { lecture_id: "music:002000" });
  enqueue("listener", unrelated);
  const local = point(6, current.version, { seconds: 40 });
  sync.useLocal(conflicts[0], local);
  assert.equal(getStored("progress:listener")[lecture].version, 10);
  assert.deepEqual(getStored("pending:listener"), [local, unrelated]);

  const flushing = sync.flush("listener");
  const next = point(7, getStored("progress:listener")[lecture].version);
  enqueue("listener", next);
  gate.resolve(response(accepted(local)));
  await flushing;
  assert.deepEqual(calls.map(({ payload }) => payload.update_id), [
    "update-2", "update-6", "update-5", "update-7",
  ]);
  assert.equal(calls.at(-1).payload.expected_version, 10);
  assert.equal(getStored("progress:listener")[lecture].version, 11);
  assert.deepEqual(getStored("pending:listener"), []);
});

test("choosing shared drops only that lecture and resumes the rest of the queue", async () => {
  const current = accepted(point(1, 8));
  const { sync, calls, conflicts } = setup((payload, call) => call === 1
    ? response({ conflict: true, current }, 409)
    : response(accepted(payload)));
  enqueue("listener", point(2, 8));
  await sync.flush("listener");
  enqueue("listener", point(3, 9));
  const other = point(4, 0, { lecture_id: "music:002000" });
  enqueue("listener", other);
  sync.keepShared(conflicts[0]);
  assert.deepEqual(getStored("progress:listener")[lecture], current);
  await sync.flush("listener");
  assert.equal(calls.length, 2);
  assert.deepEqual(calls[1].payload, other);
  assert.deepEqual(getStored("pending:listener"), []);
});

test("choosing an absent shared position removes the local checkpoint", async () => {
  const { sync, conflicts } = setup(() => response({ conflict: true, current: null }, 409));
  enqueue("listener", point(1, 0));
  await sync.flush("listener");
  sync.keepShared(conflicts[0]);
  assert.deepEqual(getStored("progress:listener"), {});
  assert.deepEqual(getStored("pending:listener"), []);
});

test("concurrent flushes share a request and retain checkpoints added in flight", async () => {
  const gate = deferred(), nextGate = deferred();
  const { sync, calls } = setup((payload, call) => call === 1
    ? gate.promise : nextGate.promise);
  const first = point(1, 0);
  enqueue("listener", first);
  const flushing = sync.flush("listener");
  assert.equal(sync.flush("listener"), flushing);
  const second = point(2, 1);
  enqueue("listener", second);
  gate.resolve(response(accepted(first)));
  // Let the first response drain and the second POST start.
  await new Promise((resolve) => setImmediate(resolve));
  assert.equal(calls.length, 2);
  assert.equal(getStored("progress:listener")[lecture].sequence, 2);
  nextGate.resolve(response(accepted(second)));
  await flushing;
  assert.deepEqual(getStored("pending:listener"), []);
});

test("connection failures retain stable event IDs for a later retry", async () => {
  const { sync, calls, errors } = setup((payload, call) => {
    if (call === 1) throw new Error("offline");
    return response(accepted(payload));
  });
  const pending = point(1, 0);
  enqueue("listener", pending);
  await sync.flush("listener");
  assert.equal(errors.length, 1);
  assert.deepEqual(getStored("pending:listener"), [pending]);
  await sync.flush("listener");
  assert.deepEqual(calls[0].payload, calls[1].payload);
  assert.deepEqual(getStored("pending:listener"), []);
});

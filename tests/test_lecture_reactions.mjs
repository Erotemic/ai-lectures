import assert from "node:assert/strict";
import { test } from "node:test";
import { ReactionState, mergeReactions, reactionValue, migrateReactions } from "../ailectures/static/reactions.mjs";
import { getStored, store } from "../ailectures/static/api.mjs";
import { allLectureRows } from "../ailectures/static/all-lectures-model.mjs";
const row = { id: "music:001000", revision: "a".repeat(64), title: "Intervals" };
const setup = () => {
  const data = new Map();
  globalThis.localStorage = { getItem: key => data.get(key) ?? null, setItem: (key, value) => data.set(key, value) };
};
const record = (field, value, stamp = "2026-11-18T01:00:00.000Z") => ({ field, value, lecture_id: row.id, updated_at: stamp, update_id: field+stamp });

test("independent field merges preserve clearing and are order-independent", () => {
  const rating = { [row.id]: { rating: record("rating", 5) } };
  const favorite = { [row.id]: { favorite: record("favorite", true) } };
  const cleared = { [row.id]: { rating: record("rating", null, "2026-11-18T02:00:00.000Z") } };
  assert.deepEqual(mergeReactions(rating, favorite, cleared), mergeReactions(cleared, favorite, rating));
  const merged = mergeReactions(rating, favorite, cleared);
  assert.equal(reactionValue(merged, row.id, "rating"), null);
  assert.equal(reactionValue(merged, row.id, "favorite"), true);
});

test("device choices persist without a server and filters use personal values", async () => {
  setup();
  const state = new ReactionState("", { post: () => { throw Error("must stay local"); } });
  await state.set(row, "favorite", true);
  await state.set(row, "rating", 4);
  const restored = new ReactionState();
  assert.equal(restored.value(row.id, "favorite"), true);
  const rows = [row, { id: "music:002000", title: "Chords" }];
  assert.equal(allLectureRows(rows, {personal:"favorites"}, restored.records).length, 1);
  assert.equal(allLectureRows(rows, {personal:"5"}, restored.records).length, 0);
  assert.equal(allLectureRows(rows, {personal:"4"}, restored.records).length, 1);
  assert.equal(allLectureRows(rows, {personal:"unrated"}, restored.records)[0].id, "music:002000");
  assert.equal(allLectureRows(rows, {sort:"rating"}, restored.records)[0].id, row.id);
  await assert.rejects(async () => state.set(row, "rating", 6));
});

test("offline writes retry with their original ID and do not leak to another listener", async () => {
  setup();
  const sent = [];
  let offline = true;
  const state = new ReactionState("one", { post: async (url, payload) => {
    sent.push({url,payload});
    if (offline) throw Error("offline");
    return payload;
  }, api: async () => ({}) });
  await state.set(row, "rating", 3);
  await state.set(row, "favorite", true);
  assert.equal(getStored(state.pendingKey).length, 2);
  assert.equal(new ReactionState("two").value(row.id, "rating"), null);
  offline = false;
  await state.load();
  assert.equal(state.value(row.id, "rating"), 3);
  assert.equal(state.value(row.id, "favorite"), true);
  assert.equal(getStored(state.pendingKey).length, 0);
  assert.equal(sent[0].payload.update_id, sent[2].payload.update_id);
  assert(sent.every(call => call.url === "/api/listeners/one/reactions"));
});

test("edits made during a GET or POST survive its response", async () => {
  setup();
  let resolve;
  const gate = new Promise(done => { resolve = done; });
  const state = new ReactionState("one", { api: async () => gate, post: async (_, payload) => payload });
  const loading = state.load();
  await state.set(row, "rating", 5);
  resolve({});
  await loading;
  assert.equal(state.value(row.id, "rating"), 5);
  let release;
  const barrier = new Promise(done => { release = done; });
  const writes = [];
  state.post = async (_, payload) => { writes.push(payload); await barrier; return payload; };
  const first = state.set(row, "favorite", true);
  const second = state.set(row, "favorite", false);
  release();
  await Promise.all([first, second]);
  assert.equal(state.value(row.id, "favorite"), false);
  assert.equal(writes.length, 2);
  assert.equal(getStored(state.pendingKey).length, 0);
});

test("profile aliases retain independent fields and retry pending updates", () => {
  setup();
  const old = new ReactionState("old"), current = new ReactionState("current");
  const rating = record("rating", 2), favorite = record("favorite", true);
  store(old.key, { [row.id]: { rating } });
  store(old.pendingKey, [rating]);
  store(current.key, { [row.id]: { favorite } });
  migrateReactions("old", "current");
  const merged = new ReactionState("current");
  assert.equal(merged.value(row.id, "rating"), 2);
  assert.equal(merged.value(row.id, "favorite"), true);
  assert.deepEqual(getStored(merged.pendingKey), [rating]);
});

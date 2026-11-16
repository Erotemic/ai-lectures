import assert from "node:assert/strict";
import { test } from "node:test";
import { ProductionPanel, partitionJobs } from "../ailectures/static/production.mjs";

test("finished requests leave the working queue while errors remain visible", () => {
  const jobs = [
    { id: "done", state: "ready", published: "release", updated_at: 10 },
    { id: "waiting", state: "queued", created_at: 1 },
    { id: "error", state: "failed", updated_at: 5 },
    { id: "stopped", state: "cancelled", updated_at: 20 },
    { id: "changed", state: "settings_changed", updated_at: 15 },
    { id: "working", state: "running", created_at: 2 },
  ];
  const { active, attention, history } = partitionJobs(jobs);
  assert.deepEqual(active.map((job) => job.id), ["working", "waiting"]);
  assert.deepEqual(attention.map((job) => job.id), ["changed", "error"]);
  assert.deepEqual(history.map((job) => job.id), ["stopped", "done"]);
  assert.equal(active.length + attention.length + history.length, jobs.length);
  assert.equal(jobs[0].id, "done", "Partitioning does not reorder the API snapshot");
});

test("requeued jobs return to the working queue and variants retain their history", () => {
  const base = { lecture_id: "music:001000", profile: "test", voice: "speaker" };
  const old = { ...base, id: "old", revision: "old", state: "ready", updated_at: 1 };
  const current = { ...base, id: "current", revision: "current", state: "ready", updated_at: 2 };
  let result = partitionJobs([old, current]);
  assert.deepEqual(result.history, [current, old]);
  current.state = "queued";
  result = partitionJobs([old, current]);
  assert.deepEqual(result.history, [old]);
  assert.deepEqual(result.active, [current]);
});

test("unknown states stay visible and older snapshots have stable ordering", () => {
  const result = partitionJobs([
    { id: "b", state: "ready" },
    { id: "a", state: "ready" },
    { id: "unknown", state: "paused" },
  ]);
  assert.deepEqual(result.history.map((job) => job.id), ["a", "b"]);
  assert.equal(result.attention[0].id, "unknown");
  assert.deepEqual(partitionJobs([]), { active: [], attention: [], history: [] });
});

test("unchanged polls keep the existing view and stale responses cannot replace it", async () => {
  const target = { isConnected: true };
  const panel = new ProductionPanel({});
  panel.root = { isConnected: true, querySelector: () => target };
  const draws = [];
  panel.drawJobs = (element, jobs) => draws.push(jobs);
  const snapshot = [{ id: "done", state: "ready" }];
  globalThis.fetch = async () => ({ ok: true, json: async () => ({ jobs: snapshot }) });
  await panel.showJobs();
  await panel.showJobs();
  assert.equal(draws.length, 1);

  const replies = [];
  globalThis.fetch = () => new Promise((resolve) => replies.push(resolve));
  const older = panel.showJobs();
  const newer = panel.showJobs();
  const current = [{ id: "next", state: "running" }];
  replies[1]({ ok: true, json: async () => ({ jobs: current }) });
  await newer;
  replies[0]({ ok: true, json: async () => ({ jobs: snapshot }) });
  await older;
  assert.equal(draws.length, 2);
  assert.deepEqual(draws.at(-1), current);
});

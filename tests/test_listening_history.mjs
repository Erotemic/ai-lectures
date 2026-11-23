import assert from "node:assert/strict";
import { test } from "node:test";
import { recentListening, historyRoute } from "../ailectures/static/listening-history.mjs";

test("recent listening includes completed and unavailable lectures without changing progress", () => {
  const progress = {
    first: { lecture_id: "sample:first", completed: false, updated_at: "2026-11-20T10:00:00Z" },
    second: { lecture_id: "sample:second", completed: true, updated_at: "2026-11-22T10:00:00Z" },
    removed: { lecture_id: "removed:one", updated_at: "2026-11-21T10:00:00Z" },
    legacy: { lecture_id: "sample:legacy" },
  };
  const before = structuredClone(progress);
  assert.deepEqual(recentListening(progress).map((p) => p.lecture_id), [
    "sample:second", "removed:one", "sample:first", "sample:legacy",
  ]);
  assert.deepEqual(progress, before);
  assert.deepEqual(recentListening({}), []);
});

const courses = [
  { id: "sample:main", role: "main", lectures: ["sample:first", "sample:second", "sample:third"] },
  { id: "sample:alternate", lectures: ["sample:first", "sample:third", "uninstalled:next", "sample:second"] },
];

test("next lecture follows the saved track rather than catalog order or completion status", () => {
  for (const completed of [false, true]) {
    const route = historyRoute({ lecture_id: "sample:first", course_id: "sample:alternate", completed }, courses);
    assert.equal(route.course.id, "sample:alternate");
    assert.equal(route.index, 0);
    assert.equal(route.next, "sample:third");
  }
  assert.equal(historyRoute({ lecture_id: "sample:first" }, courses).course.id, "sample:main");
  assert.equal(historyRoute({ lecture_id: "sample:third", course_id: "sample:alternate" }, courses).next, "uninstalled:next");
  assert.equal(historyRoute({ lecture_id: "sample:second", course_id: "sample:alternate" }, courses).next, null);
});

test("missing routes and removed membership never invent a different playback order", () => {
  for (const position of [
    { lecture_id: "sample:first", course_id: "removed:track" },
    { lecture_id: "removed:lecture", course_id: "sample:main" },
    { lecture_id: "removed:lecture" },
  ]) assert.deepEqual(historyRoute(position, courses), { course: null, index: -1, next: null });
});

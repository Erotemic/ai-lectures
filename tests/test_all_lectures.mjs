import assert from "node:assert/strict";
import { allLectureRows } from "../ailectures/static/all-lectures-model.mjs";
import { collectionReturnPath } from "../ailectures/static/browse-model.mjs";

const rows = [
  { id: "one:z", title: "Zebra", namespace: "one", origin: {pack: "first"}, categories: ["History"], words: 290,
    tags: ["Place: London"], creators: [{name: "A writer"}], description: "Discusses memory and testimony.", recordings: [{complete: true}, {complete:false}], chronology: {work: {start: 1901}} },
  { id: "two:a", title: "Alpha", namespace: "two", categories: ["History"], words: 145,
    tags: ["Place: London"], recordings: [{complete: false}], chronology: {work:{start:-500}} },
  { id: "one:unindexed", title: "Outside every collection", namespace: "one", categories: ["Science"], words: 435, recordings: [] },
];
const before = JSON.stringify(rows);
assert.deepEqual(allLectureRows(rows).map(row => row.id), ["two:a", "one:unindexed", "one:z"]);
assert.equal(allLectureRows([...rows, rows[0]]).length, 3);
assert.equal(allLectureRows(rows, {q: "testimony"})[0].id, "one:z");
assert.equal(allLectureRows(rows, {q: "a writer"})[0].id, "one:z");
assert.equal(allLectureRows(rows, {q: "unindexed"})[0].id, "one:unindexed");
assert.equal(allLectureRows(rows, {q: "unavailable"}).length, 0);
assert.equal(allLectureRows(rows, {pack:"first"}).length, 1);
assert.equal(allLectureRows(rows, {pack:"two"}).length, 1);
assert.equal(allLectureRows(rows, {category:"History",tag:"Place: London"}).length, 2);
assert.equal(allLectureRows(rows, {tag:"London"}).length, 0);
for (const audio of ["ready", "partial", "missing"]) assert.equal(allLectureRows(rows, {audio}).length, 1);
assert.equal(allLectureRows(rows, {sort:"long"})[0].id, "one:unindexed");
assert.equal(allLectureRows(rows, {sort:"short"})[0].id, "two:a");
assert.deepEqual(allLectureRows(rows, {sort:"date-work"}).map(row => row.id), ["two:a", "one:z", "one:unindexed"]);
assert.deepEqual(allLectureRows(rows, {sort:"date-work-desc"}).map(row => row.id), ["one:z", "two:a", "one:unindexed"]);
assert.equal(JSON.stringify(rows), before);
assert.deepEqual(allLectureRows([]), []);
const origin = "https://library.example";
assert.equal(collectionReturnPath("/lectures?q=memory&show=all", null, origin), "/lectures?q=memory&show=all");
assert.equal(collectionReturnPath("/lectures?tag=Place%3A+London", "one:main", origin), "/lectures?tag=Place%3A+London");
assert.equal(collectionReturnPath("https://other.example/lectures", null, origin), null);
assert.equal(collectionReturnPath("/collections/other", "one:main", origin), null);
assert.equal(collectionReturnPath("/lectures/one/z", null, origin), null);
console.log("Flat inventory: completeness, filtering, sorting, identities, and safe return paths passed.");

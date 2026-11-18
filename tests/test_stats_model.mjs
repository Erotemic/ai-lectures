import assert from "node:assert/strict";
import { contentTotals, libraryStats } from "../ailectures/static/stats-model.mjs";

const lectures = [
  { id: "a:one", words: 145, categories: ["Math", "Science", "Math"], audiences: ["Adults"],
    origin: { pack: "a" }, recordings: [{ complete: true }, { complete: true }, { complete: false }],
    companions: [{ stale: true }, { stale: false }] },
  { id: "a:two", words: 290, categories: ["Math"], origin: { pack: "a" }, recordings: [{ complete: false }],
    companions: [{ stale: true }] },
  { id: "b:three", words: 435, categories: ["Science"], origin: { pack: "b" } },
];
const courses = [
  { id: "a:hub", title: "Hub", lectures: [] },
  { id: "a:route", parent_id: "a:hub", lectures: ["a:one", "a:one", "a:two", "missing:id"] },
  { id: "b:route", parent_id: "a:hub", lectures: ["a:one", "b:three"] },
  { id: "a:archive", parent_id: "a:hub", role: "archive", lectures: ["a:two"] },
];
const catalog = { lectures, courses, packs: [{ id: "a", title: "First" }, { id: "b", title: "Second" }, { id: "c", title: "Empty" }] };
const before = JSON.stringify(catalog);
const stats = libraryStats(catalog);
assert.equal(stats.lectures, 3);
assert.equal(stats.words, 870);
assert.equal(stats.minutes, 6);
assert.equal(stats.complete, 1, "Multiple narrators do not multiply lecture coverage");
assert.equal(stats.partial, 1, "A partial variant does not downgrade another complete variant");
assert.equal(stats.missing, 1);
assert.equal(stats.companions, 1, "Stale companions do not count as current");
assert.equal(stats.collections, 4);
assert.equal(stats.packs, 3);
assert.deepEqual(stats.subjects.map(row => [row.title, row.lectures]), [["Math", 2], ["Science", 2]]);
assert.equal(stats.audiences.reduce((sum, row) => sum + row.lectures, 0), 3);
assert.equal(stats.packRows.reduce((sum, row) => sum + row.words, 0), stats.words);
assert.equal(stats.packRows.find(row => row.id === "c").lectures, 0);
assert.equal(stats.collectionRows.find(row => row.id === "a:hub").lectures, 3);
assert.equal(stats.collectionRows.find(row => row.id === "a:route").words, 435);
assert.equal(stats.collectionRows.find(row => row.id === "a:archive").lectures, 1);
assert.equal(JSON.stringify(catalog), before, "Aggregation never mutates playback or source data");
assert.deepEqual(contentTotals([...lectures, ...lectures]), contentTotals(lectures));
assert.equal(libraryStats({}).lectures, 0);
assert.equal(libraryStats({}).minutes, 0);
assert.equal(contentTotals([{ id: "bad", words: Infinity }, { id: "bad2", words: -1 }]).words, 0);
assert.equal(libraryStats({ lectures: [{ id: "unknown:one" }] }).packRows[0].lectures, 1);
// Refresh changes availability without changing the content counts.
const updated = structuredClone(catalog);
updated.lectures[1].recordings.push({ complete: true });
const next = libraryStats(updated);
assert.equal(next.complete, 2);
assert.equal(next.lectures, stats.lectures);
assert.equal(next.words, stats.words);
assert.equal(next.complete + next.partial + next.missing, next.lectures);
console.log("Library statistics: identity, overlap, estimates, and readiness checks passed.");

const coverage = libraryStats({ lectures: [
  { id: "work:one", words: 145, places: ["Dublin", "Dublin"], periods: ["Modernism"],
    time_coverage: { work: ["20th century CE"], setting: ["20th century CE"] },
    creators: [{ name: "A writer", role: "author" }, { name: "A translator", role: "translator" }],
    tags: ["Author: A writer", "Place: Dublin"], description: "A description" },
  { id: "work:two", places: ["Dublin"], time_coverage: { work: ["20th century CE"] },
    creators: [{ name: "A writer", role: "attributed_author" }] },
] });
assert.equal(coverage.places.find(row => row.title === "Dublin").lectures, 2);
assert.equal(coverage.authors.length, 1);
assert.equal(coverage.authors[0].lectures, 2);
assert.equal(coverage.dates.work[0].lectures, 2);
assert.equal(coverage.dates.setting[0].lectures, 1);
assert.equal(coverage.withPlaces, 2);
assert.equal(coverage.withDates, 2);
assert.equal(coverage.withDescriptions, 1);

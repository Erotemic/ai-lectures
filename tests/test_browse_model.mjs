import assert from "node:assert/strict";
import {
  formatMinutes,
  collectionRows,
  collectionAncestors,
  collectionSections,
  matchesLecture,
  matchesTag,
  collectionReturnPath,
} from "../ailectures/static/browse-model.mjs";

assert.equal(formatMinutes(0), "0 min");
assert.equal(formatMinutes(59.6), "1 h");
assert.equal(formatMinutes(90.4), "1 h 30 min");
assert.equal(formatMinutes(1940), "32 h 20 min");
assert.equal(formatMinutes(-4), "0 min");
assert.equal(formatMinutes(Infinity), "0 min");
assert.equal(formatMinutes(undefined), "0 min");

const rows = new Map([
  ["sample:one", { id: "sample:one", title: "A First Idea", section: "first-part" }],
  ["sample:two", { id: "sample:two", title: "Another Idea", section: "first-part" }],
  ["sample:three", { id: "sample:three", title: "A New Direction", section: "later-part" }],
  ["sample:four", { id: "sample:four", title: "Return", section: "first-part" }],
]);
const byId = (key) => rows.get(key);
const hub = { id: "sample:hub", lectures: [] };
const nested = { id: "sample:nested", parent_id: hub.id, lectures: [] };
const first = { id: "sample:first", parent_id: nested.id, lectures: ["sample:two", "missing:one", "sample:one", "sample:two"] };
const second = { id: "sample:second", parent_id: hub.id, lectures: ["sample:three", "sample:one"] };
const archive = { id: "sample:archive", parent_id: hub.id, role: "archive", lectures: ["sample:four"] };
const archiveChild = { id: "sample:archive-child", parent_id: archive.id, lectures: ["sample:four"] };
const courses = [hub, nested, first, second, archive, archiveChild];
const before = JSON.stringify(courses);
const tagged = { id: "cross:one", title: "A distant subject", tags: ["Spectral theory", "Probability"] };
assert(matchesTag(tagged, " spectral THEORY "));
assert(!matchesTag(tagged, "Spectral"), "Tags match whole topics; keyword search remains separate");
assert(matchesLecture(tagged.id, () => tagged, "spectral"), "Keyword search includes topic tags");
assert(matchesTag(tagged, ""));
assert.deepEqual(collectionRows(hub, courses, byId).map((row) => row.id), ["sample:two", "sample:one", "sample:three"]);
assert.equal(JSON.stringify(courses), before);
assert.deepEqual(collectionRows(first, courses, byId).map((row) => row.id), ["sample:two", "sample:one"]);
assert.deepEqual(collectionRows(null, courses, byId), []);
const missingParent = { id: "sample:missing", lectures: ["missing:one"] };
assert.deepEqual(collectionRows(missingParent, [missingParent, { ...second, parent_id: missingParent.id }], byId), [], "A nonempty unavailable direct sequence is not replaced by children");
const cyclic = [{ id: "cycle:a", parent_id: "cycle:b", lectures: [] }, { id: "cycle:b", parent_id: "cycle:a", lectures: [] }];
assert.deepEqual(collectionRows(cyclic[0], cyclic, byId), []);

assert.deepEqual(collectionAncestors(first, courses).map((course) => course.id), [hub.id, nested.id]);
assert.deepEqual(collectionAncestors(hub, courses), []);
assert.deepEqual(collectionAncestors({ id: "absent", parent_id: "unavailable" }, courses), []);
assert.deepEqual(collectionAncestors(cyclic[0], cyclic).map((course) => course.id), ["cycle:b"]);

const ordered = { lectures: ["sample:one", "sample:two", "missing:one", "sample:three", "sample:four", "sample:four"] };
const sections = collectionSections(ordered, byId);
assert.deepEqual(sections.map((section) => section.lectures), [["sample:one", "sample:two"], ["missing:one"], ["sample:three"], ["sample:four", "sample:four"]]);
assert.deepEqual(sections.flatMap((section) => section.lectures), ordered.lectures);
assert.equal(sections[0].id, "section-sample%3Aone");
assert.equal(collectionSections({ lectures: ["sample:one", "sample:two"] }, byId)[0].title, "Contents");
assert.equal(collectionSections({ lectures: ["sample:one"] }, byId)[0].title, byId("sample:one").title);
assert.deepEqual(collectionSections({ lectures: [] }, byId), []);

const authored = {
  lectures: ["sample:two", "missing:one", "sample:one", "sample:three"],
  chapters: [
    { title: "A curated order", collection: "sample:deeper", lectures: ["sample:two", "missing:one", "sample:one"], sessions: [
      { title: "First session", lectures: ["sample:two", "missing:one"] },
      { title: "Second session", lectures: ["sample:one"] },
    ] },
    { title: "A later chapter", lectures: ["sample:three"] },
  ],
};
const original = JSON.stringify(authored);
const grouped = collectionSections(authored, byId);
assert.equal(JSON.stringify(authored), original);
assert.equal(grouped[0].id, "section-sample%3Atwo");
assert.equal(grouped[0].collection, "sample:deeper");
assert.deepEqual(grouped[0].sessions.map((session) => session.id), ["session-sample%3Atwo", "session-sample%3Aone"]);
assert.deepEqual(grouped.flatMap((section) => section.lectures), authored.lectures);
grouped[0].lectures.push("changed");
grouped[0].sessions[0].lectures.push("changed");
assert.equal(JSON.stringify(authored), original, "Nested grouping arrays are independent copies");
const rawSessions = { chapters: [{ title: "Sessions without redundant members", sessions: [{ title: "One", lectures: ["sample:one", "missing:one"] }] }] };
assert.deepEqual(collectionSections(rawSessions, byId)[0].lectures, ["sample:one", "missing:one"]);
const imported = { lectures: ["sample:one", "sample:one", "missing:one"], chapters: [{ title: "Partial metadata", lectures: ["sample:one"] }] };
assert.deepEqual(collectionSections(imported, byId).flatMap((section) => section.lectures), imported.lectures);
const collision = collectionSections({ lectures: ["sample:one", "sample:three", "sample:one"] }, byId);
assert.equal(new Set(collision.map((section) => section.id)).size, collision.length);
assert.equal(collectionSections({ chapters: [{ title: "Empty", lectures: [] }] }, byId)[0].id, "section-0");

assert(matchesLecture("sample:one", byId, " first IDEA "));
assert(matchesLecture("sample:one", byId, "SAMPLE:ONE"));
assert(matchesLecture("sample:two", byId, "two"));
assert(matchesLecture("missing:one", byId, "missing:one"));
assert(matchesLecture("missing:one", byId, "  "));
assert(!matchesLecture("sample:one", byId, "different"));
const reader = "http://reader.test";
const back = "/collections/sample%3Amain?find=one&from=sample%3Ahub#section-sample%3Aone";
assert.equal(collectionReturnPath(back, "sample:main", reader), back);
assert.equal(collectionReturnPath("/courses/sample:main", "sample:main", reader), "/courses/sample:main");
for (const hint of ["https://other.test/collections/sample:main", "//other.test/collections/sample:main", "/collections/sample:other", "/collections/%", "http://[", "javascript:alert(1)", "/production", ""])
  assert.equal(collectionReturnPath(hint, "sample:main", reader), null);
assert.equal(collectionReturnPath(back, null, reader), null);
console.log("Catalog helpers preserve ordered content, hierarchy, missing entries, and stable search targets");

const described = { id: "book:one", title: "A novel", description: "Examines memory and political coercion.", creators: [{name: "A distinct writer", role: "author"}], outline: ["Language and testimony"] };
assert(matchesLecture(described.id, () => described, "coercion"));
assert(matchesLecture(described.id, () => described, "distinct writer"));
assert(matchesLecture(described.id, () => described, "testimony"));

assert.equal(collectionReturnPath("/stats?tag_q=Africa#stats-section-coverage", null, reader), "/stats?tag_q=Africa#stats-section-coverage");
assert.equal(collectionReturnPath("https://other.test/stats", null, reader), null);
assert.equal(collectionReturnPath("/stats/other", null, reader), null);

import assert from "node:assert/strict";
import { selectLearningMap, learningMapURL } from "../ailectures/static/learning-map.mjs";

const data = {
  nodes: Object.fromEntries([
    ["a:1", { id: "a:1", title: "Foundations" }], ["a:2", { id: "a:2", title: "Application" }],
    ["a:3", { id: "a:3", title: "Unrelated" }], ["optional:1", { id: "optional:1", title: "Optional background", available: false }],
    ["collection:a:main", { id: "collection:a:main", title: "Main" }],
  ]),
  collections: [
    { id: "a:main", lectures: ["a:1"] },
    { id: "a:deep", parent_id: "a:main", lectures: ["a:2"] },
    { id: "a:archive", parent_id: "a:main", role: "archive", lectures: ["a:3"] },
  ],
  component_lectures: { "a:old": "a:1" },
  relationships: [
    { id: "proof", from: "a:2", to: "a:1", type: "proof_depends_on", category: "proof", reasons: ["Uses the estimate"], evidence: [{ from: "a:2", to: "a:old" }] },
    { id: "order", from: "a:1", to: "a:2", type: "listening_next", category: "listening" },
    { id: "prep", from: "a:1", to: "optional:1", type: "soft_depends_on", category: "preparation" },
    { id: "internal", from: "a:1", to: "a:1", type: "proof_depends_on", category: "proof", internal: true },
    { id: "elsewhere", from: "a:3", to: "a:3", type: "related_to", category: "related" },
  ],
};
const before = structuredClone(data);
assert.deepEqual(selectLearningMap(data).relations.map(row => row.id), ["proof", "prep", "internal", "elsewhere"]);
assert.deepEqual(selectLearningMap(data, { lecture: "a:old", direction: "incoming", type: "proof" }).relations.map(row => row.id), ["proof", "internal"]);
assert.deepEqual(selectLearningMap(data, { lecture: "a:1", direction: "outgoing", type: "preparation" }).nodes.map(row => row.id), ["a:1", "optional:1"]);
assert.deepEqual(selectLearningMap(data, { collection: "a:main", type: "all" }).relations.map(row => row.id), ["proof", "order", "prep", "internal"]);
assert.deepEqual(selectLearningMap(data, { q: " A:OLD " }).relations.map(row => row.id), ["proof"]);
assert.deepEqual(selectLearningMap(data, { q: "unrelated", type: "proof" }).nodes.map(row => row.id), ["a:3"]);
assert.equal(selectLearningMap(data, { lecture: "missing:1" }).focusNode, null);
assert.equal(selectLearningMap(data, { lecture: "a:old" }).internal.length, 1);
assert.equal(learningMapURL({ lecture: "a:1", type: "connections", q: "two words", direction: "both", full: "1" }), "/learning-map?lecture=a%3A1&q=two+words&full=1");
assert.deepEqual(data, before);
const tagged = { nodes: { "math:isolated": { id: "math:isolated", title: "An isolated lecture", tags: ["Spectral theory"] } }, relationships: [] };
assert.deepEqual(selectLearningMap(tagged, { q: "spectral" }).nodes.map(row => row.id), ["math:isolated"]);
assert.equal(selectLearningMap(tagged, { q: "spectral" }).relations.length, 0, "Shared topics do not invent dependency edges");
console.log("Learning-map selection preserves evidence, scope, direction, missing nodes, and direct-link state");

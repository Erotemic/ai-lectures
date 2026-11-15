import assert from "node:assert/strict";
import { collectionGroups } from "../ailectures/static/browse.mjs";

const math = {
  id: "analysis:main",
  categories: ["Mathematics"],
  lectures: ["analysis:001000"],
};
const stories = {
  id: "stories:main",
  categories: ["Stories", "Imagination"],
  audiences: ["children"],
  lectures: ["stories:001000"],
};
const groups = collectionGroups([math, stories]);
assert.equal(groups.length, 3);
assert.equal(groups[0].children, true);
assert.deepEqual(groups.find((g) => g.title === "Mathematics").collections, [
  math,
]);
assert.equal(groups.filter((g) => g.collections.includes(stories)).length, 2);
assert.equal(
  stories.id,
  "stories:main",
  "Grouping does not rewrite collection identity",
);
console.log(
  "Independent collections can belong to several categories, with children's groups easy to reach",
);

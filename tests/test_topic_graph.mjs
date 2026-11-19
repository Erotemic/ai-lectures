import assert from "node:assert/strict";
import {
  topicGraph,
  graphNeighborhood,
} from "../ailectures/static/topic-graph-model.mjs";
const rows = [
  {
    id: "test:001000",
    title: "First",
    tag_paths: [
      ["History", "Japan", "Shinobi"],
      ["Place: Asia", "Place: Japan"],
    ],
    tags: ["History"],
  },
  {
    id: "test:002000",
    title: "Second",
    tag_paths: [
      ["History", "Japan", "Shinobi"],
      ["History", "Warfare"],
    ],
    tags: [],
  },
  {
    id: "test:003000",
    title: "Third",
    tag_paths: [["Science", "Biology"]],
    tags: [],
  },
];
const graph = topicGraph([...rows, rows[0]]);
const history = [...graph.nodes.values()].find(
  (node) => node.title === "History",
);
assert.equal(history.lectures.size, 2);
const view = graphNeighborhood(graph, history.id);
assert.deepEqual(
  view.lectures.map((row) => row.id),
  ["test:001000", "test:002000"],
);
const japan = [...graph.nodes.values()].find((node) => node.title === "Japan");
assert.equal(graphNeighborhood(graph, japan.id).focus.parent, history.id);
const nearby = graphNeighborhood(graph, "lecture:test:001000");
assert.deepEqual(
  nearby.lectures.map((row) => row.id),
  ["test:002000"],
);
assert.equal(nearby.lecture.title, "First");
const places = topicGraph(rows, "Places");
assert.equal(places.roots.length, 1);
assert.equal(places.nodes.get(places.roots[0]).title, "Place: Asia");
assert.equal(graphNeighborhood(graph, "missing").nodes[0].kind, "root");
const large = topicGraph(
  Array.from({ length: 200 }, (_, i) => ({
    id: "a:" + i,
    title: "Lecture " + i,
    tag_paths: [["Topic", "Branch " + i]],
    tags: [],
  })),
);
const focus = [...large.nodes.values()].find((node) => node.title === "Topic");
assert.ok(graphNeighborhood(large, focus.id).nodes.length <= 17);
assert.equal(graphNeighborhood(large, focus.id).lectures.length, 200);
console.log(
  "Topic graph deduplicates hierarchy membership, separates facets, preserves links, and bounds rendered neighborhoods.",
);

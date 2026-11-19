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
assert.equal(graphNeighborhood(graph, "missing").focus, undefined);
assert.equal(graphNeighborhood(graph, "missing").lecture, undefined);
const large = topicGraph(
  Array.from({ length: 200 }, (_, i) => ({
    id: "a:" + i,
    title: "Lecture " + i,
    tag_paths: [["Topic", "Branch " + i]],
    tags: [],
  })),
);
const focus = [...large.nodes.values()].find((node) => node.title === "Topic");
assert.equal(graphNeighborhood(large, focus.id).lectures.length, 200);
console.log(
  "Topic graph deduplicates hierarchy membership, separates facets, preserves links, and exposes complete connection lists.",
);

const { GraphExpansion } =
  await import("../ailectures/static/topic-graph-model.mjs");
const exploration = new GraphExpansion(large);
assert.equal(exploration.view().nodes.length, 2);
exploration.expand(focus.id);
assert.equal(exploration.view().nodes.length, 8); // Root, topic, six branches.
assert.equal(
  exploration.view().nodes.filter((n) => n.kind === "lecture").length,
  0,
);
const firstBranch = exploration.view().nodes.find((n) => n.parent === focus.id);
exploration.expand(firstBranch.id);
const firstLecture = "lecture:" + [...firstBranch.lectures][0];
assert.ok(exploration.view().nodes.some((n) => n.id === firstLecture));
for (let i = 0; i < 8; i++) exploration.expand(focus.id);
assert.ok(exploration.view().nodes.length > 17);
assert.ok(exploration.view().nodes.some((n) => n.id === firstLecture));
assert.equal(exploration.remaining(focus.id).topics, 146);
exploration.collapse(firstBranch.id);
assert.ok(!exploration.view().nodes.some((n) => n.id === firstLecture));
assert.ok(exploration.view().nodes.some((n) => n.id === firstBranch.id));
assert.ok(exploration.view().nodes.length > 17);
for (let i = 0; i < 34; i++) exploration.expand(focus.id, "topics");
assert.equal(exploration.remaining(focus.id).topics, 0);
assert.equal(exploration.view().nodes.length, 202);
exploration.expand(focus.id, "lectures");
assert.equal(
  exploration.view().nodes.filter((n) => n.kind === "lecture").length,
  6,
);

const distant = new GraphExpansion(large);
const lastBranch = [...large.nodes.values()].find(
  (n) => n.title === "Branch 199",
);
distant.reveal(lastBranch.id);
assert.equal(distant.view().nodes.length, 3); // A deep search does not load 199 siblings.
distant.expand(lastBranch.id);
assert.equal(distant.view().nodes.length, 4);
const restored = new GraphExpansion(large);
restored.restore(JSON.parse(JSON.stringify(distant.snapshot())));
assert.deepEqual(restored.view(), distant.view());
restored.collapse(focus.id);
assert.equal(restored.view().nodes.length, 2);
restored.collapse("root");
assert.deepEqual(
  restored.view().nodes.map((n) => n.id),
  ["root"],
);

const network = new GraphExpansion(graph);
network.reveal(history.id);
network.expand(history.id);
network.expand(japan.id);
const shinobi = [...graph.nodes.values()].find((n) => n.title === "Shinobi");
network.expand(shinobi.id);
network.expand("lecture:test:002000");
const warfare = [...graph.nodes.values()].find((n) => n.title === "Warfare");
assert.ok(network.view().nodes.some((n) => n.id === warfare.id));
assert.equal(
  new Set(network.view().nodes.map((n) => n.id)).size,
  network.view().nodes.length,
);
network.collapse(shinobi.id);
assert.ok(network.view().nodes.some((n) => n.id === "lecture:test:002000")); // Shared route survives.
network.collapse(history.id);
assert.ok(!network.view().nodes.some((n) => n.id === "lecture:test:002000"));

const untagged = new GraphExpansion(
  topicGraph([{ id: "empty:1", title: "Untagged", tags: [], tag_paths: [] }]),
);
untagged.reveal("lecture:empty:1");
assert.equal(untagged.view().nodes.length, 2);
assert.deepEqual(untagged.remaining("lecture:empty:1"), {
  topics: 0,
  lectures: 0,
});
console.log(
  "Incremental expansion preserves branches beyond 16 nodes, pages coarse-to-fine, reveals distant paths sparsely, restores state, and prunes collapsed/shared branches correctly.",
);

const { graphDetailVisible } =
  await import("../ailectures/static/topic-graph-model.mjs");
const leaf = { id: "lecture:test:001000", kind: "lecture", title: "First" };
assert.equal(graphDetailVisible(leaf, 0.2, history.id), false);
assert.equal(
  graphDetailVisible(leaf, 0.2, history.id, new Set([leaf.id])),
  true,
);
assert.equal(graphDetailVisible(shinobi, 0.2, history.id), false);
assert.equal(
  graphDetailVisible(shinobi, 0.2, history.id, new Set([shinobi.id])),
  true,
);
const inverse = new GraphExpansion(graph);
inverse.reveal(shinobi.id);
inverse.expand(shinobi.id);
assert.deepEqual(inverse.remaining(leaf.id), { topics: 0, lectures: 0 });
const beforeInverse = inverse.view();
assert.deepEqual(inverse.expand(leaf.id), []);
assert.deepEqual(inverse.view(), beforeInverse);
inverse.collapse(shinobi.id);
assert.ok(inverse.remaining(shinobi.id).lectures > 0);
console.log(
  "Explicit expansions survive zoom detail filtering, and existing reverse links are not offered as new connections.",
);

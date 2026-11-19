import { tagForest } from "./tag-model.mjs";

export function topicGraph(rows, facet = "Topics") {
  const lectures = new Map(rows.map((row) => [row.id, row]));
  const forest = tagForest(rows);
  const nodes = new Map(),
    roots = [];
  function visit(branches, path = [], parent = null) {
    for (const branch of branches.values()) {
      const labels = [...path, branch.label];
      const id = "topic:" + JSON.stringify([facet, ...labels]);
      const node = {
        id,
        kind: "topic",
        title: branch.label,
        path: labels,
        parent,
        lectures: branch.lectures,
        children: [],
      };
      nodes.set(id, node);
      if (parent) nodes.get(parent).children.push(id);
      else roots.push(id);
      visit(branch.children, labels, id);
    }
  }
  visit(forest.get(facet) || new Map());
  const memberships = new Map();
  for (const node of nodes.values())
    for (const id of node.lectures) {
      if (node.children.some((child) => nodes.get(child).lectures.has(id)))
        continue;
      if (!memberships.has(id)) memberships.set(id, []);
      memberships.get(id).push(node.id);
    }
  return {
    nodes,
    roots,
    lectures,
    memberships,
    facet,
    facets: [...forest.keys()],
  };
}

export function graphNeighborhood(graph, selected = "") {
  const focus = graph.nodes.get(selected);
  const lectureId = selected.startsWith("lecture:") ? selected.slice(8) : null;
  const lecture = graph.lectures.get(lectureId);
  const sort = (nodes) =>
    nodes.sort(
      (a, b) =>
        b.lectures.size - a.lectures.size || a.title.localeCompare(b.title),
    );
  let topics, lectures;
  if (lecture) {
    // Indexed specific paths keep lecture expansion proportional to its tags.
    topics = sort(
      (graph.memberships.get(lectureId) || []).map((id) => graph.nodes.get(id)),
    );
    const scores = new Map();
    for (const node of topics)
      for (const id of node.lectures)
        if (id !== lectureId) scores.set(id, (scores.get(id) || 0) + 1);
    lectures = [...scores]
      .sort((a, b) => b[1] - a[1] || a[0].localeCompare(b[0]))
      .map(([id]) => graph.lectures.get(id));
  } else {
    topics = sort(
      (focus?.children || graph.roots).map((id) => graph.nodes.get(id)),
    );
    lectures = focus
      ? [...focus.lectures]
          .map((id) => graph.lectures.get(id))
          .filter(Boolean)
          .sort((a, b) => a.title.localeCompare(b.title))
      : [];
  }
  return { topics, lectures, focus, lecture };
}

/** Incremental graph: each expansion reveals one batch, never replaces siblings. */
export class GraphExpansion {
  constructor(graph, batch = 6) {
    this.graph = graph;
    this.batch = batch;
    this.open = new Map();
    this.pins = new Map();
    this.cache = new Map();
    this.links = null;
    this.expand("root", "topics");
  }
  node(id) {
    if (id === "root") return { id, kind: "root", title: this.graph.facet };
    if (this.graph.nodes.has(id)) return this.graph.nodes.get(id);
    const row =
      id.startsWith("lecture:") && this.graph.lectures.get(id.slice(8));
    return row ? { id, kind: "lecture", title: row.title } : null;
  }
  neighbors(id) {
    if (this.cache.has(id)) return this.cache.get(id);
    const node = this.node(id);
    let topics = [],
      lectures = [];
    if (node?.kind === "root") topics = this.graph.roots;
    else if (node?.kind === "topic") {
      topics = node.children;
      lectures = [...node.lectures]
        .sort((a, b) =>
          this.graph.lectures
            .get(a)
            .title.localeCompare(this.graph.lectures.get(b).title),
        )
        .map((key) => "lecture:" + key);
    } else if (node?.kind === "lecture") {
      topics = this.graph.memberships.get(id.slice(8)) || [];
    }
    const result = {
      topics: [...topics].sort(
        (a, b) =>
          this.graph.nodes.get(b).lectures.size -
            this.graph.nodes.get(a).lectures.size ||
          this.graph.nodes
            .get(a)
            .title.localeCompare(this.graph.nodes.get(b).title),
      ),
      lectures,
    };
    this.cache.set(id, result);
    return result;
  }
  children(id) {
    const state = this.open.get(id) || { topics: 0, lectures: 0 };
    const neighbors = this.neighbors(id);
    return new Set([
      ...neighbors.topics.slice(0, state.topics),
      ...neighbors.lectures.slice(0, state.lectures),
      ...(this.pins.get(id) || []),
    ]);
  }
  connected(id) {
    if (!this.links) {
      this.links = new Map();
      for (const parent of new Set([
        ...this.open.keys(),
        ...this.pins.keys(),
      ])) {
        for (const child of this.children(parent))
          for (const [from, to] of [
            [parent, child],
            [child, parent],
          ]) {
            if (!this.links.has(from)) this.links.set(from, new Set());
            this.links.get(from).add(to);
          }
      }
    }
    return this.links.get(id) || new Set();
  }
  remaining(id) {
    const connected = this.connected(id),
      neighbors = this.neighbors(id);
    return {
      topics: neighbors.topics.filter((key) => !connected.has(key)).length,
      lectures: neighbors.lectures.filter((key) => !connected.has(key)).length,
    };
  }
  expand(id, kind = null) {
    if (!this.node(id)) return [];
    const remaining = this.remaining(id);
    kind ||= remaining.topics ? "topics" : "lectures";
    if (!remaining[kind]) return [];
    const state = this.open.get(id) || { topics: 0, lectures: 0 };
    const neighbors = this.neighbors(id)[kind];
    const children = this.connected(id);
    const added = [];
    while (state[kind] < neighbors.length && added.length < this.batch) {
      if (!children.has(neighbors[state[kind]]))
        added.push(neighbors[state[kind]]);
      state[kind]++;
    }
    this.open.set(id, state);
    this.links = null;
    return added;
  }
  pin(from, to) {
    if (!this.pins.has(from)) this.pins.set(from, new Set());
    this.pins.get(from).add(to);
    this.links = null;
  }
  reveal(id) {
    if (!this.node(id) || this.view().nodes.some((node) => node.id === id))
      return;
    const topic = this.graph.nodes.get(id);
    if (topic) {
      const path = [];
      for (let node = topic; node; node = this.graph.nodes.get(node.parent))
        path.unshift(node);
      let parent = "root";
      for (const node of path) {
        this.pin(parent, node.id);
        parent = node.id;
      }
    } else if (id.startsWith("lecture:")) {
      const parent = this.neighbors(id).topics[0];
      if (parent) {
        this.reveal(parent);
        this.pin(parent, id);
      } else this.pin("root", id);
    }
  }
  view() {
    const edges = new Map(),
      adjacency = new Map();
    for (const id of new Set([...this.open.keys(), ...this.pins.keys()])) {
      for (const child of this.children(id)) {
        if (!this.node(child)) continue;
        const key = JSON.stringify([id, child].sort());
        const kind =
          (id === "root" && this.graph.nodes.has(child)) ||
          this.graph.nodes.get(child)?.parent === id
            ? "hierarchy"
            : "association";
        edges.set(key, { from: id, to: child, kind });
        for (const [a, b] of [
          [id, child],
          [child, id],
        ]) {
          if (!adjacency.has(a)) adjacency.set(a, new Set());
          adjacency.get(a).add(b);
        }
      }
    }
    const reached = new Set(["root"]),
      queue = ["root"];
    for (let i = 0; i < queue.length; i++)
      for (const id of adjacency.get(queue[i]) || [])
        if (!reached.has(id)) {
          reached.add(id);
          queue.push(id);
        }
    return {
      nodes: queue.map((id) => this.node(id)),
      edges: [...edges.values()].filter(
        (edge) => reached.has(edge.from) && reached.has(edge.to),
      ),
    };
  }
  collapse(id) {
    this.open.delete(id);
    this.pins.delete(id);
    this.links = null;
    const reached = new Set(this.view().nodes.map((node) => node.id));
    for (const map of [this.open, this.pins])
      for (const key of map.keys()) if (!reached.has(key)) map.delete(key);
    this.links = null;
  }
  snapshot() {
    return {
      open: [...this.open],
      pins: [...this.pins].map(([id, keys]) => [id, [...keys]]),
    };
  }
  restore(snapshot) {
    if (
      !snapshot ||
      !Array.isArray(snapshot.open) ||
      !Array.isArray(snapshot.pins)
    )
      return;
    this.open.clear();
    this.pins.clear();
    this.links = null;
    for (const [id, state] of snapshot.open)
      if (
        this.node(id) &&
        state &&
        Number.isInteger(state.topics) &&
        Number.isInteger(state.lectures) &&
        state.topics >= 0 &&
        state.lectures >= 0
      ) {
        const neighbors = this.neighbors(id);
        this.open.set(id, {
          topics: Math.min(state.topics, neighbors.topics.length),
          lectures: Math.min(state.lectures, neighbors.lectures.length),
        });
      }
    for (const [id, children] of snapshot.pins)
      if (this.node(id) && Array.isArray(children))
        for (const child of children) if (this.node(child)) this.pin(id, child);
  }
}

/** Explicitly revealed connections remain visible until the user zooms out. */
export function graphDetailVisible(
  node,
  scale,
  selected,
  revealed = new Set(),
) {
  return (
    node.id === selected ||
    revealed.has(node.id) ||
    node.kind === "root" ||
    ((node.kind !== "lecture" || scale >= 0.55) &&
      (!node.path ||
        node.path.length <= (scale < 0.3 ? 1 : scale < 0.55 ? 2 : Infinity)))
  );
}

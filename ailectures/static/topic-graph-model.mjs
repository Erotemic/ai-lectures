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
  return { nodes, roots, lectures, facet, facets: [...forest.keys()] };
}

export function graphNeighborhood(graph, selected = "", limit = 16) {
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
    const memberships = [...graph.nodes.values()].filter((node) =>
      node.lectures.has(lectureId),
    );
    // Show specific paths without flooding the graph with all their ancestors.
    topics = sort(
      memberships.filter(
        (node) =>
          !node.children.some((id) =>
            graph.nodes.get(id).lectures.has(lectureId),
          ),
      ),
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
  const center =
    focus ||
    (lecture
      ? { id: selected, kind: "lecture", title: lecture.title }
      : { id: "root", kind: "root", title: graph.facet });
  const visibleTopics = topics.slice(0, 6);
  const visibleLectures = lectures.slice(
    0,
    Math.max(0, limit - visibleTopics.length - (focus?.parent ? 1 : 0)),
  );
  const nodes = [
    center,
    ...visibleTopics,
    ...visibleLectures.map((row) => ({
      id: "lecture:" + row.id,
      kind: "lecture",
      title: row.title,
    })),
  ];
  if (focus?.parent) nodes.push(graph.nodes.get(focus.parent));
  const edges = [
    ...visibleTopics.map((node) => ({
      from: center.id,
      to: node.id,
      kind: lecture ? "association" : "hierarchy",
    })),
    ...visibleLectures.map((row) => ({
      from: center.id,
      to: "lecture:" + row.id,
      kind: "association",
    })),
    ...(focus?.parent
      ? [{ from: focus.parent, to: focus.id, kind: "hierarchy" }]
      : []),
  ];
  return { center, topics, lectures, nodes, edges, focus, lecture };
}

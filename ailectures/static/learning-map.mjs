import { api, el } from "./api.mjs";

const CATEGORY_LABELS = {
  preparation: "Teaching preparation", proof: "Proof dependencies",
  history: "Historical influence", lineage: "Source adaptations",
  related: "Related and expanded treatments", listening: "Listening order",
  organization: "Collection organization",
};

/** Pure selection model shared by the view and focused behavioral checks. */
export function selectLearningMap(data, state = {}) {
  const nodes = data.nodes || {};
  const collection = state.collection || "";
  const query = String(state.q || "").trim().toLocaleLowerCase();
  const selected = state.lecture || state.node || "";
  const focus = data.component_lectures?.[selected] || selected;
  const scope = new Set();
  const courses = new Map((data.collections || []).map(row => [row.id, row]));
  const visited = new Set();
  function visit(id) {
    if (visited.has(id)) return;
    visited.add(id);
    scope.add("collection:" + id);
    for (const key of courses.get(id)?.lectures || [])
      scope.add(data.component_lectures?.[key] || key);
    for (const row of courses.values())
      if (row.parent_id === id && row.role !== "archive") visit(row.id);
  }
  if (collection) visit(collection);
  const type = state.type || "connections";
  const relations = (data.relationships || []).filter(edge => {
    if (type === "connections" && ["listening", "organization"].includes(edge.category)) return false;
    if (!["all", "connections"].includes(type) && type !== edge.type && type !== edge.category) return false;
    if (collection && !scope.has(edge.from) && !scope.has(edge.to) && !edge.collections?.includes(collection)) return false;
    if (focus) {
      if (state.direction === "incoming" && edge.to !== focus) return false;
      if (state.direction === "outgoing" && edge.from !== focus) return false;
      if (!["incoming", "outgoing"].includes(state.direction) && edge.from !== focus && edge.to !== focus) return false;
    }
    if (!query) return true;
    return [nodes[edge.from]?.title, nodes[edge.to]?.title, edge.from, edge.to,
      edge.label, edge.description, ...(edge.reasons || []),
      ...(edge.evidence || []).flatMap(claim => [claim.from, claim.to, claim.why]),
    ].filter(Boolean).join(" ").toLocaleLowerCase().includes(query);
  });
  const visible = new Set(relations.flatMap(edge => [edge.from, edge.to]));
  if (focus && nodes[focus]) visible.add(focus);
  // A title/ID search can find a lecture with no relationships of this kind.
  if (query && !focus)
    for (const node of Object.values(nodes))
      if ((!collection || scope.has(node.id)) && `${node.title} ${node.id}`.toLocaleLowerCase().includes(query)) visible.add(node.id);
  return {
    focus, relations, internal: relations.filter(edge => edge.internal),
    external: relations.filter(edge => !edge.internal),
    nodes: [...visible].map(key => nodes[key]).filter(Boolean),
    focusNode: nodes[focus] || null,
  };
}

export function learningMapURL(state = {}) {
  const params = new URLSearchParams();
  for (const key of ["lecture", "node", "collection", "q", "type", "direction", "full"])
    if (state[key] && !(key === "type" && state[key] === "connections") && !(key === "direction" && state[key] === "both")) params.set(key, state[key]);
  return "/learning-map" + (params.size ? "?" + params : "");
}

function svgElement(tag, attributes = {}, text = null) {
  const node = document.createElementNS("http://www.w3.org/2000/svg", tag);
  for (const [key, value] of Object.entries(attributes)) node.setAttribute(key, value);
  if (text !== null) node.textContent = text;
  return node;
}

function wrapTitle(text, length = 30) {
  const words = String(text).split(/\s+/);
  const lines = [""];
  for (const word of words) {
    if (lines.at(-1).length + word.length + 1 > length && lines.at(-1)) lines.push("");
    lines[lines.length - 1] += (lines.at(-1) ? " " : "") + word;
  }
  const visible = lines.slice(0, 2).map(line => line.length > length ? line.slice(0, length - 1) + "…" : line);
  if (lines.length > 2) visible[1] = visible[1].slice(0, length - 1) + "…";
  return visible;
}

/** Native library view. Inject data/link helpers for embedding or testing. */
export async function renderLearningMap(main, context = {}) {
  const root = el("section", { class: "learning-map" });
  root.style.minWidth = "0";
  main.replaceChildren(root);
  const heading = el("h1", { text: "Learning map" });
  root.append(heading, el("p", { class: "intro", text: "Explore the connections between lectures. Teaching preparation, proof use, historical influence, and listening order are separate kinds of relationship." }));
  let data;
  try { data = context.data || await (context.load || api)("/api/library/learning-map"); }
  catch (error) { root.append(el("p", { class: "notice", text: error.message })); return; }
  if (!root.isConnected) return;
  const params = new URLSearchParams(location.search);
  const state = Object.fromEntries(["lecture", "node", "collection", "q", "type", "direction", "full"].map(key => [key, params.get(key) || ""]));
  let limit = Number.isInteger(history.state?.mapLimit) ? Math.max(40, history.state.mapLimit) : 40;
  let zoom = 1;
  const link = context.link || ((label, url) => el("a", { href: url, "data-nav": "", text: label }));
  const button = (label, action) => el("button", { type: "button", onclick: action, text: label });
  const search = el("input", { id: "learning-map-search", type: "search", placeholder: "Find a title, idea, lecture ID, or explanation", "aria-label": "Search the learning map", value: state.q });
  const collections = el("select", { "aria-label": "Learning map collection" }, el("option", { value: "", text: "All collections" }),
    ...(data.collections || []).map(row => el("option", { value: row.id, text: row.title + (row.role === "archive" ? " · complete sequence" : "") })));
  if (state.collection && !(data.collections || []).some(row => row.id === state.collection))
    collections.append(el("option", { value: state.collection, text: state.collection + " · Not installed" }));
  collections.value = state.collection;
  const types = el("select", { "aria-label": "Relationship type" },
    el("option", { value: "connections", text: "Conceptual connections" }),
    el("option", { value: "all", text: "All relationships, including listening order" }),
    ...Object.entries(CATEGORY_LABELS).map(([value, text]) => el("option", { value, text })),
    el("optgroup", { label: "Specific relationship" }, ...Object.entries(data.relation_types || {}).map(([value, row]) => el("option", { value, text: row.label }))));
  types.value = state.type || "connections";
  if (!types.value) types.value = "connections";
  const direction = el("select", { "aria-label": "Relationship direction" },
    el("option", { value: "both", text: "Both directions" }),
    el("option", { value: "outgoing", text: "Outgoing" }),
    el("option", { value: "incoming", text: "Incoming" }));
  direction.value = state.direction || "both";
  const status = el("p", { class: "muted", role: "status", "aria-live": "polite" });
  const inspector = el("section", { class: "map-selection" });
  const diagram = el("div", { class: "map-diagram", tabindex: "0", "aria-label": "Interactive learning-map diagram; scroll to explore" });
  Object.assign(diagram.style, { overflow: "auto", maxHeight: "480px", minWidth: "0", border: "1px solid var(--line)", borderRadius: "8px" });
  const diagramStatus = el("small", { class: "muted" });
  const relationshipList = el("div", { class: "map-relationships" });
  const internalList = el("div", { class: "map-internal" });
  const isolatedList = el("div");
  const footer = el("div", { class: "actions" });
  root.append(el("div", { class: "filters map-filters" }, search,
    el("label", {}, "Collection", collections), el("label", {}, "Relationship", types), el("label", {}, "Direction", direction)),
    el("div", { class: "actions" }, button("Clear filters", () => {
      for (const key of Object.keys(state)) state[key] = "";
      search.value = collections.value = ""; types.value = "connections"; direction.value = "both"; limit = 40; update(); search.focus();
    }), button("Show complete view", () => { state.full = "1"; update(); })),
    status, inspector,
    el("div", { class: "actions map-zoom" }, button("Zoom in", () => { zoom = Math.min(3, zoom * 1.25); drawDiagram(); }),
      button("Zoom out", () => { zoom = Math.max(0.5, zoom / 1.25); drawDiagram(); }), button("Fit width", () => { zoom = 1; drawDiagram(); })),
    diagramStatus, diagram, relationshipList, internalList, isolatedList, footer);
  let selected;
  function focusNode(id) {
    const node = data.nodes[id];
    if (!node) return;
    state.lecture = node.kind === "lecture" ? id : "";
    state.node = node.kind === "collection" ? id : "";
    limit = 40; update();
    inspector.querySelector("h2")?.focus({ preventScroll: true });
  }
  function nodeLink(node) {
    if (!node) return el("span", { text: "Unknown entry" });
    return node.url && node.available ? link(node.title, node.url)
      : el("span", { class: "muted", text: node.title + " · Not installed" });
  }
  function entry(node) {
    return el("div", { class: "map-entry" }, nodeLink(node), " ", button("Focus connections", () => focusNode(node.id)));
  }
  function drawDiagram() {
    const all = selected.nodes;
    const ordered = selected.focusNode ? [selected.focusNode, ...all.filter(node => node.id !== selected.focus)] : all;
    const visible = state.full ? ordered : ordered.slice(0, 18);
    diagram.replaceChildren();
    diagramStatus.textContent = visible.length < all.length ? `Diagram preview: ${visible.length} of ${all.length} connected entries. The list below includes the selection; Show complete view includes every entry and relationship.` : `${visible.length} entries in the diagram. Select an entry to inspect its incoming and outgoing connections.`;
    if (!visible.length) { diagram.append(el("p", { class: "muted", text: "No connections match these filters. Try listening order, another collection, or a title search." })); return; }
    const width = Math.max(300, diagram.clientWidth || main.clientWidth || 700);
    const columns = Math.max(1, Math.floor(width / 240));
    const cellWidth = width / columns;
    const height = Math.ceil(visible.length / columns) * 112 + 32;
    const svg = svgElement("svg", { width: width * zoom, height: height * zoom, viewBox: `0 0 ${width} ${height}`, role: "group", "aria-label": "Learning connections. Entry buttons also appear in the accessible list below." });
    svg.style.display = "block"; svg.style.maxWidth = "none";
    const defs = svgElement("defs");
    const marker = svgElement("marker", { id: "learning-map-arrow", viewBox: "0 0 10 10", refX: "9", refY: "5", markerWidth: "7", markerHeight: "7", orient: "auto-start-reverse" });
    marker.append(svgElement("path", { d: "M 0 0 L 10 5 L 0 10 z", fill: "var(--muted)" })); defs.append(marker); svg.append(defs);
    const positions = new Map(visible.map((node, index) => [node.id, { x: (index % columns) * cellWidth + 12, y: Math.floor(index / columns) * 112 + 16, w: cellWidth - 24, h: 82 }]));
    const visibleIds = new Set(visible.map(node => node.id));
    for (const edge of selected.external) {
      if (!visibleIds.has(edge.from) || !visibleIds.has(edge.to)) continue;
      const first = positions.get(edge.from), last = positions.get(edge.to);
      let start, end;
      if (first.y === last.y) {
        const right = last.x > first.x;
        start = [right ? first.x + first.w : first.x, first.y + first.h / 2];
        end = [right ? last.x : last.x + last.w, last.y + last.h / 2];
      } else {
        const down = last.y > first.y;
        start = [first.x + first.w / 2, down ? first.y + first.h : first.y];
        end = [last.x + last.w / 2, down ? last.y : last.y + last.h];
      }
      const line = svgElement("path", { d: `M ${start[0]} ${start[1]} L ${end[0]} ${end[1]}`, fill: "none", stroke: "var(--muted)", "stroke-width": "1.5", "marker-end": "url(#learning-map-arrow)", opacity: "0.85" });
      line.append(svgElement("title", {}, `${data.nodes[edge.from].title} — ${edge.label} → ${data.nodes[edge.to].title}`)); svg.append(line);
    }
    for (const node of visible) {
      const p = positions.get(node.id);
      const group = svgElement("g", { tabindex: "0", role: "button", "aria-label": `${node.title}${node.available ? "" : ", not installed"}. Focus connections.`, class: "map-node" });
      group.style.cursor = "pointer";
      const box = svgElement("rect", { x: p.x, y: p.y, width: p.w, height: p.h, rx: "7", fill: node.id === selected.focus ? "var(--soft)" : "var(--panel)", stroke: node.id === selected.focus ? "var(--accent)" : "var(--line)", "stroke-width": node.id === selected.focus ? "2.5" : "1", "stroke-dasharray": node.available ? "none" : "5 3" });
      group.append(box, svgElement("title", {}, node.title + " · " + node.id));
      const titleLines = wrapTitle(node.title, Math.max(22, Math.floor(p.w / 7.4)));
      titleLines.forEach((line, index) => group.append(svgElement("text", { x: p.x + 10, y: p.y + 23 + index * 18, fill: "var(--ink)", "font-size": "13", "font-family": "system-ui, sans-serif" }, line)));
      group.append(svgElement("text", { x: p.x + 10, y: p.y + 69, fill: "var(--muted)", "font-size": "10", "font-family": "system-ui, sans-serif" }, node.available ? (node.kind === "collection" ? "Collection" : node.id.length > Math.floor((p.w - 20) / 6) ? node.id.slice(0, Math.floor((p.w - 20) / 6) - 1) + "…" : node.id) : "Not installed"));
      group.addEventListener("click", () => focusNode(node.id));
      group.addEventListener("keydown", event => { if (["Enter", " "].includes(event.key)) { event.preventDefault(); focusNode(node.id); } });
      group.addEventListener("focus", () => { box.setAttribute("stroke-width", "3"); box.setAttribute("stroke", "var(--accent)"); });
      group.addEventListener("blur", () => { box.setAttribute("stroke-width", node.id === selected.focus ? "2.5" : "1"); box.setAttribute("stroke", node.id === selected.focus ? "var(--accent)" : "var(--line)"); });
      svg.append(group);
    }
    diagram.append(svg);
  }
  function relationshipCard(edge) {
    return el("article", { class: "card map-relation" }, el("div", { class: "eyebrow", text: `${CATEGORY_LABELS[edge.category] || edge.category} · ${edge.label}` }),
      entry(data.nodes[edge.from]), el("p", { class: "muted", text: "→ " + edge.label }), entry(data.nodes[edge.to]),
      ...edge.reasons.map(reason => el("p", { text: reason })),
      el("p", { class: "muted", text: edge.description }),
      el("details", {}, el("summary", { text: `Original claims · ${edge.evidence.length}` }),
        ...edge.evidence.map(claim => el("p", {}, el("code", { text: `${claim.from} → ${claim.to}` }), claim.why ? " · " + claim.why : "", claim.collection_id ? " · " + (data.collections.find(row => row.id === claim.collection_id)?.title || claim.collection_id) : ""))));
  }
  function update() {
    state.q = search.value; state.collection = collections.value;
    state.type = types.value; state.direction = direction.value;
    selected = selectLearningMap(data, state);
    direction.disabled = !selected.focus;
    history.replaceState({ ...history.state, mapLimit: limit }, "", learningMapURL(state));
    status.textContent = `${selected.relations.length} relationships · ${selected.nodes.length} entries${selected.internal.length ? ` · ${selected.internal.length} within combined lectures` : ""}`;
    inspector.replaceChildren();
    if (selected.focusNode) {
      const node = selected.focusNode;
      inspector.append(el("h2", { tabindex: "-1", text: node.title }), nodeLink(node), el("p", { class: "muted", text: node.id + (node.available ? "" : " · Not installed in this library") }),
        button("Clear selected entry", () => { state.lecture = state.node = ""; update(); }));
    } else if (selected.focus) inspector.append(el("p", { class: "notice", text: "This entry is not available in the current map: " + selected.focus }), button("Clear selected entry", () => { state.lecture = state.node = ""; update(); }));
    drawDiagram();
    const shown = state.full ? selected.external : selected.external.slice(0, limit);
    relationshipList.replaceChildren(el("h2", { text: "Connections" }), ...shown.map(relationshipCard));
    if (!selected.external.length) relationshipList.append(el("p", { class: "muted", text: "No external relationships match. A lecture can remain useful without an authored prerequisite or proof link; collection order is available as a separate filter." }));
    const internal = state.full ? selected.internal : selected.internal.slice(0, limit);
    internalList.replaceChildren();
    if (internal.length) {
      const body = el("tbody");
      for (const edge of internal)
        for (const claim of edge.evidence)
          body.append(el("tr", {}, el("td", {}, nodeLink(data.nodes[edge.from])), el("td", {}, el("code", { text: claim.from })), el("td", { text: edge.label }), el("td", {}, el("code", { text: claim.to })), el("td", { text: claim.why || edge.description })));
      const overflow = el("div", { class: "map-table-scroll" }, el("table", {}, el("caption", { text: "Original relationships now contained within one combined manuscript" }), el("thead", {}, el("tr", {}, ...["Current lecture", "Original source", "Relationship", "Original target", "Explanation"].map(text => el("th", { scope: "col", text })))), body));
      overflow.style.overflowX = "auto";
      internalList.append(el("h2", { text: "Within combined lectures" }), el("p", { class: "muted", text: "These claims connect original components of the same current lecture. They remain evidence; they do not create a self-prerequisite." }), overflow);
    }
    const connectedIds = new Set(selected.relations.flatMap(edge => [edge.from, edge.to]));
    const isolated = selected.nodes.filter(node => !connectedIds.has(node.id));
    isolatedList.replaceChildren();
    if (isolated.length) isolatedList.append(el("h2", { text: "Matching entries" }), ...isolated.map(entry));
    footer.replaceChildren();
    if (!state.full && (selected.external.length > limit || selected.internal.length > limit)) footer.append(button("Show more connections", () => { limit += 60; update(); }), button("Show every matching connection", () => { state.full = "1"; update(); }));
    if (state.full) footer.append(button("Return to preview", () => { state.full = ""; limit = 40; update(); }));
  }
  for (const input of [search, collections, types, direction]) input.addEventListener(input === search ? "input" : "change", () => { limit = 40; update(); });
  update();
  return { element: root, data };
}

export class LearningMap {
  constructor(context = {}) { this.context = context; }
  render(main) { return renderLearningMap(main, this.context); }
}

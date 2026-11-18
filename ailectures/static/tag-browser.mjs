import { el } from "./api.mjs";
import { tagForest } from "./tag-model.mjs";

/** Expand broad tags to discover narrower coverage, with deduplicated counts. */
export function tagBrowser(rows, link) {
  const forests = tagForest(rows);
  const root = el("section", { class: "section tag-browser" }, el("h2", { text: "Browse tags from broad to specific" }),
    el("p", { class: "muted", text: "Expand a branch to see narrower tags, or select any label to see its lectures. Counts include descendants and count each lecture once within a branch. Associations can overlap; a broad date range does not imply coverage of every year." }));
  const facet = el("select", { "aria-label": "Tag dimension" }, ...[...forests.keys()].sort().map(value => el("option", { value, text: value })));
  facet.value = forests.has("Topics") ? "Topics" : facet.options[0]?.value || "";
  const search = el("input", { type: "search", "aria-label": "Search tag hierarchy", placeholder: "Find a topic, region, century, or year" });
  const result = el("div");
  root.append(el("div", { class: "filters" }, el("label", {}, "Dimension", facet), search), result);
  function draw() {
    const query = search.value.trim().toLocaleLowerCase();
    const matches = node => !query || node.label.toLocaleLowerCase().includes(query) || [...node.children.values()].some(matches);
    function level(nodes, inheritedMatch = false) {
      const visible = [...nodes.values()].filter(node => inheritedMatch || matches(node)).sort((a, b) => a.label.localeCompare(b.label, undefined, { numeric: true }));
      return el("ul", { class: "tag-tree" }, ...visible.map(node => {
        const label = node.label.includes(": ") ? node.label.slice(node.label.indexOf(": ") + 2) : node.label;
        const anchor = link(label, "/lectures?" + new URLSearchParams({ tag: node.label }));
        anchor.title = node.label;
        const count = el("span", { class: "muted tag-count", text: `${node.lectures.size.toLocaleString()} lecture${node.lectures.size === 1 ? "" : "s"}` });
        if (!node.children.size) return el("li", {}, anchor, count);
        const details = el("details", { open: Boolean(query) }, el("summary", {}, anchor, count));
        const children = () => level(node.children, inheritedMatch || Boolean(query && node.label.toLocaleLowerCase().includes(query)));
        if (query) details.append(children());
        else details.addEventListener("toggle", () => { if (details.open && details.children.length === 1) details.append(children()); });
        return el("li", {}, details);
      }));
    }
    const tree = level(forests.get(facet.value) || new Map());
    result.replaceChildren(tree);
    if (!tree.children.length) result.append(el("p", { text: "No matching tags in this dimension." }));
  }
  facet.onchange = draw;
  search.oninput = draw;
  draw();
  return root;
}

export function lectureTagPaths(row, link) {
  const paths = row.tag_paths || [];
  if (!paths.length) return null;
  return el("details", { class: "lecture-tag-paths" }, el("summary", { text: "Tags from broad to specific" }),
    el("ul", {}, ...paths.map(path => el("li", {}, ...path.flatMap((tag, index) => [index ? " › " : null,
      link(tag.includes(": ") ? tag.slice(tag.indexOf(": ") + 2) : tag, "/lectures?" + new URLSearchParams({ tag }))])))));
}

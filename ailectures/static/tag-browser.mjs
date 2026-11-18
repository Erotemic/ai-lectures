import { statsSection } from "./stats-section.mjs";
import { el, lectureURL } from "./api.mjs";
import { coverageModel } from "./coverage-model.mjs";
import { formatMinutes } from "./browse-model.mjs";

/** Compare broad branches first; expand to inspect detail and contributions. */
export function tagBrowser(rows, link, { packs = [] } = {}) {
  const packNames = new Map(packs.map(pack => [pack.id, pack.title || pack.id]));
  const model = coverageModel(rows), forests = model.forests;
  const root = statsSection("coverage", "Coverage from broad to specific",
    el("p", { text: "Expand a region, topic, or period to compare its narrower tags. Parent totals include descendants, counting each lecture once." }));
  root.classList.add("tag-browser");
  const facet = el("select", { "aria-label": "Tag dimension" }, ...[...forests.keys()].sort().map(value => el("option", { value, text: value })));
  facet.value = forests.has("Places") ? "Places" : forests.has("Topics") ? "Topics" : facet.options[0]?.value || "";
  const search = el("input", { type: "search", "aria-label": "Search tag hierarchy", placeholder: "Find a topic, region, century, or year" });
  const sort = el("select", { "aria-label": "Sort coverage" },
    ...[["name", "Name"], ["sections", "Most sections"], ["lectures", "Most lectures"], ["minutes", "Most listening time"]].map(([value, text]) => el("option", { value, text })));
  const count = el("p", { class: "muted", role: "status" });
  const result = el("div", { class: "coverage-tree" });
  root.append(el("div", { class: "filters" }, el("label", {}, "Dimension", facet), search, el("label", {}, "Order", sort)), count,
    el("details", { class: "coverage-count-help" }, el("summary", { text: "How these counts work" }), el("p", { class: "muted coverage-explanation", text: "Sections group installments by their authored section within a content pack; unsectioned lectures count separately. They are editorial groupings, not a count of distinct works. Expand any row to see which sections contribute its lectures. Place associations describe origins, settings, and context; missing tags remain unclassified. Branches can overlap, so their totals are not additive." })),
    el("div", { class: "coverage-columns", "aria-hidden": "true" }, el("span", { text: "Tag" }), el("span", { text: "Sections" }), el("span", { text: "Lectures" }), el("span", { text: "Est. listening" })), result);
  function draw() {
    const query = search.value.trim().toLocaleLowerCase();
    const matches = node => !query || node.label.toLocaleLowerCase().includes(query) || [...node.children.values()].some(matches);
    function contributions(node, open = false) {
      const data = model.totals(node);
      const groups = el("div", { class: "coverage-contributions" });
      const list = el("ul");
      const groupTitle = group => group.section ? group.section.replaceAll("-", " ").replace(/^./, first => first.toUpperCase()) : group.first.title;
      const show = limit => list.replaceChildren(...data.groups.slice(0, limit).map(group => el("li", {},
        el("span", {}, group.section ? el("span", { text: groupTitle(group) }) : link(groupTitle(group), lectureURL(group.first.id)),
          el("small", { class: "muted", text: packNames.get(group.namespace) || group.namespace })),
        el("span", { text: `${group.lectures.toLocaleString()} lecture${group.lectures === 1 ? "" : "s"} · ${Math.round(group.lectures / data.lectures * 100)}%` }))));
      show(5);
      groups.append(el("p", { class: "muted", text: `Estimated listening: ${formatMinutes(data.minutes)}. Section shares below refer to this branch’s lectures.` }), el("p", { class: "muted", text: node.children.size
        ? `${data.atLevel.toLocaleString()} lectures have no narrower tag within this branch. Section contributions include this tag and all descendants:`
        : "Contributing sections:" }), list);
      if (data.groups.length > 5) {
        const all = el("button", { type: "button", text: `Show all ${data.groups.length.toLocaleString()} sections`, onclick: () => { show(data.groups.length); all.remove(); } });
        groups.append(all);
      }
      const title = node.label.includes(": ") ? node.label.slice(node.label.indexOf(": ") + 2) : node.label;
      const details = el("details", { class: "coverage-section-details", open }, el("summary", { text: `Sections contributing to ${title} (${data.sections.toLocaleString()})` }));
      if (open) details.append(groups);
      details.addEventListener("toggle", () => { if (details.open && details.children.length === 1) details.append(groups); });
      return details;
    }
    function level(nodes, inheritedMatch = false) {
      const visible = [...nodes.values()].filter(node => inheritedMatch || matches(node)).sort((a, b) =>
        (sort.value === "name" ? 0 : model.totals(b)[sort.value] - model.totals(a)[sort.value]) || a.label.localeCompare(b.label, undefined, { numeric: true }));
      return el("ul", { class: "tag-tree" }, ...visible.map(node => {
        const label = node.label.includes(": ") ? node.label.slice(node.label.indexOf(": ") + 2) : node.label;
        const anchor = link(label, "/lectures?" + new URLSearchParams({ tag: node.label }));
        anchor.title = node.label;
        const data = model.totals(node);
        const details = el("details", { open: Boolean(query) }, el("summary", { class: "coverage-row" },
          el("span", { class: "coverage-label" }, anchor),
          el("span", { "aria-label": `${data.sections} sections`, text: data.sections.toLocaleString() }),
          el("span", { "aria-label": `${data.lectures} lectures`, text: data.lectures.toLocaleString() }),
          el("span", { "aria-label": "Estimated listening time", text: formatMinutes(data.minutes) })));
        const expand = () => {
          if (details.children.length > 1) return;
          if (node.children.size) details.append(level(node.children, inheritedMatch || Boolean(query && node.label.toLocaleLowerCase().includes(query))));
          details.append(contributions(node, !query || node.label.toLocaleLowerCase().includes(query)));
        };
        if (query) expand();
        details.addEventListener("toggle", () => { if (details.open) expand(); });
        return el("li", {}, details);
      }));
    }
    const tagged = model.tagged(facet.value).size;
    count.textContent = `${tagged.toLocaleString()} / ${model.rows.length.toLocaleString()} lectures have ${facet.value === "Places" ? "place" : facet.value === "Topics" ? "topic" : facet.value === "Authors" ? "author" : facet.value.toLowerCase()} tags · ${(model.rows.length - tagged).toLocaleString()} without tags in this dimension`;
    const nodes = forests.get(facet.value) || new Map();
    const continents = new Set(["Africa", "Americas", "Asia", "Europe", "Oceania", "Antarctica"].map(label => "Place: " + label));
    const geographical = facet.value === "Places" && !query;
    const mainNodes = geographical ? new Map([...nodes].filter(([label]) => continents.has(label))) : nodes;
    const associatedNodes = geographical ? new Map([...nodes].filter(([label, node]) => !continents.has(label) && node.children.size)) : new Map();
    const otherNodes = geographical ? new Map([...nodes].filter(([label, node]) => !continents.has(label) && !node.children.size)) : new Map();
    const tree = level(mainNodes);
    result.replaceChildren(tree);
    if (associatedNodes.size) result.append(el("details", { class: "coverage-unmapped" },
      el("summary", { text: "Oceans, polar areas, and regions spanning continents" }),
      el("p", { class: "muted", text: "These associations cross continental boundaries or describe bodies of water. Their lectures can also appear in the continental branches." }), level(associatedNodes)));
    if (otherNodes.size) result.append(el("details", { class: "coverage-unmapped" },
      el("summary", { text: `${otherNodes.size.toLocaleString()} place labels without a broader path` }),
      el("p", { class: "muted", text: "These labels have no broader geographic association recorded. They remain searchable; ambiguous names are not assigned a country automatically." }), level(otherNodes)));
    if (!tree.children.length && !otherNodes.size && !associatedNodes.size) result.append(el("p", { text: "No matching tags in this dimension." }));
  }
  facet.onchange = draw;
  search.oninput = draw;
  sort.onchange = draw;
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

import { statsSection } from "./stats-section.mjs";
import { el, lectureURL } from "./api.mjs";
import { coverageModel } from "./coverage-model.mjs";
import { formatMinutes } from "./browse-model.mjs";

/** Compare broad branches first; expand to inspect detail and contributions. */
export function tagBrowser(rows, link, { packs = [] } = {}) {
  const packNames = new Map(packs.map(pack => [pack.id, pack.title || pack.id]));
  const model = coverageModel(rows), forests = model.forests;
  const params = new URLSearchParams(location.search);
  const root = statsSection("coverage", "Coverage from broad to specific",
    el("p", { text: "Expand a region, topic, or period to compare its narrower tags. Parent totals include descendants, counting each lecture once." }));
  root.classList.add("tag-browser");
  const facet = el("select", { "aria-label": "Tag dimension" }, ...[...forests.keys()].sort().map(value => el("option", { value, text: value })));
  facet.value = forests.has("Places") ? "Places" : forests.has("Topics") ? "Topics" : facet.options[0]?.value || "";
  if (forests.has(params.get("tag_dimension"))) facet.value = params.get("tag_dimension");
  const search = el("input", { type: "search", "aria-label": "Search tag hierarchy", placeholder: "Find a topic, region, century, or year", value: params.get("tag_q") || "" });
  const sort = el("select", { "aria-label": "Sort coverage" },
    ...[["name", "Name"], ["sections", "Most sections"], ["lectures", "Most lectures"], ["minutes", "Most listening time"]].map(([value, text]) => el("option", { value, text })));
  if ([...sort.options].some(option => option.value === params.get("tag_order"))) sort.value = params.get("tag_order");
  if (search.value || params.has("tag_dimension") || params.has("tag_order")) root.open = true;
  const count = el("p", { class: "muted", role: "status" });
  const result = el("div", { class: "coverage-tree" });
  root.append(el("div", { class: "filters" }, el("label", {}, "Dimension", facet), el("label", { class: "coverage-search" }, "Find a tag", search), el("label", {}, "Order", sort)), count,
    el("details", { class: "coverage-count-help" }, el("summary", { text: "How these counts work" }), el("p", { class: "muted coverage-explanation", text: "Sections group installments by their authored section within a content pack; unsectioned lectures count separately. They are editorial groupings, not a count of distinct works. Expand any row to see which sections contribute its lectures. Place associations describe origins, settings, and context; missing tags remain unclassified. Branches can overlap, so their totals are not additive." })),
    el("div", { class: "coverage-columns", "aria-hidden": "true" }, el("span", { text: "Tag" }), el("span", { text: "Sections" }), el("span", { text: "Lectures" }), el("span", { text: "Est. listening" })), result);
  function draw() {
    const query = search.value.trim().toLocaleLowerCase();
    const state = new URLSearchParams(location.search);
    for (const [key, value] of [["tag_q", search.value], ["tag_dimension", facet.value === "Places" ? "" : facet.value], ["tag_order", sort.value === "name" ? "" : sort.value]])
      if (value) state.set(key, value); else state.delete(key);
    history.replaceState(history.state, "", location.pathname + (state.size ? "?" + state : "") + location.hash);
    const lectureHref = row => lectureURL(row.id) + "?" + new URLSearchParams({ return: "/stats" + (state.size ? "?" + state : "") + "#stats-section-coverage" });
    const matches = node => !query || node.label.toLocaleLowerCase().includes(query) || [...node.children.values()].some(matches);
    function lectureList(rows) {
      const root = el("div", { class: "coverage-lecture-list" });
      const list = el("ul");
      const show = limit => list.replaceChildren(...rows.slice(0, limit).map(row => el("li", {},
        link(row.title, lectureHref(row)),
        el("small", { class: "muted", text: formatMinutes((row.words || 0) / 145) }))));
      show(10);
      root.append(list);
      if (rows.length > 10) {
        const all = el("button", { type: "button", text: `Show all ${rows.length.toLocaleString()} lectures`, onclick: () => { show(rows.length); all.remove(); } });
        root.append(all);
      }
      return root;
    }
    function lecturesIn(node) {
      const rows = model.totals(node).groups.flatMap(group => group.members).sort((a, b) => a.title.localeCompare(b.title) || a.id.localeCompare(b.id));
      const list = el("details", { class: "coverage-tag-lectures", open: !node.children.size },
        el("summary", { text: `Lectures (${rows.length.toLocaleString()})` }));
      const fill = () => { if (list.open && list.children.length === 1) list.append(lectureList(rows)); };
      fill();
      list.addEventListener("toggle", fill);
      return list;
    }
    function contributions(node, open = false) {
      const data = model.totals(node);
      const groups = el("div", { class: "coverage-contributions" });
      const list = el("ul");
      const groupTitle = group => group.section ? group.section.replaceAll("-", " ").replace(/^./, first => first.toUpperCase()) : group.first.title;
      const show = limit => list.replaceChildren(...data.groups.slice(0, limit).map(group => {
        const share = `${group.lectures.toLocaleString()} lecture${group.lectures === 1 ? "" : "s"} · ${Math.round(group.lectures / data.lectures * 100)}%`;
        const pack = el("small", { class: "muted", text: packNames.get(group.namespace) || group.namespace });
        if (group.lectures === 1) return el("li", {},
          el("span", {}, link(group.first.title, lectureHref(group.first)), pack), el("span", { text: share }));
        const section = el("details", { class: "coverage-group" }, el("summary", {},
          el("span", {}, groupTitle(group), pack), el("span", { text: share })));
        section.addEventListener("toggle", () => {
          if (section.open && section.children.length === 1) section.append(lectureList(group.members));
        });
        return el("li", { class: "coverage-group-item" }, section);
      }));
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
          link(data.lectures.toLocaleString(), "/lectures?" + new URLSearchParams({ tag: node.label })),
          el("span", { "aria-label": "Estimated listening time", text: formatMinutes(data.minutes) })));
        const expand = () => {
          if (details.children.length > 1) return;
          details.append(lecturesIn(node));
          if (node.children.size) details.append(level(node.children, inheritedMatch || Boolean(query && node.label.toLocaleLowerCase().includes(query))));
          if (data.lectures > 1) details.append(contributions(node, Boolean(node.children.size) && (!query || node.label.toLocaleLowerCase().includes(query))));
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

import { tagLabels } from "./tag-model.mjs";
import { reactionControls } from "./reactions.mjs";
import { el } from "./api.mjs";
import { allLectureRows } from "./all-lectures-model.mjs";
import { chronologyOptions, dateOrder } from "./chronology.mjs";

export function renderAllLectures(main, catalog, { item, link, reactions }) {
  const params = new URLSearchParams(location.search);
  const lectures = catalog.lectures || [];
  const total = new Set(lectures.map(row => row.id)).size;
  const query = el("input", { id: "all-lectures-search", type: "search", class: "library-search",
    "aria-label": "Search all lectures", placeholder: "Title, author, description, place, period, or ID", value: params.get("q") || "" });
  function select(label, options, initial) {
    const control = el("select", { "aria-label": label }, ...options.map(([value, text]) => el("option", { value, text })));
    control.value = initial || "";
    return control;
  }
  const categories = [...new Set(lectures.flatMap(row => row.categories || []))].sort();
  const category = select("Category", [["", "All categories"], ...categories.map(name => [name, name])], params.get("category"));
  const packs = new Map((catalog.packs || []).map(pack => [pack.id, pack.title || pack.id]));
  for (const row of lectures) {
    const id = row.origin?.pack || row.namespace;
    if (id && !packs.has(id)) packs.set(id, id);
  }
  const pack = select("Content pack", [["", "All packs"], ...[...packs].sort((a, b) => a[1].localeCompare(b[1]))], params.get("pack"));
  const audio = select("Audio availability", [["", "All audio states"], ["ready", "Complete audio"], ["partial", "Partial audio only"], ["missing", "No prepared audio"]], params.get("audio"));
  const personal = select("Your feedback", [["", "All lectures"], ["favorites", "♥ Favorites"], ["rated", "Rated"], ["unrated", "Not rated"], ["4", "4 stars and above"], ["5", "5 stars"]], params.get("personal"));
  const sort = select("Sort all lectures", [["rating", "Your highest rated"], ["title", "Title A–Z"], ["id", "Lecture ID"], ["short", "Shortest first"], ["long", "Longest first"]], params.get("sort") || "title");
  sort.append(...chronologyOptions());
  sort.value = params.get("sort") || "title";
  if (!sort.value) sort.value = "title";
  const tags = el("datalist", { id: "all-lecture-tags" }, ...[...new Set(lectures.flatMap(tagLabels))].sort().map(value => el("option", { value })));
  const tag = el("input", { type: "search", list: "all-lecture-tags", "aria-label": "Tag",
    placeholder: "Topic, place, author, or period", value: params.get("tag") || "" });
  const count = el("p", { class: "muted", role: "status", "aria-live": "polite" });
  const results = el("div");
  const clear = el("button", { type: "button", text: "Clear filters" });
  const showAll = el("button", { type: "button" });
  let limit = params.get("show") === "all" ? Math.max(100, total)
    : Number.isSafeInteger(history.state?.allLecturesLimit) ? Math.max(100, history.state.allLecturesLimit) : 100;
  main.replaceChildren(el("h1", { text: "All lectures" }),
    el("p", { class: "intro", text: "Every available lecture in one list, including deep dives and items outside curated routes. Each lecture appears once. Search or filter the list, or show everything at once." }),
    el("p", {}, link("Browse collections", "/collections"), " · ", link("View content stats", "/stats")),
    query,
    el("details", { class: "browsing-options", open: Boolean(params.get("category") || params.get("pack") || params.get("tag") || params.get("audio") || params.get("personal")) },
      el("summary", { text: "Filter and sort" }),
      el("div", { class: "filters" }, el("label", {}, "Category", category), el("label", {}, "Content pack", pack),
        el("label", {}, "Tag", tag, tags), el("label", {}, "Audio", audio), el("label", {}, "Your feedback", personal), el("label", {}, "Order", sort))),
    el("div", { class: "actions all-lectures-status" }, count, showAll, clear), results);
  function update() {
    const filters = { q: query.value.trim(), category: category.value, pack: pack.value, tag: tag.value.trim(), audio: audio.value, personal: personal.value, sort: sort.value };
    const search = new URLSearchParams(Object.entries(filters).filter(([key, value]) => value && !(key === "sort" && value === "title")));
    if (limit >= total && total > 100) search.set("show", "all");
    const returnTo = "/lectures" + (search.size ? "?" + search : "");
    history.replaceState({ ...history.state, allLecturesLimit: limit }, "", returnTo);
    const rows = allLectureRows(lectures, filters, reactions?.records);
    const visible = rows.slice(0, limit);
    count.textContent = `${visible.length.toLocaleString()} shown · ${rows.length.toLocaleString()} matching · ${total.toLocaleString()} total lectures`;
    clear.hidden = ![filters.q, filters.category, filters.pack, filters.tag, filters.audio, filters.personal].some(Boolean) && filters.sort === "title";
    showAll.hidden = rows.length <= limit;
    showAll.textContent = `Show all ${rows.length.toLocaleString()} matching lectures`;
    showAll.onclick = () => { limit = Math.max(total, rows.length); update(); };
    const list = el("ul", { class: "list all-lectures-list" }, ...visible.map(row => {
      const node = item(row, dateOrder(sort.value)?.axis);
      node.dataset.lectureId = row.id;
      const anchor = node.querySelector(".copy > a");
      const target = new URL(anchor.href, location.origin);
      target.searchParams.set("return", returnTo);
      anchor.href = target.pathname + target.search;
      node.querySelector(".copy").append(el("small", { class: "lecture-identity", text: `${row.id} · ${packs.get(row.origin?.pack || row.namespace) || row.namespace || ""}` }));
      if (reactions) node.append(reactionControls(row, reactions, { compact: true }));
      return node;
    }));
    results.replaceChildren(list);
    if (!rows.length) results.append(el("p", { class: "notice", text: total ? "No lectures match these filters." : "No lectures are available yet. Add a content pack to begin." }));
    if (rows.length > limit) {
      const more = el("button", { type: "button", text: "Show 100 more", onclick: () => { limit += 100; update(); } });
      const all = el("button", { type: "button", text: `Show all ${rows.length.toLocaleString()} matching lectures`, onclick: () => { limit = Math.max(total, rows.length); update(); } });
      results.append(el("div", { class: "actions" }, more, all));
    }
  }
  for (const control of [query, category, pack, tag, audio, personal, sort]) {
    control.addEventListener(control === query || control === tag ? "input" : "change", () => { limit = 100; update(); });
  }
  clear.onclick = () => {
    for (const control of [query, category, pack, tag, audio, personal]) control.value = "";
    sort.value = "title";
    limit = 100;
    update();
  };
  update();
  reactions?.watch(results, () => {
    if (personal.value || sort.value === "rating") update();
  });
}

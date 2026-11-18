import { tagLabels } from "./tag-model.mjs";
import { inventoryItem, lectureView, initialLectureLimit } from "./all-lecture-views.mjs";
import { el, getStored, store } from "./api.mjs";
import { allLectureRows } from "./all-lectures-model.mjs";
import { chronologyOptions, dateOrder, chronologyRecord, dateAxes } from "./chronology.mjs";

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
  const view = select("Lecture view", [["compact", "Concise list"], ["detail", "Detailed list"], ["cards", "Cards"]],
    lectureView(params.get("view"), getStored("all-lectures-view", "compact")));
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
  const dateState = select("Date coverage", [["", "All date states"], ["dated", "Dated only"], ["undated", "Without dates"]], params.get("date"));
  const dateFilter = el("label", {}, "Date coverage", dateState);
  const coverage = el("p", { class: "muted date-coverage", role: "status" });
  const tags = el("datalist", { id: "all-lecture-tags" }, ...[...new Set(lectures.flatMap(tagLabels))].sort().map(value => el("option", { value })));
  const tag = el("input", { type: "search", list: "all-lecture-tags", "aria-label": "Tag",
    placeholder: "Topic, place, author, or period", value: params.get("tag") || "" });
  const count = el("p", { class: "muted", role: "status", "aria-live": "polite" });
  const results = el("div");
  const clear = el("button", { type: "button", text: "Clear filters" });
  const showAll = el("button", { type: "button" });
  let limit = params.get("show") === "all" ? Math.max(initialLectureLimit(view.value), total)
    : Number.isSafeInteger(history.state?.allLecturesLimit) ? Math.max(initialLectureLimit(view.value), history.state.allLecturesLimit) : initialLectureLimit(view.value);
  main.replaceChildren(el("div", { class: "inventory-heading" }, el("h1", { text: "All lectures" }),
    el("p", {}, link("Browse collections", "/collections"), " · ", link("Content stats", "/stats"))),
    query,
    el("details", { class: "browsing-options", open: Boolean(params.get("category") || params.get("pack") || params.get("tag") || params.get("audio") || params.get("personal") || params.get("date")) },
      el("summary", { text: "Filter and sort" }),
      el("div", { class: "filters" }, el("label", {}, "Category", category), el("label", {}, "Content pack", pack),
        el("label", {}, "Tag", tag, tags), el("label", {}, "Audio", audio), el("label", {}, "Your feedback", personal), el("label", {}, "Order", sort), dateFilter)),
    el("div", { class: "actions all-lectures-status" }, count, el("label", { class: "inventory-view" }, "View", view), showAll, clear), coverage, results);
  function update() {
    const filters = { q: query.value.trim(), category: category.value, pack: pack.value, tag: tag.value.trim(), audio: audio.value, personal: personal.value, sort: sort.value, date: dateOrder(sort.value) ? dateState.value : "" };
    const search = new URLSearchParams(Object.entries(filters).filter(([key, value]) => value && !(key === "sort" && value === "title")));
    search.set("view", view.value);
    if (limit >= total && total > initialLectureLimit(view.value)) search.set("show", "all");
    const returnTo = "/lectures" + (search.size ? "?" + search : "");
    history.replaceState({ ...history.state, allLecturesLimit: limit }, "", returnTo);
    const rows = allLectureRows(lectures, filters, reactions?.records);
    const axis = dateOrder(sort.value)?.axis;
    dateFilter.hidden = !axis;
    coverage.hidden = !axis;
    if (axis) {
      const candidates = allLectureRows(lectures, { ...filters, date: "" }, reactions?.records);
      const dated = candidates.filter(row => chronologyRecord(row, axis)).length;
      coverage.textContent = `${dateAxes[axis]} dates: ${dated.toLocaleString()} / ${candidates.length.toLocaleString()} matching lectures. Undated items follow; their order does not indicate age.`;
    }
    const visible = rows.slice(0, limit);
    count.textContent = `${visible.length.toLocaleString()} shown · ${rows.length.toLocaleString()} matching · ${total.toLocaleString()} total lectures`;
    clear.hidden = ![filters.q, filters.category, filters.pack, filters.tag, filters.audio, filters.personal, filters.date].some(Boolean) && filters.sort === "title";
    showAll.hidden = rows.length <= limit;
    showAll.textContent = `Show all ${rows.length.toLocaleString()} matching lectures`;
    showAll.onclick = () => { limit = Math.max(total, rows.length); update(); };
    const list = el("ul", { class: `list all-lectures-list view-${view.value}` }, ...visible.map(row => inventoryItem(row, view.value, {
      item, link, reactions, packs, returnTo, axis: dateOrder(sort.value)?.axis,
    })));
    results.replaceChildren(list);
    if (!rows.length) results.append(el("p", { class: "notice", text: total ? "No lectures match these filters." : "No lectures are available yet. Add a content pack to begin." }));
    if (rows.length > limit) {
      const more = el("button", { type: "button", text: "Show 100 more", onclick: () => { limit += 100; update(); } });
      const all = el("button", { type: "button", text: `Show all ${rows.length.toLocaleString()} matching lectures`, onclick: () => { limit = Math.max(total, rows.length); update(); } });
      results.append(el("div", { class: "actions" }, more, all));
    }
  }
  for (const control of [query, category, pack, tag, audio, personal, sort, dateState]) {
    control.addEventListener(control === query || control === tag ? "input" : "change", () => { limit = initialLectureLimit(view.value); update(); });
  }
  view.onchange = () => {
    store("all-lectures-view", view.value);
    limit = Math.max(limit, initialLectureLimit(view.value));
    update();
  };
  clear.onclick = () => {
    for (const control of [query, category, pack, tag, audio, personal, dateState]) control.value = "";
    sort.value = "title";
    limit = initialLectureLimit(view.value);
    update();
  };
  update();
  reactions?.watch(results, () => {
    if (personal.value || sort.value === "rating") update();
  });
}

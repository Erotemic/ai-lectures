import { el, getStored, store } from "./api.mjs";
import { preparationPanel } from "./narration.mjs";
import { collectionRows, collectionAncestors, collectionSections, formatMinutes, matchesLecture } from "./browse-model.mjs";

const roleLabel = (collection) => ({ main: "Guided route", deep_dive: "Deep dive", hub: "Route guide", archive: "Complete sequence" })[collection.role] || "Collection";

export function collectionGroups(collections) {
  const groups = new Map();
  for (const collection of collections) {
    for (const category of collection.categories || ["Other collections"]) {
      const group = groups.get(category) || {
        title: category,
        collections: [],
        children: false,
      };
      group.collections.push(collection);
      group.children ||= collection.audiences?.includes("children") || false;
      groups.set(category, group);
    }
  }
  return [...groups.values()].sort(
    (a, b) =>
      Number(b.children) - Number(a.children) || a.title.localeCompare(b.title),
  );
}

export function rootCollections(collections) {
  const installed = new Set(collections.map((collection) => collection.id));
  return collections.filter(
    (collection) => !installed.has(collection.parent_id),
  );
}

export class CatalogBrowser {
  constructor(context) {
    Object.assign(this, context);
  }
  item(row, collection = null) {
    const saved = this.progress()[row.id];
    return el(
      "li",
      {},
      el(
        "div",
        { class: "copy" },
        this.link(row.title, this.itemURL(row.id, collection)),
        el("small", {
          text: `${formatMinutes(row.estimated_minutes || (row.words || 0) / 145)}${saved?.legacy ? " · Old reader: passage " + (saved.legacy.page_index + 1) : saved?.completed ? " · Completed" : saved ? " · In progress" : ""}`,
        }),
        (row.short_format_reason || row.metadata?.short_format_reason)
          ? el("small", { class: "format-note", text: row.short_format_reason || row.metadata.short_format_reason })
          : null,
      ),
      this.badge(row),
    );
  }
  card(collection, origin = null) {
    const rows = collectionRows(collection, this.catalog().courses, this.byId);
    const completed = rows.filter(
      (row) => this.progress()[row.id]?.completed,
    ).length;
    return el(
      "article",
      { class: "card" },
      el("div", { class: "eyebrow", text: roleLabel(collection) }),
      el("h3", {}, this.link(collection.series_title || collection.title, this.routeURL(collection, origin))),
      collection.age_range_label
        ? el("span", { class: "badge", text: collection.age_range_label })
        : null,
      collection.sequence_recommended
        ? el("small", { class: "series-order", text: "Listen in episode order" })
        : null,
      el("p", { class: "collection-summary", text: collection.summary || "" }),
      el("small", {
        text: collection.lectures.length
          ? `${rows.length} items · ${formatMinutes(rows.reduce((minutes, row) => minutes + (row.estimated_minutes || (row.words || 0) / 145), 0))} · ${rows.filter(this.ready).length} ready${completed ? " · " + completed + " completed" : ""}`
          : `${this.catalog().courses.filter(c => c.parent_id === collection.id && c.role !== "archive").length} routes · ${rows.length} unique items`,
      }),
    );
  }
  continuation(allowed = null) {
    const rows = Object.values(this.progress())
      .filter(
        (p) =>
          !p.completed &&
          this.byId(p.lecture_id) &&
          (!allowed || allowed.has(p.lecture_id)),
      )
      .sort((a, b) => (b.updated_at || "").localeCompare(a.updated_at || ""))
      .slice(0, 4);
    if (!rows.length) return null;
    return el(
      "section",
      { class: "section" },
      el("h2", { text: "Continue listening" }),
      el(
        "ul",
        { class: "list" },
        ...rows.map((p) => this.item(this.byId(p.lecture_id), p.course_id)),
      ),
    );
  }
  browse(main, collectionsOnly = false) {
    const data = this.catalog(),
      key = "browse:" + this.listener();
    const listenerChanged =
      this.previousListener !== undefined &&
      this.previousListener !== this.listener();
    this.previousListener = this.listener();
    const query = new URLSearchParams(listenerChanged ? "" : location.search);
    const explicit = ["category", "audience", "q", "audio", "all", "view", "sort"].some(
      (field) => query.has(field),
    );
    const saved = explicit ? {} : getStored(key, {});
    const initial = (field) => query.get(field) || saved[field] || "";
    const heading = el("h1");
    const search = el("input", {
      type: "search",
      "aria-label": "Search items and collections",
      placeholder: "Search items and collections",
      value: initial("q"),
    });
    const categories = el(
      "select",
      { "aria-label": "Category" },
      el("option", { value: "", text: "All categories" }),
      ...collectionGroups(data.courses).map((group) =>
        el("option", { value: group.title, text: group.title }),
      ),
    );
    categories.value = initial("category");
    const audiences = el(
      "select",
      { "aria-label": "Audience" },
      el("option", { value: "", text: "All listeners" }),
      ...[...new Set(data.courses.flatMap((c) => c.audiences || []))]
        .sort()
        .map((audience) =>
          el("option", {
            value: audience,
            text: audience
              .replaceAll("-", " ")
              .replace(/^./, (c) => c.toUpperCase()),
          }),
        ),
    );
    audiences.value = initial("audience");
    const audio = el(
      "select",
      { "aria-label": "Audio availability" },
      el("option", { value: "", text: "All items" }),
      el("option", { value: "ready", text: "Ready to play" }),
      el("option", { value: "partial", text: "Has audio" }),
    );
    audio.value = initial("audio");
    const view = el("select", { "aria-label": "Collection depth" },
      el("option", { value: "", text: "Starting routes" }),
      el("option", { value: "all", text: "Every collection and deep dive" }),
    );
    view.value = initial("view");
    const sort = el("select", { "aria-label": "Sort results" },
      el("option", { value: "", text: "Recommended order" }),
      el("option", { value: "title", text: "Title A–Z" }),
      el("option", { value: "short", text: "Shortest first" }),
      el("option", { value: "long", text: "Longest first" }),
    );
    sort.value = initial("sort");
    let limit = Number.isInteger(history.state?.browseLimit) ? Math.max(24, history.state.browseLimit) : 24;
    const base = collectionsOnly ? "/collections" : "/";
    const results = el("div");
    const filters = el(
      "details",
      { class: "browsing-options" },
      el("summary", { text: "Browsing options" }),
      el(
        "div",
        { class: "filters" },
        el("label", {}, "Category", categories),
        el("label", {}, "Audience", audiences),
        el("label", {}, "Audio", audio),
        el("label", {}, "Collections", view),
        el("label", {}, "Order", sort),
      ),
    );
    filters.open = Boolean(categories.value || audiences.value || audio.value || view.value || sort.value);
    search.className = "library-search";
    main.replaceChildren(
      heading,
      el("p", {
        class: "intro",
        text: "Follow a guided route, explore a deep dive, or find a single lecture. Your place is saved as you listen.",
      }),
      el(
        "div",
        { class: "actions" },
        this.link("Browse all categories", base + "?all=1"),
        this.link("References and reading", "/references"),
      ),
      search,
      filters,
      results,
    );
    const update = () => {
      const state = {
        category: categories.value,
        audience: audiences.value,
        q: search.value,
        audio: audio.value,
        view: view.value,
        sort: sort.value,
      };
      store(key, state);
      const params = new URLSearchParams(
        Object.entries(state).filter(([, value]) => value),
      );
      history.replaceState(
        { ...history.state, browseLimit: limit },
        "",
        base + "?" + (params.size ? params : "all=1"),
      );
      heading.textContent =
        state.category ||
        (collectionsOnly ? "Collections" : "What would you like to hear?");
      document.title = heading.textContent + " · AI Lectures";
      const available = (row) =>
        !state.audio ||
        (state.audio === "ready" ? this.ready(row) : row?.recordings.length);
      const filtered = data.courses.filter(
        (c) =>
          (!state.category || c.categories?.includes(state.category)) &&
          (!state.audience || c.audiences?.includes(state.audience)) &&
          (!state.audio || collectionRows(c, data.courses, this.byId).some(available)),
      );
      const allowed = new Set(
        data.lectures
          .filter(
            (row) =>
              (!state.category || row.categories?.includes(state.category)) &&
              (!state.audience || row.audiences?.includes(state.audience)) &&
              available(row),
          )
          .map((row) => row.id),
      );
      const q = state.q.trim().toLocaleLowerCase();
      const collections = (q || state.view === "all" ? filtered : rootCollections(filtered)).filter(
        (c) => !q || `${c.title} ${c.series_title || ""} ${c.id} ${c.summary}`.toLocaleLowerCase().includes(q),
      );
      const rows = data.lectures.filter(
        (row) =>
          allowed.has(row.id) &&
          matchesLecture(row.id, this.byId, q),
      );
      if (state.sort) {
        const duration = (c) => collectionRows(c, data.courses, this.byId).reduce((sum, row) => sum + (row.estimated_minutes || (row.words || 0) / 145), 0);
        collections.sort((a, b) => state.sort === "title" ? a.title.localeCompare(b.title) : (duration(a) - duration(b)) * (state.sort === "long" ? -1 : 1));
        rows.sort((a, b) => state.sort === "title" ? a.title.localeCompare(b.title) : ((a.estimated_minutes || 0) - (b.estimated_minutes || 0)) * (state.sort === "long" ? -1 : 1));
      }
      results.replaceChildren();
      if (state.category || state.audience || state.audio || q || state.view || state.sort)
        results.append(el("div", { class: "browse-status" },
          el("small", { text: [state.category, state.audience, state.audio && audio.selectedOptions[0].text, q && `Search: “${state.q}”`, state.view && "All collections", state.sort && sort.selectedOptions[0].text].filter(Boolean).join(" · ") }),
          this.button("Clear filters", () => {
            for (const input of [search, categories, audiences, audio, view, sort]) input.value = "";
            limit = 24;
            update();
          }),
        ));
      if (!q && !state.category && !state.view && !state.sort) {
        const groups = collectionGroups(rootCollections(filtered));
        const categoryLink = (group) => {
          const node = this.link(
            group.title,
            group.collections.length === 1
              ? this.courseLink(group.collections[0])
              : base + "?category=" + encodeURIComponent(group.title),
          );
          node.addEventListener("click", () =>
            store(key, { ...state, category: group.title, q: "" }),
          );
          return node;
        };
        const continuation = this.continuation(allowed);
        if (!collectionsOnly && continuation) results.append(continuation);
        results.append(
          el(
            "section",
            { class: "section", "aria-label": "Browse categories" },
            el("h2", { text: "Browse by category" }),
            el(
              "div",
              { class: "grid category-grid" },
              ...groups.map((group) =>
                el(
                  "article",
                  { class: "card" },
                  el("h3", {}, categoryLink(group)),
                  el("p", {
                    text: `${group.collections.length} ${group.collections.length === 1 ? "collection" : "collections"} · ${data.lectures.filter((row) => row.categories?.includes(group.title)).length} items`,
                  }),
                ),
              ),
            ),
          ),
        );
      } else {
        results.append(
          el(
            "section",
            { class: "section" },
            el("h2", { text: `${collections.length} collections` }),
            el(
              "div",
              { class: "grid" },
              ...collections.map((c) => this.card(c)),
            ),
          ),
        );
        if (!collectionsOnly || q) {
          const section = el(
            "section",
            { class: "section" },
            el("h2", { text: `${rows.length} items` }),
            el(
              "ul",
              { class: "list" },
              ...rows.slice(0, limit).map((row) => this.item(row)),
            ),
          );
          if (rows.length > limit)
            section.append(
              this.button("Show more items", () => {
                limit += 60;
                update();
              }),
            );
          results.append(section);
        }
      }
      if (!data.lectures.length)
        results.append(
          el("p", {
            class: "notice",
            text: "No content packs are installed yet. Add a pack in Packs.",
          }),
        );
      else if (!filtered.length || (q && !collections.length && !rows.length))
        results.append(
          el("p", {
            class: "muted",
            text: "No items match these browsing choices. Choose all categories or change the filters.",
          }),
        );
    };
    for (const input of [search, categories, audiences, audio, view, sort])
      input.addEventListener(input === search ? "input" : "change", () => {
        limit = 24;
        update();
      });
    update();
  }
  collection(main, id) {
    const courses = this.catalog().courses;
    const collection = courses.find((c) => c.id === id);
    if (!collection) throw Error("This collection is not installed.");
    const params = new URLSearchParams(location.search);
    const origin = courses.find(c => c.id === params.get("from") && c.id !== id);
    const ancestors = collectionAncestors(collection, courses);
    const rows = collectionRows(collection, courses, this.byId);
    const directRows = collection.lectures.map(this.byId).filter(Boolean);
    const children = courses.filter(c => c.parent_id === id);
    const branches = children.filter(c => c.role !== "archive");
    const completed = directRows.filter(row => this.progress()[row.id]?.completed).length;
    const inProgress = directRows.filter(row => this.progress()[row.id] && !this.progress()[row.id].completed)
      .sort((a, b) => (this.progress()[b.id].updated_at || "").localeCompare(this.progress()[a.id].updated_at || ""));
    const next = inProgress[0] || directRows.find(row => !this.progress()[row.id]?.completed) || directRows[0];
    const start = next ? this.link(Object.keys(this.progress()).some(key => collection.lectures.includes(key)) ? "Continue collection →" : "Start collection →", this.itemURL(next.id, id)) : null;
    const refreshStart = () => { if (start) start.href = this.itemURL(next.id, id); };
    const breadcrumbs = el("nav", { class: "breadcrumbs", "aria-label": "Breadcrumb" },
      this.link("Library", "/?all=1"),
      ...ancestors.map(c => this.link(c.series_title || c.title, this.courseLink(c))),
      el("span", { "aria-current": "page", text: collection.series_title || collection.title }),
    );
    const summary = collection.summary ? el("p", { class: "intro hero-summary", id: "route-description", text: collection.summary }) : null;
    const summaryToggle = collection.summary?.length > 220 ? this.button("Read more", () => {
      const expanded = summary.classList.toggle("expanded");
      summaryToggle.textContent = expanded ? "Read less" : "Read more";
      summaryToggle.setAttribute("aria-expanded", String(expanded));
    }) : null;
    if (summaryToggle) {
      summaryToggle.className = "summary-toggle";
      summaryToggle.setAttribute("aria-expanded", "false");
      summaryToggle.setAttribute("aria-controls", "route-description");
    }
    const hero = el("section", { class: "collection-hero" },
      el("div", { class: "eyebrow", text: roleLabel(collection) }),
      el("h1", { text: collection.series_title || collection.title }),
      collection.age_range_label ? el("span", { class: "badge", text: collection.age_range_label }) : null,
      summary, summaryToggle,
      el("div", { class: "collection-stats" },
        el("span", { text: collection.lectures.length ? `${collection.lectures.length} items` : `${branches.length} routes · ${rows.length} unique items` }),
        collection.lectures.length ? el("span", { text: formatMinutes(directRows.reduce((sum, row) => sum + (row.estimated_minutes || (row.words || 0) / 145), 0)) }) : null,
        el("span", { text: `${rows.filter(this.ready).length} ready to play` }),
        completed ? el("span", { text: `${completed} completed` }) : null,
        collection.sequence_recommended ? el("span", { text: "Listen in episode order" }) : null,
      ),
      start ? el("div", { class: "actions collection-start" }, start) : null,
    );
    main.replaceChildren(breadcrumbs);
    if (origin) main.append(el("div", { class: "return-route" }, this.link("← Return to " + (origin.series_title || origin.title), this.courseLink(origin))));
    main.append(hero);
    // Production and reference tools remain available without preceding the contents.
    const resources = el("aside", { class: "collection-resources", "aria-label": "Collection resources" },
      el("h2", { text: "Resources & connections" }),
      this.link("References and reading", "/references?" + new URLSearchParams({ course_id: id })),
      this.link("All collections", "/collections?all=1"),
    );
    if (collection.background)
      resources.append(el("details", {}, el("summary", { text: "Background and prerequisites" }),
        el("p", { text: Array.isArray(collection.background) ? collection.background.join("; ") : collection.background }),
      ));
    if (collection.preparation_collections?.length)
      resources.append(el("details", {}, el("summary", { text: "Suggested preparation" }),
        el("div", { class: "route-links" }, ...collection.preparation_collections.map(key => this.routeLink(key, null, id))),
      ));
    const related = (collection.related_collections || []).filter(key => !ancestors.some(c => c.id === key));
    if (related.length)
      resources.append(el("details", {}, el("summary", { text: "Related routes" }),
        el("div", { class: "route-links" }, ...related.map(key => this.routeLink(key, null, id))),
      ));
    const archives = children.filter(c => c.role === "archive");
    if (archives.length)
      resources.append(el("details", {}, el("summary", { text: "Full collections" }),
        el("div", { class: "route-links" }, ...archives.map(c => this.routeLink(c.id, null, id))),
      ));
    if (directRows.some(row => row.kind === "audio")) {
      const preparation = el("details", {}, el("summary", { text: "Prepare recordings" }));
      let loaded = false;
      preparation.ontoggle = () => {
        if (preparation.open && !loaded) {
          loaded = true;
          preparation.append(preparationPanel({ courseId: id, label: "Prepare recordings", description: "Queue every installed audio item in this collection for the selected narrator." }));
        }
      };
      resources.append(preparation);
    }
    const contents = el("div", { class: "collection-contents" });
    if (branches.length) {
      const branchCards = el("div", { class: "grid" }, ...branches.map(c => this.card(c, id)));
      if (collection.lectures.length) {
        contents.append(el("details", { class: "deep-dive-routes" },
          el("summary", { text: `Explore further · ${branches.length} routes` }), branchCards,
        ));
      } else contents.append(el("h2", { text: "Choose a route" }), branchCards);
    }
    if (collection.lectures.length) this.collectionContents(contents, collection, refreshStart);
    main.append(el("div", { class: "collection-layout" }, contents, resources));
  }
  collectionContents(contents, collection, refreshStart) {
    const id = collection.id;
    const sections = collectionSections(collection, this.byId);
    const flat = collection.lectures.length <= 12 && sections.every(section =>
      !section.sessions?.length && !section.collection && (sections.length === 1 || section.lectures.length === 1));
    const params = new URLSearchParams(location.search);
    const search = el("input", { id: "collection-search", type: "search", placeholder: "Search titles, topics, or IDs", "aria-label": "Search this collection", value: params.get("find") || "" });
    const jump = el("select", { "aria-label": "Jump to section" },
      el("option", { value: "", text: "Jump to a section…" }),
      ...sections.flatMap(section => [
        el("option", { value: section.id, text: section.title }),
        ...(section.sessions || []).map(session => el("option", { value: session.id, text: "  ↳ " + session.title })),
      ]),
    );
    const count = el("small", { role: "status", "aria-live": "polite" });
    const results = el("div", { class: "collection-sections" });
    const openedKey = `contents:${this.listener()}:${id}`;
    const openState = getStored(openedKey, {});
    const controls = el("div", { class: "contents-controls" }, search,
      el("div", { class: "actions" }, sections.length > 1 || sections.some(s => s.sessions?.length) ? jump : null,
        !flat ? this.button("Expand all", () => results.querySelectorAll("details").forEach(d => { d.open = true; })) : null,
        !flat ? this.button("Collapse all", () => results.querySelectorAll("details").forEach(d => { d.open = false; })) : null,
        this.button("Clear search", () => { search.value = ""; update(); search.focus(); }),
      ), count,
    );
    contents.append(el("h2", { class: "contents-heading", text: collection.audiences?.includes("children") && /stor/i.test(collection.genre || "") ? "Stories" : "Contents" }), controls, results);
    const update = () => {
      const q = search.value.trim().toLocaleLowerCase();
      const url = new URL(location.href);
      if (q) url.searchParams.set("find", search.value);
      else url.searchParams.delete("find");
      history.replaceState(history.state, "", url);
      refreshStart();
      results.replaceChildren();
      let shown = 0;
      for (const section of sections) {
        const wholeSection = Boolean(q && section.title.toLocaleLowerCase().includes(q));
        const sourceGroups = section.sessions?.length ? section.sessions : [{ lectures: section.lectures }];
        const groups = sourceGroups.map(group => ({ ...group, lectures: group.lectures.filter(key => !q || wholeSection || group.title?.toLocaleLowerCase().includes(q) || matchesLecture(key, this.byId, q)) })).filter(group => group.lectures.length);
        if (!groups.length) continue;
        const keys = groups.flatMap(group => group.lectures);
        shown += keys.length;
        if (flat) {
          const list = el("ol", { class: "list", id: section.id, tabindex: "-1" });
          for (const key of keys) this.appendItem(list, key, id);
          results.append(list);
          continue;
        }
        const minutes = keys.reduce((sum, key) => sum + (this.byId(key)?.estimated_minutes || (this.byId(key)?.words || 0) / 145), 0);
        const done = keys.filter(key => this.progress()[key]?.completed).length;
        const detail = el("details", { class: "contents-section", id: section.id },
          el("summary", {}, el("span", { text: section.title }),
            el("small", { text: `${keys.length} ${keys.length === 1 ? "item" : "items"} · ${formatMinutes(minutes)}${done ? ` · ${done} completed` : ""}` }),
          ),
        );
        detail.open = Boolean(q) || (openState[section.id] ?? (sections.length <= 8 && collection.lectures.length <= 50));
        detail.addEventListener("toggle", () => {
          if (!search.value.trim()) { openState[section.id] = detail.open; store(openedKey, openState); }
        });
        if (section.collection)
          detail.append(el("div", { class: "topic-link" }, this.routeLink(section.collection, "Explore the full topic →", id)));
        for (const group of groups) {
          if (group.title) detail.append(el("h3", { id: group.id, tabindex: "-1", class: "session-heading", text: group.title }));
          const list = el("ol", { class: "list" });
          for (const key of group.lectures) this.appendItem(list, key, id);
          detail.append(list);
        }
        results.append(detail);
      }
      count.textContent = q ? `${shown} of ${collection.lectures.length} items match` : `${collection.lectures.length} items · Collection order`;
      if (!shown) results.append(el("p", { class: "notice", text: "No matching items. Try another title or ID, or clear the search." }));
    };
    search.addEventListener("input", update);
    jump.addEventListener("change", () => {
      if (!jump.value) return;
      // A contents jump deliberately restores the full sequence before locating it.
      if (search.value) { search.value = ""; update(); }
      history.replaceState(history.state, "", location.pathname + location.search + "#" + jump.value);
      refreshStart();
      revealAnchor();
    });
    update();
  }
  routeURL(collection, origin = null) {
    return this.courseLink(collection) + (origin ? "?" + new URLSearchParams({ from: origin }) : "");
  }
  itemURL(id, collection) {
    const href = this.lectureLink(id, collection);
    const current = /^\/(collections|courses)\/(.+)$/.exec(location.pathname);
    if (!current || decodeURIComponent(current[2]) !== collection || !href.startsWith("/lectures/")) return href;
    return href + "&" + new URLSearchParams({ return: location.pathname + location.search + location.hash });
  }
  appendItem(list, key, collection) {
    const row = this.byId(key);
    list.append(row ? this.item(row, collection) : el("li", { text: key + " · Not installed" }));
  }
  routeLink(key, label = null, origin = null) {
    const route = this.catalog().courses.find((course) => course.id === key);
    return route
      ? this.link(label || route.title, this.routeURL(route, origin))
      : el("span", { class: "muted", text: `${label || key} · Not installed` });
  }
}

// Native fragment links and the contents selector share the same reveal behavior.
export function revealAnchor() {
  const target = document.getElementById(location.hash.slice(1));
  if (!target) return false;
  for (let node = target; node; node = node.parentElement)
    if (node.tagName === "DETAILS") node.open = true;
  target.scrollIntoView({ block: "start" });
  const focus = target.tagName === "DETAILS" ? target.querySelector("summary") : target;
  focus?.focus({ preventScroll: true });
  return true;
}

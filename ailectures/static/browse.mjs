import { el, getStored, store } from "./api.mjs";
import { preparationPanel } from "./narration.mjs";

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
        this.link(row.title, this.lectureLink(row.id, collection)),
        el("small", {
          text: `${row.estimated_minutes || Math.round((row.words || 0) / 145)} min${saved?.legacy ? " · Old reader: passage " + (saved.legacy.page_index + 1) : saved?.completed ? " · Completed" : saved ? " · In progress" : ""}`,
        }),
      ),
      this.badge(row),
    );
  }
  card(collection) {
    const rows = collection.lectures.map(this.byId).filter(Boolean);
    const completed = rows.filter(
      (row) => this.progress()[row.id]?.completed,
    ).length;
    return el(
      "article",
      { class: "card" },
      el("h3", {}, this.link(collection.series_title || collection.title, this.courseLink(collection))),
      collection.age_range_label
        ? el("span", { class: "badge", text: collection.age_range_label })
        : null,
      collection.sequence_recommended
        ? el("small", { class: "series-order", text: "Listen in episode order" })
        : null,
      el("p", { class: "collection-summary", text: collection.summary || "" }),
      el("small", {
        text: `${rows.length} items · approximately ${Math.round(rows.reduce((minutes, row) => minutes + (row.estimated_minutes || (row.words || 0) / 145), 0))} min · ${rows.filter(this.ready).length} ready to play${completed ? " · " + completed + " completed" : ""}`,
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
    const explicit = ["category", "audience", "q", "audio", "all"].some(
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
    let limit = 24;
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
      ),
    );
    filters.open = Boolean(categories.value || audiences.value || audio.value);
    search.className = "library-search";
    main.replaceChildren(
      heading,
      el("p", {
        class: "intro",
        text: "Choose what you would like to hear. Collections can include lectures, stories, and other listening.",
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
      };
      store(key, state);
      const params = new URLSearchParams(
        Object.entries(state).filter(([, value]) => value),
      );
      history.replaceState(
        null,
        "",
        base + "?" + (params.size ? params : "all=1"),
      );
      heading.textContent =
        state.category ||
        (collectionsOnly ? "Collections" : "What would you like to hear?");
      const available = (row) =>
        !state.audio ||
        (state.audio === "ready" ? this.ready(row) : row?.recordings.length);
      const filtered = data.courses.filter(
        (c) =>
          (!state.category || c.categories?.includes(state.category)) &&
          (!state.audience || c.audiences?.includes(state.audience)) &&
          (!state.audio || c.lectures.some((id) => available(this.byId(id)))),
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
      const q = state.q.toLocaleLowerCase();
      const collections = (q ? filtered : rootCollections(filtered)).filter(
        (c) => !q || `${c.title} ${c.summary}`.toLocaleLowerCase().includes(q),
      );
      const rows = data.lectures.filter(
        (row) =>
          allowed.has(row.id) &&
          (!q || `${row.title} ${row.id}`.toLocaleLowerCase().includes(q)),
      );
      results.replaceChildren();
      if (!q && !state.category) {
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
        const continuation = this.continuation(allowed);
        if (!collectionsOnly && continuation) results.append(continuation);
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
        if (!collectionsOnly) {
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
    for (const input of [search, categories, audiences, audio])
      input.addEventListener(input === search ? "input" : "change", () => {
        limit = 24;
        update();
      });
    update();
  }
  collection(main, id) {
    const collection = this.catalog().courses.find((c) => c.id === id);
    if (!collection) throw Error("This collection is not installed.");
    const parent = this.catalog().courses.find((c) => c.id === collection.parent_id);
    main.replaceChildren(
      ...[
        el("div", { class: "actions" },
          parent ? this.link("Back to " + parent.title, this.courseLink(parent)) : null,
          this.link("All collections", "/collections?all=1"),
        ),
        el("h1", { text: collection.series_title || collection.title }),
        collection.age_range_label
          ? el("span", { class: "badge", text: collection.age_range_label })
          : null,
        this.link(
          "References for this collection",
          "/references?" + new URLSearchParams({ course_id: id }),
        ),
      ].filter(Boolean),
    );
    const related = (collection.related_collections || []).filter((key) => key !== parent?.id);
    if (related.length)
      main.append(
        el("div", { class: "actions" }, ...related.map((key) => this.routeLink(key))),
      );
    if (collection.preparation_collections?.length)
      main.append(el("details", { class: "section" },
        el("summary", { text: "Suggested preparation" }),
        el("p", { class: "muted", text: "Review the relevant parts of these routes as needed for the stated background." }),
        el("div", { class: "actions" }, ...collection.preparation_collections.map((key) => this.routeLink(key))),
      ));
    if (collection.summary || collection.background)
      main.append(
        el(
          "details",
          { class: "section" },
          el("summary", { text: "About this collection" }),
          el("p", { class: "intro", text: collection.summary || "" }),
          collection.background
            ? el("p", {
                class: "muted",
                text: Array.isArray(collection.background)
                  ? collection.background.join("; ")
                  : collection.background,
              })
            : null,
        ),
      );
    if (collection.lectures.some((key) => this.byId(key)?.kind === "audio")) {
      const preparation = el(
        "details",
        { class: "section" },
        el("summary", { text: "Prepare all recordings in this collection" }),
      );
      let loaded = false;
      preparation.ontoggle = () => {
        if (preparation.open && !loaded) {
          loaded = true;
          preparation.append(
            preparationPanel({
              courseId: id,
              label: "Prepare recordings",
              description:
                "Queue every installed audio item in this collection for the selected narrator.",
            }),
          );
        }
      };
      main.append(preparation);
    }
    const children = this.catalog().courses.filter((c) => c.parent_id === id);
    const branches = children.filter((c) => c.role !== "archive");
    if (branches.length) {
      const details = el("details", { class: "section" },
        el("summary", { text: `Explore further · ${branches.length} ${branches.length === 1 ? "route" : "routes"}` }),
        el("div", { class: "grid" }, ...branches.map((c) => this.card(c))),
      );
      details.open = !collection.lectures.length;
      main.append(details);
    }
    const archives = children.filter((c) => c.role === "archive");
    if (archives.length)
      main.append(el("div", { class: "actions section" }, ...archives.map((c) => this.routeLink(c.id))));
    if (!collection.lectures.length) return;
    main.append(
      el("h2", {
        class: "section",
        text:
          collection.audiences?.includes("children") &&
          /stor/i.test(collection.genre || "")
            ? "Stories"
            : "Items",
      }),
    );
    const list = el("ol", { class: "list" });
    if (collection.chapters?.length) {
      for (const chapter of collection.chapters) {
        list.append(el("li", { class: "section" },
          el("h3", { text: chapter.title }),
          chapter.collection ? this.routeLink(chapter.collection, "Explore the full topic") : null,
        ));
        if (chapter.sessions?.length) {
          for (const session of chapter.sessions) {
            const minutes = Math.round(session.lectures.reduce((sum, key) =>
              sum + (this.byId(key)?.estimated_minutes || 0), 0));
            list.append(el("li", { class: "muted" },
              el("h4", { text: session.title }),
              el("small", { text: `Approximately ${minutes} minutes` }),
            ));
            for (const key of session.lectures) this.appendItem(list, key, id);
          }
        } else {
          for (const key of chapter.lectures) this.appendItem(list, key, id);
        }
      }
    } else {
      let section = null;
      const showSections = new Set(collection.lectures.map((key) => this.byId(key)?.section).filter(Boolean)).size > 1;
      for (const key of collection.lectures) {
        const row = this.byId(key);
        if (showSections && row?.section && row.section !== section) {
          section = row.section;
          list.append(el("li", { class: "muted", text: section.replaceAll("-", " ") }));
        }
        this.appendItem(list, key, id);
      }
    }
    main.append(list);
  }
  appendItem(list, key, collection) {
    const row = this.byId(key);
    list.append(row ? this.item(row, collection) : el("li", { text: key + " · Not installed" }));
  }
  routeLink(key, label = null) {
    const route = this.catalog().courses.find((course) => course.id === key);
    return route
      ? this.link(label || route.title, this.courseLink(route))
      : el("span", { class: "muted", text: `${label || key} · Not installed` });
  }
}

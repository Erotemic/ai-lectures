import { tagLabels } from "./tag-model.mjs";
import { creatorLine } from "./creators.mjs";
import { api, el, getStored, store, randomId } from "./api.mjs";
import { preparationPanel } from "./narration.mjs";
import { collectionRows, collectionAncestors, collectionSections, formatMinutes, matchesLecture, matchesTag } from "./browse-model.mjs";
import { dateOrder, chronologyLine, chronologyOptions, sortChronologically } from "./chronology.mjs";
import { topicLinks } from "./topics.mjs";
import { recentListening, historyRoute } from "./listening-history.mjs";

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
  item(row, collection = null, dateAxis = null) {
    const saved = this.progress()[row.id];
    const title = this.link(row.title, this.itemURL(row.id, collection));
    title.className = "catalog-item-title";
    return el(
      "li",
      { class: "catalog-item" },
      el(
        "div",
        { class: "copy" },
        title,
        creatorLine(row, this.link),
        row.description ? el("p", { class: "lecture-description", text: row.description }) : null,
        topicLinks(row.tags, this.link, 4),
        chronologyLine(row, dateAxis),
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
  card(collection, origin = null, dateAxis = null) {
    const rows = collectionRows(collection, this.catalog().courses, this.byId);
    const completed = rows.filter(
      (row) => this.progress()[row.id]?.completed,
    ).length;
    return el(
      "article",
      { class: "card" },
      el("div", { class: "eyebrow", text: roleLabel(collection) }),
      el("h3", {}, this.link(collection.series_title || collection.title, this.routeURL(collection, origin))),
      chronologyLine(collection, dateAxis),
      topicLinks(collection.tags, this.link, 3),
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
  directorySections(collection, origin = null) {
    const courses = new Map(this.catalog().courses.map(row => [row.id, row]));
    const storageKey = `subject-directory:${this.listener()}:${collection.id}`;
    const opened = getStored(storageKey, {});
    const sections = (collection.browse_sections || []).map((section, index) =>
      el("details", { class: "subject-family", open: opened[section.title] ?? index === 0 },
        el("summary", {}, el("h2", { text: section.title }), el("small", { class: "muted", text: `${section.collections.length} routes` })),
        section.summary ? el("p", { class: "muted", text: section.summary }) : null,
        el("div", { class: "subject-links" }, ...section.collections.map(key => {
          const row = courses.get(key);
          if (!row) return el("article", { class: "subject-link unavailable" },
            el("h3", { text: key }), el("p", { class: "muted", text: "Not installed" }));
          const members = collectionRows(row, this.catalog().courses, this.byId);
          const minutes = members.reduce((sum, item) => sum + (item.estimated_minutes || 0), 0);
          return el("article", { class: "subject-link" },
            el("h3", {}, this.link(row.title, this.routeURL(row, origin))),
            row.summary ? el("p", { class: "collection-summary", text: row.summary }) : null,
            el("small", { class: "muted", text: `${members.length} available items${minutes ? " · " + formatMinutes(minutes) : ""}` }),
            topicLinks(row.tags, this.link, 3),
            row.lectures.length ? el("div", { class: "subject-plan" }, this.link("Adapt this route to what I know →", "/learning-plan?" + new URLSearchParams({ collection: row.id }))) : null,
          );
        })),
      ));
    for (let index = 0; index < sections.length; index++) sections[index].addEventListener("toggle", () => {
      opened[collection.browse_sections[index].title] = sections[index].open;
      store(storageKey, opened);
    });
    const jump = el("select", { "aria-label": "Jump to a subject" },
      el("option", { value: "", text: "Jump to a subject or learning path…" }),
      ...(collection.browse_sections || []).map((section, index) => el("option", { value: String(index), text: section.title })));
    jump.addEventListener("change", () => {
      if (jump.value === "") return;
      const selected = sections[Number(jump.value)];
      selected.open = true;
      selected.querySelector("summary").focus({ preventScroll: true });
      selected.scrollIntoView({ block: "start" });
      jump.value = "";
    });
    return el("div", { class: "subject-directory" }, jump, ...sections);
  }
  historyItem(position, compact = false) {
    const row = this.byId(position.lecture_id);
    const { course, index, next } = historyRoute(position, this.catalog().courses);
    const href = this.itemURL(position.lecture_id, course?.id);
    const item = row && !compact ? this.item(row, course?.id) : el("li", { class: "catalog-item" },
      el("div", { class: "copy" }, row ? this.link(row.title, href)
        : position.lecture_id + " · Pack not installed · history retained"));
    item.classList.add("history-item");
    const copy = item.querySelector(".copy");
    const date = new Date(position.updated_at);
    if (!compact && Number.isFinite(date.getTime())) copy.append(el("small", {}, "Last saved ",
      el("time", { datetime: position.updated_at, text: date.toLocaleString(undefined, { dateStyle: "medium", timeStyle: "short" }) })));
    if (course) copy.append(el("small", {},
      this.link(course.series_title || course.title, this.courseLink(course)),
      ` · ${index + 1} of ${course.lectures.length}`));
    else if (position.course_id) copy.append(el("small", { text: "Previous listening track is no longer available." }));
    const actions = el("div", { class: "actions history-actions" });
    if (row && row.kind !== "presentation")
      actions.append(this.button(position.completed ? "Listen again" : "Resume", () => this.play(href), !position.completed));
    const nextRow = this.byId(next);
    if (nextRow) actions.append(this.link("Next: " + nextRow.title, this.itemURL(next, course.id)));
    else if (next) copy.append(el("small", { text: "Next lecture is not installed on this server." }));
    else if (course) copy.append(el("small", { text: "Last lecture in this track" }));
    copy.append(actions);
    return item;
  }
  continuation(allowed = null) {
    const rows = recentListening(this.progress())
      .filter((p) => this.byId(p.lecture_id) && (!allowed || allowed.has(p.lecture_id)))
      .slice(0, 4);
    if (!rows.length) return null;
    const storageKey = `recent-listening-open:${this.listener()}`;
    return el(
      "details",
      { class: "section recent-listening", open: getStored(storageKey, true),
        ontoggle: (event) => store(storageKey, event.currentTarget.open) },
      el("summary", {}, el("h2", { text: "Recently listened" })),
      this.link("View listening history →", "/listening"),
      el(
        "ul",
        { class: "list" },
        ...rows.map((p) => this.historyItem(p, true)),
      ),
    );
  }
  browse(main) {
    const data = this.catalog();
    // The URL owns browse state so Back can restore the previous filters.
    const query = new URLSearchParams(location.search);
    const initial = (field) => query.get(field) || "";
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
    const topic = el("input", { type: "search", list: "browse-topic-tags", "aria-label": "Tag", placeholder: "Topic, place, author, or period", value: initial("tag") });
    const topicOptions = el("datalist", { id: "browse-topic-tags" });
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
      ...chronologyOptions(),
    );
    sort.value = initial("sort");
    let limit = Number.isInteger(history.state?.browseLimit) ? Math.max(24, history.state.browseLimit) : 24;
    let collectionLimit = history.state?.browseCollectionLimit || 12;
    const base = "/";
    const results = el("div");
    const filters = el(
      "details",
      { class: "browsing-options" },
      el("summary", { text: "Browsing options" }),
      el(
        "div",
        { class: "filters" },
        el("label", {}, "Category", categories),
        el("label", {}, "Tag", topic, topicOptions),
        el("label", {}, "Audience", audiences),
        el("label", {}, "Audio", audio),
        el("label", {}, "Collections", view),
        el("label", {}, "Order", sort),
      ),
    );
    filters.open = Boolean(topic.value || audiences.value || audio.value || view.value || sort.value);
    let topicsLoaded = false;
    function loadTopics() {
      if (!filters.open || topicsLoaded) return;
      topicsLoaded = true;
      topicOptions.append(...[...new Set(data.lectures.flatMap(tagLabels))].sort().map(tag => el("option", { value: tag })));
    }
    filters.addEventListener("toggle", loadTopics);
    loadTopics();
    search.className = "library-search";
    main.replaceChildren(
      el("section", { class: "browse-header" }, heading, search, filters),
      results,
    );
    const update = () => {
      const state = {
        category: categories.value,
        audience: audiences.value,
        q: search.value,
        tag: topic.value.trim(),
        audio: audio.value,
        view: view.value,
        sort: sort.value,
      };
      const params = new URLSearchParams(
        Object.entries(state).filter(([, value]) => value),
      );
      history.replaceState(
        { ...history.state, browseLimit: limit, browseCollectionLimit: collectionLimit },
        "",
        base + (params.size ? "?" + params : "") + location.hash,
      );
      heading.textContent = state.category || "Browse the library";
      document.title = heading.textContent + " · AI Lectures";
      const available = (row) =>
        !state.audio ||
        (state.audio === "ready" ? this.ready(row) : row?.recordings.length);
      const filtered = data.courses.filter(
        (c) =>
          (!state.category || c.categories?.includes(state.category)) &&
          (!state.audience || c.audiences?.includes(state.audience)) &&
          (!state.tag || matchesTag(c, state.tag) || collectionRows(c, data.courses, this.byId).some(row => matchesTag(row, state.tag))) &&
          (!state.audio || collectionRows(c, data.courses, this.byId).some(available)),
      );
      const allowed = new Set(
        data.lectures
          .filter(
            (row) =>
              (!state.category || row.categories?.includes(state.category)) &&
              (!state.audience || row.audiences?.includes(state.audience)) &&
              matchesTag(row, state.tag) &&
              available(row),
          )
          .map((row) => row.id),
      );
      const q = state.q.trim().toLocaleLowerCase();
      const collections = (q || state.view === "all" ? filtered : rootCollections(filtered)).filter(
        (c) => !q || `${c.title} ${c.series_title || ""} ${c.id} ${c.summary} ${(c.tags || []).join(" ")}`.toLocaleLowerCase().includes(q),
      );
      const rows = data.lectures.filter(
        (row) =>
          allowed.has(row.id) &&
          matchesLecture(row.id, this.byId, q),
      );
      if (state.sort) {
        const chronological = dateOrder(state.sort);
        const duration = (c) => collectionRows(c, data.courses, this.byId).reduce((sum, row) => sum + (row.estimated_minutes || (row.words || 0) / 145), 0);
        if (chronological) {
          collections.splice(0, collections.length, ...sortChronologically(collections, state.sort));
          rows.splice(0, rows.length, ...sortChronologically(rows, state.sort));
        } else {
          collections.sort((a, b) => state.sort === "title" ? a.title.localeCompare(b.title) : (duration(a) - duration(b)) * (state.sort === "long" ? -1 : 1));
          rows.sort((a, b) => state.sort === "title" ? a.title.localeCompare(b.title) : ((a.estimated_minutes || 0) - (b.estimated_minutes || 0)) * (state.sort === "long" ? -1 : 1));
        }
      }
      results.replaceChildren();
      if (dateOrder(state.sort)) results.append(el("p", { class: "muted chronology-hint", text: "Ranges sort by their starting year. Approximate or overlapping ranges do not imply a precise sequence. Undated items stay last; authored playback orders remain available." }));
      if (state.category || state.audience || state.audio || q || state.tag || state.view || state.sort)
        results.append(el("div", { class: "browse-status" },
          el("small", { text: [state.category, state.tag && `Topic: ${state.tag}`, state.audience, state.audio && audio.selectedOptions[0].text, q && `Search: “${state.q}”`, state.view && "All collections", state.sort && sort.selectedOptions[0].text].filter(Boolean).join(" · ") }),
          this.button("Clear filters", () => {
            for (const input of [search, topic, categories, audiences, audio, view, sort]) input.value = "";
            limit = 24;
            collectionLimit = 12;
            update();
          }),
        ));
      const guide = !q && !state.tag && !state.view && !state.sort && !state.audience && !state.audio && state.category
        ? collections.find(row => row.guide_for?.includes(state.category) && row.browse_sections?.length) : null;
      if (guide) {
        results.append(el("section", { class: "category-guide" },
          el("p", { class: "intro", text: guide.summary || "" }),
          el("p", { class: "muted", text: "Follow topic tags to explore ideas across courses. Study plan uses recorded prerequisites and your background to construct a learning order." }),
          el("div", { class: "actions" },
            this.link("Open subject guide", this.courseLink(guide)),
            this.link("Build a personal study plan", "/learning-plan"),
            this.link("Browse every collection and lecture", base + "?" + new URLSearchParams({ category: state.category, view: "all" }))),
          this.directorySections(guide, guide.id),
        ));
      } else if (!q && !state.tag && !state.category && !state.view && !state.sort) {
        const groups = collectionGroups(rootCollections(filtered));
        const categoryLink = (group) => {
          const node = this.link(
            group.title,
            group.collections.length === 1
              ? this.courseLink(group.collections[0])
              : base + "?category=" + encodeURIComponent(group.title),
          );
          return node;
        };
        const continuation = this.continuation(allowed);
        if (continuation) results.append(continuation);
        results.append(
          el(
            "section",
            { class: "section", "aria-label": "Browse categories" },
            el("h2", { id: "library-categories", tabindex: "-1", text: "Collections by category" }),
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
        const collectionResults = el(
            state.tag ? "details" : "section",
            { class: "section" },
            el(state.tag ? "summary" : "h2", { text: `${collections.length} collections` }),
            el(
              "div",
              { class: "grid" },
          ...collections.slice(0, collectionLimit).map((c) => this.card(c, null, dateOrder(state.sort)?.axis)),
            ),
          );
        if (collections.length > collectionLimit) {
          const more = this.button("Show more collections", () => {
            collectionLimit += 24;
            update();
          });
          more.classList.add("browse-results-more");
          collectionResults.append(more);
        }
        if (!q) results.append(collectionResults);
        if (rows.length || !q) {
          const section = el(
            "section",
            { class: "section" },
            el("h2", { text: `${rows.length} ${rows.length === 1 ? "lecture" : "lectures"}` }),
            el(
              "ul",
              { class: "list" },
              ...rows.slice(0, limit).map((row) => this.item(row, null, dateOrder(state.sort)?.axis)),
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
        if (q && collections.length) results.append(collectionResults);
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
    for (const input of [search, topic, categories, audiences, audio, view, sort])
      input.addEventListener(input === search || input === topic ? "input" : "change", () => {
        limit = 24;
        collectionLimit = 12;
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
      this.link("Library", "/"),
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
      chronologyLine(collection),
      topicLinks(collection.tags, this.link),
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
      this.link("Browse collections", "/#library-categories"),
      this.link("Explore the learning map", "/learning-map?" + new URLSearchParams({ collection: id })),
      collection.lectures.length ? this.link("Plan a learning order", "/learning-plan?" + new URLSearchParams({ collection: id })) : this.link("Build a personal study plan", "/learning-plan"),
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
    const audioRows = rows.filter(row => row.kind === "audio");
    if (audioRows.length) {
      const preparation = el("details", {class:"collection-preparation",hidden:true},el("summary",{text:"Generate all audio"}));
      resources.append(preparation);
      let loaded=false;
      preparation.ontoggle=()=>{
        if(preparation.open&&!loaded){loaded=true;preparation.append(preparationPanel({lectureIds:audioRows.map(row=>row.id),label:"Generate collection audio",description:"Queue all audio lectures in this collection using one saved voice profile. Existing matching audio is reused."}));}
      };
      api("/api/library/production?probe=0").then(profiles=>{
        if(preparation.isConnected)preparation.hidden = !profiles.tools_available || !profiles.profiles.some(profile=>profile.available!==false);
      }).catch(()=>{});
    }
    const contents = el("div", { class: "collection-contents" });
    if (collection.browse_sections?.length) contents.append(this.directorySections(collection, id));
    if (branches.length) {
      const listed = new Set((collection.browse_sections || []).flatMap(section => section.collections));
      const unlisted = branches.filter(row => !listed.has(row.id));
      const branchCards = el("div", { class: "grid" }, ...unlisted.map(c => this.card(c, id)));
      if (collection.lectures.length) {
        contents.append(el("details", { class: "deep-dive-routes" },
          el("summary", { text: `Explore further · ${branches.length} routes` }), branchCards,
        ));
      } else if (unlisted.length) contents.append(el("h2", { text: "Choose a route" }), branchCards);
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
    const order = el("select", { "aria-label": "Order this collection" }, el("option", { value: "", text: "Authored collection order" }), ...chronologyOptions());
    order.value = params.get("order") || "";
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
    let displayed = [], queueSignature = "", queueEntries = [], enqueuing = false;
    const listen = this.button("Listen in displayed order", async () => {
      enqueuing = true; listen.disabled = true;
      try { await this.enqueue(queueEntries, { play: true }); }
      finally { enqueuing = false; listen.disabled = false; }
    });
    const chronologicalActions = el("div", { class: "actions chronology-actions", hidden: true }, listen);
    const chronologicalHint = el("p", { class: "muted chronology-hint", hidden: true, text: "Use Listen in displayed order to follow this view, including any search filter. Ranges sort by starting year, undated items stay last, and equal dates keep authored order. Authored collection playback remains available." });
    const expand = !flat ? this.button("Expand all", () => results.querySelectorAll("details").forEach(d => { d.open = true; })) : null;
    const collapse = !flat ? this.button("Collapse all", () => results.querySelectorAll("details").forEach(d => { d.open = false; })) : null;
    const controls = el("div", { class: "contents-controls" }, search,
      el("div", { class: "actions" }, order, sections.length > 1 || sections.some(s => s.sessions?.length) ? jump : null,
        expand, collapse,
        this.button("Clear search", () => { search.value = ""; update(); search.focus(); }),
      ), count, chronologicalActions, chronologicalHint,
    );
    contents.append(el("h2", { class: "contents-heading", text: collection.audiences?.includes("children") && /stor/i.test(collection.genre || "") ? "Stories" : "Contents" }), controls, results);
    const update = () => {
      const q = search.value.trim().toLocaleLowerCase();
      const url = new URL(location.href);
      if (q) url.searchParams.set("find", search.value);
      else url.searchParams.delete("find");
      if (dateOrder(order.value)) url.searchParams.set("order", order.value);
      else url.searchParams.delete("order");
      history.replaceState(history.state, "", url);
      refreshStart();
      results.replaceChildren();
      const chronological = dateOrder(order.value);
      if (expand) expand.hidden = Boolean(chronological);
      if (collapse) collapse.hidden = Boolean(chronological);
      chronologicalActions.hidden = !chronological || !this.enqueue;
      chronologicalHint.hidden = !chronological;
      if (chronological) {
        const included = new Set();
        for (const section of sections) {
          const sectionMatch = Boolean(q && section.title.toLocaleLowerCase().includes(q));
          for (const group of section.sessions?.length ? section.sessions : [{ lectures: section.lectures }])
            for (const key of group.lectures)
              if (!q || sectionMatch || group.title?.toLocaleLowerCase().includes(q) || matchesLecture(key, this.byId, q)) included.add(key);
        }
        displayed = sortChronologically(collection.lectures.filter(key => included.has(key)).map(key => this.byId(key) || { id: key, title: key }), order.value).map(row => row.id);
        const signature = JSON.stringify(displayed);
        if (signature !== queueSignature) {
          queueSignature = signature;
          queueEntries = displayed.map(lecture_id => ({ id: randomId(), lecture_id, course_id: null }));
        }
        listen.disabled = enqueuing || !displayed.length || displayed.some(key => !this.byId(key));
        const list = el("ol", { class: "list chronological-contents" });
        const anchors = sections.flatMap(section => [section, ...(section.sessions || [])]);
        const located = new Set();
        for (const key of displayed) {
          this.appendItem(list, key, id, chronological.axis);
          const item = list.lastElementChild;
          for (const anchor of anchors) if (!located.has(anchor.id) && anchor.lectures.includes(key)) {
            located.add(anchor.id);
            item.prepend(el("span", { id: anchor.id, tabindex: "-1", class: "chronology-anchor" }));
            if (anchor.collection) item.querySelector(".copy")?.append(el("div", { class: "topic-link" }, this.routeLink(anchor.collection, "Explore the full topic →", id)));
          }
        }
        results.append(list);
        count.textContent = `${displayed.length}${q ? " of " + collection.lectures.length : ""} items · ${order.selectedOptions[0].text}`;
        if (!displayed.length) results.append(el("p", { class: "notice", text: "No matching items. Clear the search to see the full collection." }));
        return;
      }
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
    order.addEventListener("change", update);
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
  appendItem(list, key, collection, dateAxis = null) {
    const row = this.byId(key);
    list.append(row ? this.item(row, collection, dateAxis) : el("li", { text: key + " · Not installed" }));
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

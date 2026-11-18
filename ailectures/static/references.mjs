import { api, el, lectureURL } from "./api.mjs";

export async function referencesPage(main, catalog) {
  const root = el("section");
  main.replaceChildren(root);
  const query = new URLSearchParams(location.search);
  if (query.has("lecture")) {
    query.set("lecture_id", query.get("lecture"));
    query.delete("lecture");
  }
  const search = el("input", {
    type: "search",
    placeholder: "Search references",
    "aria-label": "Search references",
  });
  const courses = el(
    "select",
    { "aria-label": "References for collection" },
    el("option", { value: "", text: "All collections" }),
    ...catalog.courses.map((course) =>
      el("option", { value: course.id, text: course.title }),
    ),
  );
  courses.value = query.get("course_id") || "";
  const download = el("a", {
    target: "_blank",
    rel: "noopener noreferrer",
    text: "Open plain text references",
  });
  const list = el("div", { class: "feedback-list" });
  root.append(
    el("h1", { text: "References and reading" }),
    el("p", {
      class: "intro",
      text: "Source records, reading notes, and links used by the selected lectures. Reading remains available without audio generation.",
    }),
    el(
      "div",
      { class: "filters" },
      search,
      el("label", {}, "Collection", courses),
    ),
    download,
    list,
  );
  if (query.has("lecture_id")) {
    const selected = catalog.lectures.find(
      (row) => row.id === query.get("lecture_id"),
    );
    root.insertBefore(
      el(
        "p",
        { class: "reference-scope" },
        "For: ", el("a", { href: lectureURL(query.get("lecture_id")), "data-nav": "", text: selected?.title || query.get("lecture_id") }), " · ",
        el("a", {
          href: "/references",
          "data-nav": "",
          text: "Browse all references",
        }),
      ),
      search.parentElement,
    );
  }
  let items = [];
  function draw() {
    const visible = items.filter((item) =>
      JSON.stringify(item).toLowerCase().includes(search.value.toLowerCase()),
    );
    list.replaceChildren(
      ...visible.map((item) => {
        const source =
          item.source && typeof item.source === "object"
            ? item.source
            : { title: String(item.source) };
        const title = source.title || item.id;
        const heading = /^https?:\/\//.test(source.url || "")
          ? el("a", {
              href: source.url,
              text: title,
              target: "_blank",
              rel: "noopener noreferrer",
            })
          : title;
        const names = value => (Array.isArray(value) ? value : [value]).map(person =>
          typeof person === "string" ? person : person?.name).filter(Boolean).join(", ");
        const author = names(source.authors || source.author);
        const publication = [source.year || source.date, source.publisher, source.edition].filter(value => typeof value === "string" || typeof value === "number").join(" · ");
        const notes = [source.description, source.summary, source.notes].flat().filter(value => typeof value === "string" && value.trim());
        return el(
          "article",
          { class: "card" },
          el("h2", {}, heading),
          author ? el("p", { class: "muted", text: author }) : null,
          publication ? el("p", { class: "muted", text: publication }) : null,
          ...[...new Set(notes)].map(text => el("p", { text })),
          ...item.reasons.map((reason) => el("p", { text: reason })),
          el(
            "p",
            { class: "muted" },
            "Used by: ",
            ...item.used_by.flatMap((row, i) => [
              i ? "; " : "",
              el("a", {
                href: lectureURL(row.id),
                "data-nav": "",
                text: row.title,
              }),
            ]),
          ),
          el(
            "details",
            {},
            el("summary", { text: "Full source record" }),
            el("pre", { text: JSON.stringify(source, null, 2) }),
          ),
        );
      }),
    );
    if (!visible.length)
      list.append(
        el("p", {
          class: "muted",
          text: "No source records match this selection. Any unresolved citations remain in the lecture's source and metadata.",
        }),
      );
  }
  async function load() {
    download.href = "/api/library/references.txt?" + query;
    items = (await api("/api/library/references?" + query)).items;
    draw();
  }
  search.oninput = draw;
  courses.onchange = async () => {
    root.querySelector(".reference-scope")?.remove();
    query.delete("lecture_id");
    query.delete("release");
    if (courses.value) query.set("course_id", courses.value);
    else query.delete("course_id");
    history.replaceState(null, "", "/references?" + query);
    try {
      await load();
    } catch (error) {
      list.replaceChildren(el("p", { class: "notice", text: error.message }));
    }
  };
  await load();
}

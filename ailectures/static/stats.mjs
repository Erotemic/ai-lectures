import { statsSection } from "./stats-section.mjs";
import { tagBrowser } from "./tag-browser.mjs";
import { el } from "./api.mjs";
import { formatMinutes } from "./browse-model.mjs";
import { libraryStats } from "./stats-model.mjs";

const number = value => value.toLocaleString();

function totalsTable(rows, label, nameCell) {
  return el("div", { class: "stats-table-scroll", tabindex: "0", role: "region", "aria-label": label },
    el("table", { class: "stats-table" },
      el("caption", { text: label }),
      el("thead", {}, el("tr", {}, ...["Content", "Lectures", "Words", "Est. listening", "Complete audio"].map(text => el("th", { scope: "col", text })))),
      el("tbody", {}, ...rows.map(row => el("tr", {},
        el("th", { scope: "row" }, nameCell ? nameCell(row) : row.title),
        el("td", { text: number(row.lectures) }), el("td", { text: number(row.words) }),
        el("td", { text: formatMinutes(row.minutes) }),
        el("td", { text: `${number(row.complete)} / ${number(row.lectures)}` }))))));
}

export function renderStats(main, catalog, { link, refresh }) {
  const data = libraryStats(catalog);
  const reload = el("button", { type: "button", text: "Refresh stats", onclick: async () => {
    reload.disabled = true;
    reload.textContent = "Refreshing…";
    try { await refresh(); } finally { reload.disabled = false; reload.textContent = "Refresh stats"; }
  } });
  const metrics = [
    ["Unique lectures", number(data.lectures), "/lectures"], ["Collections", number(data.collections)],
    ["Content packs", number(data.packs)], ["Transcript words", number(data.words)],
    ["Estimated listening", `${(data.minutes / 60).toLocaleString(undefined, { maximumFractionDigits: 1 })} h`],
    ["Complete audio", `${number(data.complete)} / ${number(data.lectures)}`],
  ];
  main.replaceChildren(
    el("div", { class: "stats-heading" }, el("div", {}, el("p", { class: "eyebrow", text: "Across the library" }),
      el("h1", { text: "Content stats" })), reload),
    el("p", { class: "intro", text: "An overview of all currently available content. Each lecture counts once in the library totals, even when it appears in several listening routes." }),
    el("p", {}, link("Explore topic graph", "/topic-graph"), " · ", link("Review metadata coverage", "/metadata-audit")),
    el("dl", { class: "stats-metrics" }, ...metrics.map(([label, value, href]) => el("div", {},
      el("dt", { text: label }), el("dd", {}, href ? link(value, href) : value)))),
  );
  if (!data.lectures) main.append(el("p", { class: "notice" }, "No lectures are available yet. ", link("Add a content pack", "/packs"), "."));
  main.append(tagBrowser(catalog.lectures || [], link, { packs: catalog.packs || [] }));
  const availability = statsSection("audio", "Ready to listen");
  for (const [label, value, style] of [["Complete audio", data.complete, "complete"], ["Partial audio", data.partial, "partial"], ["No prepared audio", data.missing, "missing"]]) {
    const percent = data.lectures ? value / data.lectures * 100 : 0;
    const bar = el("span", { class: `stats-fill ${style}` });
    bar.style.width = `${percent}%`;
    availability.append(el("div", { class: "stats-availability" },
      el("span", { text: label }), el("strong", { text: `${number(value)} (${Math.round(percent)}%)` }),
      el("div", { class: "stats-bar", "aria-hidden": "true" }, bar)));
  }
  availability.append(el("p", { class: "muted", text: `${number(data.companions)} lectures have current companion files. Audio readiness counts a lecture once if any narrator has a complete recording; partial recordings count separately.` }));
  availability.append(el("p", { class: "muted", text: "Listening time is estimated from transcript words at 145 words per minute. Actual recordings, playback speed, and pauses will differ. Subject and audience groups may overlap; their rows should not be added together." }));
  main.append(availability);
  const tagLink = (prefix, row) => row.title === "Unspecified" ? "Not recorded" : link(row.title, "/lectures?" + new URLSearchParams({ tag: prefix + row.title }));
  main.append(statsSection("metadata", "Metadata coverage and direct place labels",
    el("p", { text: `${number(data.withPlaces)} lectures have recorded place associations; ${number(data.withDates)} have recorded dates; ${number(data.withDescriptions)} have descriptions or outline previews.` }),
    el("p", { class: "muted", text: "These are the original place labels, before rolling up the hierarchy. A city, country, and region may refer to the same lecture; their rows cannot be added together. The hierarchy above includes their broader associations. Missing metadata is not evidence of a gap in the lectures themselves." }),
    totalsTable(data.directPlaces, "Direct place labels", row => tagLink("Place: ", row))));
  const timeResults = el("div");
  const axisLabels = { period: "Historical period", work: "Work date", setting: "Story setting", life: "Lifetime", witness: "Surviving witness", composition: "Composition date", context: "Historical setting" };
  const axis = el("select", { "aria-label": "Date meaning" }, ...Object.entries(axisLabels).map(([value, text]) => el("option", { value, text })));
  axis.value = Object.keys(axisLabels).find(key => data.dates[key].length) || "period";
  const showTime = () => {
    const rows = data.dates[axis.value];
    const dated = data.dateCoverage[axis.value];
    const sort = "date-" + axis.value;
    timeResults.replaceChildren(el("p", { class: "date-coverage" },
      `${number(dated)} of ${number(data.lectures)} lectures have ${axisLabels[axis.value].toLowerCase()} dates. `,
      link("Browse dated", "/lectures?" + new URLSearchParams({ sort, date: "dated" })), " · ",
      link(`Browse ${number(data.lectures - dated)} without dates`, "/lectures?" + new URLSearchParams({ sort, date: "undated" }))), rows.length ? totalsTable(rows, `${axisLabels[axis.value]} coverage`, row => tagLink(axisLabels[axis.value] + ": ", row)) : el("p", { text: "No dates of this kind are recorded." }));
  };
  axis.onchange = showTime;
  showTime();
  main.append(statsSection("time", "Time coverage",
    el("label", {}, "Date meaning", axis),
    el("p", { class: "muted", text: "Dates retain their meaning: a book’s publication is distinct from its setting, an author’s lifetime, or a surviving manuscript. Ranges can overlap century bins. Broad ranges stay separate; uncertainty remains in each lecture’s date notes." }), timeResults,
    totalsTable(data.periods, "Named periods", row => tagLink("Period: ", row))));
  if (data.authors.length) main.append(statsSection("authors", "Literary authors",
    el("p", { class: "muted", text: "Authors and traditionally attributed authors of the works discussed. These are separate from the people or models that wrote the lectures. Compiler, translator, anonymous, and oral-tradition credits remain on the lecture items." }),
    totalsTable(data.authors, "Lectures by work author", row => tagLink("Author: ", row))));
  const topicSearch = el("input", { type: "search", "aria-label": "Find a coverage tag", placeholder: "Find a topic, place, author, or period" });
  const tagResults = el("div");
  const showTags = () => {
    const query = topicSearch.value.trim().toLocaleLowerCase();
    const matches = data.topics.filter(row => row.title !== "Unspecified" && row.title.toLocaleLowerCase().includes(query));
    tagResults.replaceChildren(el("p", { class: "muted", text: `${number(matches.length)} matching tags; showing up to 50, ordered by lecture count.` }),
      totalsTable(matches.slice(0, 50), "Tag coverage", row => tagLink("", row)));
  };
  topicSearch.oninput = showTags;
  showTags();
  main.append(statsSection("tags", "Explore all tags", topicSearch, tagResults));
  if (data.subjects.length) main.append(statsSection("subjects", "By subject",
    totalsTable(data.subjects, "Content by subject", row => row.title === "Unspecified" ? row.title : link(row.title, "/collections?" + new URLSearchParams({ category: row.title })))));
  if (data.audiences.length && data.audiences.some(row => row.title !== "Unspecified")) main.append(
    statsSection("audiences", "By audience", totalsTable(data.audiences, "Content by audience")));
  const search = el("input", { id: "stats-collection-search", type: "search", value: new URLSearchParams(location.search).get("q") || "", placeholder: "Find a collection", "aria-label": "Find a collection" });
  const results = el("div");
  const count = el("p", { class: "muted", role: "status" });
  function filter() {
    const query = search.value.trim().toLocaleLowerCase();
    const rows = data.collectionRows.filter(row => `${row.title} ${row.id}`.toLocaleLowerCase().includes(query));
    count.textContent = `${number(rows.length)} of ${number(data.collections)} collections`;
    results.replaceChildren(rows.length ? totalsTable(rows, "Content by collection", row => el("span", {},
      link(row.title, "/collections/" + encodeURIComponent(row.id)), row.role === "archive" ? " · archive" : "")) : el("p", { text: "No matching collections." }));
  }
  search.oninput = () => {
    const params = new URLSearchParams(location.search);
    if (search.value) params.set("q", search.value); else params.delete("q");
    history.replaceState(null, "", location.pathname + (params.size ? "?" + params : ""));
    filter();
  };
  filter();
  main.append(statsSection("collections", "By collection", search, count, results,
    el("p", { class: "muted", text: "Collections count unique available members, including nested listening routes. The same lecture can belong to multiple collections; archived collections are marked." })),
    statsSection("packs", "By content pack", totalsTable(data.packRows, "Content by pack"),
      el("p", {}, link("Manage content packs and storage", "/packs"))));
  if (search.value) main.querySelector("#stats-section-collections").open = true;
}

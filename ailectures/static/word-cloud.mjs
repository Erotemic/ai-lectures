import { api, el, lectureURL } from "./api.mjs";

const fmt = value => Number(value).toLocaleString();
const choice = (values, selected) => el("select", {}, ...values.map(([value, title]) =>
  el("option", { value, text: title, selected: String(value) === String(selected) })));
const field = (text, input) => el("label", {}, text, input);

function download(text, filename, type) {
  const url = URL.createObjectURL(new Blob([text], { type }));
  const anchor = el("a", { href: url, download: filename });
  document.body.append(anchor);
  anchor.click();
  anchor.remove();
  setTimeout(() => URL.revokeObjectURL(url), 1000);
}

/** A reading-oriented cloud: count and lecture coverage remain visible in a table. */
export function renderWordCloud(main, catalog, { link }) {
  const search = new URLSearchParams(location.search);
  const pack = choice([["", "All content packs"], ...(catalog.packs || [])
    .map(row => [row.id, row.title || row.id]).sort((a, b) => a[1].localeCompare(b[1]))], search.get("pack") || "");
  const n = choice([[1, "1: words"], [2, "2: bigrams"], [3, "3: trigrams"], [4, "4: four-word phrases"]], search.get("n") || "2");
  const top = choice([[25, "25"], [40, "40"], [60, "60"], [100, "100"], [150, "150"]], search.get("top") || "60");
  const rank = choice([["lectures", "Lectures using phrase"], ["count", "Total occurrences"]], search.get("rank") || "lectures");
  const minDocs = choice([[1, "1"], [2, "2"], [5, "5"], [10, "10"], [25, "25"], [50, "50"], [100, "100"], [250, "250"], [500, "500"], [1000, "1000"]], search.get("min_lectures") || "2");
  const common = el("input", { type: "checkbox", checked: search.get("include_common") === "1" });
  const generate = el("button", { type: "submit", class: "primary", text: "Generate cloud" });
  const svgDownload = el("button", { type: "button", text: "Download SVG", disabled: true });
  const csvDownload = el("button", { type: "button", text: "Download CSV", disabled: true });
  const status = el("p", { class: "muted", role: "status" });
  const visualization = el("div", { class: "word-cloud-visualization" });
  const list = el("div", { class: "word-cloud-list" });
  const phrase = el("input", { type: "search", placeholder: "e.g. matters, what matters is", "aria-label": "Look up a word or phrase", maxlength: 120 });
  const inspect = el("button", { type: "submit", text: "Find occurrences" });
  const matches = el("div", { class: "word-cloud-matches", "aria-live": "polite" });
  const controls = el("form", { class: "word-cloud-controls" },
    field("Content pack", pack), field("Phrase length", n), field("Show top", top),
    field("Rank by", rank), field("Used in at least this many lectures", minDocs),
    el("label", { class: "check" }, common, "Include common function-word phrases"),
    el("div", { class: "word-cloud-actions" }, generate, svgDownload, csvDownload));
  const findForm = el("form", { class: "word-cloud-find" },
    field("Inspect exact spoken phrase", phrase), inspect);
  main.replaceChildren(
    el("h1", { text: "Word and phrase cloud" }),
    el("p", { class: "intro", text: "Explore repeated language in spoken lectures. Compare raw occurrences with the number of lectures using a phrase, then inspect excerpts to decide what actually needs editing." }),
    el("p", { class: "muted" }, "Only spoken transcript text is counted, not citations, sidecars, or editorial notes. Phrases do not cross sentence boundaries. Ranking by lecture coverage is useful for spotting repeated habits; a frequent technical term is not automatically a writing problem."),
    controls, status, visualization,
    el("h2", { text: "Top phrases" }),
    el("p", { class: "muted", text: "Select any phrase in the cloud or table to see its uses. Frequency is reported per 10,000 spoken words for comparison between packs." }),
    list, el("h2", { text: "Inspect a phrase" }), findForm, matches,
    el("p", { class: "muted" }, link("Content stats", "/stats")));
  let latest = null, cloudRequest = 0, findRequest = 0;
  const params = () => new URLSearchParams({
    n: n.value, top: top.value, rank: rank.value,
    min_lectures: minDocs.value, include_common: common.checked ? "1" : "0",
    ...(pack.value ? { pack: pack.value } : {}),
  });

  async function lookup() {
    const requested = phrase.value.trim();
    if (!requested) { matches.replaceChildren(); return; }
    const sequence = ++findRequest;
    matches.replaceChildren(el("p", { role: "status", text: "Searching spoken transcripts..." }));
    const query = new URLSearchParams({ phrase: requested, ...(pack.value ? { pack: pack.value } : {}) });
    try {
      const data = await api("/api/library/word-cloud/find?" + query);
      if (sequence !== findRequest || !main.isConnected) return;
      const header = el("p", {}, el("strong", { text: data.phrase }),
        ` — ${fmt(data.count)} occurrences in ${fmt(data.lectures)} lectures (${data.per_10k.toFixed(2)} per 10,000 words).`);
      matches.replaceChildren(header, ...data.examples.map(row =>
        el("article", { class: "word-cloud-example" },
          el("div", {}, link(row.title, lectureURL(row.id)), ` · ${fmt(row.count)} occurrences`),
          el("p", { text: row.excerpt }))));
      if (data.lectures > data.examples.length) matches.append(
        el("p", { class: "muted", text: `Showing ${data.examples.length} lectures with the most occurrences.` }));
    } catch (error) {
      if (sequence === findRequest) matches.replaceChildren(el("p", { class: "notice", text: error.message }));
    }
  }

  function selectPhrase(value) {
    phrase.value = value;
    lookup();
    findForm.scrollIntoView({ behavior: "smooth", block: "start" });
  }

  async function update() {
    const sequence = ++cloudRequest;
    generate.disabled = true;
    svgDownload.disabled = true;
    csvDownload.disabled = true;
    status.textContent = "Counting spoken words and phrases...";
    const query = params();
    history.replaceState(null, "", "/word-cloud?" + query);
    try {
      const data = await api("/api/library/word-cloud?" + query);
      if (sequence !== cloudRequest || !main.isConnected) return;
      latest = data;
      visualization.innerHTML = data.svg;
      visualization.querySelector("svg")?.addEventListener("click", event => {
        const item = event.target.closest("text[data-phrase]");
        if (item) selectPhrase(item.dataset.phrase);
      });
      visualization.querySelector("svg")?.addEventListener("keydown", event => {
        if (event.key !== "Enter" && event.key !== " ") return;
        const item = event.target.closest("text[data-phrase]");
        if (item) { event.preventDefault(); selectPhrase(item.dataset.phrase); }
      });
      list.replaceChildren(el("ol", {}, ...data.items.map(item =>
        el("li", {}, el("button", { type: "button", class: "word-cloud-phrase", text: item.phrase,
          onclick: () => selectPhrase(item.phrase) }),
        el("span", { class: "muted", text: `${fmt(item.count)} uses · ${fmt(item.lectures)} lectures · ${item.per_10k.toFixed(2)} / 10k` })))));
      if (!data.items.length) list.replaceChildren(el("p", { text: "No phrases match this scope and minimum lecture count." }));
      status.textContent = `${fmt(data.lectures)} lectures · ${fmt(data.words)} spoken words · ${fmt(data.distinct_phrases)} distinct phrases · ${fmt(data.drawn)} placed in cloud`;
      svgDownload.disabled = false;
      csvDownload.disabled = false;
    } catch (error) {
      if (sequence === cloudRequest) status.textContent = error.message;
    } finally {
      if (sequence === cloudRequest) generate.disabled = false;
    }
  }
  controls.addEventListener("submit", event => { event.preventDefault(); update(); });
  findForm.addEventListener("submit", event => { event.preventDefault(); lookup(); });
  svgDownload.addEventListener("click", () => {
    if (latest) download(latest.svg, `word-cloud-${pack.value || "library"}-${n.value}gram.svg`, "image/svg+xml");
  });
  csvDownload.addEventListener("click", () => {
    if (!latest) return;
    const csv = ["phrase,occurrences,lectures,per_10000_words", ...latest.items.map(row =>
      `"${row.phrase.replaceAll('"', '""')}",${row.count},${row.lectures},${row.per_10k}`)].join("\n") + "\n";
    download(csv, `word-cloud-${pack.value || "library"}-${n.value}gram.csv`, "text/csv;charset=utf-8");
  });
  update();
}

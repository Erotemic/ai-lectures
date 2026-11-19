import { api, post, el, lectureURL } from "./api.mjs";

function label(item) {
  if (item.kind === "tag_path") return item.value.join(" › ");
  if (item.kind === "creator") return `${item.value.name} (${item.value.role})`;
  if (item.kind === "date")
    return `${item.value.axis}: ${item.value.approximate ? "c. " : ""}${item.value.start}–${item.value.end}`;
  return item.value;
}

export async function renderMetadataAudit(main) {
  const root = el(
    "section",
    {},
    el("h1", { text: "Metadata review" }),
    el("p", { text: "Loading audit results…" }),
  );
  main.replaceChildren(root);
  let report = await api("/api/library/metadata-audit");
  if (!root.isConnected) return;
  const params = new URLSearchParams(location.search);
  const filter = el(
    "select",
    { "aria-label": "Review status" },
    ...[
      ["open", "Open proposals"],
      ["approved", "Approved"],
      ["dismissed", "Dismissed"],
      ["stale", "Stale"],
      ["all", "All findings"],
    ].map(([value, text]) => el("option", { value, text })),
  );
  filter.value = params.get("status") || "open";
  const search = el("input", {
    type: "search",
    "aria-label": "Search metadata findings",
    placeholder: "Find a lecture, place, topic, or author",
  });
  search.value = params.get("q") || "";
  const kind = el(
    "select",
    { "aria-label": "Metadata dimension" },
    el("option", { value: "", text: "All dimensions" }),
    ...["tag", "tag_path", "place", "creator", "date"].map((value) =>
      el("option", { value, text: value.replace("_", " ") }),
    ),
  );
  kind.value = params.get("kind") || "";
  const status = el("p", { role: "status" }),
    findings = el("section", { "aria-label": "Metadata findings" }),
    coverage = el(
      "details",
      {},
      el("summary", { text: "Model review coverage" }),
    );
  let shown = 30;
  const exportLink = el("a", {
    href: "/api/library/metadata-audit/export",
    download: "approved-metadata-proposals.json",
    text: "Download approved proposals",
  });
  root.replaceChildren(
    el("h1", { text: "Metadata review" }),
    el("p", {
      class: "intro",
      text: "Review proposed gaps with their supporting excerpts. Approval keeps a proposal for export; it does not change authored metadata or certify a historical claim.",
    }),
    el(
      "p",
      {},
      el("a", {
        href: "/topic-graph",
        "data-nav": "",
        text: "Explore the topic graph",
      }),
    ),
    el(
      "details",
      {},
      el("summary", { text: "Run a review with your pi/Qwen agent" }),
      el("p", {
        text: "Point the agent at docs/metadata-audit-agent.md in the repository. It explains the read-only review contract, request export, evidence requirements, and validated result import.",
      }),
      el("pre", {
        text: "python -m ailectures metadata-audit export-requests --repository . --model pi-qwen --limit 5 --output library-data/metadata-review-requests.jsonl",
      }),
      el("p", {
        text: "No model calls run while browsing this page. Import the agent’s responses with metadata-audit import-responses, then refresh this view.",
      }),
    ),
    el(
      "div",
      { class: "filters" },
      el("label", {}, "Status", filter),
      el("label", {}, "Dimension", kind),
      el("label", {}, "Search", search),
    ),
    exportLink,
    el("button", {
      type: "button",
      text: "Refresh results",
      onclick: async () => {
        try {
          report = await api("/api/library/metadata-audit");
          if (root.isConnected) draw();
        } catch (error) {
          status.textContent = error.message;
        }
      },
    }),
    status,
    findings,
    coverage,
  );
  function lectureHref(id) {
    return (
      lectureURL(id) +
      "?" +
      new URLSearchParams({ return: location.pathname + location.search })
    );
  }
  async function decide(item, decision, button) {
    button.disabled = true;
    try {
      await post("/api/library/metadata-audit/" + item.id, { decision });
      item.decision = decision;
      if (root.isConnected) {
        draw();
        status.textContent = "Review decision saved.";
      }
    } catch (error) {
      status.textContent = error.message;
      button.disabled = false;
    }
  }
  function draw() {
    const values = new URLSearchParams();
    if (filter.value !== "open") values.set("status", filter.value);
    if (kind.value) values.set("kind", kind.value);
    if (search.value) values.set("q", search.value);
    history.replaceState(
      history.state,
      "",
      "/metadata-audit" + (values.size ? "?" + values : ""),
    );
    const query = search.value.trim().toLocaleLowerCase();
    const rows = report.findings.filter(
      (item) =>
        (filter.value === "all" ||
          (filter.value === "stale"
            ? item.stale
            : !item.stale && item.decision === filter.value)) &&
        (!kind.value || item.kind === kind.value) &&
        `${item.title} ${label(item)} ${item.reason}`
          .toLocaleLowerCase()
          .includes(query),
    );
    status.textContent = `${report.summary.reviewed}/${report.summary.lectures} lectures have a completed model pass · ${rows.length} matching proposals · ${report.summary.stale} stale. A completed pass does not establish exhaustive coverage.`;
    findings.replaceChildren(
      ...rows.slice(0, shown).map((item) => {
        const buttons = ["approved", "dismissed", "open"]
          .filter((value) => value !== item.decision)
          .map((value) => {
            const button = el("button", {
              type: "button",
              disabled: item.stale,
              text:
                value === "approved"
                  ? "Approve"
                  : value === "dismissed"
                    ? "Dismiss"
                    : "Reopen",
            });
            button.onclick = () => decide(item, value, button);
            return button;
          });
        return el(
          "article",
          { class: "metadata-finding section" },
          el(
            "h2",
            {},
            el("a", {
              href: lectureHref(item.lecture),
              "data-nav": "",
              text: item.title,
            }),
          ),
          el("p", { text: `${item.kind.replace("_", " ")}: ${label(item)}` }),
          el("blockquote", { text: item.evidence }),
          el("p", { text: item.reason }),
          el("p", {
            class: "muted",
            text: `${item.stale ? "Stale · " : ""}${item.decision} · model estimate ${Math.round(item.confidence * 100)}% · ${item.model}`,
          }),
          el("div", { class: "actions" }, ...buttons),
        );
      }),
    );
    if (!rows.length)
      findings.append(
        el("p", {
          text: report.summary.reviewed
            ? "No findings match these filters. Unreviewed lectures can still have missing metadata."
            : "No model reviews have been imported. Export requests and point your agent at the handoff instructions.",
        }),
      );
    if (rows.length > shown)
      findings.append(
        el("button", {
          type: "button",
          text: "Show more findings",
          onclick: () => {
            shown += 30;
            draw();
          },
        }),
      );
    const open = coverage.open;
    coverage.replaceChildren(
      el("summary", { text: "Model review coverage" }),
      ...report.coverage.map((unit) =>
        el(
          "p",
          {},
          el("a", {
            href: lectureHref(unit.lecture),
            "data-nav": "",
            text: unit.title,
          }),
          ` · ${unit.valid}/${unit.total} excerpts complete${unit.errors ? " · " + unit.errors + " failed/invalid" : ""} · ${unit.model}`,
        ),
      ),
    );
    coverage.open = open;
    const old = root.querySelector(".audit-structural");
    const hints = el(
      "details",
      { class: "audit-structural" },
      el("summary", {
        text: `Structural review cues · ${(report.structural_hints || []).length} lectures`,
      }),
      el("p", {
        class: "muted",
        text: "These mechanical cues prioritize review. Missing information may be unknown or inapplicable; section-wide patterns are not proof of coverage.",
      }),
      ...(report.structural_hints || [])
        .slice(0, shown)
        .map((row) =>
          el(
            "p",
            {},
            el("a", {
              href: lectureHref(row.lecture),
              "data-nav": "",
              text: row.title,
            }),
            " · " +
              row.hints
                .map(
                  (hint) =>
                    hint.reason +
                    (hint.labels ? " (" + hint.labels.join(", ") + ")" : ""),
                )
                .join(" "),
          ),
        ),
    );
    hints.open = old?.open || false;
    if (old) old.replaceWith(hints);
    else root.append(hints);
  }
  for (const input of [filter, kind, search])
    input.oninput = () => {
      shown = 30;
      draw();
    };
  draw();
}

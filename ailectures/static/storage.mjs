import { api, clock, el, post } from "./api.mjs";

const shellQuote = value => "'" + value.replaceAll("'", "'\\''") + "'";

export function bytes(value) {
  if (value < 1024) return `${value} B`;
  for (const [unit, divisor] of [
    ["GiB", 1024 ** 3],
    ["MiB", 1024 ** 2],
    ["KiB", 1024],
  ])
    if (value >= divisor) return `${(value / divisor).toFixed(1)} ${unit}`;
}

const cleanupURL = "/api/library/storage/gc";
const scanStages = {
  catalog: "Reading the current catalog",
  references: "Checking listening history and feedback",
  snapshots: "Checking historical text snapshots",
  releases: "Checking installed releases",
  exports: "Checking exported copies",
  generation: "Checking generation jobs",
  speech: "Checking speech caches",
  finalizing: "Preparing the cleanup plan",
};

function showCleanupPlan(report, plan, data) {
  const count = plan.candidates.length;
  report.replaceChildren(el("p", {
    role: "status",
    text: count
      ? `${count} stale audio/cache directories · ${bytes(plan.bytes)} reclaimable. Nothing has been deleted.`
      : "No stale audio or cache directories are eligible for cleanup.",
  }));
  if (plan.retained_recent.length) {
    report.append(el("p", {
      text: `Directories still within the ${plan.policy.keep_days}-day grace period: ${plan.retained_recent.length}.`,
    }));
  }
  if (!count) return;
  const source = data.repository_root ? `--repository ${shellQuote(data.repository_root)}` : "--installed-only";
  report.append(
    el("p", { text: "Finish generation and stop the reader before applying the reviewed plan from a terminal." }),
    el("pre", { text: `python -m ailectures --library ${shellQuote(data.library_root)} gc ${source} --apply ${plan.plan_id}` }),
    el("details", {}, el("summary", { text: "Candidate paths" }), el("ul", {},
      ...plan.candidates.map(item => el("li", { text: `${item.path} · ${bytes(item.bytes)}` })))),
  );
}

function cleanupControls(data, refresh) {
  const button = el("button", { type: "button", text: "Preview stale audio cleanup" });
  const report = el("div");
  button.onclick = async () => {
    button.disabled = refresh.disabled = true;
    const status = el("p", { role: "status", text: "Starting cleanup preview…" });
    const elapsed = el("p", { class: "muted", text: "0:00 elapsed" });
    const progress = el("progress", { "aria-label": "Files and records checked in this stage", hidden: true });
    report.replaceChildren(status, progress, elapsed);
    const started = performance.now();
    const timer = setInterval(() => {
      elapsed.textContent = `${clock((performance.now() - started) / 1000)} elapsed`;
    }, 1000);

    try {
      let preview = await post(cleanupURL, {});
      while (preview.state === "running" && report.isConnected) {
        const { stage, checked, total } = preview.progress;
        const label = scanStages[stage];
        const text = total > 0 ? `${label} · ${Math.min(checked, total)} of ${total}` : `${label}…`;
        if (status.textContent !== text) status.textContent = text;
        progress.hidden = !(total > 0);
        if (!progress.hidden) {
          progress.max = total;
          progress.value = checked;
        }
        await new Promise(resolve => setTimeout(resolve, 500));
        if (report.isConnected) preview = await api(`${cleanupURL}/${preview.id}`);
      }
      if (!report.isConnected) return;
      if (preview.state === "failed") throw new Error(preview.error);
      showCleanupPlan(report, preview.plan, data);
    } catch (error) {
      report.replaceChildren(el("p", { class: "notice", role: "status", text: `Cleanup preview failed. ${error.message}` }));
    } finally {
      clearInterval(timer);
      button.disabled = refresh.disabled = false;
    }
  };
  return [el("h3", { text: "Clean up stale audio" }), button, report];
}

export async function showStorage(panel, cards, catalog) {
  const content = el("div");
  const refresh = el("button", {
    type: "button",
    text: "Refresh storage details",
  });
  panel.replaceChildren(
    el("h2", { text: "Library storage" }),
    refresh,
    content,
  );
  const load = async () => {
    refresh.disabled = true;
    try {
      const data = await api("/api/library/storage");
      for (const card of cards.querySelectorAll("[data-pack]")) {
        const pack = catalog.packs.find((p) => p.id === card.dataset.pack);
        const stored = data.releases.find(
          (p) => p.active && p.pack_id === pack.id,
        );
        const rows = catalog.lectures.filter(
          (row) => row.origin?.pack === pack.id,
        );
        const count = pack.source ? rows.length : stored?.lectures || 0;
        const ready = pack.source
          ? rows.filter((row) => row.recordings.some((r) => r.complete)).length
          : stored?.ready || 0;
        const narrators = pack.source
          ? new Set(rows.flatMap((row) => row.recordings.map((r) => r.variant)))
              .size
          : stored?.narrators || 0;
        card.querySelector("[data-coverage]").textContent =
          `${count} lectures · ${ready} with complete audio · ${narrators} narrators${!pack.source && stored ? " · " + bytes(stored.bytes) : ""}`;
      }
      const retained = data.releases.filter((row) => !row.active);
      content.replaceChildren(
        el("p", {
          class: "intro",
          text: `Active releases ${bytes(data.active_bytes)} · retained releases ${bytes(data.retained_bytes)} · personal state ${bytes(data.state_bytes)}`,
        }),
        el("p", {
          text: `Build cache ${bytes(data.build_cache_bytes)} · exported copies ${bytes(data.exports_bytes)} · unregistered pack files ${bytes(data.unregistered_bytes)}`,
        }),
        el("p", {
          text: "Earlier releases are retained until explicit cleanup. Preview below keeps recent text and audio referenced by listening history or feedback.",
        }),
        el(
          "details",
          {},
          el("summary", { text: `Retained releases (${retained.length})` }),
          el(
            "ul",
            {},
            ...retained.map((row) =>
              el("li", {
                text: `${row.title} · ${bytes(row.bytes)}${row.available ? "" : " · files unavailable"}`,
              }),
            ),
          ),
        ),
        el("h3", { text: "Back up or move this library" }),
        el("p", {
          text: "Backups include installed releases, listening history, queues, feedback, and preparation requests. Build caches and duplicate exports are omitted.",
        }),
        el(
          "p",
          {},
          "Library directory: ",
          el("code", { text: data.library_root }),
        ),
        el("pre", {
          text: "ailectures --library LIBRARY_DIRECTORY backup BACKUP.zip\nailectures --library NEW_LIBRARY_DIRECTORY restore BACKUP.zip",
        }),
        ...cleanupControls(data, refresh),
      );
    } catch (error) {
      content.replaceChildren(
        el("p", {
          class: "notice",
          text: "Storage details unavailable: " + error.message,
        }),
      );
    } finally {
      refresh.disabled = false;
    }
  };
  refresh.onclick = load;
  await load();
}

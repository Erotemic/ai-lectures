import { api, el } from "./api.mjs";

export function bytes(value) {
  if (value < 1024) return `${value} B`;
  for (const [unit, divisor] of [
    ["GiB", 1024 ** 3],
    ["MiB", 1024 ** 2],
    ["KiB", 1024],
  ])
    if (value >= divisor) return `${(value / divisor).toFixed(1)} ${unit}`;
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
          text: "Earlier releases are retained for active players and historical feedback. Automatic media deletion is disabled.",
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

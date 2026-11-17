import { api, post, el } from "./api.mjs";

let serial = 0;
const endpoint = "/api/library/slide-decks";

export function preparedSlideCompanions(row) {
  return (Array.isArray(row.companions) ? row.companions : []).filter((item) =>
    item && item.role === "prepared" && typeof item.media_type === "string" &&
    item.media_type.split(";", 1)[0].trim().toLowerCase() === "text/html" &&
    typeof item.id === "string" && item.id && typeof item.url === "string" && item.url,
  ).map((item) => ({
    id: "prepared:" + item.id,
    kind: "prepared",
    title: item.title || item.id,
    subtitle: item.stale ? "Prepared HTML for an earlier transcript" : "Prepared HTML companion",
    revision: item.sha256,
    available: true,
    built: true,
    state: "built",
    build_available: false,
    view_url: item.url + (item.url.includes("?") ? "&" : "?") + "view=1",
    download_url: item.url,
    attribution: item.attribution,
  }));
}

export class SlideCompanionPanel {
  constructor(main, row, context = {}) {
    this.row = row;
    this.request = context.api || api;
    this.send = context.post || post;
    this.prepared = preparedSlideCompanions(row);
    this.items = new Map();
    this.selected = null;
    this.pending = new Set();
    this.loaded = false;
    this.frameDeck = null;
    const selectorId = `slide-companion-${++serial}`;
    this.root = el("details", { class: "slide-companions" });
    this.root.style.minWidth = "0";
    this.status = el("p", { role: "status", "aria-live": "polite" });
    this.error = el("p", { class: "notice", role: "alert", hidden: true });
    this.loadRetry = el("button", { type: "button", text: "Try loading slides again", hidden: true });
    this.loadRetry.onclick = () => this.load();
    this.select = el("select", { id: selectorId, "aria-label": "Slide deck" });
    this.select.style.maxWidth = "100%";
    this.select.style.minWidth = "0";
    this.select.onchange = () => {
      this.selected = this.select.value;
      this.draw();
      if (!this.frame.hidden) this.viewSelected();
    };
    this.buildButton = el("button", { type: "button", text: "Build slides" });
    this.buildButton.onclick = () => this.buildSelected();
    this.viewButton = el("button", { type: "button", text: "View slides" });
    this.viewButton.onclick = () => this.viewSelected();
    this.refreshButton = el("button", { type: "button", text: "Refresh status" });
    this.refreshButton.onclick = () => this.refresh();
    this.openLink = el("a", {
      target: "_blank", rel: "noopener noreferrer", text: "Open slides in a new tab",
    });
    this.downloadLink = el("a", { download: "", text: "Download slide HTML" });
    this.description = el("p", { class: "muted" });
    this.credits = el("details", {}, el("summary", { text: "Sources and credits" }));
    this.creditBody = el("div");
    this.credits.append(this.creditBody);
    this.controls = el("div", { class: "slide-companion-controls", hidden: true },
      el("label", { for: selectorId, text: "Slide deck" }), this.select,
      this.buildButton, this.viewButton, this.refreshButton,
      this.openLink, this.downloadLink,
    );
    Object.assign(this.controls.style, {
      display: "flex", flexWrap: "wrap", alignItems: "center", gap: ".65rem",
    });
    this.frame = el("iframe", {
      title: "Lecture slide companion", hidden: true, loading: "lazy",
      sandbox: "allow-scripts allow-modals", referrerpolicy: "no-referrer",
    });
    Object.assign(this.frame.style, {
      display: "block", width: "100%", maxWidth: "100%", minWidth: "0",
      height: "min(75vh, 52rem)", minHeight: "20rem", border: "1px solid currentColor",
    });
    this.root.append(el("summary", { text: "Slide companions" }), this.status,
      this.error, this.loadRetry, this.controls, this.description, this.credits, this.frame);
    this.status.textContent = "Open to see available slide decks.";
    this.credits.hidden = true;
    this.root.addEventListener("toggle", () => {
      if (this.root.open && !this.loaded) this.load();
    });
    main.append(this.root);
  }

  showError(error) {
    this.error.textContent = error?.message || String(error);
    this.error.hidden = false;
  }

  displayItems(items) {
    // Prepared files are already usable, including in a portable installation.
    this.items = new Map([...this.prepared, ...items].map((item) => [item.id, item]));
    this.select.replaceChildren(...[...this.items.values()].map((item) =>
      el("option", {
        value: item.id,
        text: (item.title || item.id) + (item.kind === "prepared" ? " · Prepared" : ""),
      })));
    if (!this.items.has(this.selected)) this.selected = this.items.keys().next().value;
    this.loaded = true;
    this.controls.hidden = !this.items.size;
    if (!this.items.size) {
      this.status.textContent = this.row.companions?.length
        ? "No buildable slide decks are linked here. Prepared companion files remain available."
        : "No slide decks are linked to this lecture.";
      this.description.textContent = "";
      this.credits.hidden = true;
      this.frame.hidden = true;
    } else this.draw();
  }

  async load() {
    if (this.loading) return this.loading;
    this.status.textContent = "Checking slide companions…";
    this.error.hidden = true;
    this.loadRetry.hidden = true;
    this.loading = (async () => {
      try {
        const data = await this.request(endpoint + "?" +
          new URLSearchParams({ lecture_id: this.row.id }));
        this.displayItems(data.items || []);
      } catch (error) {
        if (this.prepared.length) this.displayItems([]);
        else {
          this.status.textContent = "Slide companions could not be loaded.";
          this.showError(error);
        }
        this.loadRetry.hidden = false;
      }
    })();
    try { await this.loading; } finally { this.loading = null; }
  }

  draw() {
    const item = this.items.get(this.selected);
    if (!item) return;
    this.select.value = item.id;
    const building = this.pending.has(item.id) || item.state === "building";
    this.status.textContent = building ? "Building slides…"
      : item.kind === "prepared" ? "Prepared slides ready"
      : item.built ? `${item.slide_count || ""} slides ready`.trim()
      : item.state === "failed" ? "The slide build failed. You can retry."
      : !item.available ? "This slide source is unavailable."
      : !item.build_available ? "Slides have not been built; the slide renderer is unavailable."
      : "Slides have not been built. Build them when you want to view them.";
    this.description.textContent = item.subtitle || "";
    this.buildButton.disabled = building || item.built || !item.build_available;
    this.buildButton.hidden = item.kind === "prepared";
    this.refreshButton.hidden = item.kind === "prepared";
    this.buildButton.textContent = building ? "Building…" : item.state === "failed" ? "Retry build" : "Build slides";
    this.viewButton.disabled = !item.built;
    this.openLink.hidden = !item.built;
    this.downloadLink.hidden = !item.built;
    if (item.built) {
      this.openLink.href = item.view_url;
      this.downloadLink.href = item.download_url;
    } else {
      this.openLink.removeAttribute("href");
      this.downloadLink.removeAttribute("href");
    }
    this.error.hidden = !item.error;
    if (item.error) this.error.textContent = item.error;
    this.drawCredits(item);
  }

  drawCredits(item) {
    const nodes = [];
    if (item.attribution) nodes.push(el("p", {
      text: typeof item.attribution === "string" ? item.attribution : JSON.stringify(item.attribution),
    }));
    const sources = new Map();
    const add = (key, source) => {
      if (source && typeof source === "object") sources.set(key, source);
    };
    if (Array.isArray(item.sources))
      item.sources.forEach((source, index) => add(source.id || `deck-${index}`, source));
    else Object.entries(item.sources || {}).forEach(([key, source]) => add(key, source));
    for (const credit of item.source_credits || []) {
      Object.entries(credit.sources || {}).forEach(([key, source]) => add(key, source));
      if (credit.provenance) nodes.push(el("pre", {
        text: JSON.stringify(credit.provenance, null, 2),
      }));
    }
    for (const [key, source] of sources) {
      const title = source.title || source.author || key;
      nodes.push(el("p", {}, /^https?:\/\//.test(source.url || "")
        ? el("a", { text: title, href: source.url, target: "_blank", rel: "noopener noreferrer" })
        : String(title)));
    }
    this.creditBody.replaceChildren(...nodes);
    this.credits.hidden = !nodes.length;
  }

  viewSelected() {
    const item = this.items.get(this.selected);
    if (!item?.built) {
      this.frame.hidden = true;
      return;
    }
    // Status refreshes keep the existing viewer and its selected slide intact.
    if (this.frameDeck !== item.id || this.frameURL !== item.view_url || this.frameRevision !== item.revision) {
      this.frame.src = item.view_url + (item.view_url.includes("?") ? "&" : "?") + "embed=1";
      this.frameDeck = item.id;
      this.frameURL = item.view_url;
      this.frameRevision = item.revision;
    }
    this.frame.title = item.title || "Lecture slide companion";
    this.frame.hidden = false;
  }

  async refresh() {
    const item = this.items.get(this.selected);
    if (!item) return this.load();
    if (item.kind === "prepared") return this.draw();
    this.error.hidden = true;
    try {
      const updated = await this.request(item.status_url);
      this.items.set(item.id, updated);
      this.draw();
      if (!updated.built && this.frameDeck === item.id) this.frame.hidden = true;
    } catch (error) { this.showError(error); }
  }

  async buildSelected() {
    const item = this.items.get(this.selected);
    if (!item || item.kind === "prepared" || item.built || !item.build_available || this.pending.has(item.id)) return;
    this.pending.add(item.id);
    this.error.hidden = true;
    this.draw();
    try {
      const updated = await this.send(item.build_url, {});
      this.items.set(item.id, updated);
      if (this.selected === item.id && updated.built) this.viewSelected();
    } catch (error) {
      this.items.set(item.id, { ...item, state: "failed", error: error.message });
    } finally {
      this.pending.delete(item.id);
      this.draw();
    }
  }
}

export function showSlideCompanions(main, row, context = {}) {
  return new SlideCompanionPanel(main, row, context);
}

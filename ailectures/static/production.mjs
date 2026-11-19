import { api, post, el, store, lectureURL } from "./api.mjs";
import { NarrationControls } from "./narration.mjs";
import { blockGrid, generationStatus } from "./audio-blocks.mjs";
const $ = (id) => document.getElementById(id);
const title = (text) => el("h1", { text });
const description = (text) => el("p", { class: "intro", text });

export function partitionJobs(jobs) {
  const active = [],
    attention = [],
    history = [];
  for (const job of jobs) {
    if (["queued", "running"].includes(job.state)) active.push(job);
    else if (["ready", "cancelled"].includes(job.state)) history.push(job);
    else attention.push(job);
  }
  const newest = (a, b) =>
    (b.updated_at || b.created_at || 0) - (a.updated_at || a.created_at || 0) ||
    a.id.localeCompare(b.id);
  active.sort(
    (a, b) =>
      Number(b.state === "running") - Number(a.state === "running") ||
      (a.created_at || 0) - (b.created_at || 0) ||
      a.id.localeCompare(b.id),
  );
  attention.sort(newest);
  history.sort(newest);
  return { active, attention, history };
}

export class ProductionPanel {
  constructor(options) {
    Object.assign(this, options);
    this.cancelling = new Set();
    this.cancelErrors = new Map();
    this.historyOpen = false;
    this.historyLimit = 20;
    this.expandedHistory = new Set();
  }
  byId(id) {
    return this.catalog().lectures.find((row) => row.id === id);
  }
  async render(target) {
    const main = el("section");
    this.root = main;
    target.replaceChildren(main);
    main.replaceChildren(
      title("Audio production"),
      description(
        "Prepared recordings play independently of TTS. Generate missing recordings when a configured backend is available.",
      ),
    );
    if (this.catalog().legacy)
      main.append(el("details", { class: "compatibility-tools" },
        el("summary", { text: "Compatibility tools" }),
        this.link("Open original audio tools", "/audio"),
      ));
    const profiles = await api("/api/library/production");
    if (!main.isConnected) return;
    if (!profiles.profiles.length) {
      main.append(
        el("div", {
          class: "notice",
          text:
            profiles.error ||
            "No TTS connection is configured in this installation. Installed audio and transcripts remain available.",
        }),
      );
      main.append(el("section", { id: "jobs", class: "section" }));
      await this.showJobs();
      return;
    }
    const scope = el(
      "select",
      { "aria-label": "Preparation selection" },
      el("option", { value: "lecture", text: "Lecture" }),
      el("option", { value: "course", text: "Whole collection" }),
      el("option", { value: "library", text: "Whole library" }),
    );
    const lectures = el(
      "select",
      { "aria-label": "Lecture to prepare" },
      ...this.catalog()
        .lectures.filter((r) => r.kind === "audio")
        .map((r) => el("option", { value: r.id, text: r.title })),
    );
    const requestedLecture = new URLSearchParams(location.search).get(
      "lecture",
    );
    if (
      [...lectures.options].some((option) => option.value === requestedLecture)
    )
      lectures.value = requestedLecture;
    scope.onchange = () => {
      const rows =
        scope.value === "course"
          ? this.catalog().courses.filter((c) =>
              c.lectures.some((id) => this.byId(id)?.kind === "audio"),
            )
          : this.catalog().lectures.filter((r) => r.kind === "audio");
      lectures.replaceChildren(
        ...rows.map((row) => el("option", { value: row.id, text: row.title })),
      );
      lectures.disabled = scope.value === "library";
      $("prepare-audio").textContent =
        scope.value === "library"
          ? `Queue all ${this.catalog().lectures.filter((row) => row.kind === "audio").length} lectures`
          : scope.value === "course"
            ? "Queue whole collection"
            : "Cache whole lecture";
    };
    const narrator = new NarrationControls(profiles, {
      profileId: "production-profile",
      discover: true,
    });
    const form = el(
      "form",
      {},
      el(
        "div",
        { class: "filters" },
        el("label", {}, "Prepare", scope),
        el("label", {}, "Selection", lectures),
      ),
      narrator.root,
      el("button", {
        id: "prepare-audio",
        type: "submit",
        class: "primary",
        text: "Cache whole lecture",
        disabled: !profiles.tools_available,
      }),
    );
    form.onsubmit = async (e) => {
      e.preventDefault();
      try {
        await post("/api/library/production/prepare", {
          ...(scope.value === "library"
            ? {
                lecture_ids: this.catalog()
                  .lectures.filter((row) => row.kind === "audio")
                  .map((row) => row.id),
              }
            : {
                [scope.value === "course" ? "course_id" : "lecture_id"]:
                  lectures.value,
              }),
          ...narrator.settings(),
        });
        await this.showJobs();
      } catch (error) {
        this.message(error.message);
      }
    };
    const registerId = el("input", {
      type: "text",
      "aria-label": "Voice ID to register",
    });
    const registerLabel = el("input", {
      type: "text",
      "aria-label": "Voice display name",
      maxlength: "80",
    });
    const registerMessage = el("p", { role: "status" });
    main.append(...[
      form,
      profiles.schema === "voice-profiles-v1" ? el("a", { href: "/settings#voice-profiles", "data-nav": "", text: "Create or edit a voice profile" }) : this.button("Refresh available voices", () =>
        narrator.loadVoices(true, narrator.settings().voice),
      ),
      profiles.schema === "voice-profiles-v1" ? null : el(
        "details",
        { class: "section" },
        el("summary", { text: "Register a server voice ID" }),
        description(
          "Register a voice already available on the selected speech server. Reference recordings stay on that server.",
        ),
        el(
          "div",
          { class: "filters" },
          el("label", {}, "Voice ID", registerId),
          el("label", {}, "Display name", registerLabel),
        ),
        this.button("Register voice", async () => {
          try {
            await post("/api/library/production/voices/register", {
              profile: narrator.profile.value,
              voice: registerId.value.trim(),
              label: registerLabel.value.trim() || registerId.value.trim(),
            });
            store(
              "production-voice:" + narrator.profile.value,
              registerId.value.trim(),
            );
            await narrator.loadVoices(false, registerId.value.trim());
            registerMessage.textContent = "Voice registered for this profile.";
          } catch (error) {
            registerMessage.textContent = error.message;
          }
        }),
        registerMessage,
      ),
      el("section", { id: "jobs", class: "section" }),
    ].filter(Boolean));
    if (!profiles.tools_available)
      main.append(
        el("p", {
          class: "notice",
          text: "Generation needs the production installation and FFmpeg tools. Playback remains available.",
        }),
      );
    await this.showJobs();
    if (location.hash === "#jobs")
      $("jobs")?.scrollIntoView({ block: "start" });
  }
  async refreshHealth() {
    const select =
      this.root?.isConnected && this.root.querySelector("#production-profile");
    if (!select) return;
    const data = await api("/api/library/production");
    if (!select.isConnected) return;
    for (const option of select.options) {
      const profile = data.profiles.find((p) => p.id === option.value);
      if (profile)
        option.textContent =
          profile.label + (profile.reachable === false ? " · unavailable" : "");
    }
    if ($("prepare-audio")) $("prepare-audio").disabled = !data.tools_available;
  }
  jobTitle(job) {
    return this.byId(job.lecture_id)?.title || job.title || job.lecture_id;
  }
  jobNarrator(job) {
    return `${job.profile} · ${job.voice || "configured voice"} · ${job.model || "configured model"} · ${job.speed || 1}× speech`;
  }
  jobCard(job) {
    const id = job.id;
    const inv = job.inventory;
    return el(
      "article",
      { class: "card", "data-job": id },
      el(
        "h3",
        {},
        this.link(this.jobTitle(job), lectureURL(job.lecture_id)),
      ),
      el("p", {
        text: this.jobNarrator(job),
      }),
      el("p", {
        class: "muted",
        text: job.requested_blocks
          ? job.requested_blocks.length === 1
            ? `Block ${job.requested_blocks[0] + 1} requested`
            : `${job.requested_blocks.length} audio blocks requested`
          : "Whole lecture requested",
      }),
      el("p", {
        text: job.published
          ? "Recording published"
          : `${job.state} · ${inv.ready} / ${inv.total || "?"} passages ready`,
      }),
      el("progress", {
        value: inv.ready,
        max: Math.max(1, inv.total),
        "aria-label": "Prepared passages",
      }),
      job.error ? el("p", { class: "notice", text: job.error }) : null,
      this.cancelErrors.has(id)
        ? el("p", {
            class: "notice",
            role: "status",
            text: this.cancelErrors.get(id),
          })
        : null,
      blockGrid(inv.states || []),
      ...(["queued", "running"].includes(job.state)
        ? inv.queue || []
        : []
      ).map((item) =>
        el(
          "div",
          { class: "generation-item" },
          el("p", {
            text: `Block ${item.page + 1} · ${item.kind} · ${generationStatus(item)}`,
          }),
        ),
      ),
      job.state === "settings_changed"
        ? this.link(
            "Prepare with current settings",
            "/production?lecture=" + encodeURIComponent(job.lecture_id),
          )
        : ["failed", "cancelled"].includes(job.state)
          ? this.button("Retry preparation", async () => {
              await post(
                "/api/library/production/jobs/" + id + "/retry",
                {},
              );
              await this.showJobs();
            })
          : null,
      ["queued", "running"].includes(job.state)
        ? el("button", {
            type: "button",
            "data-cancel-job": id,
            disabled: this.cancelling.has(id),
            text: this.cancelling.has(id)
              ? "Stopping…"
              : "Cancel this lecture's generation",
            onclick: () => this.cancelJob(id),
          })
        : null,
      el(
        "details",
        {},
        el("summary", { text: "Queue and preparation details" }),
        el("pre", { text: JSON.stringify(inv, null, 2) }),
      ),
    );
  }
  historyEntry(job) {
    const entry = el("details", {
      class: "job-history-entry",
      "data-history-job": job.id,
      open: this.expandedHistory.has(job.id),
    });
    const timestamp = job.updated_at || job.created_at;
    const when = timestamp
      ? el("time", {
          datetime: new Date(timestamp * 1000).toISOString(),
          text: new Date(timestamp * 1000).toLocaleString(),
        })
      : null;
    entry.append(
      el(
        "summary",
        {},
        el("strong", { text: this.jobTitle(job) }),
        el("span", {
          class: "muted",
          text: `${this.jobNarrator(job)} · ${job.state === "ready" ? "Completed" : "Cancelled"}`,
        }),
        when,
      ),
    );
    const expand = () => {
      if (entry.open && !entry.querySelector("article"))
        entry.append(this.jobCard(job));
    };
    entry.addEventListener("toggle", () => {
      if (!entry.isConnected) return;
      if (entry.open) this.expandedHistory.add(job.id);
      else this.expandedHistory.delete(job.id);
      expand();
    });
    expand();
    return entry;
  }
  drawJobs(target, jobs) {
    const { active, attention, history } = partitionJobs(jobs);
    target.replaceChildren(
      el("h2", { text: "Preparation jobs" }),
      el("p", {
        class: "muted",
        text: `${active.length} active · ${attention.length} need attention · ${history.length} finished`,
      }),
      active.length
        ? el(
            "div",
            { class: "grid", "data-active-jobs": "" },
            ...active.map((job) => this.jobCard(job)),
          )
        : el("p", { text: "No preparations are queued or running." }),
    );
    if (attention.length)
      target.append(
        el(
          "section",
          { "data-attention-jobs": "" },
          el("h3", { text: "Needs attention" }),
          el("div", { class: "grid" }, ...attention.map((job) => this.jobCard(job))),
        ),
      );
    if (!history.length) return;
    const finished = el("details", {
      class: "section",
      "data-job-history": "",
      open: this.historyOpen,
    });
    finished.append(el("summary", { text: `Finished history (${history.length})` }));
    const entries = el("div");
    const showHistory = () => {
      entries.replaceChildren(
        ...history.slice(0, this.historyLimit).map((job) => this.historyEntry(job)),
      );
      if (history.length > this.historyLimit)
        entries.append(
          this.button("Show more finished jobs", () => {
            this.historyLimit += 20;
            showHistory();
          }),
        );
    };
    finished.addEventListener("toggle", () => {
      if (!finished.isConnected) return;
      this.historyOpen = finished.open;
      if (finished.open) showHistory();
    });
    finished.append(entries);
    if (this.historyOpen) showHistory();
    target.append(finished);
  }
  async showJobs() {
    const target = this.root?.isConnected && this.root.querySelector("#jobs");
    if (!target) return;
    const token = (this.jobsToken = (this.jobsToken || 0) + 1);
    const jobs = (await api("/api/library/production/jobs")).jobs;
    if (!target.isConnected || token !== this.jobsToken) return;
    // Unchanged polls leave open details, keyboard focus, and scroll intact.
    const signature = JSON.stringify([
      jobs,
      [...this.cancelling],
      [...this.cancelErrors],
    ]);
    if (this.jobsTarget === target && this.jobsSignature === signature) return;
    this.drawJobs(target, jobs);
    this.jobsTarget = target;
    this.jobsSignature = signature;
  }
  async cancelJob(id) {
    if (this.cancelling.has(id)) return;
    this.cancelling.add(id);
    this.cancelErrors.delete(id);
    for (const button of this.root?.querySelectorAll("[data-cancel-job]") ||
      []) {
      if (button.dataset.cancelJob === id) {
        button.disabled = true;
        button.textContent = "Stopping…";
      }
    }
    try {
      await api("/api/library/production/jobs/" + id, { method: "DELETE" });
    } catch (error) {
      this.cancelErrors.set(id, "Could not stop generation: " + error.message);
      this.message(error.message);
    } finally {
      this.cancelling.delete(id);
      await this.showJobs();
    }
  }
}

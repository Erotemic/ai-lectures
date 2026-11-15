import { api, post, el, store } from "./api.mjs";
import { NarrationControls } from "./narration.mjs";
import { blockGrid, generationStatus } from "./audio-blocks.mjs";
const $ = (id) => document.getElementById(id);
const title = (text) => el("h1", { text });
const description = (text) => el("p", { class: "intro", text });

export class ProductionPanel {
  constructor(options) {
    Object.assign(this, options);
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
      main.append(this.link("Open original audio tools", "/audio"));
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
    main.append(
      form,
      this.button("Refresh available voices", () =>
        narrator.loadVoices(true, narrator.settings().voice),
      ),
      el(
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
    );
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
  async showJobs() {
    const target = this.root?.isConnected && this.root.querySelector("#jobs");
    if (!target) return;
    const cards = [];
    const jobs = (await api("/api/library/production/jobs")).jobs;
    for (const job of jobs) {
      const id = job.id;
      try {
        const inv = job.inventory;
        cards.push(
          el(
            "article",
            { class: "card" },
            el("h3", {
              text: this.byId(job.lecture_id)?.title || job.lecture_id,
            }),
            el("p", {
              text: `${job.profile} · ${job.voice || "configured voice"} · ${job.speed || 1}× speech`,
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
            blockGrid(inv.states || []),
            ...(inv.queue || []).map((item) =>
              el(
                "div",
                { class: "generation-item" },
                el("p", {
                  text: `Block ${item.page + 1} · ${item.kind} · ${generationStatus(item)}`,
                }),
                this.button("Cancel this lecture's generation", async () => {
                  await api("/api/library/production/jobs/" + id, {
                    method: "DELETE",
                  });
                  await this.showJobs();
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
            !job.published &&
              !["failed", "cancelled", "settings_changed"].includes(job.state)
              ? this.button("Cancel generation", async () => {
                  await api("/api/library/production/jobs/" + id, {
                    method: "DELETE",
                  });
                  await this.showJobs();
                })
              : null,
            el(
              "details",
              {},
              el("summary", { text: "Queue and preparation details" }),
              el("pre", { text: JSON.stringify(inv, null, 2) }),
            ),
          ),
        );
      } catch (error) {
        cards.push(
          el("p", {
            class: "muted",
            text: error.message,
          }),
        );
      }
    }
    if (!target.isConnected) return;
    target.replaceChildren(
      el("h2", { text: "Preparation jobs" }),
      el("div", { class: "grid" }, ...cards),
    );
  }
}

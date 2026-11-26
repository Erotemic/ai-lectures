import { api, el, getStored, store } from "./api.mjs";

function oldPreference(key) {
  try {
    return JSON.parse(localStorage.getItem("dkps-audio-" + key));
  } catch {
    return null;
  }
}

export class NarrationControls {
  constructor(
    profiles,
    { profileId = "narration-profile", discover = false, compact = false } = {},
  ) {
    this.profiles = profiles;
    this.toolsAvailable = profiles.tools_available;
    this.discover = discover;
    this.root = el("div");
    this.profile = el(
      "select",
      { id: profileId, "aria-label": "Narrator profile" },
      ...profiles.profiles.map((profile) =>
        el("option", {
          value: profile.id,
          text:
            profile.label +
            (profile.output_format === "ogg" ? " · Ogg Opus" : "") +
            (profile.reachable === false || profile.available === false
              ? " · unavailable"
              : ""),
          disabled: profile.available === false,
        }),
      ),
    );
    const remembered = getStored(
      "production-profile",
      oldPreference("profile"),
    );
    const selectable = profiles.profiles.filter(
      (row) => row.available !== false,
    );
    this.profile.value = selectable.some((row) => row.id === remembered)
      ? remembered
      : selectable.find((row) => row.id === profiles.default_profile)?.id ||
        selectable[0]?.id ||
        "";
    this.fixedProfiles = profiles.schema === "voice-profiles-v1";
    if (this.fixedProfiles) {
      const note = el("p", { class: "muted" });
      const update = () => {
        const row = this.selectedProfile();
        note.textContent = row
          ? `${row.model} · ${row.output_format === "ogg" ? "Ogg Opus" : "MP3"} · saved recipe ${row.revision.slice(0, 8)}${row.available ? "" : " · backend unavailable"}`
          : "Choose a saved voice profile.";
      };
      this.profile.setAttribute("aria-label", "Voice profile");
      this.profile.onchange = () => {
        store("production-profile", this.profile.value);
        this.rememberChoice();
        update();
        this.onChange?.();
      };
      this.root.append(
        el("label", {}, "Voice profile", this.profile),
        note,
        el("a", {
          href: "/settings#voice-profiles",
          "data-nav": "",
          text: "Manage saved voice profiles",
        }),
      );
      update();
      return;
    }
    this.voice = el("select", { "aria-label": "Voice" });
    this.speed = el(
      "select",
      { "aria-label": "Speech generation speed" },
      ...[0.75, 0.9, 1, 1.1, 1.25, 1.5].map((value) =>
        el("option", { value, text: value + "×" }),
      ),
    );
    this.speed.value = String(
      getStored("speech-speed", oldPreference("ttsSpeed") || 1),
    );
    this.note = el("p", { class: "muted", role: "status" });
    this.custom = el("input", {
      type: "text",
      "aria-label": "Voice ID",
      autocomplete: "off",
      spellcheck: "false",
    });
    const advanced = el(
      "div",
      { class: "filters" },
      el("label", {}, "Voice", this.voice),
      el("label", {}, "Speech speed", this.speed),
    );
    const details = el(
      "details",
      {},
      el("summary", { text: "Voice and speech settings" }),
      compact ? advanced : null,
      this.note,
      el("button", {
        type: "button",
        text: "Refresh voice list",
        onclick: () => this.loadVoices(true, this.voice.value),
      }),
      el("label", {}, "Or enter another installed voice ID", this.custom),
    );
    this.root.append(
      el(
        "div",
        { class: "filters" },
        el("label", {}, "Narrator (registered TTS profile)", this.profile),
      ),
      ...(compact ? [] : [advanced]),
      details,
    );
    this.profile.onchange = () => {
      this.loadVoices(
        this.discover && this.selectedProfile()?.reachable === true,
      );
      this.rememberChoice();
      this.onChange?.();
    };
    this.voice.onchange = () => {
      this.custom.value = "";
      store("production-voice:" + this.profile.value, this.voice.value);
      this.rememberChoice();
      this.onChange?.();
    };
    this.custom.onchange = () => {
      if (this.custom.value.trim())
        store(
          "production-voice:" + this.profile.value,
          this.custom.value.trim(),
        );
      this.rememberChoice();
      this.onChange?.();
    };
    this.speed.onchange = () => {
      store("speech-speed", Number(this.speed.value));
      this.onChange?.();
    };
    this.loadVoices(
      this.discover && this.selectedProfile()?.reachable === true,
    );
  }
  selectedProfile() {
    return this.profiles.profiles.find(
      (profile) => profile.id === this.profile.value,
    );
  }
  rememberChoice() {
    if (this.fixedProfiles) {
      store("narrator-choice", "profile:" + this.profile.value);
      return;
    }
    const settings = this.settings();
    store("narrator-choice", `tts:${settings.profile}:${settings.voice}`);
  }
  settings() {
    if (this.fixedProfiles)
      return {
        profile: this.profile.value,
        profile_revision: this.selectedProfile()?.revision,
      };
    return {
      profile: this.profile.value,
      voice: this.custom.value.trim() || this.voice.value,
      speed: Number(this.speed.value),
    };
  }
  options(names, registered, selected) {
    const labels = new Map(registered.map((row) => [row.voice, row.label]));
    this.voice.replaceChildren(
      ...[...new Set([...names, selected].filter(Boolean))].map((voice) =>
        el("option", { value: voice, text: labels.get(voice) || voice }),
      ),
    );
    this.voice.value = selected || names[0] || "";
  }
  async loadVoices(probe = false, preferred = null) {
    if (this.fixedProfiles) return;
    const token = (this.token = (this.token || 0) + 1),
      selected = this.profile.value;
    store("production-profile", selected);
    this.custom.value = "";
    const voice =
      preferred ||
      getStored(
        "production-voice:" + selected,
        oldPreference("voice-" + selected),
      ) ||
      this.selectedProfile()?.voice ||
      "";
    this.options([this.selectedProfile()?.voice].filter(Boolean), [], voice);
    this.note.textContent = "Loading known narrators…";
    try {
      const data = await api(
        "/api/library/production/voices?" +
          new URLSearchParams({
            profile: selected,
            ...(probe ? { probe: "1" } : {}),
          }),
      );
      if (token !== this.token || selected !== this.profile.value) return;
      this.options(
        data.voices,
        data.registered,
        this.voice.value || data.default_voice,
      );
      this.note.textContent = `${data.voices.length} known narrators · ${data.registered.length} registered`;
    } catch (error) {
      if (token === this.token) this.note.textContent = error.message;
    }
  }
}

export function matchesPreparation(item, settings) {
  return (
    item.profile === settings.profile &&
    (settings.profile_revision
      ? item.profile_revision === settings.profile_revision
      : item.voice === settings.voice && (item.speed ?? item.speech_speed ?? 1) === settings.speed)
  );
}

export function collectionPreparationProgress(lectures, jobs, settings) {
  const byId = new Map(lectures.map((row) => [row.id, row]));
  const active = jobs.filter((job) => {
    const row = byId.get(job.lecture_id);
    return row && job.spoken_sha256 === row.spoken_sha256 &&
      ["queued", "running"].includes(job.state) && matchesPreparation(job, settings);
  });
  const ready = [...byId.values()].filter((row) => row.recordings.some((recording) =>
    recording.complete && recording.generator && matchesPreparation(recording.generator, settings),
  )).length;
  return { active, ready, total: byId.size, generating: new Set(active.map((job) => job.lecture_id)).size };
}

export function wholePreparationQueued(jobs, selection) {
  const ids = selection.lecture_id
    ? [selection.lecture_id]
    : selection.lecture_ids;
  const active = jobs.filter(
    (job) =>
      ["queued", "running"].includes(job.state) &&
      job.requested_blocks === null,
  );
  if (ids) {
    const queued = new Set(active.map((job) => job.lecture_id));
    return ids.length > 0 && ids.every((id) => queued.has(id));
  }
  return active.length > 0 && active.length === jobs.length;
}

export function preparationPanel({
  lectureId = null,
  courseId = null,
  lectures = null,
  revision = null,
  label,
  description,
  onPlay = null,
}) {
  const root = el(
    "section",
    { class: "preparation-panel section" },
    el("h2", { text: label || "Generate audio" }),
  );
  if (description) root.append(el("p", { class: "muted", text: description }));
  const controls = el("div");
  const status = el("p", { role: "status", class: "muted" });
  const submit = el("button", {
    type: "button",
    class: "primary",
    disabled: true,
    text: lectureId
      ? "Cache whole lecture"
      : courseId
        ? "Queue whole collection"
        : "Queue all lectures",
  });
  const stop = el("button", {
    type: "button",
    disabled: true,
    text: "Stop generation",
  });
  const ready = el("button", {
    type: "button",
    hidden: true,
    text: "Play this narrator",
  });
  const actions = el(
    "div",
    { class: "actions" },
    submit,
    stop,
    ready,
    el("a", {
      href: "/production#jobs",
      "data-nav": "",
      text: "View generation queue",
    }),
  );
  root.append(controls, actions, status);
  (async () => {
    try {
      // Showing playback controls never probes a remote speech service.
      const profiles = await api("/api/library/production?probe=0");
      if (!profiles.profiles.length) {
        status.textContent =
          "No TTS connection is configured. Prepared recordings are still available.";
        return;
      }
      const narrator = new NarrationControls(profiles, { compact: true });
      controls.append(narrator.root);
      submit.disabled = !profiles.tools_available;
      if (!profiles.tools_available)
        status.textContent =
          "Generation requires the production tools on this server.";
      let pending = [];
      const selection = lectureId
        ? { lecture_id: lectureId, ...(revision ? { revision } : {}) }
        : courseId
          ? { course_id: courseId }
          : { lecture_ids: lectures?.map((row) => row.id) };
      const poll = async () => {
        const listed = (await api("/api/library/production/jobs")).jobs;
        const settings = narrator.settings();
        const progress = lectures && collectionPreparationProgress(lectures, listed, settings);
        const jobs = progress?.active ?? listed.filter(
          (job) =>
            (lectureId
              ? job.lecture_id === lectureId &&
                (!revision || job.revision === revision)
              : pending.some((item) => item.id === job.id)) &&
            matchesPreparation(job, settings),
        );
        pending = jobs;
        const unfinished = jobs.filter((job) =>
          ["queued", "running"].includes(job.state),
        );
        stop.disabled = !unfinished.length;
        submit.disabled =
          !profiles.tools_available || wholePreparationQueued(jobs, selection);
        const completed = jobs.find((job) => job.state === "ready");
        ready.hidden = !completed || !onPlay;
        ready.onclick = () => onPlay?.(completed);
        if (progress) {
          status.textContent = `${progress.ready}/${progress.total} lectures ready in this voice · ${progress.generating} queued or running`;
        } else if (jobs.length === 1)
          status.textContent = `${jobs[0].state} · ${jobs[0].inventory.ready}/${jobs[0].inventory.total || "?"} audio blocks ready${jobs[0].error ? " · " + jobs[0].error : ""}`;
        else if (jobs.length)
          status.textContent = `${unfinished.length} queued or running · ${jobs.filter((job) => job.state === "ready").length} finished jobs`;
        else
          status.textContent =
            "Queue all audio blocks for the selected narrator. Completed matching blocks are reused.";
      };
      stop.onclick = async () => {
        stop.disabled = true;
        try {
          const results = await Promise.allSettled(
            pending
              .filter((job) => ["queued", "running"].includes(job.state))
              .map((job) =>
                api("/api/library/production/jobs/" + job.id, {
                  method: "DELETE",
                }),
              ),
          );
          const failed = results.find((result) => result.status === "rejected");
          if (failed) status.textContent = failed.reason.message;
          else await poll();
        } catch (error) {
          status.textContent = error.message;
        }
      };
      submit.onclick = async () => {
        submit.disabled = true;
        try {
          const settings = narrator.settings();
          const result = await api("/api/library/production/prepare", {
            method: "POST",
            body: JSON.stringify({ ...selection, ...settings }),
          });
          pending = result.jobs || [result];
          stop.disabled = !pending.some((job) =>
            ["queued", "running"].includes(job.state),
          );
          if (lectures) await poll();
          else {
            const count = result.jobs?.length || 1;
            status.textContent = `${count === 1 ? "Lecture" : count + " lectures"} queued for ${narrator.selectedProfile()?.label || settings.voice || settings.profile}. Completed matching audio blocks are reused.`;
          }
        } catch (error) {
          status.textContent = error.message;
        } finally {
          submit.disabled =
            !profiles.tools_available ||
            wholePreparationQueued(pending, selection);
        }
      };
      narrator.onChange = () => {
        ready.hidden = true;
        stop.disabled = true;
        poll().catch((error) => {
          status.textContent = error.message;
        });
      };
      const timer = setInterval(() => {
        if (!root.isConnected) clearInterval(timer);
        else
          poll().catch((error) => {
            status.textContent = error.message;
          });
      }, 2000);
      await poll();
    } catch (error) {
      status.textContent = error.message;
    }
  })();
  return root;
}

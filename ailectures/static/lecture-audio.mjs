import { api, post, el, getStored, store } from "./api.mjs";
import { timeAtWord } from "./transcript.mjs";
import {
  blockGrid,
  recordingStates,
  generationStatus,
} from "./audio-blocks.mjs";

export function narratorInventory(choice, row, jobs, pages) {
  const recording = row.recordings.find((r) => r.id === choice?.recording_id);
  const job = [...jobs]
    .reverse()
    .find(
      (job) =>
        job.lecture_id === row.id &&
        job.revision === row.revision &&
        job.variant === choice?.variant &&
        job.speed === choice?.speed,
    );
  const states = recording
    ? recordingStates(recording)
    : pages.map(() => "missing");
  if (job?.inventory.states?.length && (!recording || !recording.complete))
    return { states: job.inventory.states, job, recording };
  return { states, job, recording };
}

export function resumeTarget(row, progress, pages) {
  if (
    progress?.spoken_sha256 !== row.spoken_sha256 ||
    !Number.isFinite(progress?.anchor_word)
  )
    return null;
  let remaining = progress.anchor_word;
  for (let index = 0; index < pages.length; index++) {
    const words = pages[index].trim().split(/\s+/).length;
    if (remaining < words || index === pages.length - 1)
      return {
        index,
        seconds: timeAtWord(pages[index], null, Math.min(remaining, words)),
      };
    remaining -= words;
  }
  return null;
}

// One selection owns playback, missing-block requests, and whole-lecture caching.
export class LectureAudio {
  constructor({
    row,
    player,
    progress,
    onChange,
    message,
    active = () => true,
  }) {
    Object.assign(this, { row, player, progress, onChange, message, active });
    this.jobs = [];
    this.views = new Map();
    this.epoch = 0;
    this.root = el("section", { class: "preparation-panel section" });
    this.select = el("select", { "aria-label": "Voice" });
    this.status = el("p", {
      class: "muted",
      role: "status",
      "aria-live": "polite",
    });
    this.blocks = el("div");
    this.playButton = el("button", {
      type: "button",
      class: "primary",
      text: progress ? "Resume" : "Play",
      onclick: () => this.play(),
    });
    this.cache = el("button", {
      type: "button",
      text: "Cache whole lecture",
      onclick: () => this.prepare(false),
    });
    this.stop = el("button", {
      type: "button",
      text: "Stop generation",
      disabled: true,
      onclick: () => this.cancel(),
    });
    this.speed = el(
      "select",
      { "aria-label": "Speech generation speed" },
      ...[0.75, 0.9, 1, 1.1, 1.25, 1.5].map((value) =>
        el("option", { value, text: value + "×" }),
      ),
    );
    this.speed.value = String(getStored("speech-speed", 1));
    this.root.append(
      el("label", {}, "Voice for playback and generation", this.select),
      el(
        "div",
        { class: "actions" },
        this.playButton,
        this.cache,
        this.stop,
        el("a", {
          href: "/production#jobs",
          "data-nav": "",
          text: "View generation queue",
        }),
      ),
      this.status,
      this.blocks,
      el(
        "details",
        {},
        el("summary", { text: "Speech settings" }),
        el("label", {}, "Generation speed", this.speed),
        el("p", {
          class: "muted",
          text: "Changing generation speed selects a separate recording. Playback speed is available in the player below.",
        }),
      ),
    );
    this.select.onchange = () => this.choose();
    this.speed.onchange = async () => {
      const epoch = ++this.epoch;
      this.pending = null;
      this.player.audio.pause();
      store("speech-speed", Number(this.speed.value));
      try {
        await this.loadOptions();
        if (epoch === this.epoch) this.choose();
      } catch (error) {
        this.showError(error);
      }
    };
    this.ready = this.initialize();
  }
  async loadOptions() {
    const selected = this.select.value;
    this.data = await api(
      "/api/library/production/narrators?" +
        new URLSearchParams({
          lecture_id: this.row.id,
          release: this.row.origin.release,
          speed: this.speed.value,
        }),
    );
    this.choices = this.data.choices;
    this.pages = this.data.pages;
    this.select.replaceChildren(
      ...this.choices.map((choice) => el("option", { value: choice.key })),
    );
    if (this.choices.some((choice) => choice.key === selected))
      this.select.value = selected;
  }
  async initialize() {
    try {
      await this.loadOptions();
      this.jobs = (await api("/api/library/production/jobs")).jobs;
    } catch (error) {
      this.data = { tools_available: false };
      this.pages = this.row.recordings[0]?.pages || [this.row.transcript];
      this.choices = this.row.recordings.map((r) => ({
        key: "recording:" + r.variant,
        label: r.label || r.variant,
        recording_id: r.id,
      }));
      this.select.replaceChildren(
        ...this.choices.map((c) => el("option", { value: c.key })),
      );
      this.initialError = error.message;
    }
    if (this.disposed || !this.active()) return;
    const remembered = getStored("narrator-choice");
    const profile = getStored("production-profile");
    const voice = getStored("production-voice:" + profile);
    const preferred =
      this.choices.find((c) => c.key === remembered) ||
      this.choices.find(
        (c) => c.profile === profile && (!voice || c.voice === voice),
      ) ||
      this.choices.find(
        (c) =>
          c.recording_id &&
          c.recording_id ===
            (this.player.row?.id === this.row.id
              ? this.player.recording?.id
              : this.progress?.recording_id),
      ) ||
      this.choices.find(
        (c) =>
          this.row.recordings.find((r) => r.id === c.recording_id)?.complete,
      ) ||
      this.choices.find((c) => c.profile === this.data.default_profile) ||
      this.choices[0];
    this.select.value = preferred?.key || "";
    this.choose(false);
    this.timer = setInterval(() => {
      if (
        this.disposed ||
        (!this.root.isConnected &&
          this.player.requestMissing !== this.missingHandler)
      ) {
        clearInterval(this.timer);
        return;
      }
      this.poll().catch((error) => this.showError(error));
    }, 1500);
  }
  get choice() {
    return this.choices.find((choice) => choice.key === this.select.value);
  }
  get inventory() {
    return narratorInventory(this.choice, this.row, this.jobs, this.pages);
  }
  choose(remember = true) {
    this.epoch++;
    this.pending = null;
    const choice = this.choice;
    if (remember && choice) {
      store("narrator-choice", choice.key);
      if (choice.profile) {
        store("production-profile", choice.profile);
        store("production-voice:" + choice.profile, choice.voice);
      }
    }
    const position =
      this.player.row?.id === this.row.id ? this.player.position() : null;
    this.resume = position || this.resume || this.progress;
    this.player.open(
      this.views.get(choice?.recording_id) || this.row,
      this.resume,
      choice?.recording_id || false,
    );
    this.target = !this.player.recording
      ? resumeTarget(this.row, this.resume, this.pages)
      : null;
    if (this.target) this.player.index = this.target.index;
    this.missingHandler = (index, seconds) => this.require(index, seconds);
    this.player.requestMissing = this.missingHandler;
    this.onChange?.();
    this.render();
  }
  render() {
    for (const option of this.select.options) {
      const choice = this.choices.find((c) => c.key === option.value);
      const { states, job, recording } = narratorInventory(
        choice,
        this.row,
        this.jobs,
        this.pages,
      );
      const count = states.filter((state) => state === "ready").length;
      option.textContent = `${choice.label} · ${count}/${states.length} generated${recording?.complete ? " · ready" : job && ["queued", "running"].includes(job.state) ? " · generating" : ""}`;
    }
    const { states, job } = this.inventory;
    this.cache.disabled =
      !this.choice?.profile ||
      !this.data.tools_available ||
      this.submitting ||
      ["queued", "running"].includes(job?.state);
    this.stop.disabled = !["queued", "running"].includes(job?.state);
    this.select.disabled = !this.choices.length;
    this.status.textContent = this.pending
      ? `Waiting for block ${this.pending.index + 1} in ${this.choice.label}. Playback will start when it is ready.${job?.error ? " · " + job.error : ""}`
      : job
        ? `${job.state} · ${states.filter((state) => state === "ready").length}/${states.length} audio blocks ready${job.error ? " · " + job.error : ""}`
        : this.initialError ||
          (this.choice?.recording_id
            ? "Play uses the selected voice."
            : this.choice?.profile
              ? this.data.tools_available
                ? "Press Play to generate and listen in this voice. Completed blocks are reused."
                : "This server can play prepared recordings; generation tools are unavailable here."
              : "No voice or prepared recording is available. Configure a TTS connection in Production.");
    this.blocks.replaceChildren(
      el("h3", { text: "Audio blocks" }),
      blockGrid(states, (index) => this.play(index, 0)),
      ...(job?.inventory.queue || []).map((item) =>
        el("p", {
          class: "muted",
          text: `Block ${item.page + 1} · ${generationStatus(item)}`,
        }),
      ),
    );
    if (this.pending)
      document.getElementById("playing-note").textContent =
        this.status.textContent;
  }
  play(index = this.player.index, seconds = null) {
    this.player.play(index, seconds);
  }
  async require(index, seconds) {
    if (!this.choice?.profile || !this.data.tools_available) {
      this.showError(
        new Error(
          "Audio for this voice is not generated, and generation is unavailable on this server. Choose a prepared voice or configure TTS in Production.",
        ),
      );
      return;
    }
    this.pending = {
      index,
      seconds:
        seconds ?? (this.target?.index === index ? this.target.seconds : 0),
      epoch: this.epoch,
    };
    await this.prepare(true);
  }
  async prepare(forPlayback) {
    if (this.submitting) return;
    const choice = this.choice;
    if (!choice?.profile) return;
    const epoch = this.epoch;
    this.submitting = true;
    this.render();
    try {
      const job = await post("/api/library/production/prepare", {
        lecture_id: this.row.id,
        revision: this.row.revision,
        profile: choice.profile,
        voice: choice.voice,
        speed: choice.speed,
      });
      this.jobs = this.jobs
        .filter((existing) => existing.id !== job.id)
        .concat(job);
      if (epoch === this.epoch) {
        this.render();
        if (forPlayback) await this.poll();
      }
    } catch (error) {
      if (epoch === this.epoch) {
        this.pending = null;
        this.showError(error);
      }
    } finally {
      this.submitting = false;
      this.cache.disabled =
        !this.choice?.profile ||
        !this.data.tools_available ||
        ["queued", "running"].includes(this.inventory.job?.state);
    }
  }
  async poll() {
    if (this.polling) return;
    this.polling = true;
    const epoch = this.epoch;
    try {
      this.jobs = (await api("/api/library/production/jobs")).jobs;
      if (epoch !== this.epoch || this.disposed) return;
      this.render();
      const { job } = this.inventory;
      const pending = this.pending;
      if (!pending || !job) return;
      if (["failed", "cancelled", "settings_changed"].includes(job.state)) {
        this.pending = null;
        this.showError(
          new Error(
            job.error || `Generation ${job.state}. Press Play to retry.`,
          ),
        );
        return;
      }
      if (job.state === "running" && pending.priorityAttempt !== job.attempts) {
        await post(`/api/library/production/jobs/${job.id}/playback`, {
          index: pending.index,
        });
        pending.priorityAttempt = job.attempts;
        if (epoch !== this.epoch || this.pending !== pending || this.disposed)
          return;
      }
      if (
        job.inventory.states?.[pending.index] !== "ready" &&
        job.state !== "ready"
      )
        return;
      let row;
      if (job.published) {
        row = await api(
          "/api/library/lectures/" + encodeURIComponent(this.row.id),
        );
        if (
          row.revision !== this.row.revision ||
          !row.recordings.some((r) => r.variant === job.variant)
        )
          row = null;
      }
      row ||= await api(`/api/library/production/jobs/${job.id}/playback`);
      if (epoch !== this.epoch || this.pending !== pending || this.disposed)
        return;
      const recording = row.recordings.find((r) => r.variant === job.variant);
      if (!recording?.segments.some((s) => s.index === pending.index)) return;
      this.row.recordings = this.row.recordings
        .filter((r) => r.variant !== recording.variant)
        .concat(recording);
      this.choice.recording_id = recording.id;
      this.views.set(recording.id, row);
      this.pending = null;
      this.player.open(row, null, recording.id);
      this.onChange?.();
      this.render();
      this.player.play(pending.index, pending.seconds);
    } finally {
      this.polling = false;
    }
  }
  async cancel() {
    this.pending = null;
    this.epoch++;
    this.player.audio.pause();
    const job = this.inventory.job;
    if (!job) return;
    try {
      await api("/api/library/production/jobs/" + job.id, { method: "DELETE" });
      await this.poll();
    } catch (error) {
      this.showError(error);
    }
  }
  showError(error) {
    this.status.textContent = error.message;
    this.message(error.message);
  }
  dispose() {
    this.disposed = true;
    this.pending = null;
    clearInterval(this.timer);
  }
}

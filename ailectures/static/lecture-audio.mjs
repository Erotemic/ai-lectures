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
    return {
      states: job.inventory.states.map((state, index) =>
        states.length === job.inventory.states.length &&
        states[index] === "ready"
          ? "ready"
          : state,
      ),
      job,
      recording,
    };
  return { states, job, recording };
}

export function voiceGroups(choices, row, jobs, pages, selected) {
  const groups = [
    { label: "Audio available", choices: [] },
    { label: "Generating", choices: [] },
    { label: "Generate another voice", choices: [] },
  ];
  for (const choice of choices) {
    const { states, job } = narratorInventory(choice, row, jobs, pages);
    if (states.includes("ready")) groups[0].choices.push(choice);
    else if (["queued", "running"].includes(job?.state))
      groups[1].choices.push(choice);
    else if (choice.profile_default || choice.key === selected)
      groups[2].choices.push(choice);
  }
  return groups.filter((group) => group.choices.length);
}

export function lectureGenerations(
  jobs,
  lectureId,
  recentlyStopped = new Set(),
) {
  return jobs.filter(
    (job) =>
      job.lecture_id === lectureId &&
      (["queued", "running", "failed", "settings_changed"].includes(
        job.state,
      ) ||
        recentlyStopped.has(job.id)),
  );
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

export function blockWindow(index, total, ahead = 0) {
  const count = Math.max(0, Math.min(8, Math.floor(Number(ahead) || 0)));
  return Array.from(
    { length: Math.max(0, Math.min(total - index, count + 1)) },
    (_, offset) => index + offset,
  );
}

export function coversBlocks(job, blocks) {
  return Boolean(
    job &&
    !["cancelled", "failed", "settings_changed"].includes(job.state) &&
    (job.requested_blocks === null ||
      blocks.every((block) => job.requested_blocks?.includes(block))),
  );
}

export function preferredNarrator(
  choices,
  data,
  { remembered, recordingId, profile, voice } = {},
) {
  return (
    choices.find(
      (choice) =>
        choice.key === remembered || choice.aliases?.includes(remembered),
    ) ||
    choices.find(
      (choice) => choice.recording_id && choice.recording_id === recordingId,
    ) ||
    choices.find(
      (choice) =>
        choice.profile === data.preferred_profile && choice.profile_default,
    ) ||
    choices.find(
      (choice) =>
        profile &&
        choice.profile === profile &&
        (!voice || choice.voice === voice),
    ) ||
    choices.find((choice) => choice.recording_complete) ||
    choices.find((choice) => choice.recording_id) ||
    choices.find(
      (choice) =>
        choice.profile === data.default_profile && choice.profile_default,
    ) ||
    choices[0]
  );
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
    course = null,
  }) {
    Object.assign(this, { row, player, progress, onChange, message, active, course });
    this.jobs = [];
    this.views = new Map();
    this.recentlyStopped = new Set();
    this.stopping = new Set();
    this.epoch = 0;
    this.root = el("section", { class: "preparation-panel section" });
    this.select = el("select", { "aria-label": "Voice", disabled: true });
    this.status = el("p", {
      class: "muted",
      role: "status",
      "aria-live": "polite",
    });
    this.blocks = el("div");
    this.generations = el("section", {
      "aria-label": "Generation for this lecture",
    });
    this.moreSearch = el("input", {
      type: "search",
      placeholder: "Search voice or profile",
      "aria-label": "Find a voice",
    });
    this.moreSelect = el("select", { size: "6", "aria-label": "All voices" });
    this.more = el(
      "details",
      { hidden: true },
      el("summary", { text: "More voices" }),
      el("p", {
        class: "muted",
        text: "Browse the full voice catalog. Use a voice to select it for both playback and generation.",
      }),
      this.moreSearch,
      this.moreSelect,
      el("button", {
        type: "button",
        text: "Use this voice",
        onclick: () => {
          if (!this.moreSelect.value) return;
          this.voiceOptions(this.moreSelect.value);
          this.select.value = this.moreSelect.value;
          this.choose();
          this.more.open = false;
        },
      }),
    );
    this.moreSearch.oninput = () => this.catalogOptions();
    this.more.ontoggle = () => {
      if (this.more.open) this.catalogOptions();
    };
    this.playButton = el("button", {
      type: "button",
      class: "primary",
      disabled: true,
      text: progress ? "Resume" : "Play",
      onclick: () => this.play(),
    });
    this.cache = el("button", {
      type: "button",
      disabled: true,
      text: "Cache whole lecture",
      onclick: () => this.prepare(false),
    });
    this.clearCache = el("button", {
      type: "button", text: "Clear this voice’s cache", disabled: true,
      onclick: () => this.clearVoiceCache(),
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
    this.continueBlocks = el("input", {
      type: "checkbox",
      "aria-label": "Continue to next blocks",
    });
    this.continueBlocks.checked = getStored("continue-blocks", false);
    this.ahead = el("input", {
      type: "number",
      min: "0",
      max: "8",
      step: "1",
      "aria-label": "Blocks ahead",
    });
    this.ahead.value = String(getStored("blocks-ahead", 1));
    this.ahead.disabled = !this.continueBlocks.checked;
    this.status.textContent = "Loading voices…";
    this.continueBlocks.onchange = () => {
      store("continue-blocks", this.continueBlocks.checked);
      this.ahead.disabled = !this.continueBlocks.checked;
      if (!this.player.audio.paused) this.queueAhead(this.player.index);
    };
    this.ahead.onchange = () => {
      this.ahead.value = String(
        Math.max(0, Math.min(8, Math.floor(Number(this.ahead.value) || 0))),
      );
      store("blocks-ahead", Number(this.ahead.value));
      if (!this.player.audio.paused) this.queueAhead(this.player.index);
    };
    this.generationQueueLink = el("a", { href: "/production#jobs", "data-nav": "", text: "View generation queue" });
    this.speechSettings = el("details", {}, el("summary", { text: "Speech settings" }),
        el("label", {}, "Generation speed", this.speed),
        el("p", { class: "muted", text: "Changing generation speed selects a separate recording. Playback speed is available in the player below." }));
    this.audioSummary = el("summary", { text: "Audio blocks & generation" });
    this.advanced = el("details", { class: "audio-tools" },
      this.audioSummary,
      this.cache, this.stop, this.clearCache,
      this.generationQueueLink,
      el("div", { class: "filters" },
        el("label", { class: "check" }, this.continueBlocks, "Continue to next blocks"),
        el("label", {}, "Blocks ahead", this.ahead)),
      el("p", { class: "muted", text: "Complete prepared recordings play through by default. Turn off block continuation to study one passage. For missing audio, continuation and lookahead generate additional blocks only when you enable them." }),
      this.generations, this.blocks,
      this.speechSettings,
    );
    this.voiceLabelText = document.createTextNode("Voice for playback and generation");
    this.root.append(
      el("label", {}, this.voiceLabelText, this.select),
      this.more,
      el(
        "div",
        { class: "actions" },
        this.playButton,
      ),
      this.status,
      this.advanced,
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
    this.voiceSignature = null;
    this.select.replaceChildren(
      ...this.choices.map((choice) => el("option", { value: choice.key })),
    );
    if (this.choices.some((choice) => choice.key === selected))
      this.select.value = selected;
  }
  async initialize() {
    const jobs = api(this.jobsURL()).catch((error) => {
      this.queueError = error.message;
      return { jobs: [] };
    });
    try {
      await this.loadOptions();
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
    const preferred = preferredNarrator(this.choices, this.data, {
      remembered,
      profile,
      voice,
      recordingId:
        this.player.row?.id === this.row.id
          ? this.player.recording?.id
          : this.progress?.recording_id,
    });
    this.select.value = preferred?.key || "";
    this.choose(false);
    jobs.then((result) => {
      if (this.disposed || !this.active()) return;
      this.jobs = result.jobs;
      this.render();
    });
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
  jobsURL() {
    return (
      "/api/library/production/jobs?" +
      new URLSearchParams({ lecture_id: this.row.id })
    );
  }
  get inventory() {
    return narratorInventory(this.choice, this.row, this.jobs, this.pages);
  }
  choose(remember = true) {
    const selectedBlock =
      this.pending?.index ??
      (this.player.row?.id === this.row.id ? this.player.index : null);
    this.epoch++;
    this.submitting = false;
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
    if (this.player.lectureController !== this) {
      this.player.lectureController?.dispose();
      this.player.lectureController = this;
    }
    this.player.open(
      this.views.get(choice?.recording_id) || this.row,
      remember ? null : this.resume,
      choice?.recording_id || false,
      this.course,
    );
    if (this.continueBlocks) {
      this.continueBlocks.checked = getStored("continue-blocks", Boolean(this.player.recording?.complete));
      if (this.ahead) this.ahead.disabled = !this.continueBlocks.checked;
    }
    this.target = !this.player.recording
      ? resumeTarget(this.row, this.resume, this.pages)
      : null;
    if (this.target) this.player.index = this.target.index;
    if (remember && selectedBlock !== null) {
      const index = Math.min(
        selectedBlock,
        (this.player.recording?.pages || this.pages).length - 1,
      );
      this.player.index = index;
      this.target = { index, seconds: 0 };
      if (this.player.recording) this.player.load(index, 0, false);
    }
    this.missingHandler = (index, seconds) => this.require(index, seconds);
    this.player.requestMissing = this.missingHandler;
    this.player.continueBlocks = () => this.continueBlocks.checked;
    this.player.onBlockPlay = (index) => this.queueAhead(index);
    this.onChange?.();
    this.render();
  }
  render() {
    this.voiceOptions();
    const canGenerate = Boolean(this.data.tools_available && this.choice?.profile);
    this.audioSummary.textContent = this.data.tools_available ? "Audio blocks & generation" : "Audio blocks";
    this.voiceLabelText.textContent = this.data.tools_available ? "Voice for playback and generation" : "Voice for playback";
    this.clearCache.hidden = this.cache.hidden = this.stop.hidden = !canGenerate;
    this.clearCache.disabled = !canGenerate || this.submitting || this.clearing;
    this.generations.hidden = !canGenerate;
    this.generationQueueLink.hidden = !canGenerate;
    this.speechSettings.hidden = !canGenerate;
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
    this.playButton.disabled = !this.choice || (!canGenerate && !this.choice.recording_id);
    const wholeLectureActive =
      ["queued", "running"].includes(job?.state) &&
      job.requested_blocks === null;
    this.cache.textContent = wholeLectureActive
      ? "Caching whole lecture…"
      : "Cache whole lecture";
    this.cache.title = wholeLectureActive
      ? "This voice is already queued for whole-lecture preparation. See its progress below."
      : "Generate missing blocks for the selected voice; reuse existing audio.";
    this.cache.disabled =
      !this.choice?.profile ||
      !this.data.tools_available ||
      this.submitting || this.clearing ||
      wholeLectureActive;
    this.stop.disabled =
      !["queued", "running"].includes(job?.state) || this.stopping.has(job?.id);
    this.select.disabled = !this.choices.length || this.clearing;
    this.more.hidden = !this.choices.length;
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
    this.generationList();
    if (this.pending)
      document.getElementById("playing-note").textContent =
        this.status.textContent;
  }
  voiceOptions(selected = this.select.value) {
    const groups = voiceGroups(
      this.choices,
      this.row,
      this.jobs,
      this.pages,
      selected,
    );
    const signature = JSON.stringify(
      groups.map((group) => [
        group.label,
        group.choices.map((choice) => choice.key),
      ]),
    );
    if (signature !== this.voiceSignature) {
      this.select.replaceChildren(
        ...groups.map((group) =>
          el(
            "optgroup",
            { label: group.label },
            ...group.choices.map((choice) =>
              el("option", { value: choice.key }),
            ),
          ),
        ),
      );
      this.voiceSignature = signature;
    }
    this.select.value = selected;
  }
  catalogOptions() {
    const selected = this.moreSelect.value;
    const query = this.moreSearch.value.trim().toLocaleLowerCase();
    const groups = new Map();
    for (const choice of this.choices) {
      if (
        !`${choice.label} ${choice.profile || ""} ${choice.voice || ""}`
          .toLocaleLowerCase()
          .includes(query)
      )
        continue;
      const label =
        this.data.profiles?.find((profile) => profile.id === choice.profile)
          ?.label || "Installed recordings";
      if (!groups.has(label)) groups.set(label, []);
      const { states } = narratorInventory(
        choice,
        this.row,
        this.jobs,
        this.pages,
      );
      groups.get(label).push(
        el("option", {
          value: choice.key,
          text: `${choice.label} · ${states.filter((state) => state === "ready").length}/${states.length} generated`,
        }),
      );
    }
    this.moreSelect.replaceChildren(
      ...[...groups].map(([label, options]) =>
        el("optgroup", { label }, ...options),
      ),
    );
    if (
      [...this.moreSelect.options].some((option) => option.value === selected)
    )
      this.moreSelect.value = selected;
  }
  generationList() {
    const jobs = lectureGenerations(
      this.jobs,
      this.row.id,
      this.recentlyStopped,
    );
    this.generations.replaceChildren(
      el("h3", { text: "Generation for this lecture" }),
      ...jobs.map((job) => {
        const label =
          this.choices.find((choice) => choice.variant === job.variant)
            ?.label || `${job.profile} · ${job.voice}`;
        const active = ["queued", "running"].includes(job.state);
        return el(
          "div",
          { class: "generation-item", "data-job": job.id },
          el("strong", { text: label }),
          el("p", {
            class: "muted",
            text: `${job.speed || 1}× speech · ${job.state} · ${job.requested_blocks ? (job.requested_blocks.length === 1 ? "block " + (job.requested_blocks[0] + 1) + " requested" : job.requested_blocks.length + " blocks requested") : "whole lecture"} · ${job.inventory.ready}/${job.inventory.total || "?"} blocks ready${job.revision !== this.row.revision ? " · earlier transcript revision" : ""}`,
          }),
          job.error ? el("p", { class: "notice", text: job.error }) : null,
          ...(active ? job.inventory.queue || [] : []).slice(0, 1).map((item) =>
            el("p", {
              class: "muted",
              text: `Block ${item.page + 1} · ${generationStatus(item)}`,
            }),
          ),
          active
            ? el("button", {
                type: "button",
                text: this.stopping.has(job.id)
                  ? "Stopping…"
                  : "Stop generation",
                "aria-label": `Stop generation for ${label} at ${job.speed || 1}×`,
                disabled: this.stopping.has(job.id),
                onclick: () => this.cancel(job),
              })
            : null,
        );
      }),
      ...(this.queueError
        ? [
            el("p", {
              class: "notice",
              text: "Generation status unavailable: " + this.queueError,
            }),
          ]
        : []),
      ...(jobs.length || this.queueError
        ? []
        : [
            el("p", {
              class: "muted",
              text: "No active generation for this lecture.",
            }),
          ]),
    );
  }
  play(index = this.player.index, seconds = null) {
    this.player.play(index, seconds);
  }
  playPrepared(index = this.player.index, seconds = null) {
    if (!this.player.recording?.segments.some((segment) => segment.index === index)) {
      this.message("The next lecture has no prepared audio for the selected voice. Choose an available voice or press Play to generate it.");
      return;
    }
    this.play(index, seconds);
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
    const blocks = blockWindow(
      index,
      this.pages.length,
      this.continueBlocks.checked ? this.ahead.value : 0,
    );
    if (coversBlocks(this.inventory.job, blocks)) await this.poll();
    else await this.prepare(true);
  }
  queueAhead(index) {
    if (
      !this.continueBlocks.checked ||
      !this.choice?.profile ||
      !this.data.tools_available
    )
      return;
    const blocks = blockWindow(index, this.pages.length, this.ahead.value);
    const { job } = this.inventory;
    if (!blocks.length || blocks.every((index) => this.inventory.states[index] === "ready") || coversBlocks(job, blocks)) return;
    this.prepare(false, blocks);
  }
  async clearVoiceCache() {
    const choice = this.choice;
    if (!choice?.profile || this.clearing || this.submitting) return;
    if (!globalThis.confirm(`Clear cached audio for ${choice.voice} (${choice.profile}) in this lecture at all generation speeds? Other voices are kept. Historical media files remain available for later garbage collection. You can then generate fresh audio with the current title settings.`)) return;
    this.clearing = true;
    this.epoch++;
    this.pending = null;
    this.player.audio.pause();
    this.render();
    try {
      await post("/api/library/production/clear-cache", {
        lecture_id: this.row.id, revision: this.row.revision,
        profile: choice.profile, voice: choice.voice,
      });
      this.row = await api("/api/library/lectures/" + encodeURIComponent(this.row.id));
      this.views.clear();
      this.jobs = (await api(this.jobsURL())).jobs;
      await this.loadOptions();
      if (this.disposed || !this.active()) return;
      this.choose(false);
      this.message("Voice cache cleared. Play or cache the lecture to generate fresh audio.");
    } catch (error) { this.showError(error); }
    finally { this.clearing = false; if (!this.disposed) this.render(); }
  }
  async prepare(forPlayback, blocks = null) {
    if (this.submitting || this.clearing || !this.data.tools_available) return;
    const choice = this.choice;
    if (!choice?.profile) return;
    const epoch = this.epoch;
    this.submissionEpoch = epoch;
    if (forPlayback)
      blocks = blockWindow(
        this.pending.index,
        this.pages.length,
        this.continueBlocks.checked ? this.ahead.value : 0,
      );
    this.submitting = true;
    this.render();
    try {
      const job = await post("/api/library/production/prepare", {
        lecture_id: this.row.id,
        revision: this.row.revision,
        profile: choice.profile,
        voice: choice.voice,
        speed: choice.speed,
        ...(choice.base_recording_id
          ? { base_recording_id: choice.base_recording_id }
          : {}),
        ...(blocks === null ? {} : { blocks }),
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
      if (this.submissionEpoch === epoch) {
        this.submitting = false;
        this.cache.disabled =
          !this.choice?.profile ||
          !this.data.tools_available ||
          (["queued", "running"].includes(this.inventory.job?.state) &&
            this.inventory.job.requested_blocks === null);
      }
    }
  }
  async poll() {
    if (this.polling || this.clearing) return;
    this.polling = true;
    const epoch = this.epoch;
    try {
      const jobs = (await api(this.jobsURL())).jobs;
      if (epoch !== this.epoch || this.disposed) return;
      this.jobs = jobs;
      this.queueError = null;
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
  async cancel(job = this.inventory.job) {
    if (!job || this.stopping.has(job.id)) return;
    if (
      job.variant === this.choice?.variant &&
      job.revision === this.row.revision
    ) {
      this.pending = null;
      this.epoch++;
      this.player.audio.pause();
    }
    this.stopping.add(job.id);
    this.render();
    try {
      const result = await api("/api/library/production/jobs/" + job.id, {
        method: "DELETE",
      });
      this.recentlyStopped.add(job.id);
      this.jobs = this.jobs.map((item) =>
        item.id === job.id ? { ...item, ...result } : item,
      );
      this.render();
      await this.poll();
    } catch (error) {
      this.showError(error);
    } finally {
      this.stopping.delete(job.id);
      this.generationList();
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

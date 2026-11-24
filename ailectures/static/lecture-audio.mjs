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
  pages = recording?.pages || choice?.pages || pages;
  const states = recording
    ? recordingStates(recording)
    : pages.map(() => "missing");
  if (job?.inventory.states?.length && (!recording || (!recording.complete && job.inventory.states.length === states.length)))
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
    const generating = ["queued", "running"].includes(job?.state);
    if (choice.quick_select === false && choice.key !== selected && !generating) continue;
    if (states.includes("ready")) groups[0].choices.push(choice);
    else if (["queued", "running"].includes(job?.state))
      groups[1].choices.push(choice);
    else if (choice.quick_select || choice.profile_default || choice.key === selected)
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
  const rememberedChoice = choices.find((choice) => choice.key === remembered || choice.aliases?.includes(remembered));
  return (
    choices.find(
      (choice) => choice.recording_id && choice.recording_id === recordingId,
    ) ||
    (rememberedChoice?.recording_id ? rememberedChoice : null) ||
    choices.find((choice) => choice.recording_complete) ||
    choices.find((choice) => choice.recording_id) ||
    rememberedChoice ||
    choices.find((choice) => choice.server_default) ||
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
    onActivate,
    message,
    archived = false,
    active = () => true,
    course = null,
  }) {
    Object.assign(this, { row, player, progress, onChange, onActivate, message, archived, active, course });
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
      onclick: () => this.togglePlayback(),
    });
    this.cache = el("button", {
      type: "button",
      disabled: true,
      text: "Cache whole lecture",
      onclick: () => this.prepare(false),
    });
    this.generationNotice = el("p", {class:"muted", role:"status", hidden:true});
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
    this.continueBlocks.checked = getStored("continue-blocks", true);
    this.ahead = el("input", {
      type: "number",
      min: "0",
      max: "8",
      step: "1",
      "aria-label": "Blocks ahead",
    });
    this.ahead.value = String(getStored("blocks-ahead", 2));
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
      el("p", { class: "muted", text: "Continuous playback and two blocks ahead are on by default. Turn off continuation to study one passage. Lookahead generates missing upcoming blocks; prepared audio is reused." }),
      this.generations, this.blocks,
      this.speechSettings,
    );
    this.voiceLabelText = document.createTextNode("Voice for playback and generation");
    this.root.append(
      el(
        "div",
        { class: "lecture-audio-main" },
        this.playButton,
        el("label", {}, this.voiceLabelText, this.select),
      ),
      this.generationNotice,
      this.status,
      this.more,
      this.advanced,
    );
    this.select.onchange = () => this.choose();
    this.speed.onchange = async () => {
      const epoch = ++this.epoch;
      this.pending = null;
      if (this.player.lectureController === this) this.player.audio.pause();
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
  preparedOptions() {
    this.data = { tools_available: false };
    this.pages = this.row.recordings[0]?.pages || [this.row.transcript];
    this.choices = this.row.recordings.map((r) => ({ key: "recording:" + r.variant,
      label: r.label || r.variant, recording_id: r.id, recording_complete: r.complete, pages: r.pages }));
    this.select.replaceChildren(...this.choices.map((c) => el("option", { value: c.key })));
  }
  initialize() {
    if (this.archived || this.row?.recordings?.some((recording) => recording.segments.length)) {
      this.preparedOptions();
      this.select.value = preferredNarrator(this.choices, this.data, {
        remembered: getStored("narrator-choice"), recordingId: this.progress?.recording_id,
      })?.key || "";
      this.choose(false);
      // Prepared playback must not wait for profile or generation discovery.
      if (!this.archived) {
        this.optionsReady = this.initializeOptions();
        this.optionsReady.catch((error) => this.showError(error));
      }
      return Promise.resolve();
    }
    return this.initializeOptions();
  }
  async initializeOptions() {
    const jobs = api(this.jobsURL()).catch((error) => {
      this.queueError = error.message;
      return { jobs: [] };
    });
    try {
      await this.loadOptions();
    } catch (error) {
      this.preparedOptions();
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
      if (!this.pending && (document.hidden || !this.root.isConnected ||
          Date.now() - (this.lastPoll || 0) < 10000)) return;
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
  checkGenerationHealth() {
    const backend = this.choice?.backend_id;
    if (!backend) return;
    this.backendHealth ||= new Map();
    const previous = this.backendHealth.get(backend);
    if (previous && Date.now() - previous.checked < 10000) return;
    this.backendHealth.set(backend, { ...previous, checked: Date.now() });
    api(`/api/library/voice-profiles/backends/${encodeURIComponent(backend)}/health`).then((result) => {
      this.backendHealth.set(backend, { reachable: result.reachable, checked: Date.now() });
      if (!this.disposed && this.choice?.backend_id === backend && this.active()) this.render();
    }).catch(() => {});
  }
  choose(remember = true, activate = false) {
    this.pages = this.row.recordings.find((r) => r.id === this.choice?.recording_id)?.pages || this.choice?.pages || this.data?.pages || this.pages;
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
    // Browsing a different lecture or revision leaves the player in place
    // until the listener explicitly plays the displayed version.
    const different = this.player.row && (this.player.row.id !== this.row.id ||
      this.player.row.revision !== this.row.revision);
    if (different && this.player.revealed !== false && !activate) {
      this.resume ||= this.progress;
      this.target = resumeTarget(this.row, this.resume, this.pages);
      this.onChange?.();
      this.render();
      return;
    }
    const position =
      this.player.row?.id === this.row.id && this.player.row.spoken_sha256 === this.row.spoken_sha256
        ? this.player.position() : null;
    this.resume = position || this.resume || this.progress;
    if (this.player.lectureController !== this) {
      this.player.lectureController?.dispose();
      this.player.lectureController = this;
      this.onActivate?.();
    }
    this.player.open(
      this.views.get(choice?.recording_id) || this.row,
      remember ? null : this.resume,
      choice?.recording_id || false,
      this.course,
    );
    if (this.continueBlocks) {
      this.continueBlocks.checked = getStored("continue-blocks", true);
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
    this.checkGenerationHealth();
  }
  render() {
    this.jobsSignature = JSON.stringify(this.jobs);
    this.voiceOptions();
    const canGenerate = Boolean(this.data.tools_available && this.choice?.profile && this.choice.available !== false);
    const savedProfiles = this.data.schema === "voice-profiles-v1";
    this.select.setAttribute("aria-label", savedProfiles ? "Voice profile" : "Voice");
    this.more.querySelector("summary").textContent = savedProfiles ? "More profiles and recordings" : "More voices";
    this.moreSelect.setAttribute("aria-label", savedProfiles ? "All profiles and recordings" : "All voices");
    this.clearCache.textContent = savedProfiles ? "Clear this profile’s cache" : "Clear this voice’s cache";
    this.audioSummary.textContent = this.data.tools_available ? "Audio blocks & generation" : "Audio blocks";
    this.voiceLabelText.textContent = savedProfiles ? "Voice profile for playback and generation" : this.data.tools_available ? "Voice for playback and generation" : "Voice for playback";
    const generationTarget = this.choices.find(c => c.profile && c.available !== false && c.server_default) || this.choices.find(c => c.profile && c.available !== false);
    this.cache.hidden = !this.data.tools_available || !generationTarget;
    this.clearCache.hidden = this.stop.hidden = !canGenerate;
    const useChoice = key => {this.voiceOptions(key);this.select.value=key;this.choose();};
    this.generationNotice.replaceChildren();
    if (this.backendHealth?.get(this.choice?.backend_id)?.reachable === false)
      this.generationNotice.append("The speech service is unreachable. Existing audio remains playable; missing blocks cannot be generated until it returns. ");
    if (this.choice?.recording_id && (this.choice.warning || this.initialError || this.queueError))
      this.generationNotice.append((this.choice.warning || "Generation information is unavailable. Existing audio remains playable.") + " ");
    if (this.data.tools_available && !canGenerate && generationTarget) {
      this.generationNotice.append("This saved recording remains playable. Select a current voice profile to cache new audio. ",
        el("button", {type:"button", text:"Use " + generationTarget.label, onclick:()=>useChoice(generationTarget.key)}));
    } else if (canGenerate && !this.choice?.recording_id && this.row.recordings.some(r=>r.segments.length)) {
      const prepared=this.choices.find(c=>c.recording_complete)||this.choices.find(c=>c.recording_id);
      this.generationNotice.append(...["No audio is cached for this profile revision yet. Other prepared recordings are available. ",
        prepared ? el("button", {type:"button",text:"Use available recording",onclick:()=>useChoice(prepared.key)}):null].filter(Boolean));
    }
    this.generationNotice.hidden = !this.generationNotice.childNodes.length;
    this.clearCache.disabled = !canGenerate || this.submitting || this.clearing;
    this.generations.hidden = !canGenerate;
    this.generationQueueLink.hidden = !canGenerate;
    this.speechSettings.hidden = !canGenerate || savedProfiles;
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
      !canGenerate ||
      !this.data.tools_available ||
      this.submitting || this.clearing ||
      wholeLectureActive;
    this.stop.disabled =
      !["queued", "running"].includes(job?.state) || this.stopping.has(job?.id);
    this.select.disabled = !this.choices.length || this.clearing;
    this.more.hidden = this.choices.length < 2;
    this.status.textContent = this.pending
      ? `Waiting for block ${this.pending.index + 1} in ${this.choice.label}. Playback will start when it is ready.${job?.error ? " · " + job.error : ""}`
      : job
        ? `${job.state} · ${states.filter((state) => state === "ready").length}/${states.length} audio blocks ready${job.error ? " · " + job.error : ""}`
        : this.initialError ||
          (this.choice?.recording_id
            ? ""
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
    this.syncPlayback();
    this.player.syncControls?.();
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
            text: `${job.profile_revision ? "Recipe " + job.profile_revision.slice(0, 8) : (job.speed || 1) + "× speech"} · ${job.state} · ${job.requested_blocks ? (job.requested_blocks.length === 1 ? "block " + (job.requested_blocks[0] + 1) + " requested" : job.requested_blocks.length + " blocks requested") : "whole lecture"} · ${job.inventory.ready}/${job.inventory.total || "?"} blocks ready${job.revision !== this.row.revision ? " · earlier transcript revision" : ""}`,
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
                "aria-label": `Stop generation for ${label}${job.profile_revision ? "" : " at " + (job.speed || 1) + "×"}`,
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
  syncPlayback() {
    const owns = this.player.lectureController === this;
    const label = owns && this.pending ? "Cancel playback"
      : owns && !this.player.audio.paused ? "Pause"
      : (owns ? (this.player.started || this.player.resumeAvailable) : this.progress) ? "Resume" : "Play";
    if (this.playButton.textContent !== label) this.playButton.textContent = label;
  }
  togglePlayback() {
    if (this.player.lectureController === this) this.player.toggle();
    else this.play();
  }
  cancelPlayback() {
    this.pending = null;
    this.epoch++;
    this.player.audio.pause();
    this.render();
  }
  play(index = null, seconds = null) {
    if (this.player.lectureController !== this) this.choose(false, true);
    this.player.play(index ?? this.target?.index ?? this.player.index, seconds);
  }
  playPrepared(index = null, seconds = null) {
    const recording = this.player.lectureController === this ? this.player.recording
      : this.row.recordings.find(r => r.id === this.choice?.recording_id);
    const target = index ?? this.target?.index ?? (this.player.row?.id === this.row.id ? this.player.index : 0);
    if (!recording?.segments.some((segment) => segment.index === target)) {
      this.message("The next lecture has no prepared audio for the selected voice. Choose an available voice or press Play to generate it.");
      return;
    }
    this.play(target, seconds);
  }
  async require(index, seconds) {
    if (!this.choice?.profile || !this.data.tools_available || this.choice.available === false) {
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
    if (coversBlocks(this.inventory.job, blocks)) {
      this.render();
      await this.poll();
    }
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
    const prompt = choice.fixed_recipe ? `Clear cached audio for ${choice.label}, revision ${choice.profile_revision.slice(0,8)}, in this lecture? Other profiles and revisions remain available. Historical files remain for later garbage collection.` : `Clear cached audio for ${choice.voice} (${choice.profile}) in this lecture at all generation speeds? Other voices are kept. Historical media files remain available for later garbage collection. You can then generate fresh audio with the current title settings.`;
    if (!globalThis.confirm(prompt)) return;
    this.clearing = true;
    this.epoch++;
    this.pending = null;
    if (this.player.lectureController === this) this.player.audio.pause();
    this.render();
    try {
      await post("/api/library/production/clear-cache", {
        lecture_id: this.row.id, revision: this.row.revision,
        profile: choice.profile, ...(choice.fixed_recipe ? {profile_revision: choice.profile_revision} : {voice: choice.voice}),
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
        ...(choice.fixed_recipe ? {profile_revision: choice.profile_revision} : {voice: choice.voice, speed: choice.speed}),
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
    this.lastPoll = Date.now();
    this.checkGenerationHealth();
    this.polling = true;
    const epoch = this.epoch;
    try {
      const jobs = (await api(this.jobsURL())).jobs;
      if (epoch !== this.epoch || this.disposed) return;
      const signature = JSON.stringify(jobs);
      const changed = signature !== this.jobsSignature || this.queueError;
      this.jobs = jobs;
      this.queueError = null;
      if (changed) this.render();
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
      if (this.player.lectureController === this) this.player.audio.pause();
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

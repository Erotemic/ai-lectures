import { AudioBlockCache } from "./audio-cache.mjs";
import { getStored, store, clock, lectureURL } from "./api.mjs";
import {
  words,
  pageSpeechSegments,
  wordAtTime,
  timeAtWord,
  sentenceAtWord,
} from "./transcript.mjs";
export function pageDurations(recording) {
  const measured = new Map(recording.segments.map((segment) => [segment.index, segment.duration]));
  return recording.pages.map(
    (page, index) => measured.get(index) ?? (page.split(/\s+/).length / 145) * 60,
  );
}
const recordingTimelines = new WeakMap();
function timelineFor(recording) {
  if (!recordingTimelines.has(recording)) {
    const durations = pageDurations(recording);
    let total = 0;
    const starts = durations.map((duration) => {
      const start = total;
      total += duration;
      return start;
    });
    recordingTimelines.set(recording, { durations, starts, total });
  }
  return recordingTimelines.get(recording);
}
export function locateTime(durations, seconds) {
  let index = 0;
  while (index < durations.length - 1 && seconds >= durations[index])
    seconds -= durations[index++];
  return {
    index,
    seconds: Math.max(0, Math.min(seconds, durations[index] || 0)),
  };
}
export class Player {
  constructor({ checkpoint, message, next }) {
    this.audio = document.getElementById("audio");
    this.checkpoint = checkpoint;
    this.message = message;
    this.next = next;
    this.row = null;
    this.recording = null;
    this.ready = false;
    this.started = false;
    this.revealed = false;
    this.index = 0;
    this.lastSave = 0;
    this.loadToken = 0;
    this.blockCache = new AudioBlockCache();
    document.getElementById("toggle-play").onclick = () => this.toggle();
    const speed = document.getElementById("playback-rate");
    const applySpeed = (value) => {
      speed.value = String(value);
      if (!speed.value) speed.value = "1";
      const rate = Number(speed.value);
      this.audio.defaultPlaybackRate = rate;
      this.audio.playbackRate = rate;
      return rate;
    };
    applySpeed(getStored("rate", 1));
    speed.onchange = () => store("rate", applySpeed(speed.value));
    this.audio.onplay = () => {
      this.started = true;
      this.reveal();
      this.syncControls();
      this.onBlockPlay?.(this.index);
    };
    this.audio.onpause = () => {
      this.syncControls();
      this.save();
    };
    this.audio.ontimeupdate = () => {
      this.update();
      if (Date.now() - this.lastSave > 10000) this.save();
    };
    this.audio.onerror = () =>
      message(
        "This recording could not be loaded. Its saved position has been retained.",
      );
    this.audio.onwaiting = () => {
      if (this.started) document.getElementById("playing-note").textContent = "Buffering audio… your position is retained";
    };
    this.audio.onplaying = () => {
      document.getElementById("playing-note").textContent = this.recording?.label || this.recording?.variant || "";
      if (this.recording) this.blockCache.prefetch(this.recording,this.index);
    };
    this.audio.onended = () => {
      this.save(this.index === this.recording.pages.length - 1);
      if (this.index < this.recording.pages.length - 1) {
        if (this.continueBlocks && !this.continueBlocks()) return;
        this.play(this.index + 1, 0);
      } else if (document.getElementById("continue-course").checked) this.next({ automatic: true });
    };
    const timeline = document.getElementById("timeline");
    const preview = () => (Number(timeline.value) / 10000) * timelineFor(this.recording).total;
    timeline.oninput = () => {
      if (!this.recording) return;
      this.scrubbing = true;
      this.showElapsed(preview());
    };
    timeline.onchange = () => {
      this.scrubbing = false;
      if (this.recording) this.seekTo(preview());
    };
    timeline.onpointercancel = timeline.onblur = () => {
      this.scrubbing = false;
      this.update();
    };
    window.addEventListener("pagehide", () => this.save());
  }
  reveal() {
    this.revealed = true;
    document.getElementById("player").hidden = false;
  }
  syncControls() {
    const waiting = Boolean(this.lectureController?.pending);
    const control = document.getElementById("toggle-play");
    const label = waiting
      ? "Cancel playback" : this.audio.paused ? (this.started || this.resumeAvailable ? "Resume" : "Play") : "Pause";
    if (control.textContent !== label) control.textContent = label;
    this.lectureController?.syncPlayback?.();
  }
  toggle() {
    if (!this.row) return;
    if (this.lectureController?.pending) {
      this.lectureController.cancelPlayback();
    } else if (this.audio.paused) this.play(this.index, this.audio.currentTime);
    else this.audio.pause();
  }
  open(row, progress = null, preferred = null, course = this.course ?? null) {
    if (
      this.row?.id === row.id &&
      this.row.revision === row.revision &&
      JSON.stringify(this.row.recordings.map((r) => r.id)) ===
        JSON.stringify(row.recordings.map((r) => r.id)) &&
      (preferred === null || preferred === this.recording?.id)
    ) {
      if (this.course !== course) {
        this.save();
        this.course = course;
      }
      return;
    }
    this.save();
    this.ready = false;
    this.started = false;
    this.resumeAvailable = Boolean(progress && !progress.completed && progress.spoken_sha256 === row.spoken_sha256);
    this.audio.pause();
    this.loadToken++;
    this.audio.onloadedmetadata = null;
    this.audio.removeAttribute("src");
    this.audio.load();
    this.row = row;
    this.course = course;
    this.blockCache.close();
    this.recording =
      preferred === false
        ? null
        : row.recordings.find((r) => r.id === preferred) ||
          row.recordings.find((r) => r.variant === getStored("variant")) ||
          row.recordings.find((r) => r.complete) ||
          row.recordings[0] ||
          null;
    this.index = 0;
    this.scrubbing = false;
    document.getElementById("playing-title").textContent = row.title;
    document.getElementById("playing-title").href = lectureURL(row.id);
    if (this.recording) {
      let seconds = 0;
      if (progress?.spoken_sha256 === row.spoken_sha256) {
        if (progress.recording_id === this.recording.id) {
          this.index = progress.segment || 0;
          seconds = progress.seconds || 0;
        } else if (Number.isFinite(progress.anchor_word)) {
          let words = progress.anchor_word;
          for (let i = 0; i < this.recording.pages.length; i++) {
            const count = this.recording.pages[i].split(/\s+/).length;
            if (words < count) {
              this.index = i;
              seconds = timeAtWord(
                this.recording.pages[i],
                this.recording.segments.find((s) => s.index === i),
                words,
              );
              break;
            }
            words -= count;
          }
          this.message("Resume position is approximate for this narrator.");
        }
      } else if (progress && !progress.legacy)
        this.message(
          "This lecture has been revised. Your previous listening history is retained; this version starts at the beginning.",
        );
      this.load(this.index, seconds, false);
    } else {
      document.getElementById("playing-note").textContent =
        "Selected voice has no prepared recording";
      document.getElementById("elapsed").textContent = "0:00";
      document.getElementById("duration").textContent = "—";
      document.getElementById("timeline").value = "0";
    }
    this.update();
  }
  load(index, seconds = 0, autoplay = false) {
    const segment = this.recording?.segments.find((s) => s.index === index);
    if (!segment) {
      this.save();
      this.ready = false;
      this.audio.pause();
      this.index = index;
      this.loadToken++;
      this.audio.onloadedmetadata = null;
      this.audio.removeAttribute("src");
      this.audio.load();
      this.index = index;
      document.getElementById("playing-note").textContent =
        "This passage has not been generated for the selected voice";
      return;
    }
    this.save();
    this.ready = false;
    this.audio.pause();
    this.index = index;
    const token = ++this.loadToken;
    this.audio.onloadedmetadata = () => {
      if (token !== this.loadToken) return;
      this.ready = true;
      this.audio.playbackRate = this.audio.defaultPlaybackRate;
      this.audio.currentTime = Math.min(
        seconds,
        Math.max(0, this.audio.duration - 0.05),
      );
      if (autoplay) this.audio.play().catch((e) => this.playbackError(e));
      this.update();
    };
    const use = (url) => {
      if (token !== this.loadToken) return;
      this.audio.src = url || segment.url;
      this.audio.load();
    };
    const pending = this.blockCache.pending(segment.url);
    if (pending && !this.blockCache.cached(segment.url)) {
      this.audio.removeAttribute("src");
      this.audio.load();
      document.getElementById("playing-note").textContent = "Buffering next audio block…";
      pending.then(use);
    } else use(this.blockCache.cached(segment.url));
    document.getElementById("playing-note").textContent =
      this.recording.label || this.recording.variant;
    // Surface advisory metadata without delaying media loading or requiring TTS.
    if (globalThis.window?.fetch && segment.url?.startsWith("/api/library/"))
      window.fetch(segment.url, { method: "HEAD", cache: "no-store" }).then((response) => {
        const warning = response.headers.get("X-Playback-Warning");
        if (token === this.loadToken && warning) this.message(warning);
      }).catch(() => {});
    this.update();
  }
  seekSentence(index, sentence) {
    const text = this.recording.pages[index];
    const before = pageSpeechSegments(this.row, this.recording, index)
      .slice(0, sentence)
      .reduce((sum, part) => sum + words(part), 0);
    const segment = this.recording.segments.find((s) => s.index === index);
    this.play(index, timeAtWord(text, segment, before));
  }
  seekBy(seconds) {
    if (!this.recording) return;
    const { starts } = timelineFor(this.recording);
    const elapsed = (starts[this.index] || 0) +
      (this.audio.currentTime || 0);
    this.seekTo(elapsed + seconds);
  }
  seekTo(seconds) {
    if (!this.recording) return;
    const target = locateTime(timelineFor(this.recording).durations, Math.max(0, seconds));
    if (target.index === this.index && this.ready) {
      this.audio.currentTime = Math.min(target.seconds, this.audio.duration);
      this.update();
      return;
    }
    if (this.audio.paused) this.load(target.index, target.seconds, false);
    else this.play(target.index, target.seconds);
  }
  play(index = this.index, seconds = null) {
    if (this.row) this.reveal();
    if (
      !this.recording?.segments.some((s) => s.index === index) &&
      this.requestMissing
    ) {
      this.audio.pause();
      return this.requestMissing(index, seconds);
    }
    if (!this.recording)
      return this.message(
        "No recording is installed. The full transcript is available.",
      );
    this.started = true;
    if (index === this.index && this.audio.getAttribute("src")) {
      if (seconds !== null) this.audio.currentTime = seconds;
      this.audio.play().catch((e) => this.playbackError(e));
    } else this.load(index, seconds || 0, true);
  }
  showElapsed(seconds) {
    const label = document.getElementById("elapsed");
    const value = clock(seconds);
    if (label.textContent !== value) label.textContent = value;
  }
  updateTimeline(elapsed, total) {
    const value = total ? Math.max(0, Math.min(10000, Math.round((elapsed / total) * 10000))) : 0;
    document.getElementById("timeline").value = String(value);
    if (this.displayedTime !== value) {
      document.getElementById("player").style?.setProperty("--playback-progress", `${value / 100}%`);
      this.displayedTime = value;
    }
  }
  update() {
    this.syncControls();
    if (!this.recording) {
      this.updateTimeline(0, 0);
      return;
    }
    const { starts, total } = timelineFor(this.recording);
    const elapsed = (starts[this.index] || 0) + (this.audio.currentTime || 0);
    const duration = document.getElementById("duration");
    const durationText = (!this.recording.complete ? "~ " : "") + clock(total);
    if (duration.textContent !== durationText) duration.textContent = durationText;
    if (!this.scrubbing) {
      this.showElapsed(elapsed);
      this.updateTimeline(elapsed, total);
    }
    const root = document.querySelector(".transcript[data-recording]");
    if (
      root?.dataset.recording === this.recording.id &&
      root.dataset.lecture === this.row.id
    ) {
      const { index } = this;
      if (this.activePassage?.parentElement !== root || this.highlightIndex !== index) {
        this.activePassage?.classList.remove("active");
        this.activePassage = root.querySelector(`.passage[data-index="${index}"]`);
        this.activePassage?.classList.add("active");
        this.highlightIndex = index;
        this.highlightSegments = pageSpeechSegments(this.row, this.recording, index);
      }
      if (!this.activePassage) return;
      const segment = this.recording.segments.find((s) => s.index === index);
      const active = sentenceAtWord(
        this.highlightSegments,
        wordAtTime(this.recording.pages[index], segment, this.audio.currentTime || 0),
      );
      if (this.activeSentence?.parentElement?.closest(".passage") === this.activePassage &&
          Number(this.activeSentence.dataset.sentence) === active) return;
      this.activeSentence?.classList.remove("active");
      this.activeSentence?.removeAttribute("aria-current");
      this.activeSentence = this.activePassage.querySelector(`.speech-segment[data-sentence="${active}"]`);
      this.activeSentence?.classList.add("active");
      this.activeSentence?.setAttribute("aria-current", "true");
    }
  }
  playbackError(error) {
    // Pausing or changing sources can cancel an outstanding play request.
    if (error.name === "NotAllowedError") this.message("Tap Play in the player to continue listening.");
    else if (error.name !== "AbortError") this.message(error.message);
  }
  position(completed = false) {
    if (!this.row || !this.recording) return null;
    const segment = this.recording.segments.find((s) => s.index === this.index);
    const precedingWords = this.recording.pages
      .slice(0, this.index)
      .join(" ")
      .split(/\s+/)
      .filter(Boolean).length;
    return {
      lecture_id: this.row.id,
      revision: this.row.revision,
      release: this.row.origin.release,
      spoken_sha256: this.row.spoken_sha256,
      course_id: this.course,
      recording_id: this.recording.id,
      segment: this.index,
      seconds: this.audio.currentTime || 0,
      completed,
      anchor_word:
        precedingWords +
        wordAtTime(
          this.recording.pages[this.index],
          segment,
          this.audio.currentTime || 0,
        ),
    };
  }
  save(completed = false) {
    const position = this.position(completed);
    if (
      position &&
      this.started &&
      this.ready &&
      this.audio.getAttribute("src")
    ) {
      this.lastSave = Date.now();
      this.checkpoint(position);
    }
  }
}

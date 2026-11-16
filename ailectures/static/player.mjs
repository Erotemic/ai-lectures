import { getStored, store, clock, lectureURL } from "./api.mjs";
import {
  words,
  speechSegments,
  wordAtTime,
  timeAtWord,
  sentenceAtWord,
} from "./transcript.mjs";
export function pageDurations(recording) {
  return recording.pages.map(
    (page, index) =>
      recording.segments.find((s) => s.index === index)?.duration ??
      (page.split(/\s+/).length / 145) * 60,
  );
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
    this.index = 0;
    this.lastSave = 0;
    this.loadToken = 0;
    document.getElementById("toggle-play").onclick = () => {
      if (!this.row) return;
      this.audio.paused
        ? this.play(this.index, this.audio.currentTime)
        : this.audio.pause();
    };
    const speed = document.getElementById("playback-rate");
    speed.value = String(getStored("rate", 1));
    speed.onchange = () => {
      this.audio.playbackRate = Number(speed.value);
      store("rate", Number(speed.value));
    };
    this.audio.onplay = () => {
      this.started = true;
      document.getElementById("toggle-play").textContent = "Pause";
    };
    this.audio.onpause = () => {
      document.getElementById("toggle-play").textContent = "Play";
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
    this.audio.onended = () => {
      this.save(this.index === this.recording.pages.length - 1);
      if (this.index < this.recording.pages.length - 1)
        this.play(this.index + 1, 0);
      else if (document.getElementById("continue-course").checked) this.next();
    };
    document.getElementById("timeline").onchange = (event) => {
      if (!this.recording) return;
      const d = pageDurations(this.recording);
      const p = locateTime(
        d,
        (Number(event.target.value) / 10000) * d.reduce((a, b) => a + b, 0),
      );
      this.play(p.index, p.seconds);
    };
    window.addEventListener("pagehide", () => this.save());
  }
  open(row, progress = null, preferred = null) {
    if (
      this.row?.id === row.id &&
      this.row.revision === row.revision &&
      JSON.stringify(this.row.recordings.map((r) => r.id)) ===
        JSON.stringify(row.recordings.map((r) => r.id)) &&
      (preferred === null || preferred === this.recording?.id)
    )
      return;
    this.save();
    this.ready = false;
    this.started = false;
    this.audio.pause();
    this.loadToken++;
    this.audio.onloadedmetadata = null;
    this.audio.removeAttribute("src");
    this.audio.load();
    this.row = row;
    this.recording =
      preferred === false
        ? null
        : row.recordings.find((r) => r.id === preferred) ||
          row.recordings.find((r) => r.variant === getStored("variant")) ||
          row.recordings.find((r) => r.complete) ||
          row.recordings[0] ||
          null;
    this.index = 0;
    document.getElementById("player").hidden = false;
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
      this.audio.playbackRate = Number(
        document.getElementById("playback-rate").value,
      );
      this.audio.currentTime = Math.min(
        seconds,
        Math.max(0, this.audio.duration - 0.05),
      );
      if (autoplay) this.audio.play().catch((e) => this.playbackError(e));
      this.update();
    };
    this.audio.src = segment.url;
    this.audio.load();
    document.getElementById("playing-note").textContent =
      this.recording.label || this.recording.variant;
    this.update();
  }
  seekSentence(index, sentence) {
    const text = this.recording.pages[index];
    const before = speechSegments(text)
      .slice(0, sentence)
      .reduce((sum, part) => sum + words(part), 0);
    const segment = this.recording.segments.find((s) => s.index === index);
    this.play(index, timeAtWord(text, segment, before));
  }
  play(index = this.index, seconds = null) {
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
  update() {
    if (!this.recording) return;
    const durations = pageDurations(this.recording);
    const elapsed =
      durations.slice(0, this.index).reduce((a, b) => a + b, 0) +
      (this.audio.currentTime || 0);
    const total = durations.reduce((a, b) => a + b, 0);
    document.getElementById("elapsed").textContent = clock(elapsed);
    document.getElementById("duration").textContent =
      (!this.recording.complete ? "~ " : "") + clock(total);
    document.getElementById("timeline").value = String(
      total ? (elapsed / total) * 10000 : 0,
    );
    const root = document.querySelector(".transcript[data-recording]");
    if (
      root?.dataset.recording === this.recording.id &&
      root.dataset.lecture === this.row.id
    ) {
      const segment = this.recording.segments.find(
        (s) => s.index === this.index,
      );
      const active = sentenceAtWord(
        speechSegments(this.recording.pages[this.index]),
        wordAtTime(
          this.recording.pages[this.index],
          segment,
          this.audio.currentTime || 0,
        ),
      );
      for (const passage of root.querySelectorAll(".passage")) {
        const current = Number(passage.dataset.index) === this.index;
        passage.classList.toggle("active", current);
        for (const sentence of passage.querySelectorAll(".speech-segment")) {
          const selected =
            current && Number(sentence.dataset.sentence) === active;
          sentence.classList.toggle("active", selected);
          if (selected) sentence.setAttribute("aria-current", "true");
          else sentence.removeAttribute("aria-current");
        }
      }
    }
  }
  playbackError(error) {
    // Pausing or changing sources can cancel an outstanding play request.
    if (error.name !== "AbortError") this.message(error.message);
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

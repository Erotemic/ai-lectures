import { el } from "./api.mjs";

export function signalLevel(samples) {
  let energy = 0, peak = 0;
  for (const sample of samples) {
    energy += sample * sample;
    peak = Math.max(peak, Math.abs(sample));
  }
  const rms = samples.length ? Math.sqrt(energy / samples.length) : 0;
  return { rms, peak, db: Math.max(-60, Math.min(0, 20 * Math.log10(rms || 1e-6))) };
}

export class InputLevelTracker {
  constructor() { this.quietSince = null; this.clipUntil = -1; this.goodUntil = -1; }
  update(level, now) {
    if (level.peak >= 0.98) this.clipUntil = now + 1000;
    if (level.db < -38) this.quietSince ??= now;
    else { this.quietSince = null; this.goodUntil = now + 1000; }
    if (now < this.clipUntil) return "clipping";
    if (level.db > -10) return "loud";
    if (this.quietSince !== null && now - this.quietSince >= 2000)
      return level.db <= -55 ? "silent" : "quiet";
    return level.db < -38 && now >= this.goodUntil ? "listening" : "good";
  }
}

const guidance = {
  listening: "Listening. Read the prompt aloud.",
  good: "Good level. Keep this distance.",
  quiet: "Very quiet. Move closer or raise mic input.",
  silent: "No sound detected. Speak or check mic input.",
  loud: "Loud input. Move a little farther away.",
  clipping: "Clipping. Move back or lower mic input.",
};

export function microphoneMeter() {
  const segments = Array.from({ length: 24 }, () => el("span", { "aria-hidden": "true" }));
  const value = el("span", { class: "microphone-level-value", "aria-hidden": "true", text: "— dB" });
  const bar = el("div", { class: "microphone-level-bar", role: "meter", "aria-label": "Microphone input level",
    "aria-valuemin": "-60", "aria-valuemax": "0", "aria-valuenow": "-60" }, ...segments);
  const advice = el("p", { class: "microphone-level-advice", role: "status", "aria-live": "polite", text: guidance.listening });
  const resume = el("button", { type: "button", text: "Enable level meter", hidden: true });
  const element = el("div", { class: "microphone-level", hidden: true },
    el("div", { class: "microphone-level-heading" }, el("span", { text: "Mic input" }), value), bar,
    el("div", { class: "microphone-level-scale", "aria-hidden": "true" },
      el("span", { text: "Quiet" }), el("span", { text: "Good" }), el("span", { text: "Too loud" })), advice, resume);
  let context, source, analyser, frame, epoch = 0, disposed = false;

  function disconnect() {
    if (frame !== undefined) cancelAnimationFrame(frame);
    frame = undefined;
    try { source?.disconnect(); analyser?.disconnect(); } catch {}
    if (context) {
      context.onstatechange = null;
      try { context.close()?.catch(() => {}); } catch {}
    }
    context = source = analyser = null;
  }
  function stop() { epoch++; disconnect(); element.hidden = true; }
  function start(stream) {
    stop();
    if (disposed) return;
    const run = epoch;
    element.hidden = false; resume.hidden = true;
    advice.textContent = guidance.listening;
    element.setAttribute("data-level", "listening");
    value.textContent = "— dB";
    for (const segment of segments) segment.setAttribute("data-lit", "false");
    bar.setAttribute("aria-valuenow", "-60");
    const unavailable = () => {
      if (run !== epoch) return;
      disconnect(); resume.hidden = true;
      advice.textContent = "Live level meter unavailable. You can still record and listen back to your take.";
      element.setAttribute("data-level", "unavailable");
    };
    try {
      const AudioContext = globalThis.AudioContext || globalThis.webkitAudioContext;
      if (!AudioContext) { unavailable(); return; }
      context = new AudioContext();
      analyser = context.createAnalyser(); analyser.fftSize = 2048;
      source = context.createMediaStreamSource(stream);
      // This branch only measures input. Never connect the mic to the speakers.
      source.connect(analyser);
      const samples = new Float32Array(analyser.fftSize), tracker = new InputLevelTracker();
      let lastPaint = -Infinity, lastAdvice = "listening", drawing = false;
      const draw = (now) => {
        if (run !== epoch) return;
        analyser.getFloatTimeDomainData(samples);
        const level = signalLevel(samples), state = tracker.update(level, now);
        if (now - lastPaint >= 80) {
          lastPaint = now;
          const lit = Math.ceil((level.db + 60) / 60 * segments.length);
          segments.forEach((segment, index) => segment.setAttribute("data-lit", String(index < lit)));
          value.textContent = level.db <= -60 ? "< −60 dB" : `${Math.round(level.db)} dB`;
          bar.setAttribute("aria-valuenow", String(Math.round(level.db)));
          bar.setAttribute("aria-valuetext", `${Math.round(level.db)} decibels. ${guidance[state]}`);
          element.setAttribute("data-level", state);
          if (state !== lastAdvice) { advice.textContent = guidance[state]; lastAdvice = state; }
        }
        frame = requestAnimationFrame(draw);
      };
      const activated = () => {
        if (run !== epoch || !context || context.state !== "running" || drawing) return;
        drawing = true; resume.hidden = true;
        advice.textContent = guidance.listening;
        frame = requestAnimationFrame(draw);
      };
      context.onstatechange = activated;
      resume.onclick = () => {
        if (run !== epoch || !context) return;
        context.resume().then(activated).catch(unavailable);
      };
      context.resume().then(activated).catch(unavailable);
      activated();
      if (!drawing) {
        resume.hidden = false;
        advice.textContent = "Recording is active. Enable the level meter to see your microphone input.";
      }
    } catch { unavailable(); }
  }
  return { element, start, stop, dispose() { stop(); disposed = true; } };
}

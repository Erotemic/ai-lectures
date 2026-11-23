import assert from "node:assert/strict";
import { test } from "node:test";
import { signalLevel, InputLevelTracker, microphoneMeter } from "../ailectures/static/microphone-meter.mjs";

test("sample levels measure real RMS, peak, silence, and full scale", () => {
  assert.deepEqual(signalLevel([]), { rms: 0, peak: 0, db: -60 });
  assert.deepEqual(signalLevel(new Float32Array(16)), { rms: 0, peak: 0, db: -60 });
  const level = signalLevel([0.1, -0.1, 0.1, -0.1]);
  assert.equal(level.peak, 0.1);
  assert(Math.abs(level.db + 20) < 1e-10);
  const pulse = signalLevel([0, 0, 1, 0]);
  assert.equal(pulse.peak, 1);
  assert.equal(pulse.rms, 0.5);
  assert.equal(signalLevel([1, -1]).db, 0);
});

test("quiet feedback waits through pauses and clipping stays visible after a short peak", () => {
  const tracker = new InputLevelTracker();
  const silence = signalLevel([0]), quiet = signalLevel([0.004]), good = signalLevel([0.1]);
  assert.equal(tracker.update(silence, 0), "listening");
  assert.equal(tracker.update(silence, 1500), "listening");
  assert.equal(tracker.update(silence, 2100), "silent");
  assert.equal(tracker.update(good, 2200), "good");
  assert.equal(tracker.update(silence, 2400), "good", "Short speech gaps retain the good-level state");
  assert.equal(tracker.update(quiet, 4500), "quiet");
  assert.equal(tracker.update({ db: -20, peak: 0.99 }, 4600), "clipping");
  assert.equal(tracker.update(good, 5200), "clipping");
  assert.equal(tracker.update(good, 5700), "good");
  assert.equal(tracker.update(signalLevel([0.5]), 5800), "loud");
});

class Element {
  constructor(tag) { this.tag = tag; this.children = []; this.hidden = false; }
  append(...children) { this.children.push(...children); }
  setAttribute(key, value) { this[key] = key === "hidden" ? true : value; }
  addEventListener() {}
}
const find = (root, predicate) => predicate(root) ? root : root.children?.map((child) => typeof child === "object" && find(child, predicate)).find(Boolean);

function setup({ suspended = false, fail = false } = {}) {
  globalThis.document = { createElement: (tag) => new Element(tag) };
  const frames = new Map(), contexts = [];
  let nextFrame = 0;
  globalThis.requestAnimationFrame = (callback) => { frames.set(++nextFrame, callback); return nextFrame; };
  globalThis.cancelAnimationFrame = (id) => frames.delete(id);
  globalThis.AudioContext = class {
    constructor() { if (fail) throw Error("unavailable"); this.state = suspended ? "suspended" : "running"; this.connections = []; this.closed = false; contexts.push(this); }
    createAnalyser() { this.analyser = { fftSize: 0, disconnect() {}, getFloatTimeDomainData: (samples) => samples.fill(0.1) }; return this.analyser; }
    createMediaStreamSource(stream) { this.stream = stream; this.source = { connect: (node) => this.connections.push(node), disconnect() { this.disconnected = true; } }; return this.source; }
    resume() { return Promise.resolve(); }
    close() { this.closed = true; this.state = "closed"; return Promise.resolve(); }
  };
  const meter = microphoneMeter();
  return { meter, frames, contexts, draw(now) {
    const [id, callback] = frames.entries().next().value;
    frames.delete(id); callback(now);
  } };
}

test("meter reads microphone samples without speaker monitoring and releases its graph on stop", async () => {
  const { meter, frames, contexts, draw } = setup();
  const stream = {};
  meter.start(stream); await Promise.resolve(); draw(0);
  const context = contexts[0];
  assert.equal(context.stream, stream);
  assert.deepEqual(context.connections, [context.analyser]);
  assert.equal(find(meter.element, (node) => node.role === "meter")["aria-valuenow"], "-20");
  assert.equal(meter.element["data-level"], "good");
  meter.stop();
  assert.equal(frames.size, 0);
  assert.equal(context.closed, true);
  assert.equal(context.source.disconnected, true);
  assert.equal(meter.element.hidden, true);
  meter.start(stream); assert.equal(contexts.length, 2);
  meter.dispose(); assert.equal(contexts[1].closed, true); assert.equal(frames.size, 0);
  meter.start(stream); assert.equal(contexts.length, 2);
});

test("suspended meters can be activated by a user gesture, and late resume cannot restart stopped analysis", async () => {
  const { meter, contexts, frames } = setup({ suspended: true });
  meter.start({}); await Promise.resolve();
  const context = contexts[0], resume = find(meter.element, (node) => node.tag === "button");
  assert.equal(resume.hidden, false);
  context.state = "running";
  resume.onclick(); await Promise.resolve();
  assert.equal(resume.hidden, true);
  assert.equal(frames.size, 1);
  meter.stop(); await Promise.resolve();
  assert.equal(frames.size, 0);
  resume.onclick(); await Promise.resolve();
  assert.equal(frames.size, 0);
});

test("analysis failure leaves recording usable without fabricating a good input level", () => {
  const { meter, frames } = setup({ fail: true });
  meter.start({});
  assert.equal(meter.element["data-level"], "unavailable");
  assert.equal(frames.size, 0);
  assert.equal(meter.element.hidden, false);
  meter.dispose();
});

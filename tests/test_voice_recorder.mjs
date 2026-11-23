import assert from "node:assert/strict";
import { test } from "node:test";
import { voiceReferenceRecorder } from "../ailectures/static/voice-reference-recorder.mjs";

class Element {
  constructor(tag) { this.tag = tag; this.children = []; this.value = ""; this.hidden = false; this.isConnected = true; this.events = {}; this.style = {}; }
  append(...children) { this.children.push(...children); }
  setAttribute(key, value) { this[key] = value === "" ? true : value; }
  removeAttribute(key) { delete this[key]; }
  addEventListener(name, handler) { this.events[name] = handler; }
  pause() {}
  focus() {}
  scrollIntoView() {}
}
const find = (root, predicate) => predicate(root) ? root : root.children?.map((child) => typeof child === "object" && find(child, predicate)).find(Boolean);
const tick = () => new Promise((resolve) => setImmediate(resolve));

function setup(getMedia, { secure = true } = {}) {
  globalThis.document = { createElement: (tag) => new Element(tag), body: new Element("body") };
  globalThis.window = new EventTarget();
  globalThis.MutationObserver = class { constructor(callback) { this.callback = callback; } observe() {} disconnect() {} };
  globalThis.isSecureContext = secure;
  Object.defineProperty(globalThis, "navigator", { configurable: true, value: { mediaDevices: { getUserMedia: getMedia } } });
  globalThis.MediaRecorder = class {
    static isTypeSupported() { return true; }
    constructor(stream, options) { this.mimeType = options.mimeType; this.state = "inactive"; }
    start() { this.state = "recording"; }
    stop() {
      this.state = "inactive";
      queueMicrotask(() => {
        this.ondataavailable({ data: new Blob(["synthetic recording"]) });
        this.onstop();
      });
    }
  };
  globalThis.FileReader = class {
    async readAsDataURL(blob) {
      this.result = "data:" + blob.type + ";base64," + Buffer.from(await blob.arrayBuffer()).toString("base64");
      this.onload();
    }
  };
  const saved = [], busy = [];
  const controller = voiceReferenceRecorder({
    capability: { prompt: "A synthetic prompt for a reference recording.", min_seconds: 3, max_seconds: 45, max_bytes: 4096 },
    player: { audio: { pause() {} } }, onBusy: (value) => busy.push(value),
    save: async (payload) => { saved.push(payload); return { backend_visible: true }; },
  });
  const root = controller.element;
  const name = find(root, (node) => node["aria-label"] === "Reference name");
  name.value = "Synthetic voice";
  const buttons = [];
  (function collect(node) { if (node.tag === "button") buttons.push(node); for (const child of node.children || []) if (typeof child === "object") collect(child); })(root);
  return { ...controller, root, saved, busy, record: buttons[0], stop: buttons[1], submit: buttons[2],
    prompt: find(root, (node) => node.tag === "textarea") };
}

const input = () => {
  const track = { readyState: "live", stop() { this.readyState = "ended"; } };
  return { track, stream: { getTracks: () => [track] } };
};

test("reviewed takes save their matching prompt and release the microphone", async () => {
  const media = input();
  const ui = setup(async () => media.stream);
  try {
    await ui.record.onclick();
    assert.equal(ui.submit.disabled, true);
    assert.equal(ui.prompt.readOnly, true);
    ui.stop.onclick();
    await tick();
    assert.equal(media.track.readyState, "ended");
    assert.equal(ui.submit.disabled, false);
    await ui.submit.onclick();
    assert.equal(ui.saved.length, 1);
    assert.equal(ui.saved[0].transcript, ui.prompt.value);
    assert.equal(Buffer.from(ui.saved[0].audio_base64, "base64").toString(), "synthetic recording");
    assert.equal(ui.submit.disabled, true);
    assert.equal(ui.busy.at(-1), false);
  } finally { ui.dispose(); }
});

test("changing the prompt discards a previous take instead of pairing it with new words", async () => {
  const media = input(), ui = setup(async () => media.stream);
  try {
    await ui.record.onclick(); ui.stop.onclick(); await tick();
    ui.prompt.value = "Different words require a different matching take.";
    ui.prompt.oninput();
    assert.equal(ui.submit.disabled, true);
    await ui.submit.onclick();
    assert.deepEqual(ui.saved, []);
  } finally { ui.dispose(); }
});

test("closing during a pending microphone permission stops tracks if permission later resolves", async () => {
  let allow;
  const media = input(), ui = setup(() => new Promise((resolve) => { allow = resolve; }));
  const opening = ui.record.onclick();
  ui.dispose();
  allow(media.stream);
  await opening;
  assert.equal(media.track.readyState, "ended");
  assert.deepEqual(ui.saved, []);
});

test("closing during recording stops tracks and never uploads the discarded take", async () => {
  const media = input(), ui = setup(async () => media.stream);
  await ui.record.onclick(); ui.dispose(); await tick();
  assert.equal(media.track.readyState, "ended");
  assert.deepEqual(ui.saved, []);
});

test("denied microphone permission leaves recording and upload controls usable", async () => {
  const ui = setup(async () => { throw Object.assign(Error("denied"), { name: "NotAllowedError" }); });
  try {
    await ui.record.onclick();
    assert.equal(ui.record.disabled, false);
    assert.equal(ui.prompt.readOnly, false);
    assert.equal(ui.submit.disabled, true);
    assert.equal(ui.busy.at(-1), false);
  } finally { ui.dispose(); }
});

test("an uploaded take remains usable on plain HTTP without requesting microphone access", async () => {
  const ui = setup(async () => { assert.fail("insecure page must not request microphone access"); }, { secure: false });
  try {
    assert.equal(ui.record.disabled, true);
    const upload = find(ui.root, (node) => node.type === "file");
    upload.files = [Object.assign(new Blob(["synthetic upload"]), { name: "sample.wav" })];
    upload.onchange();
    assert.equal(ui.submit.disabled, false);
    await ui.submit.onclick();
    assert.equal(ui.saved[0].media_type, "audio/wav");
    assert.equal(Buffer.from(ui.saved[0].audio_base64, "base64").toString(), "synthetic upload");
    assert.equal(ui.record.disabled, true);
  } finally { ui.dispose(); }
});

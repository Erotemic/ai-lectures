import assert from "node:assert/strict";
import { test } from "node:test";
import { voicePlayground } from "../ailectures/static/voice-playground.mjs";

class Element {
  constructor(tag) { this.tag = tag; this.children = []; this.value = ""; this.isConnected = true; this.disabled = false; this.pauses = 0; }
  append(...children) { for (const child of children) if (typeof child === "object") child.parent = this; this.children.push(...children); }
  prepend(child) { child.parent = this; this.children.unshift(child); }
  replaceChildren(...children) { this.children = []; this.append(...children); }
  setAttribute(key, value) { this[key] = value; }
  addEventListener() {}
  querySelectorAll(tag) { return this.children.flatMap((child) => typeof child === "object" ? [...(child.tag === tag ? [child] : []), ...child.querySelectorAll(tag)] : []); }
  querySelector(tag) { return this.querySelectorAll(tag)[0]; }
  get lastElementChild() { return this.children.at(-1); }
  remove() { this.parent.children = this.parent.children.filter((node) => node !== this); }
  pause() { this.pauses++; }
  focus() {}
}
const tick = () => new Promise((resolve) => setImmediate(resolve));
const response = (data) => ({ ok: true, json: async () => data });
const voices = (names) => ({ voices: names.map((voice) => ({ voice, label: voice })) });
const catalog = () => ({ default_profile: "one", tools_available: true, profiles: [
  { id: "one", backend_id: "backend-one", available: true, voice: "alpha", label: "First", model: "test" },
  { id: "two", backend_id: "backend-two", available: true, voice: "gamma", label: "Second", model: "test" },
] });

function setup(send, playbackOnly = () => false) {
  globalThis.document = { createElement: (tag) => new Element(tag), body: new Element("body") };
  globalThis.MutationObserver = class { observe() {} disconnect() {} };
  const requests = [], changes = [], textChanges = [], player = { audio: new Element("audio") };
  globalThis.fetch = async (url, options) => {
    const payload = options.body ? JSON.parse(options.body) : null;
    requests.push({ url, payload });
    return send(url, payload);
  };
  const data = catalog();
  const ui = voicePlayground({ catalog: data, playbackOnly, player, text: "A custom passage remains the same across voices.",
    onText: (text) => textChanges.push(text), onProfile: (id) => changes.push(id) });
  const selects = ui.element.querySelectorAll("select"), buttons = ui.element.querySelectorAll("button");
  return { ...ui, data, player, requests, changes, textChanges,
    profile: selects[0], voice: selects[1], input: ui.element.querySelector("textarea"), generate: buttons[0], refresh: buttons[1] };
}

test("different voices preview the same custom text and retain comparison audio without saving profiles", async () => {
  const ui = setup(async (url) => response(url.endsWith("/preview") ? { url: "/audio/" + Math.random() } : voices(["alpha", "beta"])));
  const before = structuredClone(ui.data);
  try {
    await tick();
    ui.input.value = "The user chooses the words to hear."; ui.input.oninput();
    await ui.generate.onclick();
    ui.voice.value = "beta";
    await ui.generate.onclick();
    const previews = ui.requests.filter((r) => r.url.endsWith("/preview"));
    assert.deepEqual(previews.map((r) => [r.payload.text, r.payload.voice, r.payload.duplicate_of]), [
      [ui.input.value, "alpha", "one"], [ui.input.value, "beta", "one"],
    ]);
    assert.equal(ui.requests.some((r) => r.url.endsWith("/save")), false);
    assert.deepEqual(ui.data, before);
    const audio = ui.element.querySelectorAll("audio");
    assert.equal(audio.length, 2);
    audio[0].onplay();
    assert.equal(audio[1].pauses, 1);
    assert.equal(ui.player.audio.pauses, 1);
    assert.deepEqual(ui.textChanges, [ui.input.value]);
  } finally { ui.dispose(); }
});

test("a late voice catalog from the previous profile cannot replace the new profile choices", async () => {
  let finish;
  const ui = setup((url) => url.includes("backend-one") ? new Promise((resolve) => { finish = resolve; }) : response(voices(["gamma"])));
  try {
    ui.profile.value = "two"; ui.profile.onchange(); await tick();
    assert.equal(ui.voice.value, "gamma");
    finish(response(voices(["alpha", "beta"]))); await tick();
    assert.equal(ui.voice.value, "gamma");
    await ui.generate.onclick();
    const request = ui.requests.at(-1).payload;
    assert.equal(request.backend_id, "backend-two");
    assert.equal(request.duplicate_of, "two");
    assert.deepEqual(ui.changes, ["two"]);
  } finally { ui.dispose(); }
});

test("playback-only mode blocks previews and closing suppresses late results", async () => {
  let finish;
  let onlyPlayback = true;
  const ui = setup((url) => url.endsWith("/preview") ? new Promise((resolve) => { finish = resolve; }) : response(voices(["alpha"])), () => onlyPlayback);
  await tick();
  assert.equal(ui.generate.disabled, true);
  await ui.generate.onclick();
  assert.equal(ui.requests.some((r) => r.url.endsWith("/preview")), false);
  onlyPlayback = false;
  const generating = ui.generate.onclick();
  assert.equal(ui.profile.disabled, true);
  ui.dispose(); finish(response({ url: "/discarded" })); await generating;
  assert.equal(ui.element.querySelectorAll("audio").length, 0);
});

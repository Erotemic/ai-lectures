import assert from "node:assert/strict";
import { renderLearningPlan } from "../ailectures/static/learning-plan.mjs";

class Element {
  constructor(tag) { this.tagName = tag.toUpperCase(); this.children = []; this.attributes = {}; this.style = {}; this.checked = false; }
  append(...children) { for (const child of children) { if (child instanceof Element) child.parentElement = this; this.children.push(child); } }
  replaceChildren(...children) { this.children.forEach(child => { if (child instanceof Element) child.parentElement = null; }); this.children = []; this.append(...children); }
  setAttribute(key, value) { this.attributes[key] = String(value); if (key === "value") this.value = String(value); if (key === "checked") this.checked = true; }
  addEventListener() {}
  querySelectorAll(selector) { return descendants(this).filter(node => selector === "[data-plan-action]" && "data-plan-action" in node.attributes); }
  get value() { return this._value ?? this.children.find(child => child.tagName === "OPTION")?.value ?? ""; }
  set value(value) { this._value = value; }
  get textContent() { return this.text ?? this.children.map(child => child instanceof Element ? child.textContent : String(child)).join(" "); }
  set textContent(value) { this.text = String(value); this.children = []; }
  get isConnected() { return this.connected || Boolean(this.parentElement?.isConnected); }
}
function descendants(root) { return root.children.flatMap(child => child instanceof Element ? [child, ...descendants(child)] : []); }
const find = (root, predicate) => descendants(root).find(predicate);
const field = (root, label) => find(root, node => node.attributes["aria-label"] === label);
const optionIds = node => node.children.filter(child => child.tagName === "OPTION").map(child => child.value);

globalThis.document = { createElement: tag => new Element(tag) };
const cache = new Map();
globalThis.localStorage = { getItem: key => cache.get(key) ?? null, setItem: (key, value) => cache.set(key, value) };
globalThis.history = { state: {}, replaceState(_state, _unused, url) {
  const parsed = new URL(url, "http://library.test");
  globalThis.location = { href: parsed.href, pathname: parsed.pathname, search: parsed.search };
} };
const data = {
  generation: "one", component_lectures: {}, relationships: [],
  nodes: {
    "math:one": { id: "math:one", title: "Linear maps", kind: "lecture", available: true,
      url: "/lectures/math/one", categories: ["Mathematics"], tags: ["eigenvalues"], prerequisites_reviewed: true },
    "math:two": { id: "math:two", title: "Local geometry", kind: "lecture", available: true,
      url: "/lectures/math/two", categories: ["Mathematics"], tags: ["rate of change"], prerequisites_reviewed: true },
  },
  collections: [
    { id: "math:guide", title: "Mathematics guide", role: "hub", lectures: [], categories: ["Mathematics"], url: "/collections/math%3Aguide" },
    { id: "math:empty", title: "An empty route", lectures: [], categories: ["Mathematics"] },
    { id: "math:route", title: "Linear algebra", lectures: ["math:one"], categories: ["Mathematics"] },
    { id: "math:calculus", title: "Calculus", lectures: ["math:two"], categories: ["Mathematics"] },
  ],
};
let requests = [];
globalThis.fetch = async (url, options = {}) => {
  requests.push({ url, options });
  const response = options.method === "POST" ? {
    valid: true, steps: [{ ...data.nodes["math:one"], role: "goal", depends_on: [], reasons: [] }],
    unmapped: [], missing: [], cycles: [], blocked: [], assumptions: [], assumed_uncertain: [], unknown_knowledge: [],
  } : data;
  return { ok: true, json: async () => response };
};
async function render(path) {
  cache.clear(); requests = [];
  const parsed = new URL(path, "http://library.test");
  globalThis.location = { href: parsed.href, pathname: parsed.pathname, search: parsed.search };
  const main = new Element("main"); main.connected = true;
  await renderLearningPlan(main);
  return main;
}

const main = await render("/learning-plan");
assert.deepEqual(optionIds(field(main, "Planning collection")), ["", "math:route", "math:calculus"]);
assert.deepEqual(optionIds(field(main, "Background collection")), ["", "math:route", "math:calculus"]);
const goalSearch = field(main, "Find a learning goal");
goalSearch.value = "eigenvalues"; goalSearch.oninput();
assert.deepEqual(optionIds(field(main, "Learning goal")), ["", "math:one"]);
goalSearch.value = "rate-of-change"; goalSearch.oninput();
assert.deepEqual(optionIds(field(main, "Learning goal")), ["", "math:two"]);
const backgroundSearch = field(main, "Find background material");
backgroundSearch.value = "eigenvalues"; backgroundSearch.oninput();
assert.ok(find(main, node => node.attributes["data-lecture"] === "math:one"));

const hub = await render("/learning-plan?collection=math%3Aguide");
assert.equal(requests.filter(item => item.options.method === "POST").length, 0,
  "an empty hub must not become a successful empty learning plan");
assert.match(hub.textContent, /Choose a lecture route within this guide/);
assert.doesNotMatch(hub.textContent, /already covered by your familiarity/);
assert.ok(find(hub, node => node.attributes.href === "/collections/math%3Aguide"));
const retained = field(hub, "Planning collection").children.find(node => node.value === "math:guide");
assert.equal(retained.disabled, true, "a direct-linked hub is a prompt, not a selectable sequence");
const collection = field(hub, "Planning collection");
collection.value = "math:route"; collection.onchange();
const form = find(hub, node => node.tagName === "FORM");
form.onsubmit({ preventDefault() {} });
await new Promise(resolve => setImmediate(resolve));
const post = requests.find(item => item.options.method === "POST");
assert.deepEqual(JSON.parse(post.options.body).goals, ["math:one"]);

const missing = await render("/learning-plan?collection=missing%3Aguide");
assert.equal(requests.filter(item => item.options.method === "POST").length, 0);
assert.match(missing.textContent, /This collection is unavailable/);
assert.doesNotMatch(missing.textContent, /already covered by your familiarity/);
console.log("Study plan excludes empty guides, prompts direct links to choose a route, and searches concept tags");

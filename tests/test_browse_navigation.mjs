import assert from "node:assert/strict";
import { test } from "node:test";
import { CatalogBrowser } from "../ailectures/static/browse.mjs";
import { el, store } from "../ailectures/static/api.mjs";

class Element {
  constructor(tag) { this.tagName = tag; this.children = []; this.value = ""; }
  append(...children) { this.children.push(...children); }
  replaceChildren(...children) { this.children = children; }
  addEventListener() {}
  setAttribute(key, value) { this[key] = value; }
  get selectedOptions() { return this.children.filter((child) => child.value === this.value); }
  get text() { return this.textContent; }
}

test("browse destinations ignore stale storage while filtered URLs survive returning and reloading", () => {
  const storage = new Map();
  globalThis.localStorage = {
    getItem: (key) => storage.get(key) ?? null,
    setItem: (key, value) => storage.set(key, value),
  };
  globalThis.document = { createElement: (tag) => new Element(tag) };
  globalThis.history = {
    state: { scroll: 250, browseLimit: 84 },
    replaceState(state, _, path) {
      this.state = state;
      globalThis.location = new URL(path, location);
    },
  };
  store("browse:device", { category: "Science", q: "remembered search", view: "all" });
  const browser = new CatalogBrowser({
    catalog: () => ({ lectures: [], courses: [] }),
    progress: () => ({}), listener: () => "device",
    link: (text, href) => el("a", { text, href }),
    button: (text) => el("button", { text }),
    byId: () => undefined,
  });
  const main = new Element("main");
  for (const path of ["/", "/collections", "/courses", "/?all=1", "/collections?all=1"]) {
    globalThis.location = new URL(path, "http://reader.test");
    browser.browse(main);
    assert.equal(location.pathname + location.search, "/");
    assert.equal(history.state.scroll, 250);
    assert.equal(history.state.browseLimit, 84);
  }
  const filtered = "/?category=Science&q=explicit+search&sort=title";
  for (const prefix of ["", "/collections", "/courses"]) {
    const path = prefix ? prefix + filtered.slice(1) : filtered;
    globalThis.location = new URL(path, "http://reader.test");
    browser.browse(main);
    assert.equal(location.pathname + location.search, filtered);
  }
  globalThis.location = new URL("/", "http://reader.test");
  browser.browse(main);
  assert.equal(location.pathname + location.search, "/");
});

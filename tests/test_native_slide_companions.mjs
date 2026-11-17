import assert from "node:assert/strict";
import { showSlideCompanions, preparedSlideCompanions } from "../ailectures/static/slide-companions.mjs";

class Element {
  constructor(tag) {
    this.tagName = tag.toUpperCase();
    this.children = [];
    this.attributes = {};
    this.style = {};
    this.events = {};
    this.hidden = false;
    this.srcChanges = 0;
  }
  append(...children) { this.children.push(...children); }
  replaceChildren(...children) { this.children = children; }
  addEventListener(name, handler) { this.events[name] = handler; }
  setAttribute(key, value) {
    this.attributes[key] = String(value);
    if (key === "hidden") this.hidden = true;
    if (key === "value") this.value = String(value);
  }
  removeAttribute(key) { delete this.attributes[key]; delete this[key]; }
  set src(value) { this.source = value; this.srcChanges++; }
  get src() { return this.source; }
}
globalThis.document = { createElement: (tag) => new Element(tag) };

const record = (id, built = false) => ({
  id, title: id, subtitle: "An authored diagram", slide_count: 5,
  state: built ? "built" : "unbuilt", built, available: true, build_available: true,
  status_url: `/api/library/slide-decks/${id}`,
  build_url: `/api/library/slide-decks/${id}/build`,
  view_url: `/api/library/slide-decks/${id}/html`,
  download_url: `/api/library/slide-decks/${id}/html?download=1`,
  attribution: "Original author", source_credits: [{ sources: {
    primary: { title: "Primary source", url: "https://example.org/primary" },
  } }],
});

const main = new Element("main");
let reads = [], writes = [], finish;
const panel = showSlideCompanions(main, { id: "g2:001000" }, {
  api: async (path) => {
    reads.push(path);
    return path.includes("?lecture_id=")
      ? { available: true, items: [record("first"), record("second", true)] }
      : record("first", true);
  },
  post: async (path, body) => {
    writes.push({ path, body });
    return new Promise((resolve) => { finish = resolve; });
  },
});
assert.equal(reads.length, 0, "closed details must not load optional renderer metadata");
assert.equal(writes.length, 0);
assert.equal(panel.frame.hidden, true);
await panel.load();
assert.equal(reads.length, 1);
assert.match(reads[0], /lecture_id=g2%3A001000/);
assert.equal(panel.selected, "first");
assert.equal(panel.frame.srcChanges, 0, "listing never loads or builds an HTML frame");
assert.equal(panel.buildButton.disabled, false);
assert.equal(panel.viewButton.disabled, true);
assert.equal(panel.credits.hidden, false);

const pending = panel.buildSelected();
assert.equal(writes.length, 1);
assert.deepEqual(writes[0], { path: "/api/library/slide-decks/first/build", body: {} });
assert.equal(panel.buildButton.disabled, true);
await panel.buildSelected();
assert.equal(writes.length, 1, "duplicate clicks must not start duplicate builds");
finish(record("first", true));
await pending;
assert.equal(panel.frame.hidden, false);
assert.equal(panel.frame.src, "/api/library/slide-decks/first/html?embed=1");
assert.equal(panel.downloadLink.href, "/api/library/slide-decks/first/html?download=1");
assert.equal(panel.openLink.href, "/api/library/slide-decks/first/html");
const frame = panel.frame;
await panel.refresh();
panel.viewSelected();
assert.equal(panel.frame, frame);
assert.equal(panel.frame.srcChanges, 1, "refresh must preserve the viewer's selected slide");
panel.select.value = "second";
panel.select.onchange();
assert.equal(panel.frame, frame, "switching decks reuses the same iframe element");
assert.equal(panel.frame.src, "/api/library/slide-decks/second/html?embed=1");
const changes = panel.frame.srcChanges;
panel.items.set("second", { ...panel.items.get("second"), revision: "new-source-build" });
panel.viewSelected();
assert.equal(panel.frame.srcChanges, changes + 1,
  "a changed built artifact must reload even when its deck ID is unchanged");

const failed = showSlideCompanions(new Element("main"), { id: "g2:001000" }, {
  api: async () => ({ available: true, items: [record("retry")] }),
  post: async () => { throw new Error("Renderer failed"); },
});
await failed.load();
await failed.buildSelected();
assert.equal(failed.error.hidden, false);
assert.match(failed.error.textContent, /Renderer failed/);
assert.equal(failed.buildButton.disabled, false, "failed builds must remain retryable");
assert.equal(failed.frame.hidden, true);

const interrupted = showSlideCompanions(new Element("main"), { id: "g2:001000" }, {
  api: async () => ({ available: true, items: [record("slow"), record("other", true)] }),
  post: async () => new Promise((resolve) => { finish = resolve; }),
});
await interrupted.load();
const slowBuild = interrupted.buildSelected();
interrupted.select.value = "other";
interrupted.select.onchange();
interrupted.viewSelected();
finish(record("slow", true));
await slowBuild;
assert.equal(interrupted.selected, "other");
assert.equal(interrupted.frame.src, "/api/library/slide-decks/other/html?embed=1",
  "a late build response must not switch the selected deck");

let tries = 0;
const unavailable = showSlideCompanions(new Element("main"), {
  id: "portable:001000", companions: [{ title: "Prepared HTML", url: "/prepared" }],
}, {
  api: async () => {
    if (++tries === 1) throw new Error("Temporary connection problem");
    return { available: false, items: [] };
  },
});
await unavailable.load();
assert.equal(unavailable.loadRetry.hidden, false);
await unavailable.load();
assert.equal(unavailable.error.hidden, true);
assert.equal(unavailable.controls.hidden, true);
assert.match(unavailable.status.textContent, /Prepared companion files remain available/);
assert.equal(unavailable.row.companions[0].url, "/prepared");

const preparedRow = {
  id: "portable:001000",
  companions: [
    { id: "slides", title: "Prepared diagrams", role: "prepared", media_type: "text/html",
      url: "/api/library/companions/release/lecture/slides/checksum", sha256: "checksum",
      attribution: "Diagram creator" },
    { id: "source", role: "source", media_type: "text/html", url: "/source" },
    { id: "pdf", role: "prepared", media_type: "application/pdf", url: "/pdf" },
  ],
};
const originalCompanions = JSON.stringify(preparedRow.companions);
assert.equal(preparedSlideCompanions(preparedRow).length, 1);
assert.deepEqual(preparedSlideCompanions({ companions: {} }), []);
assert.deepEqual(preparedSlideCompanions({ companions: [null, { role: "prepared", media_type: 3 }] }), []);
let preparedReads = [], preparedWrites = [];
const portable = showSlideCompanions(new Element("main"), preparedRow, {
  api: async (path) => {
    preparedReads.push(path);
    return { available: false, items: [] };
  },
  post: async (...args) => { preparedWrites.push(args); },
});
await portable.load();
assert.equal(portable.selected, "prepared:slides");
assert.equal(portable.controls.hidden, false);
assert.equal(portable.buildButton.hidden, true);
assert.equal(portable.refreshButton.hidden, true);
assert.equal(portable.viewButton.disabled, false);
assert.equal(portable.items.get("prepared:slides").revision, "checksum");
assert.equal(portable.items.get("prepared:slides").attribution, "Diagram creator");
assert.equal(portable.downloadLink.href, preparedRow.companions[0].url);
assert.equal(portable.openLink.href, preparedRow.companions[0].url + "?view=1");
portable.viewSelected();
assert.equal(portable.frame.src, preparedRow.companions[0].url + "?view=1&embed=1");
const portableFrame = portable.frame;
await portable.refresh();
await portable.buildSelected();
assert.equal(preparedReads.length, 1, "prepared viewing and refresh do not request renderer status");
assert.equal(preparedWrites.length, 0, "prepared HTML never starts a renderer build");
assert.equal(portable.frame, portableFrame);
assert.equal(JSON.stringify(preparedRow.companions), originalCompanions,
  "existing prepared download links and metadata remain unchanged");

const mixed = showSlideCompanions(new Element("main"), preparedRow, {
  api: async () => ({ available: true, items: [record("repository-deck")] }),
});
await mixed.load();
assert.deepEqual([...mixed.items.keys()], ["prepared:slides", "repository-deck"]);
mixed.select.value = "repository-deck";
mixed.select.onchange();
assert.equal(mixed.buildButton.hidden, false);
assert.equal(mixed.refreshButton.hidden, false);
assert.equal(mixed.buildButton.disabled, false);

const preparedFallback = showSlideCompanions(new Element("main"), preparedRow, {
  api: async () => { throw new Error("Optional repository discovery unavailable"); },
});
await preparedFallback.load();
preparedFallback.viewSelected();
assert.equal(preparedFallback.frame.hidden, false);
assert.equal(preparedFallback.error.hidden, true);
assert.equal(preparedFallback.selected, "prepared:slides");
console.log("Native slide controls: lazy discovery, explicit builds, stable viewer, retry, deck-switch races, and portable links passed");

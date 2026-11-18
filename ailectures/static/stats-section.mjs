import { el, getStored, store } from "./api.mjs";

/** Independent sections remember the reader's choice across refresh/navigation. */
export function statsSection(id, title, ...children) {
  const root = el("details", { class: "stats-section section", id: "stats-section-" + id,
    open: getStored("stats-section:" + id, id === "coverage") },
    el("summary", {}, el("h2", { text: title })), ...children);
  let previous = root.open;
  root.addEventListener("toggle", () => {
    if (root.open !== previous) store("stats-section:" + id, root.open);
    previous = root.open;
  });
  return root;
}

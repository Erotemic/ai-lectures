import { el } from "./api.mjs";
import { formatMinutes } from "./browse-model.mjs";
import { reactionControls } from "./reactions.mjs";

export const lectureViews = ["compact", "detail", "cards"];
export const lectureView = (value, fallback = "compact") => lectureViews.includes(value) ? value : lectureViews.includes(fallback) ? fallback : "compact";
export const initialLectureLimit = view => view === "compact" ? 250 : 100;

/** All views retain the same identities, links, filters, and playback order. */
export function inventoryItem(row, view, { item, reactions, packs, returnTo, axis }) {
  const node = item(row, axis);
  node.dataset.lectureId = row.id;
  const copy = node.querySelector(".copy");
  const anchor = copy.querySelector(":scope > a");
  const target = new URL(anchor.href, location.origin);
  target.searchParams.set("return", returnTo);
  anchor.href = target.pathname + target.search;
  copy.append(el("small", { class: "lecture-identity", text: `${row.id} · ${packs.get(row.origin?.pack || row.namespace) || row.namespace || ""}` }));
  const feedback = reactions ? reactionControls(row, reactions, { compact: true }) : null;
  if (view === "compact") {
    const complete = row.recordings?.some(recording => recording.complete);
    const audio = row.kind === "presentation" ? "Slides" : complete ? "Audio" : row.recordings?.length ? "Partial" : "Text";
    anchor.classList.add("compact-lecture-title");
    anchor.title = row.title;
    const summary = el("summary", {}, anchor,
      el("span", { class: "compact-lecture-duration muted", text: formatMinutes(row.estimated_minutes || (row.words || 0) / 145) }),
      el("span", { class: "compact-lecture-audio muted", text: audio, title: complete ? "Complete audio available" : audio === "Partial" ? "Partially generated audio" : "Transcript available" }));
    const details = el("details", { class: "compact-lecture" }, summary,
      el("div", { class: "compact-lecture-info" }, copy, feedback));
    node.replaceChildren(details);
    node.classList.add("compact-inventory-item");
  } else {
    if (view === "cards") {
      node.classList.add("card", "lecture-card");
      anchor.replaceWith(el("h2", {}, anchor.cloneNode(true)));
    }
    if (feedback) node.append(feedback);
  }
  return node;
}

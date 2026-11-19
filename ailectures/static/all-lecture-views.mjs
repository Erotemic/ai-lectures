import { el } from "./api.mjs";
import { chronologyRecord } from "./chronology.mjs";
import { owningTrack, formatMinutes } from "./browse-model.mjs";
import { reactionControls } from "./reactions.mjs";

export const lectureViews = ["compact", "detail", "cards"];
export const lectureView = (value, fallback = "compact") => lectureViews.includes(value) ? value : lectureViews.includes(fallback) ? fallback : "compact";
export const initialLectureLimit = view => view === "compact" ? 250 : 100;

/** All views retain the same identities, links, filters, and playback order. */
export function inventoryItem(row, view, { item, reactions, packs, returnTo, axis, courses = [] }) {
  const node = item(row, axis);
  node.dataset.lectureId = row.id;
  const copy = node.querySelector(".copy");
  const anchor = copy.querySelector(":scope > a");
  const target = new URL(anchor.href, location.origin);
  target.searchParams.set("return", returnTo);
  anchor.href = target.pathname + target.search;
  const track = owningTrack(row, courses);
  copy.append(el("small", { class: "lecture-identity" }, row.id + " · ",
    el("a", {href: track ? "/collections/"+encodeURIComponent(track.id) : "/lectures?"+new URLSearchParams({pack:row.origin?.pack || row.namespace}),
      "data-nav":"",text:track?.title || packs.get(row.origin?.pack || row.namespace) || row.namespace || "Content pack"})));

  const feedback = reactions ? reactionControls(row, reactions, { compact: true }) : null;
  if (view === "compact") {
    const complete = row.recordings?.some(recording => recording.complete);
    const audio = row.kind === "presentation" ? "Slides" : complete ? "Audio" : row.recordings?.length ? "Partial" : "Not generated";
    anchor.classList.add("compact-lecture-title");
    anchor.title = row.title;
    const record = axis && chronologyRecord(row, axis);
    const year = value => Math.abs(value).toLocaleString() + (value < 0 ? " BCE" : " CE");
    const date = axis ? el("span", { class: "compact-lecture-date muted", text: record?.label || (record ? year(record.start) : "Undated"), title: record ? [record.label, record.note].filter(Boolean).join(" · ") : "No date recorded for this axis" }) : null;
    const summary = el("summary", { class: axis ? "with-date" : "" }, anchor, date,
      el("span", { class: "compact-lecture-duration muted", text: formatMinutes(row.estimated_minutes || (row.words || 0) / 145) }),
      el("span", { class: "compact-lecture-audio muted", text: audio, title: row.kind === "presentation" ? "Slides without a usable spoken transcript" : complete ? "Complete audio available" : audio === "Partial" ? "Partially generated audio" : "Narration text available; audio has not been generated" }));
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

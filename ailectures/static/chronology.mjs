import { el } from "./api.mjs";

export const dateAxes = {
  work: "Work date", period: "Period covered", setting: "Story setting",
  life: "Subject’s lifespan", witness: "Textual witness", composition: "Composition date", context: "Historical setting",
};

export function dateOrder(value) {
  const match = /^date-(work|period|setting|life|witness|composition|context)(-desc)?$/.exec(value || "");
  return match ? { axis: match[1], descending: Boolean(match[2]) } : null;
}

export function chronologyRecord(row, axis) {
  const record = row?.chronology?.[axis];
  if (!record || !Number.isSafeInteger(record.start) || !Number.isSafeInteger(record.end ?? record.start) ||
      Math.abs(record.start) > 1e12 || Math.abs(record.end ?? record.start) > 1e12 ||
      record.start === 0 || record.end === 0 || (record.end ?? record.start) < record.start) return null;
  return record;
}

export function sortChronologically(rows, value) {
  const order = dateOrder(value);
  if (!order) return [...rows];
  return rows.map((row, index) => ({ row, index })).sort((a, b) => {
    const first = chronologyRecord(a.row, order.axis), second = chronologyRecord(b.row, order.axis);
    if (!first || !second) return first ? -1 : second ? 1 : a.index - b.index;
    const difference = first.start - second.start || (first.end ?? first.start) - (second.end ?? second.start);
    return difference ? difference * (order.descending ? -1 : 1) : a.index - b.index;
  }).map(item => item.row);
}

export function chronologyOptions() {
  return Object.entries(dateAxes).flatMap(([axis, label]) => [
    el("option", { value: "date-" + axis, text: label + " · oldest first" }),
    el("option", { value: "date-" + axis + "-desc", text: label + " · newest first" }),
  ]);
}

export function chronologyLine(row, axis = null) {
  const key = axis || Object.keys(dateAxes).find(key => chronologyRecord(row, key));
  const record = key && chronologyRecord(row, key);
  if (!record) return axis ? el("small", { class: "chronology-label muted", text: dateAxes[axis] + " not recorded" }) : null;
  const year = value => Math.abs(value).toLocaleString("en-US") + (value < 0 ? " BCE" : " CE");
  const fallback = record.start === (record.end ?? record.start) ? year(record.start) : year(record.start) + "–" + year(record.end);
  const basis = ({ declared_coverage: "stated coverage", rounded_geological_age: "approximate geological age", contents: "dated contents", mixed: "mixed date bases" })[record.basis] || record.basis?.replaceAll("_", " ");
  return el("small", { class: "chronology-label", title: record.note || "",
    text: `${dateAxes[key]} · ${record.label || fallback}${basis ? " · " + basis : ""}${record.approximate ? " · approximate" : ""}` });
}

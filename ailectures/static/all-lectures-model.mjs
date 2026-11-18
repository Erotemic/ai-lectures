/** A flat catalog view never rewrites collection membership or playback order. */
import { matchesLecture, matchesTag } from "./browse-model.mjs";
import { dateOrder, sortChronologically } from "./chronology.mjs";

export function allLectureRows(lectures, filters = {}) {
  const byId = new Map(lectures.map(row => [row.id, row]));
  const rows = [...byId.values()].filter(row => {
    const recordings = row.recordings || [];
    const complete = recordings.some(recording => recording.complete);
    return (!filters.category || row.categories?.includes(filters.category))
      && (!filters.pack || (row.origin?.pack || row.namespace) === filters.pack)
      && matchesTag(row, filters.tag)
      && matchesLecture(row.id, id => byId.get(id), filters.q)
      && (!filters.audio || (filters.audio === "ready" ? complete
        : filters.audio === "partial" ? !complete && recordings.length > 0 : recordings.length === 0));
  });
  const sort = filters.sort || "title";
  if (dateOrder(sort)) return sortChronologically(rows, sort);
  const minutes = row => row.estimated_minutes ?? (row.words || 0) / 145;
  return rows.sort((a, b) => {
    const difference = sort === "id" ? a.id.localeCompare(b.id)
      : sort === "short" || sort === "long" ? (minutes(a) - minutes(b)) * (sort === "long" ? -1 : 1)
      : a.title.localeCompare(b.title);
    return difference || a.id.localeCompare(b.id);
  });
}

/** Library totals count content identities, never repeated listening-route entries. */
import { collectionRows } from "./browse-model.mjs";

const positive = value => Number.isFinite(value) && value > 0 ? value : 0;

export function contentTotals(rows) {
  const unique = [...new Map(rows.map(row => [row.id, row])).values()];
  let words = 0, complete = 0, partial = 0, companions = 0;
  for (const row of unique) {
    words += positive(row.words);
    const recordings = row.recordings || [];
    if (recordings.some(recording => recording.complete)) complete++;
    else if (recordings.length) partial++;
    if (row.companions?.some(companion => !companion.stale)) companions++;
  }
  return { lectures: unique.length, words, minutes: words / 145, complete, partial,
    missing: unique.length - complete - partial, companions };
}

export function libraryStats(catalog) {
  const rows = [...new Map((catalog.lectures || []).map(row => [row.id, row])).values()];
  const courses = catalog.courses || [];
  const byId = new Map(rows.map(row => [row.id, row]));
  const grouped = field => {
    const groups = new Map();
    for (const row of rows) {
      const labels = row[field]?.length ? row[field] : ["Unspecified"];
      for (const label of new Set(labels)) {
        if (!groups.has(label)) groups.set(label, []);
        groups.get(label).push(row);
      }
    }
    return [...groups].map(([title, members]) => ({ title, ...contentTotals(members) }))
      .sort((a, b) => b.lectures - a.lectures || a.title.localeCompare(b.title));
  };
  const packNames = new Map((catalog.packs || []).map(pack => [pack.id, pack.title || pack.id]));
  const packGroups = new Map([...packNames.keys()].map(id => [id, []]));
  for (const row of rows) {
    const id = row.origin?.pack || "unassigned";
    if (!packGroups.has(id)) packGroups.set(id, []);
    packGroups.get(id).push(row);
  }
  return {
    ...contentTotals(rows), collections: courses.length, packs: packNames.size,
    subjects: grouped("categories"), audiences: grouped("audiences"),
    packRows: [...packGroups].map(([id, members]) => ({ id, title: packNames.get(id) || (id === "unassigned" ? "Unassigned content" : id), ...contentTotals(members) }))
      .sort((a, b) => b.lectures - a.lectures || a.title.localeCompare(b.title)),
    collectionRows: courses.map(course => ({ id: course.id, title: course.title || course.id,
      role: course.role, ...contentTotals(collectionRows(course, courses, id => byId.get(id))) }))
      .sort((a, b) => b.lectures - a.lectures || a.title.localeCompare(b.title)),
  };
}

import { dateAxes, chronologyRecord } from "./chronology.mjs";
import { tagLabels } from "./tag-model.mjs";
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
  const placeLabels = row => [...new Set([...(row.places || []), ...tagLabels(row).filter(tag => tag.startsWith("Place: ")).map(tag => tag.slice(7))])];
  const grouped = (field, valuesFor = null) => {
    const groups = new Map();
    for (const row of rows) {
      const values = valuesFor ? valuesFor(row) : field === "tags" ? tagLabels(row) : row[field];
      const labels = values?.length ? values : ["Unspecified"];
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
  const dates = {};
  const axisNames = Object.keys(dateAxes);
  for (const axis of axisNames) {
    const buckets = new Map();
    for (const row of rows) for (const label of new Set(row.time_coverage?.[axis] || [])) {
      if (!buckets.has(label)) buckets.set(label, []);
      buckets.get(label).push(row);
    }
    dates[axis] = [...buckets].map(([title, members]) => {
      const century = /^(\d+)(?:st|nd|rd|th) century (BCE|CE)$/.exec(title);
      const start = century ? (century[2] === "BCE" ? -Number(century[1]) * 100 : (Number(century[1]) - 1) * 100 + 1)
        : Math.min(...members.map(row => row.chronology?.[axis]?.start ?? Infinity));
      return { title, start, ...contentTotals(members) };
    }).sort((a, b) => a.start - b.start || a.title.localeCompare(b.title));
  }
  const authorRows = rows.map(row => ({ ...row, author_names: [...new Set((row.creators || [])
    .filter(credit => ["author", "attributed_author"].includes(credit.role)).map(credit => credit.name))] }));
  const authorGroups = new Map();
  for (const row of authorRows) for (const name of row.author_names) {
    if (!authorGroups.has(name)) authorGroups.set(name, []);
    authorGroups.get(name).push(row);
  }
  return {
    dateCoverage: Object.fromEntries(axisNames.map(axis => [axis, rows.filter(row => chronologyRecord(row, axis)).length])),
    places: grouped("places", placeLabels), directPlaces: grouped("places"), periods: grouped("periods"), topics: grouped("tags"), dates,
    authors: [...authorGroups].map(([title, members]) => ({ title, ...contentTotals(members) }))
      .sort((a, b) => b.lectures - a.lectures || a.title.localeCompare(b.title)),
    withPlaces: rows.filter(row => placeLabels(row).length).length,
    withDates: rows.filter(row => Object.keys(row.time_coverage || {}).length).length,
    withDescriptions: rows.filter(row => row.description).length,
    ...contentTotals(rows), collections: courses.length, packs: packNames.size,
    subjects: grouped("categories"), audiences: grouped("audiences"),
    packRows: [...packGroups].map(([id, members]) => ({ id, title: packNames.get(id) || (id === "unassigned" ? "Unassigned content" : id), ...contentTotals(members) }))
      .sort((a, b) => b.lectures - a.lectures || a.title.localeCompare(b.title)),
    collectionRows: courses.map(course => ({ id: course.id, title: course.title || course.id,
      role: course.role, ...contentTotals(collectionRows(course, courses, id => byId.get(id))) }))
      .sort((a, b) => b.lectures - a.lectures || a.title.localeCompare(b.title)),
  };
}

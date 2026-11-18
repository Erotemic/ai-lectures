import { tagLabels } from "./tag-model.mjs";
/** Pure catalog views. Filtering and grouping never change playback membership. */

export function formatMinutes(minutes) {
  const value = Number(minutes);
  const total = Number.isFinite(value) ? Math.max(0, Math.round(value)) : 0;
  const hours = Math.floor(total / 60);
  const remainder = total % 60;
  if (!hours) return `${total} min`;
  return `${hours} h${remainder ? ` ${remainder} min` : ""}`;
}

export function collectionRows(collection, courses, byId) {
  const rows = [];
  const visited = new Set();
  const included = new Set();
  function visit(current) {
    if (!current) return;
    const identity = current.id ?? current;
    if (visited.has(identity)) return;
    visited.add(identity);
    const lectures = current.lectures || [];
    if (lectures.length) {
      for (const key of lectures) {
        const row = byId(key);
        if (!row) continue;
        const identity = row.id ?? key;
        if (included.has(identity)) continue;
        included.add(identity);
        rows.push(row);
      }
    } else if (current.id) {
      for (const child of courses) {
        if (child.parent_id === current.id && child.role !== "archive") visit(child);
      }
    }
  }
  visit(collection);
  return rows;
}

export function collectionAncestors(collection, courses) {
  const ancestors = [];
  const seen = new Set(collection ? [collection.id] : []);
  let parent = collection?.parent_id;
  while (parent && !seen.has(parent)) {
    const current = courses.find((candidate) => candidate.id === parent);
    if (!current) break;
    seen.add(parent);
    ancestors.push(current);
    parent = current.parent_id;
  }
  return ancestors.reverse();
}

function unmatchedEntries(entries, used) {
  const counts = new Map();
  for (const key of used) counts.set(key, (counts.get(key) || 0) + 1);
  return entries.filter((key) => {
    const count = counts.get(key) || 0;
    if (!count) return true;
    counts.set(key, count - 1);
    return false;
  });
}

export function collectionSections(collection, byId) {
  const identifiers = new Set();
  function identifier(prefix, first, fallback) {
    const base = prefix + encodeURIComponent(first || String(fallback));
    let id = base;
    let suffix = 1;
    while (identifiers.has(id)) id = `${base}--${suffix++}`;
    identifiers.add(id);
    return id;
  }
  function sessionCopy(session, fallback) {
    const lectures = [...(session.lectures || [])];
    return {
      id: identifier("session-", lectures[0], fallback),
      title: session.title || "Contents",
      lectures,
    };
  }
  if (collection.chapters?.length) {
    const sections = collection.chapters.map((chapter, index) => {
      const sessions = chapter.sessions?.map((session, sessionIndex) =>
        sessionCopy(session, `${index}-${sessionIndex}`),
      );
      const lectures = [...(chapter.lectures || sessions?.flatMap((session) => session.lectures) || [])];
      const section = {
        id: identifier("section-", lectures[0], index),
        title: chapter.title || "Contents",
        lectures,
      };
      if (sessions) {
        // Old/imported catalogs may contain incomplete optional grouping data.
        const remaining = unmatchedEntries(lectures, sessions.flatMap((session) => session.lectures));
        if (remaining.length)
          sessions.push(sessionCopy({ title: "Contents", lectures: remaining }, `${index}-remaining`));
        section.sessions = sessions;
      }
      if (chapter.collection !== undefined) section.collection = chapter.collection;
      return section;
    });
    const remaining = unmatchedEntries(
      collection.lectures || [],
      sections.flatMap((section) => section.lectures),
    );
    if (remaining.length)
      sections.push({
        id: identifier("section-", remaining[0], sections.length),
        title: "Contents",
        lectures: remaining,
      });
    return sections;
  }
  const sections = [];
  let previous = null;
  for (const key of collection.lectures || []) {
    const name = byId(key)?.section || "";
    if (!sections.length || name !== previous) {
      sections.push({
        id: identifier("section-", key, sections.length),
        title: name ? name.replaceAll("-", " ") : "Contents",
        lectures: [],
      });
    }
    sections.at(-1).lectures.push(key);
    previous = name;
  }
  for (const section of sections)
    if (section.lectures.length === 1)
      section.title = byId(section.lectures[0])?.title || section.title;
  if (sections.length === 1 && sections[0].lectures.length > 1) sections[0].title = "Contents";
  return sections;
}

export function matchesLecture(key, byId, query) {
  const term = String(query ?? "").trim().toLocaleLowerCase();
  if (!term) return true;
  const stable = String(key ?? "");
  const row = byId(key);
  const title = row?.title || "";
  return `${title} ${stable} ${stable.split(":").at(-1)} ${tagLabels(row).join(" ")} ${row?.description || ""} ${(row?.outline || []).join(" ")} ${(row?.creators || []).map(credit => credit.name).join(" ")}`
    .toLocaleLowerCase()
    .includes(term);
}

export function matchesTag(row, tag) {
  const requested = String(tag || "").trim().toLocaleLowerCase();
  return !requested || tagLabels(row).some(value => value.toLocaleLowerCase() === requested);
}

/** Return hints stay within this library's content browsing views. */
export function collectionReturnPath(hint, courseId, origin) {
  if (!hint) return null;
  try {
    const candidate = new URL(hint, origin);
    if (candidate.origin === origin && candidate.pathname === "/lectures")
      return candidate.pathname + candidate.search;
    if (candidate.origin === origin && candidate.pathname === "/stats")
      return candidate.pathname + candidate.search + candidate.hash;
    if (!courseId) return null;
    const match = /^\/(collections|courses)\/(.+)$/.exec(candidate.pathname);
    if (candidate.origin === origin && match && decodeURIComponent(match[2]) === courseId)
      return candidate.pathname + candidate.search + candidate.hash;
  } catch { /* Ignore malformed optional hints. */ }
  return null;
}

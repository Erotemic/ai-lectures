import { tagLabels, tagForest } from "./tag-model.mjs";

/** An editorial section is a declared grouping, never an inferred literary work. */
const sectionName = row => typeof row.section === "string" ? row.section.trim() : "";
export function sectionKey(row) {
  return JSON.stringify(sectionName(row) ? [row.namespace || row.origin?.pack || row.id.split(":")[0], sectionName(row)] : [row.id]);
}
export function coverageRows(rows) {
  return [...new Map(rows.map(row => [row.id, row])).values()].map(row => ({ ...row,
    tags: [...new Set([...tagLabels(row), ...(row.places || []).map(place => "Place: " + place)])],
  }));
}
export function coverageModel(rows) {
  const normalized = coverageRows(rows);
  const byId = new Map(normalized.map(row => [row.id, row]));
  const forests = tagForest(normalized);
  function sections(ids) {
    const groups = new Map();
    for (const id of ids) {
      const row = byId.get(id);
      if (!row) continue;
      const key = sectionKey(row);
      if (!groups.has(key)) groups.set(key, { key, section: sectionName(row), namespace: row.namespace || row.origin?.pack || "", lectures: 0, words: 0, first: row, members: [] });
      const group = groups.get(key);
      group.lectures++;
      group.members.push(row);
      group.words += Number.isFinite(row.words) && row.words > 0 ? row.words : 0;
    }
    return [...groups.values()].sort((a, b) => b.lectures - a.lectures || a.key.localeCompare(b.key));
  }
  const cache = new WeakMap();
  function totals(node) {
    if (cache.has(node)) return cache.get(node);
    const groups = sections(node.lectures);
    const narrower = new Set([...node.children.values()].flatMap(child => [...child.lectures]));
    const result = { lectures: node.lectures.size, sections: groups.length,
      minutes: groups.reduce((sum, group) => sum + group.words, 0) / 145,
      atLevel: [...node.lectures].filter(id => !narrower.has(id)).length, groups };
    cache.set(node, result);
    return result;
  }
  const tagged = facet => new Set([...(forests.get(facet)?.values() || [])].flatMap(node => [...node.lectures]));
  return { rows: normalized, forests, totals, tagged };
}

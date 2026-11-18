/** Path membership supplies parent matches without substring or prefix guessing. */
export function tagLabels(row) {
  return [...new Set([...(row?.tags || []), ...(row?.tag_paths || []).flat()])];
}
export function tagFacet(label) {
  if (label.startsWith("Place: ")) return "Places";
  if (label.startsWith("Author: ")) return "Authors";
  if (label.startsWith("Period: ")) return "Named periods";
  for (const axis of ["Historical period", "Work date", "Story setting", "Lifetime", "Surviving witness", "Composition date", "Historical setting"])
    if (label.startsWith(axis + ": ")) return axis;
  return "Topics";
}
export function tagForest(rows) {
  const facets = new Map();
  for (const row of new Map(rows.map(row => [row.id, row])).values()) {
    const paths = [...(row.tag_paths || [])];
    const covered = new Set(paths.flat());
    paths.push(...(row.tags || []).filter(tag => !covered.has(tag)).map(tag => [tag]));
    for (const path of paths) {
      if (!path.length) continue;
      const facet = tagFacet(path[0]);
      if (!facets.has(facet)) facets.set(facet, new Map());
      let level = facets.get(facet);
      for (const label of path) {
        if (!level.has(label)) level.set(label, { label, lectures: new Set(), children: new Map() });
        const node = level.get(label);
        node.lectures.add(row.id);
        level = node.children;
      }
    }
  }
  return facets;
}

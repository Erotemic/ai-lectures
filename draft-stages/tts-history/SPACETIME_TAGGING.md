# Spacetime coverage metadata for historical biographies

The biography track now records **what/where/when** in addition to a broad subject classification. This is pack-local, forward-compatible documentation, not a new global requirement on other tracks. The intended long-term use is to see which geographic areas and historical times have well-researched lectures, and where the catalog has gaps.

## Current search tags

Each newly authored `track.json` entry has a `tags` array. The source builder reads those tags using the existing catalog machinery; no migration of older entries is required.

- **Historical time:** `17th century`, `1660s`, etc., identify historical coverage. `Year: 1657` identifies a specific important event or publication. Do not emit one tag for every year of someone's life. Exact dates and full spans belong in chronology and coverage records.
- **Geographic scale:** `Region: East Asia`, `Country: Japan`, `Place: Edo (Tokyo)`. `Country:` means the territory's **modern country** for consistent aggregation, even if the historical polity had another name. `Historical polity: Tokugawa shogunate` preserves historical context. A subject's short visit can be a place tag if relevant to the lecture.
- **Topic and form:** descriptive tags (`Algebra`, `Decision theory`, `Probability theory`, `Biography`, `Scientific institutions`) remain ordinary tags, not coordinate codes.
- Tags describe the **biographical subject and lecture's center of coverage**, not every passing reference in a comparison. For instance, Seki's lecture discusses Basel only to compare independent mathematical developments: Basel is not tagged as a place where Seki worked.

## Structured time and space

The `metadata/<lecture-id>.json` companion contains optional additional information:

- `chronology`: existing, reader-supported axes such as `life`, `period`, and `setting`, using signed integer years, date qualifiers, provenance, and plain-language labels. A posthumous publication date can extend `period` but must not extend `life`.
- `spacetime_coverage` (pack-local, **not yet displayed by the catalog reader**): `schema_version`, `subject`, `places` and explanations. Place records have `place`, `present_day_country`, `historical_polity`, `start_year`, `end_year`, `role`, `note`, approximate modern centroid `coordinates`, and `source_ids`. These are episode-level points or coarse intervals suitable for an eventual visualization, not exhaustive travel diaries or proof of continuous residence.
- `historical_claims` and `related_resources`: documentary sources and claim-level anchors used to audit the manuscript. Coverage place source IDs must resolve through `metadata/sources.json`.

## Accuracy rules for a future coverage visualization

1. **Do not infer birthplace or travel from another person's work.** Separate the city where the subject acted from places merely discussed in the story.
2. **Respect uncertainty.** For Seki Takakazu, the birth year is debated. The approximate lower bound in `chronology.life` is a coarse indexing estimate; we do not create a precise `Year: 1642` tag, assert a definite birthplace, or place a birth map pin.
3. **Distinguish a life from a period of work.** Someone's lifespan, years of institutional residence, and posthumous reception are different ranges. Do not use `setting` (e.g., the entire Edo period) to claim they personally occupied those years.
4. **Modern labels versus historical borders.** For a global coverage map, `present_day_country` is a geographic grouping key and `historical_polity` is a different, date-sensitive attribute. The coordinates are approximate contemporary reference points, not precise locations of a historical person's home or laboratory.
5. **Only add evidenced geographic events.** A broad range can summarize multiple visits or a main work base, but must be marked as approximate in the note if it is not continuous. Interleaved locations and overlapping research appointments are normal.
6. **Don't mistake counts for depth.** A lecture with six cities does not necessarily cover six local mathematical traditions. Future maps should let viewers filter `role` (birth, education, research, teaching, visits), distinguish subjects from themes, and show uncertain ranges separately.
7. **Keep spoken narration intelligible.** Rich indexing belongs in metadata and nonspoken companions; lectures should explain chronology naturally rather than read out the tags.

This change introduces three substantive biographies: `127000` Huygens (Dutch Republic, France, England; 1629–1695), `128000` Seki (Japan, c. 1640s–1708), and `129000` Blackwell (United States, 1919–2010). Each includes audited source IDs, important years, relevant geographic tags, and chronological work and place records.

## Additional coverage examples (130000–132000)

- `130000` records **Ulugh Beg** as born in Soltaniyeh (modern Iran), governing and working in Samarqand (modern Uzbekistan), within the Timurid Empire. His published influence at Oxford in 1665 and archaeological reception in 1908 use `Reception year:` tags rather than claims of personal travel or lifetime work. The school and observatory's exact founding dates differ across sources; the metadata uses broad, qualified intervals.
- `131000` records **Alberto Calderón** in Mendoza, schooling near Zug, Buenos Aires, Chicago, and Cambridge, Massachusetts. Repeated institutional appointments have separate intervals; approximation flags do not mean continuous physical residence. Inverse conductivity chronology is pinned to the 1980 paper, not to later proofs by his successors.
- `132000` records **Chike Obi** in Zaria, Onitsha, Lagos, Ibadan, both distinct Cambridges, and a documented 1958 London political visit. His University of London *external degree* alone would not justify mapping him to London. The 1985 ICTP prize and 1986 ceremony at Trieste are different event types.

A `Reception year:` tag denotes the lecture's account of transmission or later rediscovery, not a lifetime event. This is an authoring convention for future indexing; it is not yet a special reader-supported query axis. Every map or query system should distinguish `chronology.life`, `chronology.work`, later reception and the richer `spacetime_coverage.places` role/interval entries rather than merging their spans.

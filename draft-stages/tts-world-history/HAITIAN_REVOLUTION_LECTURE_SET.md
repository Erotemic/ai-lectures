# Haitian Revolution — World History lecture set

## Scope and editorial rationale

Five audio-first, independently understandable World History lectures cover the political, military, social, and human history of the Haitian Revolution and its first decades of aftermath. The series belongs under the `atlantic-revolutions` section, uses IDs `400000` through `404000`, and adds no new audio application or runtime code. It focuses on the agency of enslaved people and free people of color; the contradictions in revolutionary leadership; women and rural households; and international coercion. It treats women and underdocumented people with source care rather than invented speech or private thoughts.

| ID | Lecture | Central question |
|---|---|---|
| 400000 | Saint-Domingue: The Wealth of a Colony and the People Who Made It | How could a prosperous export colony depend upon systematic unfreedom, and what networks sustained its people? |
| 401000 | The Night the Plantations Rose: Rebellion and Emancipation, 1791–1794 | How did organized revolt force legal emancipation, and why were the revolutionaries' demands not identical? |
| 402000 | Toussaint Louverture: Freedom, Work, and the Burden of Command | Why did a leader defending abolition impose coercive labor and centralize authority? |
| 403000 | Against Napoleon: The War That Made Haiti, 1802–1804 | How did the attempt to restore French control transform autonomy into independence? |
| 404000 | After the Victory: Haiti, Freedom, and the Price of Recognition | How did an independent state defend sovereignty, allocate land, and confront foreign financial coercion? |

## Source practice

- Source metadata uses the track's existing `metadata/sources.json` catalog and per-lecture `metadata/NNNNNN.json` sidecars; anchors identify specific factual passages in the spoken region.
- For the origin and organization of the uprising, use Carolyn Fick and Crystal Eddins, and distinguish Bwa Kayiman's place in cultural memory from contested details of historical testimony.
- For the exact legal position in 1801, inspect the 1801 constitution's first three articles: Saint-Domingue remained nominally in the French empire while prohibiting slavery. 1801 **was not** a Haitian declaration of independence.
- For gender and military history, use the Library of Congress guide as an entry point; distinguish the documented lives of Sanité Bélair and others from specific stories preserved only in later commemorations.
- For the 1804 declaration, cite its surviving text, source history, and Julia Gaffield's archival discovery. Keep longer quoted texts outside the spoken region.
- For 1825 and afterward, use Gusti-Klara Gaillard-Pourchet's detailed BnF history. Distinguish the indemnity from loans, refinancing, and later payments; the amounts are historical francs, not modern-dollar estimates.
- Do not erase the 1804 massacres or imply that they were necessary to secure freedom. Do not equate all violence without examining the different aims and power relationships of the parties.

## Delivery and integration

**This is a concurrent World History contribution.** The ZIP intentionally contains only the five lecture transcripts, five metadata sidecars, one unique roadmap, and proposals for the shared `track.json` and `metadata/sources.json`. The proposals contain the new contributions only and are **not** full replacement files.

Install using the existing merge tool:

```bash
cd ~/code/ai-lectures
python tools/merge_world_history_overlay.py --zip ~/Downloads/ai-lectures-haitian-revolution-five-lectures-2026-11-14.zip
python -m pytest -q tests/test_world_history_overlay_merge.py tests/test_audio_course_tracks.py
```

Do **not** overwrite World History's shared catalogs with `unzip -o`: the merge tool validates existing IDs and combines catalog entries without discarding contributions by other authors or agents.

## Optional future expansions

- A dedicated lecture on women and household survival during the revolutionary wars, with source-rich close analysis.
- A comparative Caribbean lecture on emancipation, Guadeloupe in 1802, and antislavery politics.
- Haitian literature and memory: the revolution in nineteenth-century histories, painting, and modern scholarship.
- Haiti after 1825, including rural landholding, changing governments, international debt, and the relationship to the Dominican Republic. These deserve separate treatments instead of compressing later centuries into a claim about one cause of every problem.

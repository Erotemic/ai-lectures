# Historical portraits: Davis, Kahan, Wedin, Björck — human-life revision

This batch revises the existing History-track narration for `018000`–`021000`.
The focus is on documented personal history, lived working circumstances,
relationships, and the continuity between those experiences and the
mathematics. The original mathematical and historical display-only companions
are byte-for-byte unchanged. Lecture IDs, titles, and ordering are unchanged.

## Chandler Davis — `018000`

The biography now develops the political and intellectual life in Davis's
family, his early science-fiction writing, Harvard mentors, his marriage and
joint life with Natalie Zemon Davis, the University of Michigan dismissal,
professional exclusion, prison sentence, and eventual Toronto professorship.
The passage on his later career includes students and colleagues, literary and
editorial work, continuing activism, and his own reflections on regrets and
political reassessment. His first-person interview with Mary Gray is the main
source; the AMS remembrance and Toronto institutional records corroborate
particular details.

## William Kahan — `019000`

Kahan's 2005 oral history supplies the personal details: his family's
immigration and experiences of antisemitism; the name Velvel; building and
reading as a child; his 1953 discovery of FERUT; Meccano tape winders and
transformer calculations; mentors and colleagues; and years of disagreement
about numerical hardware, software libraries, compilers, and floating-point
standards. Those episodes are integrated where the mathematics turns from
exact residuals to actual machine arithmetic.

## Per-Åke Wedin — `020000`

His publicly documented private life is limited. This revision uses a
1977–78 Linköping institutional record to show Wedin as faculty opponent for
Lars Eldén's defense, with Björck as examiner. In Umeå, Wedin's work with
Axel Ruhe and other collaborators is followed through the research program
and doctoral mentorship. Gunilla Wikström's 2002 thesis preserves her
first-person thanks for his guidance and links directly to coauthored studies
of error propagation. The existing singular-subspace and least-squares
teaching is retained.

## Åke Björck — `021000`

The revised lecture places Björck's Linköping teaching and dissertation
examinations alongside his research, builds on his first-person recollection
of work with Gene Golub, and gives greater weight to his relationship with
Christopher Paige, editorial stewardship at BIT, reunions with numerical
analysts, and his coauthored remembrance of colleague Axel Ruhe. The material
is grounded in the 1977–78 university report, 1992 primary paper,
contemporary conference notices, and 2015 Ruhe memorial.

## Evidence and production

- New source entries are recorded in `draft-stages/tts-history/metadata/sources.json`.
- Per-lecture `metadata/018000.json`–`021000.json` include anchored historical claims; earlier anchors were preserved or updated to the revised spoken wording.
- The `track.json` spoken word counts were recomputed using `narration_extractor` at 145 words per minute.
- No audio, images, or other binary material is included.
- Validation: `pytest -q tests/test_audio_course_tracks.py`.

Documentary asymmetry is intentional: Davis and Kahan left detailed first-person
accounts, while Wedin's personal record is represented mainly by institutional
records and students' testimony. No inferred private scenes have been added.

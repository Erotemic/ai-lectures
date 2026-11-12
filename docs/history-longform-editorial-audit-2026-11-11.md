# History audio: long-form editorial audit (11 November 2026)

The 28 initial historical portraits averaged roughly 350–400 words and
ran approximately 2–3 minutes. Those entries were all too short for the
requested substantive History track. The browseable catalog now includes
only four expanded, researched lectures.

| ID | Person | Spoken words | Approx. time at 145 wpm | Disposition |
| --- | --- | ---: | ---: | --- |
| `008000` | David Hilbert | 3,936 | 27.1 min | full narration and expanded companion |
| `016000` | Tosio Kato | 3,996 | 27.6 min | full narration and expanded companion |
| `018000` | Chandler Davis | 4,074 | 28.1 min | full narration and expanded companion |
| `019000` | William Kahan | 4,046 | 27.9 min | full narration and expanded companion |

The other **24 portraits** and their reference sidecars are retained under
`draft-stages/tts-history/stubs/`. The archive manifest retains original
identifiers and ordering, without exposing them as playable lectures. The
root historical source catalog retains the readings for later expansion.

The revised narrations develop concrete mathematics and distinguish historical
authorship from later eponymous language. Key historical records include
MacTutor, University of Michigan, UC Berkeley, and the 1970 SIAM paper;
new source links are non-spoken. Mathematical examples are worked in both
the narration and companion. Current G2/G3 lectures and generated audio are
unmodified.

### Application to an existing checkout

The ZIP overlay contains the archived copies and a small migration helper.
After extraction run `python tools/archive_history_stubs.py`, since ZIP
extraction alone cannot remove the retired root-level transcript paths. This
moves any locally modified old stubs into the archive before Git staging.
The helper is idempotent. Then stage the specific History, documentation,
style, and test paths, including History deletions/moves.

### Remaining work

The four long-form lectures have not been voice-synthesized or auditioned.
The 24 archived biographies still require full historical research and
long-form writing before being promoted. No synthetic duration is claimed
from the word-count estimate; playback speed and TTS pausing affect it.

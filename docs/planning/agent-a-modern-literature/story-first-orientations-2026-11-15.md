# Literature track: story first, interpretation second

## Implemented starting point

The existing interpretation of *To Kill a Mockingbird* retains ID `001000` and
its spoken text. Three new pre-analysis story lectures have been created:
`000200`, `000500`, `000800`. They cover the childhood and Radley sequence,
Tom Robinson's trial, and the verdict's consequences respectively. Each may be
heard as a spoken narrative; together they orient a listener who has not read
or does not remember the novel. All include plot spoilers, plain-language
character introductions, and linked bibliographic evidence in JSON sidecars.

## Continuing this work across existing novels

| Existing analysis | Work | Next authoring task | Available insertion range |
|---|---|---|---|
| `002000` | *Things Fall Apart* | Tell Okonkwo's personal and community story before analyzing colonial contact and tragic form | `001001`–`001999` |
| `003000` | *Beloved* | Make a listenable plot orientation without hiding the novel's fragmented revelation; distinguish story chronology from narration order | `002001`–`002999` |
| `004000` | *The Remains of the Day* | Tell Stevens's road journey and remembered service, carefully separating his assertions from what occurs | `003001`–`003999` |
| `005000` | *The Left Hand of Darkness* | Introduce Genly Ai, Estraven, the political stakes, exile and ice journey before thematic analysis | `004001`–`004999` |
| `006000` | *One Hundred Years of Solitude* | Tell a manageable Buendía family story with carefully differentiated generations and names; multiple episodes are welcome | `005001`–`005999` |
| `007000` | *Kindred* | Follow Dana's travel, entanglement with Rufus and Alice, and return; foreground the sequence before explanation | `006001`–`006999` |
| `008000` | *Invisible Man* | Introduce the narrator's journey across institutions with its central transformations in manageable episodes | `007001`–`007999` |
| `009000` | *The Dispossessed* | Orient to the two worlds and the alternating time structure; explain relationships and main events first | `008001`–`008999` |

No pending entry should appear in the *playable* track manifest before the corresponding file exists. Preserve the analysis IDs and stable reader URLs. The old thousand-level analysis IDs are fixed; insert story lectures in the available intervening numeric space, and give room for additional episodes if the work requires them. Keep the resulting manifest in actual listening order.

## Editorial distinction

**The storytelling lecture's job** is to allow a listener to know the plot,
people, setting, turning points and ending. Tell the story in engaging original
prose, without reproducing copyrighted passages or simulating an authorized
reading of the book. Clarify confusing time order or renamed characters as
needed. When a book deliberately withholds information, it is legitimate for a
story-orientation lecture to be chronological; another approach is to reveal
facts in the work's own order. Choose deliberately, and tell listeners what
that choice is. Historical facts and fictional events must not be conflated.

**The subsequent analysis's job** is interpretation: formal design, the
historical moment, author's choices, rival readings, cultural context, and
questions the novel leaves unsettled. Analysis should be independently
understandable for a listener entering directly, but a listener following the
ordered course now has the story in mind. Story narration is not defective
because it does not also perform a full critique.

Both forms are free to use scene-setting, narration, dialogue in original
summary form, flashback, suspense, questions, digressions, and varying lengths.
The material decides the form and length. Word count metadata only records the
finished narration and must match the extraction tool.

## Technical coordination

`tests/test_modern_literature_track.py` currently hardcodes the old count of
nine and exact thousand-only lecture IDs. Agent A should not modify that
shared test under the multi-agent ownership protocol. The coordinator must
replace those fixed assumptions with comparisons against the actual manifest.
That is a functional compatibility repair, not a new quality or style rule.
The separate coordinator test patch shipped alongside the Agent A overlay
addresses these brittle assertions. Use the safe installer to preflight files.

**Review checklist (editorial, not an automated form constraint):** A listener
who has never read the book can follow who each character is, why the stakes
matter, and what happens by the ending; the telling is accurate and avoids
unsupported invented details; the critical lecture then moves naturally from
that context into interpretation.

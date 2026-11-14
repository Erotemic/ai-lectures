# 20th-Century Literature: new audio track

## Purpose

Develop a sustained collection of literary lectures on influential works published in the twentieth century. Read major novels as works of art made by particular people in particular circumstances, not as vessels for moral slogans. Aim for intellectual substance, narrative pleasure, and critical independence.

## First complete lecture

- `001000`: **To Kill a Mockingbird: The Stories a Town Tells About Itself**. Full lecture with ~43 minutes of audio-first narration, display-only critical companion, annotated source catalog, interpretive distinctions and discussion exercises. The text has spoilers.
- The organizing argument is that the Boo Radley and Tom Robinson plots use overlapping devices of misrecognition but have sharply unequal forms of harm and protection. A fair reading should follow both the structural artistry and its limitation of Black interiority.
- Read the 1930s setting and 1960 publication in their separate contexts. Track evidence, reader knowledge, and narrator knowledge independently.

## Editorial requirements

1. A lecture must develop a reading: scene-level detail, structure, narration, imagery, and alternative interpretations. An extended synopsis alone is not a lecture.
2. Integrate the author’s documented biography and the work’s composition at points relevant to interpretation. No invented private thoughts or dialogue.
3. Distinguish what is in the primary text, what a scholar argues, and what the lecturer infers.
4. When a work addresses oppression, attend to who is allowed speech and interiority; acknowledge the work’s strengths and its limits without substituting contemporary labels for textual demonstration.
5. Include contested readings when they genuinely illuminate a passage; avoid contrived symmetric arguments.
6. Provide meaningful listening pace and enough detail to sustain a serious recording. Avoid quotas, repeated recaps, abrupt changes of topic, spoken footnotes, reading-list advertisements, and cross-lecture dependencies.
7. Document historical and biographical claims in JSON sidecars; cite the primary text and reputable criticism. Do not paste protected passages from novels; quotes must be brief and necessary.
8. Verify plot details against the original work in future audits and preserve spoiler notes. Audio listening QA may follow feedback rather than block publication.

## Future candidates (not yet commissioned or allocated IDs)

| Work | Central inquiry | Possible context |
|---|---|---|
| *Things Fall Apart* — Chinua Achebe | Whose account of historical change becomes authoritative? | Igbo society, British colonialism, narrative voice |
| *Beloved* — Toni Morrison | What forms can fiction give to historical trauma and remembrance? | Slavery’s aftermath; nonlinear time |
| *The Left Hand of Darkness* — Ursula K. Le Guin | How does an imagined society expose our categories of gender and kinship? | Anthropological science fiction, estrangement |
| *One Hundred Years of Solitude* — Gabriel García Márquez | How do family stories become political history? | Memory, repetition, magical realism |
| *1984* — George Orwell | How do language and institutional power reshape the possibilities of truth? | Totalitarianism, propaganda, surveillance |
| *Kindred* — Octavia Butler | What does it mean to encounter the historical past bodily? | Slavery, family, speculative time travel |
| *Invisible Man* — Ralph Ellison | What can a first-person voice reveal about being seen through stereotypes? | Race, identity, American modernism |
| *The Remains of the Day* — Kazuo Ishiguro | How does self-deception inhabit a formally restrained narrator? | Service, memory, postwar Britain |
| *The Dispossessed* — Ursula K. Le Guin | How do competing social systems shape freedom and solidarity? | Political philosophy, anarchism, utopia |
| *Persepolis* — Marjane Satrapi | How does graphic memoir convey revolutionary childhood? | Iranian Revolution, visual narrative |
| *Never Let Me Go* — Kazuo Ishiguro | What can subdued storytelling reveal about moral normalization? | Bioethics, personhood, narrative withholding |
| *Parable of the Sower* — Octavia Butler | How are beliefs and communities made under systemic breakdown? | Dystopia, climate, inequality |

These are candidates, not a fixed syllabus. Balance geography, genre, gender, period, translation, and the authorial perspectives represented. Each lecture should stand alone even if the track eventually supports reading sequences.

## Acceptance checks

- Transcript is substantial, coherent, contains exactly one pair of spoken markers, and extracts without citations or display appendices.
- Track ID is unique and audio reader returns it through the track-specific endpoint.
- Recorded word count equals extraction output, and all non-spoken claim anchors appear uniquely in speech.
- Original literary analysis and paraphrase predominate; quoted protected text remains limited.
- Validate backend, audio UI registration, source catalog, and any relevant shared reader tests. Do not introduce permanent source-string or quotation-presence guardrails.

## First expansion completed: four distinct literary methods (14 November 2026)

Four long-form manuscripts have been added as `002000` through `005000`. They extend the track across Nigerian, African-American, British, and speculative literary traditions, and give each lecture a separate organizing formal problem.

| ID | Work | Main craft problem | Historical-biographical anchors |
|---|---|---|---|
| `002000` | Achebe, *Things Fall Apart* | Collective social description, tragic protagonist, and the abrupt colonial reclassification of a life | Achebe's Christian/Igbo childhood; broadcast work; first-manuscript journey; 1958 publication |
| `003000` | Morrison, *Beloved* | Fragmented narration, haunting, voice, and the moral pressure of an incomplete historical record | *The Black Book*, Margaret Garner, editorial work, Morrison's account of making the dead daughter speak |
| `004000` | Ishiguro, *The Remains of the Day* | First-person self-justification: narration that reveals what it denies | Childhood between remembered Japan and Britain; four-week drafting 'Crash'; 1989 Booker Prize |
| `005000` | Le Guin, *The Left Hand of Darkness* | Thought experiment and multiple viewpoint documents that alter the observer's categories | Anthropological family background; polar expedition reading; the author's later critique of gendered narration |

The companion analyses contain scene matrices, alternatives to single-thesis readings, interpretive limits, and discussion exercises. The first five track records now share one bibliography; no reader backend change is required once the original literature track overlay has been installed.

### Editorial continuation

1. Synthesize and listen to passages with complex named entities, shifts in tense, and rhetorical questions. Adjust punctuation and paragraph spacing where the voice compresses distinctions.
2. Verify specific novel passages against the edition used for listening notes; edition page numbers should never be guessed from web summaries.
3. Prioritize genuine additions to the track over revisiting the same moral subject through multiple novels. Other candidates include *One Hundred Years of Solitude*, *Kindred*, *Invisible Man*, *1984*, and *The Dispossessed*.
4. Preserve the distinction between literary interpretation and historical assertion. In particular, the historical Margaret Garner is not identical to Sethe, Le Guin's invented biology is not a factual claim about sex and gender, and Lord Darlington is fictional.
5. An independently useful discussion or classroom plan may be developed later; it should not replace the long-form listening narrative.

## Next expansion: 20th-Century Literature, lectures `006000`–`009000` (14 November 2026)

The period label supersedes the former display name **Modern Literature**. Keep `modern-literature` as the stable internal identifier, audio URL, and repository path for compatibility; it is not the public track title. A separate **21st-Century Literature** track can hold later publications if commissioned.

| ID | Novel | Narrative problem | Historical and critical emphasis |
|---|---|---|---|
| `006000` | *One Hundred Years of Solitude* (1967) | Repetition, family memory, prophecy, and the erasure of witnessed history | García Márquez's grandparents and journalism; 1928 banana workers massacre and disputed historical toll |
| `007000` | *Kindred* (1979) | An involuntary historical witness whose ancestry depends upon coerced lives | Butler's research, bicentennial 1976 setting, and limits of recovery from records |
| `008000` | *Invisible Man* (1952) | A voice claiming personhood while institutions assign identities | Ellison's musical training, institutional scripts, speech and public recognition |
| `009000` | *The Dispossessed* (1974) | Two parallel life sequences, two imperfect societies, and scientific knowledge | Le Guin's anarchist reading, the ethics of institutional criticism and intellectual openness |

**Editorial distinctions:** Do not conflate the literary massacre figures with established history; do not represent Dana as a neutral historian or Rufus's adult coercion as redemption; do not turn Ellison's organizations into a single dated political party; distinguish the fictional ansible's communication capability from instantaneous travel. Each lecture includes scene-level analysis and a display-only critical companion.

**Future period organization:** The existing list of candidate novels also includes work published in the twenty-first century. Those candidates should be reallocated to a separately named `21st-Century Literature` track when selected; their presence in the old planning backlog is not a commitment to put them here.

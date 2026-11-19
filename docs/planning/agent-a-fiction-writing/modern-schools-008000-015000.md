# Agent A: modern schools of fiction — eight-lecture unit

**Deliverable:** additional fiction-writing lectures `008000`–`015000` and track-local metadata, preserving existing `001000`–`007000` and all other agents' paths.

## Editorial decisions

- Distinguish pedagogical institutions, literary movements, academic critical traditions, method-specific commercial story systems, genres, and born-digital narrative media. Do not present the lectures as eight mutually exclusive schools.
- Follow historical development while using independent original worked examples, not imitating the prose of copyrighted writers.
- Keep each lecture standalone and around 11–13 minutes at 145 spoken words per minute. The existing fiction track's longform introductory lectures remain unchanged.
- Include criticisms and failure cases rather than ranking a favored school. Note where terms such as 'autofiction' or 'climate fiction' have disputed definitions.
- Preserve specific distinction among Afrofuturism, Indigenous futurisms, and climate fiction; avoid treating them as a homogeneous practice.
- Keep external reading links in the per-lecture display-only companions and the track-local `metadata/sources.json` reference catalog. No copyrighted passages or illustrations are embedded.
- Do not edit global catalog code, global tests, shared planning files, or other agents' tracks. The baseline's automatic discovery handles registration.

## Lectures

- 008000: Workshop pedagogy and the normative power of its criticism (Iowa, McGurl, Salesses, Saunders).
- 009000: Minimalist omission versus maximalist social/systemic accumulation (Carver/Lish, Ercolino).
- 010000: Postmodern framing, metafiction, and Oulipian procedural constraint (Barth, Duncan).
- 011000: Narrative authority and alternative centers of story (Lanser, Le Guin, Salesses).
- 012000: Screenwriting-derived plot systems, genre promises, and the limits of beat templates (Truby, Brody, Coyne).
- 013000: Autofiction and contemporary sincerity/irony problems (Doubrovsky, Dix, Kelly).
- 014000: Climate fiction, Afrofuturism, Indigenous futurisms, and social-systems imagination (Bell, Dillon, Pratt guide).
- 015000: Hypertext and interactive fiction as narrative architectures of reader agency (Montfort, Rettberg, Twine).

## Further continuation options

If future requests call for another set, expand historically grounded schools in their own right: reader-response/cognitive narratology; contemporary horror and speculative subgenres; fiction in non-English literary systems; emerging hybrid media and self-publishing. Preserve new IDs and always use scoped Agent A overlays.

## Integration checks

- Verify spoken extraction from all new manuscripts.
- Run `python tools/lecture_inventory.py` and the focused audio-track tests.
- Preflight installation with `python tools/apply_track_overlay.py a <zip> --check`; apply only with the same installer.
- Stage `content/fiction-writing/` and `docs/planning/agent-a-fiction-writing/` only for commit.

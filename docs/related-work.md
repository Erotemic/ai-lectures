# Related work: authored lectures, audio generation, and listening

Sources checked 16 November 2026. This is a selected comparison.
Capabilities below come from project documentation and original research
records. The relevance and possible directions are our interpretation.

AI Lectures combines an authored corpus with tools for publishing and listening:
editable manuscripts, pack-local source records, ordered collections, optional
speech generation, portable releases, listener state, and feedback tied to
content revisions. Related work spans several parts of that workflow. A tool
that generates an audio file, a listening server, and a study of learning
outcomes answer different questions.

## Course and source-to-audio generation

| Project and primary source | Documented scope | Relevance here |
| --- | --- | --- |
| [okcourse](https://github.com/mmacy/okcourse) | Python course generation from a title through an outline, lecture text, cover art, and audio. | A close comparison for generating audiobook-style courses. Its course model and generation stages are worth examining alongside our independently editable source packs. |
| [Google Audio Overviews](https://support.google.com/gemininotebook/answer/16212820?hl=en) | Spoken treatments of uploaded sources, with choices of format, language, focus, and length. | A reference for the source-to-listening experience and the effect of different spoken formats. A generated overview and a deliberately authored course should be evaluated for their respective purposes. |
| [Open Notebook](https://github.com/lfnovo/open-notebook) | Self-hosted organization of sources and notes, contextual chat, search, and podcast generation with configurable AI providers. | Relevant to keeping source exploration close to authoring and allowing model/service choices. Our current reader serves authored material; it does not provide this notebook research interface. |
| [Podcastfy](https://github.com/souzatharsis/podcastfy) | A Python package and CLI for turning multimodal sources into customizable, multilingual audio conversations. | Useful for comparing transcript generation, conversational formats, and speech-pipeline configuration. |
| [ebook2audiobook](https://github.com/DrewThomasson/ebook2audiobook) | Conversion of existing ebooks into audiobooks with chapters and metadata, using multiple TTS engines and voice options. | Relevant to long-form synthesis and audiobook packaging. It starts from an existing book; our content work also includes composing explanations, examples, and reading notes. |

These comparisons suggest concrete questions: how easily can an author inspect
and revise the exact spoken text, how much evidence accompanies the resulting
claims, and which changes actually require new synthesis? This repository's
manuscript, content-revision, and speech-identity boundaries make those questions
visible during authoring and revision.

## Libraries and synchronized reading

| Project and primary source | Documented scope | Relevance here |
| --- | --- | --- |
| [Audiobookshelf](https://github.com/advplyr/audiobookshelf) | A self-hosted audiobook and podcast server with browser playback, users, progress synchronization, and metadata/library management. | A useful reference for a durable listening library, especially resume behavior and library administration. Our listener names currently select shared state without authentication. |
| [Storyteller](https://storyteller-platform.dev/) | Self-hosted alignment of existing ebooks and audiobooks, producing EPUB 3 files with media overlays for synchronized reading and listening. | Relevant to alignment quality, text highlighting, and moving between reading and listening. Our current timing metadata and downloadable companions do not constitute EPUB media-overlay export. |

Prepared playback, synthesis, and authoring can be evaluated independently.
A good listening experience should remain usable when the speech backend is
unavailable; reliable progress and backups matter after generation is finished.
These are design priorities for our library.

## Research on educational audio

### PAIGE: personalized educational podcasts

Tiffany D. Do, Usama Bin Shafqat, Elsie Ling, and Nikhil Sarda.
*PAIGE: Examining Learning Outcomes and Experiences with Personalized
AI-Generated Educational Podcasts* (2024).
[Original paper record and text](https://arxiv.org/abs/2409.04645).

The study investigates converting textbook chapters into podcasts and adapting
them to learner profiles. Its abstract reports greater enjoyment than the
textbook condition and improvements from personalization that depended on the
subject. The result makes subject choice and personalization useful variables
to include in a future evaluation.

For this project, the useful distinction is between listener preference,
immediate comprehension, and learning outcomes. A pleasant voice or a completed
playback is evidence about a different thing from understanding an argument.

### Reflection prompts in interactive podcasts

Vishnu Menon, Andy Cherney, Elizabeth B. Cloude, Li Zhang, and Tiffany D. Do.
*Evaluating the Impact of LLM-guided Reflection on Learning Outcomes with
Interactive AI-Generated Educational Podcasts* (2025).
[Original paper record and text](https://arxiv.org/abs/2508.04787).

The reported study involved 36 undergraduates. Learning outcomes were similar
with and without reflection prompts, while prompts reduced perceived
attractiveness. The result supports testing the particular implementation and
listener experience when introducing interactive features.

Neither paper evaluates this library. Source accuracy, mathematical correctness,
speech completeness, usability, and learning outcomes require their own evidence;
an automated editorial review is not a substitute for all of them.

## Publishing standards

[EPUB 3.3 media overlays](https://www.w3.org/TR/epub-33/#sec-media-overlays)
describe synchronization between prerecorded narration and document text using
a subset of SMIL. They provide an established model for portable synchronized
reading, including accessibility uses. Storyteller is a concrete related
implementation. This repository currently exports its own content-pack format;
EPUB import/export and media-overlay interoperability would be additional work.

## Directions worth investigating

These are research and engineering possibilities, not implemented features or
commitments:

- Evaluate representative lectures for comprehension and delayed recall,
  separately from voice preference, playback completion, and review findings.
- Compare continuous authored narration, short source overviews, and dialogue
  when each suits the same subject and intended listener.
- Investigate EPUB media-overlay or audiobook exports while preserving source
  attribution, transcript revisions, and recording identities.
- Compare alignment methods on actual mathematical prose, proper names, and
  literary passages before promising word-accurate highlighting.
- Use the listening-library projects as references for progress, recovery, and
  accessibility behavior as the reader develops.

Lecture-specific further reading belongs with each pack's source registry and
metadata. This document concerns related systems, research, and standards for
the library as a whole.

# Curated libraries for another computer

`curated-mac-library.json` is the proposed family library: broad classics with
extra science fiction and fantasy. It uses the existing bundle selection format,
so the same file selects lectures for generation and export. Selection is a
union; repeated membership never adds a second copy of a lecture.

The choices reflect this listener's interests and complete listening sequences,
not a claim that every recording has been auditioned or quality-ranked.

## Current selection

Inventory checked 23 November 2026. Counts and duration estimates will change as
selected packs or collections grow; rerun the preview before preparing a handoff.
Hours here are spoken-word estimates at 145 words/minute, not synthesis runtime.

| Group | Entries | Estimated hours |
| --- | ---: | ---: |
| Spider-Man, Godzilla, Star Wars | 39 | 16.5 |
| American Revolution and Civil War | 14 | 4.6 |
| All three children's story packs | 213 | 16.7 |
| GPT and Claude soapboxes | 39 | 18.4 |
| Literary classics, modern fiction, epics and tales | 140 | 60.3 |
| Total | 445 | 116.5 |

At this check, **97** entries have at least one complete published recording and
**348** need complete audio. Unpublished job caches are not counted as portable
audio. The 90 Brook Road Builders stories are already complete.

The literary selection retains complete selected study routes, including their
story and analysis parts. It includes:

- Tolkien's ten-part *Lord of the Rings* study; *Dune*, *The Left Hand of
  Darkness*, *The Dispossessed*, *Contact*, *Kindred*, *Fahrenheit 451*,
  *Nineteen Eighty-Four*, *Brave New World*, and *The Handmaid's Tale*.
- Shakespeare's four tragedies, Dante, *Don Quixote*, *Paradise Lost*, *Faust*,
  Austen, the Brontës, *Frankenstein*, *Moby-Dick*, Dickens, Flaubert, Eliot,
  Tolstoy and Dostoevsky. The *Decameron* uses its compact introduction.
- *The Great Gatsby*, *Mrs Dalloway*, *The Grapes of Wrath*, *The Trial*,
  *The Stranger*, *Ficciones*, *Things Fall Apart*, *To Kill a Mockingbird*,
  *Catch-22*, *Slaughterhouse-Five*, *Beloved*, *The Remains of the Day*,
  *One Hundred Years of Solitude*, and *The Master and Margarita*.
- Full Gilgamesh and Homer routes; selected Greek myths and tragedies,
  *Beowulf*, the *Poetic Edda*, *Sir Gawain*, the linked *Arabian Nights*
  stories, *Huckleberry Finn*, *Uncle Tom's Cabin*, *The Scarlet Letter*,
  *Little Women* and *Les Misérables*. Three Kingdoms and the Shahnameh use
  compact introductions.

Journey to the West is omitted in both its short and expanded versions, along
with mathematics, mathematical history, Flatland, and the general science and
trade curricula. The children's stories have their own browsing category; the
adult literary retellings are not children's adaptations.

## Other available additions

These are **not** included in the proposed selection. Add a pack ID to `packs`
in the JSON to include one, or select individual collections/lectures.

| Pack ID | Entries | Why consider it |
| --- | ---: | --- |
| `stargate-sg1` | 27 | Another substantial science-fiction fan series |
| `dragon-ball` | 36 | Character, creator, adaptation and fandom essays |
| `cosmos-personal-voyage` | 6 | Compact retrospective on Sagan's television series |
| `living-world` | 16 | Accessible natural history, animal senses and ecosystems |
| `world-reconsidered` | 12 | Standalone essays on institutions, history and everyday reasoning |
| `comedy-history` | 34 | Comedy traditions, performance and craft |
| `fiction-writing` | 44 | Storytelling and worldbuilding craft |

The larger ancient/medieval and modern-world history tracks are also available,
but the initial selection keeps history focused on the two American wars.

## Prepare on the production machine

Preview the exact IDs and current published-audio counts without starting TTS:

```bash
python -m ailectures --library library-data bundle --repository . \
  --selection tools/deployments/curated-mac-library.json --preview
```

Choose a saved rendering recipe in Settings. Use its profile ID as
`SAVED_PROFILE_ID`; do not put private reference names or transcripts in this
shared selection. This command queues only entries lacking any complete
published recording and waits for publication:

```bash
python -m ailectures --library library-data prepare --repository . \
  --selection tools/deployments/curated-mac-library.json \
  --skip-complete --saved-profile SAVED_PROFILE_ID --tts-config /path/to/tts.toml
```

For a legacy TOML profile, use `--profile PROFILE_NAME` instead. Saved profiles
fix their voice and speed through the recipe. `--skip-complete` preserves any
complete existing voice; omit it if every lecture must use the chosen profile.
Rerunning preparation reuses matching cached blocks and existing job identity.

After preparation, create the bundle with a completeness requirement:

```bash
python -m ailectures --library library-data bundle --repository . \
  --selection tools/deployments/curated-mac-library.json --require-complete \
  --output /path/to/transfer/curated-library.zip
uv build ailectures --out-dir /path/to/transfer
```

`--require-complete` refuses to write the ZIP while any selected lecture lacks a
complete published recording. The bundle verifies copied media, keeps stable
lecture IDs, and includes published voices, sources and supported companions.
It builds a fresh subset catalog rather than shipping the production database.
Personal listening history, feedback, TTS configuration, preparation jobs and
private voice reference files stay on the production machine.

## Run on the Mac

Transfer `curated-library.zip` and the reader wheel to the Mac. The Mac needs
Python 3.11 or newer. Installation below downloads the small reader dependencies;
playback after installation needs no internet connection, TTS service, GPU,
FFmpeg or source checkout. This is a Python server installation, not a signed
macOS application. The workflow has been tested on Linux; macOS execution still
needs to be checked on the recipient's machine.

In Terminal, from the transfer folder:

```bash
python3 -m venv .reader-env
.reader-env/bin/python -m pip install ./ailectures_reader-0.1.0-py3-none-any.whl
.reader-env/bin/python -m ailectures --library ./curated-library restore ./curated-library.zip
.reader-env/bin/python -m ailectures --library ./curated-library serve \
  --installed-only --playback-only --port 8001
```

Open `http://localhost:8001/`. Stop the server with Control-C and rerun the last
command next time; restore runs only once into a new directory. To listen from
other devices on the same network, add `--host 0.0.0.0` and open the Mac's network
address on those devices.

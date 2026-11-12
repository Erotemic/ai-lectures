# World History audio lectures

This is a separate, audio-first collection within AI Lectures. It does not
change the mathematical curricula or their course graph. Open the **World
History** tab in the audio reader, or visit `/audio?track=world-history`.

The substantive, standalone lectures are:

- **001000 · The Epic of Gilgamesh: The King Who Could Not Defeat Death** —
  narrative, archaeology, transmission of the text, flood traditions, and mortality.
- **002000 · Mary Leakey: Reading the Footprints of Deep Time** —
  early human evolution, field methods, Olduvai Gorge, Laetoli, and the
  attribution of team discoveries.
- **003000 · Uruk: How a City Learned to Count** —
  late fourth-millennium urbanism, irrigation, institutions, proto-cuneiform,
  regional exchange, and the later traditions of Gilgamesh.
- **004000 · Mansa Musa: Gold, Pilgrimage, and the Empire of Mali** —
  Sundiata and the formation of Mali, trade and political power, the 1324–1325
  pilgrimage, Cairo diplomacy, Timbuktu, and the historical sources.
- **005000 · Hatshepsut: The Woman Who Became King of Egypt** —
  Eighteenth Dynasty kingship, the co-regency with Thutmose III, royal imagery,
  Deir el-Bahri, Karnak, the expedition to Punt, and later monument erasure.
- **006000 · Fu Hao: The General, the Oracle Bones, and the Shang World** —
  Shang kingship, divination and early writing, military leadership, bronze
  craftsmanship, ancestral ritual, sacrifice, and the excavated tomb at Anyang.
- **007000 · The Austronesian Expansion: How People Crossed an Ocean World** —
  Taiwan and Island Southeast Asia, Near Oceania and Lapita, navigation,
  Micronesia, Polynesian settlement, Madagascar, and long-distance contact.

The source Markdown files contain a spoken lecture between explicit markers.
Historical notes and references after the spoken region are for reading and
editorial review; they are not synthesized. Non-spoken reading links for the
reader live in `metadata/`, with stable IDs in `metadata/sources.json`.

`track.json` lists only lectures ready for sustained listening. The manifest
order is a browsing order, not a required playback sequence. New lectures can
be added by creating a six-digit-prefixed transcript, manifest entry, and
optional reading metadata. Use a new identifier within this track; IDs may
be reused across other tracks because player, speech cache, progress, and
feedback are namespaced by track.

Run `make serve` at the repository root, and select **World History** in the
reader. The server synthesizes audio on demand with the existing TTS profiles.

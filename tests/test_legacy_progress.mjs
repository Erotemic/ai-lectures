import assert from "node:assert/strict";
import {
  legacyPositions,
  approximateLegacyPosition,
} from "../ailectures/static/legacy-progress.mjs";

const settings = {
  track: "music-theory",
  profile: "kokoro",
  voice: "af_alloy",
  speed: 1,
};
const durationKey =
  "dkps-audio-durations-music-theory-001000-" +
  encodeURIComponent(JSON.stringify([123, 600, 4, "paragraph-v1", settings]));
const values = new Map([
  ["dkps-audio-page-music-theory-001000", "2"],
  [durationKey, "[10,20,30,40]"],
  ["dkps-audio-page-world-history-002000", "1"],
  ["dkps-audio-page-g2-001000", "-1"],
  ["dkps-audio-page-g2-002000", "broken"],
]);
const storage = {
  length: values.size,
  key: (i) => [...values.keys()][i],
  getItem: (key) => values.get(key),
};
const positions = legacyPositions(storage);
assert.equal(positions.length, 2);
const selected = positions.find((p) => p.lecture_id === "music-theory:001000");
assert.equal(
  selected.revision,
  null,
  "An old page selection cannot establish a source revision",
);
assert.equal(selected.recording_id, null);
assert.equal(selected.legacy.snapshots[0].settings.voice, "af_alloy");
assert.equal(selected.legacy.page_index, 2);
assert.deepEqual(selected.legacy.snapshots[0].durations, [10, 20, 30, 40]);
const recording = {
  pages: ["first", "second"],
  segments: [
    { index: 0, duration: 30 },
    { index: 1, duration: 30 },
  ],
};
assert.deepEqual(approximateLegacyPosition(selected, recording), {
  index: 1,
  seconds: 0,
});
const withoutLayout = positions.find(
  (p) => p.lecture_id === "world-history:002000",
);
assert.deepEqual(approximateLegacyPosition(withoutLayout, recording), {
  index: 1,
  seconds: 0,
});
assert.equal(
  values.get("dkps-audio-page-music-theory-001000"),
  "2",
  "Import must leave original browser records intact",
);
console.log(
  "Legacy page selections retain unknown revisions, old settings and original storage",
);

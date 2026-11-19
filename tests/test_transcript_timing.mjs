import assert from "node:assert/strict";
import {
  speechSegments,
  wordAtTime,
  timeAtWord,
  sentenceAtWord,
} from "../ailectures/static/transcript.mjs";

const text =
  "First measured chunk. Second example follows.\n\nA final concluding observation.";
const sentences = speechSegments(text);
assert.equal(
  sentences.join(""),
  text,
  "Sentence navigation must preserve every spoken character",
);
const segment = {
  duration: 20,
  timings: {
    chunks: [
      { start: 0, end: 15, words: 3 },
      { start: 16, end: 20, words: 7 },
    ],
  },
};
assert.equal(sentenceAtWord(sentences, wordAtTime(text, segment, 10)), 0);
assert.equal(
  wordAtTime(text, segment, 15.5),
  3,
  "Silence between chunks must not advance the text",
);
assert.equal(
  timeAtWord(text, segment, 3),
  16,
  "Seeking the next chunk skips its preceding silence",
);
for (const word of [0.5, 2, 4, 8])
  assert.ok(
    Math.abs(
      wordAtTime(text, segment, timeAtWord(text, segment, word)) - word,
    ) < 1e-8,
  );
assert.equal(wordAtTime(text, { duration: 20 }, 10), 5);
assert.equal(
  wordAtTime(text, { duration: 20, timings: { chunks: [null] } }, 10),
  5,
  "Bad optional timing metadata must retain estimated navigation",
);
assert.equal(
  wordAtTime(
    text,
    { duration: 20, timings: { chunks: [{ start: 0, end: 25, words: 10 }] } },
    10,
  ),
  5,
);
console.log(
  "Transcript navigation preserves text and respects chunk timing and silence",
);

const { transcriptBlocks, recordingTranscriptParts, pageSpeechSegments } =
  await import("../ailectures/static/transcript.mjs");
const structuredText =
  "Shared heading\nBody words. Another sentence.\n\nShared heading\nFinal words.";
const headings = [
  { start: 0, end: 2, level: 1, spoken: true, text: "Shared heading" },
  { start: 2, end: 2, level: 2, spoken: false, text: "Visible caption" },
  { start: 6, end: 8, level: 2, spoken: true, text: "Shared heading" },
];
const structuredRow = {
  transcript: structuredText,
  transcript_headings: headings,
};
const structuredRecording = {
  pages: [
    "Shared heading\nBody words. Another sentence.\n\nShared",
    "heading\nFinal words.",
  ],
};
const parts = structuredRecording.pages.map((_, i) =>
  recordingTranscriptParts(structuredRow, structuredRecording, i),
);
assert.equal(parts[0].filter((p) => p.spoken === false).length, 1);
assert.equal(parts[1][0].kind, "heading");
assert.equal(parts[1][0].level, 2);
for (let i = 0; i < 2; i++) {
  assert.equal(
    pageSpeechSegments(structuredRow, structuredRecording, i).join(""),
    structuredRecording.pages[i],
  );
  assert.deepEqual(
    parts[i].filter((p) => p.spoken !== false).map((p) => p.sentence),
    pageSpeechSegments(structuredRow, structuredRecording, i).map((_, i) => i),
  );
}
assert.ok(
  !pageSpeechSegments(structuredRow, structuredRecording, 0)
    .join("")
    .includes("Visible caption"),
);
assert.equal(
  recordingTranscriptParts(
    { ...structuredRow, transcript: "Different revision." },
    structuredRecording,
    0,
  ).filter((p) => p.kind === "heading").length,
  0,
);
const duplicate =
  "Shared heading\n\nWe discuss Shared heading here.\n\nShared heading\n\nLast sentence.";
const blocks = transcriptBlocks(duplicate, [
  { start: 0, end: 2, level: 1 },
  { start: 7, end: 9, level: 2 },
]);
assert.equal(blocks.filter((p) => p.kind === "heading").length, 2);
assert.ok(
  blocks.some(
    (p) => p.kind === "body" && p.text.includes("discuss Shared heading"),
  ),
);
assert.equal(blocks.map((p) => p.text).join(""), duplicate);
console.log(
  "Structured transcript headings preserve speech, paragraph offsets, paginated titles, captions, and seek indexes.",
);

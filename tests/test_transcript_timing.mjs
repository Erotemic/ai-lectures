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

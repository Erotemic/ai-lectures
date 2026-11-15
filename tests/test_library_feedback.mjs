import assert from "node:assert/strict";
import {
  feedbackThreads,
  changedPassages,
} from "../ailectures/static/feedback.mjs";

const original = {
  type: "submission",
  id: "one",
  transcript_snapshot: "An old explanation.",
  revision: "old",
};
const revision = {
  type: "status",
  feedback_id: "one",
  status: "resolved",
  addressed_revision: "new",
};
// Imports may list a status before the submission. Resolution retains its
// original transcript and does not turn a new comment into resolved feedback.
const threads = feedbackThreads([
  revision,
  original,
  { type: "submission", id: "two" },
]);
assert.equal(threads[0].status, "open");
assert.equal(threads[1].status, "resolved");
assert.equal(threads[1].submission.revision, "old");
assert.equal(threads[1].history[0].addressed_revision, "new");
assert.equal(
  feedbackThreads([original, revision, { ...revision, status: "reopened" }])[0]
    .status,
  "reopened",
);

const before =
  "Opening.\n\nOld example.\n\nShared bridge.\n\nOld ending.\n\nReading notes.";
const after =
  "Opening.\n\nNew example.\n\nShared bridge.\n\nNew ending.\n\nReading notes.";
assert.deepEqual(changedPassages(before, after), {
  changed: true,
  before: "Old example.\n\nShared bridge.\n\nOld ending.",
  after: "New example.\n\nShared bridge.\n\nNew ending.",
});
assert.equal(changedPassages(after, after).changed, false);
assert.equal(changedPassages("Opening.", "Opening.\n\nAddition.").before, "");
console.log(
  "Feedback keeps original context, explicit status history and changed transcript spans",
);

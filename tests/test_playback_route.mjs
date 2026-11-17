import assert from "node:assert/strict";
import { listeningCourse, followingLecture } from "../ailectures/static/playback-route.mjs";

const a = "literature:001000", b = "literature:002000", c = "literature:003000";
const archive = { id: "literature:main", role: "archive", lectures: [a, b, c] };
const survey = { id: "literature:survey", role: "main", lectures: [a, b] };
const branch = { id: "literature:topic", role: "deep_dive", lectures: [a, c] };
const courses = [archive, survey, branch];
assert.equal(listeningCourse(courses, a, branch.id, survey.id).id, branch.id);
assert.equal(listeningCourse(courses, a, "removed", branch.id).id, branch.id);
assert.equal(listeningCourse(courses, c, survey.id).id, branch.id);
assert.equal(listeningCourse(courses, a).id, survey.id);
assert.equal(listeningCourse(courses, "other:001000", branch.id), null);
assert.equal(listeningCourse([archive], a).id, archive.id);
assert.deepEqual(followingLecture(courses, branch.id, a), { course: branch, index: 0, next: c });
assert.deepEqual(followingLecture(courses, survey.id, a), { course: survey, index: 0, next: b });
assert.equal(followingLecture(courses, branch.id, c).next, null);
// A removed/foreign playing lecture must not wrap to the collection's first item.
assert.deepEqual(followingLecture(courses, branch.id, b), { course: null, index: -1, next: null });
assert.deepEqual(followingLecture(courses, "removed", a), { course: null, index: -1, next: null });
console.log("Playback follows the selected route, with honest end and missing-membership behavior");

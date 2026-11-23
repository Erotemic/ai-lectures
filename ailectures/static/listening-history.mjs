import { followingLecture, listeningCourse } from "./playback-route.mjs";

// Progress retains the latest checkpoint per lecture, including completed items.
export function recentListening(progress) {
  return Object.values(progress).sort((a, b) =>
    (b.updated_at || "").localeCompare(a.updated_at || ""),
  );
}

export function historyRoute(position, courses) {
  // A saved route must not silently become a different sequence after removal.
  const course = position.course_id
    ? courses.find((candidate) => candidate.id === position.course_id
      && candidate.lectures.includes(position.lecture_id))
    : listeningCourse(courses, position.lecture_id);
  return followingLecture(courses, course?.id, position.lecture_id);
}

// Playback order belongs to the selected collection, independently of browsing.
export function listeningCourse(courses, lectureId, ...preferences) {
  const contains = (course) => course?.lectures.includes(lectureId);
  for (const id of preferences) {
    const course = courses.find((candidate) => candidate.id === id);
    if (contains(course)) return course;
  }
  const main = courses.find((course) =>
    course.id === lectureId.split(":")[0] + ":main" && contains(course));
  const curated = courses.find((course) => course.role === "main" && contains(course)) ||
    courses.find((course) => course.role && course.role !== "archive" && contains(course));
  return curated || main || courses.find(contains) || null;
}

export function followingLecture(courses, courseId, lectureId) {
  const course = courses.find((candidate) => candidate.id === courseId);
  const index = course?.lectures.indexOf(lectureId) ?? -1;
  if (index < 0) return { course: null, index: -1, next: null };
  return { course, index, next: course.lectures[index + 1] || null };
}

#!/usr/bin/env python3
"""Report route coverage and listening time without producing audio or media."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from statistics import median
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from ailectures.catalog import repository_track


def audit_repository(root):
    root = Path(root)
    packs = []
    for directory in sorted(
        [*root.glob("draft-stages/tts-*"), *root.glob("content/*")]
    ):
        if directory.is_dir() and (
            (directory / "track.json").exists()
            or any(directory.glob("[0-9][0-9][0-9][0-9][0-9][0-9]-*.md"))
        ):
            packs.append((directory, repository_track(directory)))
    lectures = {key: row for _, pack in packs for key, row in pack["lectures"].items()}
    courses = {key: row for _, pack in packs for key, row in pack["courses"].items()}
    namespaces = {pack["id"] for _, pack in packs}
    minutes = {
        key: len(row["transcript"].split()) / 145 for key, row in lectures.items()
    }
    named_sessions = {}
    linked_topics = {}
    for course in courses.values():
        for chapter in course.get("chapters", []):
            if chapter.get("collection"):
                for key in chapter["lectures"]:
                    linked_topics.setdefault(key, set()).add(chapter["collection"])
            for session in chapter.get("sessions", []):
                for key in session["lectures"]:
                    named_sessions.setdefault(key, []).append(
                        dict(
                            collection=course["id"],
                            title=session["title"],
                            parts=len(session["lectures"]),
                            estimated_minutes=round(
                                sum(minutes.get(part, 0) for part in session["lectures"]),
                                1,
                            ),
                        )
                    )
    errors = []
    optional = set()
    stops = []
    inventory = []
    short_adult_entries = []
    adult_minutes = []
    children_entries = 0
    for directory, pack in packs:
        errors.extend(
            warning for warning in pack["warnings"] if "navigation.json" in warning
        )
        curated = [
            course
            for course in pack["courses"].values()
            if course.get("role") != "archive"
        ]
        placed = {key for course in curated for key in course["lectures"]}
        unplaced = sorted(set(pack["lectures"]) - placed)
        if unplaced:
            errors.append(
                f"{pack['id']}: manuscripts outside all curated routes: {unplaced}"
            )
        children = "children" in pack["courses"][f"{pack['id']}:main"].get(
            "audiences", []
        )
        durations = [minutes[key] for key in pack["lectures"]]
        if children:
            children_entries += len(durations)
        else:
            adult_minutes.extend(durations)
            short_adult_entries.extend(
                dict(
                    id=key,
                    title=row["title"],
                    pack=pack["id"],
                    estimated_minutes=round(minutes[key], 1),
                    named_sessions=named_sessions.get(key, []),
                    linked_topic_routes=sorted(linked_topics.get(key, [])),
                )
                for key, row in pack["lectures"].items()
                if minutes[key] < 10
            )
        inventory.append(
            dict(
                id=pack["id"],
                directory=directory.relative_to(root).as_posix(),
                title=pack["title"],
                manuscripts=len(pack["lectures"]),
                estimated_hours=round(
                    sum(minutes[key] for key in pack["lectures"]) / 60, 2
                ),
                custom_navigation=(directory / "navigation.json").is_file(),
                duration_review=dict(
                    audience="children" if children else "adult",
                    under_ten_minutes=sum(value < 10 for value in durations),
                    under_five_minutes=sum(value < 5 for value in durations),
                    over_sixty_minutes=sum(value > 60 for value in durations),
                    median_minutes=round(median(durations), 1) if durations else 0,
                ),
                root_collections=[
                    course["id"] for course in curated if not course.get("parent_id")
                ],
                unplaced=unplaced,
            )
        )
        for course in pack["courses"].values():
            for key in course["lectures"]:
                if key not in lectures:
                    if key.split(":")[0] in namespaces:
                        errors.append(
                            f"{course['id']}: missing lecture {key} in an available pack"
                        )
                    else:
                        optional.add(key)
            links = (
                course.get("related_collections", [])
                + course.get("preparation_collections", [])
                + [
                    chapter["collection"]
                    for chapter in course.get("chapters", [])
                    if chapter.get("collection")
                ]
            )
            for key in links:
                if key not in courses:
                    if key.split(":")[0] in namespaces:
                        errors.append(
                            f"{course['id']}: missing collection {key} in an available pack"
                        )
                    else:
                        optional.add(key)
            for chapter in course.get("chapters", []):
                stops.append(
                    dict(
                        course=course["id"],
                        title=chapter["title"],
                        items=len(chapter["lectures"]),
                        estimated_minutes=round(
                            sum(minutes.get(key, 0) for key in chapter["lectures"]), 1
                        ),
                        sessions=[
                            dict(
                                title=session["title"],
                                items=len(session["lectures"]),
                                estimated_minutes=round(
                                    sum(
                                        minutes.get(key, 0)
                                        for key in session["lectures"]
                                    ),
                                    1,
                                ),
                            )
                            for session in chapter.get("sessions", [])
                        ],
                    )
                )
    return dict(
        audio_packs=len(packs),
        audio_manuscripts=len(lectures),
        estimated_audio_hours=round(sum(minutes.values()) / 60, 2),
        collections=len(courses),
        inventory=inventory,
        survey_stops=stops,
        duration_review=dict(
            words_per_minute=145,
            note="Duration is descriptive, not an acceptance gate. A linked topic or named session does not establish that an entry is an overview or a combined lecture.",
            adult_entries=len(adult_minutes),
            adult_entries_under_ten_minutes=sum(value < 10 for value in adult_minutes),
            adult_entries_under_five_minutes=sum(value < 5 for value in adult_minutes),
            adult_entries_over_sixty_minutes=sum(value > 60 for value in adult_minutes),
            children_entries_excluded=children_entries,
            short_adult_entries=short_adult_entries,
        ),
        optional_unavailable_references=sorted(optional),
        errors=errors,
    )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--repository", type=Path, default=Path(__file__).resolve().parents[1]
    )
    parser.add_argument(
        "--output", type=Path, help="Write a descriptive JSON snapshot."
    )
    args = parser.parse_args()
    report = audit_repository(args.repository.resolve())
    if args.output:
        args.output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    else:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    if report["errors"]:
        for error in report["errors"]:
            print(error, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

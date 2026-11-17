"""Pack-local listening routes; manuscripts and their identities stay independent."""

from copy import deepcopy

from .core import name, qualified, read_json
from .organization import collection_metadata


def route_collections(
    path, main, *, known, lecture_sections=None, previous=None, issue=lambda msg: None
):
    """Expand authored navigation into portable course records.

    Optional navigation is published atomically. A bad update keeps the previous
    routes, or the original collection on first discovery, without hiding audio.
    Cross-pack lecture and collection references may be installed later.
    """
    if not path.exists():
        return {main["id"]: main}
    namespace = main["id"].split(":")[0]

    def reference(value):
        if not isinstance(value, str):
            raise ValueError("route references must be strings")
        return qualified(value if ":" in value else f"{namespace}:{value}")

    def members(values):
        if not isinstance(values, list):
            raise ValueError("route lectures must be a list")
        result = [reference(value) for value in values]
        for key in result:
            if key.startswith(namespace + ":") and key not in known:
                raise ValueError(f"unknown local lecture {key}")
        return result

    def selection(entry):
        if "include_sections" not in entry:
            return members(entry.get("lectures", []))
        if "lectures" in entry or "chapters" in entry or "sessions" in entry:
            raise ValueError("use either include_sections or an explicit lecture order")
        sections = entry["include_sections"]
        if (
            not isinstance(sections, list)
            or not sections
            or not all(isinstance(section, str) and section for section in sections)
        ):
            raise ValueError(
                "include_sections must be a nonempty list of section names"
            )
        return [
            key
            for key in main["lectures"]
            if (lecture_sections or {}).get(key) in sections
        ]

    try:
        plan = read_json(path)
        if not isinstance(plan, dict) or not isinstance(plan.get("collections"), list):
            raise ValueError("expected an object with a collections list")
        courses = {main["id"]: deepcopy(main)}
        for entry in plan["collections"]:
            if not isinstance(entry, dict):
                raise ValueError("collection must be an object")
            local_id = name(entry["id"])
            key = f"{namespace}:{local_id}"
            if key in courses:
                raise ValueError(f"duplicate or reserved collection {key}")
            if not isinstance(entry.get("title"), str) or not entry["title"].strip():
                raise ValueError(f"missing title for {key}")
            role = entry.get("role", "deep_dive")
            if role not in {"main", "deep_dive", "hub"}:
                raise ValueError(f"invalid collection role for {key}")
            course = dict(
                id=key,
                title=entry["title"],
                summary=entry.get("summary", ""),
                background=entry.get("assumed_background", main.get("background", "")),
                role=role,
                **collection_metadata({**main, **entry, "browse_sections": entry.get("browse_sections"), "guide_for": entry.get("guide_for")}, namespace),
            )
            if "chapters" in entry:
                if "lectures" in entry or not isinstance(entry["chapters"], list):
                    raise ValueError(f"use either chapters or lectures in {key}")
                chapters = []
                for chapter in entry["chapters"]:
                    if not isinstance(chapter, dict) or not isinstance(
                        chapter.get("title"), str
                    ):
                        raise ValueError(f"invalid chapter in {key}")
                    part = dict(title=chapter["title"])
                    if "sessions" in chapter:
                        if "lectures" in chapter or not isinstance(
                            chapter["sessions"], list
                        ):
                            raise ValueError(
                                f"use either sessions or lectures in a chapter of {key}"
                            )
                        sessions = []
                        for session in chapter["sessions"]:
                            if not isinstance(session, dict) or not isinstance(
                                session.get("title"), str
                            ):
                                raise ValueError(f"invalid listening session in {key}")
                            session_members = members(session["lectures"])
                            if not session_members:
                                raise ValueError(f"empty listening session in {key}")
                            sessions.append(
                                dict(title=session["title"], lectures=session_members)
                            )
                        if not sessions:
                            raise ValueError(f"empty session list in {key}")
                        part["sessions"] = sessions
                        part["lectures"] = [
                            member
                            for session in sessions
                            for member in session["lectures"]
                        ]
                    else:
                        part["lectures"] = selection(chapter)
                    if chapter.get("collection"):
                        part["collection"] = reference(chapter["collection"])
                    chapters.append(part)
                course["chapters"] = chapters
                course["lectures"] = [
                    item for part in chapters for item in part["lectures"]
                ]
            else:
                course["lectures"] = selection(entry)
            if len(set(course["lectures"])) != len(course["lectures"]):
                raise ValueError(f"duplicate lecture in {key}")
            if entry.get("parent"):
                course["parent_id"] = reference(entry["parent"])
            course["related_collections"] = [
                reference(value) for value in entry.get("related_collections", [])
            ]
            course["preparation_collections"] = [
                reference(value) for value in entry.get("preparation_collections", [])
            ]
            courses[key] = course
        default = reference(plan["default_collection"])
        if default == main["id"] or default not in courses:
            raise ValueError("default_collection must identify an authored route")
        if courses[default].get("parent_id"):
            raise ValueError("default_collection must be a top-level route")
        courses[main["id"]].update(
            title=plan.get(
                "archive_title", main["title"] + " · Complete original sequence"
            ),
            role="archive",
            parent_id=default,
        )
        for course in courses.values():
            links = (
                course.get("related_collections", [])
                + course.get("preparation_collections", [])
                + [
                    part["collection"]
                    for part in course.get("chapters", [])
                    if part.get("collection")
                ]
                + [target for section in course.get("browse_sections", []) for target in section["collections"]]
            )
            for target in links:
                if target.startswith(namespace + ":") and target not in courses:
                    raise ValueError(f"unknown local collection {target}")
        # Parents are pack-local so a portable release never loses its hierarchy.
        for key, course in courses.items():
            seen = {key}
            parent = course.get("parent_id")
            while parent:
                if parent not in courses or parent in seen:
                    raise ValueError(f"missing or cyclic parent for {key}")
                seen.add(parent)
                parent = courses[parent].get("parent_id")
        return courses
    except (OSError, ValueError, KeyError, TypeError) as exc:
        issue(f"navigation.json: {exc}; retaining available collections")
        if not previous:
            return {main["id"]: main}
        restored = deepcopy(previous)
        # A broken route edit must not keep newly indexed manuscripts out of the
        # original full collection while its last usable branches are retained.
        old_main = restored.get(main["id"], {})
        restored[main["id"]] = {
            **old_main,
            **main,
            "title": old_main.get("title", main["title"]),
        }
        return restored

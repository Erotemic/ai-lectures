"""Read the original syllabus without importing deck or rendering modules."""

from pathlib import Path
import json

from .core import BEGIN, digest, lecture_revision, text_digest
from .manuscripts import spoken_transcript
from .descriptions import description_fields


def presentation_pack(repository):
    import yaml  # Only the optional repository adapter needs YAML.

    root = Path(repository) / "lectures"
    plan = yaml.safe_load((root / "index.yaml").read_text())["lectures"]
    ordered, pending = [], dict(plan)
    while pending:
        available = next(
            (
                key
                for key, row in pending.items()
                if all(p in ordered for p in row.get("requires", []))
            ),
            None,
        )
        if available is None:
            raise ValueError("Missing or cyclic presentation prerequisite")
        ordered.append(available)
        pending.pop(available)
    lectures, relationships = {}, []
    for key in ordered:
        entry = plan[key]
        folders = list(root.glob("[0-9]" * 6 + "_" + key))
        if (root / key).is_dir():
            folders.append(root / key)
        if len(folders) != 1:
            raise ValueError(f"Expected one presentation source folder for {key}")
        folder = folders[0]
        source = (folder / "lecture.md").read_text()
        provenance = folder / "provenance.yaml"
        transcript = ""
        diagnostic = None
        try:
            transcript = spoken_transcript(source, str(folder / "lecture.md"))
        except ValueError as exc:
            diagnostic = str(exc)
        row = dict(
            id="g1:" + entry["deck"],
            namespace="g1",
            kind="audio" if transcript else "presentation",
            title=entry["title"],
            transcript=transcript,
            spoken_sha256=text_digest(transcript),
            source=source,
            metadata={
                "provenance": (
                    yaml.safe_load(provenance.read_text())
                    if provenance.exists()
                    else {}
                )
            },
            sources={},
            recordings=[],
            section=entry.get("series", ""),
            deck=entry["deck"],
            aliases=["g1:" + folder.name],
        )
        if diagnostic:
            row["metadata"]["narration_diagnostic"] = diagnostic
        else:
            row["metadata"]["source_format"] = (
                "spoken-region-v1" if BEGIN in source else "scene-narration-v1"
            )
        row.update(description_fields(row))
        readings = folder / "resources.yaml"
        if readings.is_file():
            try:
                data = yaml.safe_load(readings.read_text())
                for resource in data.get("resources", []):
                    if not isinstance(resource, dict):
                        continue
                    source = json.loads(json.dumps(resource, default=str))
                    source["checked_on"] = str(data.get("checked_on", "not recorded"))
                    source_id = "reading-" + digest(source)[:20]
                    row["sources"][source_id] = source
                    row["metadata"].setdefault("related_resources", []).append(
                        {"source_id": source_id, "reason": resource.get("why", "")}
                    )
            except (
                OSError,
                ValueError,
                TypeError,
                AttributeError,
                yaml.YAMLError,
            ) as exc:
                row["metadata"]["reading_diagnostic"] = str(exc)
        row["revision"] = lecture_revision(row)
        lectures[row["id"]] = row
        for parent in entry.get("requires", []):
            relationships.append(
                {
                    "from": row["id"],
                    "to": "g1:" + plan[parent]["deck"],
                    "type": "soft_depends_on",
                }
            )
    course = dict(
        id="g1:main",
        title="Animated Mathematics",
        summary="Original mathematical presentations, handouts, and narrated videos.",
        lectures=list(lectures),
    )
    return dict(
        id="g1",
        title=course["title"],
        lectures=lectures,
        courses={course["id"]: course},
        relationships=relationships,
        extra_files={},
    )

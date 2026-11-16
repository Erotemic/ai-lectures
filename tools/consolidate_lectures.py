#!/usr/bin/env python3
"""Compose reviewed lecture groups into single manuscripts, with a dry-run default.

The plan supplies editorial boundaries; this tool never chooses groups by length.
It preserves narration, companions, source claims and component metadata. Removed
parts are not redirects or hidden entries. Git remains the history of the sources.
"""
from __future__ import annotations

import argparse
from copy import deepcopy
from datetime import date
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
import unicodedata
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from ailectures.catalog import repository_track
from ailectures.core import BEGIN, END, extract_text


def pretty(value):
    return json.dumps(value, ensure_ascii=False, indent=2) + "\n"


def slug(value):
    value = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")[:110].rstrip("-")


def qualified(namespace, key):
    return key if ":" in key else namespace + ":" + key


def compose(title, parts):
    spoken, companions = [], []
    for part_title, text in parts:
        # Validate before splitting, including the exact single-marker contract.
        extract_text(text)
        prefix, remainder = text.split(BEGIN)
        body, suffix = remainder.split(END)
        body = body.strip()
        body = re.sub(r"\A#[^\n]*\n+", "", body, count=1)
        body = re.sub(r"(?m)^(#{1,5}) ", r"\1# ", body)
        spoken.append("## " + part_title + "\n\n" + body)
        prefix = re.sub(r"\A#[^\n]*\n+", "", prefix.strip(), count=1).strip()
        outside = "\n\n".join(piece for piece in (prefix, suffix.strip()) if piece)
        if outside:
            outside = re.sub(r"(?m)^(#{1,4}) ", r"\1## ", outside)
            companions.append("### " + part_title + "\n\n" + outside)
    result = "# " + title + "\n\n" + BEGIN + "\n\n# " + title + "\n\n"
    result += "\n\n".join(spoken) + "\n\n" + END + "\n"
    if companions:
        result += "\n## Companions, sources, and study material (not spoken)\n\n" + "\n\n".join(companions) + "\n"
    extract_text(result)
    return result


def merge_metadata(inputs, survivor, filename, provenance):
    result = deepcopy(inputs[0])
    for data in inputs[1:]:
        for field, value in data.items():
            if isinstance(value, list):
                target = result.setdefault(field, [])
                if not isinstance(target, list):
                    continue
                for entry in value:
                    if entry not in target:
                        target.append(deepcopy(entry))
            elif field not in result:
                result[field] = deepcopy(value)
    result.update(lecture_id=survivor, transcript=filename)
    result["consolidation"] = provenance
    return result


def prepare(root, plan):
    root = Path(root).resolve()
    packs = {}
    courses = {}
    for directory in sorted([*root.glob("draft-stages/tts-*"), *root.glob("content/*")]):
        if not directory.is_dir() or not ((directory / "track.json").is_file() or any(directory.glob("[0-9][0-9][0-9][0-9][0-9][0-9]-*.md"))):
            continue
        pack = repository_track(directory)
        navigation_warnings = [warning for warning in pack["warnings"] if "navigation.json" in warning]
        if navigation_warnings:
            raise ValueError("Fix route metadata before consolidating: " + "; ".join(navigation_warnings))
        packs[pack["id"]] = (directory, pack)
        courses.update(pack["courses"])
    for key, order in plan.get("collection_orders", {}).items():
        if key not in courses or len(set(order)) != len(order):
            raise ValueError(f"Invalid reviewed collection order: {key}")
        if any(member.split(":")[0] not in packs or member not in packs[member.split(":")[0]][1]["lectures"] for member in order):
            raise ValueError(f"Missing source in reviewed collection order: {key}")
        courses[key] = {**courses[key], "lectures": order}
    groups = plan.get("groups", [])
    if not isinstance(groups, list) or not groups:
        raise ValueError("The plan must contain reviewed groups")
    observed, writes, deletes, replacements, summaries = {}, {}, set(), {}, []
    by_pack = {}
    try:
        revision = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=root, text=True, stderr=subprocess.DEVNULL).strip()
    except subprocess.CalledProcessError:
        revision = "unrecorded"

    def read(path):
        data = path.read_bytes()
        observed.setdefault(path, data)
        return data.decode("utf-8")

    def read_track(directory, pack):
        path = directory / "track.json"
        if path.exists():
            return json.loads(read(path))
        main = pack["courses"][pack["id"] + ":main"]
        files = {file.name[:6]: file.name for file in directory.glob("[0-9][0-9][0-9][0-9][0-9][0-9]-*.md")}
        return dict(id=pack["id"], title=pack["title"], categories=main.get("categories", []),
                    lectures=[dict(id=key.split(":")[1], file=files[key.split(":")[1]], title=pack["lectures"][key]["title"], section=pack["lectures"][key].get("section", "")) for key in main["lectures"]])

    for group in groups:
        namespace = group["pack"]
        directory, pack = packs[namespace]
        if "children" in pack["courses"][namespace + ":main"].get("audiences", []):
            raise ValueError("Children's stories are outside this consolidation")
        keys = [qualified(namespace, key) for key in group["lectures"]]
        if len(keys) < 2 or len(set(keys)) != len(keys):
            raise ValueError("A group needs at least two distinct source lectures")
        if any(key.split(":")[0] != namespace for key in keys):
            raise ValueError("A manuscript group must stay within its source pack")
        if any(key in replacements for key in keys):
            raise ValueError("Source merge groups must be disjoint")
        for course in courses.values():
            if course.get("role") == "archive":
                continue
            selected = set(keys).intersection(course["lectures"])
            if selected and len(selected) != len(keys) and not group.get("allow_route_expansion"):
                raise ValueError(f"{group['title']}: partial selection in {course['id']}; review the changed coverage explicitly")
        track_path = directory / "track.json"
        track = read_track(directory, pack)
        entries = {row["id"]: row for row in track["lectures"]}
        local_ids = [key.split(":")[1] for key in keys]
        originals = [entries[key] for key in local_ids]
        if any(key not in pack["lectures"] for key in keys):
            raise ValueError("A source member is missing or unusable")
        survivor = local_ids[0]
        filename = survivor + "-" + slug(group["title"]) + ".md"
        target = directory / filename
        if target.exists() and target.name not in [entry["file"] for entry in originals]:
            raise ValueError(f"Refusing to overwrite unrelated manuscript {target}")
        parts, metadata, sources = [], [], []
        for key, entry in zip(local_ids, originals):
            source = directory / entry["file"]
            text = read(source)
            parts.append((entry["title"], text))
            sidecar = directory / "metadata" / (key + ".json")
            data = json.loads(read(sidecar)) if sidecar.exists() else {}
            metadata.append(data)
            sources.append(dict(id=namespace + ":" + key, file=entry["file"], sha256=hashlib.sha256(text.encode()).hexdigest(), metadata=data))
            deletes.add(source)
            if sidecar.exists():
                deletes.add(sidecar)
        text = compose(group["title"], parts)
        provenance = dict(date=str(date.today()), models=["GPT-6 (exact variant unavailable)"], source_git_revision=revision, scope="Compose existing narration into one lecture; retain component arguments, source claims and non-spoken companions.", sources=sources)
        writes[target] = text
        writes[directory / "metadata" / (survivor + ".json")] = pretty(merge_metadata(metadata, survivor, filename, provenance))
        words = len(extract_text(text).split())
        entry = deepcopy(originals[0])
        entry.update(title=group["title"], file=filename, spoken_words=words, estimated_minutes_at_145_wpm=round(words / 145, 1))
        entry["consolidated_from"] = list(dict.fromkeys(
            key for original in originals
            for key in original.get("consolidated_from", [original["id"]])
        ))
        by_pack.setdefault(namespace, []).append((keys, entry))
        replacements.update({key: namespace + ":" + survivor for key in keys})
        summaries.append(dict(pack=namespace, id=survivor, title=group["title"], parts=len(keys), estimated_minutes=round(words / 145, 1)))

    for namespace, pack_groups in by_pack.items():
        directory, pack = packs[namespace]
        path = directory / "track.json"
        track = read_track(directory, pack)
        merged = {key: entry for keys, entry in pack_groups for key in keys}
        emitted, rows = set(), []
        for entry in track["lectures"]:
            key = namespace + ":" + entry["id"]
            replacement = merged.get(key, entry)
            if replacement["id"] not in emitted:
                rows.append(replacement)
                emitted.add(replacement["id"])
        order = plan.get("orders", {}).get(namespace)
        if order:
            order = [key.split(":")[-1] for key in order]
            if set(order) != emitted or len(order) != len(emitted):
                raise ValueError(f"{namespace}: explicit order must name every resulting lecture once")
            indexed = {entry["id"]: entry for entry in rows}
            rows = [indexed[key] for key in order]
        track["lectures"] = rows
        if "sections" in track:
            used = {row.get("section") for row in rows}
            track["sections"] = [section for section in track["sections"] if section in used]
        writes[path] = pretty(track)
        provenance_path = directory / "provenance.yaml"
        provenance = yaml.safe_load(read(provenance_path)) if provenance_path.exists() else {}
        provenance = provenance or {}
        provenance.setdefault("transcript", {}).setdefault("revisions", []).append(dict(
            date=str(date.today()),
            models=["GPT-6 (exact variant unavailable)"],
            sources=[dict(lecture=entry["id"], composition_record="metadata/" + entry["id"] + ".json") for _, entry in pack_groups],
            scope="Consolidate reviewed source parts into single lecture manuscripts. Original text and source attribution are retained in component records and Git history; this revision does not claim original authorship of inherited prose.",
        ))
        writes[provenance_path] = yaml.safe_dump(provenance, sort_keys=False, allow_unicode=True)

    # Update references in every owning pack, including cross-pack survey routes.
    for namespace, (directory, _) in packs.items():
        path = directory / "navigation.json"
        if not path.exists():
            continue
        original = read(path)
        navigation = json.loads(original)
        for course in navigation["collections"]:
            revised = plan.get("collection_orders", {}).get(namespace + ":" + course["id"])
            if revised is not None:
                course.pop("chapters", None)
                course.pop("include_sections", None)
                course["lectures"] = [key.split(":")[1] if key.startswith(namespace + ":") else key for key in revised]
            seen = set()

            def remap(container):
                if "lectures" in container:
                    output = []
                    for local in container["lectures"]:
                        old = qualified(namespace, local)
                        new = replacements.get(old, old)
                        if new in seen:
                            continue
                        seen.add(new)
                        output.append(new.split(":")[1] if ":" not in local and new.startswith(namespace + ":") else new)
                    container["lectures"] = output
                if "sessions" in container:
                    for session in container["sessions"]:
                        remap(session)
                    container["sessions"] = [session for session in container["sessions"] if session.get("lectures")]
                if "chapters" in container:
                    for chapter in container["chapters"]:
                        remap(chapter)
                    container["chapters"] = [chapter for chapter in container["chapters"] if chapter.get("lectures") or chapter.get("sessions") or chapter.get("include_sections")]
            remap(course)
        if navigation != json.loads(original):
            writes[path] = pretty(navigation)
    for path in writes:
        if path not in observed:
            observed[path] = path.read_bytes() if path.exists() else None
    return observed, writes, deletes - writes.keys(), summaries


def apply_prepared(observed, writes, deletes):
    # All conflicts are checked before the first mutation; don't overwrite active authors.
    for path, original in observed.items():
        current = path.read_bytes() if path.exists() else None
        if current != original:
            raise ValueError(f"Changed during preparation: {path}")
    previous = {path: path.read_bytes() if path.exists() else None for path in set(writes) | set(deletes)}
    try:
        for path, text in writes.items():
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(text, encoding="utf-8")
        for path in deletes:
            path.unlink()
    except BaseException:
        for path, content in previous.items():
            if content is None:
                path.unlink(missing_ok=True)
            else:
                path.write_bytes(content)
        raise


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--plan", required=True, type=Path)
    parser.add_argument("--repository", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    observed, writes, deletes, summary = prepare(args.repository, json.loads(args.plan.read_text()))
    print(pretty(dict(lectures=summary, files_written=len(writes), files_removed=len(deletes), applied=args.apply)))
    if args.apply:
        apply_prepared(observed, writes, deletes)


if __name__ == "__main__":
    main()

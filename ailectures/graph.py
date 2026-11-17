"""Portable learning-map views of a library snapshot, without presentation imports.

Typed authored evidence is kept separate from derived navigation. A listening
sequence never becomes a teaching prerequisite, proof claim, or historical link.
"""
from __future__ import annotations

from collections import defaultdict
from hashlib import sha256
import json
from urllib.parse import quote
from .core import qualified, text_digest
from .organization import collection_metadata, item_organization


RELATION_TYPES = {
    "hard_depends_on": ("Required background", "preparation", "An authored teaching prerequisite; this is not a formal proof import or a playback restriction."),
    "soft_depends_on": ("Suggested background", "preparation", "Helpful teaching preparation, without a required listening order."),
    "suggested_preparation": ("Suggested collection preparation", "preparation", "A collection recommends reviewing this other collection as needed."),
    "proof_depends_on": ("Proof dependency", "proof", "An authored claim that a proof uses a result or construction. Original component evidence is retained."),
    "historical_influence": ("Historical influence", "history", "An explicitly supplied historical relationship; listening order and shared subject matter do not establish influence."),
    "original_parent": ("Source adaptation", "lineage", "Records an adaptation or source relationship, rather than a teaching prerequisite or historical influence."),
    "listening_next": ("Next in listening order", "listening", "A next step in an authored listening route; it does not assert a mathematical dependency."),
    "expands_on": ("Expanded treatment", "related", "A more detailed treatment of related material."),
    "alternative_presentation": ("Alternative presentation", "related", "A different presentation of overlapping material."),
    "related_to": ("Related material", "related", "Related material without an asserted prerequisite, proof dependency, or historical influence."),
    "contains": ("Contains lecture", "organization", "Collection membership only."),
    "collection_parent": ("Part of collection", "organization", "Collection hierarchy only; it does not assert prerequisites."),
}


def _rows(value):
    if isinstance(value, dict):
        return value
    return {row["id"]: row for row in value or [] if isinstance(row, dict) and isinstance(row.get("id"), str)}


def _list(value):
    return value if isinstance(value, list) else []


def _lecture_url(key):
    return "/lectures/" + "/".join(quote(part, safe="") for part in key.split(":"))


def build_learning_map(snapshot):
    """Return a JSON-safe, deterministic graph from live or installed-pack data.

    No repository paths or optional dkvis/NetworkX modules are consulted. Older
    component endpoints are resolved using the composition records transferred
    with packs; evidence retains its original endpoints and explanations.
    """
    lectures = _rows(snapshot.get("lectures", {}))
    courses = _rows(snapshot.get("courses", {}))
    aliases = dict(snapshot.get("aliases", {}))
    diagnostics = []

    def alias(old, current):
        if not isinstance(old, str) or not old:
            return
        if ":" not in old:
            old = current.split(":", 1)[0] + ":" + old
        if old in aliases and aliases[old] != current:
            diagnostics.append(f"Conflicting component identity: {old}")
        else:
            aliases[old] = current

    def composition(record, current):
        if not isinstance(record, dict):
            return
        consolidation = record.get("consolidation", {})
        if not isinstance(consolidation, dict):
            return
        for source in _list(consolidation.get("sources")):
            if isinstance(source, dict):
                alias(source.get("id"), current)
                composition(source.get("metadata", {}), current)

    for key, row in lectures.items():
        for old in _list(row.get("aliases")):
            alias(old, key)
        for old in _list(row.get("consolidated_from")):
            alias(old, key)
        composition(row.get("metadata", {}), key)

    def resolve(key):
        seen = set()
        while key in aliases and aliases[key] != key and key not in seen:
            seen.add(key)
            key = aliases[key]
        return min(seen) if key in seen else key

    memberships = defaultdict(list)
    for course_id, course in courses.items():
        for key in course.get("lectures", []):
            current = resolve(key)
            if course_id not in memberships[current]:
                memberships[current].append(course_id)
    nodes = {}
    organized_courses = [dict(course, **collection_metadata(course, key.split(":", 1)[0])) for key, course in courses.items()]
    for key, row in lectures.items():
        node = {
            "id": key, "kind": "lecture", "title": row.get("title", key),
            "available": True, "namespace": row.get("namespace", key.split(":", 1)[0]),
            "collections": memberships.get(key, []), "section": row.get("section", ""),
            "url": _lecture_url(key),
            "revision": row.get("revision"),
            "knowledge_revision": text_digest(row.get("source") or row.get("transcript", "")),
            "estimated_minutes": round(len(row.get("transcript", "").split()) / 145, 1),
            **item_organization(row, organized_courses),
        }
        metadata = row.get("metadata", {})
        learning = metadata.get("learning", {}) if isinstance(metadata, dict) else {}
        if not isinstance(learning, dict):
            learning = {}
            diagnostics.append(f"Ignored malformed learning notes for {key}.")
        node["prerequisites_reviewed"] = learning.get("reviewed") is True
        for field in ("background", "readiness_checks"):
            node[field] = [value for value in _list(learning.get(field)) if isinstance(value, str) and value.strip()]
        if row.get("kind") == "presentation":
            node["format"] = "presentation"
            node["url"] = "/presentations?deck=" + quote(row.get("deck", key.split(":", 1)[-1]), safe="")
        else:
            node["format"] = "audio"
        nodes[key] = node
    collections = []
    for key, course in courses.items():
        record = {
            "id": key, "node_id": "collection:" + key, "title": course.get("title", key),
            "role": course.get("role", "main"), "parent_id": course.get("parent_id"),
            "lectures": list(course.get("lectures", [])), "summary": course.get("summary", ""),
            "url": "/collections/" + quote(key, safe=""),
            "background": course.get("background", []),
            **collection_metadata(course, key.split(":", 1)[0]),
        }
        collections.append(record)
        nodes[record["node_id"]] = {
            "id": record["node_id"], "kind": "collection", "collection_id": key,
            "title": record["title"], "available": True, "url": record["url"],
            "collections": [key], "role": record["role"],
        }

    def optional(key):
        if key not in nodes:
            is_collection = key.startswith("collection:")
            nodes[key] = {
                "id": key, "kind": "collection" if is_collection else "lecture",
                "title": key.removeprefix("collection:"), "available": False,
                "url": None, "collections": memberships.get(key, []),
                "status": "Not installed",
            }
            if is_collection:
                nodes[key]["collection_id"] = key.removeprefix("collection:")

    relations = {}

    def add(source, kind, target, why=None, *, origin="authored", collection_id=None, evidence=None):
        if not all(isinstance(value, str) and value for value in (source, kind, target)):
            diagnostics.append("Ignored a relationship with missing endpoints or type.")
            return
        original_source, original_target = source, target
        source, target = resolve(source), resolve(target)
        claim_source = evidence.get("from", original_source) if isinstance(evidence, dict) else original_source
        claim_target = evidence.get("to", original_target) if isinstance(evidence, dict) else original_target
        internal = source == target and (original_source != original_target or claim_source != claim_target)
        optional(source)
        optional(target)
        identity = source, kind, target
        if identity not in relations:
            label, category, description = RELATION_TYPES.get(kind, (kind.replace("_", " ").capitalize(), "related", "An explicitly supplied relationship."))
            stable = json.dumps(identity, separators=(",", ":"), ensure_ascii=False)
            relations[identity] = {
                "id": "relation-" + sha256(stable.encode()).hexdigest()[:20],
                "from": source, "to": target, "type": kind, "label": label,
                "category": category, "description": description,
                "internal": internal, "reasons": [], "collections": [], "evidence": [],
            }
        record = relations[identity]
        record["internal"] = record["internal"] and internal
        if isinstance(why, str) and why.strip() and why not in record["reasons"]:
            record["reasons"].append(why)
        if collection_id and collection_id not in record["collections"]:
            record["collections"].append(collection_id)
        claim = {"from": original_source, "to": original_target, "origin": origin}
        if isinstance(why, str) and why.strip():
            claim["why"] = why
        if collection_id:
            claim["collection_id"] = collection_id
        if isinstance(evidence, dict):
            claim.update({key: evidence[key] for key in ("from", "to", "why") if key in evidence})
        if claim not in record["evidence"]:
            record["evidence"].append(claim)

    for edge in snapshot.get("relationships", []):
        if not isinstance(edge, dict):
            diagnostics.append("Ignored a malformed relationship.")
            continue
        evidence = edge.get("component_relations")
        if isinstance(evidence, list) and evidence:
            for claim in evidence:
                if isinstance(claim, dict):
                    add(edge.get("from"), edge.get("type"), edge.get("to"), claim.get("why", edge.get("why")), evidence=claim)
        else:
            add(edge.get("from"), edge.get("type"), edge.get("to"), edge.get("why"))
    for key, row in lectures.items():
        metadata = row.get("metadata", {})
        learning = metadata.get("learning", {}) if isinstance(metadata, dict) else {}
        if not isinstance(learning, dict):
            continue
        for field, kind in (("prerequisites", "hard_depends_on"), ("recommended", "soft_depends_on")):
            entries = learning.get(field, [])
            if not isinstance(entries, list):
                nodes[key]["prerequisites_reviewed"] = False
                diagnostics.append(f"Ignored malformed {field} for {key}.")
                continue
            for entry in entries:
                try:
                    if not isinstance(entry, dict):
                        raise ValueError("expected a preparation record")
                    target = entry["lecture_id"]
                    if not isinstance(target, str):
                        raise ValueError("expected a lecture ID")
                    if ":" not in target:
                        target = key.split(":", 1)[0] + ":" + target
                    qualified(target)
                    reason = entry["reason"]
                    if not isinstance(reason, str) or not reason.strip():
                        raise ValueError("expected a teaching explanation")
                    add(key, kind, target, reason, origin="lecture_learning_notes")
                except (KeyError, ValueError, TypeError):
                    nodes[key]["prerequisites_reviewed"] = False
                    diagnostics.append(f"Ignored a malformed {field} entry for {key}.")
    for course_id, course in courses.items():
        source = "collection:" + course_id
        members = course.get("lectures", [])
        for member in members:
            add(source, "contains", member, origin="collection", collection_id=course_id)
        for first, second in zip(members, members[1:]):
            if resolve(first) != resolve(second):
                add(first, "listening_next", second, f"Next in {course.get('title', course_id)}.", origin="listening_route", collection_id=course_id)
        if course.get("parent_id"):
            add(source, "collection_parent", "collection:" + course["parent_id"], origin="collection", collection_id=course_id)
        for target in _list(course.get("preparation_collections")):
            if not isinstance(target, str):
                continue
            add(source, "suggested_preparation", "collection:" + target, "Review the relevant parts as needed for this collection's stated background.", origin="navigation", collection_id=course_id)
        for target in _list(course.get("related_collections")):
            if not isinstance(target, str):
                continue
            add(source, "related_to", "collection:" + target, origin="navigation", collection_id=course_id)
        for chapter in _list(course.get("chapters")):
            if isinstance(chapter, dict) and isinstance(chapter.get("collection"), str) and chapter["collection"]:
                add("collection:" + chapter["collection"], "expands_on", source, "Expanded treatment of " + chapter.get("title", "this topic") + ".", origin="navigation", collection_id=course_id)
    type_records = {
        kind: {"label": label, "category": category, "description": description}
        for kind, (label, category, description) in RELATION_TYPES.items()
    }
    for record in relations.values():
        type_records.setdefault(record["type"], {key: record[key] for key in ("label", "category", "description")})
    return {
        "schema_version": 1, "generation": snapshot.get("generation"),
        "nodes": nodes, "collections": collections, "relationships": list(relations.values()),
        "relation_types": type_records,
        "component_lectures": {key: resolve(key) for key in aliases if key != resolve(key)},
        "counts": {"lectures": len(lectures), "collections": len(collections),
                   "relationships": len(relations), "internal_relationships": sum(row["internal"] for row in relations.values()),
                   "unavailable_nodes": sum(not row["available"] for row in nodes.values())},
        "diagnostics": list(dict.fromkeys(diagnostics)),
    }


learning_map = build_learning_map

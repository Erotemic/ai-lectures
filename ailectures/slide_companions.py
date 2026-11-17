"""Optional repository slide companions, independent of the audio reader.

Construction and portable use do not import dkvis. Listing lazily uses its
source/cache reader; only an explicit build calls the optional renderer.
"""

from __future__ import annotations

from copy import deepcopy
import importlib.util
import json
from pathlib import Path
import re
import threading
from urllib.parse import quote


DECK_ID = re.compile(r"[a-z][a-z0-9-]{1,63}\Z")


class SlideCompanionsUnavailable(RuntimeError):
    """An optional repository capability or its source is unavailable."""


def _component_ids(row):
    """Use retained source lineage, including nested successive compositions."""
    result = {row["id"]}
    result.update(item for item in row.get("aliases", []) if isinstance(item, str))
    namespace = row["id"].split(":", 1)[0]

    def add(identifier):
        if isinstance(identifier, str):
            result.add(identifier if ":" in identifier else namespace + ":" + identifier)

    def visit(metadata):
        if not isinstance(metadata, dict):
            return
        consolidation = metadata.get("consolidation")
        if not isinstance(consolidation, dict):
            return
        sources = consolidation.get("sources", [])
        for item in sources if isinstance(sources, list) else []:
            if isinstance(item, dict):
                add(item.get("id"))
                visit(item.get("metadata"))

    visit(row.get("metadata", {}))
    for field in ("consolidated_from", "consolidated_lineage"):
        for item in row.get(field, []):
            add(item.get("id") if isinstance(item, dict) else item)
    return result


class SlideCompanions:
    def __init__(self, repository=None, *, renderer_factory=None):
        self.repository = repository
        self._factory = renderer_factory
        self._renderer_instance = None
        self._lock = threading.RLock()
        self._building = set()
        self._errors = {}

    @property
    def source(self):
        return Path(self.repository.root) / "companion-slides"

    def _entries(self):
        if self.repository is None or not (self.source / "manifest.json").is_file():
            raise SlideCompanionsUnavailable("No repository slide sources are available.")
        data = json.loads((self.source / "manifest.json").read_text())
        if not isinstance(data, dict) or data.get("schema_version") != 1 or not isinstance(data.get("decks"), list):
            raise ValueError("Invalid companion slide manifest")
        entries = {}
        for entry in data["decks"]:
            if not isinstance(entry, dict):
                raise ValueError("Invalid companion slide entry")
            key = entry.get("id")
            if not isinstance(key, str) or not DECK_ID.fullmatch(key) or key in entries:
                raise ValueError("Invalid or duplicate companion slide identity")
            if entry.get("source") != key + ".json":
                raise ValueError("Invalid companion slide source path")
            if not isinstance(entry.get("lecture_nodes"), list) or not all(
                isinstance(node, str) for node in entry["lecture_nodes"]
            ):
                raise ValueError("Invalid companion lecture associations")
            entries[key] = entry
        return entries

    def _renderer(self):
        with self._lock:
            if self._renderer_instance is None:
                if self._factory is not None:
                    self._renderer_instance = self._factory()
                else:
                    from dkvis.presentation.companion_slides import CompanionSlideLibrary

                    self._renderer_instance = CompanionSlideLibrary(
                        self.source, Path(self.repository.root) / "companion-slide-cache"
                    )
            return self._renderer_instance

    def _associations(self):
        rows = {
            key: row
            for pack in self.repository.snapshot(copy=False).values()
            for key, row in pack["lectures"].items()
        }
        by_component = {}
        for key, row in rows.items():
            for component in _component_ids(row):
                by_component.setdefault(component, []).append(key)
        return rows, by_component

    def _record(self, entry, rows, by_component):
        key = entry["id"]
        native = "/api/library/slide-decks/" + quote(key, safe="")
        lectures = list(dict.fromkeys(
            current
            for node in entry["lecture_nodes"]
            for current in by_component.get(node, [])
        ))
        record = dict(
            id=key, title=key, subtitle="", lecture_nodes=entry["lecture_nodes"],
            lecture_ids=lectures, built=False, available=True,
            status_url=native, build_url=native + "/build",
            view_url=native + "/html", download_url=native + "/html?download=1",
        )
        try:
            status = self._renderer().status(key)
            record.update({k: v for k, v in status.items()
                           if k not in {"url", "download_url", "lecture_nodes"}})
            authored = json.loads((self.source / entry["source"]).read_text())
            if not isinstance(authored, dict):
                raise ValueError("Invalid companion slide source")
            record["attribution"] = deepcopy(
                authored.get("attribution", authored.get("credits", authored.get("provenance")))
            )
            record["sources"] = deepcopy(authored.get("sources", []))
            if record["built"]:
                # The renderer names cached HTML by its source/renderer revision.
                record["revision"] = self._renderer().rendered(key).name
        except (OSError, ImportError, ValueError, KeyError, TypeError) as exc:
            record.update(available=False, built=False, error="Slide source unavailable: " + str(exc))
        record["source_credits"] = [
            dict(lecture_id=lecture, sources=deepcopy(rows[lecture].get("sources", {})),
                 provenance=deepcopy(rows[lecture].get("metadata", {}).get("provenance")))
            for lecture in lectures
        ]
        record["build_available"] = record["available"] and (
            self._factory is not None or importlib.util.find_spec("manim") is not None
        )
        with self._lock:
            error = self._errors.get(key)
            if key in self._building:
                record["state"] = "building"
            elif record["built"]:
                record["state"] = "built"
            elif not record["available"]:
                record["state"] = "unavailable"
            elif error:
                record.update(state="failed", error=error)
            else:
                record["state"] = "unbuilt"
        return record

    def list_for_lecture(self, lecture_id):
        """A missing optional capability never prevents reading a lecture."""
        try:
            entries = self._entries()
            rows, associations = self._associations()
        except (OSError, ImportError, ValueError, TypeError, SlideCompanionsUnavailable) as exc:
            return dict(available=False, items=[], reason=str(exc))
        if lecture_id not in rows:
            raise KeyError(lecture_id)
        return dict(available=True, items=[
            self._record(entry, rows, associations)
            for entry in entries.values()
            if any(lecture_id in associations.get(node, []) for node in entry["lecture_nodes"])
        ])

    def status(self, deck_id):
        entry = self._entries().get(deck_id)
        if entry is None:
            raise KeyError(deck_id)
        rows, associations = self._associations()
        return self._record(entry, rows, associations)

    def build(self, deck_id):
        """Synchronous worker entry point; duplicate requests share build state."""
        before = self.status(deck_id)
        if before["built"] or not before["available"]:
            return before
        if not before["build_available"]:
            return dict(before, state="unavailable", error="The slide renderer is not installed.")
        with self._lock:
            if deck_id in self._building:
                return dict(before, state="building")
            self._building.add(deck_id)
            self._errors.pop(deck_id, None)
        try:
            self._renderer().build(deck_id)
        except Exception as exc:
            # This is an optional renderer boundary, not an audio/source error.
            with self._lock:
                self._errors[deck_id] = "Slide build failed: " + str(exc)
        finally:
            with self._lock:
                self._building.discard(deck_id)
        return self.status(deck_id)

    def html_file(self, deck_id):
        status = self.status(deck_id)
        if not status["available"]:
            raise SlideCompanionsUnavailable(status["error"])
        if not status["built"]:
            raise FileNotFoundError("Build this slide deck before opening its HTML.")
        return self._renderer().rendered(deck_id)

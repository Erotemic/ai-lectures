"""Authoring-format adapters for a common spoken transcript, without renderers."""

from __future__ import annotations

from dataclasses import dataclass
import re

from .core import BEGIN, END, extract_text


@dataclass(frozen=True)
class Narration:
    title: str
    motivation: str
    reminder: str
    beats: tuple[str, ...]
    pauses: tuple[float, ...] = ()

    @property
    def text(self) -> str:
        return "\n\n".join(self.beats)


def read_scene_narration(
    source: str, *, scenes=None, source_name="transcript"
) -> dict[str, Narration]:
    """Adapt older scene manuscripts; motivations and reminders are unspoken."""
    headings = list(re.finditer(r"^## ([A-Za-z_]\w*): (.+)$", source, re.MULTILINE))
    if not headings:
        raise ValueError(f"No scene narration sections: {source_name}")
    result = {}
    for i, match in enumerate(headings):
        name, title = match.groups()
        end = headings[i + 1].start() if i + 1 < len(headings) else len(source)
        body = source[match.end() : end].strip()
        why = re.match(r"Why: ([^\n]+)\n", body)
        if not why:
            raise ValueError(f"missing learner motivation: {name}")
        body = body[why.end() :].strip()
        recall = re.match(r"Recall: ([^\n]+)\n", body)
        if not recall:
            raise ValueError(f"missing local notation reminder: {name}")
        body = body[recall.end() :].strip()
        if name in result or not body:
            raise ValueError(f"duplicate or empty narration section: {name}")
        beats = tuple(
            "\n\n".join(" ".join(p.split()) for p in beat.split("\n\n") if p.strip())
            for beat in body.split("<!-- beat -->")
        )
        if not all(beats):
            raise ValueError(f"empty narration build: {name}")
        result[name] = Narration(title, why.group(1), recall.group(1), beats)
    if scenes is not None and list(result) != list(scenes):
        raise ValueError(
            f"narration sections must follow the deck's scene order: {source_name}"
        )
    return result


def spoken_transcript(source: str, source_name="transcript") -> str:
    """Normalize declared narration, never guess that editorial notes are spoken."""
    if BEGIN in source or END in source:
        return extract_text(source, source_name).strip()
    sections = read_scene_narration(source, source_name=source_name)
    text = "\n\n".join(section.text for section in sections.values())
    return extract_text(BEGIN + "\n" + text + "\n" + END, source_name).strip()

"""Speech roles from authored Markdown, without changing canonical spoken words."""
from copy import deepcopy
from functools import lru_cache
import re

from .core import BEGIN, END, extract_text, digest

TITLE_POLICY = 'section-titles-v1'
TITLE_INSTRUCTION = ('Read this as a section heading, clearly and with measured emphasis. '
                     'Use a self-contained title cadence, not a running sentence. '
                     'Speak only the supplied title.')


def title_spans(source, transcript):
    """Return word ranges only when the source matches the chosen speech snapshot."""
    if not isinstance(source, str): return []
    try:
        if extract_text(source).split() != transcript.split(): return []
    except ValueError:
        return []
    raw = source.split(BEGIN,1)[1].split(END,1)[0]
    words, spans = [], []
    for line in raw.splitlines():
        if not line.strip(): continue
        try: tokens = extract_text(BEGIN+'\n'+line+'\n'+END).split()
        except ValueError: return []
        start = len(words); words.extend(tokens)
        if tokens and re.match(r'^#{1,6}[ \t]+\S',line):
            spans.append((start,len(words)))
    return spans if words == transcript.split() else []


@lru_cache(maxsize=64)
def page_delivery(source, transcript, pages):
    """Partition existing pages; retain pagination, text, and occurrence identity."""
    spans = title_spans(source,transcript)
    if not spans or ' '.join(' '.join(pages).split()) != ' '.join(transcript.split()):
        return tuple(() for _ in pages)
    result, offset = [], 0
    for page in pages:
        tokens = list(re.finditer(r'\S+',page))
        count = len(tokens)
        titles = [(max(0,a-offset),min(count,b-offset)) for a,b in spans if a < offset+count and b > offset]
        if not titles:
            result.append(()); offset += count; continue
        boundaries = sorted({0,count,*[value for pair in titles for value in pair]})
        parts = []
        for a,b in zip(boundaries,boundaries[1:]):
            role = 'title' if any(start<=a and b<=end for start,end in titles) else 'body'
            parts.append(dict(role=role,text=page[tokens[a].start():tokens[b-1].end()]))
        result.append(tuple(parts)); offset += count
    return tuple(result)


def speech_cache_key(lecture, configuration):
    # Per-page delivery is already in the page request hash. A new delivery
    # policy must not move unchanged body pages out of their shared cache.
    config = deepcopy(configuration)
    config.get('settings', {}).pop('reader_title_policy', None)
    return digest(dict(lecture=lecture, configuration=config))


def transcript_headings(source, transcript):
    """Display structure is separate from speech words and recording identity."""
    if not isinstance(source, str) or not isinstance(transcript, str):
        return ()
    return _transcript_headings(source, transcript)


@lru_cache(maxsize=128)
def _transcript_headings(source, transcript):
    if BEGIN in source or END in source:
        spans = title_spans(source, transcript)
        if not spans:
            return ()
        raw = source.split(BEGIN, 1)[1].split(END, 1)[0]
        levels = [
            len(match.group(1))
            for line in raw.splitlines()
            if (match := re.match(r"^(#{1,6})[ \t]+\S", line))
        ]
        words = transcript.split()
        return tuple(
            dict(start=a, end=b, level=level, text=" ".join(words[a:b]), spoken=True)
            for (a, b), level in zip(spans, levels)
        )
    from .manuscripts import read_scene_narration

    try:
        sections = read_scene_narration(source)
        texts = [
            extract_text(BEGIN + "\n" + section.text + "\n" + END).strip()
            for section in sections.values()
        ]
    except ValueError:
        return ()
    if " ".join(" ".join(texts).split()) != " ".join(transcript.split()):
        return ()
    headings, offset = [], 0
    for index, (section, text) in enumerate(zip(sections.values(), texts)):
        first = extract_text(BEGIN + "\n" + section.beats[0] + "\n" + END).strip()
        spoken = " ".join(first.split()).rstrip(".!?") == section.title.rstrip(".!?")
        headings.append(
            dict(
                start=offset,
                end=offset + len(first.split()) if spoken else offset,
                level=1 if index == 0 else 2,
                text=first if spoken else section.title,
                spoken=spoken,
            )
        )
        offset += len(text.split())
    return tuple(headings)

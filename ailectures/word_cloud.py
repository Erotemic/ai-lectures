"""Explore repeated spoken words and n-grams, independent of TTS and playback.

The corpus is the parsed spoken transcript, not the manuscript's citations,
metadata, or editorial notes. The browser and CLI use the same counting and
SVG rendering functions.
"""

from __future__ import annotations

from collections import Counter
from html import escape
import math
import re
from typing import Iterable, Mapping

# Unicode letters and internal apostrophes. Exclude digits and underscores,
# which are generally identifiers or notation rather than spoken prose.
WORD = re.compile(r"[^\W\d_]+(?:['\u2019][^\W\d_]+)*", re.UNICODE)
BREAK = re.compile(r"(?:\r?\n){2,}|(?<=[.!?;:])\s+|\s*[\u2014\u2013]\s*")

# Modest English function-word list, deliberately transparent and editable.
# For multiword phrases, retain expressions with *any* non-stopword token.
STOPWORDS = frozenset("""
a about above after again against all am an and any are as at be because been
before being below between both but by can cannot could did do does doing down
during each either for from further had has have having he her here hers herself
him himself his how i if in into is it its itself just let's me more most my
myself no nor not of off on once only or other our ours ourselves out over own
same she should so some such than that the their theirs them themselves then
there these they this those through to too under until up us very was we were
what when where which while who whom why will with would you your yours yourself
yourselves aint aren't can't couldn't didn't doesn't don't hadn't hasn't haven't
isn't shouldn't wasn't weren't won't wouldn't it's that's there's they're we're
you're i'll we've i've you're i'm i'd wasn't what's who's there's
""".split())

COLORS = ("#1b6258", "#355d77", "#684b7a", "#865237", "#406b43", "#303f58")


def segments(text: str):
    """Each segment is a narration span that n-grams may not cross."""
    for match in BREAK.split(text):
        if match.strip():
            yield match


def tokens(text: str):
    return WORD.findall(text.casefold().replace("\u2019", "'"))


def _gram_tokens(words, n, include_common):
    if len(words) < n:
        return
    # Sliding count avoids a membership-test generator for every word window.
    if include_common:
        for i in range(len(words) - n + 1):
            yield " ".join(words[i : i + n])
    else:
        noncommon = [word not in STOPWORDS for word in words]
        active = sum(noncommon[:n])
        for i in range(len(words) - n + 1):
            if active:
                yield " ".join(words[i : i + n])
            if i + n < len(words):
                active += noncommon[i + n] - noncommon[i]


def _grams(text: str, n: int, include_common: bool):
    for segment in segments(text):
        yield from _gram_tokens(tokens(segment), n, include_common)


def _selected(rows: Iterable[Mapping], pack: str | None = None, lecture: str | None = None):
    result = []
    for row in rows:
        if pack and row.get("origin", {}).get("pack", row.get("namespace")) != pack:
            continue
        if lecture and row["id"] != lecture:
            continue
        if row.get("transcript"):
            result.append(row)
    return result


def _coverage(rows, candidates, n, include_common):
    counts = Counter()
    for row in rows:
        counts.update(set(_grams(row["transcript"], n, include_common)) & candidates)
    return counts


def cloud_data(
    lectures: Iterable[Mapping], *, n=1, top=60, pack=None, lecture=None,
    rank="count", min_lectures=2, include_common=False,
):
    """Exact top-k counts and per-lecture coverage for narrated text.

    Coverage is measured on increasingly large frequency candidate sets.
    Since document frequency cannot exceed occurrence count, candidates are
    expanded until the next unseen occurrence count is below the k-th score.
    This keeps the expensive document-frequency pass bounded in normal cases.
    """
    if not 1 <= n <= 4 or not 1 <= top <= 150 or min_lectures < 1:
        raise ValueError("n must be 1-4, top 1-150, and min_lectures positive")
    if rank not in {"count", "lectures"}:
        raise ValueError("rank must be count or lectures")
    rows = _selected(lectures, pack, lecture)
    if (pack or lecture) and not rows:
        raise ValueError("No narrated lectures match the selected scope")
    words = 0
    counts = Counter()
    for row in rows:
        for segment in segments(row["transcript"]):
            local_tokens = tokens(segment)
            words += len(local_tokens)
            counts.update(_gram_tokens(local_tokens, n, include_common))
    size = min(len(counts), max(500, top * 12))
    best = []
    while size:
        candidates = counts.most_common(size)
        docs = _coverage(rows, {term for term, _ in candidates}, n, include_common)
        eligible = [
            (term, count, docs[term])
            for term, count in candidates if docs[term] >= min_lectures
        ]
        if rank == "count":
            eligible.sort(key=lambda item: (-item[1], -item[2], item[0]))
        else:
            eligible.sort(key=lambda item: (-item[2], -item[1], item[0]))
        best = eligible[:top]
        # A not-yet-considered phrase's lecture count <= its occurrence count.
        next_count = counts.most_common(size + 1)[-1][1] if size < len(counts) else -1
        kth_score = (best[-1][1] if rank == "count" else best[-1][2]) if len(best) == top else -1
        if size == len(counts) or next_count < kth_score:
            break
        size = min(len(counts), size * 2)
    items = [
        {"phrase": phrase, "count": count, "lectures": document_count,
         "per_10k": round(10000 * count / words, 2) if words else 0.0}
        for phrase, count, document_count in best
    ]
    result = {
        "n": n, "top": top, "rank": rank, "pack": pack, "lecture": lecture,
        "min_lectures": min_lectures, "include_common": include_common,
        "words": words, "lectures": len(rows), "distinct_phrases": len(counts),
        "items": items,
    }
    result["svg"], result["drawn"] = render_svg(items)
    return result


def phrase_data(lectures: Iterable[Mapping], phrase: str, *, pack=None, lecture=None, limit=15):
    """Find literal adjacent word sequences and excerpts in spoken narration."""
    needle = tokens(phrase)
    if not 1 <= len(needle) <= 10:
        raise ValueError("Enter a phrase of 1-10 words")
    if not 1 <= limit <= 50:
        raise ValueError("limit must be between 1 and 50")
    rows = _selected(lectures, pack, lecture)
    if (pack or lecture) and not rows:
        raise ValueError("No narrated lectures match the selected scope")
    hits, total, words = [], 0, 0
    for row in rows:
        count, excerpt = 0, None
        for segment in segments(row["transcript"]):
            matches = list(WORD.finditer(segment))
            normal = [m.group().replace("\u2019", "'").casefold() for m in matches]
            words += len(normal)
            for i in range(len(normal) - len(needle) + 1):
                if normal[i : i + len(needle)] == needle:
                    count += 1
                    if excerpt is None:
                        start, end = matches[i].start(), matches[i + len(needle) - 1].end()
                        excerpt = ("..." if start > 90 else "") + segment[max(0, start - 90) : min(len(segment), end + 100)].strip() + ("..." if end + 100 < len(segment) else "")
        if count:
            hits.append({"id": row["id"], "title": row["title"], "count": count,
                         "excerpt": excerpt, "pack": row.get("origin", {}).get("pack", row.get("namespace"))})
            total += count
    hits.sort(key=lambda row: (-row["count"], row["title"], row["id"]))
    return {"phrase": " ".join(needle), "count": total, "lectures": len(hits),
            "words": words, "per_10k": round(10000 * total / words, 2) if words else 0.0,
            "examples": hits[:limit]}


def render_svg(items, *, width=1180, height=780):
    """Portable, dependency-free SVG for the web and --svg CLI output."""
    boxes, labels = [], []
    maximum = max((item["count"] for item in items), default=1)
    minimum = min((item["count"] for item in items), default=1)
    for index, item in enumerate(items):
        phrase, count = item["phrase"], item["count"]
        span = math.log1p(maximum) - math.log1p(minimum)
        weight = ((math.log1p(count) - math.log1p(minimum)) / span) ** 0.8 if span else 0.3
        size = 18 + 47 * weight
        # Approximate text width conservatively, reducing font size for long terms.
        size = min(size, (width - 60) / max(1, sum(0.61 if ord(c) < 256 else 0.92 for c in phrase)))
        boxw = max(8, size * sum(0.61 if ord(c) < 256 else 0.92 for c in phrase))
        boxh = size * 1.12
        position = None
        for step in range(4400):
            angle = step * 2.39996323 + index * 1.7
            radius = 7.7 * math.sqrt(step)
            cx = width / 2 + radius * 1.36 * math.cos(angle)
            cy = height / 2 + radius * 0.94 * math.sin(angle)
            rect = (cx - boxw / 2 - 4, cy - boxh / 2 - 3, cx + boxw / 2 + 4, cy + boxh / 2 + 3)
            if rect[0] < 14 or rect[2] > width - 14 or rect[1] < 12 or rect[3] > height - 12:
                continue
            if any(rect[0] < b[2] and rect[2] > b[0] and rect[1] < b[3] and rect[3] > b[1] for b in boxes):
                continue
            position = cx, cy
            boxes.append(rect)
            break
        if position is None:
            continue
        cx, cy = position
        color = COLORS[index % len(COLORS)]
        label = escape(phrase, quote=True)
        labels.append(
            f'<text x="{cx:.1f}" y="{cy:.1f}" text-anchor="middle" dominant-baseline="middle" '
            f'font-size="{size:.1f}" font-family="system-ui, sans-serif" font-weight="600" '
            f'fill="{color}" data-phrase="{label}" role="button" tabindex="0">'
            f'<title>{label}: {count} occurrences in {item["lectures"]} lectures</title>'
            f'{escape(phrase)}</text>'
        )
    svg = (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
        f'role="img" aria-label="Word and phrase cloud with {len(labels)} entries">'
        '<rect width="100%" height="100%" fill="#fafaf8" rx="14"/>'
        + "".join(labels) + "</svg>"
    )
    return svg, len(labels)

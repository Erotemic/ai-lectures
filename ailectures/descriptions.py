"""Compact discovery descriptions and outlines, independent of spoken content."""
import re


def short_text(value, limit=1200):
    if not isinstance(value, str) or any((ord(c) < 32 and c not in '\n\r\t') or ord(c) == 127 for c in value):
        return ''
    value = ' '.join(value.split())
    if len(value) > limit:
        value = value[:limit].rsplit(' ', 1)[0].rstrip(' ,;:') + '…'
    return value


def lecture_outline(source):
    """Use authored section headings; omit nonspoken production appendices."""
    if not isinstance(source, str):
        return []
    if '<!-- BEGIN SPOKEN LECTURE -->' in source:
        source = source.split('<!-- BEGIN SPOKEN LECTURE -->', 1)[1]
    source = source.split('<!-- END SPOKEN LECTURE -->', 1)[0]
    headings = []
    for heading in re.findall(r'^##\s+(.+?)\s*$', source, re.M):
        heading = short_text(re.sub(r'[*`]', '', heading), 180)
        if re.search(r'not spoken|non.spoken|display.only|^(?:(?:mathematical|historical|reading|source|study)\s+)?companions?\b|reading notes|source note|further reading|study material', heading, re.I):
            continue
        if heading and heading not in headings:
            headings.append(heading)
    return headings[:32]


def description_fields(row):
    metadata = row.get('metadata')
    metadata = metadata if isinstance(metadata, dict) else {}
    stored_outline = row.get('outline')
    stored_outline = stored_outline if isinstance(stored_outline, list) else []
    outline = list(dict.fromkeys(filter(None, (short_text(item, 180) for item in stored_outline if isinstance(item, str)))))[:32] or lecture_outline(row.get('source', ''))
    for value, basis in ((metadata.get('description'), 'authored'), (row.get('description'), row.get('description_basis', 'authored')), (metadata.get('synopsis'), 'authored')):
        if description := short_text(value):
            return dict(description=description, description_basis=basis if basis in {'authored', 'outline'} else 'authored', outline=outline)
    source = row.get('source', '')
    preface = source.split('<!-- BEGIN SPOKEN LECTURE -->', 1)[0] if isinstance(source, str) else ''
    objective = re.search(r'\*\*(?:Aim|Purpose|Focus|Theme|Method|Scope|Approach|Question|Central question|Central example|Project|Example|Case study|Core question):\*\*\s*(.+?)(?=\s+\*\*|$)', preface, re.I | re.M)
    if objective and (description := short_text(objective[1])):
        return dict(description=description, description_basis='authored', outline=outline)
    companion = re.search(r'\*\*Companion:\*\*\s*(.+?)(?=\s+\*\*|$)', preface, re.I | re.M)
    if companion:
        description = short_text(f"{row.get('title', 'Lecture')}. Companion coverage: {companion[1]}")
        return dict(description=description, description_basis='authored', outline=outline)
    # This is an explicit outline preview, not a claim to have summarized prose.
    if outline:
        selected = outline[:5]
        if len(outline) > 5:
            selected.append(outline[-1])
        description = short_text('Topics: ' + '; '.join(selected) + '.', 900)
        return dict(description=description, description_basis='outline', outline=outline)
    return dict(description='', description_basis='unrecorded', outline=[])

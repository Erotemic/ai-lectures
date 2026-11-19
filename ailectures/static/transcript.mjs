// Chunk boundaries are measured; word and sentence positions within them are
// interpolated. Missing or unusable timings fall back to measured page duration.
export const words = (text) => (text.match(/\S+/g) || []).length;

export function speechSegments(text) {
  const breaks = /[.!?]["”’)]?\s+(?=[A-Z0-9“"(])|\n\s*\n/g;
  const segments = [];
  let start = 0,
    match;
  while ((match = breaks.exec(text)) !== null) {
    segments.push(text.slice(start, breaks.lastIndex));
    start = breaks.lastIndex;
  }
  if (start < text.length) segments.push(text.slice(start));
  return segments.length ? segments : [text];
}

function chunks(segment) {
  const values = segment?.timings?.chunks;
  if (!Array.isArray(values) || !values.length) return [];
  let end = 0;
  for (const chunk of values) {
    if (
      !chunk ||
      ![chunk.start, chunk.end, chunk.words].every(Number.isFinite) ||
      chunk.start < end ||
      chunk.end <= chunk.start ||
      chunk.words <= 0 ||
      chunk.end > segment.duration + 0.1
    )
      return [];
    end = chunk.end;
  }
  return values;
}

export function wordAtTime(text, segment, seconds) {
  const count = words(text),
    measured = chunks(segment);
  if (!measured.length)
    return count * Math.max(0, Math.min(1, seconds / (segment?.duration || 1)));
  let passed = 0;
  const total = measured.reduce((sum, chunk) => sum + chunk.words, 0);
  for (const chunk of measured) {
    if (seconds < chunk.start) break;
    if (seconds <= chunk.end) {
      passed +=
        (chunk.words * (seconds - chunk.start)) / (chunk.end - chunk.start);
      break;
    }
    passed += chunk.words;
  }
  return (count * passed) / total;
}

export function timeAtWord(text, segment, word) {
  const count = Math.max(1, words(text)),
    measured = chunks(segment);
  const fraction = Math.max(0, Math.min(1, word / count));
  if (!measured.length)
    return fraction * (segment?.duration || (count / 145) * 60);
  let remaining =
    fraction * measured.reduce((sum, chunk) => sum + chunk.words, 0);
  for (const chunk of measured) {
    if (remaining < chunk.words)
      return (
        chunk.start + ((chunk.end - chunk.start) * remaining) / chunk.words
      );
    remaining -= chunk.words;
  }
  return measured.at(-1).end;
}

export function sentenceAtWord(segments, word) {
  let end = 0;
  for (let i = 0; i < segments.length; i++) {
    end += words(segments[i]);
    if (word < end) return i;
  }
  return Math.max(0, segments.length - 1);
}

/** Split at authored heading boundaries while preserving every spoken character. */
export function transcriptBlocks(text, headings = [], offset = 0) {
  const tokens = [...text.matchAll(/\S+/g)];
  const result = [];
  let cursor = 0;
  const character = (word) => tokens[word]?.index ?? text.length;
  for (const heading of headings) {
    if (
      !Number.isInteger(heading.start) ||
      !Number.isInteger(heading.end) ||
      heading.start < 0 ||
      heading.end < heading.start
    )
      continue;
    if (heading.spoken === false) {
      if (heading.start < offset || heading.start >= offset + tokens.length)
        continue;
      const position = character(heading.start - offset);
      if (position > cursor)
        result.push({ kind: "body", text: text.slice(cursor, position) });
      result.push({
        kind: "heading",
        text: heading.text,
        level: heading.level,
        spoken: false,
      });
      cursor = position;
    } else {
      if (heading.start >= offset + tokens.length || heading.end <= offset)
        continue;
      const start = character(Math.max(0, heading.start - offset)),
        end = character(Math.min(tokens.length, heading.end - offset));
      if (start < cursor) continue;
      if (start > cursor)
        result.push({ kind: "body", text: text.slice(cursor, start) });
      result.push({
        kind: "heading",
        text: text.slice(start, end),
        level: heading.level,
        spoken: true,
      });
      cursor = end;
    }
  }
  if (cursor < text.length)
    result.push({ kind: "body", text: text.slice(cursor) });
  return result;
}

const pageStructures = new WeakMap(),
  noHeadings = [];
export function recordingTranscriptParts(row, recording, index) {
  const headings = row?.transcript_headings || noHeadings;
  let cached = pageStructures.get(recording);
  if (
    !cached ||
    cached.headings !== headings ||
    cached.transcript !== row?.transcript
  ) {
    const matches =
      typeof row?.transcript === "string" &&
      recording.pages.join(" ").split(/\s+/).filter(Boolean).join(" ") ===
        row.transcript.split(/\s+/).filter(Boolean).join(" ");
    let offset = 0;
    const pages = recording.pages.map((page) => {
      let sentence = 0,
        prefix = "";
      const parts = [];
      for (const block of transcriptBlocks(
        page,
        matches ? headings : [],
        offset,
      )) {
        if (block.spoken === false) {
          parts.push(block);
          continue;
        }
        const values =
          block.kind === "heading" ? [block.text] : speechSegments(block.text);
        for (const text of values) {
          if (!words(text)) {
            if (parts.length && parts.at(-1).spoken !== false)
              parts.at(-1).text += text;
            else prefix += text;
            continue;
          }
          parts.push({ ...block, text: prefix + text, sentence: sentence++ });
          prefix = "";
        }
      }
      offset += words(page);
      return parts;
    });
    cached = { headings, transcript: row?.transcript, pages };
    pageStructures.set(recording, cached);
  }
  return cached.pages[index] || [];
}
export function pageSpeechSegments(row, recording, index) {
  return recordingTranscriptParts(row, recording, index)
    .filter((part) => part.spoken !== false)
    .map((part) => part.text);
}

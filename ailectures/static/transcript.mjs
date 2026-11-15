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

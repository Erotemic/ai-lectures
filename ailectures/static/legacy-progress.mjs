// Read old keys without changing or deleting them. The old reader stored a page
// selection, not a timestamp, completion state or source/recording revision.
export function legacyPositions(storage) {
  const positions = [];
  for (let i = 0; i < storage.length; i++) {
    const key = storage.key(i),
      match = /^dkps-audio-page-([a-z0-9][a-z0-9._-]*)-([0-9]{6})$/.exec(key);
    if (!match) continue;
    try {
      const page = JSON.parse(storage.getItem(key));
      if (!Number.isInteger(page) || page < 0) continue;
      const snapshots = [];
      const prefix = `dkps-audio-durations-${match[1]}-${match[2]}-`;
      for (let j = 0; j < storage.length; j++) {
        const durationKey = storage.key(j);
        if (!durationKey.startsWith(prefix)) continue;
        try {
          const [
            source_modified,
            page_chars,
            page_count,
            pagination_version,
            settings,
          ] = JSON.parse(decodeURIComponent(durationKey.slice(prefix.length)));
          const durations = JSON.parse(storage.getItem(durationKey));
          if (
            Number.isInteger(page_count) &&
            page_count > page &&
            Array.isArray(durations)
          )
            snapshots.push({
              source_modified,
              page_chars,
              page_count,
              pagination_version,
              settings,
              durations,
            });
        } catch {} // An incomplete browser key does not hide other history.
      }
      positions.push({
        lecture_id: `${match[1]}:${match[2]}`,
        revision: null,
        release: null,
        spoken_sha256: null,
        recording_id: null,
        segment: page,
        seconds: 0,
        completed: false,
        legacy: { page_index: page, storage_key: key, snapshots },
      });
    } catch {}
  }
  return positions;
}

export function approximateLegacyPosition(position, recording) {
  const page = position.legacy.page_index;
  const counts = new Set(
    position.legacy.snapshots.map((snapshot) => snapshot.page_count),
  );
  // A single known old layout permits an approximate lecture fraction. Multiple
  // layouts cannot establish which one was active when the selected page saved.
  if (counts.size === 1) {
    const pageFraction = page / [...counts][0];
    const durations = recording.pages.map(
      (text, index) =>
        recording.segments.find((s) => s.index === index)?.duration ||
        (text.split(/\s+/).length / 145) * 60,
    );
    let seconds =
      pageFraction * durations.reduce((sum, value) => sum + value, 0);
    for (let index = 0; index < durations.length; index++) {
      if (seconds < durations[index] || index === durations.length - 1)
        return { index, seconds };
      seconds -= durations[index];
    }
  }
  return { index: Math.min(page, recording.pages.length - 1), seconds: 0 };
}

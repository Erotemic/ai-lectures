import { getStored, store, post } from "./api.mjs";

export function mergeSharedProgress(remote, local, pending) {
  const merged = { ...remote };
  const queued = new Set(pending.map((p) => p.lecture_id));
  for (const [id, position] of Object.entries(local)) {
    // A GET can finish after a checkpoint or its POST. Neither a queued local
    // position nor a newer acknowledged version may be replaced by that GET.
    if (queued.has(id) || position.version > (remote[id]?.version || 0))
      merged[id] = position;
  }
  for (const position of pending)
    if (!local[position.lecture_id]) merged[position.lecture_id] = position;
  return merged;
}

export class ProgressSync {
  constructor({ onSaved, onConflict, onError }) {
    Object.assign(this, { onSaved, onConflict, onError });
    this.flushing = new Map();
    this.conflicts = new Map();
  }

  flush(profile) {
    if (!profile) return Promise.resolve();
    if (this.flushing.has(profile)) return this.flushing.get(profile);
    if (this.conflicts.has(profile)) {
      this.onConflict(this.conflicts.get(profile));
      return Promise.resolve();
    }
    const work = this.drain(profile).finally(() => this.flushing.delete(profile));
    this.flushing.set(profile, work);
    return work;
  }

  async drain(profile) {
    while (true) {
      const queue = getStored("pending:" + profile, []);
      if (!queue.length) return;
      const payload = queue[0];
      try {
        const result = await post(
          "/api/listeners/" + encodeURIComponent(profile) + "/progress",
          payload,
        );
        const remaining = getStored("pending:" + profile, []).filter(
          (p) => p.update_id !== payload.update_id,
        );
        const state = getStored("progress:" + profile, {});
        if (!remaining.some((p) => p.lecture_id === payload.lecture_id))
          state[payload.lecture_id] = result;
        store("progress:" + profile, state);
        store("pending:" + profile, remaining);
        this.onSaved(profile, state);
      } catch (error) {
        if (error.status === 409 && error.data?.conflict) {
          const conflict = { profile, payload, current: error.data.current };
          // Replaying a rejected event returns the same stored conflict. Wait
          // for a choice instead of retrying it on every poll and checkpoint.
          this.conflicts.set(profile, conflict);
          this.onConflict(conflict);
        } else this.onError(error);
        return;
      }
    }
  }

  useLocal(conflict, payload) {
    const { profile } = conflict;
    const remaining = getStored("pending:" + profile, []).filter(
      (p) => p.lecture_id !== payload.lecture_id,
    );
    const state = getStored("progress:" + profile, {});
    state[payload.lecture_id] = {
      ...payload,
      updated_at: new Date().toISOString(),
      version: payload.expected_version + 1,
    };
    // New checkpoints must build on the rebased version while this POST is in
    // flight, rather than the discarded queue's optimistic version count.
    store("progress:" + profile, state);
    store("pending:" + profile, [payload, ...remaining]);
    this.conflicts.delete(profile);
    this.onSaved(profile, state);
  }

  keepShared(conflict) {
    const { profile, payload, current } = conflict;
    const remaining = getStored("pending:" + profile, []).filter(
      (p) => p.lecture_id !== payload.lecture_id,
    );
    const state = getStored("progress:" + profile, {});
    if (current) state[payload.lecture_id] = current;
    else delete state[payload.lecture_id];
    store("progress:" + profile, state);
    store("pending:" + profile, remaining);
    this.conflicts.delete(profile);
    this.onSaved(profile, state);
  }
}

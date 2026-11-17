import { api, post, getStored, store, randomId } from "./api.mjs";

export function mergeKnowledge(remote, local, pending = []) {
  const result = { ...remote };
  const waiting = new Set(pending.map(event => event.lecture_id));
  for (const [id, record] of Object.entries(local)) {
    const shared = remote[id];
    if (waiting.has(id) || !shared ||
        [record.updated_at || "", record.update_id || ""].join("/") >
        [shared.updated_at || "", shared.update_id || ""].join("/")) result[id] = record;
  }
  return result;
}

export function familiarityStatus(record, node) {
  if (!record) return "unknown";
  const revision = node?.knowledge_revision || node?.revision;
  if (record.status === "known" && revision && revision !== record.revision) return "uncertain";
  return record.status;
}

export function migrateLearningState(previous, current) {
  const oldKey = "knowledge:" + previous, newKey = "knowledge:" + current;
  const oldPending = "knowledge-pending:" + previous, newPending = "knowledge-pending:" + current;
  const oldRecords = getStored(oldKey, {}), newRecords = getStored(newKey, {});
  const events = [...new Map([...getStored(oldPending, []), ...getStored(newPending, [])].map(event => [event.id, event])).values()];
  const records = mergeKnowledge(oldRecords, newRecords);
  for (const event of events) {
    const prior = oldRecords[event.lecture_id], latest = newRecords[event.lecture_id];
    records[event.lecture_id] = latest?.update_id === event.id ? latest : prior?.update_id === event.id ? prior :
      { lecture_id: event.lecture_id, status: event.status, revision: event.revision, update_id: event.id, updated_at: "" };
  }
  store(newKey, records);
  store(newPending, events);
  store(oldPending, []);
}

// An immutable listener selection keeps in-flight writes out of another profile.
export class LearningState {
  constructor(profile = "", context = {}) {
    this.profile = profile;
    this.api = context.api || api;
    this.post = context.post || post;
    this.key = "knowledge:" + (profile || "device");
    this.pendingKey = "knowledge-pending:" + (profile || "device");
    this.records = getStored(this.key, {});
  }
  async load() {
    if (!this.profile) return this.records;
    await this.flush();
    try {
      const remote = await this.api("/api/listeners/" + encodeURIComponent(this.profile) + "/learning");
      this.records = mergeKnowledge(remote.knowledge, getStored(this.key, {}), getStored(this.pendingKey, []));
      store(this.key, this.records);
    } catch (error) { this.error = error.message; }
    return this.records;
  }
  async setMany(entries) {
    const pending = getStored(this.pendingKey, []);
    this.records = getStored(this.key, {});
    for (const { id: lecture_id, status, revision = null } of entries) {
      if (!["known", "uncertain", "unknown"].includes(status)) throw new Error("Invalid familiarity choice");
      const event = { id: randomId(), lecture_id, status, revision };
      this.records[lecture_id] = { lecture_id, status, revision, update_id: event.id, updated_at: new Date().toISOString() };
      if (this.profile) pending.push(event);
    }
    store(this.key, this.records);
    if (this.profile) store(this.pendingKey, pending);
    await this.flush();
    return this.records;
  }
  async flush() {
    if (!this.profile) return;
    if (this.sending) return this.sending;
    this.sending = this.send();
    try { await this.sending; } finally { this.sending = null; }
  }
  async send() {
    this.error = null;
    while (getStored(this.pendingKey, []).length) {
      const event = getStored(this.pendingKey, [])[0];
      try {
        const saved = await this.post("/api/listeners/" + encodeURIComponent(this.profile) + "/learning", event);
        this.records = getStored(this.key, {});
        if (this.records[event.lecture_id]?.update_id === event.id) this.records[event.lecture_id] = saved;
        store(this.key, this.records);
        store(this.pendingKey, getStored(this.pendingKey, []).filter(item => item.id !== event.id));
      } catch (error) { this.error = error.message; break; }
    }
  }
}

export function planRequest(data, settings, knowledge) {
  const course = data.collections.find(row => row.id === settings.collection);
  const scope = course ? course.lectures : Object.values(data.nodes)
    .filter(node => node.kind === "lecture" && (!settings.category || node.categories?.includes(settings.category))).map(node => node.id);
  let goals = [];
  if (settings.mode === "goal" && settings.goal) goals = [settings.goal];
  if (settings.mode === "collection" && course) {
    const begin = settings.start ? course.lectures.indexOf(settings.start) : 0;
    goals = course.lectures.slice(Math.max(0, begin));
  }
  return { goals, scope, order_hint: course?.lectures || [],
    start: settings.mode === "collection" ? settings.start || null : null,
    known: Object.entries(knowledge).filter(([id, row]) => familiarityStatus(row, data.nodes[id]) === "known").map(([id]) => id),
    uncertain: Object.entries(knowledge).filter(([id, row]) => familiarityStatus(row, data.nodes[id]) === "uncertain").map(([id]) => id),
    assume_uncertain: Boolean(settings.assume_uncertain), include_soft: Boolean(settings.include_soft), include_proof: Boolean(settings.include_proof),
  };
}

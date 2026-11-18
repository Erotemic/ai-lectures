import { api, post, getStored, store, randomId, el } from "./api.mjs";

const order = record => `${record.updated_at}/${record.update_id}`;
export function mergeReactions(...sources) {
  const result = {};
  for (const source of sources) for (const [id, fields] of Object.entries(source)) {
    result[id] ||= {};
    for (const [field, record] of Object.entries(fields))
      if (!result[id][field] || order(record) > order(result[id][field])) result[id][field] = record;
  }
  return result;
}
export const reactionValue = (records, id, field) => records[id]?.[field]?.value ?? (field === "favorite" ? false : null);

export function migrateReactions(previous, current) {
  const before = new ReactionState(previous), after = new ReactionState(current);
  store(after.key, mergeReactions(getStored(before.key, {}), getStored(after.key, {})));
  store(after.pendingKey, [...new Map([...getStored(before.pendingKey, []), ...getStored(after.pendingKey, [])].map(event => [event.update_id, event])).values()]);
  store(before.pendingKey, []);
}

// Each instance keeps its original listener even if a request outlives a switch.
export class ReactionState {
  constructor(profile = "", context = {}) {
    this.profile = profile;
    this.api = context.api || api;
    this.post = context.post || post;
    this.key = "reactions:" + (profile || "device");
    this.pendingKey = "reactions-pending:" + (profile || "device");
    this.records = getStored(this.key, {});
    this.watchers = new Map();
  }
  watch(root, draw) { this.watchers.set(root, draw); }
  notify() {
    for (const [root, draw] of [...this.watchers])
      if (root.isConnected) draw(); else this.watchers.delete(root);
  }
  value(id, field) { return reactionValue(this.records, id, field); }
  async load() {
    if (!this.profile) return;
    await this.flush();
    try {
      const remote = await this.api(`/api/listeners/${encodeURIComponent(this.profile)}/reactions`);
      const records = mergeReactions(remote, getStored(this.key, {}));
      const changed = JSON.stringify(records) !== JSON.stringify(this.records);
      this.records = records;
      store(this.key, records);
      if (changed) this.notify();
    } catch (error) { this.error = error.message; }
  }
  set(row, field, value) {
    if (field === "rating" ? value !== null && (!Number.isInteger(value) || value < 1 || value > 5)
      : field !== "favorite" || typeof value !== "boolean") throw new Error("Invalid lecture reaction");
    this.records = getStored(this.key, {});
    const previous = this.records[row.id]?.[field];
    const event = { lecture_id: row.id, field, value, revision: row.revision || null,
      update_id: randomId(), updated_at: new Date(Math.max(Date.now(), Date.parse(previous?.updated_at || "") + 1 || 0)).toISOString() };
    this.records = mergeReactions(this.records, { [row.id]: { [field]: event } });
    store(this.key, this.records);
    if (this.profile) store(this.pendingKey, [...getStored(this.pendingKey, []), event]);
    this.notify();
    return this.flush().then(() => this.notify());
  }
  async flush() {
    if (!this.profile) return;
    if (this.sending) return this.sending;
    this.sending = Promise.resolve().then(() => this.send());
    try { await this.sending; } finally { this.sending = null; }
  }
  async send() {
    this.error = null;
    while (getStored(this.pendingKey, []).length) {
      const event = getStored(this.pendingKey, [])[0];
      try {
        const saved = await this.post(`/api/listeners/${encodeURIComponent(this.profile)}/reactions`, event);
        this.records = mergeReactions(getStored(this.key, {}), { [saved.lecture_id]: { [saved.field]: saved } });
        store(this.key, this.records);
        store(this.pendingKey, getStored(this.pendingKey, []).filter(item => item.update_id !== event.update_id));
      } catch (error) { this.error = error.message; break; }
    }
  }
}

export function reactionControls(row, state, { compact = false } = {}) {
  const root = el("div", { class: "lecture-reactions" + (compact ? " compact" : ""), "aria-label": "Your lecture feedback" });
  const heart = el("button", { type: "button", class: "favorite-toggle" });
  heart.onclick = () => state.set(row, "favorite", !state.value(row.id, "favorite"));
  const rating = el("span", { class: "rating-value" });
  const stars = el("div", { class: "rating-stars", role: "group", "aria-label": "Rate this lecture" });
  const choices = Array.from({ length: 5 }, (_, index) => el("button", {
    type: "button", text: "★", "aria-label": `Rate ${index + 1} ${index ? "stars" : "star"}`,
    title: `${index + 1} ${index ? "stars" : "star"}`, onclick: () => state.set(row, "rating", index + 1),
  }));
  stars.append(...choices);
  const clear = el("button", { type: "button", class: "clear-rating", text: "Clear rating", onclick: () => state.set(row, "rating", null) });
  const status = el("small", { class: "muted reaction-save-status", role: "status" });
  root.append(heart, ...(compact ? [rating] : [stars, rating, clear, status]));
  function draw() {
    const favorite = state.value(row.id, "favorite"), value = state.value(row.id, "rating");
    heart.textContent = favorite ? "♥" : "♡";
    heart.setAttribute("aria-label", favorite ? "Remove from favorites" : "Add to favorites");
    heart.title = favorite ? "Remove from favorites" : "Add to favorites";
    heart.setAttribute("aria-pressed", String(favorite));
    rating.textContent = value ? `${value}/5 stars` : compact ? "" : "Not rated";
    choices.forEach((choice, index) => {
      choice.classList.toggle("filled", index < value);
      choice.setAttribute("aria-pressed", String(index + 1 === value));
    });
    clear.hidden = value === null;
    status.textContent = state.error ? "Saved on this device; sharing will retry."
      : getStored(state.pendingKey, []).length ? "Saved on this device; syncing…"
      : state.profile ? "Saved for this listener" : "Saved on this device";
  }
  draw();
  state.watch(root, draw);
  return root;
}

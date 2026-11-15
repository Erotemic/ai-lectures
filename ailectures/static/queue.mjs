import { api, post, el, getStored, store } from "./api.mjs";

export function editDeviceQueue(entries, operation) {
  if (operation.action === "add") {
    const existing = entries.find((entry) => entry.id === operation.entry.id);
    if (
      existing &&
      JSON.stringify(existing) !== JSON.stringify(operation.entry)
    )
      throw new Error("Queue entry ID has conflicting content.");
    return existing ? entries : [...entries, operation.entry];
  }
  const result = entries.filter(
    (entry) => entry.id !== (operation.id || operation.entry?.id),
  );
  if (operation.action === "remove") return result;
  const item = entries.find((entry) => entry.id === operation.id);
  if (!item) throw new Error("This queue entry has already been removed.");
  if (operation.before === operation.id) return entries;
  const index = operation.before
    ? result.findIndex((entry) => entry.id === operation.before)
    : result.length;
  if (index < 0)
    throw new Error("The queue changed; refresh before moving this item.");
  result.splice(index, 0, item);
  return result;
}

export class ListeningQueue {
  constructor({ profile, lectures, play, message }) {
    Object.assign(this, { profile, lectures, play, message });
  }
  async read(selected = this.profile()) {
    const key = "queue:" + (selected || "device");
    const entries = selected
      ? (await api("/api/listeners/" + encodeURIComponent(selected) + "/queue"))
          .entries
      : getStored(key, []);
    store(key, entries);
    return entries;
  }
  async edit(operation) {
    const selected = this.profile(),
      key = "queue:" + (selected || "device");
    const entries = selected
      ? (
          await post(
            "/api/listeners/" + encodeURIComponent(selected) + "/queue",
            operation,
          )
        ).entries
      : editDeviceQueue(getStored(key, []), operation);
    store(key, entries);
    if (selected === this.profile() && this.container?.isConnected)
      await this.render(this.container);
    return entries;
  }
  async add(lecture_id, course_id = null) {
    await this.edit({
      action: "add",
      entry: { id: crypto.randomUUID(), lecture_id, course_id },
    });
    this.message("Added to your listening queue.");
  }
  async advance(id) {
    try {
      const selected = this.profile();
      const entries = await this.read(),
        index = entries.findIndex((entry) => entry.id === id);
      if (selected !== this.profile()) return;
      if (index < 0)
        return this.message(
          "The playing lecture was removed from the queue. Choose the next lecture in Listening.",
        );
      const next = entries[index + 1];
      await this.edit({ action: "remove", id });
      if (next) {
        if (this.lectures().some((row) => row.id === next.lecture_id))
          this.play(next);
        else
          this.message(
            "The next queued lecture is not installed. Your queue is retained in Listening.",
          );
      }
    } catch (error) {
      this.message(error.message);
    }
  }
  async render(container) {
    this.container = container;
    const token = (this.renderToken = (this.renderToken || 0) + 1);
    const selected = this.profile();
    try {
      const entries = await this.read(selected);
      if (selected !== this.profile() || token !== this.renderToken) return;
      this.draw(container, entries);
    } catch (error) {
      if (selected !== this.profile() || token !== this.renderToken) return;
      this.draw(container, getStored("queue:" + (selected || "device"), []));
      container.append(el("p", { class: "notice", text: error.message }));
    }
  }
  draw(container, entries) {
    container.querySelector(".notice")?.remove();
    const signature = JSON.stringify([this.profile(), entries]);
    if (container === this.renderedContainer && signature === this.signature)
      return;
    this.renderedContainer = container;
    this.signature = signature;
    container.replaceChildren(el("h2", { text: "Listening queue" }));
    const action = (text, callback, attrs = {}) =>
      el("button", {
        type: "button",
        text,
        ...attrs,
        onclick: () =>
          Promise.resolve(callback()).catch((error) =>
            this.message(error.message),
          ),
      });
    const list = el("ol", { class: "list" });
    entries.forEach((entry, index) => {
      const row = this.lectures().find((row) => row.id === entry.lecture_id);
      const controls = el(
        "div",
        { class: "actions" },
        action("Play", () => this.play(entry), { disabled: !row }),
        action(
          "↑",
          () =>
            this.edit({
              action: "move",
              id: entry.id,
              before: entries[index - 1].id,
            }),
          { disabled: index === 0, "aria-label": "Move up" },
        ),
        action(
          "↓",
          () =>
            this.edit({
              action: "move",
              id: entry.id,
              before: entries[index + 2]?.id || null,
            }),
          { disabled: index === entries.length - 1, "aria-label": "Move down" },
        ),
        action("Remove", () => this.edit({ action: "remove", id: entry.id })),
      );
      list.append(
        el(
          "li",
          {},
          el(
            "div",
            { class: "copy" },
            el("strong", { text: row?.title || entry.lecture_id }),
            !row
              ? el("small", { text: "Not installed · queue entry retained" })
              : null,
          ),
          controls,
        ),
      );
    });
    container.append(list);
    if (!entries.length)
      container.append(
        el("p", {
          class: "muted",
          text: "Add lectures from their lecture pages. Reorder them here and choose Play to start the queue.",
        }),
      );
  }
}

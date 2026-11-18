import { randomId, api, post, el, lectureURL, clock } from "./api.mjs";

export function feedbackThreads(events) {
  const threads = new Map();
  for (const event of events)
    if (event.type === "submission")
      threads.set(event.id, { submission: event, status: "open", history: [] });
  for (const event of events) {
    const thread = threads.get(event.feedback_id);
    if (event.type === "status" && thread) {
      thread.status = event.status;
      thread.history.push(event);
    }
  }
  return [...threads.values()].reverse();
}

// Show the changed span, retaining any unchanged passages between separate edits.
export function changedPassages(before, after) {
  const old = before.split("\n\n"),
    current = after.split("\n\n");
  let first = 0,
    endOld = old.length,
    endCurrent = current.length;
  while (first < endOld && first < endCurrent && old[first] === current[first])
    first++;
  while (
    endOld > first &&
    endCurrent > first &&
    old[endOld - 1] === current[endCurrent - 1]
  ) {
    endOld--;
    endCurrent--;
  }
  return {
    changed: before !== after,
    before: old.slice(first, endOld).join("\n\n"),
    after: current.slice(first, endCurrent).join("\n\n"),
  };
}

const statuses = ["open", "triaged", "resolved", "reopened", "superseded"];
const navLink = (text, href) => el("a", { href, "data-nav": "", text });

export async function reviewFeedback(main, lectures) {
  const root = el("section");
  main.replaceChildren(root);
  root.append(
    el("h1", { text: "Lecture feedback" }),
    el("p", {
      class: "intro",
      text: "Review comments against the transcript that prompted them. Revisions leave feedback open until you explicitly change its status.",
    }),
    navLink("Back to packs", "/packs"),
  );
  const reactions = el("details", { class: "section" },
    el("summary", { text: "Star ratings & favorites" }),
    el("p", { class: "muted", text: "Totals from shared listeners. Each listener contributes their current rating and favorite choice once per lecture. Device-only choices stay on that device; comments retain their separate editorial history." }));
  const reactionList = el("ul", { class: "list" });
  reactions.append(reactionList);
  root.append(reactions);
  let reactionTotals = {};
  try { reactionTotals = await api("/api/library/reactions"); }
  catch { reactionList.append(el("p", { text: "Rating totals are temporarily unavailable." })); }
  const filter = el(
    "select",
    { "aria-label": "Feedback status" },
    el("option", { value: "unresolved", text: "Unresolved" }),
    el("option", { value: "all", text: "All feedback" }),
    ...statuses.map((status) => el("option", { value: status, text: status })),
  );
  const search = el("input", {
    type: "search",
    placeholder: "Search feedback",
    "aria-label": "Search feedback",
  });
  const list = el("div", { class: "feedback-list" });
  root.append(
    el("div", { class: "filters" }, search, el("label", {}, "Status", filter)),
    list,
  );
  let events = (await api("/api/library/feedback")).events;
  function draw() {
    const rated = Object.entries(reactionTotals).filter(([id]) =>
      (lectures.find(row => row.id === id)?.title || id).toLowerCase().includes(search.value.toLowerCase()));
    reactionList.replaceChildren(...rated.sort((a, b) => b[1].ratings - a[1].ratings || a[0].localeCompare(b[0])).map(([id, value]) => {
      const row = lectures.find(row => row.id === id);
      return el("li", {}, el("div", { class: "copy" }, navLink(row?.title || id, lectureURL(id)),
        el("small", { text: `${value.average === null ? "Not rated" : value.average.toFixed(1) + "/5 stars · " + value.ratings + " rating" + (value.ratings === 1 ? "" : "s")} · ♥ ${value.favorites}` }),
        value.ratings ? el("small", { text: value.distribution.map((count, index) => `${index + 1}★: ${count}`).join(" · ") }) : null));
    }));
    if (!rated.length) reactionList.append(el("li", { text: "No shared ratings or favorites match this selection." }));
    const threads = feedbackThreads(events).filter(({ submission, status }) => {
      const matches =
        filter.value === "all" ||
        (filter.value === "unresolved"
          ? ["open", "triaged", "reopened"].includes(status)
          : status === filter.value);
      const row = lectures.find((row) => row.id === submission.lecture_id);
      return (
        matches &&
        `${row?.title || submission.lecture_id} ${submission.text}`
          .toLowerCase()
          .includes(search.value.toLowerCase())
      );
    });
    list.replaceChildren(...threads.map(card));
    if (!threads.length)
      list.append(
        el("p", {
          class: "muted",
          text: "No feedback matches this selection.",
        }),
      );
  }
  function card({ submission, status, history }) {
    const summary = lectures.find((row) => row.id === submission.lecture_id);
    const article = el(
      "article",
      { class: "card" },
      el(
        "h2",
        {},
        summary
          ? navLink(summary.title, lectureURL(summary.id))
          : submission.lecture_id,
      ),
      el("span", { class: "badge", text: status }),
      el("p", { class: "feedback-text", text: submission.text }),
      el("p", { class: "muted", text: submission.created_at }),
    );
    const currentLecture = () =>
      api("/api/library/lectures/" + encodeURIComponent(submission.lecture_id));
    const context = el(
      "details",
      {},
      el("summary", { text: "Transcript context and revisions" }),
    );
    if (submission.recording)
      context.append(
        el("p", {
          text: `${submission.recording.variant} · passage ${submission.recording.segment + 1} · ${clock(submission.recording.seconds)}`,
        }),
      );
    if (submission.context)
      context.append(el("blockquote", { text: submission.context }));
    context.append(
      el(
        "details",
        {},
        el("summary", { text: "Submitted transcript" }),
        el("pre", { text: submission.transcript_snapshot }),
      ),
    );
    const comparison = el("div");
    const compare = el("button", {
      type: "button",
      text: "Compare with current lecture",
    });
    compare.onclick = async () => {
      try {
        const row = await currentLecture();
        const diff = changedPassages(
          submission.transcript_snapshot,
          row.transcript,
        );
        comparison.replaceChildren(
          el("p", {
            text: diff.changed
              ? "Changed passages; unchanged beginning and end omitted."
              : "The spoken transcript is unchanged.",
          }),
        );
        if (diff.changed)
          comparison.append(
            el(
              "div",
              { class: "revision-comparison" },
              el(
                "section",
                {},
                el("h3", { text: "When submitted" }),
                el("pre", { text: diff.before || "(No passage)" }),
              ),
              el(
                "section",
                {},
                el("h3", { text: "Current lecture" }),
                el("pre", { text: diff.after || "(No passage)" }),
              ),
            ),
          );
        comparison.append(
          el(
            "details",
            {},
            el("summary", { text: "Revision identifiers" }),
            el("pre", {
              text: `Submitted: ${submission.revision}\nCurrent: ${row.revision}`,
            }),
          ),
        );
      } catch (error) {
        comparison.replaceChildren(
          el("p", {
            class: "notice",
            text:
              error.status === 404
                ? "This lecture is not installed. Its submitted transcript is retained here."
                : error.message,
          }),
        );
      }
    };
    context.append(compare, comparison);
    article.append(context);
    const select = el(
      "select",
      { "aria-label": "Editorial status" },
      ...statuses.map((value) => el("option", { value, text: value })),
    );
    select.value = status;
    const addressed = el("input", { type: "checkbox" });
    const note = el("textarea", {
      rows: 2,
      maxlength: 4000,
      "aria-label": "Editorial note",
    });
    const result = el("p", { role: "status" });
    const form = el(
      "form",
      { class: "section" },
      el("label", {}, "Status", select),
      el("label", {}, "Editorial note (optional)", note),
      el(
        "label",
        { class: "check" },
        addressed,
        "Record the current lecture revision as addressed",
      ),
      el("button", { type: "submit", text: "Save status" }),
      result,
    );
    let pending;
    form.onsubmit = async (event) => {
      event.preventDefault();
      try {
        const revision = addressed.checked
          ? (await currentLecture()).revision
          : null;
        const change = {
          lecture_id: submission.lecture_id,
          feedback_id: submission.id,
          status: select.value,
          note: note.value,
          addressed_revision: revision,
        };
        if (
          !pending ||
          JSON.stringify(pending.change) !== JSON.stringify(change)
        )
          pending = {
            change,
            id: randomId(),
            created_at: new Date().toISOString(),
          };
        const saved = await post("/api/library/feedback/status", {
          ...pending.change,
          id: pending.id,
          created_at: pending.created_at,
        });
        events.push(saved);
        draw();
      } catch (error) {
        result.textContent = error.message;
      }
    };
    article.append(form);
    if (history.length)
      article.append(
        el(
          "details",
          {},
          el("summary", { text: "Status history" }),
          el(
            "ol",
            {},
            ...history.map((event) =>
              el(
                "li",
                {},
                el("p", { text: `${event.status} · ${event.created_at}` }),
                event.note
                  ? el("p", { class: "feedback-text", text: event.note })
                  : null,
                event.addressed_revision
                  ? el("code", { text: event.addressed_revision })
                  : null,
              ),
            ),
          ),
        ),
      );
    return article;
  }
  filter.onchange = draw;
  search.oninput = draw;
  draw();
}

import { api, post, el, getStored, store, lectureURL, clock } from "./api.mjs";
import { Player } from "./player.mjs";
const $ = (id) => document.getElementById(id);
let catalog = { lectures: [], courses: [], packs: [] },
  profile = getStored("listener", ""),
  progress = {},
  currentCourse = null,
  pendingConflict = null;
let search = "",
  subject = "",
  availability = "",
  limit = 24,
  renderToken = 0;
const device = getStored("device") || crypto.randomUUID();
store("device", device);
let sequence = getStored("sequence", 0),
  saveChain = Promise.resolve();
const message = (text) => {
  $("message").textContent = text || "";
};
const link = (text, href) =>
  el("a", {
    href,
    ...(href.startsWith("/presentations") ? {} : { "data-nav": "" }),
    text,
  });
const button = (text, action, primary = false) =>
  el("button", {
    type: "button",
    class: primary ? "primary" : "",
    onclick: () => Promise.resolve(action()).catch((e) => message(e.message)),
    text,
  });
const description = (text) => el("p", { class: "intro", text });
const title = (text) => el("h1", { text });
const byId = (id) => catalog.lectures.find((r) => r.id === id);
const ready = (row) => row?.recordings.some((r) => r.complete);
const badgeText = (row) =>
  row?.kind === "presentation"
    ? "Presentation"
    : ready(row)
      ? "Ready to play"
      : row?.recordings.length
        ? "Partial audio"
        : "Transcript available";
const badge = (row) => el("span", { class: "badge", text: badgeText(row) });
const courseLink = (course) => "/courses/" + encodeURIComponent(course.id);
const lectureLink = (id, course = null) =>
  byId(id)?.kind === "presentation"
    ? "/presentations?deck=" + encodeURIComponent(byId(id).deck)
    : lectureURL(id) + (course ? "?course=" + encodeURIComponent(course) : "");
const contextKey = () => profile || "device";
function persistProgress() {
  store("progress:" + contextKey(), progress);
}
function saveCheckpoint(position) {
  if (!position) return;
  const selectedProfile = profile,
    key = selectedProfile || "device";
  const state = getStored("progress:" + key, {}),
    old = state[position.lecture_id];
  const payload = {
    ...position,
    course_id: position.course_id || currentCourse,
    completed: position.explicit_completion
      ? position.completed
      : position.completed || old?.completed || false,
    update_id: crypto.randomUUID(),
    device_id: device,
    sequence: ++sequence,
    expected_version: old?.version || 0,
  };
  store("sequence", sequence);
  state[position.lecture_id] = {
    ...payload,
    updated_at: new Date().toISOString(),
    version: (old?.version || 0) + (selectedProfile ? 1 : 0),
  };
  store("progress:" + key, state);
  if (profile === selectedProfile) progress = state;
  if (!selectedProfile) return;
  const queue = getStored("pending:" + selectedProfile, []);
  queue.push(payload);
  store("pending:" + selectedProfile, queue);
  saveChain = saveChain
    .then(() => flushProgress(selectedProfile))
    .catch((e) => message(e.message));
}
const flushing = new Map();
function flushProgress(selectedProfile = profile) {
  if (!selectedProfile) return Promise.resolve();
  if (flushing.has(selectedProfile)) return flushing.get(selectedProfile);
  const work = (async () => {
    while (true) {
      const queue = getStored("pending:" + selectedProfile, []);
      if (!queue.length) return;
      const payload = queue[0];
      try {
        const result = await post(
          "/api/listeners/" + encodeURIComponent(selectedProfile) + "/progress",
          payload,
        );
        const remaining = getStored("pending:" + selectedProfile, []).filter(
          (p) => p.update_id !== payload.update_id,
        );
        const state = getStored("progress:" + selectedProfile, {});
        if (
          !remaining.some(
            (p) =>
              p.lecture_id === payload.lecture_id &&
              p.sequence > payload.sequence,
          )
        )
          state[payload.lecture_id] = result;
        store("progress:" + selectedProfile, state);
        store("pending:" + selectedProfile, remaining);
        if (profile === selectedProfile) progress = state;
      } catch (error) {
        if (error.status === 409 && error.data?.conflict) {
          pendingConflict = {
            profile: selectedProfile,
            payload,
            current: error.data.current,
          };
          $("progress-conflict").hidden = false;
        } else if (error.status !== 409)
          message(
            "Progress is saved on this device and will sync when the server is reachable.",
          );
        return;
      }
    }
  })().finally(() => flushing.delete(selectedProfile));
  flushing.set(selectedProfile, work);
  return work;
}
$("use-local").onclick = async () => {
  if (!pendingConflict) return;
  const c = pendingConflict;
  const queue = getStored("pending:" + c.profile, []);
  const latest =
    [...queue].reverse().find((p) => p.lecture_id === c.payload.lecture_id) ||
    c.payload;
  const payload = {
    ...latest,
    expected_version: c.current?.version || 0,
    update_id: crypto.randomUUID(),
    sequence: ++sequence,
  };
  store("sequence", sequence);
  store(
    "pending:" + c.profile,
    queue.filter((p) => p.lecture_id !== c.payload.lecture_id),
  );
  const rest = getStored("pending:" + c.profile, []);
  rest.unshift(payload);
  store("pending:" + c.profile, rest);
  pendingConflict = null;
  $("progress-conflict").hidden = true;
  await flushProgress(c.profile);
};
$("keep-shared").onclick = () => {
  if (!pendingConflict) return;
  const c = pendingConflict;
  store(
    "pending:" + c.profile,
    getStored("pending:" + c.profile, []).filter(
      (p) => p.lecture_id !== c.payload.lecture_id,
    ),
  );
  const state = getStored("progress:" + c.profile, {});
  if (c.current) state[c.payload.lecture_id] = c.current;
  else delete state[c.payload.lecture_id];
  store("progress:" + c.profile, state);
  if (profile === c.profile) {
    progress = state;
    if (player.row?.id === c.payload.lecture_id) {
      player.ready = false;
      player.open(
        player.row,
        c.current,
        c.current?.recording_id || player.recording?.id,
      );
    }
  }
  pendingConflict = null;
  $("progress-conflict").hidden = true;
  render();
};
const player = new Player({
  checkpoint: saveCheckpoint,
  message,
  next: () => {
    const course = catalog.courses.find((c) => c.id === currentCourse);
    if (!course || !player.row) return;
    const next = course.lectures[course.lectures.indexOf(player.row.id) + 1];
    if (next && byId(next)) {
      navigate(lectureLink(next, course.id), true);
    } else if (next)
      message("The next course step is not installed on this server.");
  },
});
async function loadListeners() {
  const data = await api("/api/listeners");
  $("listener").replaceChildren(
    el("option", { value: "", text: "This device" }),
    ...data.profiles.map((p) => el("option", { value: p.id, text: p.name })),
  );
  if (!data.profiles.some((p) => p.id === profile)) profile = "";
  $("listener").value = profile;
  progress = getStored("progress:" + contextKey(), {});
  if (profile) {
    const remote = await api("/api/listeners/" + profile + "/progress");
    const pending = getStored("pending:" + profile, []);
    progress = {
      ...remote,
      ...Object.fromEntries(
        pending.map((p) => [p.lecture_id, progress[p.lecture_id] || p]),
      ),
    };
    persistProgress();
    await flushProgress();
  }
}
$("listener").onchange = async () => {
  player.save();
  await saveChain;
  profile = $("listener").value;
  store("listener", profile);
  await loadListeners();
  render();
};
$("add-listener").onclick = () => $("listener-dialog").showModal();
$("listener-cancel").onclick = () => $("listener-dialog").close();
$("listener-form").onsubmit = async (event) => {
  event.preventDefault();
  try {
    const row = await post("/api/listeners", {
      name: $("listener-name").value,
    });
    profile = row.id;
    store("listener", profile);
    $("listener-dialog").close();
    $("listener-name").value = "";
    await loadListeners();
    render();
  } catch (e) {
    message(e.message);
  }
};
function courseCard(course) {
  const rows = course.lectures.map(byId).filter(Boolean);
  const completed = rows.filter((r) => progress[r.id]?.completed).length;
  return el(
    "article",
    { class: "card" },
    el("h3", {}, link(course.title, courseLink(course))),
    el("p", { text: course.summary || "" }),
    el("small", {
      text: `${rows.length} lectures · ${rows.filter(ready).length} ready to play${completed ? " · " + completed + " completed" : ""}`,
    }),
  );
}
function lectureItem(row, course = null) {
  const saved = progress[row.id];
  return el(
    "li",
    {},
    el(
      "div",
      { class: "copy" },
      link(row.title, lectureLink(row.id, course)),
      el("small", {
        text: `${row.namespace} · ${row.estimated_minutes || Math.round((row.words || 0) / 145)} min${saved?.completed ? " · Completed" : saved ? " · In progress" : ""}`,
      }),
    ),
    badge(row),
  );
}
function continueListening() {
  const rows = Object.values(progress)
    .filter((p) => !p.completed && byId(p.lecture_id))
    .sort((a, b) => (b.updated_at || "").localeCompare(a.updated_at || ""))
    .slice(0, 4);
  if (!rows.length) return null;
  return el(
    "section",
    { class: "section" },
    el("h2", { text: "Continue listening" }),
    el(
      "ul",
      { class: "list" },
      ...rows.map((p) => lectureItem(byId(p.lecture_id), p.course_id)),
    ),
  );
}
function browse(coursesOnly = false) {
  const main = $("main");
  main.replaceChildren(
    el("div", { class: "eyebrow", text: "Your installed library" }),
    title(coursesOnly ? "Courses" : "Listen, learn, explore"),
    description(
      "Standalone lectures across subjects. Choose a course, explore a question, or pick up where you left off.",
    ),
  );
  const continuation = continueListening();
  if (!coursesOnly && continuation) main.append(continuation);
  const searchInput = el("input", {
    type: "search",
    placeholder: "Search lectures and courses",
    value: search,
    "aria-label": "Search lectures and courses",
  });
  const subjectSelect = el(
    "select",
    { "aria-label": "Subject" },
    el("option", { value: "", text: "All subjects" }),
    ...catalog.courses.map((c) =>
      el("option", { value: c.id.split(":")[0], text: c.title }),
    ),
  );
  subjectSelect.value = subject;
  const audioSelect = el(
    "select",
    { "aria-label": "Audio availability" },
    el("option", { value: "", text: "All content" }),
    el("option", { value: "ready", text: "Ready to play" }),
    el("option", { value: "partial", text: "Has audio" }),
  );
  audioSelect.value = availability;
  const results = el("div");
  const update = () => {
    search = searchInput.value;
    subject = subjectSelect.value;
    availability = audioSelect.value;
    const q = search.toLocaleLowerCase();
    const courses = catalog.courses.filter(
      (c) =>
        (!subject || c.id.startsWith(subject + ":")) &&
        (!availability ||
          c.lectures.some((id) =>
            availability === "ready"
              ? ready(byId(id))
              : byId(id)?.recordings.length,
          )) &&
        (c.title + " " + c.summary).toLocaleLowerCase().includes(q),
    );
    const lectures = catalog.lectures.filter(
      (r) =>
        (!subject || r.namespace === subject) &&
        (!availability ||
          (availability === "ready" ? ready(r) : r.recordings.length)) &&
        (r.title + " " + r.id).toLocaleLowerCase().includes(q),
    );
    results.replaceChildren(
      el(
        "section",
        { class: "section" },
        el("h2", { text: `${courses.length} courses` }),
        el(
          "div",
          { class: "grid" },
          ...(coursesOnly || q || subject ? courses : courses.slice(0, 6)).map(
            courseCard,
          ),
        ),
      ),
    );
    if (!coursesOnly && !q && !subject && courses.length > 6)
      results.append(
        link("Browse all " + courses.length + " courses", "/courses"),
      );
    if (!coursesOnly) {
      const section = el(
        "section",
        { class: "section" },
        el("h2", { text: `${lectures.length} lectures` }),
        el(
          "ul",
          { class: "list" },
          ...lectures.slice(0, limit).map((r) => lectureItem(r)),
        ),
      );
      if (lectures.length > limit)
        section.append(
          button("Show more lectures", () => {
            limit += 60;
            update();
          }),
        );
      results.append(section);
    }
    if (!catalog.lectures.length)
      results.append(
        el("div", {
          class: "notice",
          text: "No content packs are installed yet. Add a pack in Packs, or configure a discovery folder.",
        }),
      );
  };
  searchInput.oninput = update;
  subjectSelect.onchange = update;
  audioSelect.onchange = update;
  main.append(
    el(
      "div",
      { class: "filters" },
      searchInput,
      el("label", {}, "Subject", subjectSelect),
      el("label", {}, "Audio", audioSelect),
    ),
    results,
  );
  update();
}
function coursePage(courseId) {
  const course = catalog.courses.find((c) => c.id === courseId);
  if (!course) throw Error("This course is not installed.");
  $("main").replaceChildren(
    link("All courses", "/courses"),
    title(course.title),
    description(course.summary),
    el("p", {
      class: "muted",
      text:
        typeof course.background === "string"
          ? course.background
          : JSON.stringify(course.background),
    }),
  );
  let section = null;
  const list = el("ol", { class: "list" });
  for (const id of course.lectures) {
    const row = byId(id);
    if (row && row.section && row.section !== section) {
      section = row.section;
      list.append(
        el("li", { class: "muted", text: section.replaceAll("-", " ") }),
      );
    }
    list.append(
      row
        ? lectureItem(row, course.id)
        : el("li", { text: id + " · Not installed" }),
    );
  }
  $("main").append(list);
}
async function lecturePage(id, autoplay = false, historical = null) {
  const token = ++renderToken;
  const latest =
    historical ||
    (await api("/api/library/lectures/" + encodeURIComponent(id)));
  const row =
    !historical && player.row?.id === id && !player.audio.paused
      ? player.row
      : latest;
  if (token !== renderToken) return;
  if (row.kind === "presentation") {
    location.href = "/presentations?deck=" + encodeURIComponent(row.deck);
    return;
  }
  currentCourse =
    new URLSearchParams(location.search).get("course") ||
    progress[id]?.course_id ||
    currentCourse;
  const position = player.row?.id === id ? player.position() : null;
  player.open(row, position || progress[id]);
  player.course = currentCourse;
  const course = catalog.courses.find((c) => c.id === currentCourse);
  const top = el(
    "div",
    {},
    course ? link(course.title, courseLink(course)) : link("Library", "/"),
    title(row.title),
    el(
      "div",
      { class: "actions" },
      button(progress[id] ? "Resume" : "Play", () => player.play(), true),
      badge(row),
      el("span", {
        class: "muted",
        text: `${row.words.toLocaleString()} words · approximately ${row.estimated_minutes} minutes`,
      }),
    ),
  );
  if (catalog.lectures.find((r) => r.id === id)?.revision !== row.revision)
    top.append(
      el(
        "div",
        { class: "notice" },
        "You are viewing an earlier revision. ",
        button("Open current revision", async () => {
          player.open(
            await api("/api/library/lectures/" + encodeURIComponent(id)),
            null,
          );
          await lecturePage(id);
        }),
      ),
    );
  const saved = progress[id];
  if (saved?.release && saved.spoken_sha256 !== row.spoken_sha256)
    top.append(
      el(
        "div",
        { class: "notice" },
        "Your previous position belongs to an earlier transcript. ",
        button("Open previous revision", async () => {
          const old = await api(
            "/api/library/lectures/" +
              encodeURIComponent(id) +
              "?release=" +
              saved.release,
          );
          player.open(old, saved);
          await lecturePage(id, false, old);
        }),
      ),
    );
  const text = el("section", {
    class: "transcript",
    "aria-label": "Lecture transcript",
  });
  if (player.recording) {
    player.recording.pages.forEach((page, index) => {
      const node = el("button", {
        type: "button",
        class: "passage" + (player.index === index ? " active" : ""),
        "data-index": index,
        "aria-label": `Listen from passage ${index + 1}`,
        "aria-disabled": !player.recording.segments.some(
          (s) => s.index === index,
        ),
        text: page,
        onclick: () => player.play(index, 0),
      });
      text.append(node);
    });
  } else
    row.transcript
      .split(/\n\s*\n/)
      .forEach((p) => text.append(el("p", { text: p })));
  const side = el("aside", { class: "sidebar" });
  if (row.recordings.length) {
    const select = el(
      "select",
      { "aria-label": "Installed narrator" },
      ...row.recordings.map((r) =>
        el("option", {
          value: r.id,
          text: (r.label || r.variant) + (r.complete ? "" : " · partial"),
        }),
      ),
    );
    select.value = player.recording.id;
    select.onchange = () => {
      const position = player.position();
      const rec = row.recordings.find((r) => r.id === select.value);
      store("variant", rec.variant);
      player.open(row, position, select.value);
      lecturePage(id, false, row);
    };
    side.append(el("section", {}, el("h3", { text: "Narrator" }), select));
  }
  const transcriptLink = el("a", {
    href:
      "/api/library/lectures/" +
      encodeURIComponent(id) +
      "/transcript.txt?release=" +
      row.origin.release,
    text: "Plain text transcript",
    target: "_blank",
  });
  side.append(
    el(
      "section",
      {},
      transcriptLink,
      el(
        "p",
        {},
        link(
          "Prepare another recording",
          "/production?lecture=" + encodeURIComponent(id),
        ),
      ),
    ),
  );
  const resources = (Array.isArray(row.metadata?.related_resources) ? row.metadata.related_resources : [])
    .filter((r) => r && typeof r === "object")
    .map((r) => ({ ...r, source: row.sources?.[r.source_id] }))
    .filter((r) => r.source && /^https?:\/\//.test(r.source.url));
  if (resources.length)
    side.append(
      el(
        "section",
        {},
        el("h3", { text: "Reading" }),
        el(
          "ul",
          {},
          ...resources.map((r) =>
            el(
              "li",
              {},
              el("a", {
                href: r.source.url,
                text: r.source.title,
                target: "_blank",
                rel: "noopener noreferrer",
              }),
            ),
          ),
        ),
      ),
    );
  side.append(feedbackForm(row));
  side.append(
    el(
      "details",
      {},
      el("summary", { text: "Source and revision" }),
      el("pre", {
        text: JSON.stringify(
          {
            id: row.id,
            revision: row.revision,
            release: row.origin.release,
            metadata: row.metadata,
          },
          null,
          2,
        ),
      }),
    ),
  );
  $("main").replaceChildren(
    top,
    el("div", { class: "lecture-layout" }, text, side),
  );
  if (autoplay) player.play();
}
function feedbackForm(row) {
  const key = "feedback:" + row.id + ":" + row.revision;
  let draft = getStored(key, {
    text: "",
    id: crypto.randomUUID(),
    created_at: new Date().toISOString(),
  });
  const textarea = el("textarea", {
    rows: "5",
    maxlength: "10000",
    placeholder: "What was unclear, incorrect, or helpful?",
    "aria-label": "Lecture feedback",
  });
  textarea.value = draft.text;
  const context = () => {
    const pos = player.row?.id === row.id ? player.position() : null;
    return {
      lecture_id: row.id,
      release: row.origin.release,
      revision: row.revision,
      recording_id: pos?.recording_id,
      segment: pos?.segment,
      seconds: pos?.seconds,
    };
  };
  textarea.oninput = () => {
    if (textarea.value && !draft.context) draft.context = context();
    if (!textarea.value) delete draft.context;
    draft.text = textarea.value;
    store(key, draft);
  };
  const status = el("p", { role: "status", class: "muted" });
  const form = el(
    "form",
    {},
    el("h3", { text: "Lecture feedback" }),
    textarea,
    el("button", { type: "submit", text: "Save feedback" }),
    status,
  );
  form.onsubmit = async (event) => {
    event.preventDefault();
    if (!textarea.value.trim()) return;
    try {
      if (draft.sent_text !== undefined && draft.sent_text !== textarea.value) {
        draft.id = crypto.randomUUID();
        draft.created_at = new Date().toISOString();
      }
      draft.sent_text = textarea.value;
      store(key, draft);
      const payload = {
        id: draft.id,
        created_at: draft.created_at,
        ...(draft.context || context()),
        text: textarea.value,
      };
      await post("/api/library/feedback", payload);
      store(key, null);
      textarea.value = "";
      draft = {
        text: "",
        id: crypto.randomUUID(),
        created_at: new Date().toISOString(),
      };
      status.textContent = "Feedback saved for this revision.";
    } catch (e) {
      status.textContent = e.message;
    }
  };
  return form;
}
function downloadJSON(data, filename) {
  const url = URL.createObjectURL(
    new Blob([JSON.stringify(data, null, 2)], { type: "application/json" }),
  );
  const a = el("a", { href: url, download: filename });
  a.click();
  setTimeout(() => URL.revokeObjectURL(url), 1000);
}
function listeningPage() {
  const main = $("main");
  main.replaceChildren(
    title("Your listening"),
    description(
      profile
        ? "Progress is shared with devices using this listener."
        : "This device remembers your progress. Choose a named listener to share it with other devices.",
    ),
  );
  const values = Object.values(progress).sort((a, b) =>
    (b.updated_at || "").localeCompare(a.updated_at || ""),
  );
  main.append(
    el(
      "ul",
      { class: "list" },
      ...values.map((p) => {
        const row = byId(p.lecture_id);
        const item = row
          ? lectureItem(row, p.course_id)
          : el("li", {
              text: p.lecture_id + " · Pack not installed · history retained",
            });
        item.append(
          button(p.completed ? "Mark unplayed" : "Mark complete", () => {
            saveCheckpoint({
              ...p,
              completed: !p.completed,
              explicit_completion: true,
            });
            render();
          }),
        );
        return item;
      }),
    ),
  );
  if (!values.length)
    main.append(
      description("Start a lecture to build your listening history."),
    );
  if (profile) {
    main.append(
      button("Export listener history", async () =>
        downloadJSON(
          await api("/api/listeners/" + profile + "/export"),
          "listener-history.json",
        ),
      ),
    );
    main.append(
      button("Forget listener on this device", async () => {
        player.save();
        await saveChain;
        profile = "";
        store("listener", "");
        await loadListeners();
        render();
      }),
    );
    main.append(
      button("Copy device history into this listener", async () => {
        const guest = getStored("progress:device", {});
        for (const [id, position] of Object.entries(guest))
          if (!progress[id]) saveCheckpoint(position);
        await saveChain;
        message(
          "Device history copied where this listener had no existing position.",
        );
        render();
      }),
    );
  }
  const input = el("input", {
    type: "file",
    accept: ".json",
    "aria-label": "Import listener history",
  });
  input.onchange = async () => {
    try {
      const p = await post(
        "/api/listeners/import",
        JSON.parse(await input.files[0].text()),
      );
      profile = p.id;
      store("listener", profile);
      await loadListeners();
      render();
    } catch (e) {
      message(e.message);
    }
  };
  main.append(
    el(
      "section",
      { class: "section" },
      el("h2", { text: "Move listening history" }),
      description(
        "Content packs and personal listening history travel separately.",
      ),
      el("label", {}, "Import listener history", input),
    ),
  );
}
function packsPage() {
  const main = $("main");
  main.replaceChildren(
    title("Content packs"),
    description(
      "Independent collections of source material and recordings. New releases appear without restarting this server.",
    ),
  );
  main.append(
    el(
      "div",
      { class: "grid" },
      ...catalog.packs.map((pack) =>
        el(
          "article",
          { class: "card" },
          el("h3", { text: pack.title }),
          el("p", { text: pack.id }),
          el("span", {
            class: "badge",
            text: pack.source ? "Live authored sources" : "Installed release",
          }),
          el(
            "details",
            {},
            el("summary", { text: "Release details" }),
            el("pre", { text: JSON.stringify(pack, null, 2) }),
          ),
          !pack.source
            ? button("Remove from library", async () => {
                await post("/api/library/packs", {
                  action: "remove",
                  pack_id: pack.id,
                });
                await refresh(true);
                render();
              })
            : null,
        ),
      ),
    ),
  );
  const path = el("input", {
    type: "text",
    placeholder: "/path/to/pack-or-archive.zip",
    "aria-label": "Pack path on this server",
  });
  const form = el(
    "form",
    { class: "section" },
    el("h2", { text: "Install a transferred pack" }),
    el("label", {}, "Directory or archive on this server", path),
    el("button", { type: "submit", text: "Install pack" }),
  );
  form.onsubmit = async (e) => {
    e.preventDefault();
    try {
      await post("/api/library/packs", { path: path.value });
      await refresh(true);
      render();
      message("Pack installed.");
    } catch (error) {
      message(error.message);
    }
  };
  main.append(
    form,
    el(
      "section",
      { class: "section" },
      el("h2", { text: "Library status" }),
      button("Refresh packs", async () => {
        await refresh(true);
        render();
      }),
      ...catalog.errors.map((error) =>
        el("p", { class: "notice error", text: error }),
      ),
    ),
  );
  main.append(
    el(
      "section",
      { class: "section" },
      el("h2", { text: "Feedback for revision work" }),
      button("Export feedback", async () =>
        downloadJSON(
          await api("/api/library/feedback"),
          "lecture-feedback.json",
        ),
      ),
    ),
  );
  const feedbackFile = el("input", {
    type: "file",
    accept: ".json",
    "aria-label": "Import editorial feedback",
  });
  feedbackFile.onchange = async () => {
    try {
      const result = await post(
        "/api/library/feedback/import",
        JSON.parse(await feedbackFile.files[0].text()),
      );
      message(`${result.added} feedback events added.`);
    } catch (e) {
      message(e.message);
    }
  };
  main.append(
    el(
      "label",
      {},
      "Import feedback and editorial status events",
      feedbackFile,
    ),
  );
}
async function productionPage() {
  const main = $("main");
  main.replaceChildren(
    title("Audio production"),
    description(
      "Prepared recordings play independently of TTS. Generate missing recordings when a configured backend is available.",
    ),
  );
  const profiles = await api("/api/library/production");
  if (!profiles.profiles.length) {
    main.append(
      el("div", {
        class: "notice",
        text:
          profiles.error ||
          "No TTS connection is configured in this installation. Installed audio and transcripts remain available.",
      }),
    );
    return;
  }
  const scope = el(
    "select",
    { "aria-label": "Preparation selection" },
    el("option", { value: "lecture", text: "Lecture" }),
    el("option", { value: "course", text: "Whole course" }),
  );
  const lectures = el(
    "select",
    { "aria-label": "Lecture to prepare" },
    ...catalog.lectures
      .filter((r) => r.kind === "audio")
      .map((r) => el("option", { value: r.id, text: r.title })),
  );
  const requestedLecture = new URLSearchParams(location.search).get("lecture");
  if ([...lectures.options].some((option) => option.value === requestedLecture))
    lectures.value = requestedLecture;
  scope.onchange = () => {
    const rows =
      scope.value === "course"
        ? catalog.courses.filter((c) =>
            c.lectures.some((id) => byId(id)?.kind === "audio"),
          )
        : catalog.lectures.filter((r) => r.kind === "audio");
    lectures.replaceChildren(
      ...rows.map((row) => el("option", { value: row.id, text: row.title })),
    );
  };
  const providers = el(
    "select",
    { id: "production-profile", "aria-label": "TTS profile" },
    ...profiles.profiles.map((p) =>
      el("option", {
        value: p.id,
        text: p.label + (p.reachable === false ? " · unavailable" : ""),
      }),
    ),
  );
  providers.value = profiles.default_profile || providers.value;
  const voice = el("input", { type: "text", "aria-label": "Voice ID" });
  const updateVoice = () =>
    (voice.value =
      profiles.profiles.find((p) => p.id === providers.value)?.voice || "");
  providers.onchange = updateVoice;
  updateVoice();
  const form = el(
    "form",
    {},
    el(
      "div",
      { class: "filters" },
      el("label", {}, "Prepare", scope),
      el("label", {}, "Selection", lectures),
      el("label", {}, "TTS profile", providers),
      el("label", {}, "Voice", voice),
    ),
    el("button", {
      id: "prepare-audio",
      type: "submit",
      class: "primary",
      text: "Prepare audio",
      disabled: !profiles.tools_available,
    }),
  );
  form.onsubmit = async (e) => {
    e.preventDefault();
    try {
      await post("/api/library/production/prepare", {
        [scope.value === "course" ? "course_id" : "lecture_id"]: lectures.value,
        profile: providers.value,
        voice: voice.value,
      });
      await showJobs();
    } catch (error) {
      message(error.message);
    }
  };
  main.append(form, el("section", { id: "jobs", class: "section" }));
  if (!profiles.tools_available)
    main.append(
      el("p", {
        class: "notice",
        text: "Generation needs the production installation and FFmpeg tools. Playback remains available.",
      }),
    );
  await showJobs();
}
async function refreshProductionHealth() {
  const select = $("production-profile");
  if (!select) return;
  const data = await api("/api/library/production");
  for (const option of select.options) {
    const profile = data.profiles.find((p) => p.id === option.value);
    if (profile)
      option.textContent =
        profile.label + (profile.reachable === false ? " · unavailable" : "");
  }
  if ($("prepare-audio")) $("prepare-audio").disabled = !data.tools_available;
}
async function showJobs() {
  const target = $("jobs");
  if (!target) return;
  const cards = [];
  const jobs = (await api("/api/library/production/jobs")).jobs;
  for (const job of jobs) {
    const id = job.id;
    try {
      const inv = job.inventory;
      cards.push(
        el(
          "article",
          { class: "card" },
          el("h3", { text: byId(job.lecture_id)?.title || job.lecture_id }),
          el("p", {
            text: job.published
              ? "Recording published"
              : `${job.state} · ${inv.ready} / ${inv.total || "?"} passages ready`,
          }),
          el("progress", {
            value: inv.ready,
            max: Math.max(1, inv.total),
            "aria-label": "Prepared passages",
          }),
          job.error ? el("p", { class: "notice", text: job.error }) : null,
          job.state === "settings_changed"
            ? link("Prepare with current settings", "/production?lecture=" + encodeURIComponent(job.lecture_id))
            : ["failed", "cancelled"].includes(job.state)
            ? button("Retry preparation", async () => {
                await post("/api/library/production/jobs/" + id + "/retry", {});
                await showJobs();
              })
            : null,
          !job.published &&
            !["failed", "cancelled", "settings_changed"].includes(job.state)
            ? button("Cancel generation", () =>
                api("/api/library/production/jobs/" + id, { method: "DELETE" }),
              )
            : null,
          el(
            "details",
            {},
            el("summary", { text: "Queue and preparation details" }),
            el("pre", { text: JSON.stringify(inv, null, 2) }),
          ),
        ),
      );
    } catch (error) {
      cards.push(
        el("p", {
          class: "muted",
          text: error.message,
        }),
      );
    }
  }
  target.replaceChildren(
    el("h2", { text: "Preparation jobs" }),
    el("div", { class: "grid" }, ...cards),
  );
}
function navigate(path, autoplay = false) {
  history.pushState({}, "", path);
  render(autoplay);
  window.scrollTo(0, 0);
}
document.addEventListener("click", (event) => {
  const a = event.target.closest("a[data-nav]");
  if (
    !a ||
    event.ctrlKey ||
    event.metaKey ||
    event.shiftKey ||
    event.altKey ||
    event.button !== 0
  )
    return;
  event.preventDefault();
  navigate(a.getAttribute("href"));
});
window.addEventListener("popstate", () => render());
async function render(autoplay = false) {
  renderToken++;
  message("");
  for (const a of document.querySelectorAll("nav a"))
    a.setAttribute(
      "aria-current",
      a.getAttribute("href") === location.pathname ? "page" : "false",
    );
  try {
    const path = location.pathname;
    if (path === "/courses") browse(true);
    else if (path.startsWith("/courses/"))
      coursePage(decodeURIComponent(path.slice(9)));
    else if (path.startsWith("/lectures/"))
      await lecturePage(
        path.slice(10).split("/").map(decodeURIComponent).join(":"),
        autoplay,
      );
    else if (path === "/listening") listeningPage();
    else if (path === "/packs") packsPage();
    else if (path === "/production") await productionPage();
    else browse();
  } catch (e) {
    message(e.message);
  }
}
async function refresh(force = false) {
  const next = await api("/api/library/catalog" + (force ? "?refresh=1" : ""));
  const changed = next.generation !== catalog.generation;
  catalog = next;
  $("presentations").hidden = !catalog.legacy;
  return changed;
}
async function init() {
  const results = await Promise.allSettled([refresh(), loadListeners()]);
  for (const result of results)
    if (result.status === "rejected") message(result.reason.message);
  await render();
  setInterval(async () => {
    try {
      const changed = await refresh();
      if (
        changed &&
        !location.pathname.startsWith("/lectures/") &&
        location.pathname != "/production"
      )
        await render();
      else if (
        changed &&
        location.pathname.startsWith("/lectures/") &&
        player.row
      ) {
        const current = byId(player.row.id);
        if (current && current.origin.release !== player.row.origin.release)
          message(
            "An updated lecture or recording is available. Current playback and feedback retain their revision; reopen the lecture after pausing to load the update.",
          );
      }
      await showJobs();
      await refreshProductionHealth();
      if (profile) {
        await flushProgress();
        if (!getStored("pending:" + profile, []).length) {
          const selected = profile;
          const remote = await api("/api/listeners/" + selected + "/progress");
          if (profile === selected) {
            const changed = JSON.stringify(remote) !== JSON.stringify(progress);
            progress = remote;
            persistProgress();
            if (changed && location.pathname === "/listening") render();
          }
        }
      }
    } catch {}
  }, 4000);
}
init();

import { api, post, el, getStored, store, lectureURL, clock } from "./api.mjs";
import { Player } from "./player.mjs";
import { reviewFeedback } from "./feedback.mjs";
import { ListeningQueue } from "./queue.mjs";
import { speechSegments } from "./transcript.mjs";
import { showStorage } from "./storage.mjs";
import { referencesPage } from "./references.mjs";
import { CatalogBrowser } from "./browse.mjs";
import { NarrationControls, preparationPanel } from "./narration.mjs";
import {
  blockGrid,
  recordingStates,
  generationStatus,
} from "./audio-blocks.mjs";
import {
  legacyPositions,
  approximateLegacyPosition,
} from "./legacy-progress.mjs";
const $ = (id) => document.getElementById(id);
let catalog = { lectures: [], courses: [], packs: [] },
  profile = getStored("listener", ""),
  progress = {},
  currentCourse = null,
  pendingConflict = null;
let playingQueueEntry = null;
let renderToken = 0;
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
    ...(["/presentations", "/audio", "/learning-paths"].some((prefix) =>
      href.startsWith(prefix),
    )
      ? {}
      : { "data-nav": "" }),
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
const courseLink = (course) => "/collections/" + encodeURIComponent(course.id);
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
    if (playingQueueEntry) {
      const id = playingQueueEntry.id;
      playingQueueEntry = null;
      return listeningQueue.advance(id);
    }
    const course = catalog.courses.find((c) => c.id === currentCourse);
    if (!course || !player.row) return;
    const next = course.lectures[course.lectures.indexOf(player.row.id) + 1];
    if (next && byId(next)) {
      navigate(lectureLink(next, course.id), true);
    } else if (next)
      message("The next course step is not installed on this server.");
  },
});
const listeningQueue = new ListeningQueue({
  profile: () => profile,
  lectures: () => catalog.lectures,
  message,
  play: (entry) => {
    playingQueueEntry = entry;
    navigate(lectureLink(entry.lecture_id, entry.course_id), true);
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
  playingQueueEntry = null;
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
const browser = new CatalogBrowser({
  catalog: () => catalog,
  progress: () => progress,
  listener: () => profile || "device",
  link,
  button,
  byId,
  ready,
  badge,
  courseLink,
  lectureLink,
});
const lectureItem = (row, collection = null) => browser.item(row, collection);
const browse = (collectionsOnly = false) =>
  browser.browse($("main"), collectionsOnly);
const coursePage = (id) => browser.collection($("main"), id);
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
  if (playingQueueEntry?.lecture_id !== id) playingQueueEntry = null;
  if (row.kind === "presentation") {
    location.href = "/presentations?deck=" + encodeURIComponent(row.deck);
    return;
  }
  const selectedCourse =
    new URLSearchParams(location.search).get("course") ||
    progress[id]?.course_id ||
    currentCourse;
  currentCourse = catalog.courses.some(
    (course) => course.id === selectedCourse && course.lectures.includes(id),
  )
    ? selectedCourse
    : null;
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
      button("Add to listening queue", () =>
        listeningQueue.add(id, currentCourse),
      ),
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
  if (saved?.legacy)
    top.append(
      el(
        "div",
        { class: "notice" },
        `The old reader saved passage ${saved.legacy.page_index + 1}, without source or narrator revisions. Its original history is retained. `,
        player.recording
          ? button("Resume approximately", () => {
              const position = approximateLegacyPosition(
                saved,
                player.recording,
              );
              player.play(position.index, position.seconds);
              message(
                "This is an approximate position from the old reader's selected passage.",
              );
            })
          : null,
        player.recording
          ? button("Start from beginning", () => player.play(0, 0))
          : null,
      ),
    );
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
  top.append(
    preparationPanel({
      lectureId: id,
      revision: row.revision,
      label: "Generate audio",
      onPlay: async (job) => {
        const updated = await api(
          "/api/library/lectures/" + encodeURIComponent(id),
        );
        const recording = updated.recordings.find(
          (recording) => recording.variant === job.variant,
        );
        if (!recording)
          return message(
            "The prepared recording belongs to another transcript revision.",
          );
        store("variant", recording.variant);
        player.open(updated, player.position() || progress[id], recording.id);
        await lecturePage(id, true, updated);
      },
    }),
  );
  const text = el("section", {
    class: "transcript",
    "aria-label": "Lecture transcript",
  });
  if (player.recording) {
    text.dataset.lecture = row.id;
    text.dataset.recording = player.recording.id;
    player.recording.pages.forEach((page, index) => {
      const node = el("section", {
        class: "passage" + (player.index === index ? " active" : ""),
        "data-index": index,
      });
      const available = player.recording.segments.some(
        (s) => s.index === index,
      );
      speechSegments(page).forEach((sentence, sentenceIndex) => {
        const seek = () => player.seekSentence(index, sentenceIndex);
        const trailing = sentence.match(/\s*$/)[0];
        node.append(
          el("span", {
            class: "speech-segment",
            role: "button",
            tabindex: "0",
            "data-sentence": sentenceIndex,
            "aria-label": `Listen from sentence ${sentenceIndex + 1} in passage ${index + 1}`,
            "aria-disabled": !available,
            text: sentence.slice(0, sentence.length - trailing.length),
            onclick: seek,
            onkeydown: (event) => {
              if (event.key === "Enter" || event.key === " ") {
                event.preventDefault();
                seek();
              }
            },
          }),
          trailing,
        );
      });
      text.append(node);
    });
    top.append(
      el("p", {
        class: "muted",
        text: "Select a sentence to seek. Highlights interpolate within recorded speech chunks when available; sentence positions are approximate.",
      }),
    );
  } else
    row.transcript
      .split(/\n\s*\n/)
      .forEach((p) => text.append(el("p", { text: p })));
  const side = el("aside", { class: "sidebar" });
  side.append(
    el(
      "p",
      {},
      el("a", {
        href:
          "/references?" +
          new URLSearchParams({ lecture_id: id, release: row.origin.release }),
        target: "_blank",
        rel: "noopener noreferrer",
        text: "Open references page",
      }),
    ),
  );
  if (row.recordings.length) {
    side.append(
      el(
        "section",
        {},
        el("h3", { text: "Audio blocks" }),
        el("p", {
          class: "muted",
          text: `${player.recording.segments.length}/${player.recording.pages.length} generated for this narrator. Select a block to listen.`,
        }),
        blockGrid(recordingStates(player.recording), (index) =>
          player.play(index, 0),
        ),
      ),
    );
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
  if (catalog.legacy)
    side.append(
      el(
        "p",
        {},
        el("a", {
          href:
            "/audio?" +
            new URLSearchParams({
              track: row.namespace,
              lecture: row.id.split(":")[1],
            }),
          target: "_blank",
          rel: "noopener noreferrer",
          text: "Companion slides and original audio tools",
        }),
      ),
    );
  const resources = (
    Array.isArray(row.metadata?.related_resources)
      ? row.metadata.related_resources
      : []
  )
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
              r.reason ? el("p", { class: "muted", text: r.reason }) : null,
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
  player.update();
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
  const queuePanel = el("section", { class: "section", id: "listening-queue" });
  main.append(queuePanel);
  listeningQueue.render(queuePanel);
  main.append(el("h2", { class: "section", text: "Listening history" }));
  let oldPositions = [];
  try {
    oldPositions = legacyPositions(localStorage).filter(
      (position) => !progress[position.lecture_id],
    );
  } catch {}
  if (oldPositions.length)
    main.append(
      button(`Import old reader history (${oldPositions.length})`, async () => {
        store("legacy-reader-history", legacyPositions(localStorage));
        for (const position of oldPositions) saveCheckpoint(position);
        await saveChain;
        await render();
        message(
          "Old selected pages imported. Source and narrator revisions remain unknown; existing positions and old browser records are unchanged.",
        );
      }),
    );
  const values = Object.values(progress).sort((a, b) =>
    (b.updated_at || "").localeCompare(a.updated_at || ""),
  );
  main.append(
    el(
      "ul",
      { class: "list", id: "listening-history" },
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
      button("Copy device history and queue into this listener", async () => {
        const guest = getStored("progress:device", {});
        for (const [id, position] of Object.entries(guest))
          if (!progress[id]) saveCheckpoint(position);
        for (const entry of getStored("queue:device", []))
          await listeningQueue.edit({ action: "add", entry });
        await saveChain;
        message(
          "Device queue copied; history copied where this listener had no existing position.",
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
          { class: "card", "data-pack": pack.id },
          el("h3", { text: pack.title }),
          el("p", { "data-coverage": "", class: "muted" }),
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
  const storage = el("section", { class: "section" });
  main.append(storage);
  showStorage(storage, main, catalog);
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
      link("Browse all references", "/references"),
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
      link("Review feedback", "/feedback"),
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
  const target = $("main");
  const main = el("section");
  target.replaceChildren(main);
  main.replaceChildren(
    title("Audio production"),
    description(
      "Prepared recordings play independently of TTS. Generate missing recordings when a configured backend is available.",
    ),
  );
  if (catalog.legacy) main.append(link("Open original audio tools", "/audio"));
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
    el("option", { value: "course", text: "Whole collection" }),
    el("option", { value: "library", text: "Whole library" }),
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
    lectures.disabled = scope.value === "library";
    $("prepare-audio").textContent =
      scope.value === "library"
        ? `Queue all ${catalog.lectures.filter((row) => row.kind === "audio").length} lectures`
        : scope.value === "course"
          ? "Queue whole collection"
          : "Cache whole lecture";
  };
  const narrator = new NarrationControls(profiles, {
    profileId: "production-profile",
    discover: true,
  });
  const form = el(
    "form",
    {},
    el(
      "div",
      { class: "filters" },
      el("label", {}, "Prepare", scope),
      el("label", {}, "Selection", lectures),
    ),
    narrator.root,
    el("button", {
      id: "prepare-audio",
      type: "submit",
      class: "primary",
      text: "Cache whole lecture",
      disabled: !profiles.tools_available,
    }),
  );
  form.onsubmit = async (e) => {
    e.preventDefault();
    try {
      await post("/api/library/production/prepare", {
        ...(scope.value === "library"
          ? {
              lecture_ids: catalog.lectures
                .filter((row) => row.kind === "audio")
                .map((row) => row.id),
            }
          : {
              [scope.value === "course" ? "course_id" : "lecture_id"]:
                lectures.value,
            }),
        ...narrator.settings(),
      });
      await showJobs();
    } catch (error) {
      message(error.message);
    }
  };
  const registerId = el("input", {
    type: "text",
    "aria-label": "Voice ID to register",
  });
  const registerLabel = el("input", {
    type: "text",
    "aria-label": "Voice display name",
    maxlength: "80",
  });
  const registerMessage = el("p", { role: "status" });
  main.append(
    form,
    button("Refresh available voices", () =>
      narrator.loadVoices(true, narrator.settings().voice),
    ),
    el(
      "details",
      { class: "section" },
      el("summary", { text: "Register a server voice ID" }),
      description(
        "Register a voice already available on the selected speech server. Reference recordings stay on that server.",
      ),
      el(
        "div",
        { class: "filters" },
        el("label", {}, "Voice ID", registerId),
        el("label", {}, "Display name", registerLabel),
      ),
      button("Register voice", async () => {
        try {
          await post("/api/library/production/voices/register", {
            profile: narrator.profile.value,
            voice: registerId.value.trim(),
            label: registerLabel.value.trim() || registerId.value.trim(),
          });
          store(
            "production-voice:" + narrator.profile.value,
            registerId.value.trim(),
          );
          await narrator.loadVoices(false, registerId.value.trim());
          registerMessage.textContent = "Voice registered for this profile.";
        } catch (error) {
          registerMessage.textContent = error.message;
        }
      }),
      registerMessage,
    ),
    el("section", { id: "jobs", class: "section" }),
  );
  if (!profiles.tools_available)
    main.append(
      el("p", {
        class: "notice",
        text: "Generation needs the production installation and FFmpeg tools. Playback remains available.",
      }),
    );
  await showJobs();
  if (location.hash === "#jobs") $("jobs")?.scrollIntoView({ block: "start" });
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
            text: `${job.profile} · ${job.voice || "configured voice"} · ${job.speed || 1}× speech`,
          }),
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
          blockGrid(inv.states || []),
          ...(inv.queue || []).map((item) =>
            el(
              "div",
              { class: "generation-item" },
              el("p", {
                text: `Block ${item.page + 1} · ${item.kind} · ${generationStatus(item)}`,
              }),
              button("Cancel this lecture's generation", async () => {
                await api("/api/library/production/jobs/" + id, {
                  method: "DELETE",
                });
                await showJobs();
              }),
            ),
          ),
          job.state === "settings_changed"
            ? link(
                "Prepare with current settings",
                "/production?lecture=" + encodeURIComponent(job.lecture_id),
              )
            : ["failed", "cancelled"].includes(job.state)
              ? button("Retry preparation", async () => {
                  await post(
                    "/api/library/production/jobs/" + id + "/retry",
                    {},
                  );
                  await showJobs();
                })
              : null,
          !job.published &&
            !["failed", "cancelled", "settings_changed"].includes(job.state)
            ? button("Cancel generation", async () => {
                await api("/api/library/production/jobs/" + id, {
                  method: "DELETE",
                });
                await showJobs();
              })
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
    if (["/courses", "/collections"].includes(path)) browse(true);
    else if (path.startsWith("/courses/") || path.startsWith("/collections/"))
      coursePage(
        decodeURIComponent(
          path.slice(path.startsWith("/collections/") ? 13 : 9),
        ),
      );
    else if (path.startsWith("/lectures/"))
      await lecturePage(
        path.slice(10).split("/").map(decodeURIComponent).join(":"),
        autoplay,
      );
    else if (path === "/listening") listeningPage();
    else if (path === "/packs") packsPage();
    else if (path === "/feedback")
      await reviewFeedback($("main"), catalog.lectures);
    else if (path === "/references") await referencesPage($("main"), catalog);
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
        location.pathname != "/feedback" &&
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
      if ($("listening-queue"))
        await listeningQueue.render($("listening-queue"));
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

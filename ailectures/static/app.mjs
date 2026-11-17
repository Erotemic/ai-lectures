import { ProductionPanel } from "./production.mjs";
import {
  randomId,
  api,
  post,
  el,
  getStored,
  store,
  lectureURL,
  clock,
} from "./api.mjs";
import { Player } from "./player.mjs";
import { ProgressSync, mergeSharedProgress } from "./progress.mjs";
import { reviewFeedback } from "./feedback.mjs";
import { ListeningQueue } from "./queue.mjs";
import { speechSegments } from "./transcript.mjs";
import { showStorage } from "./storage.mjs";
import { referencesPage } from "./references.mjs";
import { CatalogBrowser, revealAnchor } from "./browse.mjs";
import { renderLearningMap } from "./learning-map.mjs";
import { showSlideCompanions } from "./slide-companions.mjs";
import { collectionReturnPath } from "./browse-model.mjs";
import { LectureAudio } from "./lecture-audio.mjs";
import { listeningCourse, followingLecture } from "./playback-route.mjs";
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
let navigationToken = 0;
let lectureAudio = null;
let lectureIndex = new Map(),
  catalogTag = null;
const device = getStored("device") || randomId();
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
const byId = (id) => lectureIndex.get(id);
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
const lectureLink = (id, course = null) => {
  if (byId(id)?.kind === "presentation") return "/presentations?deck=" + encodeURIComponent(byId(id).deck);
  const params = new URLSearchParams(course ? { course } : {});
  const current = new URLSearchParams(location.search);
  const returnTo = collectionReturnPath(current.get("return"), course, location.origin);
  if (returnTo && location.pathname.startsWith("/lectures/") && current.get("course") === course)
    params.set("return", returnTo);
  return lectureURL(id) + (params.size ? "?" + params : "");
};
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
    course_id: position.course_id ?? null,
    completed: position.explicit_completion
      ? position.completed
      : position.completed || old?.completed || false,
    update_id: randomId(),
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
const progressSync = new ProgressSync({
  onSaved: (selectedProfile, state) => {
    if (profile === selectedProfile) progress = state;
  },
  onConflict: (conflict) => {
    if (profile !== conflict.profile) return;
    pendingConflict = conflict;
    $("progress-conflict").hidden = false;
  },
  onError: () =>
    message(
      "Progress is saved on this device and will sync when the server is reachable.",
    ),
});
const flushProgress = (selectedProfile = profile) =>
  progressSync.flush(selectedProfile);
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
    update_id: randomId(),
    sequence: ++sequence,
  };
  store("sequence", sequence);
  progressSync.useLocal(c, payload);
  pendingConflict = null;
  $("progress-conflict").hidden = true;
  await flushProgress(c.profile);
};
$("keep-shared").onclick = async () => {
  if (!pendingConflict) return;
  const c = pendingConflict;
  progressSync.keepShared(c);
  if (profile === c.profile) {
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
  await flushProgress(c.profile);
};
const player = new Player({
  checkpoint: saveCheckpoint,
  message,
  next: ({ automatic = false } = {}) => {
    if (playingQueueEntry) {
      const id = playingQueueEntry.id;
      return listeningQueue.advance(id, automatic).then(updatePlaybackRoute);
    }
    if (!player.row) return;
    const { course, next } = followingLecture(catalog.courses, player.course, player.row.id);
    if (!course) return message("Choose a playing track in the player’s More controls.");
    if (next && byId(next)) {
      if (byId(next).kind === "presentation") {
        if (automatic) return message("The next step is a presentation. Choose Next to open it.");
        location.assign(lectureLink(next, course.id));
        return;
      }
      return navigate(lectureLink(next, course.id), automatic ? "prepared" : true);
    } else if (next)
      message("The next lecture in this track is not installed on this server.");
    else message("You’ve reached the end of this track.");
  },
});
const listeningQueue = new ListeningQueue({
  profile: () => profile,
  lectures: () => catalog.lectures,
  message,
  onChange: () => updatePlaybackRoute(),
  play: (entry, automatic = false) => {
    if (byId(entry.lecture_id)?.kind === "presentation") {
      location.assign(lectureLink(entry.lecture_id, entry.course_id));
      return;
    }
    playingQueueEntry = entry;
    return navigate(lectureLink(entry.lecture_id, entry.course_id), automatic ? "prepared" : true);
  },
});
const continuation = $("continue-course");
continuation.checked = getStored("continue-course", true);
continuation.onchange = () => store("continue-course", continuation.checked);
$("next-lecture").onclick = () => Promise.resolve(player.next()).catch((error) => message(error.message));
$("skip-back").onclick = () => player.seekBy(-15);
$("skip-forward").onclick = () => player.seekBy(15);
$("playing-course").onchange = () => {
  player.save();
  player.course = $("playing-course").value || null;
  if (lectureAudio?.row.id === player.row?.id) lectureAudio.course = player.course;
  playingQueueEntry = null;
  player.save();
  updatePlaybackRoute();
};
let playbackRouteToken = 0;
async function updatePlaybackRoute() {
  const token = ++playbackRouteToken;
  const row = player.row;
  if (!row) return;
  const { course, index, next } = followingLecture(catalog.courses, player.course, row.id);
  const selector = $("playing-course");
  const routes = catalog.courses.filter((candidate) => candidate.lectures.includes(row.id));
  const signature = JSON.stringify([course?.id, routes.map((candidate) => [candidate.id, candidate.title])]);
  if (selector.dataset.routes !== signature) {
    selector.replaceChildren(el("option", { value: "", text: "Choose a track" }),
      ...routes.map((candidate) => el("option", { value: candidate.id, text: candidate.title })));
    selector.value = course?.id || "";
    selector.dataset.routes = signature;
  }
  $("playing-title").href = lectureLink(row.id, player.course);
  $("playing-title").title = row.title;
  const track = $("playing-track");
  track.hidden = !course;
  track.textContent = course ? `${course.title} · ${index + 1} / ${course.lectures.length}` : "";
  track.href = course ? courseLink(course) : "/collections";
  let nextId = next;
  let queued = false;
  if (playingQueueEntry) {
    const entries = await listeningQueue.read().catch(() => []);
    if (token !== playbackRouteToken) return;
    const queueIndex = entries.findIndex((entry) => entry.id === playingQueueEntry?.id);
    nextId = queueIndex >= 0 ? entries[queueIndex + 1]?.lecture_id : null;
    queued = true;
  }
  const nextRow = byId(nextId);
  $("next-lecture").disabled = !nextRow;
  $("next-lecture").title = nextRow ? "Next lecture: " + nextRow.title : "No next installed lecture";
  $("up-next").textContent = nextId ? `Next${queued ? " in queue" : ""}: ${nextRow?.title || "Lecture not installed"}`
    : queued ? "End of listening queue" : course ? "Last lecture in this track" : "Choose a playing track in More";
  $("up-next").title = $("up-next").textContent;
}
const optionsToggle = $("toggle-player-options");
function showPlayerOptions(open) {
  $("player-options").hidden = !open;
  optionsToggle.setAttribute("aria-expanded", String(open));
  optionsToggle.textContent = open ? "Less" : "More";
}
optionsToggle.onclick = () => showPlayerOptions($("player-options").hidden);
const menuToggle = $("toggle-library-menu");
function showLibraryMenu(open) {
  menuToggle.setAttribute("aria-expanded", String(open));
  document.querySelector("header").classList.toggle("menu-open", open);
}
menuToggle.onclick = () => showLibraryMenu(menuToggle.getAttribute("aria-expanded") !== "true");
document.addEventListener("keydown", (event) => {
  if (event.key !== "Escape") return;
  if (!$("player-options").hidden) { showPlayerOptions(false); optionsToggle.focus(); }
  else if (menuToggle.getAttribute("aria-expanded") === "true") { showLibraryMenu(false); menuToggle.focus(); }
});
new ResizeObserver(() => {
  document.documentElement.style.setProperty("--player-height", $("player").getBoundingClientRect().height + "px");
}).observe($("player"));
async function loadListeners() {
  const data = await api("/api/listeners");
  if (data.aliases?.[profile]) {
    const old = profile;
    profile = data.aliases[profile];
    store("listener", profile);
    const pending = getStored("pending:" + profile, []);
    const known = new Set(pending.map((event) => event.update_id));
    store(
      "pending:" + profile,
      pending.concat(
        getStored("pending:" + old, []).filter(
          (event) => !known.has(event.update_id),
        ),
      ),
    );
  }
  $("listener").replaceChildren(
    el("option", { value: "", text: "This device" }),
    ...data.profiles.map((p) => el("option", { value: p.id, text: p.name })),
  );
  if (!data.profiles.some((p) => p.id === profile)) profile = "";
  $("listener").value = profile;
  pendingConflict = null;
  $("progress-conflict").hidden = true;
  progress = getStored("progress:" + contextKey(), {});
  if (profile) {
    const remote = await api("/api/listeners/" + profile + "/progress");
    const pending = getStored("pending:" + profile, []);
    progress = mergeSharedProgress(
      remote,
      getStored("progress:" + profile, {}),
      pending,
    );
    persistProgress();
    await flushProgress();
  }
}
async function selectListener(id) {
  player.save();
  playingQueueEntry = null;
  await saveChain;
  profile = id;
  store("listener", profile);
  await loadListeners();
  await render();
  updatePlaybackRoute();
}
$("listener").onchange = () =>
  selectListener($("listener").value).catch((error) => message(error.message));
$("add-listener").onclick = () => $("listener-dialog").showModal();
$("listener-cancel").onclick = () => $("listener-dialog").close();
$("listener-form").onsubmit = async (event) => {
  event.preventDefault();
  try {
    const row = await post("/api/listeners", {
      name: $("listener-name").value,
    });
    $("listener-dialog").close();
    $("listener-name").value = "";
    await selectListener(row.id);
  } catch (e) {
    message(e.message);
  }
};
const production = new ProductionPanel({
  catalog: () => catalog,
  link,
  button,
  message,
});
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
  $("main").replaceChildren(
    title(byId(id)?.title || "Loading lecture…"),
    description("Loading lecture…"),
  );
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
  currentCourse = listeningCourse(catalog.courses, id,
    new URLSearchParams(location.search).get("course"), progress[id]?.course_id, currentCourse)?.id || null;
  const position = player.row?.id === id ? player.position() : null;
  if (lectureAudio && lectureAudio !== player.lectureController) lectureAudio.dispose();
  let refreshTranscript = () => {};
  const audio = new LectureAudio({
    row,
    player,
    progress: position || progress[id],
    message,
    course: currentCourse,
    active: () => token === renderToken,
    onChange: () => refreshTranscript(),
  });
  lectureAudio = audio;
  audio.ready.catch((error) => {
    if (token === renderToken) message(error.message);
  });
  audio.ready
    .then(() => {
      if (token === renderToken) updatePlaybackRoute();
    })
    .catch(() => {});
  const course = catalog.courses.find((c) => c.id === currentCourse);
  const returnTo = collectionReturnPath(new URLSearchParams(location.search).get("return"), course?.id, location.origin)
    || (course ? courseLink(course) : "/");
  const top = el(
    "div",
    {},
    course ? link("← " + course.title, returnTo) : link("Library", "/"),
    title(row.title),
    el(
      "div",
      { class: "actions" },
      button("Add to listening queue", () =>
        listeningQueue.add(id, currentCourse),
      ),
      el("span", {
        class: "muted",
        text: `${row.words.toLocaleString()} words · approximately ${row.estimated_minutes} minutes`,
      }),
    ),
  );
  const otherRoutes = catalog.courses.filter(
    (candidate) =>
      candidate.role &&
      candidate.role !== "archive" &&
      candidate.id !== currentCourse &&
      candidate.lectures.includes(id),
  );
  if (otherRoutes.length)
    top.append(
      el(
        "details",
        { class: "section" },
        el("summary", { text: "Other listening routes" }),
        el(
          "div",
          { class: "actions" },
          ...otherRoutes.map((candidate) =>
            link(candidate.title, courseLink(candidate)),
          ),
        ),
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
  if (saved?.legacy) {
    const legacyActions = el("div", { class: "actions" });
    top.append(
      el(
        "div",
        { class: "notice" },
        `The old reader saved passage ${saved.legacy.page_index + 1}, without source or narrator revisions. Its original history is retained. `,
        legacyActions,
      ),
    );
    audio.ready
      .then(() => {
        if (token !== renderToken || !player.recording) return;
        legacyActions.append(
          button("Resume approximately", () => {
            const position = approximateLegacyPosition(saved, player.recording);
            player.play(position.index, position.seconds);
            message(
              "This is an approximate position from the old reader's selected passage.",
            );
          }),
          button("Start from beginning", () => player.play(0, 0)),
        );
      })
      .catch(() => {});
  }
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
  top.append(audio.root);
  if (row.companions?.length)
    top.append(
      el(
        "section",
        {},
        el("h2", { text: "Companion files" }),
        ...row.companions.map((item) =>
          el(
            "p",
            {},
            el("a", { href: item.url, text: item.title, download: "" }),
            ` · ${item.role === "source" ? "Source" : "Prepared"}`,
            item.stale ? " · prepared for an earlier transcript" : "",
            item.attribution
              ? el("span", {
                  class: "muted",
                  text:
                    " · " +
                    (typeof item.attribution === "string"
                      ? item.attribution
                      : JSON.stringify(item.attribution)),
                })
              : null,
          ),
        ),
      ),
    );
  if (catalog.capabilities?.slide_companions || row.companions?.some(item => item.role === "prepared" && item.media_type === "text/html"))
    showSlideCompanions(top, row, { message });
  const text = el("section", {
    class: "transcript",
    "aria-label": "Lecture transcript",
  });
  refreshTranscript = () => {
    text.replaceChildren();
    delete text.dataset.recording;
    delete text.dataset.lecture;
    if (
      player.row?.id === row.id &&
      player.row.revision === row.revision &&
      player.recording
    ) {
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
              "aria-disabled": !available && !audio.data.tools_available,
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
      text.append(
        el("p", {
          class: "muted",
          text: "Select a sentence to seek. Highlights interpolate within recorded speech chunks when available; sentence positions are approximate.",
        }),
      );
    } else
      row.transcript
        .split(/\n\s*\n/)
        .forEach((p) => text.append(el("p", { text: p })));
    player.update();
  };
  refreshTranscript();
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
  side.append(el("p", {}, link("Explore related lectures", "/learning-map?" + new URLSearchParams({ lecture: id }))));
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
  if (autoplay) {
    await audio.ready;
    if (token === renderToken) {
      const restart = Boolean(playingQueueEntry || autoplay === "prepared" || progress[id]?.completed);
      if (autoplay === "prepared") audio.playPrepared(restart ? 0 : player.index, restart ? 0 : null);
      else audio.play(restart ? 0 : player.index, restart ? 0 : null);
    }
  }
}
function feedbackForm(row) {
  const key = "feedback:" + row.id + ":" + row.revision;
  let draft = getStored(key, {
    text: "",
    id: randomId(),
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
      release:
        pos?.revision === row.revision ? pos.release : row.origin.release,
      revision: row.revision,
      recording_id: pos?.revision === row.revision ? pos.recording_id : null,
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
        draft.id = randomId();
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
        id: randomId(),
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
          packExportControls(pack),
          el(
            "details",
            {},
            el("summary", { text: "Release details" }),
            el("pre", { text: JSON.stringify(pack, null, 2) }),
          ),
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
function packExportControls(pack) {
  const includeAudio = el("input", { type: "checkbox", checked: true });
  const status = el("p", { class: "muted", role: "status", "aria-live": "polite" });
  const download = button("Create downloadable ZIP", async () => {
    download.disabled = true;
    status.textContent = "Preparing pack download…";
    try {
      const result = await post("/api/library/exports", { pack_id: pack.id, source_only: !includeAudio.checked });
      const file = el("a", { href: result.url, download: result.filename, text: "Download " + result.filename });
      status.replaceChildren(file, el("small", { text: `${result.lectures} lectures · ${result.recordings} recordings` }));
      file.click();
    } catch (error) {
      status.textContent = error.message;
    } finally {
      download.disabled = false;
    }
  });
  return el("details", { class: "pack-export" }, el("summary", { text: "Transfer this pack" }),
    el("p", { class: "muted", text: "Download transcripts, notes, companions, and optionally all published audio. Listening history travels separately." }),
    el("label", { class: "check" }, includeAudio, "Include prepared audio"), download, status,
  );
}
async function navigate(path, autoplay = false) {
  showLibraryMenu(false);
  const token = ++navigationToken;
  history.replaceState({ ...history.state, scroll: window.scrollY }, "");
  history.pushState({}, "", path);
  await render(autoplay);
  if (token !== navigationToken) return;
  $("main").focus({ preventScroll: true });
  if (!revealAnchor()) window.scrollTo(0, 0);
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
window.addEventListener("popstate", async (event) => {
  const token = ++navigationToken;
  await render();
  if (token !== navigationToken) return;
  $("main").focus({ preventScroll: true });
  if (!revealAnchor()) window.scrollTo(0, event.state?.scroll || 0);
});
window.addEventListener("hashchange", () => revealAnchor());
history.scrollRestoration = "manual";
let scrollPending = false;
window.addEventListener("scroll", () => {
  if (scrollPending) return;
  scrollPending = true;
  const token = navigationToken;
  requestAnimationFrame(() => {
    scrollPending = false;
    if (token === navigationToken)
      history.replaceState({ ...history.state, scroll: window.scrollY }, "");
  });
}, { passive: true });
async function findLibrary() {
  await navigate("/?all=1");
  document.querySelector(".library-search")?.focus();
}
$("find-library").addEventListener("click", findLibrary);
document.addEventListener("keydown", (event) => {
  if (document.querySelector("dialog[open]")) return;
  if ((event.ctrlKey || event.metaKey) && !event.altKey && event.key.toLowerCase() === "k") {
    event.preventDefault();
    findLibrary();
  } else if (event.key === "/" && !event.ctrlKey && !event.metaKey && !event.altKey &&
    !event.target.closest("input, textarea, select, [contenteditable]")) {
    event.preventDefault();
    const search = document.querySelector("#collection-search, .library-search");
    if (search) search.focus(); else findLibrary();
  }
});
async function render(autoplay = false) {
  renderToken++;
  message("");
  for (const a of document.querySelectorAll("header nav a"))
    a.setAttribute(
      "aria-current",
      a.getAttribute("href") === location.pathname ||
      (a.getAttribute("href") === "/collections" && /^\/(collections|courses|lectures)\//.test(location.pathname)) ? "page" : "false",
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
    else if (path === "/learning-map") await renderLearningMap($("main"), { link, navigate });
    else if (path === "/production") await production.render($("main"));
    else browse();
    document.title = ($("main").querySelector("h1")?.textContent || "Library") + " · AI Lectures";
  } catch (e) {
    message(e.message);
  }
}
async function refresh(force = false) {
  const response = await fetch(
    "/api/library/catalog" + (force ? "?refresh=1" : ""),
    {
      cache: "no-store",
      headers: !force && catalogTag ? { "If-None-Match": catalogTag } : {},
    },
  );
  if (response.status === 304) return false;
  const next = await response.json();
  if (!response.ok)
    throw new Error(
      next.error || `Catalog request failed (${response.status})`,
    );
  catalogTag = response.headers.get("ETag");
  const changed = next.generation !== catalog.generation;
  catalog = next;
  lectureIndex = new Map(next.lectures.map((row) => [row.id, row]));
  $("presentations").hidden = !catalog.legacy;
  updatePlaybackRoute();
  return changed;
}
async function init() {
  const results = await Promise.allSettled([refresh(), loadListeners()]);
  for (const result of results)
    if (result.status === "rejected") message(result.reason.message);
  await render();
  if (location.hash) revealAnchor();
  setInterval(async () => {
    try {
      const changed = await refresh();
      if (
        changed &&
        !location.pathname.startsWith("/lectures/") &&
        location.pathname != "/feedback" &&
        location.pathname != "/production"
      ) {
        const token = navigationToken;
        const destination = location.href;
        const active = document.activeElement;
        const selector = active?.id ? "#" + CSS.escape(active.id)
          : active?.matches(".library-search") ? ".library-search"
          : active?.hasAttribute("aria-label") ? `[aria-label="${CSS.escape(active.getAttribute("aria-label"))}"]`
          : active?.matches("summary") && active.parentElement.id ? `#${CSS.escape(active.parentElement.id)} > summary`
          : active?.matches("a[href]") ? `a[href="${CSS.escape(active.getAttribute("href"))}"]` : null;
        const selection = active?.matches("input[type=search], textarea") ? [active.selectionStart, active.selectionEnd] : null;
        const scroll = window.scrollY;
        await render();
        if (token !== navigationToken || destination !== location.href) return;
        const restored = selector && document.querySelector(selector);
        restored?.focus({ preventScroll: true });
        if (restored && selection) restored.setSelectionRange(...selection);
        window.scrollTo(0, scroll);
      } else if (
        changed &&
        location.pathname.startsWith("/lectures/") &&
        player.row
      ) {
        const current = byId(player.row.id);
        if (current && current.revision !== player.row.revision)
          message(
            "An updated lecture is available. Current playback and feedback retain their revision; reopen the lecture after pausing to load the update.",
          );
      }
      await production.showJobs();
      await production.refreshHealth();
      if ($("listening-queue"))
        await listeningQueue.render($("listening-queue"));
      if (playingQueueEntry) await updatePlaybackRoute();
      if (profile) {
        await flushProgress();
        if (!getStored("pending:" + profile, []).length) {
          const selected = profile;
          const remote = await api("/api/listeners/" + selected + "/progress");
          if (profile === selected) {
            const merged = mergeSharedProgress(
              remote,
              getStored("progress:" + selected, {}),
              getStored("pending:" + selected, []),
            );
            const changed = JSON.stringify(merged) !== JSON.stringify(progress);
            progress = merged;
            persistProgress();
            if (changed && location.pathname === "/listening") render();
          }
        }
      }
    } catch {}
  }, 4000);
}
init();

import { el, clock } from "./api.mjs";

export function recordingStates(recording) {
  return recording.pages.map((_, index) =>
    recording.segments.some((segment) => segment.index === index)
      ? "ready"
      : "missing",
  );
}

export function blockGrid(states, select = null) {
  const counts = [...new Set(states)]
    .map(
      (state) => `${states.filter((value) => value === state).length} ${state}`,
    )
    .join(" · ");
  return el(
    "div",
    {},
    el("p", { class: "muted", text: counts }),
    el(
      "div",
      {
        class: "audio-blocks",
        role: "list",
        "aria-label": "Audio block readiness",
      },
      ...states.map((state, index) =>
        el(
          "span",
          { role: "listitem" },
          el(select ? "button" : "span", {
            class: "audio-block " + state,
            text: String(index + 1),
            title: `Block ${index + 1}: ${state}`,
            "aria-label": `Block ${index + 1}: ${state}`,
            ...(select ? { type: "button", onclick: () => select(index) } : {}),
          }),
        ),
      ),
    ),
  );
}

export function generationStatus(item) {
  const progress = item.progress || {};
  const state =
    progress.upstream_state === "queued"
      ? "Waiting for speech server"
      : item.state;
  const passage =
    progress.current_passage && progress.phase === "synthesizing"
      ? ` · passage ${progress.current_passage}/${progress.total_passages || "?"}`
      : progress.total_passages
        ? ` · ${progress.completed_passages || 0}/${progress.total_passages} passages`
        : "";
  const eta = Number.isFinite(item.eta_seconds)
    ? ` · approximately ${clock(item.eta_seconds)} remaining`
    : Number.isFinite(item.estimate_exceeded_seconds)
      ? " · still working beyond its initial estimate"
      : "";
  return `${state}${item.queued_position ? " · queue position " + item.queued_position : ""}${passage}${eta}`;
}

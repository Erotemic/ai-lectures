import { api, post, el, getStored, store } from "./api.mjs";
import { renderVoiceProfiles } from "./voice-profile-settings.mjs";

export async function renderSettings(target, { message, player }) {
  const root = el(
    "section",
    {},
    el("h1", { text: "Settings" }),
    el("p", { text: "Loading settings…" }),
  );
  target.replaceChildren(root);
  let data = await api("/api/library/settings");
  if (!root.isConnected) return;
  const status = el("p", { role: "status", "aria-live": "polite" });
  const onlyPlayback = el("input", {
    type: "checkbox",
    disabled: data.playback_locked,
  });
  onlyPlayback.checked = data.playback_only;
  const save = el("button", {
    type: "submit",
    class: "primary",
    text: "Save server mode",
  });
  const server = el(
    "form",
    { class: "section" },
    el("h2", { text: "Server" }),
    el("p", {
      class: "muted",
      text: "Server mode and saved voice profiles apply to everyone using this server.",
    }),
    el("label", { class: "check" }, onlyPlayback, "Playback only"),
    el("p", {
      class: "muted",
      text: data.playback_locked
        ? "Playback-only mode was set at startup. Restart without that option to enable generation."
        : "Playback-only mode hides generation and cache-clearing controls and stops pending generation. Completed recordings remain playable.",
    }),
    save,
    status,
  );
  server.onsubmit = async (event) => {
    event.preventDefault();
    save.disabled = true;
    try {
      data = await post("/api/library/settings", {
        configuration: {
          ...data.configuration,
          playback_only: data.playback_locked || onlyPlayback.checked,
        },
        revision: data.revision,
      });
      status.textContent = "Server mode saved.";
      for (const button of document.querySelectorAll("[data-profile-preview]"))
        button.disabled = data.playback_only;
    } catch (error) {
      status.textContent = error.message;
    } finally {
      save.disabled = false;
    }
  };
  const continuing = el("input", { type: "checkbox" });
  continuing.checked = getStored("continue-blocks", true);
  const ahead = el("input", {
    type: "number",
    min: "0",
    max: "8",
    step: "1",
    "aria-label": "Blocks ahead",
  });
  ahead.value = String(getStored("blocks-ahead", 2));
  continuing.onchange = () => {
    store("continue-blocks", continuing.checked);
    const controller = player.lectureController;
    if (controller) {
      controller.continueBlocks.checked = continuing.checked;
      controller.ahead.disabled = !continuing.checked;
    }
  };
  ahead.onchange = () => {
    const count = Math.max(
      0,
      Math.min(8, Math.floor(Number(ahead.value) || 0)),
    );
    ahead.value = String(count);
    store("blocks-ahead", count);
    if (player.lectureController)
      player.lectureController.ahead.value = String(count);
  };
  const profiles = el("section", { id: "voice-profiles" });
  root.replaceChildren(
    el("h1", { text: "Settings" }),
    server,
    profiles,
    el(
      "section",
      { class: "section" },
      el("h2", { text: "Playback on this device" }),
      el("p", {
        class: "muted",
        text: "These choices save immediately on this device. Continuous playback defaults to on with two blocks ahead. Playback speed in the player never changes the saved recording.",
      }),
      el("label", { class: "check" }, continuing, "Continue to next blocks"),
      el("label", {}, "Blocks ahead", ahead),
    ),
  );
  await renderVoiceProfiles(profiles, {
    playbackOnly: () => data.playback_only,
    player,
    message,
  });
}

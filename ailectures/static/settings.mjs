import { api, post, el, getStored, store } from "./api.mjs";

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
  let draft = structuredClone(data.configuration),
    revision = data.revision;
  if (!data.profiles.some((row) => row.id === draft.default_profile))
    draft.default_profile = null;
  const status = el("p", { role: "status", "aria-live": "polite" });
  const fail = (error) => {
    status.textContent = error.message;
  };
  const policyFor = (id) =>
    (draft.profiles[id] ||= { default_voice: null, quick_voices: null });

  function draw() {
    if (!root.isConnected) return;
    const expanded = new Set(
      [...root.querySelectorAll("details[data-profile][open]")].map(
        (node) => node.dataset.profile,
      ),
    );
    const onlyPlayback = el("input", {
      type: "checkbox",
      disabled: data.playback_locked,
    });
    onlyPlayback.checked = data.playback_locked || draft.playback_only;
    onlyPlayback.onchange = () => {
      draft.playback_only = onlyPlayback.checked;
    };
    const profile = el(
      "select",
      { "aria-label": "Default TTS profile" },
      el("option", { value: "", text: "Use configured default" }),
      ...data.profiles.map((row) =>
        el("option", { value: row.id, text: row.label }),
      ),
    );
    profile.value = draft.default_profile || "";
    profile.onchange = () => {
      draft.default_profile = profile.value || null;
    };
    const save = el("button", {
      type: "submit",
      class: "primary",
      text: "Save server settings",
    });
    const form = el(
      "form",
      { class: "section" },
      el("h2", { text: "Server" }),
      el("p", {
        class: "muted",
        text: "These preferences apply to everyone using this server. Existing recordings are kept.",
      }),
      el("label", { class: "check" }, onlyPlayback, "Playback only"),
      el("p", {
        class: "muted",
        text: data.playback_locked
          ? "Playback-only mode was set at startup. Restart without that option to enable generation."
          : "Playback-only mode hides generation and cache-clearing controls and stops pending generation. Completed audio remains available.",
      }),
      el("p", {
        text: data.tools_available
          ? "Audio generation tools are installed."
          : "This installation can serve prepared recordings; audio generation tools are unavailable.",
      }),
      el("label", {}, "Default TTS profile", profile),
      el("p", {
        class: "muted",
        text: "Connections, models and audio formats come from the server’s TTS configuration. Voice defaults below apply when a device has not already selected a voice.",
      }),
    );
    form.onsubmit = async (event) => {
      event.preventDefault();
      save.disabled = true;
      status.textContent = "Saving…";
      try {
        if (data.playback_locked) draft.playback_only = true;
        data = await post("/api/library/settings", {
          configuration: draft,
          revision,
        });
        draft = structuredClone(data.configuration);
        revision = data.revision;
        draw();
        status.textContent = "Server settings saved.";
      } catch (error) {
        fail(error);
      } finally {
        save.disabled = false;
      }
    };
    const voices = el(
      "section",
      {},
      el("h2", { text: "Voices" }),
      el("p", {
        class: "muted",
        text: "Choose each profile’s default and quick-select voices. More voices always contains the full catalog. A voice you are using or actively generating stays accessible.",
      }),
    );
    if (!data.profiles.length)
      voices.append(
        el("p", {
          text: "No TTS profiles or prepared voices are available. Configure a TTS profile or install recordings to manage voices here.",
        }),
      );
    for (const row of data.profiles) {
      const catalog = data.voices[row.id],
        policy = policyFor(row.id);
      const labels = new Map(
        catalog.registered.map((voice) => [voice.voice, voice.label]),
      );
      const defaultVoice = el(
        "select",
        { "aria-label": `Default voice for ${row.label}` },
        el("option", {
          value: "",
          text: `Use configured default (${catalog.default_voice})`,
        }),
        ...catalog.voices.map((voice) =>
          el("option", { value: voice, text: labels.get(voice) || voice }),
        ),
      );
      defaultVoice.value = policy.default_voice || "";
      defaultVoice.onchange = () => {
        policy.default_voice = defaultVoice.value || null;
      };
      const automatic = el("input", { type: "checkbox" });
      automatic.checked = policy.quick_voices === null;
      const list = el("div", { class: "voice-settings-list" });
      const search = el("input", {
        type: "search",
        placeholder: "Find a voice",
        "aria-label": `Find a voice in ${row.label}`,
      });
      const checks = catalog.voices.map((voice) => {
        const checkbox = el("input", {
          type: "checkbox",
          disabled: automatic.checked,
        });
        checkbox.checked =
          policy.quick_voices?.includes(voice) ??
          voice === catalog.default_voice;
        const label = el(
          "label",
          { class: "check" },
          checkbox,
          labels.get(voice) || voice,
        );
        checkbox.onchange = () => {
          policy.quick_voices = checks
            .filter((item) => item.checkbox.checked)
            .map((item) => item.voice);
        };
        list.append(label);
        return { voice, checkbox, label };
      });
      automatic.onchange = () => {
        policy.quick_voices = automatic.checked
          ? null
          : checks
              .filter((item) => item.checkbox.checked)
              .map((item) => item.voice);
        for (const item of checks) item.checkbox.disabled = automatic.checked;
      };
      search.oninput = () => {
        const query = search.value.trim().toLowerCase();
        for (const item of checks)
          item.label.hidden = !`${labels.get(item.voice) || ""} ${item.voice}`
            .toLowerCase()
            .includes(query);
      };
      const panel = el(
        "details",
        {
          class: "section",
          "data-profile": row.id,
          open: expanded.has(row.id),
        },
        el("summary", {
          text: `${row.label} · ${catalog.voices.length} voices`,
        }),
        el("p", {
          class: "muted",
          text: [
            row.model,
            row.output_format === "ogg"
              ? "Ogg Opus"
              : row.output_format === "mp3"
                ? "MP3"
                : "Prepared audio",
          ]
            .filter(Boolean)
            .join(" · "),
        }),
        el("label", {}, "Default voice", defaultVoice),
        el("label", { class: "check" }, automatic, "Automatic quick select"),
        el("p", {
          class: "muted",
          text: "Automatic includes prepared voices, active jobs and profile defaults. Turn it off to choose the quick-select voices below.",
        }),
        search,
        list,
      );
      if (row.configured) {
        const refresh = el("button", {
          type: "button",
          text: "Refresh available voices",
          onclick: async () => {
            refresh.disabled = true;
            status.textContent = "Refreshing voices…";
            try {
              data = await post("/api/library/settings/voices", {
                profile: row.id,
                refresh: true,
              });
              draw();
              status.textContent = "Voice catalog refreshed.";
            } catch (error) {
              fail(error);
            } finally {
              refresh.disabled = false;
            }
          },
        });
        const id = el("input", {
          "aria-label": `Voice ID for ${row.label}`,
          placeholder: "Voice ID",
        });
        const label = el("input", {
          "aria-label": `Voice label for ${row.label}`,
          placeholder: "Display name (optional)",
        });
        const register = el("button", {
          type: "button",
          text: "Register voice",
          onclick: async () => {
            register.disabled = true;
            try {
              data = await post("/api/library/settings/voices", {
                profile: row.id,
                voice: id.value.trim(),
                label: label.value.trim() || null,
              });
              draw();
              status.textContent =
                "Voice registered. Choose its default and quick-select settings, then save.";
            } catch (error) {
              fail(error);
            } finally {
              register.disabled = false;
            }
          },
        });
        panel.append(
          refresh,
          el(
            "details",
            {},
            el("summary", { text: "Register a voice ID" }),
            id,
            label,
            register,
          ),
        );
      }
      voices.append(panel);
    }
    form.append(voices, save, status);
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
    const useDefault = el("button", {
      type: "button",
      text: "Use server default on this device",
      onclick: () => {
        const profile =
          data.profiles.find(
            (row) => row.id === data.configuration.default_profile,
          ) || data.profiles[0];
        if (!profile) return;
        const voice =
          data.configuration.profiles[profile.id]?.default_voice ||
          data.voices[profile.id].default_voice;
        store(
          "narrator-choice",
          profile.id === "prepared"
            ? `recording:${voice}`
            : `tts:${profile.id}:${voice}`,
        );
        store("production-profile", profile.id);
        store(`production-voice:${profile.id}`, voice);
        message(
          "The server default will be selected when you next open a lecture. Current playback is unchanged.",
        );
      },
    });
    root.replaceChildren(
      el("h1", { text: "Settings" }),
      form,
      el(
        "section",
        { class: "section" },
        el("h2", { text: "Playback on this device" }),
        el("p", {
          class: "muted",
          text: "These choices save immediately on this device. New devices default to continuous playback with two blocks ahead.",
        }),
        el("label", { class: "check" }, continuing, "Continue to next blocks"),
        el("label", {}, "Blocks ahead", ahead),
        useDefault,
      ),
    );
  }
  draw();
}

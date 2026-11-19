import { api, post, el, store } from "./api.mjs";

export async function renderVoiceProfiles(
  root,
  { playbackOnly, player, message },
) {
  let catalog = await api("/api/library/voice-profiles?archived=1");
  if (!root.isConnected) return;
  const status = el("p", { role: "status", "aria-live": "polite" });
  async function refresh() {
    catalog = await api("/api/library/voice-profiles?archived=1");
    if (root.isConnected) draw();
  }
  async function action(id, payload) {
    try {
      await post(`/api/library/voice-profiles/${id}/action`, payload);
      await refresh();
    } catch (error) {
      status.textContent = error.message;
    }
  }
  function draw() {
    const active = catalog.profiles.filter((row) => !row.archived);
    const archived = catalog.profiles.filter((row) => row.archived);
    function profileRow(row) {
      const quick = el("input", {
        type: "checkbox",
        "aria-label": "Quick select: " + row.label,
      });
      quick.checked = row.quick_select;
      quick.onchange = () =>
        action(row.id, { action: "pin", quick: quick.checked });
      const more = el(
        "details",
        { class: "voice-profile-options" },
        el("summary", {
          text: "More",
          "aria-label": "More options for " + row.label,
        }),
        el(
          "div",
          { class: "actions" },
          row.archived
            ? el("button", {
                type: "button",
                text: "Restore profile",
                onclick: () => action(row.id, { action: "restore" }),
              })
            : catalog.default_profile === row.id
              ? null
              : el("button", {
                  type: "button",
                  text: "Make default",
                  onclick: () => action(row.id, { action: "default" }),
                }),
          el("button", {
            type: "button",
            text: "Duplicate profile",
            disabled: !row.available,
            onclick: () => edit(row, true),
          }),
          row.archived
            ? null
            : el("button", {
                type: "button",
                text: "Archive profile",
                onclick: () => action(row.id, { action: "archive" }),
              }),
          el("label", { class: "check" }, quick, "Quick select"),
        ),
        el("p", {
          class: "muted",
          text: `${row.output_format === "ogg" ? "Ogg Opus" : "MP3"} · native rate ${row.native_rate}× · saved-audio tempo ${row.tempo}×`,
        }),
        el(
          "details",
          {},
          el("summary", { text: "Profile identity" }),
          el("code", { text: row.id }),
          el("p", { text: row.revision }),
        ),
      );
      return el(
        "li",
        { class: "voice-profile-row" },
        el(
          "div",
          { class: "voice-profile-line" },
          el(
            "div",
            { class: "voice-profile-name" },
            el("strong", { text: row.label }),
            catalog.default_profile === row.id && !row.archived
              ? el("span", { class: "voice-profile-default", text: "Default" })
              : null,
            el("small", {
              class: "muted",
              text: `${row.model} · ${row.voice}${row.available ? "" : " · unavailable"}`,
            }),
          ),
          !row.archived
            ? el("button", {
                type: "button",
                text: "Edit",
                "aria-label": "Edit " + row.label,
                disabled: !row.available,
                onclick: () => edit(row),
              })
            : null,
        ),
        more,
      );
    }
    root.replaceChildren(
      ...[
        el(
          "div",
          { class: "voice-profile-heading" },
          el("h2", { text: "Saved voice profiles" }),
          el("button", {
            type: "button",
            text: "Add profile",
            disabled: !catalog.backends.some((row) => row.available),
            onclick: () => edit(),
          }),
        ),
        status,
        active.length
          ? el(
              "ul",
              {
                class: "voice-profile-list",
                "aria-label": "Available voice profiles",
              },
              ...active.map(profileRow),
            )
          : el("p", {
              class: "muted",
              text: "No voice profiles yet. Add one using an available speech backend.",
            }),
        archived.length
          ? el(
              "details",
              { class: "voice-profile-archived" },
              el("summary", { text: `Archived profiles (${archived.length})` }),
              el(
                "ul",
                {
                  class: "voice-profile-list",
                  "aria-label": "Archived voice profiles",
                },
                ...archived.map(profileRow),
              ),
            )
          : null,
        el(
          "details",
          { class: "voice-profile-device" },
          el("summary", { text: "Selection on this device" }),
          el("button", {
            type: "button",
            text: "Use server default on this device",
            disabled: !catalog.default_profile,
            onclick: () => {
              store("narrator-choice", "profile:" + catalog.default_profile);
              store("production-profile", catalog.default_profile);
              message(
                "The saved default profile will be selected when you next open a lecture. Current playback is unchanged.",
              );
            },
          }),
        ),
      ].filter(Boolean),
    );
  }
  async function edit(existing = null, duplicate = false) {
    const dialog = el("dialog", {
      class: "voice-profile-dialog",
      "aria-label": existing
        ? duplicate
          ? "Duplicate voice profile"
          : "Edit voice profile"
        : "Create voice profile",
    });
    document.body.append(dialog);
    const error = el("p", { role: "status", "aria-live": "polite" });
    const label = el("input", {
      required: true,
      maxlength: "100",
      "aria-label": "Profile name",
    });
    label.value = existing ? existing.label + (duplicate ? " copy" : "") : "";
    const backend = el(
      "select",
      {
        "aria-label": "Speech backend",
        disabled: Boolean(existing && !duplicate),
      },
      ...catalog.backends
        .filter((row) => row.available)
        .map((row) => el("option", { value: row.id, text: row.label })),
    );
    if (existing) backend.value = existing.backend_id;
    const voice = el("select", {
      "aria-label": "Voice or reference",
    });
    const voiceStatus = el("p", {
      class: "muted",
      role: "status",
      "aria-live": "polite",
    });
    const fields = el("div"),
      preview = el("div");
    const registerId = el("input", {
      "aria-label": "Backend voice ID",
      placeholder: "Voice ID already installed on this backend",
    });
    const refreshVoices = el("button", {
      type: "button",
      text: "Refresh backend voices",
      onclick: async () => {
        refreshVoices.disabled = true;
        try {
          await discoverVoices(backend.value, token);
        } catch (failure) {
          error.textContent = failure.message;
        } finally {
          refreshVoices.disabled = false;
        }
      },
    });
    const registerVoice = el("button", {
      type: "button",
      text: "Register voice ID",
      onclick: async () => {
        registerVoice.disabled = true;
        try {
          await post(
            `/api/library/voice-profiles/backends/${backend.value}/voices`,
            { voice: registerId.value.trim() },
          );
          const data = await api(
            `/api/library/voice-profiles/backends/${backend.value}/voices`,
          );
          voiceOptions(data, registerId.value.trim());
          await voice.onchange();
          registerId.value = "";
        } catch (failure) {
          error.textContent = failure.message;
        } finally {
          registerVoice.disabled = false;
        }
      },
    });
    const save = el("button", {
      type: "submit",
      class: "primary",
      text: "Save voice profile",
    });
    const test = el("button", {
      type: "button",
      text: "Test title and prose",
      "data-profile-preview": "",
      disabled: playbackOnly() || !catalog.tools_available,
    });
    const close = () => {
      preview.querySelector("audio")?.pause();
      dialog.close();
      dialog.remove();
    };
    const form = el(
      "form",
      {},
      el("h2", {
        text: existing
          ? duplicate
            ? "Duplicate voice profile"
            : "Edit voice profile"
          : "Create voice profile",
      }),
      el("p", {
        class: "muted",
        text:
          existing && !duplicate
            ? "Change the voice reference or speaking settings. Saving creates a new revision; existing recordings stay available."
            : "Choose a backend voice, then set how it speaks normal text and titles.",
      }),
      el("label", {}, "Profile name", label),
      el(
        "div",
        { class: "filters" },
        el("label", {}, "Backend", backend),
        el("label", {}, "Voice/reference", voice),
      ),
      voiceStatus,
      el(
        "details",
        {},
        el("summary", { text: "Backend voice catalog" }),
        el("p", {
          class: "muted",
          text: "Refresh advertised voices, or register an ID already supported by this backend. Registration does not upload or create a reference voice.",
        }),
        refreshVoices,
        el("label", {}, "Backend voice ID", registerId),
        registerVoice,
      ),
      fields,
      error,
      el(
        "div",
        { class: "actions" },
        save,
        test,
        el("button", { type: "button", text: "Cancel", onclick: close }),
      ),
      preview,
    );
    dialog.append(form);
    dialog.showModal();
    dialog.oncancel = (event) => {
      event.preventDefault();
      close();
    };
    let settings,
      readSettings,
      token = 0;
    const selectedBackend = () =>
      catalog.backends.find((row) => row.id === backend.value);
    function identity() {
      return {
        ...(existing
          ? duplicate
            ? { duplicate_of: existing.id }
            : { id: existing.id, expected_revision: existing.revision }
          : {}),
        backend_id: backend.value,
        voice: voice.value,
      };
    }
    function voiceOptions(data, preferred) {
      voice.replaceChildren(
        ...data.voices.map((row) =>
          el("option", {
            value: row.voice,
            text: row.label + (row.reference ? " · reference" : ""),
          }),
        ),
      );
      if (preferred) {
        if (!data.voices.some((row) => row.voice === preferred))
          voice.append(
            el("option", {
              value: preferred,
              text: preferred + " · saved voice",
            }),
          );
        voice.value = preferred;
      }
    }
    async function discoverVoices(backendId, generation) {
      voiceStatus.textContent = "Checking the server for available voices…";
      try {
        const data = await post(
          `/api/library/voice-profiles/backends/${backendId}/voices`,
          { refresh: true },
        );
        if (
          !dialog.isConnected ||
          generation !== token ||
          backend.value !== backendId
        )
          return;
        voiceOptions(data, voice.value);
        voiceStatus.textContent =
          data.discovery === "live"
            ? `${data.voices.length} available voices · server catalog updated`
            : "Server discovery unavailable. Showing saved voices; you can retry under Backend voice catalog.";
      } catch (failure) {
        if (dialog.isConnected && generation === token)
          voiceStatus.textContent =
            "Could not refresh server voices. Your saved choices remain available.";
      }
    }
    async function loadVoiceOptions(preferred = null, discover = true) {
      const generation = ++token;
      save.disabled = test.disabled = true;
      try {
        const data = await api(
          `/api/library/voice-profiles/backends/${backend.value}/voices`,
        );
        if (!dialog.isConnected || generation !== token) return;
        voiceOptions(data, preferred);
        if (existing && !duplicate) {
          const data = await api(`/api/library/voice-profiles/${existing.id}`);
          settings = data.settings;
        } else if (
          existing &&
          duplicate &&
          voice.value === existing.voice &&
          backend.value === existing.backend_id
        ) {
          const data = await api(`/api/library/voice-profiles/${existing.id}`);
          settings = data.settings;
        } else {
          const data = await post(
            "/api/library/voice-profiles/template",
            identity(),
          );
          settings = data.settings;
        }
        if (!dialog.isConnected || generation !== token) return;
        drawFields();
        save.disabled = false;
        test.disabled = playbackOnly() || !catalog.tools_available;
        if (discover) void discoverVoices(backend.value, generation);
      } catch (failure) {
        error.textContent = failure.message;
      }
    }
    function drawFields() {
      const cap = selectedBackend().capabilities;
      const number = (title, value, min, max, step = ".05") => {
        const input = el("input", {
          type: "number",
          "aria-label": title,
          min,
          max,
          step,
        });
        input.value = value;
        return { input, label: el("label", {}, title, input) };
      };
      const native = number(
        "Native speaking rate",
        settings.native_rate,
        ".5",
        "2",
      );
      native.input.disabled = !cap.native_rate;
      const tempo = number("Saved-audio tempo", settings.tempo, ".5", "2");
      const mode = el(
        "select",
        { "aria-label": "Prose delivery" },
        ...(cap.paragraph_delivery
          ? [
              el("option", {
                value: "paragraph",
                text: "Stable paragraph narration",
              }),
            ]
          : []),
        el("option", {
          value: "directed",
          text: cap.instruction_field
            ? "Directed narration"
            : "Standard narration",
        }),
      );
      mode.value = settings.body_mode;
      const body = el("textarea", {
        "aria-label": "Normal text instructions",
        placeholder: "Optional directions for normal narration",
        maxlength: "4000",
      });
      body.value = settings.body_request[cap.instruction_field] || "";
      const cfg = number(
        "Prose CFG",
        settings.body_request.cfg_scale ?? 1,
        ".1",
        "20",
        ".1",
      );
      const titleOn = el("input", { type: "checkbox" });
      titleOn.checked = settings.title_enabled;
      const titleDirections = el("input", {
        type: "checkbox",
        disabled: !cap.instruction_field,
      });
      titleDirections.checked = Boolean(
        settings.title_instruction_field &&
        settings.title_instruction_field !== "none",
      );
      const title = el("textarea", {
        "aria-label": "Title instructions",
        maxlength: "4000",
      });
      title.value = settings.title_instruction;
      const before = number(
        "Pause before title (seconds)",
        settings.title_pause_before,
        "0",
        "5",
      );
      const after = number(
        "Pause after title (seconds)",
        settings.title_pause_after,
        "0",
        "5",
      );
      const titleCfg = number(
        "Title CFG",
        settings.title_cfg_scale ?? 4,
        ".1",
        "20",
        ".1",
      );
      const processing = el("input", { type: "checkbox" });
      processing.checked = settings.processing.enabled;
      const loudness = number(
        "Target loudness (LUFS)",
        settings.processing.target_lufs,
        "-36",
        "-10",
        ".5",
      );
      const peak = number(
        "Peak limit (dB)",
        settings.processing.peak_db,
        "-9",
        "-.1",
        ".1",
      );
      const highpass = number(
        "High-pass cutoff (Hz)",
        settings.processing.highpass_hz,
        "0",
        "500",
        "1",
      );
      const compression = el("input", { type: "checkbox" });
      compression.checked = settings.processing.compression;
      const format = el(
        "select",
        { "aria-label": "Saved audio format" },
        el("option", { value: "ogg", text: "Ogg Opus" }),
        el("option", { value: "mp3", text: "MP3" }),
      );
      format.value = settings.output_format;
      const generation = el("input", {
        "aria-label": "Voice/model generation revision",
        maxlength: "120",
        required: true,
      });
      generation.value = settings.generation_revision;
      const extras = el("textarea", {
        "aria-label": "Additional engine parameters (JSON)",
        maxlength: "12000",
      });
      const request = { ...settings.body_request };
      for (const key of [
        "instruction",
        "instructions",
        "voice_direction",
        "direction",
      ])
        delete request[key];
      if (cap.adapter === "breeze-tts2") delete request.cfg_scale;
      extras.value = JSON.stringify(request, null, 2);
      const pronunciation = el("textarea", {
        "aria-label": "Pronunciation replacements (JSON)",
        maxlength: "30000",
      });
      pronunciation.value = JSON.stringify(
        settings.pronunciation_replacements,
        null,
        2,
      );
      const reader = el("textarea", {
        "aria-label": "Chunk bounds (JSON)",
        maxlength: "2000",
      });
      reader.value = JSON.stringify(settings.reader, null, 2);
      const processingExtra = el("textarea", {
        "aria-label": "Processing settings (JSON)",
        maxlength: "4000",
      });
      processingExtra.value = JSON.stringify(settings.processing, null, 2);
      const bodyHint = el("p", { class: "muted" });
      function available() {
        body.disabled = !cap.instruction_field;
        bodyHint.textContent =
          mode.value === "paragraph"
            ? "Optional. Enter instructions to switch to directed narration. Leave blank for stable paragraph cloning."
            : "These instructions apply to normal text. Titles use their own instructions below.";
        cfg.input.disabled = mode.value === "paragraph";
        title.disabled =
          !titleOn.checked ||
          !titleDirections.checked ||
          !cap.instruction_field;
        before.input.disabled = after.input.disabled = !titleOn.checked;
        titleCfg.input.disabled = !titleOn.checked || !titleDirections.checked;
        loudness.input.disabled =
          peak.input.disabled =
          highpass.input.disabled =
          compression.disabled =
            !processing.checked;
      }
      mode.onchange = () => {
        if (
          mode.value === "directed" &&
          cap.adapter === "breeze-tts2" &&
          Number(cfg.input.value) === 1
        )
          cfg.input.value = "4";
        available();
      };
      body.oninput = () => {
        if (body.value.trim() && mode.value === "paragraph") {
          mode.value = "directed";
          mode.onchange();
        }
      };
      titleOn.onchange =
        titleDirections.onchange =
        processing.onchange =
          available;
      fields.replaceChildren(
        ...[
          el("h3", { text: "Normal text" }),
          el("label", {}, "Prose delivery", mode),
          cap.instruction_field
            ? el("label", {}, "Normal text instructions", body)
            : null,
          cap.instruction_field ? bodyHint : null,
          el("h3", { text: "Section titles" }),
          el("label", { class: "check" }, titleOn, "Separate title delivery"),
          cap.instruction_field
            ? el(
                "label",
                { class: "check" },
                titleDirections,
                "Use a title instruction",
              )
            : el("p", {
                class: "muted",
                text: "Title instructions are unavailable on this adapter. Isolated title requests and pauses are still supported.",
              }),
          cap.instruction_field
            ? el("label", {}, "Title instructions", title)
            : null,
          el("div", { class: "filters" }, before.label, after.label),
          el("h3", { text: "Speaking rate" }),
          el("div", { class: "filters" }, native.label, tempo.label),
          el("p", {
            class: "muted",
            text: cap.native_rate
              ? "Native rate is sent to this backend. Saved-audio tempo is applied after synthesis; neither is the player’s playback speed."
              : "This backend does not advertise native speaking-rate control. Saved-audio tempo is postprocessing, not a server synthesis instruction.",
          }),
          el("h3", { text: "Saved audio processing" }),
          el(
            "label",
            { class: "check" },
            processing,
            "Apply loudness and shaping",
          ),
          el(
            "div",
            { class: "filters" },
            loudness.label,
            peak.label,
            highpass.label,
          ),
          el("label", { class: "check" }, compression, "Compression"),
          el("label", {}, "Saved format", format),
          el("label", {}, "Voice/model generation revision", generation),
          el("p", {
            class: "muted",
            text: "Change the generation revision when server-side model weights or reference material changes. Renaming a profile or changing quick select does not change its audio revision.",
          }),
          el(
            "details",
            {},
            el("summary", { text: "Advanced recipe settings" }),
            ...(cap.adapter === "breeze-tts2"
              ? [cfg.label, titleCfg.label]
              : []),
            el("label", {}, "Additional engine parameters (JSON)", extras),
            el("label", {}, "Pronunciation replacements (JSON)", pronunciation),
            el("label", {}, "Chunk bounds (JSON)", reader),
            el("label", {}, "Processing settings (JSON)", processingExtra),
          ),
        ].filter((value) => value !== null && value !== undefined),
      );
      available();
      readSettings = () => {
        const bodyRequest = JSON.parse(extras.value);
        if (
          !bodyRequest ||
          typeof bodyRequest !== "object" ||
          Array.isArray(bodyRequest)
        )
          throw Error("Engine parameters must be a JSON object");
        if (
          cap.instruction_field &&
          mode.value === "directed" &&
          body.value.trim()
        )
          bodyRequest[cap.instruction_field] = body.value.trim();
        if (cap.adapter === "breeze-tts2")
          bodyRequest.cfg_scale =
            mode.value === "paragraph" ? 1 : Number(cfg.input.value);
        return {
          native_rate: cap.native_rate ? Number(native.input.value) : 1,
          tempo: Number(tempo.input.value),
          body_mode: mode.value,
          body_request: bodyRequest,
          title_enabled: titleOn.checked,
          title_instruction_field:
            titleDirections.checked && cap.instruction_field
              ? cap.instruction_field
              : null,
          title_instruction: title.value,
          title_pause_before: Number(before.input.value),
          title_pause_after: Number(after.input.value),
          title_cfg_scale:
            cap.adapter === "breeze-tts2" ? Number(titleCfg.input.value) : null,
          processing: {
            ...JSON.parse(processingExtra.value),
            enabled: processing.checked,
            target_lufs: Number(loudness.input.value),
            peak_db: Number(peak.input.value),
            highpass_hz: Number(highpass.input.value),
            compression: compression.checked,
          },
          output_format: format.value,
          generation_revision: generation.value.trim(),
          pronunciation_replacements: JSON.parse(pronunciation.value),
          reader: JSON.parse(reader.value),
        };
      };
    }
    backend.onchange = () => loadVoiceOptions();
    let voiceChange = 0;
    voice.onchange = async () => {
      const change = ++voiceChange,
        generation = token;
      const selected = voice.value;
      save.disabled = test.disabled = true;
      try {
        const draft = readSettings?.();
        const data = await post("/api/library/voice-profiles/template", {
          ...identity(),
          ...(draft ? { settings: draft } : {}),
        });
        if (
          !dialog.isConnected ||
          change !== voiceChange ||
          generation !== token ||
          voice.value !== selected
        )
          return;
        settings = data.settings;
        drawFields();
        error.textContent = "";
      } catch (failure) {
        if (
          dialog.isConnected &&
          change === voiceChange &&
          generation === token
        )
          error.textContent = failure.message;
      } finally {
        if (
          dialog.isConnected &&
          change === voiceChange &&
          generation === token
        ) {
          save.disabled = false;
          test.disabled = playbackOnly() || !catalog.tools_available;
        }
      }
    };
    form.onsubmit = async (event) => {
      event.preventDefault();
      save.disabled = test.disabled = true;
      try {
        await post("/api/library/voice-profiles/save", {
          ...identity(),
          label: label.value.trim(),
          settings: readSettings(),
        });
        close();
        await refresh();
        status.textContent =
          "Voice profile saved. Previous revisions and recordings are retained.";
      } catch (failure) {
        error.textContent = failure.message;
        save.disabled = false;
        test.disabled = playbackOnly() || !catalog.tools_available;
      }
    };
    test.onclick = async () => {
      test.disabled = save.disabled = true;
      error.textContent = "Generating a short title and prose preview…";
      try {
        const data = await post("/api/library/voice-profiles/preview", {
          ...identity(),
          label: label.value.trim() || "Preview",
          settings: readSettings(),
        });
        if (!dialog.isConnected) return;
        const audio = el("audio", {
          controls: true,
          src: data.url,
          "aria-label": "Profile title and prose preview",
        });
        audio.onplay = () => player.audio.pause();
        preview.replaceChildren(audio);
        error.textContent = "Preview ready.";
      } catch (failure) {
        error.textContent = failure.message;
      } finally {
        if (dialog.isConnected) {
          save.disabled = false;
          test.disabled = playbackOnly() || !catalog.tools_available;
        }
      }
    };
    await loadVoiceOptions(existing?.voice);
  }
  draw();
}

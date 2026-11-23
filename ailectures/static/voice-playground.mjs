import { api, post, el } from "./api.mjs";

export const DEFAULT_PREVIEW_TEXT = "A familiar voice can make a new idea easier to follow. Take a moment to listen to the pace, the pronunciation, and the pauses between these sentences.";

export function voicePlayground({ catalog, playbackOnly, player, text = DEFAULT_PREVIEW_TEXT, preferred, onText, onProfile }) {
  const profiles = catalog.profiles.filter((row) => row.available && !row.archived);
  let generation = 0, disposed = false, loading = false, generating = false;
  let voiceLabels = new Map();
  const profile = el("select", { "aria-label": "Preview voice profile" },
    ...profiles.map((row) => el("option", { value: row.id, text: row.label + " · " + row.model })));
  if (profiles.some((row) => row.id === preferred)) profile.value = preferred;
  else if (profiles.some((row) => row.id === catalog.default_profile)) profile.value = catalog.default_profile;
  const voice = el("select", { "aria-label": "Preview voice" });
  const input = el("textarea", { "aria-label": "Text to speak", maxlength: "6000", rows: "4" });
  input.value = text;
  input.oninput = () => onText(input.value);
  const status = el("p", { class: "muted", role: "status", "aria-live": "polite" });
  const generate = el("button", { type: "button", class: "primary", text: "Generate preview", "data-profile-preview": "" });
  const refresh = el("button", { type: "button", text: "Refresh voices" });
  const results = el("div", { class: "voice-preview-results" });
  const root = el("section", { class: "voice-playground", "aria-label": "Try voices" },
    el("h3", { text: "Try voices" }),
    el("p", { class: "muted", text: "Enter your own text, choose a voice, and compare previews. Uses the selected profile’s speaking settings without saving changes." }),
    el("label", {}, "Text to speak", input),
    el("div", { class: "filters" }, el("label", {}, "Profile settings", profile), el("label", {}, "Voice", voice)),
    el("div", { class: "actions" }, generate, refresh), status, results);
  const selected = () => profiles.find((row) => row.id === profile.value);
  function controls() {
    generate.disabled = playbackOnly() || !catalog.tools_available || !selected() || !voice.value || loading || generating;
    profile.disabled = voice.disabled = generating || !profiles.length;
    refresh.disabled = !selected() || loading || generating;
  }
  function voiceOptions(data, preferredVoice) {
    voiceLabels = new Map(data.voices.map((row) => [row.voice, row.label]));
    voice.replaceChildren(...data.voices.map((row) => el("option", { value: row.voice, text: row.label })));
    if (preferredVoice) {
      if (!data.voices.some((row) => row.voice === preferredVoice)) voice.append(el("option", { value: preferredVoice, text: preferredVoice }));
      voice.value = preferredVoice;
    }
  }
  async function loadVoices(discover = false) {
    const chosen = selected();
    if (!chosen) { controls(); return; }
    const token = ++generation;
    const preferredVoice = discover ? voice.value : chosen.voice;
    if (!discover) voiceOptions({ voices: [{ voice: chosen.voice, label: chosen.voice }] }, chosen.voice);
    loading = true; controls();
    try {
      const endpoint = `/api/library/voice-profiles/backends/${chosen.backend_id}/voices`;
      const data = discover ? await post(endpoint, { refresh: true }) : await api(endpoint);
      if (disposed || token !== generation) return;
      voiceOptions(data, preferredVoice);
      status.textContent = playbackOnly() ? "Voice previews are unavailable in playback-only mode."
        : !catalog.tools_available ? "Voice previews need an available speech backend and FFmpeg tools."
        : discover && data.discovery !== "live" ? "The speech service could not be reached. Showing saved voice choices." : "";
    } catch (error) { if (!disposed && token === generation) status.textContent = error.message; }
    finally { if (!disposed && token === generation) { loading = false; controls(); } }
  }
  profile.onchange = () => { onProfile(profile.value); void loadVoices(); };
  refresh.onclick = () => loadVoices(true);
  generate.onclick = async () => {
    if (playbackOnly() || generating || loading) return;
    const chosen = selected(), spoken = input.value.trim(), selectedVoice = voice.value;
    const voiceLabel = voiceLabels.get(selectedVoice) || selectedVoice;
    if (!chosen || !selectedVoice) return;
    if (!spoken) { status.textContent = "Enter some text to preview."; input.focus(); return; }
    generating = true; controls(); status.textContent = "Generating your voice preview…";
    try {
      const data = await post("/api/library/voice-profiles/preview", {
        duplicate_of: chosen.id, backend_id: chosen.backend_id, voice: selectedVoice, text: spoken,
      });
      if (disposed || !root.isConnected) return;
      const audio = el("audio", { controls: true, src: data.url, "aria-label": "Voice preview: " + chosen.label + " · " + voiceLabel });
      audio.onplay = () => {
        player.audio.pause();
        for (const other of results.querySelectorAll("audio")) if (other !== audio) other.pause();
      };
      results.prepend(el("article", { class: "voice-preview-result" },
        el("strong", { text: chosen.label + " · " + voiceLabel }),
        el("p", { class: "muted", text: spoken.length > 180 ? spoken.slice(0, 180) + "…" : spoken }), audio));
      while (results.children.length > 4) {
        results.lastElementChild.querySelector("audio")?.pause();
        results.lastElementChild.remove();
      }
      status.textContent = "Preview ready. Choose another voice to compare the same text.";
    } catch (error) { if (!disposed) status.textContent = error.message; }
    finally { if (!disposed) { generating = false; controls(); } }
  };
  if (!profiles.length) status.textContent = "Add an available voice profile to try voices.";
  controls();
  void loadVoices();
  function dispose() {
    disposed = true; generation++; observer.disconnect();
    for (const audio of results.querySelectorAll("audio")) audio.pause();
  }
  const observer = new MutationObserver(() => { if (!root.isConnected) dispose(); });
  observer.observe(document.body, { childList: true, subtree: true });
  return { element: root, dispose };
}

import { el } from "./api.mjs";

export function voiceReferenceRecorder({ capability, save, onBusy, player }) {
  let stream, recorder, timer, deadline, take, previewURL, disposed = false;
  let microphoneRequest = 0, waitingForMicrophone = false;
  const name = el("input", { "aria-label": "Reference name", maxlength: "80", placeholder: "A name for this voice" });
  const prompt = el("textarea", { "aria-label": "Reference text prompt", maxlength: "4000", rows: "5" });
  prompt.value = capability.prompt;
  const status = el("p", { role: "status", "aria-live": "polite", class: "muted" });
  const preview = el("audio", { controls: true, hidden: true, "aria-label": "Your reference recording" });
  preview.onplay = () => player.audio.pause();
  const canRecord = Boolean(globalThis.isSecureContext && navigator.mediaDevices?.getUserMedia && globalThis.MediaRecorder);
  const record = el("button", { type: "button", text: canRecord ? "Start recording" : "Enable microphone recording" });
  const stop = el("button", { type: "button", text: "Stop recording", hidden: true });
  const upload = el("input", { type: "file", accept: ".webm,.ogg,.mp4,.m4a,.wav,.mp3", "aria-label": "Upload a reference recording" });
  const submit = el("button", { type: "button", class: "primary", text: "Save reference voice", disabled: true });
  const localAddress = globalThis.location?.hostname === "0.0.0.0"
    ? new URL("/settings#voice-profiles", globalThis.location.href) : null;
  if (localAddress) localAddress.hostname = "localhost";
  const accessHelp = el("aside", { class: "notice", role: "note", tabindex: "-1", hidden: canRecord },
    el("p", { text: !globalThis.isSecureContext
      ? "Your browser blocks microphone access at this HTTP address. Recording works over HTTP on localhost, or through HTTPS."
      : "This browser does not provide microphone recording. Open the library in a browser with microphone support, or upload a recording." }),
    localAddress ? el("p", {}, el("a", { href: localAddress.href, target: "_blank", rel: "noopener", text: "Open recording on localhost" }),
      " on the computer running this server. The 0.0.0.0 address is for server binding; localhost allows recording over HTTP.") : null,
    el("p", { text: "You can also record these words in another app and upload the audio below." }));
  const root = el("details", { class: "voice-reference-recorder" },
    el("summary", { text: "Record a reference voice" }),
    el("p", { text: `Read the prompt exactly in your normal speaking voice (${capability.min_seconds}–${capability.max_seconds} seconds). Review your take before saving.` }),
    el("p", { class: "muted", text: "Saved voices are available to everyone using this server for future generation. The reference recording and prompt stay on this server." }),
    el("label", {}, "Reference name", name),
    el("label", {}, "Words to read", prompt),
    accessHelp,
    el("div", { class: "actions" }, record, stop),
    status,
    el("label", {}, "Or upload a recording of these words", upload),
    preview, submit);

  function busy(value) {
    name.disabled = upload.disabled = value;
    prompt.readOnly = value;
    record.disabled = value;
    submit.disabled = value || !take;
    onBusy(value);
  }
  function fitPrompt() {
    if (!root.open) return;
    prompt.style.height = "auto";
    prompt.style.height = Math.max(160, prompt.scrollHeight + 4) + "px";
  }
  function releaseMicrophone() {
    clearInterval(timer); clearTimeout(deadline);
    stream?.getTracks().forEach((track) => track.stop());
    stream = null;
  }
  function clearTake() {
    take = null; submit.disabled = true;
    upload.value = "";
    preview.pause(); preview.removeAttribute("src"); preview.hidden = true;
    if (previewURL) URL.revokeObjectURL(previewURL);
    previewURL = null;
  }
  function review(blob) {
    clearTake();
    if (!blob.size || blob.size > capability.max_bytes) {
      status.textContent = "Use a recording smaller than 4 MiB.";
      return;
    }
    take = blob;
    previewURL = URL.createObjectURL(blob);
    preview.src = previewURL; preview.hidden = false; submit.disabled = false;
    if (canRecord) record.textContent = "Record another take";
    status.textContent = "Listen to your take and check that it matches the prompt, then save it.";
  }
  function stopRecording() {
    if (waitingForMicrophone) {
      waitingForMicrophone = false;
      ++microphoneRequest;
      if (!disposed) {
        busy(false); stop.hidden = true;
        status.textContent = "Microphone request cancelled. You can try again or upload a recording.";
      }
    }
    if (recorder?.state === "recording") recorder.stop();
    releaseMicrophone();
  }
  record.onclick = async () => {
    if (disposed) return;
    if (!canRecord) {
      accessHelp.hidden = false;
      accessHelp.focus(); accessHelp.scrollIntoView({ block: "nearest" });
      return;
    }
    if (prompt.value.trim().length < 20) { status.textContent = "Enter the words you will read (at least 20 characters)."; prompt.focus(); return; }
    const request = ++microphoneRequest;
    waitingForMicrophone = true;
    busy(true); status.textContent = "Waiting for microphone access…";
    stop.textContent = "Cancel microphone request"; stop.hidden = false;
    try {
      const input = await navigator.mediaDevices.getUserMedia({ audio: { channelCount: 1, echoCancellation: false, noiseSuppression: false, autoGainControl: false } });
      if (disposed || request !== microphoneRequest) { input.getTracks().forEach((track) => track.stop()); return; }
      waitingForMicrophone = false;
      stream = input;
      stop.textContent = "Stop recording";
      const type = ["audio/webm;codecs=opus", "audio/ogg;codecs=opus", "audio/mp4"].find((mime) => MediaRecorder.isTypeSupported(mime));
      recorder = new MediaRecorder(stream, type ? { mimeType: type } : {});
      const chunks = []; let bytes = 0, failed = false;
      const started = Date.now();
      recorder.ondataavailable = (event) => {
        bytes += event.data.size;
        if (bytes > capability.max_bytes) { failed = true; stopRecording(); }
        else if (event.data.size) chunks.push(event.data);
      };
      recorder.onerror = () => { failed = true; stopRecording(); };
      recorder.onstop = () => {
        releaseMicrophone();
        if (disposed) return;
        stop.hidden = true;
        busy(false);
        if (failed) { clearTake(); status.textContent = "This take could not be recorded. Try another take or upload an audio file."; }
        else review(new Blob(chunks, { type: recorder.mimeType }));
      };
      clearTake(); player.audio.pause();
      recorder.start(250); stop.hidden = false;
      fitPrompt(); prompt.scrollIntoView({ block: "center" });
      const update = () => { status.textContent = `Recording · ${Math.floor((Date.now() - started) / 1000)} / ${capability.max_seconds} seconds`; };
      update(); timer = setInterval(update, 1000);
      deadline = setTimeout(stopRecording, (capability.max_seconds - 0.5) * 1000);
    } catch (error) {
      if (disposed || request !== microphoneRequest) return;
      waitingForMicrophone = false;
      releaseMicrophone();
      stop.hidden = true;
      busy(false);
      status.textContent = error.name === "NotAllowedError"
        ? "Microphone access was not granted. Allow the microphone for this site in your browser’s address bar and system settings, then try again. You can also upload a recording."
        : error.name === "NotFoundError" ? "No microphone was found. Connect a microphone and try again, or upload a recording."
        : "Could not open the microphone. Check your input device and system permissions, then try again or upload a recording.";
    }
  };
  stop.onclick = stopRecording;
  root.addEventListener("toggle", () => { if (!root.open) stopRecording(); else fitPrompt(); });
  prompt.oninput = () => { fitPrompt(); clearTake(); status.textContent = "The words changed. Record or upload a new take matching this prompt."; };
  upload.onchange = () => {
    const file = upload.files[0];
    if (!file) return;
    const extension = file.name.split(".").pop().toLowerCase();
    const type = ({ webm: "audio/webm", ogg: "audio/ogg", mp4: "audio/mp4", m4a: "audio/mp4", wav: "audio/wav", mp3: "audio/mpeg" })[extension];
    if (!type) { clearTake(); status.textContent = "Choose a WebM, Ogg, MP4, WAV, or MP3 audio file."; return; }
    review(new Blob([file], { type }));
  };
  submit.onclick = async () => {
    if (!take) return;
    if (!name.value.trim()) { status.textContent = "Give this reference a name first."; name.focus(); return; }
    busy(true); status.textContent = "Saving your reference voice…";
    try {
      const audio_base64 = await new Promise((resolve, reject) => {
        const reader = new FileReader();
        reader.onload = () => resolve(reader.result.split(",")[1]);
        reader.onerror = () => reject(Error("Could not read this take. Record or upload it again."));
        reader.readAsDataURL(take);
      });
      if (disposed) return;
      const result = await save({ label: name.value.trim(), transcript: prompt.value.trim(), media_type: take.type, audio_base64 });
      if (disposed) return;
      clearTake();
      status.textContent = result.backend_visible
        ? "Reference saved and selected. Save the voice profile to use it for future generation."
        : "Reference saved and selected, but the speech service has not advertised it yet. Check that it shares this server’s reference folder, then refresh backend voices before generating.";
    } catch (error) { if (!disposed) status.textContent = error.message; }
    finally { if (!disposed) busy(false); }
  };
  function dispose() {
    if (disposed) return;
    disposed = true;
    stopRecording(); clearTake(); observer.disconnect();
    window.removeEventListener("pagehide", stopRecording);
    window.removeEventListener("resize", fitPrompt);
  }
  const observer = new MutationObserver(() => { if (!root.isConnected) dispose(); });
  observer.observe(document.body, { childList: true, subtree: true });
  window.addEventListener("pagehide", stopRecording);
  window.addEventListener("resize", fitPrompt);
  return { element: root, dispose };
}

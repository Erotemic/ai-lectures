export async function api(path, options = {}) {
  const response = await fetch(path, {
    cache: "no-store",
    ...options,
    headers: { "Content-Type": "application/json", ...options.headers },
  });
  const data = await response.json();
  if (!response.ok) {
    const error = new Error(
      data.error || `Request failed (${response.status})`,
    );
    error.status = response.status;
    error.data = data;
    throw error;
  }
  return data;
}
export const post = (path, data) =>
  api(path, { method: "POST", body: JSON.stringify(data) });
export const getStored = (key, fallback = null) => {
  try {
    return JSON.parse(localStorage.getItem("ailectures:" + key)) ?? fallback;
  } catch {
    return fallback;
  }
};
export const store = (key, value) => {
  try {
    localStorage.setItem("ailectures:" + key, JSON.stringify(value));
  } catch {}
};
export function randomId() {
  // randomUUID requires a secure context; household HTTP addresses need the
  // getRandomValues fallback for device, queue, and feedback identifiers.
  if (globalThis.crypto?.randomUUID) return globalThis.crypto.randomUUID();
  const bytes = new Uint8Array(16);
  if (globalThis.crypto?.getRandomValues)
    globalThis.crypto.getRandomValues(bytes);
  else
    for (let index = 0; index < bytes.length; index++)
      bytes[index] = Math.floor(Math.random() * 256);
  bytes[6] = (bytes[6] & 15) | 64;
  bytes[8] = (bytes[8] & 63) | 128;
  const hex = [...bytes]
    .map((byte) => byte.toString(16).padStart(2, "0"))
    .join("");
  return `${hex.slice(0, 8)}-${hex.slice(8, 12)}-${hex.slice(12, 16)}-${hex.slice(16, 20)}-${hex.slice(20)}`;
}
export function el(tag, attrs = {}, ...children) {
  const node = document.createElement(tag);
  for (const [key, value] of Object.entries(attrs)) {
    if (key.startsWith("on")) node.addEventListener(key.slice(2), value);
    else if (key === "class") node.className = value;
    else if (key === "text") node.textContent = value;
    else if (value !== null && value !== undefined && value !== false)
      node.setAttribute(key, value === true ? "" : value);
  }
  node.append(...children.filter((v) => v !== null && v !== undefined));
  return node;
}
export const lectureURL = (id) =>
  "/lectures/" + id.split(":").map(encodeURIComponent).join("/");
export const clock = (seconds) => {
  seconds = Math.max(0, Math.floor(seconds || 0));
  return `${Math.floor(seconds / 60)}:${String(seconds % 60).padStart(2, "0")}`;
};

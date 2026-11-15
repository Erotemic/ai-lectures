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

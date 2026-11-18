import { el } from "./api.mjs";

export function topicURL(tag) {
  return "/?" + new URLSearchParams({ tag });
}

export function topicLinks(tags, link, limit = Infinity) {
  if (!Array.isArray(tags) || !tags.length) return null;
  const visible = tags.slice(0, limit);
  return el("div", { class: "topic-tags", "aria-label": "Tags" },
    ...visible.map(tag => {
      const anchor = link(tag, topicURL(tag));
      anchor.classList.add("topic-tag");
      anchor.setAttribute("aria-label", "Find lectures tagged " + tag);
      return anchor;
    }));
}

import { el } from "./api.mjs";
const roles = { author: "Author", attributed_author: "Traditionally attributed to", compiler: "Compiler", translator: "Translator", storyteller: "Storyteller", oral_tradition: "Oral tradition", anonymous: "Anonymous or collective tradition" };
export function creatorLine(row, link) {
  if (!row.creators?.length) return null;
  return el("p", { class: "work-creators", "aria-label": "Creators of the work discussed" },
    ...row.creators.flatMap((credit, index) => [index ? "; " : "", `${roles[credit.role] || credit.role}: `,
      ["author", "attributed_author"].includes(credit.role)
        ? link(credit.name, "/?" + new URLSearchParams({ tag: "Author: " + credit.name }))
        : el("span", { text: credit.name, title: credit.note || null })]));
}

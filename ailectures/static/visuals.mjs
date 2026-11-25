import { el } from "./api.mjs";

export function visualFigure(visual, sizes = "(max-width: 520px) calc(100vw - 2rem), 30rem") {
  if (!visual) return null;
  const caption = visual.caption ? el("figcaption", { text: visual.caption }) : null;
  if (visual.mathml) {
    const equation = new DOMParser().parseFromString(visual.mathml, "application/xml").documentElement;
    if (equation.localName !== "math" || equation.namespaceURI !== "http://www.w3.org/1998/Math/MathML") return null;
    return el("figure", { class: "reading-visual reading-equation" }, document.importNode(equation, true), caption);
  }
  const image = el("img", {
    loading: "lazy",
    decoding: "async",
    alt: visual.alt,
    width: visual.width,
    height: visual.height,
  });
  const figure = el("figure", { class: "reading-visual" },
    el("a", { href: visual.original, target: "_blank", rel: "noopener", title: "Open full-size illustration" },
      el("picture", {},
        visual.srcset ? el("source", { type: "image/webp", srcset: visual.srcset, sizes }) : null,
        image,
      ),
    ),
    caption,
  );
  image.onerror = () => { figure.hidden = true; };
  image.src = visual.original;
  return figure;
}

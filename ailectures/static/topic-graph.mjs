import { el, lectureURL } from "./api.mjs";
import { topicGraph, graphNeighborhood } from "./topic-graph-model.mjs";

const svgEl = (tag, attrs = {}) => {
  const node = document.createElementNS("http://www.w3.org/2000/svg", tag);
  for (const [key, value] of Object.entries(attrs))
    node.setAttribute(key, String(value));
  return node;
};

export function renderTopicGraph(main, catalog) {
  const params = new URLSearchParams(location.search);
  const root = el("section", { class: "topic-explorer" });
  main.replaceChildren(root);
  const collection = el(
    "select",
    { "aria-label": "Graph collection" },
    el("option", { value: "", text: "All content" }),
    ...catalog.courses.map((row) =>
      el("option", { value: row.id, text: row.title }),
    ),
  );
  collection.value = params.get("collection") || "";
  const facet = el("select", { "aria-label": "Graph dimension" });
  const search = el("input", {
    type: "search",
    placeholder: "Find a topic, place, author, or lecture",
    "aria-label": "Search graph",
  });
  search.value = params.get("q") || "";
  const body = el("div", { class: "topic-graph-layout" }),
    results = el("section", { "aria-label": "Graph connections" });
  const canvas = el("section", {
    class: "topic-graph-panel",
    "aria-label": "Interactive content graph",
  });
  const graphStatus = el("p", { class: "muted", role: "status" });
  root.append(
    el("h1", { text: "Topic graph" }),
    el("p", {
      class: "intro",
      text: "Explore lectures through topics, places, authors, and time. Connections describe content associations, not prerequisites.",
    }),
    el(
      "div",
      { class: "filters" },
      el("label", {}, "Collection", collection),
      el("label", {}, "Dimension", facet),
      el("label", {}, "Search", search),
    ),
    graphStatus,
    body,
  );
  body.append(canvas, results);
  let graph,
    selected = params.get("node") || "",
    shown = 25;
  function save() {
    const values = new URLSearchParams();
    if (collection.value) values.set("collection", collection.value);
    if (facet.value !== "Topics") values.set("facet", facet.value);
    if (selected) values.set("node", selected);
    if (search.value) values.set("q", search.value);
    history.replaceState(
      history.state,
      "",
      "/topic-graph" + (values.size ? "?" + values : ""),
    );
  }
  function lectureHref(id) {
    const params = new URLSearchParams({
      return: location.pathname + location.search,
    });
    if (collection.value) params.set("course", collection.value);
    return lectureURL(id) + "?" + params;
  }
  function choose(id) {
    selected = id;
    shown = 25;
    search.value = "";
    save();
    draw();
  }
  function rebuild() {
    const course = catalog.courses.find((row) => row.id === collection.value);
    const ids = course ? new Set(course.lectures) : null;
    const rows = catalog.lectures.filter((row) => !ids || ids.has(row.id));
    const current = facet.value || params.get("facet") || "Topics";
    graph = topicGraph(rows, current);
    facet.replaceChildren(
      ...graph.facets.map((label) =>
        el("option", { value: label, text: label }),
      ),
    );
    facet.value = graph.facets.includes(current)
      ? current
      : graph.facets[0] || "Topics";
    if (facet.value !== current) graph = topicGraph(rows, facet.value);
    save();
    draw();
  }
  function draw() {
    const view = graphNeighborhood(graph, selected);
    if (!view.focus && !view.lecture) selected = "";
    const query = search.value.trim().toLocaleLowerCase();
    const matches = query
      ? [
          ...[...graph.nodes.values()]
            .filter((node) =>
              node.path.join(" ").toLocaleLowerCase().includes(query),
            )
            .map((node) => ({
              id: node.id,
              title: node.path.join(" › "),
              kind: "topic",
            })),
          ...[...graph.lectures.values()]
            .filter((row) =>
              `${row.title} ${row.description || ""}`
                .toLocaleLowerCase()
                .includes(query),
            )
            .map((row) => ({
              id: "lecture:" + row.id,
              title: row.title,
              kind: "lecture",
            })),
        ]
      : null;
    const heading = view.focus
      ? view.focus.path.join(" › ")
      : view.lecture?.title || facet.value;
    graphStatus.textContent = `${graph.lectures.size} lectures in this collection scope · ${graph.nodes.size} nodes in ${facet.value.toLowerCase()}. Graph shows up to 16 neighbors; the lists expose the remaining connections.`;
    const home = el("button", {
      type: "button",
      text: "All " + facet.value.toLowerCase(),
      onclick: () => choose(""),
    });
    const parent = view.focus?.parent
      ? el("button", {
          type: "button",
          text: "Broader topic",
          onclick: () => choose(view.focus.parent),
        })
      : null;
    results.replaceChildren(
      ...[el("h2", { text: heading }), home, parent].filter(Boolean),
    );
    if (view.lecture)
      results.append(
        el(
          "p",
          {},
          el("a", {
            href: lectureHref(view.lecture.id),
            "data-nav": "",
            text: "Open this lecture",
          }),
        ),
        el("p", { text: view.lecture.description || "" }),
      );
    if (matches) {
      results.append(
        el("h3", { text: `${matches.length} search matches` }),
        ...matches
          .slice(0, shown)
          .map((item) =>
            el("button", {
              class: "graph-result",
              type: "button",
              text: (item.kind === "lecture" ? "Lecture: " : "") + item.title,
              onclick: () => choose(item.id),
            }),
          ),
      );
      if (matches.length > shown)
        results.append(
          el("button", {
            type: "button",
            text: "Show more matches",
            onclick: () => {
              shown += 25;
              draw();
            },
          }),
        );
    } else {
      results.append(
        el("h3", {
          text: `${view.topics.length} topic connection${view.topics.length === 1 ? "" : "s"}`,
        }),
        ...view.topics
          .slice(0, shown)
          .map((node) =>
            el("button", {
              type: "button",
              class: "graph-result",
              text: `${node.title} · ${node.lectures.size} lecture${node.lectures.size === 1 ? "" : "s"}`,
              onclick: () => choose(node.id),
            }),
          ),
        el("h3", {
          text: `${view.lectures.length} ${view.lecture ? "related " : ""}lecture${view.lectures.length === 1 ? "" : "s"}`,
        }),
        ...view.lectures
          .slice(0, shown)
          .map((row) =>
            el(
              "div",
              { class: "graph-lecture" },
              el("a", {
                href: lectureHref(row.id),
                "data-nav": "",
                text: row.title,
              }),
              el("button", {
                type: "button",
                "aria-label": "Show connections for " + row.title,
                text: "Connections",
                onclick: () => choose("lecture:" + row.id),
              }),
            ),
          ),
      );
      if (view.topics.length > shown || view.lectures.length > shown)
        results.append(
          el("button", {
            type: "button",
            text: "Show more connections",
            onclick: () => {
              shown += 25;
              draw();
            },
          }),
        );
    }
    if (!graph.nodes.size)
      results.append(
        el("p", {
          text: "No tags in this dimension for the selected content.",
        }),
      );
    drawCanvas(view, heading);
  }
  function drawCanvas(view, heading) {
    const initialWidth = Math.max(280, canvas.clientWidth),
      initialHeight = initialWidth < 600 ? 420 : 570;
    const narrow = initialWidth < 600;
    let width = initialWidth,
      height = initialHeight,
      x = -width / 2,
      y = -height / 2,
      drag = null,
      moved = false;
    const svg = svgEl("svg", {
      viewBox: `${x} ${y} ${width} ${height}`,
      role: "group",
      "aria-label": "Content connections for " + heading,
      tabindex: "0",
    });
    const positions = new Map([[view.center.id, { x: 0, y: 0 }]]);
    for (const kind of ["topic", "lecture"]) {
      const neighbors = view.nodes
        .slice(1)
        .filter((node) => node.kind === kind);
      neighbors.forEach((node, index) =>
        positions.set(node.id, {
          x: (kind === "topic" ? -1 : 1) * initialWidth * 0.29,
          y:
            (index - (neighbors.length - 1) / 2) *
            Math.min(
              85,
              (initialHeight * 0.7) / Math.max(1, neighbors.length - 1),
            ),
        }),
      );
    }
    const lines = view.edges.map((edge) => {
      const line = svgEl("line", { class: "graph-edge " + edge.kind });
      svg.append(line);
      return { edge, line };
    });
    const elements = new Map();
    for (const node of view.nodes) {
      const group = svgEl("g", {
        class: "graph-node " + node.kind,
        tabindex: 0,
        role: "button",
        "aria-label": `${node.kind}: ${node.title}${node.lectures ? "; " + node.lectures.size + " lectures" : ""}`,
      });
      const title = svgEl("title");
      title.textContent = node.title;
      group.append(
        title,
        svgEl("circle", {
          r:
            node.id === view.center.id
              ? narrow
                ? 28
                : 34
              : node.kind === "topic"
                ? 16
                : 11,
        }),
      );
      const center = node.id === view.center.id;
      const labelX = center || narrow ? 0 : node.kind === "topic" ? -25 : 22;
      const label = svgEl("text", {
        x: labelX,
        y: center ? 52 : narrow ? 30 : 5,
        "text-anchor":
          center || narrow ? "middle" : node.kind === "topic" ? "end" : "start",
      });
      const words = node.title.split(/\s+/),
        lines = [""],
        characterLimit = narrow ? 14 : 18;
      for (const word of words) {
        if (lines.at(-1).length + word.length > characterLimit && lines.at(-1))
          lines.push("");
        lines[lines.length - 1] += (lines.at(-1) ? " " : "") + word;
      }
      lines.slice(0, 2).forEach((line, index) => {
        const span = svgEl("tspan", { x: labelX, dy: index ? 17 : 0 });
        span.textContent =
          line.slice(0, characterLimit) +
          (index === 1 && lines.length > 2 ? "…" : "");
        label.append(span);
      });
      group.append(label);
      group.onclick = () => {
        if (!moved)
          choose(
            node.id === view.center.id && node.kind === "lecture"
              ? selected
              : node.id,
          );
        moved = false;
      };
      group.onkeydown = (event) => {
        if (event.key === "Enter" || event.key === " ") {
          event.preventDefault();
          choose(node.id);
        }
      };
      group.onpointerdown = (event) => {
        event.stopPropagation();
        drag = { id: node.id, startX: event.clientX, startY: event.clientY };
        moved = false;
        group.setPointerCapture(event.pointerId);
      };
      svg.append(group);
      elements.set(node.id, group);
    }
    function update() {
      svg.setAttribute("viewBox", `${x} ${y} ${width} ${height}`);
      for (const [id, group] of elements) {
        const p = positions.get(id);
        group.setAttribute("transform", `translate(${p.x},${p.y})`);
      }
      for (const { edge, line } of lines) {
        const a = positions.get(edge.from),
          b = positions.get(edge.to);
        if (a && b)
          for (const [key, value] of Object.entries({
            x1: a.x,
            y1: a.y,
            x2: b.x,
            y2: b.y,
          }))
            line.setAttribute(key, value);
      }
    }
    function zoom(factor) {
      const cx = x + width / 2,
        cy = y + height / 2;
      width = Math.max(160, Math.min(5000, width * factor));
      height = (width * initialHeight) / initialWidth;
      x = cx - width / 2;
      y = cy - height / 2;
      update();
    }
    svg.onwheel = (event) => {
      event.preventDefault();
      zoom(event.deltaY > 0 ? 1.15 : 1 / 1.15);
    };
    svg.onpointerdown = (event) => {
      drag = { startX: event.clientX, startY: event.clientY };
      svg.setPointerCapture(event.pointerId);
      moved = false;
    };
    svg.onpointermove = (event) => {
      if (!drag) return;
      const bounds = svg.getBoundingClientRect();
      const dx = ((event.clientX - drag.startX) * width) / bounds.width,
        dy = ((event.clientY - drag.startY) * height) / bounds.height;
      if (
        Math.abs(event.clientX - drag.startX) +
          Math.abs(event.clientY - drag.startY) >
        3
      )
        moved = true;
      if (drag.id) {
        const p = positions.get(drag.id);
        p.x += dx;
        p.y += dy;
      } else {
        x -= dx;
        y -= dy;
      }
      drag.startX = event.clientX;
      drag.startY = event.clientY;
      update();
    };
    svg.onpointerup = () => {
      drag = null;
    };
    svg.onpointercancel = () => {
      drag = null;
    };
    svg.onkeydown = (event) => {
      if (event.target !== svg) return;
      if (event.key === "+" || event.key === "=") zoom(1 / 1.2);
      else if (event.key === "-") zoom(1.2);
    };
    canvas.replaceChildren(
      el(
        "div",
        { class: "actions" },
        el("button", {
          type: "button",
          text: "Zoom in",
          onclick: () => zoom(1 / 1.2),
        }),
        el("button", {
          type: "button",
          text: "Zoom out",
          onclick: () => zoom(1.2),
        }),
        el("button", {
          type: "button",
          text: "Reset view",
          onclick: () => {
            width = initialWidth;
            height = initialHeight;
            x = -width / 2;
            y = -height / 2;
            update();
          },
        }),
      ),
      svg,
      el("p", {
        class: "muted",
        text: "Teal: topics. Ochre: lectures. The central node is the selected item. Solid lines: hierarchy; dotted lines: content associations. Click a node to explore. Drag nodes to rearrange; drag the background to pan. Use the lists to open lectures.",
      }),
    );
    update();
  }
  collection.onchange = () => {
    selected = "";
    shown = 25;
    rebuild();
  };
  facet.onchange = () => {
    selected = "";
    shown = 25;
    rebuild();
  };
  search.oninput = () => {
    shown = 25;
    save();
    draw();
  };
  rebuild();
}

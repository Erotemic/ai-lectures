import { el, lectureURL } from "./api.mjs";
import {
  topicGraph,
  graphNeighborhood,
  GraphExpansion,
} from "./topic-graph-model.mjs";

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
    explorer,
    positions = new Map(),
    camera = null,
    focusRequested = null,
    resizeObserver = null,
    lectureListOpen = null,
    selected = params.get("node") || "",
    shown = 25;
  function stateKey() {
    return (
      "ailectures:topic-graph:" +
      JSON.stringify([collection.value, facet.value])
    );
  }
  function save() {
    if (explorer)
      try {
        sessionStorage.setItem(
          stateKey(),
          JSON.stringify({
            expansion: explorer.snapshot(),
            selected,
            positions: [...positions],
            camera,
          }),
        );
      } catch {}
    const values = new URLSearchParams();
    if (collection.value) values.set("collection", collection.value);
    if (facet.value !== "Topics") values.set("facet", facet.value);
    if (selected) values.set("node", selected);
    if (search.value) values.set("q", search.value);
    const url = "/topic-graph" + (values.size ? "?" + values : "");
    if (location.pathname + location.search !== url)
      history.replaceState(history.state, "", url);
  }
  function lectureHref(id) {
    const params = new URLSearchParams({
      return: location.pathname + location.search,
    });
    if (collection.value) params.set("course", collection.value);
    return lectureURL(id) + "?" + params;
  }
  function choose(id, expand = true) {
    id = id || "root";
    explorer.reveal(id);
    if (expand) explorer.expand(id);
    focusRequested = id;
    selected = id === "root" ? "" : id;
    shown = 25;
    lectureListOpen = null;
    search.value = "";
    save();
    draw();
  }
  function collapse(id) {
    id ||= "root";
    explorer.collapse(id);
    const visible = new Set(explorer.view().nodes.map((node) => node.id));
    if (!visible.has(selected || "root"))
      selected = visible.has(id) && id !== "root" ? id : "";
    lectureListOpen = null;
    draw();
    save();
  }
  function rebuild() {
    lectureListOpen = null;
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
    explorer = new GraphExpansion(graph);
    positions = new Map();
    camera = null;
    let restored = false;
    try {
      const stored = JSON.parse(sessionStorage.getItem(stateKey()));
      if (stored) {
        explorer.restore(stored.expansion);
        restored = true;
        selected ||= stored.selected || "";
        positions = new Map(
          (stored.positions || []).filter(
            ([id, p]) =>
              explorer.node(id) &&
              Number.isFinite(p?.x) &&
              Number.isFinite(p?.y),
          ),
        );
        if (
          stored.camera &&
          ["x", "y", "width", "height"].every((key) =>
            Number.isFinite(stored.camera[key]),
          ) &&
          stored.camera.width > 0 &&
          stored.camera.height > 0
        )
          camera = stored.camera;
      }
    } catch {}
    if (selected && explorer.node(selected)) {
      explorer.reveal(selected);
      if (!restored) {
        explorer.expand(selected);
        focusRequested = selected;
      }
    }
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
    graphStatus.textContent = `${graph.lectures.size} lectures in this collection scope · ${graph.nodes.size} nodes in ${facet.value.toLowerCase()}. Expand branches to keep exploring, in batches of ${explorer.batch} connections.`;
    const home = el("button", {
      type: "button",
      text: "All " + facet.value.toLowerCase(),
      onclick: () => choose("", false),
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
    const current = selected || "root",
      remaining = explorer.remaining(current);
    results.append(
      el(
        "div",
        { class: "actions graph-expansion-actions" },
        remaining.topics
          ? el("button", {
              type: "button",
              text: `Add next ${Math.min(explorer.batch, remaining.topics)} topics (${remaining.topics} remaining)`,
              onclick: () => {
                explorer.expand(current, "topics");
                focusRequested = current;
                draw();
                save();
              },
            })
          : null,
        remaining.lectures
          ? el("button", {
              type: "button",
              text: `${explorer.children(current).size ? "Add" : "Show"} ${Math.min(explorer.batch, remaining.lectures)} lectures (${remaining.lectures} remaining)`,
              onclick: () => {
                explorer.expand(current, "lectures");
                focusRequested = current;
                draw();
                save();
              },
            })
          : null,
        explorer.children(current).size
          ? el("button", {
              type: "button",
              text: "Collapse branch",
              onclick: () => collapse(current),
            })
          : null,
      ),
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
        ...matches.slice(0, shown).map((item) =>
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
        ...view.topics.slice(0, shown).map((node) =>
          el("button", {
            type: "button",
            class: "graph-result",
            text: `${node.title} · ${node.lectures.size} lecture${node.lectures.size === 1 ? "" : "s"}`,
            onclick: () => choose(node.id),
          }),
        ),
      );
      if (view.topics.length > shown)
        results.append(
          el("button", {
            type: "button",
            text: "Show more topics",
            onclick: () => {
              shown += 25;
              draw();
            },
          }),
        );
      const lectureList = el(
        "details",
        {
          class: "graph-lecture-list",
          open: lectureListOpen ?? Boolean(view.lecture || !view.topics.length),
        },
        el("summary", {
          text: `${view.lectures.length} ${view.lecture ? "related " : ""}lecture${view.lectures.length === 1 ? "" : "s"}`,
        }),
        ...view.lectures.slice(0, shown).map((row) =>
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
        view.lectures.length > shown
          ? el("button", {
              type: "button",
              text: "Show more lectures",
              onclick: () => {
                shown += 25;
                draw();
              },
            })
          : null,
      );
      lectureList.ontoggle = () => {
        if (lectureList.isConnected) lectureListOpen = lectureList.open;
      };
      results.append(lectureList);
    }
    if (!graph.nodes.size)
      results.append(
        el("p", {
          text: "No tags in this dimension for the selected content.",
        }),
      );
    drawCanvas(explorer.view());
  }
  function drawCanvas(view) {
    resizeObserver?.disconnect();
    let initialWidth = Math.max(280, canvas.clientWidth),
      initialHeight = initialWidth < 600 ? 420 : 570;
    const adjacency = new Map();
    for (const edge of view.edges)
      for (const [a, b] of [
        [edge.from, edge.to],
        [edge.to, edge.from],
      ]) {
        if (!adjacency.has(a)) adjacency.set(a, []);
        adjacency.get(a).push(b);
      }
    const occupied = new Set(
      view.nodes
        .filter((node) => positions.has(node.id))
        .map((node) => {
          const p = positions.get(node.id);
          return Math.round(p.x / 280) + ":" + Math.round(p.y / 105);
        }),
    );
    for (const node of view.nodes) {
      if (positions.has(node.id)) continue;
      if (node.id === "root") {
        positions.set(node.id, { x: 0, y: 0 });
        occupied.add("0:0");
        continue;
      }
      const parent =
        (adjacency.get(node.id) || []).find((id) => positions.has(id)) ||
        "root";
      const point = positions.get(parent),
        column = Math.round(point.x / 280) + 1;
      let row = Math.round(point.y / 105),
        offset = 0;
      while (occupied.has(column + ":" + row)) {
        offset++;
        row =
          Math.round(point.y / 105) +
          (offset % 2 ? -Math.ceil(offset / 2) : offset / 2);
      }
      occupied.add(column + ":" + row);
      positions.set(node.id, { x: column * 280, y: row * 105 });
    }
    function frame(ids) {
      const points = ids.map((id) => positions.get(id)).filter(Boolean);
      if (!points.length) return;
      let left = Infinity,
        right = -Infinity,
        top = Infinity,
        bottom = -Infinity;
      for (const p of points) {
        left = Math.min(left, p.x - 120);
        right = Math.max(right, p.x + 120);
        top = Math.min(top, p.y - 65);
        bottom = Math.max(bottom, p.y + 80);
      }
      const width = Math.max(
          400,
          right - left,
          ((bottom - top) * initialWidth) / initialHeight,
        ),
        height = (width * initialHeight) / initialWidth;
      camera = {
        x: (left + right - width) / 2,
        y: (top + bottom - height) / 2,
        width,
        height,
      };
    }
    if (!camera) frame(view.nodes.map((node) => node.id));
    else camera.height = (camera.width * initialHeight) / initialWidth;
    if (focusRequested && positions.has(focusRequested)) {
      const ids = [focusRequested, ...explorer.children(focusRequested)];
      const points = ids.map((id) => positions.get(id)).filter(Boolean);
      if (
        points.some(
          (p) =>
            p.x < camera.x + 80 ||
            p.x > camera.x + camera.width - 80 ||
            p.y < camera.y + 50 ||
            p.y > camera.y + camera.height - 70,
        )
      ) {
        const anchor = positions.get(focusRequested);
        const child = points[1] || anchor;
        camera.x = (anchor.x + child.x) / 2 - camera.width / 2;
        camera.y = anchor.y - camera.height / 2;
      }
      focusRequested = null;
    }
    const svg = svgEl("svg", {
      role: "group",
      "aria-label": "Expandable content graph",
      tabindex: 0,
    });
    const edgeLayer = svgEl("g"),
      nodeLayer = svgEl("g");
    svg.append(edgeLayer, nodeLayer);
    const nodeElements = new Map(),
      edgeElements = new Map();
    const remaining = new Map(
      view.nodes.map((node) => [node.id, explorer.remaining(node.id)]),
    );
    const visibleStatus = el("p", { class: "muted" });
    let drag = null,
      moved = false,
      pendingFrame = false;
    const selectedId = selected || "root";
    function makeNode(node) {
      const group = svgEl("g", {
        class:
          "graph-node " +
          node.kind +
          (node.id === selectedId ? " selected" : ""),
        tabindex: 0,
        role: "button",
        "data-node-id": node.id,
      });
      const count = remaining.get(node.id),
        description = count.topics
          ? count.topics + " more topics"
          : count.lectures
            ? count.lectures + " lectures to reveal"
            : "all connections revealed";
      group.setAttribute(
        "aria-label",
        `${node.kind}: ${node.title}; ${description}. Activate to expand.`,
      );
      const title = svgEl("title");
      title.textContent = node.title + " — " + description;
      const circle = svgEl("circle", {
        r: node.id === selectedId ? 25 : node.kind === "lecture" ? 12 : 18,
      });
      group.append(title, circle);
      if (count.topics || count.lectures) {
        const badge = svgEl("text", {
          class: "graph-expand-badge",
          "text-anchor": "middle",
          y: 5,
        });
        badge.textContent = "+";
        group.append(badge);
      }
      const label = svgEl("text", {
        class: "graph-label",
        x: 0,
        y: node.id === selectedId ? 43 : 35,
        "text-anchor": "middle",
      });
      const words = node.title.split(/\s+/),
        lines = [""];
      for (const word of words) {
        if (lines.at(-1).length + word.length > 27 && lines.at(-1))
          lines.push("");
        lines[lines.length - 1] += (lines.at(-1) ? " " : "") + word;
      }
      lines.slice(0, 2).forEach((line, index) => {
        const span = svgEl("tspan", { x: 0, dy: index ? 17 : 0 });
        span.textContent =
          line.slice(0, 30) + (index === 1 && lines.length > 2 ? "…" : "");
        label.append(span);
      });
      group.append(label);
      group.onclick = (event) => {
        if (!moved) {
          if (event.shiftKey) collapse(node.id);
          else choose(node.id);
        }
        moved = false;
      };
      group.onkeydown = (event) => {
        if (event.key === "Enter" || event.key === " ") {
          event.preventDefault();
          if (event.shiftKey) collapse(node.id);
          else choose(node.id);
        }
      };
      group.onpointerdown = (event) => {
        event.stopPropagation();
        drag = {
          id: node.id,
          x: event.clientX,
          y: event.clientY,
          originX: event.clientX,
          originY: event.clientY,
        };
        moved = false;
        group.setPointerCapture(event.pointerId);
      };
      return group;
    }
    function update() {
      pendingFrame = false;
      if (!svg.isConnected) return;
      svg.setAttribute(
        "viewBox",
        `${camera.x} ${camera.y} ${camera.width} ${camera.height}`,
      );
      const scale = initialWidth / camera.width,
        visible = new Set();
      for (const node of view.nodes) {
        const p = positions.get(node.id);
        const detailed =
          node.id === selectedId ||
          node.kind === "root" ||
          ((node.kind !== "lecture" || scale >= 0.55) &&
            (!node.path ||
              node.path.length <=
                (scale < 0.3 ? 1 : scale < 0.55 ? 2 : Infinity)));
        const onScreen =
          p.x > camera.x - 140 &&
          p.x < camera.x + camera.width + 140 &&
          p.y > camera.y - 80 &&
          p.y < camera.y + camera.height + 80;
        if (!(detailed && onScreen) && node.id !== drag?.id) continue;
        visible.add(node.id);
        let group = nodeElements.get(node.id);
        if (!group) {
          group = makeNode(node);
          nodeElements.set(node.id, group);
          nodeLayer.append(group);
        }
        group.setAttribute("transform", `translate(${p.x},${p.y})`);
        group.querySelector(".graph-label").style.display =
          scale >= 0.7 ||
          view.nodes.length <= 30 ||
          (node.path?.length === 1 && scale >= 0.3) ||
          node.id === selectedId ||
          node.kind === "root"
            ? ""
            : "none";
        group.querySelector(".graph-label").style.fontSize =
          Math.max(14, 11 / scale) + "px";
      }
      for (const [id, group] of nodeElements)
        if (!visible.has(id)) {
          group.remove();
          nodeElements.delete(id);
        }
      const lines = new Set();
      for (const edge of view.edges) {
        if (!visible.has(edge.from) || !visible.has(edge.to)) continue;
        const key = JSON.stringify([edge.from, edge.to]);
        lines.add(key);
        let line = edgeElements.get(key);
        if (!line) {
          line = svgEl("line", { class: "graph-edge " + edge.kind });
          edgeElements.set(key, line);
          edgeLayer.append(line);
        }
        const a = positions.get(edge.from),
          b = positions.get(edge.to);
        for (const [name, value] of Object.entries({
          x1: a.x,
          y1: a.y,
          x2: b.x,
          y2: b.y,
        }))
          line.setAttribute(name, value);
      }
      for (const [key, line] of edgeElements)
        if (!lines.has(key)) {
          line.remove();
          edgeElements.delete(key);
        }
      visibleStatus.textContent = `${view.nodes.length} nodes explored · ${visible.size} drawn in this view${scale < 0.7 ? " · zoom in for finer topics, lectures, and labels" : ""}`;
    }
    function schedule() {
      if (!pendingFrame) {
        pendingFrame = true;
        requestAnimationFrame(update);
      }
    }
    function zoom(factor, point = null) {
      const width = Math.max(160, Math.min(1e7, camera.width * factor)),
        ratio = width / camera.width;
      const cx = point?.x ?? camera.x + camera.width / 2,
        cy = point?.y ?? camera.y + camera.height / 2;
      camera = {
        x: cx + (camera.x - cx) * ratio,
        y: cy + (camera.y - cy) * ratio,
        width,
        height: (width * initialHeight) / initialWidth,
      };
      schedule();
      save();
    }
    svg.onwheel = (event) => {
      event.preventDefault();
      const bounds = svg.getBoundingClientRect();
      zoom(event.deltaY > 0 ? 1.15 : 1 / 1.15, {
        x:
          camera.x +
          ((event.clientX - bounds.left) * camera.width) / bounds.width,
        y:
          camera.y +
          ((event.clientY - bounds.top) * camera.height) / bounds.height,
      });
    };
    svg.onpointerdown = (event) => {
      drag = {
        x: event.clientX,
        y: event.clientY,
        originX: event.clientX,
        originY: event.clientY,
      };
      moved = false;
      svg.setPointerCapture(event.pointerId);
    };
    svg.onpointermove = (event) => {
      if (!drag) return;
      const bounds = svg.getBoundingClientRect(),
        dx = ((event.clientX - drag.x) * camera.width) / bounds.width,
        dy = ((event.clientY - drag.y) * camera.height) / bounds.height;
      moved ||=
        Math.abs(event.clientX - drag.originX) +
          Math.abs(event.clientY - drag.originY) >
        3;
      if (drag.id) {
        const p = positions.get(drag.id);
        p.x += dx;
        p.y += dy;
      } else {
        camera.x -= dx;
        camera.y -= dy;
      }
      drag.x = event.clientX;
      drag.y = event.clientY;
      schedule();
    };
    svg.onpointerup = svg.onpointercancel = () => {
      drag = null;
      save();
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
          text: "Fit graph",
          onclick: () => {
            frame(view.nodes.map((node) => node.id));
            update();
            save();
          },
        }),
        el("button", {
          type: "button",
          text: "Focus selected",
          onclick: () => {
            frame([selectedId, ...(adjacency.get(selectedId) || [])]);
            update();
            save();
          },
        }),
        el("button", {
          type: "button",
          text: "Reset graph",
          onclick: () => {
            explorer = new GraphExpansion(graph);
            positions.clear();
            camera = null;
            selected = "";
            draw();
            save();
          },
        }),
      ),
      svg,
      visibleStatus,
      el("p", {
        class: "muted",
        text: "Click a node to add its next connections. Topics expand from broad to specific; lectures appear in batches. Shift-click a node to collapse its branch. Drag nodes to arrange, or the background to pan. Zooming out hides finer detail without forgetting it.",
      }),
    );
    update();
    save();
    const observer = new ResizeObserver(() => {
      if (!svg.isConnected) {
        observer.disconnect();
        return;
      }
      const nextWidth = Math.max(280, canvas.clientWidth),
        nextHeight = nextWidth < 600 ? 420 : 570;
      if (
        Math.abs(nextWidth - initialWidth) < 1 &&
        nextHeight === initialHeight
      )
        return;
      const cx = camera.x + camera.width / 2,
        cy = camera.y + camera.height / 2;
      camera.width = Math.max(
        nextWidth < 600 ? 560 : 160,
        (camera.width * nextWidth) / initialWidth,
      );
      camera.height = (camera.width * nextHeight) / nextWidth;
      camera.x = cx - camera.width / 2;
      camera.y = cy - camera.height / 2;
      initialWidth = nextWidth;
      initialHeight = nextHeight;
      schedule();
      save();
    });
    observer.observe(canvas);
    resizeObserver = observer;
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

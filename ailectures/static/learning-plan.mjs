import { api, post, el, getStored, store, randomId } from "./api.mjs";
import { LearningState, planRequest, familiarityStatus } from "./learning-state.mjs";

const choices = [["unknown", "Need to learn"], ["uncertain", "Think I know · review"], ["known", "Confident I know"]];
const option = (value, text) => el("option", { value, text });
const strings = value => Array.isArray(value) ? value.filter(item => typeof item === "string") : typeof value === "string" ? [value] : [];
const hasLectures = collection => Array.isArray(collection?.lectures) && collection.lectures.length > 0;

export async function renderLearningPlan(main, context = {}) {
  const root = el("section", { class: "learning-planner" });
  main.replaceChildren(root);
  root.append(el("h1", { text: "Build a learning plan" }), el("p", { class: "intro", text: "Choose where to begin or what to reach, then mark familiar material. The plan orders recorded prerequisites and keeps uncertain knowledge for review." }));
  const status = el("p", { role: "status", "aria-live": "polite", class: "muted" });
  const action = (text, callback, attributes = {}) => el("button", { type: "button", text, ...attributes,
    onclick: () => Promise.resolve(callback()).catch(error => { status.textContent = error.message; }) });
  root.append(status);
  let data;
  const knowledge = new LearningState(context.profile || "");
  try { [data] = await Promise.all([api("/api/library/learning-map"), knowledge.load()]); }
  catch (error) { status.textContent = error.message; return; }
  if (!root.isConnected) return;
  const planCollections = data.collections.filter(hasLectures);
  const link = context.link || ((text, href) => el("a", { href, "data-nav": "", text }));
  const preferenceKey = "learning-plan:" + (context.profile || "device");
  const params = new URLSearchParams(location.search);
  const categories = [...new Set(Object.values(data.nodes).flatMap(node => node.categories || []))].sort();
  const settings = { mode: "goal", category: categories.includes("Mathematics") ? "Mathematics" : "", collection: "", goal: "", start: "",
    include_proof: false, include_soft: false, assume_uncertain: false, ...getStored(preferenceKey, {}) };
  if (params.has("goal")) { settings.goal = data.component_lectures[params.get("goal")] || params.get("goal"); settings.mode = "goal"; }
  if (params.has("collection")) { settings.collection = params.get("collection"); if (!params.has("goal")) settings.mode = "collection"; }
  if (params.has("mode") && ["goal", "collection", "ready"].includes(params.get("mode"))) settings.mode = params.get("mode");
  if (params.has("start")) settings.start = params.get("start");
  for (const key of ["include_proof", "include_soft", "assume_uncertain"]) if (params.has(key)) settings[key] = params.get(key) === "1";
  const initialNode = data.nodes[settings.goal];
  const initialCollection = data.collections.find(row => row.id === settings.collection);
  if (initialNode && settings.category && !initialNode.categories?.includes(settings.category)) settings.category = "";
  if (initialCollection && settings.category && !initialCollection.categories?.includes(settings.category)) settings.category = "";
  const mode = el("select", { id: "plan-mode", "aria-label": "Planning mode" }, option("goal", "Reach a lecture"), option("collection", "Follow a collection"), option("ready", "What can I study next?"));
  mode.value = settings.mode;
  const category = el("select", { "aria-label": "Planning subject" }, option("", "All subjects"), ...categories.map(value => option(value, value)));
  category.value = settings.category;
  const collection = el("select", { id: "plan-collection", "aria-label": "Planning collection" });
  const search = el("input", { type: "search", placeholder: "Search titles or lecture IDs", "aria-label": "Find a learning goal" });
  const goal = el("select", { id: "plan-goal", "aria-label": "Learning goal" });
  const start = el("select", { id: "plan-start", "aria-label": "Starting lecture" });
  const goalFields = el("div", { class: "plan-goal-fields" }, el("label", {}, "Find your destination", search), el("label", {}, "Lecture to reach", goal));
  const startFields = el("label", {}, "Start this collection at", start);
  const startHint = el("p", { class: "muted", text: "Starting later removes earlier lectures as destinations. Any recorded prerequisites you still need are added back before the starting point." });
  const proof = el("input", { type: "checkbox", "aria-label": "Include proof dependencies", checked: Boolean(settings.include_proof) });
  const soft = el("input", { type: "checkbox", "aria-label": "Enforce suggested background", checked: Boolean(settings.include_soft) });
  const assume = el("input", { type: "checkbox", "aria-label": "Assume uncertain knowledge", checked: Boolean(settings.assume_uncertain) });
  const build = el("button", { type: "submit", class: "primary", text: "Build learning order" });
  const form = el("form", { class: "card plan-controls" },
    el("div", { class: "filters" }, el("label", {}, "Plan", mode), el("label", {}, "Subject", category)),
    el("label", {}, "Collection or scope", collection), goalFields, startFields, startHint,
    el("details", {}, el("summary", { text: "Dependency and confidence options" }),
      el("label", { class: "check" }, proof, "Also include dependencies used in proofs"),
      el("label", { class: "check" }, soft, "Also enforce suggested background links"),
      el("p", { class: "muted", text: "Proof use and suggested background are separate from required teaching preparation. Enforcing suggested links can expose cycles; it does not change the authored requirements." }),
      el("label", { class: "check" }, assume, "Assume material I only think I know"),
      el("p", { class: "muted", text: "By default uncertain material stays as review. If you skip it, those assumptions remain listed with the result." })),
    build);
  const backgroundSummary = el("summary", { text: "What do you already know?" });
  const background = el("details", { class: "section plan-background" }, backgroundSummary,
    el("p", { class: "muted", text: context.profile ? "These choices are shared with this named listener’s other devices and travel with listener history. Heard or completed lectures are not automatically marked known." : "These choices stay on this device. Choose a named listener from the menu to share future choices across devices. Heard or completed lectures are not automatically marked known." }));
  const backgroundSearch = el("input", { type: "search", placeholder: "For example: linear maps, completeness, or a lecture ID", "aria-label": "Find background material" });
  const bulkCourse = el("select", { "aria-label": "Background collection" }, option("", "Choose a collection to assess"),
    ...planCollections.map(row => option(row.id, row.title)));
  const bulkStatus = el("select", { "aria-label": "Collection familiarity" }, ...choices.map(([id, text]) => option(id, text)));
  bulkStatus.value = "uncertain";
  const knowledgeList = el("div", { class: "plan-knowledge-list" });
  const savedStatus = el("p", { class: "muted", role: "status" });
  const assessCollection = action("Apply to this collection", async () => {
    const selected = data.collections.find(row => row.id === bulkCourse.value);
    if (!hasLectures(selected)) { savedStatus.textContent = "Choose a background lecture route first."; return; }
    assessCollection.disabled = true;
    savedStatus.textContent = `Saving ${selected.lectures.length} familiarity choices…`;
    try { await updateKnowledge(selected.lectures, bulkStatus.value); }
    finally { assessCollection.disabled = false; }
  });
  background.append(el("div", { class: "filters" }, el("label", {}, "Assess a collection", bulkCourse), el("label", {}, "Familiarity", bulkStatus)), assessCollection,
    el("label", { class: "section" }, "Or assess individual material", backgroundSearch), savedStatus, knowledgeList,
    action("Refresh saved background", async () => { invalidate(); await knowledge.load(); drawKnowledge(); if (hasPlan) await compute(); }));
  if (context.profile && Object.keys(getStored("knowledge:device", {})).length) background.append(action("Copy device background where this listener has no choice", async () => {
    invalidate();
    await knowledge.load();
    const entries = Object.entries(getStored("knowledge:device", {})).filter(([id]) => !knowledge.records[id])
      .map(([id, row]) => ({ id, status: row.status, revision: row.revision || null }));
    await knowledge.setMany(entries);
    savedStatus.textContent = `Copied ${entries.length} background choices; existing listener choices were retained.`;
    drawKnowledge(); if (hasPlan) await compute();
  }));
  const result = el("section", { class: "section plan-result", "aria-label": "Learning order" });
  root.append(form, background, result);
  let hasPlan = false, computation = 0, timer;
  const collectionTitles = new Map(data.collections.map(row => [row.id, row.title]));
  const normalize = value => String(value).toLocaleLowerCase().replace(/[-_]/g, " ").replace(/\s+/g, " ").trim();
  const searchText = node => normalize([node.title, node.id, node.section,
    ...strings(node.tags), ...strings(node.background), ...strings(node.readiness_checks),
    ...(node.collections || []).map(id => collectionTitles.get(id) || id)].join(" "));
  function invalidate() {
    computation++;
    build.disabled = false;
    for (const button of result.querySelectorAll("[data-plan-action]")) button.disabled = true;
  }
  function courseRows() { return planCollections.filter(row => !category.value || row.categories?.includes(category.value)); }
  function nodeRows() {
    const selected = planCollections.find(row => row.id === collection.value);
    const ids = selected ? new Set(selected.lectures) : null;
    return Object.values(data.nodes).filter(node => node.kind === "lecture" && (ids ? ids.has(node.id) : !category.value || node.categories?.includes(category.value)));
  }
  function populate() {
    const current = settings.collection;
    collection.replaceChildren(option("", "All collections in this subject"), ...courseRows().map(row => option(row.id, row.title)));
    if (current && !courseRows().some(row => row.id === current)) {
      const selected = data.collections.find(row => row.id === current);
      const retained = option(current, selected && !hasLectures(selected)
        ? selected.title + " · choose a route" : current + " · not in this subject");
      retained.disabled = Boolean(selected && !hasLectures(selected));
      collection.append(retained);
    }
    collection.value = current;
    const query = normalize(search.value);
    const rows = nodeRows().filter(node => searchText(node).includes(query));
    goal.replaceChildren(option("", "Choose a lecture"), ...rows.map(node => option(node.id, node.title + " · " + node.id + (node.available ? "" : " · not installed"))));
    if (settings.goal && !rows.some(row => row.id === settings.goal)) goal.append(option(settings.goal, (data.nodes[settings.goal]?.title || settings.goal) + " · selected destination"));
    goal.value = settings.goal;
    const selected = data.collections.find(row => row.id === current);
    start.replaceChildren(option("", "Beginning of the collection"), ...(selected?.lectures || []).map(id => option(id, data.nodes[id]?.title || id)));
    start.value = settings.start;
    goalFields.hidden = mode.value !== "goal";
    startFields.hidden = startHint.hidden = mode.value !== "collection";
    build.textContent = mode.value === "ready" ? "Find available next steps" : "Build learning order";
  }
  function saveSettings() {
    Object.assign(settings, { mode: mode.value, category: category.value, collection: collection.value, goal: goal.value, start: start.value,
      include_proof: proof.checked, include_soft: soft.checked, assume_uncertain: assume.checked });
    store(preferenceKey, settings);
    const url = new URLSearchParams();
    if (settings.mode !== "goal") url.set("mode", settings.mode);
    if (settings.mode === "goal" && settings.goal) url.set("goal", settings.goal);
    if (settings.collection) url.set("collection", settings.collection);
    if (settings.mode === "collection" && settings.start) url.set("start", settings.start);
    for (const key of ["include_proof", "include_soft", "assume_uncertain"]) if (settings[key]) url.set(key, "1");
    history.replaceState(history.state, "", "/learning-plan" + (url.size ? "?" + url : ""));
  }
  function familiarity(id) {
    const select = el("select", { "aria-label": "Familiarity: " + (data.nodes[id]?.title || id) }, ...choices.map(([value, text]) => option(value, text)));
    select.value = familiarityStatus(knowledge.records[id], data.nodes[id]);
    select.onchange = () => updateKnowledge([id], select.value).catch(error => { savedStatus.textContent = error.message; });
    return select;
  }
  function backgroundDetails(node) {
    const notes = el("details", {}, el("summary", { text: "Check readiness & see why" }));
    if (!node.prerequisites_reviewed) notes.append(el("p", { class: "muted", text: "This lecture’s prerequisite coverage has not yet been reviewed in full. No recorded requirement does not mean no background is needed." }));
    if (node.background?.length) notes.append(el("p", { text: "Assumed background: " + strings(node.background).join("; ") }));
    if (node.readiness_checks?.length) notes.append(el("p", { text: "Could you do the following without following the lecture’s answer?" }),
      el("ul", {}, ...node.readiness_checks.map(text => el("li", { text }))));
    if (node.reasons?.length) notes.append(el("ul", {}, ...node.reasons.map(text => el("li", { text }))));
    if (node.depends_on?.length) notes.append(el("p", {}, "Recorded preparation: ", ...node.depends_on.flatMap((id, index) => {
      const prerequisite = data.nodes[id];
      const name = prerequisite?.title || id;
      return [index ? "; " : "", prerequisite?.available && prerequisite.url ? link(name, prerequisite.url) : name];
    })));
    notes.append(link("Inspect the original connections", "/learning-map?" + new URLSearchParams({ lecture: node.id })));
    return notes;
  }
  function material(node, role = "") {
    const saved = knowledge.records[node.id];
    const title = node.available && node.url ? link(node.title, node.url) : el("strong", { text: node.title || node.id });
    return el("article", { class: "card plan-step", "data-lecture": node.id },
      el("div", { class: "plan-step-heading" }, el("div", {}, el("small", { class: "eyebrow", text: role || (node.prerequisites_reviewed ? "Reviewed preparation" : "Background mapping incomplete") }), el("h3", {}, title), el("small", { text: node.id + (node.estimated_minutes ? ` · about ${node.estimated_minutes} min` : "") })),
        el("label", {}, "Familiarity", familiarity(node.id))),
      saved?.status === "known" && familiarityStatus(saved, data.nodes[node.id]) === "uncertain" ? el("p", { class: "muted", text: "The lecture content has changed or expanded since you assessed it. Familiarity is treated as uncertain until you reconfirm it for the current material." }) : null,
      backgroundDetails(node));
  }
  function drawKnowledge() {
    const assessed = Object.values(knowledge.records).filter(record => ["known", "uncertain"].includes(record.status)).length;
    backgroundSummary.textContent = `What do you already know? · ${assessed} assessed ${assessed === 1 ? "entry" : "entries"}`;
    const query = normalize(backgroundSearch.value);
    const orphaned = Object.keys(knowledge.records).filter(id => !data.nodes[id]).map(id => ({ id, title: id + " · no longer mapped", kind: "lecture", available: false }));
    const rows = [...Object.values(data.nodes), ...orphaned].filter(node => node.kind === "lecture" &&
      (query ? searchText(node).includes(query) : knowledge.records[node.id]?.status && knowledge.records[node.id].status !== "unknown"));
    knowledgeList.replaceChildren(...rows.slice(0, 12).map(node => material(node)));
    if (rows.length > 12) knowledgeList.append(el("p", { class: "muted", text: `${rows.length} matches. Narrow the search to assess other entries.` }));
    if (!rows.length) knowledgeList.append(el("p", { class: "muted", text: query ? "No matching material in this library." : "Search for a concept or assess a collection. Nothing is assumed known yet." }));
    if (knowledge.error) savedStatus.textContent = "Choices are saved on this device; shared-state sync will retry. " + knowledge.error;
  }
  async function updateKnowledge(ids, value) {
    invalidate();
    await knowledge.setMany(ids.map(id => ({ id, status: value, revision: data.nodes[id]?.knowledge_revision || data.nodes[id]?.revision || null })));
    if (!root.isConnected) return;
    savedStatus.textContent = knowledge.error ? "Saved on this device; sharing is pending. " + knowledge.error : "Background choices saved.";
    drawKnowledge();
    if (hasPlan) await compute();
  }
  async function compute() {
    if (!root.isConnected) return;
    clearTimeout(timer);
    invalidate();
    const token = computation;
    saveSettings();
    if (context.profile) {
      await knowledge.load();
      if (token !== computation || !root.isConnected) return;
      drawKnowledge();
    }
    const request = planRequest(data, settings, knowledge.records);
    const selectedCollection = data.collections.find(row => row.id === settings.collection);
    if (settings.collection && !hasLectures(selectedCollection)) {
      result.replaceChildren();
      if (selectedCollection) {
        status.textContent = "Choose a lecture route within this guide before building a study plan.";
        result.append(el("p", { class: "notice", text: "This guide links to several routes. Choose one of those routes or another collection to plan its lectures." }),
          link("Choose a route in " + selectedCollection.title,
            selectedCollection.url || "/collections/" + encodeURIComponent(selectedCollection.id)));
      } else status.textContent = "This collection is unavailable. Choose an installed lecture route.";
      return;
    }
    if (settings.mode === "goal" && !settings.goal) { result.replaceChildren(); status.textContent = "Choose a lecture to reach."; return; }
    if (settings.mode === "collection" && !settings.collection) { result.replaceChildren(); status.textContent = "Choose a collection to follow."; return; }
    hasPlan = true; build.disabled = true; status.textContent = "Checking recorded prerequisites…";
    try {
      const plan = await post("/api/library/learning-plan", { ...request, generation: data.generation });
      if (token !== computation || !root.isConnected) return;
      status.textContent = plan.valid ? "Order checked against recorded prerequisites." : "A complete order is blocked by missing material or dependency cycles. Available preparation is shown below.";
      drawPlan(plan);
    } catch (error) {
      if (token === computation && root.isConnected) {
        if (error.status === 409) { await renderLearningPlan(main, context); return; }
        status.textContent = error.message;
      }
    }
    finally { if (token === computation) build.disabled = false; }
  }
  function nodeList(ids) { return el("ul", {}, ...ids.map(id => el("li", {}, data.nodes[id]?.available && data.nodes[id]?.url ? link(data.nodes[id].title, data.nodes[id].url) : id))); }
  function drawPlan(plan) {
    const readyMode = settings.mode === "ready";
    const steps = readyMode ? plan.ready.map(id => ({ ...data.nodes[id], role: familiarityStatus(knowledge.records[id], data.nodes[id]) === "uncertain" ? "review" : "available next" })) : plan.steps;
    const relevant = new Set(steps.map(row => row.id));
    const unmapped = plan.unmapped.filter(id => relevant.has(id));
    result.replaceChildren(el("h2", { text: readyMode ? "Available next according to recorded prerequisites" : plan.valid ? "Your learning order" : "A complete order needs attention" }),
      el("p", { class: "muted", text: `${steps.length} ${readyMode ? "candidates" : "steps"} · ${Math.round(steps.reduce((total, row) => total + (row.estimated_minutes || 0), 0))} estimated minutes` }));
    if (unmapped.length && !readyMode) result.append(el("div", { class: "notice" }, `${unmapped.length} of these entries have incompletely reviewed prerequisite coverage. This plan cannot certify all the background they need.`,
      el("details", {}, el("summary", { text: "Show entries with coverage gaps" }), nodeList(unmapped))));
    if (plan.missing.length) result.append(el("section", { class: "notice error" }, el("h3", { text: "Required material is not installed" }),
      el("p", { text: "You can install it or explicitly record that you know it from elsewhere. Dependent steps remain blocked until then." }),
      ...plan.missing.map(id => material(data.nodes[id] || { id, title: id, available: false }, "Missing required material"))));
    if (plan.cycles.length) result.append(el("section", { class: "notice error" }, el("h3", { text: "Dependency cycles prevent a linear order" }),
      el("p", { text: "These recorded links require editorial review or a joint study unit. No dependency has been silently dropped. If suggested links are enabled, try keeping them as recommendations." }),
      ...plan.cycles.map(ids => nodeList(ids))));
    if (plan.blocked.length) result.append(el("details", {}, el("summary", { text: `${plan.blocked.length} blocked steps` }), nodeList(plan.blocked)));
    const assumptions = plan.assumptions || [];
    result.append(el("details", { class: "plan-assumptions" }, el("summary", { text: `${assumptions.length} familiarity assumptions · ${plan.assumed_uncertain.length} uncertain assumptions` }),
      el("p", { class: "muted", text: "A familiar lecture is treated as knowledge you bring from elsewhere. Its own preparation is not rechecked. Change a familiarity choice to put it back in the plan." }),
      ...assumptions.map(record => material(data.nodes[record.id], record.basis === "assumed_uncertain" ? "Uncertain knowledge skipped by choice" : "Assumed known"))));
    if (plan.unknown_knowledge.length) result.append(el("div", { class: "notice" }, "Some saved knowledge refers to unavailable or former component IDs. It was not counted as mastery of a larger combined lecture.", nodeList(plan.unknown_knowledge)));
    const selected = data.collections.find(row => row.id === settings.collection);
    if (strings(selected?.background).length) result.append(el("details", {}, el("summary", { text: "Collection-level assumed background" }), el("p", { text: strings(selected.background).join("; ") })));
    const recommendations = data.relationships.filter(edge => !edge.internal && relevant.has(edge.from) && edge.type === "soft_depends_on");
    const collectionPreparation = selected ? data.relationships.filter(edge => edge.type === "suggested_preparation" && edge.from === "collection:" + selected.id) : [];
    if (recommendations.length || collectionPreparation.length) result.append(el("details", {}, el("summary", { text: settings.include_soft ? "Suggested links enforced in this order · collection suggestions remain optional" : "Suggested preparation · not required by this plan" }),
      ...[...recommendations, ...collectionPreparation].map(edge => el("p", {},
        data.nodes[edge.to]?.available && data.nodes[edge.to]?.url ? link(data.nodes[edge.to].title, data.nodes[edge.to].url) : edge.to,
        edge.reasons.length ? " · " + edge.reasons.join("; ") : ""))));
    if (!readyMode && steps.length) {
      const entries = steps.map(row => ({ id: randomId(), lecture_id: row.id, course_id: null }));
      const enqueue = async (play) => {
        queue.disabled = listen.disabled = true;
        try { await context.enqueue?.(entries, { play }); if (root.isConnected) result.append(el("p", {}, link("Open listening queue", "/listening"))); }
        catch (error) { status.textContent = error.message; queue.disabled = listen.disabled = false; }
      };
      const queue = action("Add this order to my listening queue", () => enqueue(false), { disabled: !plan.valid, "data-plan-action": "" });
      const listen = action("Listen in this order", () => enqueue(true), { disabled: !plan.valid, class: "primary", "data-plan-action": "" });
      result.append(el("div", { class: "actions section" }, listen, queue), el("p", { class: "muted", text: "Appends the order to your existing queue. Listen starts its first step; audio can continue automatically. Presentations remain explicit steps to open." }));
    }
    const list = el("ol", { class: "plan-steps" });
    const primary = readyMode ? steps.filter(row => row.prerequisites_reviewed) : steps;
    for (const row of primary) list.append(el("li", {}, material(row, row.role === "review" ? "Review · uncertain familiarity" : row.role === "prerequisite" ? "Preparation for your destination" : row.role === "goal" ? "Selected material" : row.role)));
    result.append(list);
    if (readyMode && unmapped.length) {
      const others = steps.filter(row => !row.prerequisites_reviewed);
      const more = el("details", { class: "plan-unmapped-ready" }, el("summary", { text: `${others.length} other candidates need background review` }),
        el("p", { class: "muted", text: "No recorded constraint is missing, but these lessons have incomplete prerequisite coverage. Inspect their background before treating them as a starting point." }));
      const candidates = el("ol", { class: "plan-steps" });
      const append = rows => rows.forEach(row => candidates.append(el("li", {}, material(row, "Background mapping incomplete"))));
      append(others.slice(0, 20)); more.append(candidates);
      if (others.length > 20) {
        const expand = action("Show all candidates with incomplete background", () => { append(others.slice(20)); expand.remove(); });
        more.append(expand);
      }
      result.append(more);
      if (!primary.length) result.prepend(el("p", { class: "muted", text: "No candidate in this scope has a completed prerequisite review yet. Other candidates remain available below." }));
    }
    if (!steps.length && plan.valid) result.append(el("p", { text: readyMode ? "No further candidates meet the recorded requirements in this scope. Revisit your background choices or choose another scope." : "The selected material is already covered by your familiarity assumptions. Change those choices if you want it included for review." }));
  }
  function changed() { invalidate(); saveSettings(); populate(); if (hasPlan) { clearTimeout(timer); timer = setTimeout(() => { if (root.isConnected) compute(); }, 180); } }
  form.onsubmit = event => { event.preventDefault(); compute(); };
  mode.onchange = goal.onchange = start.onchange = changed;
  category.onchange = () => { settings.collection = settings.goal = settings.start = ""; collection.value = goal.value = start.value = ""; changed(); };
  collection.onchange = () => { settings.start = ""; start.value = ""; changed(); };
  proof.onchange = soft.onchange = assume.onchange = changed;
  search.oninput = () => populate();
  backgroundSearch.oninput = drawKnowledge;
  populate(); drawKnowledge();
  if (settings.goal || (settings.mode === "collection" && settings.collection) || settings.mode === "ready") await compute();
}

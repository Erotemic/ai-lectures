"""Personal learning order from explicit prerequisite evidence, using stdlib only.

Relationship direction is dependent -> prerequisite. Navigation, history and
collection membership never imply preparation. This module does no I/O.
"""

from collections import defaultdict, deque
from copy import deepcopy
import heapq


_LIST_FIELDS = {"goals", "known", "uncertain", "order_hint", "scope"}
_BOOL_FIELDS = {"assume_uncertain", "include_soft", "include_proof"}
_MAX_IDS = 5000
_MAX_TOTAL_IDS = 10000
_MAX_ID_LENGTH = 256
_LABELS = {
    "hard_depends_on": "Required background",
    "soft_depends_on": "Suggested background, included by request",
    "proof_depends_on": "Proof dependency, included by request",
}


def _request(value):
    if not isinstance(value, dict):
        raise ValueError("The learning-plan request must be an object")
    unknown = set(value) - _LIST_FIELDS - _BOOL_FIELDS - {"start"}
    if unknown:
        raise ValueError("Unknown learning-plan request field: " + str(next(iter(unknown))))
    result = {}
    total = 0
    for field in _LIST_FIELDS:
        if field == "scope" and field not in value:
            continue
        items = value.get(field, [])
        if not isinstance(items, list) or len(items) > _MAX_IDS:
            raise ValueError(f"{field} must be a list of at most {_MAX_IDS} lecture IDs")
        if any(not isinstance(item, str) or not item.strip() or item != item.strip()
               or len(item) > _MAX_ID_LENGTH for item in items):
            raise ValueError(f"{field} must contain nonempty lecture IDs of at most {_MAX_ID_LENGTH} characters")
        total += len(items)
        result[field] = list(dict.fromkeys(items))
    if total > _MAX_TOTAL_IDS:
        raise ValueError("Too many learning-plan request IDs")
    for field in _BOOL_FIELDS:
        flag = value.get(field, False)
        if not isinstance(flag, bool):
            raise ValueError(f"{field} must be a boolean")
        result[field] = flag
    start = value.get("start")
    if start is not None and (not isinstance(start, str) or not start.strip()
                              or start != start.strip() or len(start) > _MAX_ID_LENGTH):
        raise ValueError("start must be a lecture ID or null")
    result["start"] = start
    return result


def _cycles(vertices, dependencies):
    """Iterative Kosaraju SCCs: only genuine cyclic components, not their tails."""
    seen, finished = set(), []
    for seed in sorted(vertices):
        stack = [(seed, False)]
        while stack:
            key, leaving = stack.pop()
            if leaving:
                finished.append(key)
            elif key not in seen:
                seen.add(key)
                stack.append((key, True))
                stack.extend((other, False) for other in sorted(
                    dependencies.get(key, set()) & vertices, reverse=True
                ) if other not in seen)
    reverse = defaultdict(set)
    for key in vertices:
        for other in dependencies.get(key, set()) & vertices:
            reverse[other].add(key)
    seen, result = set(), []
    for seed in reversed(finished):
        if seed in seen:
            continue
        component, stack = set(), [seed]
        while stack:
            key = stack.pop()
            if key in seen:
                continue
            seen.add(key)
            component.add(key)
            stack.extend(reverse[key] - seen)
        if len(component) > 1 or seed in dependencies.get(seed, set()):
            result.append(sorted(component))
    return sorted(result)


def build_learning_plan(graph, request):
    """Return a deterministic JSON-safe plan; reject malformed requests.

    ``steps`` is the executable portion of the required closure. Missing nodes
    and cycles invalidate a full plan; their dependants are explicitly blocked,
    never silently treated as satisfied. ``required_by`` names requested goals.

    Knowledge is accepted only for exact current lecture IDs, even when an old
    component can resolve to a combined lecture for navigation. Uncertainty wins
    over a conflicting known selection and remains review unless assumed known.
    ``ready`` examines the supplied scope, or all lecture nodes when omitted.
    ``unmapped`` means prerequisite review is not explicitly marked complete;
    absence of recorded constraints is never a complete-curriculum guarantee.
    """
    options = _request(request)
    if not isinstance(graph, dict) or not isinstance(graph.get("nodes"), dict):
        raise ValueError("A learning map with nodes is required")
    nodes = graph["nodes"]
    aliases = graph.get("component_lectures", {})
    if not isinstance(aliases, dict) or not isinstance(graph.get("relationships", []), list):
        raise ValueError("Invalid learning-map associations or relationships")

    def resolve(key):
        seen = set()
        while isinstance(aliases.get(key), str) and aliases[key] != key:
            if key in seen:
                # An alias loop supplies no usable current identity.
                return None
            seen.add(key)
            key = aliases[key]
        return key

    def lecture(key):
        return isinstance(nodes.get(key), dict) and nodes[key].get("kind", "lecture") == "lecture"

    def available(key):
        return lecture(key) and nodes[key].get("available", True) is not False

    goals = list(dict.fromkeys(resolve(key) or key for key in options["goals"]))
    if any(key in nodes and not lecture(key) for key in goals):
        raise ValueError("Learning goals must be lecture IDs, not collection IDs")
    unknown_knowledge = sorted({
        key for field in ("known", "uncertain") for key in options[field]
        if not lecture(key) or resolve(key) != key
    })
    uncertain = {key for key in options["uncertain"] if lecture(key) and resolve(key) == key}
    supplied_known = {key for key in options["known"] if lecture(key) and resolve(key) == key}
    known = supplied_known - uncertain
    assumed = uncertain if options["assume_uncertain"] else set()
    mastered = known | assumed
    selected_types = {"hard_depends_on"}
    if options["include_soft"]:
        selected_types.add("soft_depends_on")
    if options["include_proof"]:
        selected_types.add("proof_depends_on")

    dependencies = defaultdict(set)
    evidence = defaultdict(list)
    for edge in graph.get("relationships", []):
        if not isinstance(edge, dict) or edge.get("type") not in selected_types:
            continue
        original_from, original_to = edge.get("from"), edge.get("to")
        if not all(isinstance(key, str) and key for key in (original_from, original_to)):
            raise ValueError("A selected prerequisite relationship has invalid endpoints")
        source, target = resolve(original_from) or original_from, resolve(original_to) or original_to
        if source == target and (edge.get("internal") or original_from != original_to):
            continue
        dependencies[source].add(target)
        reasons = edge.get("reasons", [])
        reasons = reasons if isinstance(reasons, list) else []
        why = [reason for reason in reasons if isinstance(reason, str) and reason.strip()]
        if isinstance(edge.get("why"), str) and edge["why"].strip():
            why.append(edge["why"])
        evidence[(source, target)].append((edge["type"], why))

    needed, required_by = set(), defaultdict(set)
    for goal in goals:
        visited, stack = set(), [goal]
        while stack:
            key = stack.pop()
            if key in visited or key in mastered:
                continue
            visited.add(key)
            needed.add(key)
            if key != goal:
                required_by[key].add(goal)
            stack.extend(dependencies[key] - visited)

    missing = {key for key in needed if not available(key)}
    cycles = _cycles(needed, dependencies)
    cyclic = {key for cycle in cycles for key in cycle}
    dependants = defaultdict(set)
    for key in needed:
        for prerequisite in dependencies[key] & needed:
            dependants[prerequisite].add(key)
    # Retain the actual failure roots for each blocked dependant.
    blocked_by = defaultdict(set)
    for problem in sorted(missing | cyclic):
        visited, queue = set(), deque([problem])
        while queue:
            key = queue.popleft()
            if key in visited:
                continue
            visited.add(key)
            blocked_by[key].add(problem)
            queue.extend(dependants[key] - visited)
    blocked = set(blocked_by) - missing
    actionable = needed - missing - blocked

    preferences = [resolve(key) or key for key in options["order_hint"]]
    hint_rank = {key: index for index, key in reversed(list(enumerate(preferences)))}
    start = resolve(options["start"]) if options["start"] is not None else None

    def priority(key):
        return key != start, hint_rank.get(key, len(preferences)), key

    counts = {key: len(dependencies[key] & actionable) for key in actionable}
    heap = [priority(key) for key, count in counts.items() if not count]
    heapq.heapify(heap)
    ordered = []
    while heap:
        key = heapq.heappop(heap)[-1]
        ordered.append(key)
        for dependant in sorted(dependants[key] & actionable):
            counts[dependant] -= 1
            if counts[dependant] == 0:
                heapq.heappush(heap, priority(dependant))

    steps = []
    for key in ordered:
        row = nodes[key]
        role = "review" if key in uncertain else "goal" if key in goals else "prerequisite"
        reasons = []
        if key in goals:
            reasons.append("Selected as a learning goal.")
        if key in uncertain:
            reasons.append("Knowledge is uncertain; review remains in the plan.")
        for dependant in sorted(dependants[key]):
            for kind, why in evidence[(dependant, key)]:
                reasons.append(f"{_LABELS[kind]} for {nodes.get(dependant, {}).get('title', dependant)}.")
                reasons.extend(why)
        step = dict(
            id=key, title=row.get("title", key), url=row.get("url"), available=True,
            role=role, depends_on=sorted(dependencies[key]),
            required_by=sorted(required_by[key]), reasons=list(dict.fromkeys(reasons)),
        )
        for field in ("prerequisites_reviewed", "background", "estimated_minutes", "readiness_checks"):
            if field in row:
                step[field] = deepcopy(row[field])
        steps.append(step)

    if "scope" in options:
        scope = {resolve(key) or key for key in options["scope"]}
    else:
        scope = {key for key in nodes if lecture(key) and resolve(key) == key}
    ready = sorted((key for key in scope if available(key) and key not in mastered
                    and dependencies[key] <= mastered), key=priority)
    unmapped = sorted(key for key in scope | needed
                      if available(key) and nodes[key].get("prerequisites_reviewed") is not True)
    return dict(
        schema_version=1, generation=deepcopy(graph.get("generation")),
        valid=not missing and not cycles, steps=steps, goals=goals,
        known=sorted(known), assumed_uncertain=sorted(assumed), uncertain=sorted(uncertain),
        missing=sorted(missing), cycles=cycles, blocked=sorted(blocked), ready=ready,
        unmapped=unmapped, unknown_knowledge=unknown_knowledge,
        blocked_by={key: sorted(blocked_by[key]) for key in sorted(blocked)},
        unknown_scope=sorted(key for key in scope if not lecture(key)),
        ignored_preferences=sorted({key for key in preferences + ([start] if start else []) if not lecture(key)}),
        knowledge_conflicts=sorted(supplied_known & uncertain),
        constraint_types=sorted(selected_types),
        assumptions=[dict(id=key, basis="known" if key in known else "assumed_uncertain",
                          available=available(key), prerequisites_not_rechecked=True)
                     for key in sorted(mastered)],
        limitations=["Only recorded prerequisite constraints are checked; a ready or valid plan does not certify complete background coverage."],
    )

"""Bounded metadata reviewer commands; model calls are explicit CLI actions."""

from pathlib import Path
import json
import os
import sys

from .core import digest
from .library import Library
from .metadata_audit import (
    AuditStore,
    CONTRACT,
    call_model,
    requests_for,
    structural_hints,
)


def add_commands(commands):
    audit = commands.add_parser(
        "metadata-audit",
        help="Plan/run small-model metadata reviews and export approved proposals",
    )
    sub = audit.add_subparsers(dest="audit_action", required=True)
    for action in (
        "plan",
        "run",
        "export-requests",
        "import-responses",
        "report",
        "list-requests",
        "show-request",
    ):
        parser = sub.add_parser(action)
        parser.add_argument("--repository", type=Path)
        parser.add_argument("--installed-only", action="store_true")
        parser.add_argument("--lecture", action="append", default=[])
        parser.add_argument("--collection", action="append", default=[])
        if action in {"plan", "run", "export-requests"}:
            parser.add_argument(
                "--model",
                default=os.environ.get("AI_LECTURES_REVIEW_MODEL", "local-reviewer"),
            )
            parser.add_argument("--chunk-chars", type=int, default=6000)
            parser.add_argument(
                "--base-url", default=os.environ.get("AI_LECTURES_REVIEW_BASE_URL")
            )
            parser.add_argument(
                "--limit",
                type=int,
                default=5,
                help="Maximum pending lectures per invocation",
            )
        if action == "run":
            parser.add_argument("--max-requests", type=int, default=20)
            parser.add_argument("--max-tokens", type=int, default=1600)
            parser.add_argument("--timeout", type=int, default=180)
        if action == "export-requests":
            parser.add_argument("--output", type=Path, required=True)
        if action in {"list-requests", "show-request"}:
            parser.add_argument("--requests", type=Path, required=True)
        if action == "list-requests":
            parser.add_argument("--pending-only", action="store_true")
        if action == "show-request":
            parser.add_argument("--id", required=True)
        if action == "import-responses":
            parser.add_argument("--requests", type=Path, required=True)
            parser.add_argument(
                "--responses",
                type=Path,
                required=True,
                help="JSONL: id, response, optional model",
            )
        if action == "report":
            parser.add_argument("--output", type=Path)
            parser.add_argument("--approved-only", action="store_true")


def selected_rows(snapshot, args):
    selected = set(args.lecture)
    for key in args.collection:
        if key not in snapshot["courses"]:
            raise ValueError("Unknown collection: " + key)
        selected.update(snapshot["courses"][key]["lectures"])
    if selected - snapshot["lectures"].keys():
        raise ValueError("Unknown lecture selection")
    return {
        key: row
        for key, row in snapshot["lectures"].items()
        if row.get("kind") == "audio" and (not selected or key in selected)
    }


def run(args, repository):
    if args.audit_action in {"list-requests", "show-request"}:
        requests = (
            json.loads(line)
            for line in args.requests.read_text().splitlines()
            if line.strip()
        )
        if args.audit_action == "list-requests":
            if args.pending_only:
                cached = AuditStore(args.library / "state").cached_ids()
                requests = (item for item in requests if item["id"] not in cached)
            print(
                json.dumps(
                    [
                        dict(
                            id=item["id"],
                            lecture=item["specification"]["lecture_id"],
                            index=item["specification"]["index"],
                            total=item["specification"]["total"],
                        )
                        for item in requests
                    ],
                    indent=2,
                )
            )
        else:
            item = next((item for item in requests if item["id"] == args.id), None)
            if item is None:
                raise ValueError("Unknown request ID")
            print(
                json.dumps(
                    dict(id=item["id"], messages=item["messages"]),
                    ensure_ascii=False,
                    indent=2,
                )
            )
        return 0
    library = Library(args.library, repository=repository)
    rows = selected_rows(library.snapshot(copy=False), args)
    store = AuditStore(library.store.state)
    action = args.audit_action
    if action == "report":
        report = store.report(
            rows, include_removed=not (args.lecture or args.collection)
        )
        if args.approved_only:
            report["findings"] = [
                item
                for item in report["findings"]
                if item["decision"] == "approved" and not item["stale"]
            ]
        text = json.dumps(report, ensure_ascii=False, indent=2) + "\n"
        if args.output:
            args.output.write_text(text)
        else:
            print(text)
        return 0
    if action == "import-responses":
        requests = {
            item["id"]: item
            for line in args.requests.read_text().splitlines()
            if line.strip()
            for item in [json.loads(line)]
        }
        count, failures, seen = 0, 0, set()
        for line in args.responses.read_text().splitlines():
            if not line.strip():
                continue
            item = json.loads(line)
            if item["id"] in seen:
                raise ValueError("Duplicate request ID in response file")
            seen.add(item["id"])
            if item["id"] not in requests:
                raise ValueError("Unknown review request in response file")
            request = requests[item["id"]]
            # Imported findings retain their original fingerprint; stale findings
            # remain inspectable but cannot be approved against current content.
            if request["specification"]["lecture_id"] not in rows:
                raise ValueError("Response outside selected content")
            receipt = store.ingest(
                request, item["response"], actual_model=item.get("model")
            )
            print(json.dumps(receipt))
            failures += receipt["status"] != "valid"
            count += 1
        print(json.dumps(dict(imported=count, failures=failures)))
        return 1 if failures else 0
    if args.limit < 1:
        raise ValueError("--limit must be positive")
    if not args.model.strip():
        raise ValueError("Select a model name")
    if action == "run" and not args.base_url:
        raise ValueError(
            "Set --base-url or AI_LECTURES_REVIEW_BASE_URL; no model service is contacted by default"
        )
    if action == "run" and (
        args.max_requests < 1 or args.max_tokens < 128 or args.timeout < 1
    ):
        raise ValueError("Request budget, output tokens and timeout must be positive")
    provider = digest(args.base_url.rstrip("/")) if args.base_url else "offline"
    hints = structural_hints(rows)
    pending = []
    cached = store.cached_ids()
    for key in sorted(rows, key=lambda key: (-len(hints.get(key, [])), key)):
        requests = list(
            requests_for(
                rows[key], model=args.model, size=args.chunk_chars, provider=provider
            )
        )
        todo = [request for request in requests if request["id"] not in cached]
        if todo:
            pending.append(
                dict(
                    lecture=key,
                    title=rows[key]["title"],
                    hints=hints.get(key, []),
                    requests=todo if len(pending) < args.limit else [],
                    pending=len(todo),
                    total=len(requests),
                )
            )
    pending.sort(key=lambda row: (-len(row["hints"]), row["lecture"]))
    if action == "plan":
        print(
            json.dumps(
                dict(
                    contract=CONTRACT,
                    lectures=len(rows),
                    pending_lectures=len(pending),
                    pending_requests=sum(row["pending"] for row in pending),
                    next=[
                        {key: value for key, value in row.items() if key != "requests"}
                        for row in pending[: args.limit]
                    ],
                ),
                ensure_ascii=False,
                indent=2,
            )
        )
        return 0
    selected = [request for row in pending[: args.limit] for request in row["requests"]]
    if action == "export-requests":
        text = "".join(
            json.dumps(request, ensure_ascii=False) + "\n" for request in selected
        )
        if args.output.exists() and args.output.read_text() != text:
            raise ValueError(
                "Request file already exists; choose a new batch filename to preserve previous assignments"
            )
        args.output.write_text(text)
        print(json.dumps(dict(requests=len(selected), output=str(args.output))))
        return 0
    failures = 0
    for request in selected[: args.max_requests]:
        try:
            response, actual_model = call_model(
                args.base_url,
                args.model,
                request["messages"],
                timeout=args.timeout,
                max_tokens=args.max_tokens,
            )
            receipt = store.ingest(request, response, actual_model=actual_model)
            failures += receipt["status"] != "valid"
        except (ValueError, KeyError, IndexError, TypeError) as exc:
            error = (
                str(exc) if isinstance(exc, ValueError) else "Malformed model response"
            )
            store.record_error(request, error)
            receipt = dict(request_id=request["id"], status="error", error=error)
            failures += 1
        print(
            json.dumps(dict(lecture=request["specification"]["lecture_id"], **receipt)),
            flush=True,
        )
    print(
        json.dumps(
            dict(
                requests=min(len(selected), args.max_requests),
                failures=failures,
                remaining_selected=max(0, len(selected) - args.max_requests),
            )
        )
    )
    return 1 if failures else 0

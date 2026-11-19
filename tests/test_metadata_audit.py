"""Metadata review validates evidence and stays separate from authored content."""

from copy import deepcopy
import json
from pathlib import Path
import subprocess
import sys
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer

import pytest
from starlette.testclient import TestClient

from ailectures.core import Conflict, text_digest
from ailectures.metadata_audit import (
    AuditStore,
    already_present,
    chunks,
    fingerprint,
    parse_response,
    requests_for,
    structural_hints,
    call_model,
)
from ailectures.packs import export_release
from ailectures.web import create_app
from test_content_packs import source_pack


def lecture(text=None):
    return source_pack(
        text=text
        or "The household provided information about military movements. Agents listened carefully and compared accounts before reporting."
    )["lectures"]["music:001000"]


def suggestion(row, **changes):
    return (
        dict(
            kind="tag",
            value="Intelligence and espionage",
            evidence=row["transcript"][:90],
            reason="The passage explains information collection as sustained subject matter.",
            confidence=0.85,
            coverage="substantial",
        )
        | changes
    )


def test_excerpts_cover_entire_text_and_prompt_context_is_bounded():
    text = " ".join(f"word{index:05}" for index in range(3500))
    parts = chunks(text, 1000)
    cursor = 0
    for part in parts:
        start = text.find(part, max(0, cursor - 400))
        assert start <= cursor and len(part) <= 1000
        cursor = start + len(part)
    assert cursor == len(text)
    row = lecture(text)
    row["metadata"] = {
        "tags": ["Long label " + str(n) + "x" * 100 for n in range(300)],
        "chronology": {"period": {"start": 1600, "end": 1700, "note": "x" * 7000}},
    }
    for request in requests_for(row, model="test", size=1000):
        assert len(request["messages"][1]["content"]) < 14500
    with pytest.raises(ValueError):
        chunks(text, 100)


def test_validation_rejects_bad_quotes_and_incidental_or_existing_metadata():
    row = lecture()
    row["metadata"] = {
        "tags": ["History"],
        "tag_paths": [["History", "Military history", "Espionage"]],
    }
    request = next(requests_for(row, model="test"))
    items = [
        suggestion(row),
        suggestion(row, evidence="A quotation the lecture does not contain."),
        suggestion(row, value="Households", coverage="incidental"),
        suggestion(row, value="History"),
        suggestion(
            row,
            kind="date",
            value={"axis": "period", "start": 0, "end": 1, "approximate": False},
        ),
    ]
    accepted, rejected, invalid = parse_response(
        {"suggestions": items}, request["specification"]
    )
    assert len(accepted) == 1 and len(rejected) == 2 and len(invalid) == 2
    assert already_present(
        "tag_path",
        ["History", "Military history"],
        request["specification"]["metadata"],
    )
    with pytest.raises(ValueError):
        parse_response({"not_suggestions": []}, request["specification"])


def test_caching_dedup_decisions_staleness_and_complete_coverage(tmp_path):
    row = lecture(
        ("The household provided information about military movements. " * 40)
    )
    requests = list(requests_for(row, model="test", size=1000))
    store = AuditStore(tmp_path)
    for request in requests[:-1]:
        item = suggestion(row, evidence=request["specification"]["excerpt"][:90])
        assert (
            store.ingest(
                request, {"suggestions": [item]}, actual_model="Exact test model"
            )["status"]
            == "valid"
        )
    assert store.report({row["id"]: row})["summary"]["reviewed"] == 0
    store.ingest(requests[-1], {"suggestions": []}, actual_model="Exact test model")
    report = store.report({row["id"]: row})
    assert report["summary"]["reviewed"] == 1 and len(report["findings"]) == 1
    finding = report["findings"][0]
    store.decide(finding["id"], "approved", {row["id"]: row})
    assert AuditStore(tmp_path).cached(requests[0]["id"])
    store.ingest(
        requests[0],
        {
            "suggestions": [
                suggestion(row, evidence=requests[0]["specification"]["excerpt"][:90])
            ]
        },
        actual_model="Another model",
    )
    assert store.report({row["id"]: row})["findings"][0]["decision"] == "approved"
    changed = deepcopy(row)
    changed["metadata"]["tags"] = ["New subject"]
    assert fingerprint(changed) != fingerprint(row)
    assert store.report({row["id"]: changed})["summary"]["stale"] == 1
    with pytest.raises(Conflict):
        store.decide(finding["id"], "approved", {row["id"]: changed})
    assert not store.cached(next(requests_for(changed, model="test", size=1000))["id"])


def test_invalid_response_is_retryable_and_empty_valid_response_is_clean(tmp_path):
    row = lecture()
    request = next(requests_for(row, model="test"))
    store = AuditStore(tmp_path)
    receipt = store.ingest(
        request,
        {
            "suggestions": [
                suggestion(row, evidence="Invented unsupported evidence text.")
            ]
        },
    )
    assert receipt["status"] == "invalid" and not store.cached(request["id"])
    assert store.report({row["id"]: row})["summary"]["reviewed"] == 0
    store.ingest(request, {"suggestions": []})
    assert (
        store.cached(request["id"])
        and store.report({row["id"]: row})["summary"]["reviewed"] == 1
    )


def test_structural_cues_are_applicable_and_never_automatic_metadata():
    row = lecture()
    row["metadata"] = {
        "tags": ["Literature"],
        "places": ["Africa", "Unmapped fictional city"],
    }
    row["title"] = "A book from 1850"
    before = deepcopy(row)
    hints = structural_hints({row["id"]: row})[row["id"]]
    assert row == before
    assert {item["kind"] for item in hints} >= {
        "creator_gap",
        "date_label_gap",
        "unmapped_places",
    }
    assert next(item for item in hints if item["kind"] == "unmapped_places")[
        "labels"
    ] == ["Unmapped fictional city"]


def test_reader_review_decisions_and_export_do_not_edit_pack(tmp_path):
    pack = source_pack()
    directory = tmp_path / "source"
    export_release(pack, directory)
    app = create_app(tmp_path / "library", playback_only=True)
    app.state.library.store.install(directory)
    row = app.state.library.snapshot()["lectures"]["music:001000"]
    store = AuditStore(app.state.library.store.state)
    request = next(requests_for(row, model="pi-qwen"))
    store.ingest(
        request,
        {"suggestions": [suggestion(row, evidence=row["transcript"])]},
        actual_model="Test Qwen identity",
    )
    before = {
        p.relative_to(directory): p.read_bytes()
        for p in directory.rglob("*")
        if p.is_file()
    }
    with TestClient(app) as client:
        assert (
            client.get("/topic-graph").status_code
            == client.get("/metadata-audit").status_code
            == 200
        )
        report = client.get("/api/library/metadata-audit").json()
        finding = report["findings"][0]
        assert (
            client.post(
                "/api/library/metadata-audit/" + finding["id"],
                json={"decision": "approved"},
            ).status_code
            == 200
        )
        exported = client.get("/api/library/metadata-audit/export").json()
        assert (
            len(exported["findings"]) == 1
            and exported["findings"][0]["model"] == "Test Qwen identity"
        )
        assert (
            client.post(
                "/api/library/metadata-audit/" + finding["id"],
                headers={"Origin": "https://other.example"},
                json={"decision": "dismissed"},
            ).status_code
            == 403
        )
    assert before == {
        p.relative_to(directory): p.read_bytes()
        for p in directory.rglob("*")
        if p.is_file()
    }


def test_agent_export_import_cli_and_partial_response(tmp_path):
    pack = source_pack(
        text="A long supported statement about collecting intelligence in a household. "
        * 40
    )
    root = tmp_path / "library"
    export_release(pack, tmp_path / "source")
    from ailectures.packs import PackStore

    PackStore(root).install(tmp_path / "source")

    def cli(*args):
        return subprocess.run(
            [
                sys.executable,
                "-m",
                "ailectures",
                "--library",
                str(root),
                "metadata-audit",
                *args,
                "--installed-only",
            ],
            capture_output=True,
            text=True,
        )

    requests = tmp_path / "requests.jsonl"
    responses = tmp_path / "responses.jsonl"
    result = cli(
        "export-requests",
        "--model",
        "pi-qwen",
        "--chunk-chars",
        "1000",
        "--output",
        str(requests),
    )
    assert result.returncode == 0, result.stderr
    items = [json.loads(line) for line in requests.read_text().splitlines()]
    assert len(items) > 1
    listed = json.loads(cli("list-requests", "--requests", str(requests)).stdout)
    shown = json.loads(
        cli("show-request", "--requests", str(requests), "--id", items[0]["id"]).stdout
    )
    assert len(listed) == len(items) and set(shown) == {"id", "messages"}
    responses.write_text(
        json.dumps(
            {
                "id": items[0]["id"],
                "model": "Exact reviewer",
                "response": {"suggestions": []},
            }
        )
        + "\n"
    )
    assert (
        cli(
            "import-responses",
            "--requests",
            str(requests),
            "--responses",
            str(responses),
        ).returncode
        == 0
    )
    report = json.loads(cli("report").stdout)
    assert report["summary"]["reviewed"] == 0
    assert (
        len(
            json.loads(
                cli(
                    "list-requests", "--pending-only", "--requests", str(requests)
                ).stdout
            )
        )
        == len(items) - 1
    )
    assert (
        json.loads(cli("plan", "--model", "pi-qwen", "--chunk-chars", "1000").stdout)[
            "pending_requests"
        ]
        == len(items) - 1
    )


def test_openai_compatible_transport_with_local_mock():
    class Handler(BaseHTTPRequestHandler):
        def do_POST(self):
            payload = json.loads(self.rfile.read(int(self.headers["Content-Length"])))
            assert payload["model"] == "test-model"
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(
                json.dumps(
                    {
                        "model": "mock-exact",
                        "choices": [
                            {
                                "finish_reason": "stop",
                                "message": {"content": '{"suggestions":[]}'},
                            }
                        ],
                    }
                ).encode()
            )

        def log_message(self, *args):
            pass

    server = HTTPServer(("127.0.0.1", 0), Handler)
    thread = threading.Thread(target=server.serve_forever)
    thread.start()
    try:
        content, model = call_model(
            f"http://127.0.0.1:{server.server_port}/v1",
            "test-model",
            [{"role": "user", "content": "Review"}],
        )
        assert json.loads(content) == {"suggestions": []} and model == "mock-exact"
    finally:
        server.shutdown()
        thread.join()
        server.server_close()


def test_changed_review_contract_can_refresh_a_previous_finding(tmp_path, monkeypatch):
    import ailectures.metadata_audit as audit

    row = lecture()
    store = AuditStore(tmp_path)
    request = next(requests_for(row, model="test"))
    store.ingest(
        request, {"suggestions": [suggestion(row)]}, actual_model="First model"
    )
    finding = store.report({row["id"]: row})["findings"][0]
    store.decide(finding["id"], "dismissed", {row["id"]: row})
    monkeypatch.setattr(audit, "PROMPT", audit.PROMPT + "\nAdditional review guidance.")
    assert store.report({row["id"]: row})["findings"][0]["stale"]
    updated = next(requests_for(row, model="test"))
    assert updated["id"] != request["id"]
    store.ingest(updated, {"suggestions": [suggestion(row)]}, actual_model="New model")
    refreshed = store.report({row["id"]: row})["findings"][0]
    assert (
        not refreshed["stale"]
        and refreshed["decision"] == "dismissed"
        and refreshed["model"] == "New model"
    )

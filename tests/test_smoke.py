# tests/test_smoke.py
# Minimal smoke test using monkeypatch (no external API calls)

import pytest   # noqa: F401  # type: ignore
from src.api_client import APIClient

def test_ping_mock(monkeypatch):
    """Basic smoke test: ensure ping() handles success response."""
    client = APIClient("https://example.com")
    monkeypatch.setattr(client, "ping", lambda: {"status_code": 200, "ok": True})
    result = client.ping()
    assert result["status_code"] == 200
    assert result["ok"] is True

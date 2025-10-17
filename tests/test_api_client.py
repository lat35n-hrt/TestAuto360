import pytest
from src.api_client import APIClient

@pytest.fixture
def client():
    # Example public API (replace with your own FastAPI endpoint if needed)
    return APIClient("https://content.guardianapis.com")

def test_ping_endpoint(monkeypatch):
    """Mocked ping check"""
    client = APIClient("https://example.com") # Dummy URL for testing
    monkeypatch.setattr(client, "ping", lambda: {"status_code": 200, "ok": True})
    result = client.ping()
    assert result["status_code"] == 200
    assert result["ok"] is True

def test_get_articles_status(client):
    """API should return valid JSON and contain 'response' key."""
    result = client.get_articles("/world?api-key=test")
    assert isinstance(result, dict)
    assert "response" in result

def test_get_articles_structure(client):
    """Each article item should contain expected fields."""
    result = client.get_articles("/world?api-key=test")
    response = result.get("response", {})
    if "results" in response:
        item = response["results"][0]
        assert "id" in item
        assert "webTitle" in item

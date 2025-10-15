import requests

class APIClient:
    """Simple API client wrapper for demonstration."""

    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip("/")

    def get_articles(self, endpoint: str = "/world/"):
        """Fetch world news articles."""
        url = f"{self.base_url}{endpoint}"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()

    def ping(self):
        """Health check endpoint (for test)."""
        url = f"{self.base_url}/ping"
        response = requests.get(url, timeout=5)
        return {"status_code": response.status_code, "ok": response.ok}

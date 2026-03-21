"""REST API client wrapper.

Handles base URL construction, optional Bearer token auth,
and a single get() method for all requests.
"""
from __future__ import annotations

import os
import requests
from typing import Any, Dict, Optional


class APIClient:
    def __init__(self, base_url: Optional[str] = None, token: Optional[str] = None) -> None:
        self.base_url = (base_url or os.getenv("API_BASE_URL", "https://jsonplaceholder.typicode.com")).rstrip("/")
        self.token = token or os.getenv("API_TOKEN", "")
        self.session = requests.Session()
        if self.token:
            # Bearer token auth — swap for API key header or Basic as needed
            self.session.headers.update({"Authorization": f"Bearer {self.token}"})

    def get(self, endpoint: str, params: Optional[Dict[str, Any]] = None) -> Any:
        """Make a GET request and return parsed JSON.

        Raises requests.HTTPError on non-2xx responses.
        """
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        response = self.session.get(url, params=params or {}, timeout=30)
        response.raise_for_status()
        return response.json()

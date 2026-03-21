"""REST API client wrapper.

Provides a simple, reusable interface for making authenticated GET requests
to a REST API. Designed to be adapted for different APIs by changing the
base URL, auth method, and any required headers.

Current auth: Bearer token (set via .env or environment variable API_TOKEN)
To adapt for API key headers: swap the Authorization header for the key name your API expects
To adapt for Basic auth: use requests.auth.HTTPBasicAuth instead
"""
from __future__ import annotations

import os
import requests
from typing import Any, Dict, Optional


class APIClient:
    def __init__(self, base_url: Optional[str] = None, token: Optional[str] = None) -> None:
        """Initialize the API client with a base URL and optional auth token.

        Reads configuration from environment variables if not passed directly.
        This keeps credentials out of source code and makes the template
        safe to share publicly.

        Args:
            base_url: root URL of the API (e.g. "https://api.example.com")
            token: Bearer token for authentication (or set API_TOKEN in .env)
        """
        # Fall back to environment variable so credentials stay out of code
        self.base_url = (base_url or os.getenv("API_BASE_URL", "https://jsonplaceholder.typicode.com")).rstrip("/")
        self.token = token or os.getenv("API_TOKEN", "")

        # Use a requests.Session for connection reuse across multiple requests
        self.session = requests.Session()

        # Add Bearer token auth if a token is present
        # To switch to an API key header, replace this with:
        # self.session.headers.update({"X-API-Key": self.token})
        if self.token:
            self.session.headers.update({"Authorization": f"Bearer {self.token}"})

    def get(self, endpoint: str, params: Optional[Dict[str, Any]] = None) -> Any:
        """Make a GET request to the given endpoint and return parsed JSON.

        Constructs the full URL from base_url + endpoint, passes any query
        params, and raises an HTTPError on non-2xx responses so callers
        don't have to check status codes manually.

        Args:
            endpoint: API path relative to base_url (e.g. "posts" or "users/1")
            params: optional dict of query string parameters

        Returns:
            parsed JSON response (usually a list or dict)

        Raises:
            requests.HTTPError: on 4xx or 5xx responses
        """
        url = f"{self.base_url}/{endpoint.lstrip('/')}"  # avoid double slashes
        response = self.session.get(url, params=params or {}, timeout=30)
        response.raise_for_status()  # raise immediately on error status codes
        return response.json()

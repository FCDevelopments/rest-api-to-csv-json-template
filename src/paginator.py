"""Offset/limit paginator for REST APIs.

Fetches pages until the API returns fewer results than the page size,
which signals the last page. Adapt for cursor-based APIs by replacing
the offset logic with a next_cursor field.
"""
from __future__ import annotations

import os
from typing import Any, Dict, Iterator, List
from client import APIClient


def paginate(client: APIClient, endpoint: str, page_size: int = 0) -> List[Dict[str, Any]]:
    """Collect all results from a paginated endpoint.

    Args:
        client: authenticated APIClient instance
        endpoint: API path to call (e.g. "posts" or "users")
        page_size: number of records per request (0 = use PAGE_SIZE env var or default 10)

    Returns:
        flat list of all result objects across all pages
    """
    if page_size == 0:
        page_size = int(os.getenv("PAGE_SIZE", "10"))

    all_results: List[Dict[str, Any]] = []
    offset = 0

    while True:
        params = {"_start": offset, "_limit": page_size}
        page = client.get(endpoint, params=params)

        # JSONPlaceholder returns a list — adapt shape check for your API
        if not isinstance(page, list) or len(page) == 0:
            break

        all_results.extend(page)

        # If we got fewer results than requested, this is the last page
        if len(page) < page_size:
            break

        offset += page_size

    return all_results

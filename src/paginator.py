"""Offset/limit paginator for REST APIs.

This module handles the most common REST pagination pattern: offset + limit.
It keeps fetching pages until the API returns fewer results than the page size,
which signals there are no more records.

To adapt for cursor-based APIs (e.g. GitHub, Stripe):
- Replace the _start/_limit params with your API's cursor field
- Use the response's next_cursor or next_page_token to set the next request param
- Stop when the cursor is null/empty instead of checking result count
"""
from __future__ import annotations

import os
from typing import Any, Dict, List
from client import APIClient


def paginate(client: APIClient, endpoint: str, page_size: int = 0) -> List[Dict[str, Any]]:
    """Collect all results from a paginated REST endpoint.

    Repeatedly calls the endpoint with increasing offset values until the
    API returns a partial page (fewer results than page_size), then stops.

    Args:
        client: authenticated APIClient instance
        endpoint: API path to paginate (e.g. "posts" or "users")
        page_size: number of records per request; reads PAGE_SIZE env var or defaults to 10

    Returns:
        flat list of all result dicts across all pages
    """
    # Allow page size to be set via env var for easy adjustment without code changes
    if page_size == 0:
        page_size = int(os.getenv("PAGE_SIZE", "10"))

    all_results: List[Dict[str, Any]] = []
    offset = 0  # tracks where we are in the full result set

    while True:
        # JSONPlaceholder uses _start and _limit — adapt these param names for your API
        params = {"_start": offset, "_limit": page_size}
        page = client.get(endpoint, params=params)

        # JSONPlaceholder returns a list; check for empty or non-list to stop
        if not isinstance(page, list) or len(page) == 0:
            break  # no more results

        all_results.extend(page)

        # If we got fewer results than the page size, this is the last page
        if len(page) < page_size:
            break

        # Move the offset forward for the next request
        offset += page_size

    return all_results

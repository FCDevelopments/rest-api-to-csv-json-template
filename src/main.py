"""REST API to CSV/JSON Integration Template.

Demo: pulls posts from JSONPlaceholder (free public API, no key needed).
Adapt client.py for your target API auth and paginator.py for your pagination style.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

from client import APIClient
from paginator import paginate
from exporter import export_csv, export_json


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Pull data from a REST API and export as CSV or JSON."
    )
    parser.add_argument(
        "--endpoint",
        default="posts",
        help="API endpoint to pull from (default: posts)",
    )
    parser.add_argument(
        "--output-format",
        choices=["csv", "json", "both"],
        default="both",
        help="Output format: csv, json, or both (default: both)",
    )
    parser.add_argument(
        "--output-dir",
        default="output",
        help="Directory for output files (default: output)",
    )
    parser.add_argument(
        "--page-size",
        type=int,
        default=10,
        help="Results per API page (default: 10)",
    )
    args = parser.parse_args()

    print(f"Connecting to API...")
    client = APIClient()

    print(f"Fetching '{args.endpoint}' with page size {args.page_size}...")
    results = paginate(client, args.endpoint, page_size=args.page_size)
    print(f"Fetched {len(results)} records.")

    if not results:
        print("No results returned. Check endpoint or API connectivity.")
        sys.exit(1)

    if args.output_format in ("csv", "both"):
        path = export_csv(results, args.output_dir)
        print(f"CSV saved: {path}")

    if args.output_format in ("json", "both"):
        path = export_json(results, args.output_dir)
        print(f"JSON saved: {path}")

    print("Done.")


if __name__ == "__main__":
    main()

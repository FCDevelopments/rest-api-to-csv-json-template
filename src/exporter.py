"""CSV and JSON export utilities.

Handles writing API result data to disk in either CSV or JSON format.
Both functions accept the same list-of-dicts input so callers don't
need to worry about format differences — just call the right function.
"""
from __future__ import annotations

import csv
import json
from pathlib import Path
from typing import Any, Dict, List


def export_csv(results: List[Dict[str, Any]], output_dir: str, filename: str = "results.csv") -> Path:
    """Write a list of result dicts to a CSV file.

    Column names are inferred from the keys of the first result row,
    so no schema needs to be defined in advance. Extra keys in later
    rows are ignored via extrasaction="ignore".

    Args:
        results: list of dicts from the API (all should have the same keys)
        output_dir: directory to write the file into (created if needed)
        filename: output filename (default: results.csv)

    Returns:
        Path object pointing to the written file
    """
    out_dir = Path(output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)  # create directory if it doesn't exist
    output_path = out_dir / filename

    # Handle empty results gracefully — write an empty file rather than crashing
    if not results:
        output_path.write_text("", encoding="utf-8")
        return output_path

    # Infer column names from the first row's keys
    fieldnames = list(results[0].keys())

    with output_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(results)  # writes all rows in one call

    return output_path


def export_json(results: List[Dict[str, Any]], output_dir: str, filename: str = "results.json") -> Path:
    """Write a list of result dicts to a formatted JSON file.

    Uses indent=2 for human-readable output and ensure_ascii=False
    to preserve non-ASCII characters (e.g. accented names, emoji).

    Args:
        results: list of dicts from the API
        output_dir: directory to write the file into (created if needed)
        filename: output filename (default: results.json)

    Returns:
        Path object pointing to the written file
    """
    out_dir = Path(output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    output_path = out_dir / filename

    # ensure_ascii=False preserves international characters correctly
    output_path.write_text(
        json.dumps(results, indent=2, ensure_ascii=False),
        encoding="utf-8"
    )

    return output_path

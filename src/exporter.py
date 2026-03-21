"""CSV and JSON export utilities.

Takes a list of dicts (API results) and writes them to disk
in the requested format with consistent field ordering.
"""
from __future__ import annotations

import csv
import json
from pathlib import Path
from typing import Any, Dict, List


def export_csv(results: List[Dict[str, Any]], output_dir: str, filename: str = "results.csv") -> Path:
    """Write results to a CSV file.

    Infers column names from the first result row.
    """
    out_dir = Path(output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    output_path = out_dir / filename

    if not results:
        output_path.write_text("", encoding="utf-8")
        return output_path

    fieldnames = list(results[0].keys())
    with output_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(results)

    return output_path


def export_json(results: List[Dict[str, Any]], output_dir: str, filename: str = "results.json") -> Path:
    """Write results to a formatted JSON file."""
    out_dir = Path(output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    output_path = out_dir / filename
    output_path.write_text(json.dumps(results, indent=2, ensure_ascii=False), encoding="utf-8")
    return output_path

import json
import tempfile
from pathlib import Path
from src.exporter import export_csv, export_json


SAMPLE = [
    {"id": 1, "title": "Test post", "body": "Hello world"},
    {"id": 2, "title": "Another post", "body": "More content"},
]


def test_export_csv_creates_file() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        path = export_csv(SAMPLE, tmp)
        assert Path(path).exists()
        content = Path(path).read_text(encoding="utf-8")
        assert "id" in content
        assert "Test post" in content


def test_export_json_creates_file() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        path = export_json(SAMPLE, tmp)
        assert Path(path).exists()
        data = json.loads(Path(path).read_text(encoding="utf-8"))
        assert len(data) == 2
        assert data[0]["title"] == "Test post"


def test_export_csv_handles_empty() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        path = export_csv([], tmp)
        assert Path(path).exists()

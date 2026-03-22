# REST API to CSV/JSON Integration Template

> A clean, heavily-commented Python template for pulling data from any REST API and saving it as CSV or JSON — built for IT/support/admin workflows.

## What it does
This template demonstrates how to authenticate against a REST API, paginate through results, handle errors cleanly, and export the response data as either CSV or JSON. It ships with a working public demo against a free API so it runs out of the box.

## Who it's for
- IT admins and support engineers who need to pull data from internal tools or SaaS platforms
- Anyone building lightweight API-to-spreadsheet automation
- Junior developers learning how to structure a clean API integration script

## Problem it solves
Writing a first REST API integration usually means looking up how to handle auth, pagination, errors, and output formatting all at once. This template solves that by showing a clean, real-world-shaped example with every pattern commented and explained.

## Usage
```bash
python src/main.py --output-format csv --output-dir output
python src/main.py --output-format json --output-dir output
```

## Demo API
Uses the free [JSONPlaceholder](https://jsonplaceholder.typicode.com/) API — no API key required for the demo.

## Outputs
| File | What it contains |
|---|---|
| `output/results.csv` | Paginated API results as a flat CSV |
| `output/results.json` | Paginated API results as formatted JSON |
| `sample_output/results_sample.csv` | Sample CSV generated from a real JSONPlaceholder run |
| `sample_output/results_sample.json` | Sample JSON generated from a real JSONPlaceholder run |

## Validation status
- local exporter tests passing
- live JSONPlaceholder demo run passing on 2026-03-22
- generated sample output files included for portfolio review

## Requirements
- Python 3.9+
- `requests` library (only external dependency)

```bash
pip install requests
```

## Limitations (template)
- Demo uses a free public API, not a production endpoint
- Auth pattern shown is Bearer token — adapt for OAuth, API key, or Basic as needed
- Pagination assumes offset/limit style — adapt for cursor-based APIs

## Project structure
```
rest-api-to-csv-json-template/
├── README.md
├── requirements.txt
├── .env.example
├── .gitignore
├── sample_output/
│   ├── results_sample.csv
│   └── results_sample.json
├── src/
│   ├── main.py
│   ├── client.py
│   ├── paginator.py
│   └── exporter.py
└── tests/
    └── test_exporter.py
```

## Roadmap
- additional auth patterns (OAuth2, API key header, Basic)
- cursor-based pagination variant
- rate-limit retry handling
- multi-endpoint batch pull template

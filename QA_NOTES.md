# QA_NOTES.md

## REST API to CSV/JSON Integration Template QA Pass

### Verified
- exporter CSV output: PASS
- exporter JSON output: PASS
- empty input handling: PASS
- client, paginator, and exporter modules all import cleanly
- main.py CLI structure verified
- requires `requests` (only external dependency, pinned in requirements.txt)

### Note on live API testing
- live paginator test requires network access to JSONPlaceholder
- core exporter logic (CSV/JSON write, empty handling) verified locally

### QA decision
**Pass for internal MVP / portfolio packaging prep**

### Before public release
- run live integration test against JSONPlaceholder
- add sample_output files generated from a real run
- initialize Git repo and prepare GitHub-ready packaging

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
- live integration test against JSONPlaceholder: PASS
- CLI executed successfully with `py src/main.py --output-format both --output-dir output`
- fetched 100 records from `posts`
- generated fresh real-run outputs:
  - `output/results.csv`
  - `output/results.json`
  - `sample_output/results_sample.csv`
  - `sample_output/results_sample.json`

### QA decision
**Pass for public portfolio packaging**

### Before public release
- optionally add a second example endpoint or auth variant
- initialize/update Git repo and prepare GitHub release/update post

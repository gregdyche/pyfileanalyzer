# PyFileAnalyzer

A safe, cross-platform tool to analyze and manage file systems: find duplicates, large/old files, and clean up safely.

## Quick Start

```bash
# create & activate venv (example)
python -m venv .venv && source .venv/bin/activate    # Windows: .venv\Scripts\activate

pip install -U pip
pip install -r requirements.txt

# run
python -m pyfileanalyzer --help
pyfileanalyzer analyze .
```

## Development

```bash
pip install -r requirements-dev.txt
pytest -q
```

## Features (MVP)

- Duplicate detection (hash-based + optional byte-compare)
- Large file & old file analysis
- File type breakdown
- Safe operations: move to trash, undo, dry-run
- JSON/CSV/HTML reporting

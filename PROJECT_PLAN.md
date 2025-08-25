# File Analyzer & Manager – Project Definition Report (Refined)

## 1. Project Overview

### 1.1 Project Name
**PyFileAnalyzer** – A Python-based file analysis and management tool.

### 1.2 Purpose
Provide a safe, cross-platform tool to analyze, organize, and manage file systems by identifying duplicates, large files, old files, and unused files, while offering safe cleanup operations.

### 1.3 Target Users
- Power users cleaning up large file collections  
- Developers managing project directories  
- System administrators maintaining file servers  
- Anyone running out of storage space  

### 1.4 Success Criteria
- Accurately identify duplicate files (multiple strategies)  
- Provide detailed file system analysis (size, age, usage patterns)  
- Safe operations only (move to trash, undo log, dry run)  
- Generate clear reports (console, JSON, CSV, HTML, PDF)  
- Handle large directories (100k+ files) efficiently  
- **Usability**: Non-technical users can complete a cleanup in <10 minutes using just CLI help  

---

## 2. Architecture Overview

### 2.1 Architecture Pattern
**Modular CLI with Plugin Architecture**

```
CLI (click/argparse) → Core Engine → Analyzers → Reports & Operations
```

- Core modules: Scanner, Analyzer Orchestrator, Report Generator  
- Analyzers: Duplicates, Large Files, Old Files, File Types, Usage Patterns  
- Utility modules: File Ops, Hashing, Config, Logging, Report Formatters  

### 2.2 Design Principles
- **Single Responsibility** per module  
- **Extensible** via plugin analyzers  
- **Safety First** – no permanent deletes  
- **Performance** – caching, progress indicators, resumable scans  
- **Cross-platform** – Linux, macOS, Windows  

---

## 3. Technical Specifications

### 3.1 Core Dependencies
```python
# Built-in
pathlib, hashlib, os, sys, argparse, json, csv, sqlite3, logging

# External
click>=8.0       # CLI framework
tqdm>=4.60       # Progress bars
pandas>=1.3      # Data analysis/reporting
send2trash>=1.8  # Safe deletion
colorama>=0.4    # Cross-platform colors
rich>=12.0       # Rich console output
loguru>=0.7      # Structured logging
```

### 3.2 Optional
```python
psutil>=5.8       # System monitoring
pillow>=9.0       # Image analysis
mutagen>=1.45     # Media metadata
python-magic>=0.4 # File type detection
```

### 3.3 Python Version
- **Minimum**: 3.8  
- **Recommended**: 3.9+  
- **Tested**: 3.8 – 3.12  

---

## 4. Feature Requirements

### 4.1 Core Features (MVP)
- **Duplicate Detection**: hash-based, size prefilter, optional byte compare  
- **Large File Analysis**: configurable thresholds, distribution reports  
- **Old File Detection**: age filters, extension-specific rules  
- **File Type Analysis**: extensions + MIME detection  
- **Safe File Operations**: move to trash, undo log, dry run, batch confirm  

### 4.2 Advanced Features
- **SQLite Caching** (early, Phase 2): speed up rescans  
- **Config Profiles**: multiple YAML configs (“media cleanup,” “project cleanup”)  
- **Resumable Scans**: pick up where a canceled scan left off  
- **HTML & PDF Reports**: sharable, visual charts  
- **Plugin System**: simple analyzer template for extending functionality  

### 4.3 Future Ideas (Out of Scope for MVP)
- Machine learning (smart similarity, usage prediction)  
- Cloud integrations (Google Drive, Dropbox, S3)  
- Cost/compliance analytics  

---

## 5. Project Structure
(simplified for focus)

```
pyfileanalyzer/
├── src/pyfileanalyzer/
│   ├── cli.py
│   ├── config.py
│   ├── logging.py
│   ├── core/ (scanner, analyzer, db, progress)
│   ├── analyzers/ (duplicates, large, old, types, usage)
│   ├── operations/ (file_ops, undo)
│   ├── reports/ (console, json, csv, html, charts)
│   └── utils/ (hashing, formatting, file_utils, platform)
├── tests/
├── docs/
└── scripts/
```

---

## 6. Implementation Phases

### Phase 1: Core Foundation (Week 1–2)
- Repo + structure + CI/CD  
- CLI framework (click)  
- File scanner + logging  
- Basic duplicate detection  
- Console reports  
- Unit tests  

**Deliverable**: CLI tool that finds duplicates & reports in console  

---

### Phase 2: Core Analyzers (Week 3–4)
- Large file & old file analyzers  
- File type analysis  
- SQLite caching (moved up here)  
- JSON + CSV reporting  
- Safe file operations (trash, undo, dry-run)  

**Deliverable**: Full analyzer set with caching and safe ops  

---

### Phase 3: Advanced Features (Week 5–6)
- Config profiles (YAML)  
- HTML/PDF reporting  
- Resumable scans  
- Plugin framework  

**Deliverable**: Extensible, production-ready analyzer  

---

### Phase 4: Polish & Distribution (Week 7–8)
- Performance optimization  
- Memory/IO tuning  
- Comprehensive docs  
- Integration tests  
- PyPI distribution + release scripts  

**Deliverable**: Stable, distributable package  

---

## 7. CLI Design

### Main Commands
```bash
pyfileanalyzer analyze /path/to/dir
pyfileanalyzer duplicates /path/to/dir
pyfileanalyzer large-files /path/to/dir --size 500MB
pyfileanalyzer old-files /path/to/dir --age 365d
pyfileanalyzer report /path/to/dir --format html --output report.html
pyfileanalyzer cleanup --plan plan.json --confirm
```

### Global Options
```bash
--config CONFIG_FILE
--cache-dir CACHE_DIR
--no-cache
--dry-run
--threads N
--verbose / --quiet
```

---

## 8. Configuration System

### Config Profiles
Support multiple YAML configs (e.g., `~/.pyfileanalyzer/media.yaml`).  

```yaml
analysis:
  large_files:
    threshold: "500MB"
  old_files:
    default_age: "90d"
operations:
  safe_delete: true
  backup_before_operation: true
```

Environment overrides:
```bash
PYFILEANALYZER_CONFIG_DIR
PYFILEANALYZER_CACHE_DIR
PYFILEANALYZER_LOG_LEVEL
```

---

## 9. Database Schema (SQLite)

```sql
CREATE TABLE file_cache (
    path TEXT NOT NULL,
    size INTEGER,
    modified_time REAL,
    hash_md5 TEXT,
    hash_sha256 TEXT,
    file_type TEXT,
    analyzed_at REAL,
    PRIMARY KEY(path, modified_time, size)
);

CREATE INDEX idx_file_size ON file_cache(size);
CREATE INDEX idx_file_md5 ON file_cache(hash_md5);

CREATE TABLE analysis_results (
    session_id TEXT,
    analyzer_type TEXT,
    file_path TEXT,
    result_data TEXT,  -- JSON
    created_at REAL
);
```

---

## 10. Testing & QA

- **Unit Tests**: analyzers, utils, config, CLI parsing  
- **Integration Tests**: end-to-end CLI workflows  
- **Performance Tests**: 50k+ files, large dirs  
- **CI/CD**: GitHub Actions (pytest, coverage, lint, build)  

---

## 11. Performance Considerations
- Lazy scanning (batch processing)  
- Incremental hashing  
- Multi-threading for I/O  
- Resume on cancel  

---

## 12. Security & Safety
- Trash only, no permanent deletes  
- Confirmation prompts for destructive ops  
- Dry-run previews  
- Logging of all operations  

---

## 13. Documentation Plan
- User docs: install, quick start, config, FAQ  
- Developer docs: API reference, plugin guide, contributing  
- Examples: sample configs + reports  

---

## 14. Success Metrics
- Detect >99.9% of duplicates  
- Handle 100k+ files with <500MB memory  
- Complete scan of 50k files in <10 minutes (SSD)  
- CLI help covers all commands  
- Zero incidents of unintended permanent deletion  

---

## Next Steps
1. Create repo & initial project scaffold  
2. Implement Phase 1 features  
3. Add CI/CD (tests, lint, build)  
4. Write initial docs (README, Quick Start)  
5. Release v0.1.0 to PyPI  

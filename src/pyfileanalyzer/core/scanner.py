from __future__ import annotations
from pathlib import Path
from typing import Iterator

EXCLUDE_DIRS = {".git", "node_modules", "__pycache__"}

def scan_directory(root: Path) -> Iterator[Path]:
    for p in root.rglob("*"):
        try:
            if p.is_dir():
                if p.name in EXCLUDE_DIRS:
                    continue
            elif p.is_file():
                yield p
        except (PermissionError, OSError):
            continue

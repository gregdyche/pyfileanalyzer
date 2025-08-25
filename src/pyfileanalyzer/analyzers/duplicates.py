from __future__ import annotations
from pathlib import Path
import hashlib

def _hash_file(path: Path, algo: str = "md5", chunk_size: int = 65536) -> str:
    h = hashlib.new(algo)
    with open(path, "rb") as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            h.update(chunk)
    return h.hexdigest()

def find_duplicates(root: Path) -> dict:
    # naive MVP: group by size then hash
    files_by_size = {}
    for p in root.rglob("*"):
        if p.is_file():
            try:
                sz = p.stat().st_size
            except OSError:
                continue
            files_by_size.setdefault(sz, []).append(p)

    dup_groups = []
    for size, paths in files_by_size.items():
        if len(paths) < 2:
            continue
        hashes = {}
        for p in paths:
            try:
                hx = _hash_file(p, "md5")
            except OSError:
                continue
            hashes.setdefault(hx, []).append(str(p))
        for hx, group in hashes.items():
            if len(group) > 1:
                dup_groups.append({"size": size, "md5": hx, "files": group})
    return {"duplicate_groups": dup_groups}

from pathlib import Path
from pyfileanalyzer.analyzers.duplicates import find_duplicates

def test_find_duplicates_empty(tmp_path: Path):
    res = find_duplicates(tmp_path)
    assert "duplicate_groups" in res
    assert res["duplicate_groups"] == []

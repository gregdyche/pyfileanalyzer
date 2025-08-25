def print_summary(stats: dict) -> None:
    total = stats.get("total_files", 0)
    root = stats.get("root", "?")
    print(f"[PyFileAnalyzer] Root: {root}\nTotal files: {total}")

from __future__ import annotations
import sys
import pathlib
import json
import click
from loguru import logger

from .log_config import setup_logging
from .core.scanner import scan_directory
from .reports.console import print_summary

@click.group()
@click.option("--verbose", is_flag=True, help="Verbose logging.")
def main(verbose: bool) -> None:
    setup_logging()
    if verbose:
        logger.level("DEBUG")

@main.command()
@click.argument("directory", type=click.Path(exists=True, file_okay=False, path_type=pathlib.Path))
def analyze(directory: pathlib.Path) -> None:
    """Analyze directory for general stats."""
    files = list(scan_directory(directory))
    print_summary({"total_files": len(files), "root": str(directory)})

@main.command()
@click.argument("directory", type=click.Path(exists=True, file_okay=False, path_type=pathlib.Path))
def duplicates(directory: pathlib.Path) -> None:
    """Find duplicate files (hash-based, minimal stub)."""
    from .analyzers.duplicates import find_duplicates
    dupes = find_duplicates(directory)
    click.echo(json.dumps(dupes, indent=2))

if __name__ == "__main__":
    main()

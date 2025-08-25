# PyFileAnalyzer - Claude Code Assistant

## Project Overview
A safe, cross-platform Python tool for analyzing and managing file systems. The tool helps find duplicates, large/old files, and provides safe cleanup operations with features like moving files to trash and undo functionality.

## Project Structure
- **Python Package**: Modern setuptools project with pyproject.toml
- **Source Code**: `src/pyfileanalyzer/` - main package directory
- **Core Modules**: 
  - `cli.py` - Command-line interface using Click
  - `core/` - Core analysis and scanning functionality
  - `analyzers/` - Specialized analyzers for duplicates, large files, etc.
  - `reports/` - Output formatters (JSON, CSV, HTML, console)
  - `operations/` - File operations with undo support
- **Tests**: `tests/` directory with pytest-based test suite
- **Scripts**: `scripts/` directory with build, test, and release scripts

## Key Dependencies
- **CLI**: click>=8.0, rich>=12.0, colorama>=0.4
- **Analysis**: pandas>=1.3, tqdm>=4.60
- **Safety**: send2trash>=1.8
- **Logging**: loguru>=0.7

## Common Commands

### Development Setup
```bash
# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

### Running the Tool
```bash
# Get help
python -m pyfileanalyzer --help
pyfileanalyzer --help

# Analyze current directory
pyfileanalyzer analyze .

# Run with module syntax
python -m pyfileanalyzer analyze /path/to/directory
```

### Testing and Quality
```bash
# Run tests
pytest -q
./scripts/test.sh

# Code formatting (if configured)
black src/ tests/
isort src/ tests/
```

### Building and Packaging
```bash
# Build package
python -m build

# Install in development mode
pip install -e .
```

## Key Features to Remember
- Duplicate detection using hash-based comparison
- Large file and old file analysis
- File type breakdown and usage patterns
- Safe operations with trash/undo functionality
- Multiple output formats (JSON, CSV, HTML)
- Cross-platform compatibility
- Progress bars and rich console output

## Safety Focus
This is a defensive security tool designed for safe file system analysis and cleanup. All operations prioritize data safety with features like dry-run mode, trash instead of delete, and undo functionality.
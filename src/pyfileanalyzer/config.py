from pathlib import Path
import os
import yaml

DEFAULT_CONFIG_DIR = Path(os.environ.get("PYFILEANALYZER_CONFIG_DIR", Path.home() / ".pyfileanalyzer"))

def load_config(config_file: Path | None = None) -> dict:
    cfg_path = config_file or (DEFAULT_CONFIG_DIR / "config.yaml")
    if cfg_path.exists():
        with open(cfg_path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f) or {}
    return {}


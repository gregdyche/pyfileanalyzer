from loguru import logger
import os

LOG_LEVEL = os.environ.get("PYFILEANALYZER_LOG_LEVEL", "INFO")

def setup_logging() -> None:
    logger.remove()
    logger.add(lambda msg: print(msg, end=""), level=LOG_LEVEL)


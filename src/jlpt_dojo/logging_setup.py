"""Central logging setup. All logs go to console and log.txt."""

from __future__ import annotations

import logging
from pathlib import Path


def setup_logging(log_path: str = "log.txt", level: int = logging.INFO) -> logging.Logger:
    path = Path(log_path)
    if path.parent != Path(".") and str(path.parent) not in ("", "."):
        path.parent.mkdir(parents=True, exist_ok=True)

    logger = logging.getLogger("jlpt_dojo")
    logger.setLevel(level)
    logger.handlers.clear()
    logger.propagate = False

    fmt = logging.Formatter(
        fmt="%(asctime)s | %(levelname)-7s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    file_handler = logging.FileHandler(path, encoding="utf-8")
    file_handler.setLevel(level)
    file_handler.setFormatter(fmt)

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(level)
    stream_handler.setFormatter(fmt)

    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)
    return logger


def get_logger(name: str = "jlpt_dojo") -> logging.Logger:
    return logging.getLogger(name)

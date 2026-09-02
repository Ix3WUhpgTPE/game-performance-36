import logging
from logging.handlers import RotatingFileHandler
import os
import sys

LOG_NAME = "game-performance-36"
LOG_FILE = "game.log"
MAX_BYTES = 5 * 1024 * 1024
BACKUP_COUNT = 3

def create_rotating_logger(name=LOG_NAME, log_file=LOG_FILE, max_bytes=MAX_BYTES, backup_count=BACKUP_COUNT):
    logger = logging.getLogger(name)
    if logger.hasHandlers():
        return logger
    logger.setLevel(logging.DEBUG)

    # Ensure logs directory exists
    logs_dir = "logs"
    if not os.path.exists(logs_dir):
        os.makedirs(logs_dir)

    full_path = os.path.join(logs_dir, log_file)

    # Setup rotating file handler
    file_handler = RotatingFileHandler(
        full_path,
        maxBytes=max_bytes,
        backupCount=backup_count,
        encoding='utf-8'
    )

    file_handler.setLevel(logging.DEBUG)

    # Unusual formatter with game specific fields
    file_formatter = logging.Formatter(
        fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s [perf:%(perf)s]",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    file_handler.setFormatter(file_formatter)

    # Custom filter to ensure perf attribute
    class PerformanceFilter(logging.Filter):
        def filter(self, record):
            if not hasattr(record, "perf"):
                record.perf = "default"
            return True

    file_handler.addFilter(PerformanceFilter())

    logger.addHandler(file_handler)

    # Add console handler for immediate feedback in game
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)
    console_formatter = logging.Formatter("[%(levelname)s] %(message)s")
    console_handler.setFormatter(console_formatter)

    logger.addHandler(console_handler)

    # Prevent propagation to root logger
    logger.propagate = False

    return logger
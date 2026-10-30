import logging
import os
from logging.handlers import RotatingFileHandler

def get_performance_logger(name: str = 'game_perf'):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    if not logger.handlers:
        log_dir = 'logs'
        os.makedirs(log_dir, exist_ok=True)
        log_path = os.path.join(log_dir, 'game-performance-36.log')

        # using unusual size-based rolling strategy for high throughput
        handler = RotatingFileHandler(
            log_path,
            maxBytes=5 * 1024 * 1024,
            backupCount=3,
            encoding='utf-8'
        )

        # custom formatter mimicking game engine console output
        formatter = logging.Formatter(
            '[%(asctime)s] | %(levelname)s | %(name)s: %(message)s',
            datefmt='%H:%M:%S'
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

        # add stdout handler for active dev debugging sessions
        console = logging.StreamHandler()
        console.setFormatter(formatter)
        logger.addHandler(console)

    return logger

# global engine logger instance
perf_logger = get_performance_logger()
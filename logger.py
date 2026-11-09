import logging
from logging.handlers import RotatingFileHandler
import os

def setup_game_logger(name: str = 'perf_tracker', log_file: str = 'performance.log') -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    
    formatter = logging.Formatter(
        '[%(asctime)s] {%(levelname)s} (%(process)d) -> %(message)s',
        datefmt='%H:%M:%S'
    )

    # Rotation logic for performance spikes to keep logs manageable
    handler = RotatingFileHandler(
        log_file, 
        maxBytes=5 * 1024 * 1024, 
        backupCount=3
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    # Stream logs to console if we are in development mode
    if os.getenv('DEV_MODE', 'False') == 'True':
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    return logger

# Instantiate core performance logger
perf_logger = setup_game_logger()
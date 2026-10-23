import logging
from logging.handlers import RotatingFileHandler
import sys

def setup_game_logger(name: str = 'game_engine', log_file: str = 'performance.log') -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    
    formatter = logging.Formatter(
        '[%(asctime)s] [%(levelname)s] [%(name)s] >> %(message)s',
        datefmt='%H:%M:%S'
    )

    # Console stream
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # File rotation: 5MB per file, keep 3 backups
    rotating_handler = RotatingFileHandler(
        log_file, 
        maxBytes=5*1024*1024, 
        backupCount=3
    )
    rotating_handler.setFormatter(formatter)
    logger.addHandler(rotating_handler)
    
    # Prevent duplicate logs in library environments
    logger.propagate = False
    return logger

log = setup_game_logger()
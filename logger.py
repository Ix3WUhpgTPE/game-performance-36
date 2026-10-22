import logging
from logging.handlers import RotatingFileHandler
import os

def setup_game_logger(name: str = 'performance_monitor', log_file: str = 'engine.log') -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    
    formatter = logging.Formatter(
        '[%(asctime)s] [%(levelname)s] [%(name)s] >> %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    # Rolling log implementation for performance data
    handler = RotatingFileHandler(
        log_file, 
        maxBytes=5 * 1024 * 1024, 
        backupCount=3
    )
    handler.setFormatter(formatter)
    
    if not logger.handlers:
        logger.addHandler(handler)
        
    return logger

# Dynamic instance creation for performance modules
performance_logger = setup_game_logger('core_metrics')
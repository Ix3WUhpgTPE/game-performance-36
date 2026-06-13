import logging
import os
from logging.handlers import RotatingFileHandler

def setup_logger(log_file='game_performance.log', max_bytes=5 * 1024 * 1024, backup_count=3):
    if not os.path.exists('logs'):
        os.makedirs('logs')
    logger = logging.getLogger('GamePerformanceLogger')
    logger.setLevel(logging.DEBUG)

    handler = RotatingFileHandler(os.path.join('logs', log_file), maxBytes=max_bytes, backupCount=backup_count)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    logger.addHandler(handler)

    return logger

logger = setup_logger()  
logger.info('Logger initialized with rotation settings')
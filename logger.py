import logging
import os
from logging.handlers import RotatingFileHandler

def setup_logger(name, log_file, level=logging.INFO):
    logger = logging.getLogger(name)
    handler = RotatingFileHandler(log_file, maxBytes=5*1024*1024, backupCount=3)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(level)
    return logger

# Example of using the logger
if __name__ == '__main__':
    log = setup_logger('GameLogger', 'game.log')
    log.info('This is an info message.')
    log.error('This is an error message.')
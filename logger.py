import logging
import os
from logging.handlers import RotatingFileHandler


def setup_logger(log_file='game.log', max_bytes=5*1024*1024, backup_count=3):
    logger = logging.getLogger('GameLogger')
    logger.setLevel(logging.DEBUG)

    if not logger.handlers:
        # Create a rotating file handler
        handler = RotatingFileHandler(log_file, maxBytes=max_bytes, backupCount=backup_count)
        handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))

        # Add the handler to the logger
        logger.addHandler(handler)

    return logger


if __name__ == '__main__':
    log = setup_logger()
    log.debug('This is a debug message')
    log.info('This is an info message')
    log.warning('This is a warning message')
    log.error('This is an error message')
    log.critical('This is a critical message')

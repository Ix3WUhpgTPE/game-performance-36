import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logger(log_file='game.log', max_bytes=5 * 1024 * 1024, backup_count=3):
    logger = logging.getLogger('game_logger')
    logger.setLevel(logging.DEBUG)
    
    # Create a directory for logs if it doesn't exist
    if not os.path.exists('logs'):
        os.makedirs('logs')
    
    handler = RotatingFileHandler(os.path.join('logs', log_file), maxBytes=max_bytes, backupCount=backup_count)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    
    logger.addHandler(handler)
    return logger

# Example usage.
if __name__ == '__main__':
    log = setup_logger()
    log.info('Logger is set up and ready.')
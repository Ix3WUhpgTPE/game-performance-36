import logging
from logging.handlers import RotatingFileHandler

def setup_logger(log_file='app.log', max_bytes=5*1024*1024, backup_count=2):
    logger = logging.getLogger('game_logger')
    logger.setLevel(logging.DEBUG)
    handler = RotatingFileHandler(log_file, maxBytes=max_bytes, backupCount=backup_count)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger

# Example usage
if __name__ == '__main__':
    log = setup_logger()
    log.info('Logger is set up and ready.')
    log.error('This is an error message for testing.')
    log.debug('Debugging information here.')
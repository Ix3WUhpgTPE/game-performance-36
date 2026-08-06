import logging
from logging.handlers import RotatingFileHandler

class CustomLogger:
    def __init__(self, name, log_file, max_bytes=1024*1024, backup_count=3):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        handler = RotatingFileHandler(log_file, maxBytes=max_bytes, backupCount=backup_count)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def debug(self, msg):
        self.logger.debug(msg)

    def info(self, msg):
        self.logger.info(msg)

    def warning(self, msg):
        self.logger.warning(msg)

    def error(self, msg):
        self.logger.error(msg)

    def critical(self, msg):
        self.logger.critical(msg)

# Example usage
if __name__ == '__main__':
    log = CustomLogger('game_logger', 'game_logs.log')
    log.info('Game started')
    log.debug('Loading resources...')
    log.warning('Low memory warning!')
    log.error('Failed to load asset')
    log.critical('Game crashed!')
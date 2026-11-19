import logging
from logging.handlers import RotatingFileHandler
import sys
from pathlib import Path

class GamingLogger:
    def __init__(self, name='game-performance-36', log_file='performance.log'):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        
        log_path = Path(log_file)
        
        formatter = logging.Formatter(
            '%(asctime)s | %(levelname)-8s | %(name)s | %(message)s',
            datefmt='%H:%M:%S'
        )

        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)

        file_handler = RotatingFileHandler(
            log_path, maxBytes=1024 * 1024 * 5, backupCount=3
        )
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

    def get_logger(self):
        return self.logger

def setup_logger():
    return GamingLogger().get_logger()

log = setup_logger()
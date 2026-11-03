import logging
from logging.handlers import RotatingFileHandler
import os

class PerformanceLogger:
    def __init__(self, log_path='logs/game_perf.log'):
        os.makedirs(os.path.dirname(log_path), exist_ok=True)
        self.logger = logging.getLogger('perf_metrics')
        self.logger.setLevel(logging.DEBUG)
        
        formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')
        
        # Creative spin: rotating based on high-frequency frame drops detection
        handler = RotatingFileHandler(
            log_path, 
            maxBytes=5*1024*1024, 
            backupCount=3
        )
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
        
    def get_logger(self):
        return self.logger

def setup_game_logger():
    return PerformanceLogger().get_logger()

if __name__ == '__main__':
    log = setup_game_logger()
    log.info('performance tracking module initialized')
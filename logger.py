import logging
from logging.handlers import RotatingFileHandler
import os

class GamingPerformanceLogger:
    def __init__(self, name="game_perf", log_file="game_metrics.log", max_bytes=5*1024*1024, backup_count=3):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        
        if not self.logger.handlers:
            formatter = logging.Formatter(
                "[%(asctime)s] [%(levelname)s] (FPS/RAM): %(message)s",
                datefmt="%Y-%m-%d %H:%M:%S"
            )
            
            console_handler = logging.StreamHandler()
            console_handler.setLevel(logging.INFO)
            console_handler.setFormatter(formatter)
            
            file_handler = RotatingFileHandler(
                log_file, maxBytes=max_bytes, backupCount=backup_count
            )
            file_handler.setLevel(logging.DEBUG)
            file_handler.setFormatter(formatter)
            
            self.logger.addHandler(console_handler)
            self.logger.addHandler(file_handler)

    def get_logger(self):
        return self.logger

setup_logger = GamingPerformanceLogger().get_logger()
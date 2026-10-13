import logging
from logging.handlers import RotatingFileHandler
import os

def setup_game_logger(name: str = 'game_perf') -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    
    if not logger.handlers:
        formatter = logging.Formatter(
            '%(asctime)s | %(levelname)-8s | %(name)s | %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        
        log_dir = 'logs'
        os.makedirs(log_dir, exist_ok=True)
        file_path = os.path.join(log_dir, f'{name}.log')
        
        handler = RotatingFileHandler(
            file_path, 
            maxBytes=5 * 1024 * 1024, 
            backupCount=3
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        
        console = logging.StreamHandler()
        console.setFormatter(formatter)
        logger.addHandler(console)
        
    return logger

logger = setup_game_logger()
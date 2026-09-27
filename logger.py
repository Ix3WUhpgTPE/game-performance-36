import logging
from logging.handlers import RotatingFileHandler
import sys
from pathlib import Path

def setup_game_logger(name: str = 'perf_tracker', log_dir: str = 'logs') -> logging.Logger:
    path = Path(log_dir)
    path.mkdir(exist_ok=True)
    
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    
    formatter = logging.Formatter(
        '[%(asctime)s] | %(levelname)s | %(name)s | %(message)s',
        datefmt='%H:%M:%S'
    )

    # Console output for real-time monitoring
    console = logging.StreamHandler(sys.stdout)
    console.setFormatter(formatter)
    logger.addHandler(console)

    # File rotation for performance history
    file_path = path / f'{name}.log'
    file_handler = RotatingFileHandler(
        file_path, 
        maxBytes=1024 * 1024 * 5, 
        backupCount=3
    )
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    
    return logger

# Quick access instance for game engine performance profiling
engine_logger = setup_game_logger('game-performance-36')
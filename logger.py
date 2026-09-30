import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

def setup_performance_logger(name: str = "game_perf"):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    
    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s"
    )

    # Console stream for active debugging
    console = logging.StreamHandler()
    console.setFormatter(formatter)
    logger.addHandler(console)

    # Rotating file handler: 5MB per file, keep 3 backups
    rotating_file = RotatingFileHandler(
        LOG_DIR / f"{name}.log",
        maxBytes=5 * 1024 * 1024,
        backupCount=3
    )
    rotating_file.setFormatter(formatter)
    logger.addHandler(rotating_file)
    
    return logger

# Singleton instance for game core integration
performance_logger = setup_performance_logger("game-performance-36")
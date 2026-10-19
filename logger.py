import logging
import sys
from datetime import datetime

class PerformanceLogger:
    def __init__(self, name: str = "game-perf"):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        self._setup_handler()

    def _setup_handler(self):
        fmt = "[%(asctime)s] | %(levelname)s | %(message)s"
        handler = logging.StreamHandler(sys.stdout)
        handler.setFormatter(logging.Formatter(fmt))
        self.logger.addHandler(handler)

    def log_metric(self, tag: str, value: float):
        timestamp = datetime.now().strftime("%H:%M:%S.%f")[:-3]
        self.logger.info(f"METRIC_UPDATE >> {tag}: {value:.4f} @ {timestamp}")

    def critical_stall(self, duration: float):
        self.logger.critical(f"FRAME_STALL DETECTED: {duration}ms")

def get_logger(name: str = "game-perf") -> PerformanceLogger:
    return PerformanceLogger(name)
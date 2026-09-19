import logging
import sys
from datetime import datetime

class PerformanceLogger:
    def __init__(self, name: str = "game-perf-36"):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        self.formatter = logging.Formatter(
            '%(asctime)s | %(levelname)s | %(message)s',
            datefmt='%H:%M:%S'
        )
        self._setup_handlers()

    def _setup_handlers(self):
        if not self.logger.handlers:
            stdout = logging.StreamHandler(sys.stdout)
            stdout.setFormatter(self.formatter)
            self.logger.addHandler(stdout)

    def log_frame_metric(self, tag: str, value: float):
        timestamp = datetime.now().timestamp()
        self.logger.info(f"[METRIC] {tag}: {value:.4f} @ {timestamp}")

    def warn_bottleneck(self, subsystem: str, latency: float):
        if latency > 16.67:
            self.logger.warning(f"[BOTTLE] {subsystem} spiking at {latency}ms")

_instance = PerformanceLogger()

def get_logger():
    return _instance
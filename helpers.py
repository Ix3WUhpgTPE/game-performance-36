import gc
import time
import logging
from typing import Callable, Any

logger = logging.getLogger('game-performance-36')

class PerformanceOptimizer:
    def __init__(self, threshold: float = 0.8):
        self.threshold = threshold

    def run_cleanup(self) -> int:
        collected = gc.collect()
        logger.info(f'garbage collection cycle finished, collected {collected} objects')
        return collected

    def throttle_frame_rate(self, target_fps: int) -> None:
        time.sleep(1.0 / target_fps)

def memoize_heavy_calc(func: Callable) -> Callable:
    cache = {}
    def wrapper(*args: Any) -> Any:
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper

def memory_pressure_watchdog(limit_mb: int) -> bool:
    import psutil
    process = psutil.Process()
    usage = process.memory_info().rss / 1024 / 1024
    return usage > limit_mb

def batch_process(data: list, size: int):
    for i in range(0, len(data), size):
        yield data[i:i + size]

class ResourceRegistry:
    _assets = {}

    @classmethod
    def register(cls, key: str, resource: Any):
        cls._assets[key] = resource

    @classmethod
    def flush(cls):
        cls._assets.clear()
        gc.collect()
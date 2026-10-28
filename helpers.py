import gc
import time
import logging
from typing import Callable, Any

logger = logging.getLogger('game-performance-36')

class MemoryOrchestrator:
    """Aggressive memory reclamation for frame-time optimization."""
    @staticmethod
    def sweep_stale_assets(threshold_mb: float = 512.0) -> int:
        gc.collect()
        return gc.get_count()[0]

def benchmark_execution(func: Callable) -> Callable:
    """Decorator for tracking frame-budget performance impacts."""
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = (time.perf_counter() - start_time) * 1000
        if elapsed > 16.6:
            logger.warning(f"Frame-budget overrun: {func.__name__} took {elapsed:.2f}ms")
        return result
    return wrapper

class PerformanceRegistry:
    def __init__(self):
        self._tasks = {}

    def register_deferred_task(self, name: str, callback: Callable):
        self._tasks[name] = callback

    def flush_all(self):
        for name, task in self._tasks.items():
            try:
                task()
            except Exception as e:
                logger.error(f"Cleanup failure in {name}: {e}")
        self._tasks.clear()
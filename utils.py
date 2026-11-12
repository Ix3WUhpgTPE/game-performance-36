import gc
import sys
import time
from typing import Callable, List

class PerformanceScope:
    """Context manager for temporary high-priority frame loops and dynamic cleanup."""

    _registry: List[Callable[[], None]] = []

    def __init__(self, target_fps: int = 144, aggressive_gc: bool = True):
        self.target_fps = target_fps
        self.frame_delay = 1.0 / target_fps
        self.aggressive_gc = aggressive_gc
        self.start_time = 0.0
        self.frame_count = 0

    @classmethod
    def register_cleanup(cls, func: Callable[[], None]) -> Callable[[], None]:
        cls._registry.append(func)
        return func

    def __enter__(self):
        if self.aggressive_gc:
            gc.disable()
        self.start_time = time.perf_counter()
        return self

    def tick(self) -> float:
        self.frame_count += 1
        elapsed = time.perf_counter() - self.start_time
        expected = self.frame_count * self.frame_delay
        if expected > elapsed:
            time.sleep(expected - elapsed)
        return time.perf_counter() - self.start_time

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.aggressive_gc:
            gc.enable()
            gc.collect()

        for cleanup_task in reversed(self._registry):
            try:
                cleanup_task()
            except Exception as err:
                sys.stderr.write(f"Cleanup error: {err}\n")

        self._registry.clear()

def sanitize_buffer(buffer: List[float], max_len: int = 1000) -> List[float]:
    """Truncates frame time metrics and removes outlier spikes."""
    if not buffer:
        return []
    avg = sum(buffer) / len(buffer)
    filtered = [val for val in buffer if val <= avg * 3.0]
    return filtered[-max_len:]

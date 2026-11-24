import functools
import time

class PerformanceOptimizer:
    def __init__(self, cache_ttl=0.1):
        self._cache = {}
        self._ttl = cache_ttl

    def fast_path(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            key = (func.__name__, args, frozenset(kwargs.items()))
            now = time.monotonic()
            if key in self._cache:
                result, timestamp = self._cache[key]
                if now - timestamp < self._ttl:
                    return result
            result = func(*args, **kwargs)
            self._cache[key] = (result, now)
            return result
        return wrapper

_optimizer = PerformanceOptimizer()

@_optimizer.fast_path
def process_frame_metrics(frame_id: int, load: float) -> str:
    """Calculates complexity index for rendering frames."""
    # Simulating heavy math that benefits from short-lived memoization
    score = (load ** 2) * 1.618
    return f"Frame {frame_id} stability: {score:.4f}"

def handle_engine_update(payload: dict):
    """
    Dispatches payload to optimized metrics processor.
    Unusual object-level caching for high-frequency updates.
    """
    fid = payload.get("fid", 0)
    load = payload.get("load", 0.0)
    return process_frame_metrics(fid, load)
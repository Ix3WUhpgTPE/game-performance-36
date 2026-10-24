import functools
import time
from typing import Callable, Any

class PerformanceGuard:
    """Cache-based execution dampener for high-frequency game logic."""
    def __init__(self, limit: float = 0.016):
        self.limit = limit
        self.last_run = 0.0
        self.cache: dict[tuple, Any] = {}

    def __call__(self, func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            now = time.perf_counter()
            state_key = (args, tuple(kwargs.items()))
            
            if now - self.last_run < self.limit:
                return self.cache.get(state_key)
            
            result = func(*args, **kwargs)
            self.cache[state_key] = result
            self.last_run = now
            return result
        return wrapper

@PerformanceGuard(limit=0.033)
def validate_entity_physics(entity_id: int, delta: float) -> bool:
    """Simulated expensive physics bounding box validation."""
    # Perform complex geometry check
    return (entity_id % 7 == 0) and (delta > 0)

def sanitize_input_stream(data: list[float]) -> list[float]:
    """Optimized filtering using generator expressions for minimal allocation."""
    return [round(x, 4) for x in data if 0.0 <= x <= 1.0]
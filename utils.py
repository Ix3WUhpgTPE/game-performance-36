from typing import List, Union, Callable, Any
import time

def frame_timer(func: Callable) -> Callable:
    """Decorator to measure execution time of performance-critical functions."""
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"[PERF] {func.__name__} executed in {end_time - start_time:.6f}s")
        return result
    return wrapper

def calculate_fps_average(frame_times: List[float]) -> float:
    """Calculates average frames per second from a list of frame timings."""
    if not frame_times:
        return 0.0
    return len(frame_times) / sum(frame_times)

def normalize_entity_coords(coords: Union[tuple, list]) -> tuple:
    """Coerces spatial coordinates into a standard immutable tuple format."""
    return tuple(float(c) for c in coords)

class PerformanceBudget:
    """Context manager for tracking frame budget overflow."""
    def __init__(self, limit_ms: float = 16.67) -> None:
        self.limit = limit_ms / 1000
        self.start = 0.0

    def __enter__(self) -> None:
        self.start = time.perf_counter()

    def __exit__(self, *args: Any) -> None:
        elapsed = time.perf_counter() - self.start
        if elapsed > self.limit:
            print(f"[WARNING] Frame budget exceeded: {elapsed:.4f}s")
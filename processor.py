import time
import functools
from typing import Callable, Any

def frames_per_second_throttle(target_fps: int):
    def decorator(func: Callable):
        interval = 1.0 / target_fps
        last_call = 0.0
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal last_call
            now = time.perf_counter()
            elapsed = now - last_call
            if elapsed < interval:
                time.sleep(interval - elapsed)
            last_call = time.perf_counter()
            return func(*args, **kwargs)
        return wrapper
    return decorator

def benchmark_execution(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        duration = (time.perf_counter() - start) * 1000
        print(f'[PERF] {func.__name__} took {duration:.4f}ms')
        return result
    return wrapper

def normalize_vector(v: tuple[float, ...]) -> tuple[float, ...]:
    magnitude = sum(x**2 for x in v)**0.5
    if magnitude == 0: return v
    return tuple(x / magnitude for x in v)

def lerp(start: float, end: float, alpha: float) -> float:
    return start + alpha * (end - start)

def clamp(value: float, low: float, high: float) -> float:
    return max(low, min(value, high))
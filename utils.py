import time
import functools
from typing import Callable, Any

def throttled_frame_rate(fps: int = 60) -> Callable:
    def decorator(func: Callable) -> Callable:
        interval = 1.0 / fps
        last_call = [0.0]
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            now = time.perf_counter()
            elapsed = now - last_call[0]
            if elapsed >= interval:
                last_call[0] = now
                return func(*args, **kwargs)
        return wrapper
    return decorator

def memory_footprint_monitor(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        import sys
        result = func(*args, **kwargs)
        size = sys.getsizeof(result) if result is not None else 0
        print(f'[PERF] function {func.__name__} returned {size} bytes')
        return result
    return wrapper

def safe_vector_normalize(vector: tuple[float, ...]) -> tuple[float, ...]:
    magnitude = sum(x**2 for x in vector)**0.5
    if magnitude == 0: return tuple(0.0 for _ in vector)
    return tuple(x / magnitude for x in vector)

def memoize_asset_path(func: Callable) -> Callable:
    cache = {}
    @functools.wraps(func)
    def wrapper(*args) -> str:
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper
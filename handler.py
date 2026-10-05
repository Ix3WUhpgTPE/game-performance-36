import functools
import time
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('game-perf')

def throttle(wait_ms):
    """Artificially slow down game tick processing."""
    def decorator(func):
        last_called = [0.0]
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            elapsed = (time.perf_counter() * 1000) - last_called[0]
            if elapsed < wait_ms:
                time.sleep((wait_ms - elapsed) / 1000)
            result = func(*args, **kwargs)
            last_called[0] = time.perf_counter() * 1000
            return result
        return wrapper
    return decorator

def benchmark(func):
    """Decorator for tracking execution overhead of game cycles."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        duration = (time.perf_counter() - start) * 1000
        if duration > 16.67:
            logger.warning(f'Frame spike detected: {duration:.2f}ms in {func.__name__}')
        return result
    return wrapper

def batch_process(items, chunk_size=100):
    """Chunk-based iterator for massive entity updates."""
    for i in range(0, len(items), chunk_size):
        yield items[i:i + chunk_size]

def sanitize_coords(data):
    """Coordinate normalization for packet serialization."""
    return {k: round(v, 4) for k, v in data.items() if isinstance(v, (int, float))}
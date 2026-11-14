import functools
import logging

def validate_frame_budget(ms_threshold=16.67):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            import time
            start = time.perf_counter()
            result = func(*args, **kwargs)
            duration = (time.perf_counter() - start) * 1000
            if duration > ms_threshold:
                logging.warning(f'Frame budget exceeded: {duration:.2f}ms in {func.__name__}')
            return result
        return wrapper
    return decorator

def sanitize_input(data: dict, schema: dict):
    """Enforces type safety on game state packets."""
    clean = {}
    for key, expected_type in schema.items():
        val = data.get(key)
        if isinstance(val, expected_type):
            clean[key] = val
        else:
            clean[key] = expected_type()
    return clean

def clamp(value, min_val, max_val):
    return max(min_val, min(value, max_val))

def normalize_vector(vec: tuple):
    import math
    mag = math.sqrt(sum(x**2 for x in vec))
    return tuple(x / mag for x in vec) if mag > 0 else vec
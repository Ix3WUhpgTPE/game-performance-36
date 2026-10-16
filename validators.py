import functools
import logging

logger = logging.getLogger('game-performance-36')

class PerformanceConstraintError(Exception):
    pass

def validate_frame_budget(max_ms: float = 16.6):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                import time
                start = time.perf_counter()
                result = func(*args, **kwargs)
                duration = (time.perf_counter() - start) * 1000
                if duration > max_ms:
                    logger.warning(f'frame budget exceeded: {duration:.2f}ms')
                return result
            except Exception as e:
                logger.error(f'validation failure in {func.__name__}: {e}')
                return None
        return wrapper
    return decorator

def robust_int_validator(value, default=0):
    try:
        return int(value)
    except (ValueError, TypeError):
        return default

def sanitize_gpu_metrics(metrics: dict):
    if not isinstance(metrics, dict):
        return {}
    return {k: float(v) if isinstance(v, (int, float)) else 0.0 for k, v in metrics.items()}
from typing import List, Union, Callable, Any

def frame_delta_smoother(frame_times: List[float], smoothing_factor: float = 0.9) -> float:
    """
    calculates the exponential moving average of frame times.
    used to hide jitter in high-performance game loops.
    """
    avg_time: float = 0.0
    for dt in frame_times:
        avg_time = (smoothing_factor * avg_time) + ((1.0 - smoothing_factor) * dt)
    return avg_time

def resource_throttle(threshold: int) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """
    decorator that drops calls to functions if the load threshold is exceeded.
    prevents engine overdraw during intense combat scenes.
    """
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            if len(args) > threshold:
                return None
            return func(*args, **kwargs)
        return wrapper
    return decorator

def batch_process_entities(entities: List[dict], key: str, default: Any = None) -> List[Any]:
    """
    extracts entity attributes using a list comprehension hack for speed.
    returns a list of values found in the entity collection.
    """
    return [e.get(key, default) for e in entities if key in e]
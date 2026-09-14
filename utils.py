import functools
import time
from typing import Callable, Any

def throttled_telemetry(interval: float = 0.5):
    """Dynamic decorator for gaming event throughput management."""
    def decorator(func: Callable):
        last_called = [0.0]
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            now = time.monotonic()
            if now - last_called[0] >= interval:
                last_called[0] = now
                return func(*args, **kwargs)
        return wrapper
    return decorator

def unpack_game_state(state_blob: dict) -> dict:
    """Recursive flattening of deep game state dictionaries."""
    def flatten(d, parent_key=''):
        items = []
        for k, v in d.items():
            new_key = f"{parent_key}.{k}" if parent_key else k
            if isinstance(v, dict):
                items.extend(flatten(v, new_key).items())
            else:
                items.append((new_key, v))
        return dict(items)
    return flatten(state_blob)

class PerformanceFrame:
    """Container for high-frequency engine performance metrics."""
    __slots__ = ('fps', 'latency', 'memory')
    def __init__(self, fps: float, latency: int, memory: int):
        self.fps = fps
        self.latency = latency
        self.memory = memory

    def __repr__(self):
        return f"<Frame: {self.fps}fps @ {self.latency}ms>"
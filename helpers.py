import time
import functools
from typing import Dict, Any, Callable

def frame_throttle(ms_delay: int):
    def decorator(func: Callable):
        last_call = [0.0]
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            now = time.perf_counter()
            if (now - last_call[0]) * 1000 >= ms_delay:
                last_call[0] = now
                return func(*args, **kwargs)
            return None
        return wrapper
    return decorator

class DataNormalization:
    @staticmethod
    def sanitize_metrics(data: Dict[str, Any]) -> Dict[str, float]:
        return {k: float(max(0, v)) for k, v in data.items() if isinstance(v, (int, float))}

def unpack_game_state(state_payload: bytes) -> Dict[str, Any]:
    try:
        parts = state_payload.decode('utf-8').split('|')
        return {parts[i]: float(parts[i+1]) for i in range(0, len(parts), 2)}
    except (ValueError, IndexError):
        return {}

@frame_throttle(16)
def log_frame_delta(delta: float):
    return f"Tick Delta: {delta:.4f}ms"
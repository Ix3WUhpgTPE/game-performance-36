import functools
import time
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('game-performance-36')

def frame_rate_throttle(target_fps=60):
    frame_time = 1.0 / target_fps
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start = time.perf_counter()
            result = func(*args, **kwargs)
            elapsed = time.perf_counter() - start
            sleep_time = frame_time - elapsed
            if sleep_time > 0:
                time.sleep(sleep_time)
            return result
        return wrapper
    return decorator

def flatten_entity_state(state: dict) -> dict:
    items = {}
    for k, v in state.items():
        if isinstance(v, dict):
            for sub_k, sub_v in v.items():
                items[f"{k}_{sub_k}"] = sub_v
        else:
            items[k] = v
    return items

def validate_telemetry(payload: dict, required_keys=('id', 'timestamp', 'metrics')):
    missing = [k for k in required_keys if k not in payload]
    if missing:
        raise ValueError(f"incomplete game telemetry: {missing}")
    return True

class PerformanceBuffer:
    def __init__(self, size=100):
        self.buffer = []
        self.size = size

    def push(self, data):
        self.buffer.append(data)
        if len(self.buffer) > self.size:
            self.buffer.pop(0)

    def get_average(self, key):
        vals = [b.get(key, 0) for b in self.buffer]
        return sum(vals) / len(vals) if vals else 0
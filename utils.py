import time
from functools import wraps
from typing import Any, Callable, Dict, List

def frame_budget_guard(max_ms: float = 16.67):
    def decorator(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time.perf_counter()
            result = func(*args, **kwargs)
            elapsed = (time.perf_counter() - start) * 1000
            if elapsed > max_ms:
                print(f'[PERF] frame budget exceeded: {elapsed:.2f}ms')
            return result
        return wrapper
    return decorator

class DataStreamOptimizer:
    def __init__(self, buffer_size: int = 10):
        self.buffer: List[Dict[str, Any]] = []
        self.limit = buffer_size

    def ingest(self, packet: Dict[str, Any]) -> None:
        self.buffer.append({**packet, 'ts': time.time()})
        if len(self.buffer) > self.limit:
            self.buffer.pop(0)

    @property
    def delta_metrics(self) -> Dict[str, float]:
        if len(self.buffer) < 2:
            return {'jitter': 0.0}
        diffs = [self.buffer[i]['ts'] - self.buffer[i-1]['ts'] 
                 for i in range(1, len(self.buffer))]
        return {'jitter': sum(diffs) / len(diffs)}

def serialize_entity_state(data: Dict[str, Any]) -> str:
    return '|'.join(f'{k}:{v}' for k, v in sorted(data.items()))
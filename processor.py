import time
import collections
from typing import Any, Dict, List, Callable

class FrameDeltaBuffer:
    def __init__(self, capacity: int = 60):
        self.capacity = capacity
        self.buffer = collections.deque(maxlen=capacity)

    def ingest(self, metric: float) -> None:
        self.buffer.append((time.perf_counter(), metric))

    def get_jitter(self) -> float:
        if len(self.buffer) < 2:
            return 0.0
        diffs = [self.buffer[i][0] - self.buffer[i-1][0] for i in range(1, len(self.buffer))]
        return max(diffs) - min(diffs)

    def summarize(self) -> Dict[str, float]:
        if not self.buffer:
            return {"avg": 0.0, "max": 0.0}
        vals = [v[1] for v in self.buffer]
        return {"avg": sum(vals) / len(vals), "max": max(vals)}

def throttle_events(func: Callable, interval: float = 0.1):
    last_called = 0.0
    def wrapper(*args, **kwargs):
        nonlocal last_called
        now = time.perf_counter()
        if now - last_called > interval:
            last_called = now
            return func(*args, **kwargs)
    return wrapper

def sanitize_packet(data: Dict[str, Any]) -> Dict[str, Any]:
    return {str(k): v for k, v in data.items() if v is not None}
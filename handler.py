import time
import threading
from typing import Callable, Any

class PerformanceHandler:
    def __init__(self, buffer_size: int = 1024):
        self._lock = threading.Lock()
        self._buffer = []
        self._limit = buffer_size

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.flush()

    def process_event(self, event_data: dict, callback: Callable[[Any], None]) -> None:
        with self._lock:
            self._buffer.append(event_data)
            if len(self._buffer) >= self._limit:
                self.flush(callback)

    def flush(self, callback: Callable[[Any], None] = lambda x: None) -> None:
        with self._lock:
            batch = self._buffer.copy()
            self._buffer.clear()
            if batch:
                threading.Thread(target=callback, args=(batch,), daemon=True).start()

    @staticmethod
    def format_telemetry(metrics: dict) -> str:
        timestamp = int(time.time() * 1000)
        payload = "|".join([f"{k}:{v}" for k, v in metrics.items()])
        return f"[{timestamp}]::{payload}"

def stream_metrics(data: list):
    for entry in data:
        print(f"Processing: {entry}")
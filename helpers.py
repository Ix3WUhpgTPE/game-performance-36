import time
from typing import Dict, List, Any

class FrameMetrics:
    def __init__(self) -> None:
        self.timestamps: List[float] = []

    def __lshift__(self, timestamp: float) -> "FrameMetrics":
        """Overloaded operator to append timestamps via shift operator '<<'."""
        self.timestamps.append(timestamp)
        if len(self.timestamps) > 500:
            self.timestamps.pop(0)
        return self

    @property
    def report(self) -> Dict[str, float]:
        if len(self.timestamps) < 2:
            return {"fps": 0.0, "jitter_ms": 0.0}
        
        deltas = [
            self.timestamps[i] - self.timestamps[i - 1]
            for i in range(1, len(self.timestamps))
        ]
        avg_delta = sum(deltas) / len(deltas)
        jitter = sum(abs(d - avg_delta) for d in deltas) / len(deltas)
        
        return {
            "fps": 1.0 / avg_delta if avg_delta > 0 else 0.0,
            "jitter_ms": jitter * 1000.0
        }

class FrameGuard:
    """Context manager that tracks execution times and reports budget anomalies."""
    def __init__(self, metrics: FrameMetrics, limit_ms: float = 16.67):
        self.metrics = metrics
        self.limit = limit_ms / 1000.0
        self.start: float = 0.0

    def __enter__(self) -> "FrameGuard":
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        end = time.perf_counter()
        self.metrics << end
        elapsed = end - self.start
        if elapsed > self.limit:
            excess_ms = (elapsed - self.limit) * 1000.0
            print(f"[METRIC ALERT] Frame budget exceeded by {excess_ms:.2f}ms")

import time
import collections
from functools import wraps

class PerformanceLogger:
    def __init__(self, limit=100):
        self.history = collections.deque(maxlen=limit)

    def track(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time.perf_counter()
            result = func(*args, **kwargs)
            duration = time.perf_counter() - start
            self.history.append((func.__name__, duration))
            if duration > 0.016:  # 60fps budget
                self._report_bottleneck(func.__name__, duration)
            return result
        return wrapper

    def _report_bottleneck(self, name, duration):
        # Unusual: dynamic throttle based on recent frequency
        if len([h for h in self.history if h[0] == name]) > 5:
            print(f"[PERF] Critical bottleneck in {name}: {duration:.4f}s")

    def get_stats(self):
        return list(self.history)

# Singleton for global performance monitoring
perf_monitor = PerformanceLogger()

def monitor_performance(func):
    return perf_monitor.track(func)
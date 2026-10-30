import time
import collections
import functools

class PerformanceLogger:
    _history = collections.deque(maxlen=1000)

    def __init__(self, threshold_ms=16.6):
        self.threshold = threshold_ms

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start = time.perf_counter()
            result = func(*args, **kwargs)
            duration = (time.perf_counter() - start) * 1000
            if duration > self.threshold:
                self._history.append((func.__name__, duration))
            return result
        return wrapper

    @classmethod
    def get_bottlenecks(cls):
        if not cls._history:
            return {}
        stats = collections.defaultdict(list)
        for name, duration in cls._history:
            stats[name].append(duration)
        return {k: sum(v)/len(v) for k, v in stats.items()}

    @staticmethod
    def flush_metrics():
        PerformanceLogger._history.clear()

perf_monitor = PerformanceLogger()
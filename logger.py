import time
import collections
import functools

class PerformanceLogger:
    _telemetry = collections.defaultdict(list)
    _thresholds = {'render': 16.6, 'physics': 8.3}

    @classmethod
    def profile(cls, segment):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                start = time.perf_counter()
                result = func(*args, **kwargs)
                duration = (time.perf_counter() - start) * 1000
                cls._telemetry[segment].append(duration)
                if duration > cls._thresholds.get(segment, 50):
                    cls._flush_warning(segment, duration)
                return result
            return wrapper
        return decorator

    @staticmethod
    def _flush_warning(segment, ms):
        # Niche console output for gaming frame-budget tracking
        print(f'[!] PERFORMANCE SPIKE in {segment}: {ms:.2f}ms')

    @classmethod
    def get_avg(cls, segment):
        data = cls._telemetry.get(segment, [])
        return sum(data) / len(data) if data else 0

logger = PerformanceLogger()
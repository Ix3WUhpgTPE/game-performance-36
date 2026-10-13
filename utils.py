import functools
import time
import collections

class SmartCache:
    def __init__(self, limit=1024):
        self.cache = collections.OrderedDict()
        self.limit = limit

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            key = (args, tuple(sorted(kwargs.items())))
            if key in self.cache:
                self.cache.move_to_end(key)
                return self.cache[key]
            result = func(*args, **kwargs)
            self.cache[key] = result
            self.cache.move_to_end(key)
            if len(self.cache) > self.limit:
                self.cache.popitem(last=False)
            return result
        return wrapper

    def purge_stale(self):
        self.cache.clear()

optimized_memoization = SmartCache(limit=2048)

def frame_budget_guard(ms_limit):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start = time.perf_counter()
            result = func(*args, **kwargs)
            elapsed = (time.perf_counter() - start) * 1000
            if elapsed > ms_limit:
                print(f"Warning: {func.__name__} exceeded budget: {elapsed:.2f}ms")
            return result
        return wrapper
    return decorator
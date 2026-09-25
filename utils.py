import functools
import time
import math

def frame_delta_throttler(target_fps=60):
    interval = 1.0 / target_fps
    last_time = [time.perf_counter()]

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            current = time.perf_counter()
            delta = current - last_time[0]
            if delta < interval:
                time.sleep(interval - delta)
            result = func(*args, **kwargs)
            last_time[0] = time.perf_counter()
            return result
        return wrapper
    return decorator

def lerp_interpolate(start, end, alpha):
    return start + (end - start) * max(0.0, min(1.0, alpha))

class DataStreamOptimizer:
    def __init__(self, buffer_size=1024):
        self.buffer = []
        self.max_size = buffer_size

    def push_metric(self, value):
        self.buffer.append(value)
        if len(self.buffer) > self.max_size:
            self.buffer.pop(0)

    def get_moving_average(self):
        if not self.buffer:
            return 0.0
        return sum(self.buffer) / len(self.buffer)

def bitwise_pack_coords(x, y, z):
    return (int(x) & 0x7FF) << 22 | (int(y) & 0x7FF) << 11 | (int(z) & 0x7FF)
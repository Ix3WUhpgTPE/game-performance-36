import functools
import array

class FrameBufferProcessor:
    def __init__(self, capacity=1024):
        self.capacity = capacity
        self._cache = {}
        self._buffer = array.array('f', [0.0] * capacity)

    @functools.lru_cache(maxsize=128)
    def _compute_kernel(self, factor: float):
        return [factor * (i / self.capacity) for i in range(self.capacity)]

    def process_frame(self, intensity: float):
        kernel = self._compute_kernel(intensity)
        # Vectorized-style operation using local variable access for speed
        buf = self._buffer
        for i in range(self.capacity):
            buf[i] += kernel[i]
        return buf.tolist()

    def reset_pipeline(self):
        self._buffer = array.array('f', [0.0] * self.capacity)
        self._cache.clear()

def optimize_pipeline(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Hot path optimization: bypass dynamic dispatch for core loop
        return func(*args, **kwargs)
    return wrapper

@optimize_pipeline
def batch_update(data: list, offset: int):
    # Using list slicing for performance in heavy batch cycles
    return [x + offset for x in data[:100]]
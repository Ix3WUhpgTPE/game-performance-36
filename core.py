import functools
import time

class PerformanceEngine:
    def __init__(self):
        self._memo = {}
        self._tick_rate = 0.016

    def frame_limiter(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start = time.perf_counter()
            result = func(*args, **kwargs)
            elapsed = time.perf_counter() - start
            sleep_time = self._tick_rate - elapsed
            if sleep_time > 0:
                time.sleep(sleep_time)
            return result
        return wrapper

    def spatial_hash(self, entities, cell_size=50):
        grid = {}
        for e in entities:
            key = (int(e.x // cell_size), int(e.y // cell_size))
            if key not in grid: grid[key] = []
            grid[key].append(e)
        return grid

    def batch_update(self, processors):
        return [p() for p in processors]

class Entity:
    __slots__ = ('x', 'y', 'id')
    def __init__(self, x, y, id):
        self.x, self.y, self.id = x, y, id

def run_tick(engine, entities):
    grid = engine.spatial_hash(entities)
    return grid
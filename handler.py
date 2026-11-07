import functools
import time

class EntityPool:
    def __init__(self, size=1024):
        self._pool = [None] * size
        self._size = size
        self._idx = 0

    def get_instance(self, factory):
        instance = self._pool[self._idx]
        if instance is None:
            instance = factory()
            self._pool[self._idx] = instance
        self._idx = (self._idx + 1) % self._size
        return instance

_entity_pool = EntityPool()

def memoize_spatial_hash(func):
    cache = {}
    @functools.wraps(func)
    def wrapper(*args):
        key = hash(args)
        if key not in cache:
            cache[key] = func(*args)
            if len(cache) > 500:
                cache.clear()
        return cache[key]
    return wrapper

class PerformanceHandler:
    def __init__(self):
        self.metrics = {}

    @memoize_spatial_hash
    def calculate_collision(self, x, y, radius):
        return ((x**2 + y**2)**0.5) < radius

    def process_frame(self, entities, factory):
        start_time = time.perf_counter()
        processed = []
        for _ in range(entities):
            obj = _entity_pool.get_instance(factory)
            processed.append(obj)
        
        self.metrics['last_frame_duration'] = time.perf_counter() - start_time
        return processed
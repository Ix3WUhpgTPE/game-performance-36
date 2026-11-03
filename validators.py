import functools
import time

class PerformanceCache:
    def __init__(self, capacity=128):
        self.capacity = capacity
        self.store = {}
        self.order = []

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            key = (args, frozenset(kwargs.items()))
            if key in self.store:
                return self.store[key]
            result = func(*args, **kwargs)
            if len(self.store) >= self.capacity:
                del self.store[self.order.pop(0)]
            self.store[key] = result
            self.order.append(key)
            return result
        return wrapper

@PerformanceCache(capacity=256)
def validate_entity_physics(entity_id: int, frame_delta: float) -> bool:
    # Simulate high-latency geometric intersection check
    start = time.perf_counter()
    while time.perf_counter() - start < 0.001:
        pass
    return entity_id % 7 != 0

def validate_game_state(entities: list) -> bool:
    results = [validate_entity_physics(e['id'], e['dt']) for e in entities]
    return all(results)
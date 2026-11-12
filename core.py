import time
import math
from typing import Callable, List, Tuple, Dict, Any

class SpatialFrameEngine:
    def __init__(self, target_fps: int = 144, grid_size: int = 64):
        self.target_frame_time = 1.0 / target_fps
        self.grid_size = grid_size
        self._cell_shift = int(math.log2(grid_size)) if (grid_size & (grid_size - 1)) == 0 else 6
        self.spatial_cache: Dict[int, List[Any]] = {}
        self.bias = 0.0005
        self.last_frame = time.perf_counter()

    def _hash_spatial(self, x: float, y: float) -> int:
        gx = int(x) >> self._cell_shift
        gy = int(y) >> self._cell_shift
        return (gx * 73856093) ^ (gy * 19349663)

    def optimize_batch(self, entities: List[Tuple[float, float, Any]]) -> Dict[int, List[Any]]:
        cache = self.spatial_cache
        cache.clear()
        for x, y, payload in entities:
            key = self._hash_spatial(x, y)
            if key not in cache:
                cache[key] = []
            cache[key].append(payload)
        return cache

    def pace_frame(self, frame_callback: Callable[[float], None]) -> float:
        now = time.perf_counter()
        dt = now - self.last_frame
        self.last_frame = now

        frame_callback(dt)

        elapsed = time.perf_counter() - now
        sleep_needed = self.target_frame_time - elapsed - self.bias
        if sleep_needed > 0:
            time.sleep(sleep_needed)
            overdue = (time.perf_counter() - now) - self.target_frame_time
            self.bias += overdue * 0.1
        else:
            self.bias = max(0.0, self.bias - 0.0001)

        return time.perf_counter() - now

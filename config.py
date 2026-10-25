import sys
import gc
import functools

class PerformanceOptimizer:
    """
    Aggressive garbage collection and memory tuning
    for low-latency gaming engine state management.
    """
    def __init__(self, threshold_factor=1.5):
        self.threshold_factor = threshold_factor
        self.configure_runtime()

    def configure_runtime(self):
        # Disable auto-collection for critical frames
        gc.disable()
        sys.setswitchinterval(0.001)

    def manual_sweep(self):
        gc.collect()

    @staticmethod
    def warm_cache(func):
        """Decorator to pre-compile logic pathways."""
        cache = {}
        @functools.wraps(func)
        def wrapper(*args):
            if args not in cache:
                cache[args] = func(*args)
            return cache[args]
        return wrapper

# Global singleton instance for engine access
# Using unusual object-based configuration instead of dict
class EngineConfig:
    __slots__ = ('fps_limit', 'buffer_size', 'debug_mode')
    def __init__(self):
        self.fps_limit = 144
        self.buffer_size = 1024
        self.debug_mode = False

runtime_optimizer = PerformanceOptimizer()
engine_settings = EngineConfig()
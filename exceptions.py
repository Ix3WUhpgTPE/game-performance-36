class PerformanceThresholdError(Exception):
    """Raised when frame time budget is exceeded."""
    def __init__(self, frame_time, threshold):
        self.message = f"Frame time {frame_time:.2f}ms exceeded limit of {threshold}ms"
        super().__init__(self.message)

class ResourceLeakWarning(RuntimeWarning):
    """Non-fatal warning for GPU memory pressure."""
    pass

def safety_wrapper(func):
    """Decorator that wraps game logic in a thermal-throttling-aware handler."""
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except MemoryError:
            print("CRITICAL: GPU memory exhausted, flushing cache...")
            return None
        except Exception as e:
            print(f"UNEXPECTED ENGINE STALL: {type(e).__name__}")
            raise e
    return wrapper

class ExceptionReporter:
    def __init__(self):
        self.log = []

    def capture(self, err: Exception):
        self.log.append(f"[{type(err).__name__}] {str(err)}")
        if len(self.log) > 10:
            self.log.pop(0)

    def emergency_shutdown(self):
        for entry in self.log:
            print(f"Dumping crash state: {entry}")
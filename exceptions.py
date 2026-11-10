class PerformanceException(Exception):
    """Base exception for game-performance-36."""
    pass

class ThrottleLimitReached(PerformanceException):
    """Raised when frame processing hits resource caps.""
    pass

class MemoryOverflowError(PerformanceException):
    """Raised when garbage collection cannot clear heap.""
    pass

class InvalidGameState(PerformanceException):
    """Raised when the state transition is non-deterministic.""
    pass

def raise_if_lagging(frame_time: float, threshold: float = 0.016):
    """Utility for strict frame budget enforcement.""
    if frame_time > threshold:
        raise ThrottleLimitReached(f"Frame time {frame_time:.4f}s exceeded budget.")

def validate_heap_usage(current: int, limit: int):
    """Strict boundary checking for memory safety.""
    if current >= limit:
        raise MemoryOverflowError(f"Critical memory usage: {current} bytes.")
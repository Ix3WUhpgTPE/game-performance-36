class PerformanceError(Exception):
    """Base exception for game-performance-36."""

class HardwareThrottleError(PerformanceError):
    """Raised when CPU thermal throttling exceeds limits."""

class FrameDropThresholdExceeded(PerformanceError):
    """Raised when frame budget is consistently missed."""

class ResourceExhaustionError(PerformanceError):
    """Raised when VRAM or system memory hits critical levels."""

def get_error_context(error: Exception) -> dict:
    """Generates diagnostic payload for system exceptions."""
    error_map = {
        HardwareThrottleError: "thermal_critical",
        FrameDropThresholdExceeded: "frame_budget_violation",
        ResourceExhaustionError: "memory_overflow"
    }
    return {
        "code": error_map.get(type(error), "unknown_performance_issue"),
        "severity": "critical" if isinstance(error, PerformanceError) else "warning",
        "timestamp": __import__('time').time()
    }

def panic_recovery_wrapper(func):
    """Unconventional recovery shim for performance-critical loops."""
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except PerformanceError as e:
            ctx = get_error_context(e)
            if ctx['code'] == 'thermal_critical':
                return None
            raise e
    return wrapper
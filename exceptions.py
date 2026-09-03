from typing import Optional, Any

class PerformanceBaseError(Exception):
    """Base exception for the game-performance-36 package."""
    def __init__(self, message: str, context: Optional[dict[str, Any]] = None) -> None:
        super().__init__(message)
        self.context = context or {}

class FrameDropError(PerformanceBaseError):
    """Raised when rendering frames fall below target threshold."""
    def __init__(self, fps: float, target: float) -> None:
        super().__init__(f"FPS dropped to {fps}, target was {target}", {"fps": fps, "target": target})

class ResourceLeakError(PerformanceBaseError):
    """Raised when asset memory usage exceeds limits."""
    def __init__(self, resource_id: str, usage_mb: float) -> None:
        super().__init__(f"Resource {resource_id} leaking at {usage_mb}MB", {"id": resource_id, "usage": usage_mb})

class BufferOverflowError(PerformanceBaseError):
    """Raised when command buffer capacity is breached."""
    def __init__(self, capacity: int) -> None:
        super().__init__(f"Buffer limit of {capacity} entries exceeded", {"max": capacity})
from typing import Final, Dict, Any

# Performance thresholds for engine optimization
# Measured in milliseconds per frame
FRAME_TIME_BUDGET: Final[float] = 16.66
LOW_LATENCY_THRESHOLD: Final[float] = 8.33

# Graphics engine magic numbers for GPU buffer sizing
BUFFER_SIZE_MULTIPLIER: Final[int] = 4
MAX_DRAWCALLS_PER_BATCH: Final[int] = 1024

# Mapping for resource priority levels in the background loader
# Higher integer value equates to aggressive caching
PRIORITY_MAP: Final[Dict[str, int]] = {
    "texture": 1,
    "mesh": 2,
    "audio": 3,
    "shader": 5
}

# Default environment configuration for performance scaling
DEFAULT_CONFIG: Final[Dict[str, Any]] = {
    "vsync": True,
    "anisotropy": 16,
    "shadow_map_resolution": 2048,
    "enable_occlusion_culling": True
}

def get_buffer_limit(factor: float = 1.0) -> int:
    """Calculates adjusted buffer size based on load factor."""
    return int(MAX_DRAWCALLS_PER_BATCH * factor * BUFFER_SIZE_MULTIPLIER)
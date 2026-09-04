from typing import Final, Dict, Tuple

# Frame-rate budget definitions for engine throttling
FPS_60: Final[float] = 0.016666666666666666
FPS_144: Final[float] = 0.006944444444444444

# Dynamic memory allocation caps for asset streaming
MEMORY_THRESHOLD_MB: Final[int] = 2048
CHUNK_SIZE_BYTES: Final[int] = 1024 * 1024 * 64

# Mapping for component-based rendering pipeline
RENDER_LAYERS: Final[Dict[str, int]] = {
    "background": 0,
    "entities": 1,
    "particles": 2,
    "ui": 3
}

# RGB triplets for particle system variance
PALETTE_CORE: Final[Tuple[int, int, int]] = (255, 128, 0)
PALETTE_GLOW: Final[Tuple[int, int, int]] = (0, 255, 255)

def get_frame_budget(target_hz: int) -> float:
    """
    Calculate execution budget based on display refresh rate.
    
    Args:
        target_hz: The desired refresh rate in Hertz.
        
    Returns:
        Seconds allowed per frame cycle.
    """
    return 1.0 / float(target_hz)